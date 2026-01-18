---
name: note-lookup
description: Search and retrieve notes by metadata, tags, or content. Use when finding specific notes in a collection, searching by frontmatter fields, or exploring notes by topic.
---

# Note Lookup

Search and retrieve notes from a collection.

## When This Triggers

- User wants to find a specific note
- User asks "what notes do I have about X?"
- User wants to search by tag, domain, or type
- User needs to explore their note collection

## Search Methods

### By Frontmatter Fields

Search notes by YAML frontmatter:

```bash
# Find all notes with specific type
python scripts/search_notes.py --type procedure

# Find notes in a domain
python scripts/search_notes.py --domain security

# Find notes with specific stability
python scripts/search_notes.py --stability high

# Combine filters
python scripts/search_notes.py --type reference --domain api
```

### By Tags

```bash
python scripts/search_notes.py --tag authentication
python scripts/search_notes.py --tag oauth --tag security
```

### By Content (grep)

```bash
# Simple content search
rg "OAuth" notes/

# Search with context
rg -C 3 "authentication flow" notes/

# Search only in specific file types
rg --type md "bearer token" notes/
```

### By Title/ID

```bash
# Find by ID pattern
python scripts/search_notes.py --id "auth-*"

# Find by title keyword
python scripts/search_notes.py --title "OAuth"
```

## Output Format

When presenting search results:

```markdown
## Found Notes

### 1. [Title](path/to/note.md)
- **ID**: note-id
- **Type**: procedure
- **Domain**: security, authentication
- **Tags**: oauth, tokens
- **Stability**: high

**Excerpt**: [relevant snippet]

### 2. [Title](path/to/another.md)
...
```

## Search Strategy

1. **Start broad**: Search by domain or type first
2. **Narrow down**: Add filters if too many results
3. **Content search**: Use grep for specific phrases
4. **Cross-reference**: Check related tags/domains

## Common Searches

### "What do I know about X?"

```bash
# Search domain
python scripts/search_notes.py --domain X

# Search tags
python scripts/search_notes.py --tag X

# Content search
rg -i "X" notes/
```

### "Find all procedures"

```bash
python scripts/search_notes.py --type procedure
```

### "What's stable/reliable?"

```bash
python scripts/search_notes.py --stability high --confidence high
```

### "What needs review?"

```bash
python scripts/search_notes.py --stability low
python scripts/search_notes.py --confidence low
```

## Manual Search

If scripts aren't available, use standard tools:

```bash
# Find all notes with frontmatter field
rg "^type: procedure" notes/ -l

# Find by tag in frontmatter
rg "^\s+- oauth" notes/ -l

# Find by domain
rg "^domain:.*security" notes/ -l
```

## Rules

- Do NOT hallucinate notes that don't exist
- If no notes match, say so clearly
- Surface conflicts if notes disagree
- Include paths so user can open them

## See Also

`scripts/search_notes.py` for the search implementation.
