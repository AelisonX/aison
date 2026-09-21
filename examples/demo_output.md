# AISØN v0.1 — Demo Output

This example shows the core behavior AISØN is designed to preserve.

## Scenario

Expected council:

- ANALYST
- RED_TEAM
- SYNTHESIZER

Received packets:

- ANALYST: ACCEPT
- RED_TEAM: DISSENT
- SYNTHESIZER: UNKNOWN

The SYNTHESIZER expected input from both ANALYST and RED_TEAM, but only received ANALYST.

## Result

```text
AISØN COUNCIL DEMO
------------------

Status: UNRESOLVED

Consensus:
- ANALYST

Dissent:
- RED_TEAM

Unknown:
- SYNTHESIZER

Provenance gaps:
- SYNTHESIZER

What was lost:
- DISSENT:RED_TEAM
- UNKNOWN:SYNTHESIZER
- PROVENANCE_GAP:SYNTHESIZER

Human decision required:
YES