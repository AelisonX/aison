AISØN — Epistemic Agency

Phase 0 Findings

Status: Early research result
Scope: Representation only
Code status: No implementation justified yet

⸻

Research Question

How can an information system preserve human epistemic agency without becoming another hidden authority layer?

Working North Star:

Show the selection, not just the result.

The aim is not to build a better oracle.

It is to preserve enough visibility around:

* source selection,
* evidence,
* uncertainty,
* disagreement,
* interpretation,
* revision,

that a user can still inspect, disagree, delay, revise, and refuse.

⸻

Phase 0 Test 001

The first test used a fixed set of four sources covering the evolving reporting around the 2024 Odysseus lunar lander.

A frozen list of 34 claims was independently classified by GPT, Claude, and Grok using:

* FACT
* INTERPRETATION
* SPECULATION

with TAXONOMY_BREAK allowed.

Result:

Model	FACT	INTERPRETATION	SPECULATION	TAXONOMY_BREAK
GPT	34	0	0	0
Claude	32	0	0	2
Grok	32	0	0	2

The taxonomy largely collapsed.

Why?

Most claims had been written as:

Source X said Y.

The classifiers therefore mostly answered:

Did Source X say Y?

instead of:

What kind of epistemic claim is Y?

Finding 1

Attribution truth and content epistemic status are different variables.

A statement may be fully anchored while its embedded content remains:

* uncertain,
* interpretive,
* hypothetical,
* predictive,
* revised.

⸻

Phase 0 Test 002

The second test separated two questions.

Axis A — Attribution / Provenance

Who said it, and is that attribution clear?

Axis B — Embedded Content Type

What kind of statement is being made?

Candidate content types included:

* state report,
* interpretation,
* hypothesis,
* forecast,
* plan,
* revision,
* uncertainty report,
* meta report.

The same frozen 34-claim set was reused.

Two genuinely independent reviewers, Grok and Claude, were compared.

Result:

* Axis A agreement: 33 / 34
* Axis B agreement: 27 / 34

The provenance layer became highly stable.

The content layer became substantially more informative than in Test 001, but several category boundaries remained unstable.

⸻

Boundary Findings

The seven Axis B disagreements clustered into three patterns.

1. Interpretation vs Hypothesis

A hedged causal reconstruction may be read as:

* interpretation of evidence,
* or a hypothesis about what happened.

The source text often does not expose enough of the underlying evidence chain to make this distinction cleanly.

2. State Report vs Interpretation

Qualitative assessments such as:

“quite a bit of operational capability”

can sit between:

* reporting a state,
* and interpreting what the available evidence means.

3. Multi-Type Claims

Some sentences contain several epistemic acts at once.

For example:

* state report,
* uncertainty,
* causal interpretation,
* forecast.

This suggests:

One sentence does not necessarily equal one epistemic unit.

Forcing one primary label may itself introduce editorial distortion.

⸻

Process Integrity Finding

GPT did not produce an independent blind Test 002 classification.

Claude’s classification had already been visible before GPT could classify.

Therefore GPT was not counted as a third independent reviewer for Test 002.

This limitation is preserved explicitly rather than hidden.

That is itself part of the research principle:

Show the selection, not just the result.

Methodological imperfections are provenance too.

⸻

Strongest Current Findings

1. Separate attribution from epistemic content

Who said it and what kind of claim they made should not be represented as the same variable.

2. Align the object before comparing the verdict

Two systems may appear to disagree because they are judging different layers.

Two systems may appear to agree because both are judging only the reporting wrapper.

3. Provenance is easier to stabilize than interpretation

Attribution/provenance showed much higher cross-model agreement than embedded-content classification.

4. Structure itself can become authority

A clean packet with labels, timestamps, citations, and UNKNOWN markers may feel more trustworthy than the evidence deserves.

Structural transparency ≠ preserved inspection behaviour.

5. The system must not merely re-encode hedge words

If labels reduce to spotting:

* may,
* believes,
* appears,
* thought,

the representation is only a hedge detector.

That is not enough.

⸻

Current Research Principle

Preserve human judgment by keeping selection, evidence, uncertainty, disagreement, and exit visible.

And:

A synthesis should expose its seams.

The objective is not to eliminate influence.

It is to keep influence:

* visible,
* contestable,
* inspectable,
* resistible.

⸻

Current Non-Claims

Phase 0 does not establish that:

* the current taxonomy is correct,
* a two-axis schema is final,
* structured packets preserve human agency,
* automated source selection is safe,
* a product should be built,
* AI can determine truth.

The current result is narrower:

A representation that collapses provenance and epistemic content can appear clean while hiding important differences.

Separating those layers improves clarity, but does not remove interpretive ambiguity.

⸻

Current Boundary

No code is justified yet.

No new repo is justified.

No product is justified.

The work remains an AISØN research artifact.

Future work should test whether a more precise representation helps humans inspect information better without teaching them to trust the representation itself.

⸻

Short Compression

Phase 0 failed in a useful way.

Test 001 turned almost everything into FACT.

Test 002 showed why:

“A source said X” is not the same claim as “X is established.”

Separating provenance from embedded content greatly improved the representation.

But interpretation remains the harder layer.

That is where the next real research problem begins.