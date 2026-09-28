# Recovery Companion — Show Me How Example

**Status:** EXAMPLE / EXPERIMENTAL

This file demonstrates how an automated workflow could expose a human-readable manual path on demand.

It is not yet a live interface.

## Capability

`github_publish_aison`

## Principle

Automation should not require the human to remember every step.

It should keep a manual path available when requested.

## Example Interaction

Current automated step:

```text
COMMIT_CHANGE
```

Human selects:

```text
SHOW_ME_HOW
```

Recovery Companion responds:

### How to do this step manually

1. Review the file changes.
2. Select **Commit changes**.
3. Enter a short commit message describing what changed.
4. Add an optional description if useful.
5. Confirm the commit.
6. Return to the repository and verify that the new commit appears.

## Context

The automated workflow may already know:

```text
repository: AelisonX/aison
target_file: docs/recovery-companion.md
current_step: COMMIT_CHANGE
previous_step: REVIEW_CHANGE
next_step: VERIFY_PUBLISHED_RESULT
```

The human does not need to reconstruct that context from memory.

The explanation should describe the manual equivalent of the current step.

## Design Behaviour

`SHOW_ME_HOW` should:

- explain only the relevant step,
- use simple language,
- preserve the current workflow context,
- avoid interrupting automation unless requested,
- avoid turning every task into a lesson.

## Example

```text
Automation status:

✓ Open repository
✓ Open target file
✓ Replace file content
✓ Review change
→ Commit change
○ Verify published result

Need the manual path?

[ Show me how ]
```

If selected:

```text
Commit change manually:

1. Select "Commit changes".
2. Write a short commit message.
3. Confirm the commit.
4. Check that the new commit appears in the repository.
```

## What This Tests

This example explores whether a user can recover understanding without being forced to study the full workflow every time.

It does not test long-term skill retention.

It tests whether the manual path remains visible and reachable.

## Prototype Question

Can automation remain fast while manual understanding stays one action away?

This example represents the second Recovery Companion behaviour:

> Show me how.