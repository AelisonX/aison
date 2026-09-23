# Example: Evidence-Tagged Review

This example shows how AISØN can review a simple engineering claim without turning model agreement into evidence.

## Claim

> Increasing a service timeout from 2 seconds to 5 seconds will reduce user-visible failures.

Initial status:

`HYP`

The claim is testable, but no measurement has been provided yet.

## Multi-model review

### Model A

Verdict: `REVISE`

Reason:

A longer timeout may reduce premature failures, but it may also increase perceived latency.

Suggested status:

`HYP`

### Model B

Verdict: `ACCEPT FOR TESTING`

Reason:

The claim is plausible under unstable network conditions, but current production behavior is unknown.

Suggested status:

`HYP`

### Model C

Verdict: `REVISE`

Reason:

The correct timeout may depend on request type rather than one global value.

Suggested status:

`HYP`

## Synthesis

All three models consider the claim plausible.

That does not upgrade the claim.

Final pre-test status:

`HYP`

Reason:

No production measurement or verified literature was added during review.

## Human adjudication

Decision:

Run an experiment before changing the default timeout.

Suggested test:

- compare 2-second and 5-second timeout behavior
- measure completion rate
- measure user-visible latency
- record timeout failures
- preserve request-type differences

## What was lost

The synthesis must preserve the main disagreement:

- a longer timeout may reduce premature failures
- a longer timeout may also increase latency
- one timeout may not fit every request type

## After evidence arrives

If production data shows that 5 seconds reduces failures without unacceptable latency, the claim may be reclassified based on the actual evidence.

Model agreement alone is not enough.

> Agreement can prioritize a test. It cannot replace the test.
