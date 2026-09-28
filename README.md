# AISØN

[![Tests](https://github.com/AelisonX/aison/actions/workflows/tests.yml/badge.svg)](https://github.com/AelisonX/aison/actions/workflows/tests.yml)

**A small framework for decisions that remember disagreement.**

Most multi-agent systems optimize for an answer.

AISØN asks a different question:

> What was lost while producing it?

AISØN is an experimental framework for preserving:

- provenance
- dissent
- uncertainty
- packet integrity
- reversible decisions
- human final authority

## Evidence-tagged review

AISØN can preserve the evidence status behind model-reviewed claims.

> Evidence should keep its provenance even when models agree.

See [`docs/evidence-tagged-review.md`](docs/evidence-tagged-review.md) for the current review pattern.

## Recovery Companion

Automation can become faster than human attention.

AISØN is exploring whether automated workflows can remain convenient while keeping human recovery visible and reachable.

Current design questions include:

- Can the human see what the automation did?
- Can the human learn the manual path on demand?
- Can the human take over from a checkpoint?
- Can the human restart from an earlier safe point?
- Can persistent delegation preserve a usable recovery path?

> Automation should never make the manual path invisible.

See [`docs/recovery-companion.md`](docs/recovery-companion.md) for the current experimental concept.

## Core principle

**Missing is not consent.**

A missing response must not be silently converted into agreement.

If an expected agent response is missing, truncated, or incomplete, AISØN should preserve that uncertainty explicitly.

## What was lost

A finished-looking answer is not allowed to hide what was dropped.

Synthesis records losses such as:

- `DISSENT:<agent>`
- `UNKNOWN:<agent>`
- `PROVENANCE_GAP:<agent>`

If the decision is unresolved, `what_was_lost` must not be empty.

If every packet is a clean `ACCEPT` and nothing is missing, `what_was_lost` is empty.

## Example

Expected council:

- ANALYST
- RED_TEAM
- SYNTHESIZER

Received:

- ANALYST: ACCEPT
- RED_TEAM: UNKNOWN
- SYNTHESIZER: ACCEPT

Result:

```text
PACKET_INTEGRITY_WARNING

Consensus: NOT ESTABLISHED
Human decision required: YES
```