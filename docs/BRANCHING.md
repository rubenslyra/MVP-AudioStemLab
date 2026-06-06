# Branching Strategy

This repository uses a simple release-oriented workflow.

## Branches

### `main`

Stable production branch.

Use `main` only for:

- released application versions;
- production-ready documentation;
- release notes;
- packaging metadata;
- important files required by end users;
- tagged release states.

Every public release must be tagged from `main`.

Examples:

```text
v0.3.5
v0.4.0
v1.0.0
```

### `develop`

Active development branch.

Use `develop` for:

- new features;
- bug fixes before release;
- build pipeline changes under validation;
- UI/UX experiments;
- dependency changes;
- packaging experiments;
- documentation drafts.

When `develop` is stable and tested, merge it into `main` and create a new release tag.

## Release Flow

1. Work on `develop`.
2. Run tests.
3. Validate packaging workflow.
4. Merge `develop` into `main`.
5. Update `VERSION`, `CHANGELOG.md`, and release notes.
6. Create an annotated tag from `main`.
7. Push `main` and the tag.

## Current Stable Release

```text
v0.3.5
```

## Current Development Line

```text
develop
```
