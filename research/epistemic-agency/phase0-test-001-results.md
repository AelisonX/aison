AISØN Epistemic Agency Layer

Phase 0 Test 001 — Results Note

Test ID: EA-P0-001
Status: Completed
Phase: 0
Case: Odysseus lunar lander attitude reporting
Purpose: Test whether multiple AI systems can consistently classify claims extracted from the same fixed source set.

⸻

1. Summary

EA-P0-001 produced a clear result:

The original three-label taxonomy:

* FACT
* INTERPRETATION
* SPECULATION

was not discriminative enough when applied to claims written with attribution preserved.

The primary reason was structural.

Most frozen claims had the form:

Source X said Y.

Under the instruction:

Classify the claim as written, including its attribution.

the models mostly classified whether the attributed statement was actually present in the source.

That is an attribution/provenance question.

It is not the same question as:

What is the epistemic character of Y?

As a result, nearly every claim became FACT.

The experiment therefore identified a representation problem before any reader-facing packet was built.

⸻

2. Frozen Claim Set

The extraction stage produced:

34 claims: C001–C034

The claim list was frozen before classification.

No model was allowed to:

* add claims,
* remove claims,
* merge claims,
* rewrite claims,
* add sources,
* use later knowledge to repair earlier claims.

⸻

3. Independent Classification Results

GPT

* FACT: 34
* INTERPRETATION: 0
* SPECULATION: 0
* TAXONOMY_BREAK: 0

GPT treated all frozen claims as classifiable at the attribution layer.

Key interpretation:

The classification succeeded formally but became minimally informative.

GPT’s position was that even claims with complex or unclear embedded content could still be classified as FACT if the reporting act itself was anchored.

⸻

Claude

* FACT: 32
* INTERPRETATION: 0
* SPECULATION: 0
* TAXONOMY_BREAK: 2

Claude marked:

* C012
* C023

as TAXONOMY_BREAK.

C012

C012 bundled:

1. a prior company upright reading,
2. a later correction,
3. an explanation for the earlier error.

Claude argued that one label cannot adequately represent:

* a proposition,
* its withdrawal,
* and the reason for revision.

This exposed a missing representation for claim revision.

C023

C023 used:

“is thought”

without identifying who held that belief.

Claude argued that classifying the claim as FACT would only record that AP printed the sentence, while classifying it as INTERPRETATION would silently turn an agentless statement into an event claim.

This exposed a missing representation for agentless belief.

⸻

Grok

* FACT: 32
* INTERPRETATION: 0
* SPECULATION: 0
* TAXONOMY_BREAK: 2

Grok marked:

* C023
* C032

as TAXONOMY_BREAK.

C023

Grok agreed with Claude that:

“is thought”

without a named holder does not fit cleanly into the three-label taxonomy.

C032

C032 stated only that an image provided:

“additional insight into Odysseus’ position”

without specifying:

* the position,
* the interpretation,
* the hypothesis,
* or the actual new proposition.

Grok argued that forcing the sentence into FACT, INTERPRETATION, or SPECULATION would invent content that was not present.

This exposed a missing representation for vague meta-claims.

⸻

4. Cross-Model Comparison

Model	FACT	TAXONOMY_BREAK	Break claims
GPT	34	0	none
Claude	32	2	C012, C023
Grok	32	2	C023, C032

There was no meaningful use of:

* INTERPRETATION
* SPECULATION

across any model.

This is itself the main result.

The three-label taxonomy did not meaningfully separate the frozen claims.

⸻

5. Primary Finding

The first major finding is:

Attribution truth and content epistemic status are different variables.

These two questions must not be collapsed:

Question A — Attribution / provenance

Did Source X actually say Y?

Question B — Embedded content status

What kind of claim is Y?

Examples of embedded content may include:

* state report,
* interpretation,
* forecast,
* plan,
* hypothesis,
* revision,
* uncertainty,
* speculation.

A claim can be:

FACT at the attribution layer

while containing:

speculation at the embedded-content layer.

Example:

Reuters reported that Altemus said the lander “may have snapped a leg.”

It may be factual that Reuters reported this.

But:

“may have snapped a leg”

is still a hedged hypothesis inside the attributed statement.

⸻

6. Representation Failure vs Classification Failure

The models exposed two different failure interpretations.

Claude-style interpretation

Some claims cannot honestly fit one label.

This is:

classification failure.

GPT-style interpretation

The claim can still be classified at the attribution layer, but the classification loses useful meaning.

This is:

classification succeeds while representation fails.

These are not contradictory.

They describe two different places where the schema can break.

⸻

7. Break Types Identified

EA-P0-001 surfaced at least three representation problems.

A. Revision

Example:

C012

A prior proposition was stated and later withdrawn or corrected.

A single static label does not represent:

* earlier belief,
* later rejection,
* reason for revision,
* temporal order.

⸻

B. Agentless belief

Example:

C023

A claim says:

“is thought”

without clearly identifying who holds the view.

This makes attribution ambiguous.

⸻

C. Vague meta-claim

Example:

C032

A source says there is:

“additional insight”

without specifying the actual proposition produced by that insight.

The statement may be anchored while remaining too semantically thin to classify meaningfully.

⸻

8. Additional Finding: Claim Granularity Matters

Several frozen claims bundled more than one epistemic act.

Examples include:

* state report + forecast,
* geometry report + causal consequence,
* revision + explanation,
* uncertainty + operational assessment.

This suggests that:

one sentence does not necessarily equal one epistemic unit.

Future representation may need to distinguish:

* source sentence,
* extracted claim,
* embedded proposition,
* revision event.

No new schema is adopted yet.

⸻

9. Important Negative Result

EA-P0-001 did not show that the three models disagreed strongly about the Odysseus event itself.

Instead, they mostly agreed on the attribution layer.

The disagreement was primarily about:

what exactly the classification task was supposed to represent.

This means the first Phase 0 problem is not model disagreement about reality.

It is representation alignment.

⸻

10. Research Principle Produced

EA-P0-001 supports the following principle:

Before comparing judgments, align what object is being judged.

A shorter form:

Align the object before comparing the verdict.

This applies beyond this experiment.

Two systems can appear to disagree while actually answering different questions.

Likewise, two systems can appear to agree because they are classifying a shallow wrapper rather than the underlying proposition.

⸻

11. Connection to Epistemic Agency

This result matters to the broader Epistemic Agency Layer because a reader-facing packet could easily display:

FACT

while the underlying meaning is only:

It is a fact that someone said this.

A user may instead read that label as:

This event claim is established.

That would create structure-as-authority.

The packet could therefore become more misleading precisely because it looks organized and transparent.

This supports the broader warning:

Structural transparency does not guarantee preserved agency.

A fluent, well-labeled packet may still move authority into the layout itself.

⸻

12. What EA-P0-001 Does Not Establish

This test does not establish:

* that any source was wrong,
* that any model was correct,
* that one taxonomy replacement is best,
* that a two-axis schema will work,
* that the Epistemic Agency Layer preserves human agency,
* that readers will inspect original sources,
* that a product should be built.

The result only establishes that the current representation is insufficient for the intended classification task.

⸻

13. Candidate Direction — Not Yet Adopted

A possible future representation may separate:

Axis 1 — Attribution / provenance status

Examples:

* anchored
* unanchored
* attribution unclear

Axis 2 — Embedded content type

Possible examples:

* state report
* interpretation
* hypothesis
* forecast
* plan
* revision
* uncertainty

This is only a candidate direction.

EA-P0-001 does not validate this schema.

No code should be written from it yet.

⸻

14. Repo Boundary

The result remains:

AISØN research artifact only.

No change is currently justified to:

* aison
* control-ledger
* any runtime system
* any new repo

This is still Phase 0 research.

⸻

15. Standing Social-Media Relevance

The result also strengthens the AELIS’ØN publishing principle:

Show the selection, not just the result.

A public post should avoid using labels or structure that silently imply more certainty than the evidence supports.

In particular:

“Source X said Y”

must remain distinguishable from:

“Y is established.”

Reader disagreement should remain possible without destroying the structural honesty of the post.

⸻

16. Current Status

EA-P0-001 is complete.

The next research step should not be automatic.

Before Test 002, the team should decide whether to:

* redesign the representation,
* test claim granularity,
* test attribution vs embedded-content separation,
* or stop the line if the complexity no longer serves the original goal.

No automatic progression is assumed.

⸻

17. Final Compression

EA-P0-001 found that:

Preserving attribution is necessary, but attribution alone can make epistemic classification collapse into trivial FACT labels.

Therefore:

The system must preserve both who said something and what kind of statement they made.

And before comparing model judgments:

Align the object before comparing the verdict.