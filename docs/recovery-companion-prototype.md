# Recovery Companion Prototype

**Status:** EXPERIMENTAL / SESSION-LEVEL PRIMITIVES IMPLEMENTED / LIVE INTERFACE NOT IMPLEMENTED

## Goal

Turn the Recovery Companion concept into a small testable recovery layer for one workflow:

`GitHub publishing for the aison repository`

The prototype explores four human recovery capabilities:

1. See what happened.
2. Show me how.
3. Take over from here.
4. Start again from here.

The goal is not to make the human faster than automation.

The goal is to preserve a usable recovery path when automation is faster than the human.

> Automation should never make the manual path invisible.

> Human control should not depend on reacting faster than AI.

---

## 1. See What Happened

The human can see the major steps of an automated workflow.

Example:

```text
✓ Open repository
✓ Edit file
→ Commit changes
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

`RecoveryStep` represents individual workflow steps.

`RecoverySession` groups those steps into one recovery-aware workflow session.

`format_recovery_steps()` provides a human-readable progress view.

`current_step()` identifies the active step when one exists.

Status:

`SESSION_PRIMITIVE_IMPLEMENTED / LIVE_INTERFACE_NOT_IMPLEMENTED`

---

## 2. Show Me How

The human can request simple manual instructions for a major workflow step.

The explanation should be available on demand and should not interrupt normal automation.

### Success condition

For each major step, the system can expose a human-readable manual path when one has been defined.

Design example:

[`examples/recovery-companion-show-me-how.md`](../examples/recovery-companion-show-me-how.md)

Implementation:

`RecoveryStep` can store an optional manual instruction.

`show_manual_instruction()` retrieves that instruction without inventing one when none exists.

Status:

`PRIMITIVE_IMPLEMENTED / LIVE_INTERFACE_NOT_IMPLEMENTED`

---

## 3. Take Over From Here

The human can continue manually from a safe checkpoint.

Takeover safety is explicit.

It is not inferred merely because a step exists.

### Success condition

A recovery session can identify the most recent checkpoint that:

- has already been reached,
- is explicitly marked safe for takeover,
- and is not merely a future pending step.

Design example:

[`examples/recovery-companion-take-over.md`](../examples/recovery-companion-take-over.md)

Implementation:

`RecoveryStep.safe_checkpoint` records whether a step is safe for takeover.

`can_take_over()` evaluates an individual step.

`latest_takeover_checkpoint()` searches the session for the most recent reached safe checkpoint.

Status:

`SESSION_PRIMITIVE_IMPLEMENTED / REAL_PAUSE_CONTROL_NOT_IMPLEMENTED`

---

## 4. Start Again From Here

Human control should not depend on reacting faster than AI.

If automation has already completed or moved beyond the point where live takeover is possible, the human may need a separate recovery path:

return to a known checkpoint and safely replay from there.

Restart is intentionally different from rollback.

A restart should preserve the original history rather than pretending the earlier execution never happened.

### Success condition

A recovery session can identify the most recent checkpoint that:

- has already been reached,
- is explicitly marked replayable,
- and is not merely a future pending step.

Design example:

[`examples/recovery-companion-start-again.md`](../examples/recovery-companion-start-again.md)

Implementation:

`RecoveryStep.replayable_checkpoint` records whether a step may be used as a restart point.

`can_start_again()` evaluates an individual step.

`latest_restart_checkpoint()` searches the session for the most recent reached replayable checkpoint.

Replayability and live takeover safety are intentionally independent.

A checkpoint may be:

- safe for takeover but not replayable,
- replayable but not safe for live takeover,
- both,
- or neither.

Status:

`SESSION_PRIMITIVE_IMPLEMENTED / REAL_REPLAY_ENGINE_NOT_IMPLEMENTED`

---

## Recovery Session Model

The current implementation introduces:

```text
RecoverySession
    capability
    steps
```

A session groups recovery information around one automated capability.

For the current prototype:

```text
capability = github_publish_aison
```

This allows recovery logic to reason about the workflow as a sequence rather than treating every step as an isolated object.

Current session-level operations include:

- find the active step,
- find the latest reached safe takeover checkpoint,
- find the latest reached replayable checkpoint.

---

## Existing Recovery Artifacts

Manual recovery already has two experimental artifacts:

- [`docs/runbooks/github-publish.md`](runbooks/github-publish.md)
- [`docs/recovery/github-publish-state.md`](recovery/github-publish-state.md)

These document the current manual fallback and recovery state.

---

## Current Code

The implementation lives in:

`src/aison/recovery.py`

Current tested primitives include:

- workflow step status,
- human-readable progress formatting,
- optional manual instructions,
- safe takeover checkpoints,
- replayable checkpoints,
- recovery session grouping,
- active-step lookup,
- latest reached takeover checkpoint lookup,
- latest reached restart checkpoint lookup,
- independence between takeover and restart semantics.

Tests live in:

`tests/test_recovery_step.py`

The repository test workflow currently passes with these primitives.

---

## What Is Still Missing

The current code does **not** yet provide:

- a live Recovery Companion user interface,
- an automated GitHub agent,
- real pause or takeover control,
- real checkpoint restoration,
- safe replay of external side effects,
- persistent recovery history,
- external-system state verification,
- crash recovery,
- multi-agent recovery coordination.

Those are later implementation problems.

The current prototype is deliberately smaller.

It establishes the recovery semantics before building machinery around them.

---

## Current Prototype Result

The prototype now demonstrates a minimal recovery model in which automation can expose:

```text
What happened?
How would I do this manually?
Where can I safely take over?
Where can I safely start again?
```

The current implementation does not prove that Recovery Companion works in real-world agent systems.

It does show that these four recovery questions can be represented separately rather than collapsed into a single generic "undo" or "human override" control.

That distinction is the main result of this prototype phase.

---

## Prototype Rule

Build one workflow first.

Do not generalise the design until the GitHub publishing prototype exposes what actually works, what is annoying, and what is missing.

Examples are not validation.

Passing tests show that the current code behaves as specified.

They do not prove that the overall Recovery Companion concept works in real use.

**Status remains experimental.**