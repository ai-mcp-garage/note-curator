# Note Curator

Skills for capturing, organizing, and retrieving structured notes with YAML frontmatter.

## Skills

| Skill | Purpose |
|-------|---------|
| **note-capture** | Capture raw input into a structured note |
| **note-planner** | Plan how to organize content before capturing |
| **note-lookup** | Search notes by metadata, tags, or content |

## Workflow

```
Raw Input
    ↓
note-planner (plan structure, if needed)
    ↓
note-capture (create structured note)
    ↓
note-lookup (find it later)
```

## Note Format

Notes use YAML frontmatter for structured metadata:

```markdown
---
id: my-note-id
title: "Human Readable Title"
type: concept | procedure | reference | guide | narrative
scope: work | home | health | creative | tooling | mixed
domain: [list, of, domains]
stability: low | medium | high
intent: inform | guide | enforce | recall
tags:
  - lowercase
  - freeform
confidence: low | medium | high
---

# Content

The actual note content with sections...
```

## What Each Does

### note-capture

Takes raw, unstructured input and creates a well-organized note:
- Assigns appropriate frontmatter
- Structures content with headings
- Preserves all information (loss-minimizing)

### note-planner

Planning mode for when you're not sure how to organize:
- Analyzes input for distinct topics
- Proposes structure options
- Helps decide single note vs multiple
- Collaborative discussion before capturing

### note-lookup

Find notes in your collection:
- Search by frontmatter fields (type, domain, stability)
- Search by tags
- Content search via grep
- Outputs structured results

## Installation

```bash
# Cursor
cp -r skills/* ~/.cursor/skills/

# Claude Code
cp -r skills/* ~/.claude/skills/

# Codex
cp -r skills/* ~/.codex/skills/

# Roo
cp -r skills/* ~/.roo/skills/
```

## Structure

```
skills/
├── note-capture/
│   ├── SKILL.md
│   └── references/
│       └── frontmatter-schema.md
├── note-planner/
│   ├── SKILL.md
│   └── references/
│       └── planning-heuristics.md
└── note-lookup/
    ├── SKILL.md
    └── scripts/
        └── search_notes.py
```

## Dependencies

The `search_notes.py` script requires PyYAML:

```bash
pip install pyyaml
```
