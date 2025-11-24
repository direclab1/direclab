#!/usr/bin/env python3
"""
Clean publication markdown files to only show source document and DOI buttons
"""
import os
import re
from pathlib import Path

pub_dir = Path('content/publication')

# Find all publication index.md files
pub_files = list(pub_dir.glob('*/index.md'))
pub_files = [f for f in pub_files if f.parent.name not in ['_index.md']]

print(f"Found {len(pub_files)} publication files to clean...")

for i, pub_file in enumerate(pub_files):
    try:
        with open(pub_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"  Skipping {pub_file}: Invalid format")
            continue

        frontmatter = parts[1]
        body = parts[2]

        # Remove all url_ fields except url_source
        # Keep doi field
        lines = frontmatter.split('\n')
        new_lines = []
        skip_line = False

        for line in lines:
            # Skip url_pdf, url_code, url_dataset, url_poster, url_project, url_slides, url_video
            if re.match(r'\s*url_(pdf|code|dataset|poster|project|slides|video):', line):
                continue
            # Skip projects and slides fields
            if re.match(r'\s*(projects|slides):', line):
                skip_line = True
                continue
            if skip_line:
                if line.strip() and not line.startswith(' '):
                    skip_line = False
                else:
                    continue

            new_lines.append(line)

        new_frontmatter = '\n'.join(new_lines)

        # Rebuild the file
        new_content = f"---{new_frontmatter}---{body}"

        with open(pub_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        if (i + 1) % 50 == 0:
            print(f"  Cleaned {i+1} files...")

    except Exception as e:
        print(f"  Error processing {pub_file}: {e}")

print(f"\nDone! Cleaned {len(pub_files)} publication files.")
print("Each publication now only shows:")
print("  - Source Document button (url_source)")
print("  - DOI button (if doi is present)")
