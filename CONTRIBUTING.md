# Contributing

AISØN is an experimental framework for decisions that preserve disagreement, uncertainty, provenance, and human authority.

Contributions should keep those properties visible rather than optimizing only for a clean final answer.

## Core principles

Contributions should preserve these invariants:

- human final authority
- missing is not consent
- unknown is not accept
- dissent survives synthesis
- unresolved decisions should record `what_was_lost`
- provenance should remain visible
- capability does not imply authority

## Evidence-tagged review

Claims may use the following evidence statuses:

- `LIT` — literature-supported
- `ENG` — engineering inference
- `HYP` — hypothesis
- `UNK` — unknown

AI consensus does not upgrade evidence.

A claim should change evidence status only when the reason is explicit and auditable.

See [`docs/evidence-tagged-review.md`](docs/evidence-tagged-review.md).

## Review workflow

A contribution should make clear:

1. what claim or change is being proposed
2. what evidence supports it
3. what remains uncertain
4. whether meaningful dissent exists
5. what a human reviewer must decide

Models may assist with review, but model agreement does not replace human adjudication.

## Disagreement preservation

Important disagreement should not disappear merely because a final answer was produced.

Where relevant, preserve:

- dissent
- unknowns
- provenance gaps
- unresolved alternatives
- what was removed during synthesis

Preserving disagreement does not mean publishing everything.

Retention must still respect:

- privacy
- security
- publication status
- repository scope
- retention rules

## Pull requests

Keep pull requests narrow.

A pull request should explain:

- what changed
- why it changed
- how it was checked
- what remains unresolved

Avoid combining unrelated framework changes into one pull request.

## Tests

Behavioral invariants should be tested when practical.

Examples include:

- dissent survives synthesis
- missing input does not become consent
- unknown does not become accept
- unresolved decisions preserve `what_was_lost`

## Repository discipline

Do not create new abstractions, protocols, or files unless they solve a specific problem.

Prefer the smallest change that makes the system more explicit, testable, or auditable.

A polished result should not hide uncertainty that still matters.
