# Recovery Companion — Take Over From Here Example

**Status:** EXAMPLE / EXPERIMENTAL

This file demonstrates how a human could take over an automated workflow from a safe checkpoint.

It is not yet a live interface.

## Capability

`github_publish_aison`

## Principle

Human control should remain available even when automation is already in progress.

A takeover should happen from a known checkpoint with clear context.

## Example Workflow

```text
✓ Open repository
✓ Open target file
✓ Replace file content
→ Review change
○ Commit change
○ Verify published result
```

Current checkpoint:

```text
REVIEW_CHANGE
```

Human selects:

```text
TAKE_OVER_FROM_HERE
```

## Recovery Companion Response

Before handing control back, the system should show:

```text
Repository:
AelisonX/aison

Target file:
docs/recovery-companion.md

Completed:
- Open repository
- Open target file
- Replace file content

Current checkpoint:
REVIEW_CHANGE

Next manual action:
Review the proposed file content before committing.
```

## Manual Continuation

The human can now continue manually:

1. Review the file content.
2. Check that the intended changes are correct.
3. Select **Commit changes**.
4. Enter a commit message.
5. Confirm the commit.
6. Verify that the published result is correct.

## Takeover Rules

`TAKE_OVER_FROM_HERE` should:

- stop further automation at a safe checkpoint,
- preserve the current state,
- show what has already happened,
- show the next manual action,
- avoid repeating completed steps unless requested,
- avoid hiding changes that occurred before takeover.

## Unsafe Takeover

A takeover should not pretend to be safe if the current step cannot be paused cleanly.

Example:

```text
Current step:
EXTERNAL_ACTION_IN_PROGRESS

Takeover availability:
NOT SAFE YET
```

The system should instead move to the nearest safe checkpoint before handing control back.

## Example Interface

```text
Automation status:

✓ Open repository
✓ Open target file
✓ Replace file content
→ Review change
○ Commit change
○ Verify published result

[ Show me how ]
[ Take over from here ]
```

If selected:

```text
Automation paused at:
REVIEW_CHANGE

You are now in control.

Next action:
Review the proposed change.
```

## What This Tests

This example tests whether human control can remain meaningful during automation without requiring the human to perform every step manually.

It does not prove that every workflow can be safely interrupted.

It tests whether takeover can be defined around explicit safe checkpoints.

## Prototype Question

Can a human regain control without losing context?

This example represents the third Recovery Companion behaviour:

> Take over from here.