# Evidence-Tagged Multi-Model Review

AISØN uses multiple models to review claims, proposals, and decisions.

Model agreement is useful, but agreement is not evidence.

> Evidence should keep its provenance even when models agree.

Each claim should keep an explicit evidence status.

## Evidence statuses

### `LIT` — Literature-supported

Use when a claim is supported by a real, relevant, human-verifiable source.

A model cannot promote a claim to `LIT` merely because other models agree with it.

### `ENG` — Engineering inference

Use when a claim follows from engineering reasoning, constraints, or known system behavior, but is not directly established by a cited source.

`ENG` is reasoning, not measurement.

### `HYP` — Hypothesis

Use when a claim is testable but not yet sufficiently supported.

A useful hypothesis should be capable of being proven wrong.

### `UNK` — Unknown

Use when there is not enough evidence to classify a claim confidently.

`UNK` is not failure. It preserves the boundary of what is currently known.

## Core rule

**AI consensus does not upgrade evidence.**

If three models agree that a claim is `HYP`, the claim remains `HYP`.

Agreement may make a question worth investigating. It does not change the source of evidence.

## Human adjudication

Models may:

- propose evidence statuses
- challenge classifications
- request sources
- identify contradictions
- suggest experiments
- preserve dissent

The human reviewer remains the final authority for accepting, revising, rejecting, or reclassifying claims.

## Disagreement preservation

Disagreement should survive synthesis when it materially affects the decision.

Preserving disagreement does not mean publishing everything.

Retention must still respect:

- privacy
- security
- publication status
- repository scope
- retention rules

## `what_was_lost`

When synthesis removes uncertainty, dissent, or unresolved alternatives, the decision record should state what disappeared.

Examples include:

- `DISSENT:RED_TEAM`
- `UNKNOWN:ANALYST`
- `PROVENANCE_GAP:SYNTHESIZER`

If a decision remains unresolved, `what_was_lost` should not be empty.

## Evidence changes

Evidence status should change only when the reason is explicit.

Examples:

- `HYP -> LIT`: a human-verified source was added
- `UNK -> ENG`: an engineering constraint was clarified
- `ENG -> HYP`: the inference depended on an unsupported assumption

Status changes should be auditable.

## Minimal review pattern

1. State the claim.
2. Attach an evidence status.
3. Ask multiple models to review independently.
4. Preserve disagreements.
5. Check for unsupported facts.
6. Human adjudicates.
7. Record what changed and what was lost.

## Non-goals

This framework does not assume that:

- more models produce more truth
- consensus proves correctness
- literature is automatically correct
- every disagreement must be public
- every review requires a large council

The goal is narrower:

**Make the reasoning state visible enough that agreement does not erase uncertainty.**
