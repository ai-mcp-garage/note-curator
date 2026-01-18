---
name: note-capture
description: Capture and structure raw input into a well-organized markdown note. Use when ingesting new information, cleaning up rough notes, or creating structured documents from unstructured sources.
---

# Note Capture

Capture raw, unstructured input and structure it into a well-organized markdown note.

## When This Triggers

- User has raw information to capture
- User wants to structure messy input
- User asks to "capture", "ingest", or "create a note" from something
- User needs to turn unstructured content into a proper note

## Output Format

A **single markdown note** with YAML frontmatter and logical sections:

```markdown
---
id: <stable-slug-or-uuid>
title: <clear, human-readable title>
type: <concept | procedure | reference | guide | narrative>
scope: <work | home | health | creative | tooling | mixed>
domain: [list, of, domains]
stability: <low | medium | high>
intent: <inform | guide | enforce | recall>
tags:
  - lowercase
  - freeform
source: <optional: memory | doc | conversation | link>
confidence: <low | medium | high>
---

# Title

## Section 1
<content>

## Section 2
<content>
```

## Consolidation Rules

- **One note per input**, regardless of how many ideas are present
- Use **headings** (##, ###) to separate topics
- Use **bullet points** for lists of related items
- Keep related examples and context with their parent topic
- Preserve the logical flow of the original content

## Writing Rules

- Prefer declarative statements
- Avoid imperative language unless describing a procedure
- Preserve nuance and uncertainty
- Do NOT invent facts
- Do NOT over-summarize — this is **loss-minimizing**

## Frontmatter Fields

### type
- `concept`: explanation or mental model
- `procedure`: step-by-step actions
- `reference`: consolidated information for lookup
- `guide`: multi-part instructional content
- `narrative`: memory or story
- `checklist`: verification items
- `heuristic`: rule-of-thumb

### stability
- `high`: unlikely to change
- `medium`: context-dependent
- `low`: exploratory or personal

### intent
- `inform`: knowledge transfer
- `guide`: influence thinking
- `enforce`: invariant or rule
- `recall`: memory aid

## Process

1. Read all input
2. Identify the core topic or theme
3. Group related information into sections
4. Draft frontmatter based on content
5. Write sections with appropriate headings
6. Review for completeness — nothing should be lost

## When to Use This vs note-planner

- **Use note-capture** when you know you want one note from the input
- **Use note-planner** when you need to plan how to organize content first

## Non-Goals

- Do NOT split into multiple notes
- Do NOT decide how this note will be used later
- Do NOT optimize for agents yet

This creates a coherent reference document, not scattered fragments.

## See Also

`references/frontmatter-schema.md` for field specifications.
