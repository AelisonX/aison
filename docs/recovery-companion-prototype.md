# Recovery Companion Prototype

**Status:** EXPERIMENTAL / CORE PRIMITIVES IMPLEMENTED / INTERFACE NOT IMPLEMENTED

## Goal

Turn the Recovery Companion concept into a small testable interface for one workflow:

`GitHub publishing for the aison repository`

The prototype should preserve four human recovery capabilities.

## 1. See What Happened

The human can see the major steps of the automated workflow.

Example:

```text
✓ Open repository
✓ Edit file
✓ Commit changes
→ Push
○ Verify result
```

### Success condition

A human can identify:

- what has already happened,
- what is happening now,
- and what remains.

Design example:

[`examples/recovery-companion-github-session.md`](../examples/recovery-companion-github-session.md)

Implementation:

`src/aison/recovery.py` can represent workflow step status and format steps into a human-readable progress view.

Status: `PRIMITIVE_IMPLEMENTED / INTERFACE_NOT_IMPLEMENTED`

---

## 2. Show Me How

The human can request simple manual instructions for any major step.

The explanation should be available on demand and should not interrupt normal automation.

### Success condition

For each major step, the system can show a human-readable manual path.

Design example:

[`examples/recovery-companion-show-me-how.md`](../examples/recovery-companion-show-me-how.md)

Implementation:

`RecoveryStep` can store an optional manual instruction, and the recovery module can retrieve it on demand.

Status: `PRIMITIVE_IMPLEMENTED / INTERFACE_NOT_IMPLEMENTED`

---

## 3. Take Over From Here

The human can stop automation at a safe checkpoint and continue manually.

### Success condition

A checkpoint clearly identifies:

- the current state,
- what has already changed,
- and the next manual action.

Design example:

[`examples/recovery-companion-take-over.md`](../examples/recovery-companion-take-over.md)

Implementation:

`RecoveryStep` can mark a step as a safe takeover checkpoint, and the recovery module can determine whether takeover is allowed.

Status: `PRIMITIVE_IMPLEMENTED / INTERFACE_NOT_IMPLEMENTED`

---

## 4. Start Again From Here

Human control should not depend on reacting faster than AI.

If automation has already finished or moved too quickly, the human should be able to return to a safe checkpoint and replay the workflow from there.

### Success condition

A previous checkpoint can be selected without silently losing the original history.

Design example:

[`examples/recovery-companion-start-again.md`](../examples/recovery-companion-start-again.md)

Implementation:

`RecoveryStep` can independently mark a checkpoint as replayable, and the recovery module can determine whether restart is allowed.

Replayability is intentionally separate from live takeover safety.

Status: `PRIMITIVE_IMPLEMENTED / INTERFACE_NOT_IMPLEMENTED`

---

## Existing Recovery Artifacts

Manual recovery already has two experimental artifacts:

- [`docs/runbooks/github-publish.md`](runbooks/github-publish.md)
- [`docs/recovery/github-publish-state.md`](recovery/github-publish-state.md)

These document the current manual fallback.

## Current Code

The first implementation lives in:

`src/aison/recovery.py`

Current tested primitives include:

- workflow step status,
- human-readable progress formatting,
- optional manual instructions,
- safe takeover checkpoints,
- replayable checkpoints.

Tests live in:

`tests/test_recovery_step.py`

The repository test workflow currently passes with these primitives.

## What Is Still Missing

The current code does **not** yet provide:

- a live Recovery Companion interface,
- an automated GitHub agent,
- real pause or takeover control,
- real checkpoint restoration,
- safe replay of external actions,
- persistent workflow history.

The current implementation is only the smallest code layer needed to explore those behaviours.

## Prototype Rule

Build one workflow first.

Do not generalise the design until the GitHub publishing prototype exposes what actually works, what is annoying, and what is missing.

Examples are not validation.

Passing tests show that the current code behaves as specified; they do not prove that the overall Recovery Companion concept works in real use.