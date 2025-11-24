#!/usr/bin/env python3
"""
Fix author formatting in publication files
"""
import os
import re
from pathlib import Path

pub_dir = Path('content/publication')
pub_files = list(pub_dir.glob('*/index.md'))
pub_files = [f for f in pub_files if f.parent.name not in ['_index.md']]

print(f"Found {len(pub_files)} publication files to fix...")

for i, pub_file in enumerate(pub_files):
    try:
        with open(pub_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue

        frontmatter = parts[1]
        body = parts[2]

        # Extract authors section
        authors_match = re.search(r'authors:\n((?:- .*\n)+)', frontmatter)
        if not authors_match:
            continue

        authors_section = authors_match.group(1)
        author_lines = [line.strip('- \n') for line in authors_section.split('\n') if line.strip().startswith('-')]

        # Reconstruct authors properly
        # Combine consecutive items that seem to be parts of the same name
        new_authors = []
        j = 0
        while j < len(author_lines):
            author = author_lines[j]

            # Skip empty lines
            if not author.strip():
                j += 1
                continue

            # If this is 'admin', keep it as is
            if author == 'admin':
                new_authors.append('admin')
                j += 1
                continue

            # Check if next items are initials (length <= 4 and contains . or single letter)
            # Combine: "LastName" + "F." or "LastName" + "F. M." etc.
            while j + 1 < len(author_lines):
                next_item = author_lines[j + 1].strip(', ')
                # Check if it's an initial (contains . or is very short)
                if (len(next_item) <= 4 and ('.' in next_item or len(next_item) <= 2)) and next_item != 'admin':
                    author += ', ' + next_item
                    j += 1
                else:
                    break

            # Clean up
            author = author.strip(', ')
            if author:
                new_authors.append(author)
            j += 1

        # Rebuild authors section
        new_authors_section = 'authors:\n' + '\n'.join([f'- {author}' for author in new_authors]) + '\n'

        # Replace in frontmatter
        new_frontmatter = re.sub(r'authors:\n(?:- .*\n)+', new_authors_section, frontmatter)

        # Rebuild file
        new_content = f"---{new_frontmatter}---{body}"

        with open(pub_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        if (i + 1) % 50 == 0:
            print(f"  Fixed {i+1} files...")

    except Exception as e:
        print(f"  Error processing {pub_file}: {e}")

print(f"\nDone! Fixed author formatting in {len(pub_files)} files.")
