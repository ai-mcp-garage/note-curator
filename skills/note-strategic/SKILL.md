---
name: note-strategic
description: Strategic planning for note organization. Use when you have a large amount of content and need to plan how to structure it before condensing. Proposes note breakdowns and organization strategies.
---

# Note Strategic

Architect mode for planning note structure before condensing.

## When This Triggers

- User has a lot of content and isn't sure how to organize it
- User asks "how should I structure this?"
- User wants to plan before condensing
- User needs help deciding what becomes one note vs multiple

## Purpose

Unlike note-capture (which just creates one note), this skill helps you **think through** how content should be organized:

- What are the distinct topics?
- What should be combined vs kept separate?
- What's the right level of granularity?
- How will this be used later?

## Process

### 1. Analyze the Input

Read through all content and identify:
- **Core topics**: What distinct subjects are present?
- **Relationships**: How do topics connect?
- **Audiences**: Who will use this information?
- **Use cases**: How will it be retrieved/used?

### 2. Propose Structure Options

Present 2-3 organizational approaches:

**Option A: Single Document**
- When content is tightly related
- When it will be used together
- When splitting would lose context

**Option B: Topic-Based Split**
- When there are distinct subjects
- When different audiences need different parts
- When topics have different stability

**Option C: Use-Case Split**
- When same info serves different purposes
- When retrieval patterns differ
- When update frequencies differ

### 3. Recommend with Reasoning

For each proposed note, explain:
- What it would contain
- Why it's grouped this way
- Suggested frontmatter (type, stability, intent)
- How it relates to other notes

### 4. Get User Input

This is collaborative. Ask:
- Does this grouping make sense?
- Are there relationships I'm missing?
- How do you expect to use these notes?

## Output Format

```markdown
## Analysis

[Summary of what's in the input]

## Proposed Structure

### Option A: [Name]

**Notes:**
1. **[Note title]**
   - Contains: [what goes here]
   - Type: [concept/procedure/reference/etc.]
   - Why: [reasoning]

2. **[Note title]**
   - Contains: [what goes here]
   - Type: [type]
   - Why: [reasoning]

### Option B: [Name]

[Alternative structure with reasoning]

## Recommendation

[Which option and why]

## Questions

- [Clarifying questions for user]
```

## Heuristics for Splitting

**Combine when:**
- Topics are always used together
- Splitting would require duplicating context
- Content is short (<500 lines combined)
- Same audience and use case

**Split when:**
- Topics have different stability levels
- Different audiences need different parts
- Content would exceed ~500 lines
- Topics change independently
- Different retrieval patterns

## What This Is NOT

- This is not atomization (splitting everything into tiny pieces)
- This is not automatic — it's a planning discussion
- This doesn't create notes — that's note-condense's job

## Workflow

1. Run **note-strategic** to plan structure
2. Discuss and refine with user
3. Run **note-capture** for each agreed note

## See Also

`references/planning-heuristics.md` for detailed decision criteria.
