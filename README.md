# aison
[![Tests](https://github.com/AelisonX/aison/actions/workflows/tests.yml/badge.svg)](https://github.com/AelisonX/aison/actions/workflows/tests.yml)
A small framework for decisions that remember disagreement.
# AISØN

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