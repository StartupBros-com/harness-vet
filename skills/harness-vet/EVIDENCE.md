# Evidence dossier

The receipts behind the default-SKIP prior and the supply-chain bar. Each
claim carries its source and a status flag: **[peer-track]** (academic work,
may still be preprint), **[vendor]** (company research or blog),
**[measured-here]** (observed on the harness this skill was mined from,
2026-07/08), **[directional]** (source too weak to carry a number — use the
direction, drop the digits). SKILL.md's inline shorthand maps here as:
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
