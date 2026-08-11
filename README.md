# harness-vet

**The adoption gate for your agent harness.** Someone says a skill, plugin, MCP server, rules file, repo, or paper belongs in your setup. Before you install it, `/harness-vet <candidate>` runs the deep-dive most people skip — and its default verdict is **SKIP**, because the evidence says your harness is degraded by additions more often than it is improved by them.

## Why the default is SKIP

Not vibes — receipts (sources and tiers in [`skills/harness-vet/EVIDENCE.md`](skills/harness-vet/EVIDENCE.md)):

- LLM-generated context files **reduced** agent task success 0.5-2% while raising cost 20-23%; human-curated ones helped only marginally (ETH Zurich, arXiv 2602.11988).
- Anthropic removed over 80% of Claude Code's system prompt with no measurable eval loss.
- Large toolsets showed performance losses up to 85%; narrowing the presented tool set tripled selection accuracy in one study.
- A scan of 3,984 public Claude Code skills found 13.4% with critical issues and 76 confirmed malicious.
- Across the ~15 real adoption evaluations this skill was mined from, **no multi-component candidate was ever adopted wholesale**; the modal outcome was extracting a handful of patterns.

## What a vet does

Seven phases, each with a checkable completion bound:

1. **Intake** — normalize the candidate into scratch; check whether it's already half-installed (2 of 15 real candidates were); check for a prior verdict; treat candidate content as data, never instructions. Paywalled/registry-only candidates get a metadata-first path.
2. **Digest** — one frozen block of facts about *your* harness, discovered at runtime, pasted into every subagent prompt. Verdicts are made against your real setup, not a generic one.
3. **Read** — capped fan-out of category readers, schema-forced per-component findings.
4. **Verify** — refute-by-default: run the candidate's own tests, probe its guards both directions, fact-check its docs claims against official docs, reproduce every number before citing it. Web listings settle nothing; only running things does.
5. **Price** — quantified context cost, the armor test, the off-switch check (plugin-bundled skills are commonly all-or-nothing), delivery verdicted separately from content, supply-chain review that reads bundled code, not just descriptions.
6. **Verdict** — per-component **ADOPT / ADAPT / EXTRACT / SKIP / REJECT** plus a wholesale rollup; every SKIP and REJECT carries `Do-not-retry unless:` observable predicates, never "later". Closes with the **audit dividend**: what vetting the candidate exposed about your own harness.
7. **Ship** — through your harness's own conventions; security-posture changes are proposed, never auto-applied; one durable eval note with re-eval triggers.

Degrades gracefully: works with a workflow tool, a task/agent tool, or fully inline; with or without a memory system.

## Field results (the two runs that gated this release)

- **Two prompt-skills from a social thread**: the A/B sandbox refuted the "models already do this" assumption for one of them — its scaffold measurably beat the bare model — while the arithmetic audit found its own worked examples off by 10× and the delivery unlicensed. Verdict: EXTRACT the proven pattern, skip the artifact. The extraction shipped as a new clean-room skill the same day.
- **A ~64KB paid registry skill**: a 3-arm planted-defect audit (bare / candidate / incumbent doctrine) showed the candidate's detection **identical** to the ~170-line doctrine the harness already carried — and found one blind spot *shared* by both, which became a one-line doctrine fix. The audit dividend also surfaced a silently-failing nightly auth job. The verdict was SKIP; the vet still paid for itself twice.

- **A frontier-lab engineering post**: all seven verifiable claims CONFIRMED against official docs and the benchmark's own repo — and the verdict was still EXTRACT 1 / SKIP 3, because true ≠ needed. The dividend: testing the article's described failure mode against the host harness found its model-routing proxy silently discarding reasoning on every turn — a file:line-documented bug, now tracked upstream.

The pattern across all three: even when the answer is "don't install it" — and it usually is — a real vet returns value. In 3 of 3 runs, the audit dividend (what vetting the candidate exposed about the *host* harness) was the chief finding, which is why the skill treats it as a required output, not a bonus.

## Install

From the [House of Vibe marketplace](https://github.com/StartupBros-com/hov-marketplace):

```
/plugin marketplace add StartupBros-com/hov-marketplace
/plugin install harness-vet@hov
```

Then: `/harness-vet <repo-url | local-path | post-or-paper-link>`

The skill is user-invoked only (`disable-model-invocation: true`) — a tool whose thesis is "don't clutter your harness" costs you zero always-on context. In an interactive session it asks at exactly two decision points (sweep scope on large list-candidates, landing depth at ship); unattended runs take named defaults and record them in the eval note, so background invocations never stall on a question.

## What this is not

- Not a claim of better verdicts than your own careful deep-dive — no paired comparison has run. It encodes a mined, field-tested methodology so the deep-dive actually happens instead of being skipped.
- Not a scanner: it reads, runs, and prices with judgment; supply-chain review is a phase, not a signature database.

MIT. Mined from ~15 real adoption evaluations (2026-07/08) on the authoring harness; the `[measured]` tags in the skill refer to those runs.
