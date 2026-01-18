# Frontmatter Schema Reference

Complete specification for note YAML frontmatter.

## Required Fields

### id

Stable identifier for the note.

```yaml
id: my-note-slug
```

- Use kebab-case slugs or UUIDs
- Should be stable (don't change once set)
- Used for cross-references

### title

Human-readable title.

```yaml
title: "How Authentication Works in Our System"
```

- Clear and descriptive
- Can include punctuation
- Should make sense standalone

## Classification Fields

### type

What kind of content this is:

| Value | Description | Example |
|-------|-------------|---------|
| `concept` | Explanation or mental model | "What is OAuth?" |
| `heuristic` | Rule-of-thumb | "When to use caching" |
| `procedure` | Step-by-step actions | "How to deploy" |
| `checklist` | Verification items | "PR review checklist" |
| `reference` | Consolidated lookup info | "API endpoints" |
| `narrative` | Memory or story | "Why we chose React" |
| `guide` | Multi-part instructional | "Getting started" |
| `tool` | Tool documentation | "Using the CLI" |

### scope

Life domain this applies to:

| Value | Description |
|-------|-------------|
| `work` | Professional/job-related |
| `home` | Personal/household |
| `health` | Physical/mental health |
| `creative` | Art, writing, music |
| `tooling` | Developer tools |
| `mixed` | Multiple domains |

### domain

Short list of topic areas:

```yaml
domain: [security, authentication, oauth]
```

- Use lowercase
- Be specific but not too narrow
- 2-5 domains is typical

### stability

How likely this is to change:

| Value | Description |
|-------|-------------|
| `high` | Unlikely to change, foundational |
| `medium` | Context-dependent, may evolve |
| `low` | Exploratory, personal, draft |

### intent

What the note is meant to do:

| Value | Description |
|-------|-------------|
| `inform` | Transfer knowledge |
| `guide` | Influence thinking/decisions |
| `enforce` | State invariants or rules |
| `recall` | Aid memory |

## Optional Fields

### tags

Freeform classification:

```yaml
tags:
  - authentication
  - security
  - best-practices
```

- Lowercase
- Can overlap with domain
- Good for cross-cutting concerns

### source

Where the information came from:

| Value | Description |
|-------|-------------|
| `memory` | Personal recollection |
| `doc` | Documentation |
| `conversation` | Discussion/meeting |
| `link` | External URL |

### confidence

How confident you are in accuracy:

| Value | Description |
|-------|-------------|
| `high` | Verified, well-established |
| `medium` | Probably correct, some uncertainty |
| `low` | Speculative, needs verification |

## Complete Example

```yaml
---
id: oauth-flow-overview
title: "OAuth 2.0 Authorization Flow"
type: concept
scope: work
domain: [security, authentication, api]
stability: high
intent: inform
tags:
  - oauth
  - authorization
  - tokens
source: doc
confidence: high
---
```

## Validation Rules

- `id`: required, non-empty string
- `title`: required, non-empty string
- `type`: required, must be from allowed list
- `scope`: required, must be from allowed list
- `domain`: required, array of strings
- `stability`: required, must be low/medium/high
- `intent`: required, must be from allowed list
- `tags`: optional, array of lowercase strings
- `source`: optional, must be from allowed list if present
- `confidence`: optional, must be low/medium/high if present
