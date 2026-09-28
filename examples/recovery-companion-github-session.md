# Recovery Companion — GitHub Session Example

**Status:** EXAMPLE / EXPERIMENTAL

This file shows what a human-readable automated workflow could look like.

It is not yet a live interface.

## Workflow

Capability:

`github_publish_aison`

Goal:

Publish a documentation update to the `aison` repository.

## Current Session

```text
✓ Open repository
✓ Open target file
✓ Replace file content
✓ Review change
✓ Commit change
→ Verify published result
```

## Step Details

### 1. Open repository

Status: `COMPLETED`

Human-readable action:

Open the `AelisonX/aison` repository.

Manual equivalent:

Navigate to the repository through GitHub.

---

### 2. Open target file

Status: `COMPLETED`

Human-readable action:

Open the file that needs to be changed.

Manual equivalent:

Select the file from the repository and choose the edit action.

---

### 3. Replace file content

Status: `COMPLETED`

Human-readable action:

Replace the existing file with the prepared full-file version.

Manual equivalent:

Select all existing content, replace it with the new version, and review the result.

---

### 4. Review change

Status: `COMPLETED`

Human-readable action:

Check that the intended file and content are correct before committing.

Manual equivalent:

Use the GitHub preview or diff to review the change.

---

### 5. Commit change

Status: `COMPLETED`

Human-readable action:

Create a commit describing the update.

Manual equivalent:

Enter the commit message and confirm the commit.

---

### 6. Verify published result

Status: `IN_PROGRESS`

Human-readable action:

Confirm that the new commit and file content appear in the repository.

Manual equivalent:

Return to the repository, open the file, and confirm the latest version is visible.

## Recovery Actions

At a safe checkpoint, a Recovery Companion could expose:

- `SHOW_ME_HOW`
- `TAKE_OVER_FROM_HERE`
- `START_AGAIN_FROM_HERE`

Example:

```text
Current checkpoint: VERIFY_PUBLISHED_RESULT

[ Show me how ]
[ Take over from here ]
[ Start again from Review change ]
```

## Why This Example Exists

The goal is not to prove that the Recovery Companion works.

The goal is to make the proposed interaction concrete enough to inspect, criticise, and eventually implement.

This example represents the first step toward:

> See what happened.