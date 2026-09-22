# Transformation Ledger

A small experimental example for tracking how information changes as it passes through a sequence of transformations.

The core question is:

> When information passes through multiple transforming interfaces, what is preserved, altered, lost, or introduced?

## Why this exists

Provenance tells us where information came from.

A Transformation Ledger asks a different question:

> What happened to the information along the way?

This example represents a transformation pipeline as:

```text
INPUT
  ↓
INTERFACE
  ↓
TRANSFORMATION
  ↓
OUTPUT