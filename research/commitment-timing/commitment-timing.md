# AISØN — Commitment Timing

STATUS: PARKED / INTERNAL  
NOVELTY CLAIM: NONE  
EXPERIMENT: NO  
NEW PHASE: NO  
PUBLICATION: NO

## Purpose

This parked internal note consolidates decisions already made in prior AISØN discussions. It records a bounded engineering consideration, not a new research direction, mechanism, or AISØN doctrine.

## Core Principle

`Fast inference ≠ fast commitment.`

A system may form a candidate decision quickly without immediately converting it into irreversible action.

A reconsideration window may depend on uncertainty, reversibility, urgency, and the system's current decision state. These considerations do not establish a universal waiting period or imply that delay is always preferable.

This principle remains a design consideration. This note specifies no implementation or experiment and claims no validated benefit.

## Deferred Commitment Under Explicit Decision Boundaries

Fast inference does not imply immediate commitment. This subsection applies only where a discrete commitment can be deferred and the policy maintains an explicit decision variable governed by a threshold, hysteresis band, or similar boundary.

While commitment is withheld, that variable may change without an external action. The eventual commitment may therefore appear abrupt even though the decision variable evolved earlier.

Separate two design questions:

1. **Online observability:** whether a supervisor can see the pre-commitment decision-variable state before action.
2. **Post-hoc reconstructability:** whether the system can later reconstruct the decision-variable trajectory and operative boundary at the time of commitment.

Online observability is an interface-design choice. Post-hoc reconstructability is a separate logging choice. Providing one does not establish the other.

This subsection does not apply to policies without an explicit decision variable, or to systems without a discrete, deferrable commitment.

### Threshold-Crossing Explanations: Why Now vs Why Act

The observation that crosses the boundary may explain why the action occurred at that time without adequately summarizing why the action was taken.

Core rule:

`Do not log only the boundary-crossing event.`

At minimum, preserve:

- the decision-variable trajectory;
- the operative boundary at crossing.

Record the following only where the policy actually defines them:

- per-step contributions;
- margin-to-threshold.

These are conditional logging examples, not general requirements for every policy. This note requires enough information to reconstruct the relevant trajectory and boundary, not an exact reconstruction of every internal computation.

## General Provenance Concerns

Data freshness remains a general provenance concern. It is separate from the distinction between why an action occurred at a particular time and why the action was taken.

## Scope and Non-Claims

This note does not claim:

- `Trigger ≠ Cause`;
- causal symmetry between the final observation and prior evidence;
- that CUSUM change time versus alarm time is equivalent to belief formation versus commitment;
- a new mechanism, AISØN doctrine, or terminology;
- empirical validation or a general explanation of black-box policies.

Status remains PARKED / INTERNAL. No experiment, new Phase, or publication is authorized by this note.
