AISØN Epistemic Agency Layer

Phase 0 Test 001 — Kickoff Note

Status: Pre-registered research artifact
Phase: 0
Test ID: EA-P0-001
Working topic: Odysseus lunar lander attitude reporting
Purpose: Test whether multiple AI systems can consistently extract and classify claims from the same fixed source set before any human-subject experiment is attempted.

⸻

1. Research Context

This test belongs to the AISØN Epistemic Agency Layer research line.

North Star:

Show the selection, not just the result.

The broader research goal is to explore whether an information layer can preserve human epistemic agency by making source selection, claim extraction, uncertainty, disagreement, and synthesis visible.

This test does not attempt to prove that such a system improves human agency.

It tests a smaller prerequisite:

Can multiple AI systems even agree on what claims are present in the same fixed set of sources?

If claim extraction or classification is unstable at this stage, later reader-facing packet experiments would risk measuring presentation quality rather than epistemic reliability.

⸻

2. Case Selection

The selected case is the 2024 Intuitive Machines IM-1 mission involving the lunar lander Odysseus.

This case was chosen because early reporting about the lander’s attitude changed as additional information became available.

The event therefore contains:

* incomplete early information,
* evolving interpretation,
* later correction or clarification,
* multiple reporting layers,
* direct mission sources,
* later official updates.

This makes it useful for studying:

* claim extraction,
* temporal instability,
* source dependency,
* uncertainty,
* later correction,
* classification disagreement.

This test is not intended to judge whether any source acted irresponsibly.

The purpose is to study how claims evolve when evidence changes.

⸻

3. Fixed Source Set

Exactly four source roles are used.

Source S1 — Mission operator

Intuitive Machines official IM-1 mission updates.

Role:

* direct mission operator communication,
* early-status reporting,
* first-party interpretation.

Source S2 — News wire / external reporting

Reuters reporting from 23 February 2024.

Role:

* external journalistic reporting,
* synthesis of company statements and developing information.

Source S3 — Independent news reporting

Associated Press reporting from 23–24 February 2024.

Role:

* separate journalistic reporting,
* comparison with S2,
* possible shared-source or dependency analysis.

Source S4 — Later official evidence/update

NASA mission update from 28 February 2024.

Role:

* later-stage official reporting,
* subsequent imagery and mission-status context.

⸻

4. Source Selection Lock

The source set is fixed before claim extraction begins.

No reviewer may silently add another source.

If an additional source appears useful, it must be recorded separately as:

SUGGESTED_SOURCE

It must not be incorporated into Test 001 unless the test is formally restarted as a new version.

The purpose of this rule is to keep source selection itself visible.

⸻

5. Phase 0 Question

Primary question:

Given the same fixed sources, can Grok, Claude, and GPT consistently identify and classify the claims being made?

This phase does not test:

* whether readers prefer the packet,
* whether the summary is clearer,
* whether the system saves time,
* whether users feel more informed,
* whether the final account is “the truth.”

⸻

6. Test Sequence

Step A — Claim extraction

Grok receives the fixed source set first.

Grok produces a claim list.

Each extracted claim should include:

* claim ID,
* source ID,
* claim paraphrase,
* exact source anchor or quoted span where possible,
* attribution if the claim is itself reporting what another actor said,
* relevant time or scope,
* anchoring status.

Allowed anchoring status:

* ANCHORED
* UNANCHORED

If a claim cannot be linked reliably to source text, it must remain:

UNANCHORED

It must not be repaired through inference.

⸻

Step B — Source dependency notes

Grok may identify observable dependency signals such as:

* explicit citation of another outlet,
* near-identical wording,
* shared quoted material,
* common attribution,
* common document or event source.

Independence must not be assumed.

Default:

SOURCE_INDEPENDENCE = UNKNOWN

Five logos must not be treated as five independent observations.

⸻

Step C — Source-internal drop log

Grok records materially relevant source content encountered during extraction but excluded from the final claim list.

Each exclusion should include a short reason.

The drop log applies only to the fixed source set.

It is not intended to represent everything absent from the wider information environment.

⸻

Step D — Independent classification

After claim extraction is frozen, the same claim list is given separately to:

* Grok
* Claude
* GPT

Each system independently classifies the claims.

The classifiers must not see the other systems’ classifications before submitting their own.

⸻

7. Classification Labels

Initial candidate labels:

* FACT
* INTERPRETATION
* SPECULATION

These labels are treated as contestable editorial judgments, not ground truth.

Every classification must include a brief rationale.

Model agreement does not establish truth.

Model disagreement does not automatically establish uncertainty about the underlying event.

Classification disagreement itself is research data.

⸻

8. Critical Distinctions

The following distinctions must remain visible:

Attribution ≠ event

Example structure:

“The company said X”

is not equivalent to:

“X happened.”

⸻

Multiple sources ≠ independent confirmation

Repeated reporting may derive from:

* the same press conference,
* the same press release,
* the same wire story,
* the same underlying witness,
* the same quoted document.

⸻

Correction ≠ proof of misconduct

An early statement that later changes may reflect normal evidence updating.

⸻

Later knowledge ≠ earlier available knowledge

Reviewers must not silently judge early reporting using information that became available only later.

⸻

UNKNOWN ≠ FALSE

Failure to establish a claim does not establish its opposite.

⸻

9. Anti-Authority Rules

This experiment must not produce:

* truth scores,
* confidence rankings,
* source leaderboards,
* source reputation scores,
* winner labels,
* numeric epistemic ratings.

The purpose is to expose structure, not replace human judgment with a cleaner authority layer.

⸻

10. Reviewer Provenance

Every extraction and classification output must identify:

* model/provider,
* task role,
* date,
* whether the system had access to other reviewers’ outputs.

Known institutional relationships should be disclosed where relevant.

Reviewer provenance does not invalidate an analysis.

It remains visible because provenance and authority are separate questions.

⸻

11. Failure Conditions

Test 001 should be considered informative even if it fails.

Important failure signals include:

* reviewers cannot agree on claim boundaries,
* source anchors are unreliable,
* classification labels prove too unstable,
* attribution is repeatedly collapsed into event claims,
* source independence is assumed without evidence,
* later information contaminates interpretation of earlier reporting,
* drop-log decisions differ substantially,
* apparently simple claims cannot be cleanly represented.

Such results would argue against moving directly to a reader-facing packet experiment.

⸻

12. What Success Does NOT Mean

Even if Grok, Claude, and GPT classify claims similarly, this does not prove:

* that the classifications are correct,
* that the packet is neutral,
* that the packet preserves epistemic agency,
* that readers will inspect underlying sources,
* that the approach should become a product,
* that automated source selection is safe.

It only supports moving to the next research question.

⸻

13. Current Boundary

For Phase 0:

* no code,
* no new repo,
* no aison feature,
* no control-ledger change,
* no automated feed ingestion,
* no source recommendation engine,
* no political test case,
* no multilingual test case,
* no human-subject test yet.

This remains an AISØN research artifact.

⸻

14. Standing Social-Media Connection

The same research line informs AELIS’ØN public-post practice.

Working publishing principle:

Show the selection, not just the result.

A structurally honest evidence-based post should allow a reader to reject the interpretation while still identifying:

* what was observed,
* what evidence was used,
* where interpretation begins,
* what remains unresolved.

This principle should not be applied performatively to jokes, metaphors, or casual posts.

⸻

15. Phase 0 Test 001 Stop Condition

Do not proceed to human-reader experiments until the extraction and classification layer has produced interpretable evidence.

The immediate next action after this kickoff note is:

Freeze the four-source set and ask Grok to perform claim extraction only.

No classification should occur before the extraction list is frozen.