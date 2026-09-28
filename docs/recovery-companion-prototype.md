# Recovery Companion Prototype

**Status:** EXPERIMENTAL / NOT IMPLEMENTED

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

Status: `TODO`

---

## 2. Show Me How

The human can request simple manual instructions for any major step.

The explanation should be available on demand and should not interrupt normal automation.

### Success condition

For each major step, the system can show a human-readable manual path.

Status: `TODO`

---

## 3. Take Over From Here

The human can stop automation at a safe checkpoint and continue manually.

### Success condition

A checkpoint clearly identifies:

- the current state,
- what has already changed,
- and the next manual action.

Status: `TODO`

---

## 4. Start Again From Here

Human control should not depend on reacting faster than AI.

If automation has already finished or moved too quickly, the human should be able to return to a safe checkpoint and replay the workflow from there.

### Success condition

A previous checkpoint can be selected without silently losing the original history.

Status: `TODO`

---

## Existing Recovery Artifacts

Manual recovery already has two experimental artifacts:

- [`docs/runbooks/github-publish.md`](runbooks/github-publish.md)
- [`docs/recovery/github-publish-state.md`](recovery/github-publish-state.md)

These document the current manual fallback.

They do not yet implement the Recovery Companion interface.

## Prototype Rule

Build one workflow first.

Do not generalise the design until the GitHub publishing prototype exposes what actually works, what is annoying, and what is missing.