AISØN Epistemic Agency

Phase 0 Test 002 — Kickoff Note

Test ID: EA-P0-002
Status: Pre-registered research artifact
Phase: 0
Case: Same Odysseus source set and frozen claim list from EA-P0-001
Purpose: Test whether separating attribution/provenance from embedded content type produces a more informative and stable cross-model representation.

⸻

1. Why Test 002 Exists

EA-P0-001 found that the original taxonomy:

* FACT
* INTERPRETATION
* SPECULATION

largely collapsed when applied to claims written with attribution preserved.

Most claims had the form:

Source X said Y.

The models therefore classified the outer reporting act:

Did Source X say Y?

rather than the inner proposition:

What kind of claim is Y?

This produced mostly FACT.

EA-P0-002 tests a narrower representation change:

Separate attribution/provenance status from embedded content type.

This test does not assume that the new representation is correct.

It attempts to falsify it.

⸻

2. Fixed Inputs

EA-P0-002 reuses:

* the same four locked sources,
* the same frozen C001–C034 claim list,
* the same source anchors,
* the same attribution fields.

No new source may be added.

No claim may be:

* added,
* removed,
* merged,
* rewritten.

The purpose is to change only the representation task.

⸻

3. Research Question

Primary question:

When attribution/provenance and embedded content are classified separately, do GPT, Claude, and Grok produce more informative and more stable judgments than in EA-P0-001?

Secondary question:

Does the two-axis structure clarify disagreement, or merely create more labels and new ambiguity?

⸻

4. Axis A — Attribution / Provenance Status

Each frozen claim must receive exactly one Axis A label.

Allowed labels:

ANCHORED_ATTRIBUTION

The claim has a clear source anchor and a clear identified speaker, publisher, or reporting source.

ATTRIBUTION_UNCLEAR

The claim is anchored, but the holder of the belief, assertion, or judgment is unclear or missing.

UNANCHORED

The claim cannot be reliably linked to a supporting source span.

Important:

Axis A does not evaluate whether the embedded content is true.

It evaluates whether the statement is traceable.

⸻

5. Axis B — Embedded Content Type

Each frozen claim receives one primary Axis B label.

Allowed labels:

STATE_REPORT

A claim about an observed, reported, or current state.

Examples:

* communications exist,
* telemetry is available,
* an image was captured,
* a vehicle is in a reported condition.

INTERPRETATION

A claim that explains or interprets observed information.

Examples:

* the craft apparently tripped,
* a signal pattern means a particular condition,
* an image implies a specific state.

HYPOTHESIS

A claim proposing a possible explanation or event without establishing it.

Examples:

* may have snapped a leg,
* could have struck a rock,
* possibly leaned against something.

FORECAST

A claim about what is expected to happen later.

Examples:

* operations may continue for nine days,
* communications will be limited.

PLAN

A claim about intended future action.

Examples:

* a press conference will occur,
* an orbiter will attempt a location pass.

REVISION

A claim whose important function is to revise, withdraw, or correct an earlier proposition.

UNCERTAINTY_REPORT

A claim whose important content is that something remains unknown, unresolved, or still being determined.

META_REPORT

A claim about information status rather than the underlying physical state.

Examples:

* additional insight became available,
* a briefing occurred,
* data are ready for analysis.

⸻

6. Mixed Claims

Some frozen claims contain more than one content type.

Do not rewrite or split them.

If one type clearly dominates the function of the frozen claim:

assign that as the primary Axis B label.

Then add:

SECONDARY_TYPE:

If no primary type can be chosen without substantial distortion, use:

MULTI_TYPE_BREAK

and explain why.

Do not force a clean label merely for consistency.

⸻

7. Special Rules

Attribution ≠ Content

A claim may be:

ANCHORED_ATTRIBUTION

while its embedded content is:

HYPOTHESIS

or:

INTERPRETATION.

This is expected.

⸻

Anchored ≠ True

A source anchor proves that the source said something.

It does not establish the truth of the embedded proposition.

⸻

Revision ≠ Falsehood

If an earlier proposition is revised, this does not automatically mean its opposite is established.

⸻

UNKNOWN Stays UNKNOWN

Do not turn missing information into a negative claim.

⸻

Agreement ≠ Truth

Cross-model agreement is a consistency signal only.

It is not epistemic authority.

⸻

8. Reviewer Procedure

GPT, Claude, and Grok must classify independently.

Each reviewer receives:

* the frozen C001–C034 list,
* this kickoff note,
* no other model’s Test 002 classification.

For every claim, return:

CLAIM_ID:
AXIS_A:
AXIS_B:
SECONDARY_TYPE:
RATIONALE:

If no secondary type is needed:

SECONDARY_TYPE: none

If the content cannot be represented without distortion:

AXIS_B: MULTI_TYPE_BREAK

⸻

9. Evaluation

EA-P0-002 will compare:

A. Axis A agreement

Do models agree on:

* anchored attribution,
* unclear attribution,
* unanchored status?

B. Axis B agreement

Do models agree on content type?

C. Break frequency

How often does the schema require:

* ATTRIBUTION_UNCLEAR
* MULTI_TYPE_BREAK

D. Information gain

Does the new representation preserve distinctions that disappeared in EA-P0-001?

For example:

Can it distinguish:

“Reuters reported Altemus said X”

from:

“X is a hypothesis”?

E. Complexity cost

Does the new representation become so complicated that it is harder to inspect than the original source?

A more expressive schema is not automatically a better schema.

⸻

10. Failure Conditions

The candidate representation should be treated as failing or needing major revision if:

* Axis B agreement remains low,
* most claims become MULTI_TYPE_BREAK,
* labels depend strongly on reviewer interpretation,
* the distinction adds little information beyond the original text,
* users would need a taxonomy manual to understand the packet,
* attribution and content still collapse into each other,
* the structure creates false confidence through formatting.

⸻

11. Success Does Not Mean Product Readiness

Even strong agreement would not establish that:

* the schema is objectively correct,
* the packet preserves human agency,
* readers understand the distinction,
* the system should select sources automatically,
* the system should become a product.

This test evaluates representation only.

⸻

12. Current Boundary

EA-P0-002 remains:

* no code,
* no new repo,
* no human subjects,
* no political case,
* no automated source selection,
* no feed ingestion,
* no product claims.

It remains an AISØN research artifact.

⸻

13. Expected Research Value

EA-P0-002 is useful even if it fails.

Possible outcomes include:

Outcome A

The two-axis structure produces substantially better agreement and information.

Result:

Worth further testing.

Outcome B

Attribution becomes stable, but embedded content classification remains unstable.

Result:

The provenance problem and interpretation problem should remain separated.

Outcome C

The schema creates too many breaks or mixed labels.

Result:

The representation is over-engineered.

Outcome D

Models agree strongly, but only because the categories remain shallow.

Result:

Apparent stability may still be uninformative.

⸻

14. Stop Condition

Do not proceed to human-reader testing after this experiment automatically.

First determine:

Did the representation become more informative without becoming more authoritative or more complex than the evidence deserves?

Only then should another phase be considered.