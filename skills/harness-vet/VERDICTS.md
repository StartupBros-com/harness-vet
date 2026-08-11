# Verdicts

## Vocabulary (per component)

- **ADOPT** — install as-is: net-new capability that survived phase-4
  verification and beats its phase-5 price.
- **ADAPT** — the capability is real, the packaging fails a price check:
  install behind an overlay, patch, or fork that removes the objectionable
  part (a dependency, an always-on surface, a self-updater). Name the
  adaptation in the verdict; an unnamed adaptation is an ADOPT wearing a
  disguise.
- **EXTRACT** — the idea clears the bar, the artifact doesn't: port the
  pattern into the harness's own idiom and leave the candidate's code out.
  When the ported material shapes future agent behavior (prompts, doctrine,
  rules), absence from the incumbent is not evidence of value — run it
  against one live task before landing, or land it carrying an explicit
  unverified-value marker naming the measurement that settles it; the
  marker stands until that measurement runs.
- **SKIP** — nothing wrong, nothing needed: duplicates capability the digest
  already lists, or fails the price test. Duplication is SKIP even when the
  candidate is well-made.
- **REJECT** — affirmatively disqualified: refuted claims, security red
  flags, license conflict, dead maintenance. State a confidence and point at
  the disqualifying evidence.

**Wholesale rollup**: one line with counts — "ADOPT 1 / EXTRACT 3 / SKIP 9 of
13" — plus a separate verdict on the delivery mechanism (plugin, installer,
MCP server) from the content it delivers.

## Re-eval triggers

Every SKIP and REJECT ends with `Do-not-retry unless:` followed by observable
predicates — events a future session can check: "upstream ships CI and commits
the benchmark artifacts", "the plugin system gains per-skill disable", "three
months of stable tagged releases". Bare time ("revisit later", "in a few
months") is not a predicate. A fired trigger is the only thing that reopens a
settled verdict; pressure, enthusiasm, or a second ask is not.

## The eval note

One durable note per vet, in whatever memory the harness keeps — or as a
plain committed file in a stated location when the digest found no memory
system:

0. Frontmatter, if the memory system uses it: name, a verdict-dense one-line
   description, and a pointer back to the vet run (session id, transcript
   path, or PR) so the note traces to its evidence.
1. First line of the body: the wholesale verdict, followed by a one-line
   record of run decisions (sweep scope, landing depth — chosen or
   defaulted).
2. `Measured, not inferred:` — the commands run and numbers reproduced that
   carried the verdict.
3. Per-component table: component / verdict / one-line evidence.
4. For anything adopted, adapted, or extracted: why, and how to apply it.
5. Audit dividend: what this vet exposed about the harness itself.
6. `Do-not-retry unless:` block.
7. Corrections append with dates; earlier text stays visible and flagged, so
   the note's history stays trustworthy.

## Closing checklist

The vet is done when every line passes:

- [ ] Adopted / adapted / extracted changes landed as reviewable artifacts,
      each verified by running it, not by reading its diff.
- [ ] Landed changes passed the review tier the harness's conventions assign
      to their risk level; extractions touching harness files ran their
      adversarial review, and behavior-shaping ports carry a live-task result
      or their named deciding measurement — or the eval note names why none
      was needed.
- [ ] Deferred ambitions filed as tracked issues, not built mid-vet.
- [ ] Security-posture proposals handed to the operator with evidence,
      explicitly awaiting sign-off — none silently applied.
- [ ] The eval note exists and carries its triggers — indexed where the
      harness indexes memory, or committed as a plain file where no memory
      system exists.
- [ ] Every citation of shipped state was read from the merged artifact — a
      draft PR's numbers are claims, not evidence.
