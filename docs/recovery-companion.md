# Recovery Companion

**Status:** CONCEPT / EXPERIMENTAL / NOT VALIDATED

## Problem

AI automation can become faster than human attention.

A human may still technically remain "in control" while no longer understanding:

- what the AI just did,
- where the workflow currently is,
- how to continue manually,
- or how to recover when automation fails.

Human control should not depend on reacting faster than AI.

## Value

AISØN should preserve human judgment and recovery paths even when routine work is delegated.

Automation may remove work.

It should not make the manual path invisible.

## Hypothesis

A lightweight recovery interface may help preserve human control without forcing continuous training.

For important automated workflows, the system could keep four actions available:

### 1. See what happened

Show the workflow as understandable steps.

```text
✓ Open repository
✓ Edit README
✓ Commit changes
→ Push
○ Verify result
```

### 2. Show me how

Explain how the human could perform the current step manually.

This should be available on demand rather than interrupting normal automation.

### 3. Take over from here

Allow the human to stop automation and continue manually from the current checkpoint.

### 4. Start again from here

AI may finish too quickly for a human to interrupt it.

The human should therefore be able to return to a safe checkpoint and replay the workflow manually from that point.

## Learn Once, Then Automate

For some persistently delegated capabilities, AISØN may optionally offer a short manual walkthrough before full automation.

Example:

```text
learn basic GitHub publish path
↓
perform it once
↓
automation enabled
↓
manual instructions remain available
```

This is not intended as a permanent training requirement.

Human final authority remains higher priority than pedagogy.

A user may explicitly waive the walkthrough.

## Recovery Is Not Always Manual Replication

Recovery does not always mean doing the AI's job by hand.

Depending on the workflow, the correct recovery mode may be:

- `REPLICATE` — perform the task manually
- `HALT` — stop safely
- `ROLLBACK` — undo the action
- `SWITCH` — use another tool, system, or person
- `WAIT` — take no action until conditions change
- `ESCALATE` — hand control to another human

The recovery mode should match the actual risk.

## Current Design Principle

> **Automation should never make the manual path invisible.**

And:

> **Human control should not depend on reacting faster than AI.**

## First Prototype

Test one capability only:

`GitHub publishing for the aison repository`

Prototype questions:

- Can the human see every major step?
- Can the human ask how a step would be done manually?
- Can the human take over?
- Can the human restart from a previous checkpoint?
- Is the documented recovery path actually usable?

### Prototype Artifacts

The first experimental recovery path is now documented:

- Runbook: [`docs/runbooks/github-publish.md`](runbooks/github-publish.md)
- Recovery state: [`docs/recovery/github-publish-state.md`](recovery/github-publish-state.md)

This connects the concept to one manually demonstrated recovery path.

The prototype remains experimental and does not yet establish that the recovery path will remain usable over time.

## What This Does Not Claim

This concept does **not** currently claim that:

- one manual demonstration permanently preserves skill,
- every automated task requires training,
- human capability can be reduced to a score,
- this approach has been validated,
- or this framing is unique to AISØN.

The first goal is simply to test whether automation can remain convenient while keeping recovery understandable and reachable.