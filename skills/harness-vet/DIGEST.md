# The harness digest

One frozen text block describing the harness the candidate must beat, pasted
verbatim into every subagent prompt of the run. It prevents two measured
failures: parallel agents each re-discovering harness state (slow, and they
disagree), and verdicts made against an imagined generic harness instead of
the real one.

## Discovery sweep

Inventory what actually exists — skip what doesn't. Typical locations, by
harness:

- **Instruction files**: user- and project-level agent instructions
  (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, equivalent) with rough sizes —
  these are the always-on budget the candidate competes for.
- **Skills**: user skills directory, project skills, plugin-bundled skills,
  and any skill-manager lock or state files (the install-state lookup in
  phase 1 reuses this).
- **MCP servers**: global and project config, with per-server tool counts —
  tool count is a priced quantity, not trivia (EVIDENCE.md).
- **Guards and permissions**: hooks, allow/ask/deny rules, sandboxing, and
  what they actually block — a candidate guard gets diffed against these in
  phase 4.
- **Capability the harness already has on demand**: user-invoked skills,
  CLIs, subagent types, review tooling. Overlap verdicts are made against
  this list.
- **Memory and prior verdicts**: where durable notes live, plus the names and
  one-line outcomes of prior vets that touch the candidate's space.
- **Operator conventions**: tracking units (issues/PRs), review ladder,
  commit style, worktree discipline — phase 7 ships through these.

## Template

```
Context (established facts, do not re-derive):
- Environment: <OS, agent CLI(s) + versions, package managers>
- Always-on context: <instruction files + sizes; auto-firing skills/plugins;
  MCP servers + tool counts>
- On-demand capability: <user-invoked skills, CLIs, subagent types,
  review tooling>
- Guards & permissions: <hooks, deny/ask rules, sandboxing>
- Conventions: <tracking units, review ladder, memory system>
- Prior verdicts near this candidate: <note names + one-line outcomes>
- Base rate: <N prior vets on this harness, M adoptions among them — or,
  where no local vet history exists: "no local history; imported prior from
  the harness this skill was mined from: wholesale adoption is rare" —
  labeled as imported, never stated as local fact>
- Standing rule: duplicating a capability already listed above is SKIP even
  when the candidate is well-made.

Your task: <reader or verifier brief>. Report against THIS harness, not a
generic one. Evidence means file:line or the output of a command you ran.
Platform or model facts newer than your training data get checked against
live documentation — never read newer-than-you as fabricated.
```

## Freshness

Rebuild the inventory sections each run — the sweep is cheap and the state
drifts, including names: one run's digest pointed at a skill's old deploy
name and handed every reader a dead path until one caught it [measured].
Carry forward only the conventions prose. If a conversation-history
index or memory search backs the prior-verdict lookup, check the index's
freshness before trusting an absent result: a stale index reads as "never
evaluated" [measured: a 4-day-stale index hid the newest eval on the
authoring harness].
