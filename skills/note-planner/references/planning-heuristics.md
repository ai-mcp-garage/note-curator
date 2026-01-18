# Note Planning Heuristics

Decision criteria for organizing content into notes.

## Core Questions

Before structuring, ask:

1. **Who uses this?** — Same person? Different teams?
2. **How is it found?** — Search? Browse? Reference?
3. **When does it change?** — Stable? Evolving? Volatile?
4. **What's the context?** — Standalone? Part of a flow?

## Combination Indicators

Signs that content should be ONE note:

### Tight Coupling
- Understanding A requires understanding B
- Examples in A reference concepts from B
- Splitting would require duplicating context

### Same Lifecycle
- Content changes together
- Same author/owner
- Same update frequency

### Single Retrieval
- Always looked up together
- Same search terms would find both
- One use case

### Manageable Size
- Combined content < 500 lines
- Fits comfortably in one read
- Not overwhelming

## Separation Indicators

Signs that content should be MULTIPLE notes:

### Different Stability

| Content A | Content B | Action |
|-----------|-----------|--------|
| High stability | Low stability | Split |
| Foundational | Exploratory | Split |
| Documented | Personal notes | Split |

### Different Audiences

| Audience A | Audience B | Action |
|------------|------------|--------|
| Developers | Designers | Split |
| New hires | Veterans | Split |
| Internal | External | Split |

### Independent Changes
- A can be updated without touching B
- Different owners
- Different review processes

### Different Types

| Type A | Type B | Often Split? |
|--------|--------|--------------|
| Concept | Procedure | Yes |
| Reference | Narrative | Yes |
| Checklist | Guide | Sometimes |

### Size Concerns
- Combined > 500 lines
- Too much to absorb in one read
- Distinct logical sections

## Granularity Spectrum

```
Too Fine ←――――――――――――――――――→ Too Coarse
   ↓                              ↓
One idea per note          Everything in one note
Hard to find context       Hard to find anything
Lots of cross-references   Wall of text
```

**Sweet spot**: Notes that are self-contained but focused. A reader should be able to understand the note without reading 5 others, but shouldn't have to wade through unrelated content.

## Common Patterns

### The Reference Split

One concept explanation + one quick reference:
- `oauth-explained.md` — What OAuth is, how it works
- `oauth-reference.md` — Endpoints, token formats, error codes

### The Audience Split

Same topic, different depths:
- `auth-overview.md` — For new team members
- `auth-implementation.md` — For developers building it

### The Stability Split

Core + evolving:
- `api-design-principles.md` — Stable guidelines
- `api-current-endpoints.md` — Updated as API changes

### The Type Split

Different note types for different purposes:
- `deployment-guide.md` — Procedure (how to do it)
- `deployment-checklist.md` — Checklist (verify it's done)
- `deployment-troubleshooting.md` — Reference (when things break)

## Anti-Patterns

### Over-Atomization
Splitting everything into tiny notes:
- Hard to get context
- Lots of duplication
- Navigation overhead

### Kitchen Sink
One note with everything:
- Hard to find specific info
- Unclear what it's about
- Intimidating to read

### Arbitrary Splits
Splitting by arbitrary criteria (alphabetical, date created):
- No logical grouping
- Doesn't match how content is used

## Decision Framework

```
1. Can this be understood standalone?
   No → Probably combine with related content
   Yes → Continue

2. Is it < 500 lines combined with related content?
   Yes → Consider combining
   No → Continue

3. Do parts change at different rates?
   Yes → Split by stability
   No → Continue

4. Do different audiences need different parts?
   Yes → Split by audience
   No → Probably keep together
```

## When in Doubt

- Err toward fewer, larger notes
- You can always split later
- Splitting is harder to undo than combining
- Context is valuable — don't fragment it unnecessarily
