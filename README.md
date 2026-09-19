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

## Core principle

**Missing is not consent.**

A missing response must not be silently converted into agreement.

If an expected agent response is missing, truncated, or incomplete, AISØN should preserve that uncertainty explicitly.

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

## Epistemic labels

AISØN distinguishes between:

- FACT
- INTERPRETATION
- SPECULATION
- MODEL_SELF_REPORT
- FICTION
- JOKE

These labels describe the status of a claim.

They do not determine its truth automatically.

## Human authority

Models may:

- analyze
- challenge
- propose
- synthesize
- audit

Models may not silently convert:

- suggestion into command
- consensus into truth
- missing evidence into agreement

Final authority remains human.

## Tests

AISØN currently protects four core invariants with automated tests:

- **Missing is not consent.**
- **UNKNOWN is not ACCEPT.**
- **DISSENT survives synthesis.**
- **Human final authority remains required.**

Tests run automatically on every push through GitHub Actions.

## Status

AISØN is currently in **v0.1 prototype development**.

The first implementation uses simple local Python structures and mocked agent outputs.

No API keys required.

---

**A good system does not only remember what it decided.  
It remembers what it could not resolve.**