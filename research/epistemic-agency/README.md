AISØN — Epistemic Agency

Working subtitle: Preserving human judgment in mediated information environments
Status: Early research line
Current phase: Phase 0
Code status: No implementation justified yet

⸻

1. Core Question

Modern humans increasingly encounter the world through mediated systems:

* social platforms,
* recommendation systems,
* news media,
* search engines,
* advertising,
* AI assistants,
* influencers,
* institutional communications.

These systems do not need direct physical control to affect real-world action.

They can shape:

* what a person sees,
* what feels important,
* what appears urgent,
* what seems familiar,
* what appears widely believed,
* which options feel available,
* how confident a person feels about acting.

A human may therefore retain formal decision authority while their information environment substantially shapes the decisions that feel possible or necessary.

The research question is:

How can information systems preserve meaningful human epistemic agency without becoming another hidden authority layer?

⸻

2. Working Definition of Epistemic Agency

Epistemic agency is not the absence of influence.

No human decision environment is influence-free.

The relevant question is whether the person can still meaningfully:

* inspect,
* compare,
* disagree,
* delay,
* ask for evidence,
* recognize uncertainty,
* revise,
* refuse.

Formal choice is not sufficient if these actions become functionally difficult or prohibitively costly.

A useful agency test is:

Can the human still meaningfully disagree, delay, inspect, reverse, and refuse?

A further refinement is:

Refuse at what cost?

A theoretical right to refuse is weaker than a practical ability to refuse.

⸻

3. Research North Star

Initial formulation:

Do not curate reality for the user. Curate the evidence around reality.

This remains useful as an intuition, but it risks implying that the system can cleanly identify the boundaries of reality itself.

The more defensible operational form is:

Show the selection, not just the result.

This means making materially relevant choices visible, including:

* what sources were selected,
* who selected them,
* what was excluded,
* what evidence supports each claim,
* where disagreement remains,
* where interpretation begins,
* what remains UNKNOWN.

The objective is not to eliminate synthesis.

It is to produce:

a synthesis with exposed seams.

⸻

4. Foundational Principles

Influence ≠ Authority

A system may influence a human without acquiring legitimate authority over the human’s decision.

Recommendation ≠ Command

Advice must remain rejectable.

Familiarity ≠ Trustworthiness

A familiar model, persona, platform, institution, or voice does not earn epistemic authority merely through repeated exposure.

Emotional Salience ≠ Evidence

Fear, excitement, outrage, urgency, repetition, or emotional resonance must not silently become evidentiary weight.

Provenance ≠ Authority

Knowing where a claim came from does not determine whether the claim is true or whether the source deserves decision authority.

UNKNOWN Stays UNKNOWN

Failure to establish a proposition does not establish its opposite.

Dissent Must Remain Legible

Disagreement may be compressed for readability but must not disappear where it remains materially unresolved.

Agreement ≠ Independent Confirmation

Multiple outlets can repeat one underlying report.

Five logos may still represent one observation.

Human Authority Must Remain Exercisable

Human final authority is meaningful only if the surrounding system preserves real opportunities to inspect, resist, delay, reverse, and refuse.

⸻

5. A Key Governance Extension

“Human stays in command” is necessary but incomplete if interpreted only as a question of formal authority.

The human command layer also operates inside an information environment.

A better principle is:

The human remains in command; the inputs, dissent, and exit options surrounding that command must remain inspectable. A system may flag that options are narrowing, but must not use that observation as justification to take control.

This distinction is essential.

The system may warn:

* dissent is disappearing,
* refusal costs are rising,
* previous red lines have shifted,
* evidence is becoming narrower,
* one narrative dominates the decision environment.

But it must not conclude:

The human is captured, therefore human authority is void.

That would transform a safety mechanism into an override mechanism.

⸻

6. The Core Failure Mode

The dangerous outcome is not necessarily an obvious “truth machine.”

A more realistic failure is:

a fluent, elegant, well-sourced, apparently transparent information layer that users trust so much that they stop checking what lies beneath it.

This produces a critical distinction:

Structural transparency ≠ preserved inspection behaviour.

Showing citations, labels, timestamps, UNKNOWN markers, and provenance may still create a stronger authority effect if the resulting packet feels more complete than the underlying evidence warrants.

The layer may simply move authority:

from conclusion
to presentation.

⸻

7. Why Source Selection Matters

An information system does not only shape understanding through what it says.

It also shapes understanding through what enters the system at all.

This creates an upstream editorial problem:

What gets into the packet?

Selection itself is epistemically consequential.

Therefore source selection should remain visible.

A user-facing system should not silently:

* add sources,
* remove inconvenient claims,
* collapse repeated reporting into apparent consensus,
* treat missing perspectives as irrelevant,
* hide its own retrieval limits.

The selector is part of the evidence chain.

⸻

8. Phase 0 Test 001

EA-P0-001 used the 2024 Odysseus lunar lander reporting sequence.

The case was selected because early understanding of the lander’s orientation evolved as new information became available.

A fixed four-source set was used:

* Intuitive Machines,
* Reuters,
* Associated Press,
* NASA.

Grok first extracted a frozen claim list.

The extraction preserved:

* attribution,
* uncertainty,
* source anchors,
* timing,
* observable source dependency,
* a bounded source-internal drop log.

The frozen list contained 34 claims.

GPT, Claude, and Grok then independently classified the claims using:

* FACT,
* INTERPRETATION,
* SPECULATION,

with TAXONOMY_BREAK allowed where necessary.

⸻

9. Phase 0 Result

The taxonomy largely collapsed.

Results:

Model	FACT	INTERPRETATION	SPECULATION	TAXONOMY_BREAK
GPT	34	0	0	0
Claude	32	0	0	2
Grok	32	0	0	2

The problem was structural.

Most claims had been written as:

Source X said Y.

The classifiers therefore answered:

Did Source X say Y?

instead of:

What kind of epistemic claim is Y?

This exposed a major distinction:

Attribution truth and content epistemic status are different variables.

⸻

10. First Major Research Finding

EA-P0-001 produced the following principle:

Before comparing judgments, align what object is being judged.

Short form:

Align the object before comparing the verdict.

Two models may appear to disagree because they classify different layers.

Two models may also appear to agree because both classify only a shallow reporting wrapper.

Agreement alone therefore does not guarantee semantic alignment.

⸻

11. Representation Problems Identified

EA-P0-001 exposed at least three classes of representation failure.

Revision

A proposition can be:

* believed,
* reported,
* withdrawn,
* corrected,
* explained.

A static one-label classification does not represent this lifecycle.

Agentless Belief

Phrases such as:

“is thought”

may contain a belief without naming who holds it.

This creates attribution ambiguity.

Vague Meta-Claim

A source may say there is:

“additional insight”

without specifying the actual proposition.

The sentence may be anchored while remaining semantically too thin to classify meaningfully.

⸻

12. Claim Granularity

Another finding is:

One sentence does not necessarily contain one epistemic act.

A single sentence may bundle:

* observation,
* interpretation,
* forecast,
* uncertainty,
* causality,
* revision.

Future representation may need to distinguish:

1. source span,
2. extracted claim,
3. embedded proposition,
4. epistemic type,
5. revision history.

No schema is adopted yet.

⸻

13. Candidate Representation Direction

One possible future design is a two-axis system.

Axis 1 — Attribution / Provenance

Possible states:

* anchored,
* unanchored,
* attribution unclear.

Axis 2 — Embedded Content Type

Possible forms:

* state report,
* interpretation,
* hypothesis,
* forecast,
* plan,
* uncertainty,
* revision.

This remains a candidate.

Phase 0 has not yet established that this is the correct schema.

No code should be built from it yet.

⸻

14. Social-Media Implication

The same research principles now apply to AELIS’ØN public posting.

Working public principle:

Show the selection, not just the result.

For evidence-based posts, readers should be able to identify:

* what was observed,
* what evidence was used,
* where interpretation begins,
* what remains unresolved.

A structurally honest post should survive reader disagreement.

That means:

A reader may reject the interpretation while still understanding the evidence and reasoning path.

This does not mean every post requires a methodological appendix.

For ordinary X posts, the lightweight standard is:

* expose at least one meaningful seam,
* keep FACT / INTERPRETATION / SPECULATION distinguishable,
* put source context or limitations in a reply when necessary,
* do not use familiarity, urgency, or confidence as substitutes for evidence.

Jokes remain jokes.

Metaphors remain metaphors.

Not every fart requires provenance metadata.

Civilization has limits.

⸻

15. Current Boundary

This research line currently remains:

AISØN research artifact only.

It does not currently justify:

* a new repo,
* a new named agent,
* changes to aison,
* changes to control-ledger,
* automated source selection,
* feed ingestion,
* a product,
* a startup.

The work should remain reversible while its representation model is still unstable.

⸻

16. Current Non-Claims

This research does not claim:

* that AI systems are secretly controlling users,
* that social media users lack free will,
* that one source class is universally more trustworthy,
* that neutrality can be automated,
* that a structured packet is inherently safer than raw sources,
* that more transparency automatically increases agency,
* that the proposed system can determine truth.

The research begins from a narrower claim:

Information environments influence human judgment.

The governance question is:

How can that influence remain visible, contestable, and resistible?

⸻

17. Current North Star

The strongest current formulation is:

Preserve human judgment by keeping selection, evidence, uncertainty, disagreement, and exit visible.

The shortest operational rule remains:

Show the selection, not just the result.

The goal is not to create a better oracle.

The goal is to make it harder for any oracle, including AISØN itself, to quietly become the user’s reality.

⸻

Research Artifacts

* phase0-test-001-kickoff.md
* phase0-test-001-results.md

Future tests should be added only when the current representation problem has been deliberately reframed.