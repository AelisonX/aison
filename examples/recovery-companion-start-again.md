# Recovery Companion — Start Again From Here Example

**Status:** EXAMPLE / EXPERIMENTAL

This file demonstrates how a human could restart an automated workflow from an earlier safe checkpoint.

It is not yet a live interface.

## Capability

`github_publish_aison`

## Principle

Human control should not depend on reacting faster than AI.

If automation has already moved past a useful takeover point, the human should be able to return to an earlier safe checkpoint and replay the workflow from there.

## Example Workflow

Automation has already completed:

```text
✓ Open repository
✓ Open target file
✓ Replace file content
✓ Review change
✓ Commit change
✓ Verify published result
```

The human later decides:

```text
START_AGAIN_FROM_HERE
```

Selected checkpoint:

```text
REVIEW_CHANGE
```

## Recovery Companion Response

Before restarting, the system should show:

```text
Selected checkpoint:
REVIEW_CHANGE

Original workflow:
PRESERVED

Completed after this checkpoint:
- Commit change
- Verify published result

Restart mode:
SAFE_REPLAY

Next action:
Recreate a safe working state from REVIEW_CHANGE.
```

## Replay Behaviour

A restart should not silently erase the original history.

The system should preserve:

- what originally happened,
- which checkpoint was selected,
- which later steps had already occurred,
- why the replay was started,
- and which version is now considered active.

## Example

```text
Original session:
COMPLETED

Replay requested from:
REVIEW_CHANGE

[ Show original history ]
[ Start safe replay ]
[ Cancel ]
```

If replay begins:

```text
Replay session created.

✓ Open repository
✓ Open target file
✓ Restore checkpoint state
→ Review change
○ Commit change
○ Verify published result
```

## Important Distinction

`START_AGAIN_FROM_HERE` is not the same as `ROLLBACK`.

`ROLLBACK` attempts to undo an earlier action.

`START_AGAIN_FROM_HERE` creates a new attempt from a known checkpoint while preserving the original history.

## Restart Rules

`START_AGAIN_FROM_HERE` should:

- preserve the original workflow record,
- identify the selected checkpoint,
- recreate a safe state where possible,
- avoid silently overwriting later work,
- make the replay distinguishable from the original run.

## When Restart Is Not Safe

Some workflows cannot be safely replayed from an earlier point.

Example:

```text
Checkpoint:
PAYMENT_SUBMITTED

Replay availability:
NOT SAFE

Reason:
The external action may already have irreversible effects.
```

In those cases, the Recovery Companion should recommend another recovery mode such as:

- `HALT`
- `ROLLBACK`
- `WAIT`
- `ESCALATE`

## What This Tests

This example explores whether human control can remain meaningful even after automation has already finished.

It does not assume that every workflow is replayable.

It tests whether safe replay can be separated from rollback and from live takeover.

## Prototype Question

Can the human return to an earlier decision point without erasing what already happened?

This example represents the fourth Recovery Companion behaviour:

> Start again from here.