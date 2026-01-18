#!/usr/bin/env python3
"""
Note Search - Find notes by frontmatter metadata

Usage:
    search_notes.py [options] <notes_directory>

Options:
    --type TYPE         Filter by note type
    --domain DOMAIN     Filter by domain (can repeat)
    --tag TAG           Filter by tag (can repeat)
    --stability LEVEL   Filter by stability (low/medium/high)
    --confidence LEVEL  Filter by confidence (low/medium/high)
    --scope SCOPE       Filter by scope
    --intent INTENT     Filter by intent
    --id PATTERN        Filter by ID (supports * wildcards)
    --title KEYWORD     Filter by title keyword (case-insensitive)
    --json              Output as JSON

Examples:
    search_notes.py notes/
    search_notes.py --type procedure notes/
    search_notes.py --domain security --tag oauth notes/
    search_notes.py --stability high --confidence high notes/
"""

import sys
import re
import json
import fnmatch
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None
    
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def matches_filter(note, filters):
    """Check if a note matches all filters."""
    fm = note['frontmatter']
    
    if filters.get('type') and fm.get('type') != filters['type']:
        return False
    
    if filters.get('domains'):
        note_domains = fm.get('domain', [])
        if isinstance(note_domains, str):
            note_domains = [note_domains]
        if not any(d in note_domains for d in filters['domains']):
            return False
    
    if filters.get('tags'):
        note_tags = fm.get('tags', [])
        if not any(t in note_tags for t in filters['tags']):
            return False
    
    if filters.get('stability') and fm.get('stability') != filters['stability']:
        return False
    
    if filters.get('confidence') and fm.get('confidence') != filters['confidence']:
        return False
    
    if filters.get('scope') and fm.get('scope') != filters['scope']:
        return False
    
    if filters.get('intent') and fm.get('intent') != filters['intent']:
        return False
    
    if filters.get('id_pattern'):
        note_id = fm.get('id', '')
        if not fnmatch.fnmatch(note_id, filters['id_pattern']):
            return False
    
    if filters.get('title_keyword'):
        title = fm.get('title', '').lower()
        if filters['title_keyword'].lower() not in title:
            return False
    
    return True


def get_excerpt(content, max_length=200):
    """Get a short excerpt from the note body."""
    # Remove frontmatter
    parts = content.split('---', 2)
    if len(parts) >= 3:
        body = parts[2].strip()
    else:
        body = content
    
    # Get first non-heading paragraph
    lines = body.split('\n')
    excerpt_lines = []
    for line in lines:
        if line.startswith('#'):
            continue
        if line.strip():
            excerpt_lines.append(line.strip())
            if len(' '.join(excerpt_lines)) > max_length:
                break
    
    excerpt = ' '.join(excerpt_lines)
    if len(excerpt) > max_length:
        excerpt = excerpt[:max_length] + '...'
    
    return excerpt


def search_notes(directory, filters):
    """Search notes in directory matching filters."""
    results = []
    notes_path = Path(directory)
    
    if not notes_path.exists():
        print(f"Error: Directory not found: {directory}")
        return results
    
    for md_file in notes_path.rglob('*.md'):
        content = md_file.read_text()
        frontmatter = parse_frontmatter(content)
        
        if not frontmatter:
            continue
        
        note = {
            'path': str(md_file),
            'frontmatter': frontmatter,
            'excerpt': get_excerpt(content)
        }
        
        if matches_filter(note, filters):
            results.append(note)
    
    return results


def print_results(results, as_json=False):
    """Print search results."""
    if as_json:
        print(json.dumps(results, indent=2))
        return
    
    if not results:
        print("No notes found matching criteria.")
        return
    
    print(f"Found {len(results)} note(s):\n")
    
    for i, note in enumerate(results, 1):
        fm = note['frontmatter']
        print(f"### {i}. {fm.get('title', 'Untitled')}")
        print(f"**Path**: {note['path']}")
        print(f"**ID**: {fm.get('id', 'N/A')}")
        print(f"**Type**: {fm.get('type', 'N/A')}")
        
        domains = fm.get('domain', [])
        if isinstance(domains, list):
            domains = ', '.join(domains)
        print(f"**Domain**: {domains}")
        
        tags = fm.get('tags', [])
        if tags:
            print(f"**Tags**: {', '.join(tags)}")
        
        print(f"**Stability**: {fm.get('stability', 'N/A')}")
        
        if note['excerpt']:
            print(f"\n> {note['excerpt']}")
        
        print()


def main():
    args = sys.argv[1:]
    
    if not args or '--help' in args or '-h' in args:
        print(__doc__)
        sys.exit(0)
    
    filters = {
        'domains': [],
        'tags': []
    }
    as_json = False
    directory = None
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == '--type' and i + 1 < len(args):
            filters['type'] = args[i + 1]
            i += 2
        elif arg == '--domain' and i + 1 < len(args):
            filters['domains'].append(args[i + 1])
            i += 2
        elif arg == '--tag' and i + 1 < len(args):
            filters['tags'].append(args[i + 1])
            i += 2
        elif arg == '--stability' and i + 1 < len(args):
            filters['stability'] = args[i + 1]
            i += 2
        elif arg == '--confidence' and i + 1 < len(args):
            filters['confidence'] = args[i + 1]
            i += 2
        elif arg == '--scope' and i + 1 < len(args):
            filters['scope'] = args[i + 1]
            i += 2
        elif arg == '--intent' and i + 1 < len(args):
            filters['intent'] = args[i + 1]
            i += 2
        elif arg == '--id' and i + 1 < len(args):
            filters['id_pattern'] = args[i + 1]
            i += 2
        elif arg == '--title' and i + 1 < len(args):
            filters['title_keyword'] = args[i + 1]
            i += 2
        elif arg == '--json':
            as_json = True
            i += 1
        elif not arg.startswith('--'):
            directory = arg
            i += 1
        else:
            i += 1
    
    if not directory:
        print("Error: No notes directory specified")
        print(__doc__)
        sys.exit(1)
    
    # Clean up empty filter lists
    if not filters['domains']:
        del filters['domains']
    if not filters['tags']:
        del filters['tags']
    
    results = search_notes(directory, filters)
    print_results(results, as_json)


if __name__ == "__main__":
    main()
