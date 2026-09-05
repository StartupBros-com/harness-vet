# Evidence dossier

The receipts behind the default-SKIP prior and the supply-chain bar. Each
claim carries its source and a status flag: **[peer-track]** (academic work,
may still be preprint), **[vendor]** (company research or blog),
**[measured-here]** (observed on the harness this skill was mined from,
2026-07 through 2026-09), **[directional]** (source too weak to carry a
number — use the direction, drop the digits). SKILL.md's inline shorthand maps here as:
[research] = [peer-track] or [vendor]; [measured] = [measured-here]. The
dossier flag is the authoritative tier.

Meta-rule, itself part of the method: a percentage from an unreviewed preprint
or a vendor PDF is directional until replicated. What carries weight is
convergence across independent sources — and on "less context, fewer tools,
vetted sources" the convergence below is unusually strong.

## Why the default verdict is SKIP

- LLM-generated context files (AGENTS.md-style) *reduced* agent task success
  by 0.5-2% while raising cost 20-23%; human-curated ones helped only
  marginally (~+4%, and not for every agent tested). Authors' conclusion:
  context files should state minimal requirements only. Gloaguen et al., ETH
  Zurich SRI Lab, arXiv 2602.11988. [peer-track]
- Anthropic removed over 80% of Claude Code's system prompt for newer models
  with no measurable eval loss (blog, 2026-07-24); an independent replication
  on a small model reported score parity with 32% fewer input tokens
  (Antigma, 2026-07-25). [vendor]
- Pruning agent context to recent tool calls plus light summarization beat
  full-context retention 91.6% vs 71.0% task completion at ~64% fewer tokens
  on a 50-task agentic benchmark — stale context misleads, it is not neutral
  overhead. arXiv 2606.10209. [peer-track]
- Clutter can silently not work at all: a legacy rules format scored 0/9 rule
  compliance in one migration test where the current format scored 9/9 — the
  cost was paid, the behavior never fired. [directional]
- Base rate: across ~15 vets of popular, well-regarded candidates on the
  authoring harness, no multi-component candidate was adopted wholesale as
  delivered; single scoped components occasionally earned ADOPT, the modal
  outcome was EXTRACT of a handful of patterns, and two vets' chief value
  was the drift they exposed in the host harness. [measured-here]
- The starkest duplication receipt: a ~64KB, 7-file commercial skill's
  detection verdicts came back identical, item for item, to the authoring
  harness's existing ~170-line doctrine on a 7-item planted audit — same
  hits, same miss, zero false positives, both arms (2026-08-10).
  [measured-here]
- The audit dividend generalizes: in 3 of 3 dogfood runs, testing the
  candidate's described failure mode against the host harness produced the
  run's chief finding — a doctrine blind spot, a silently-failing nightly
  auth job, and a routing proxy structurally discarding model reasoning
  (2026-08). [measured-here]

## Tool count is a priced quantity

- Narrowing the tool set presented to the model raised tool-selection
  accuracy from 13.6% to 43.1% in the RAG-MCP study. [peer-track]
- Microsoft Research, citing OpenAI's own guidance: keep tool count under
  roughly 20; large toolsets showed performance losses up to 85%, and
  oversized tool *responses* (one tool emitted 557,766 tokens) degraded
  performance up to 91%. [vendor]
- The threshold moves with model generation — one production telemetry set
  showed a small model dropping below 90% accuracy at 10-15 tools while a
  larger one held to 20-30. Encode the *test* (measure selection accuracy at
  your tool count), never a fixed N. [directional]

## Supply chain

- Snyk scanned 3,984 public Claude Code skills: 13.4% carried critical
  issues, 36.8% carried some issue, 76 were confirmed malicious. [vendor]
- OX Security submitted a benign proof-of-concept package to 11 public MCP
  registries; 9 accepted it with zero security review. Named CVEs exist for
  protocol-level STDIO command injection (CVE-2026-30623, CVE-2026-30615).
  [vendor]
- Combined attacks — a prompt-injected description *plus* malicious bundled
  code — achieved 66.7-100% success where single-vector attacks scored far
  lower; reviewing only descriptions misses the highest-yield shape. Read
  the code. arXiv 2604.01905. [peer-track]
- Trust is transitive: approving a plugin approves every component author
  beneath it — its skills, hooks, binaries, and their update channels
  ("trust pyramid", Pluto Security). A component that rewrites its own
  instructions on a schedule extends that trust to every future version
  sight unseen [measured-here: one vetted skill pack ran a daily
  self-updater over its own instruction files]. [vendor]
- Anthropic's official posture puts vetting on the operator: install skills
  only from trusted sources and audit the skill file plus bundled scripts —
  no platform sandboxing guarantee is claimed. [vendor]
- A release pipeline can suppress its own integrity signals: one desktop
  candidate set a null signing identity, disabled notarization, had CI *fail
  the build if signed*, and self-updated silently on a 6h timer behind a
  SHA-256 produced by that same pipeline. Deliberate suppression is the
  signal — an unfunded project that merely lacks a certificate is not
  [measured-here: local-mcp / chat-on-steroids vet, 2026-09].
- Terms are the operator's call, and their own uptime is the evidence: the
  same vet flagged a candidate's chatgpt.com automation as disqualifying on
  OpenAI's terms while this harness's own terminal review gate drove the
  same site the same way — 309 runs in 7 days, months of operation, one
  anti-scraping trip ever (2026-07-03, under 3 parallel runs), no account
  action. The vet had read phase 1's warning that same session and applied
  the clause anyway. Where a verdict *does* rest on terms, its re-eval
  trigger is a documented API, since commits cannot change what the terms
  permit [measured-here: local-mcp / chat-on-steroids vet, 2026-09].
- A sandbox is not all-or-nothing: that vet's candidate engaged Landlock and
  blocked network egress correctly, yet two live probes escaped it because
  the writable allow-list was derived from caller-supplied arguments (the
  write target's parent directory; the caller's `cwd`). Working confinement
  plus a caller-defined boundary is the shape to probe for — and it is a
  reason not to run the artifact, not a reason to skip reading it
  [measured-here: same vet].

## Method gates (mined from failed shortcuts)

- **Model confound**: before trusting any before/after transcript delta,
  control for model mix — one naive -1.35pp effect dissolved to -0.36pp
  (n.s.) once model drift was controlled. [measured-here]
- **Instrument validity**: verify the detector before believing a zero — one
  audit's grep tool silently skipped hidden directories; never trust a
  detector whose matches you have not read. [measured-here]
- **Numbers decay**: a merged PR's stated verification numbers failed to
  reproduce from its own squashed code weeks later; re-run before citing.
  [measured-here]
- **Fabricated documentation exists in the wild**: a popular skill pack's
  feature docs described platform commands that do not exist — 5 of 5
  checked claims were confabulated. Official docs are the reference, the
  candidate's prose is the claim. [measured-here]
- **Vibes dressed as data**: sources whose headline numbers came from
  self-validation or vendor-hosted, unreviewed PDFs get flagged and their
  digits excluded from verdicts — the flag itself goes in the eval note so
  the exclusion is auditable. [measured-here]


## Scope-aware adoption: primary sources checked 2026-09-05

These sources guide the v0.2 design; they are not measurements of this skill.
Historical numbers above belong to their original studies and harness runs,
not a guaranteed effect or a universal skill-count budget.

- **Platform scope is source-specific.** The [Claude Code skills reference](https://code.claude.com/docs/en/skills) distinguishes personal, project,
  managed, plugin and nested sources, along with precedence, activation and
  hosted-session differences. A plugin namespace prevents some name conflicts,
  not semantic duplication. Check the current host rather than freezing this
  inventory as a portable law. [vendor]
- **Progressive disclosure, not universal installation.** Anthropic's
  [Agent Skills engineering guide](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  separates discovery metadata, the invoked body, references and executable
  resources, and warns to inspect trusted provenance and bundled behavior.
  Price these layers separately at the scope where they load. [vendor]
- **Measure useful skills as well as clutter.** [SkillsBench](https://arxiv.org/abs/2602.12670) compares curated skills with matched
  no-skill runs and deterministic task verifiers. Its current abstract reports
  benefits that vary by model/harness and skill composition. This supports
  target-task paired evaluation, not a blanket claim that skills hurt or help.
  Results are study-specific; do not import their gains into this harness.
  [peer-track]
- **Composition is not availability.** [AgentSkillOS](https://arxiv.org/abs/2603.02176) reports structured composition outperforming
  flat invocation with the same skill set, using model-judged artifact quality.
  Its benchmark is not proof that every small project needs an orchestrator.
  [peer-track]
- **Instructions are operational supply-chain content.** [Agent Skill registry
  attacks](https://arxiv.org/abs/2605.11418) studies metadata/instruction attacks
  on discovery, selection and admission. Review whole instruction files and
  execution surfaces; registry badges and benign descriptions are not enough.
  Project-local loading does not make malicious instructions safe. [peer-track]
- **Keep the mechanism small.** Anthropic's [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) recommends
  the simplest system that works and adding complexity only when needed.
  [Seeing like an agent](https://claude.com/blog/seeing-like-an-agent) describes
  revisiting tool assumptions as models change. Recheck changed premises and
  prefer native scoping/evaluation tools over another permanent service.
  [vendor]

The target/task applicability and cross-location note rules are this skill's
engineering design, not a claimed vendor standard. The v0.2 regression cases
exercise decision behavior; they do not prove SEO or estate-planning quality,
actual runtime containment, or a general improvement across all harnesses.
