# GitHub Publish Runbook

**Status:** EXPERIMENTAL

## Goal

Publish a small change to the `aison` repository without relying on an AI agent.

## Manual Path

1. Open the `aison` repository on GitHub.
2. Open the file you want to change.
3. Select **Edit this file**.
4. Make the change.
5. Select **Commit changes**.
6. Write a short commit message describing the change.
7. Commit directly to the current branch, unless a separate branch is required.
8. Confirm that the new commit appears in the repository.

## Recovery Check

If automation is unavailable, the human should still be able to:

- find this runbook,
- access the repository,
- edit a file,
- commit the change,
- and confirm that the change was published.

## Current Recovery Mode

`REPLICATE`

The manual fallback is to perform the GitHub publishing steps directly.