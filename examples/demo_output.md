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

Human decision required:
YES
```

## Interpretation

AISØN does not convert missing context into agreement.

It preserves:

- dissent
- unknown states
- provenance gaps
- human final authority

The system may still synthesize an incomplete council.

It may not call that completeness consensus.

> Missing is not consent.