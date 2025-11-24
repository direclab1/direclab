#!/usr/bin/env python3
"""
Script to generate publication markdown files from pub.txt
"""
import os
import re
from pathlib import Path

# Read pub.txt
with open('pub.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into sections
sections = content.split('\n\n')
current_section = None
journal_papers = []
books = []
conferences = []

for line in content.split('\n'):
    line = line.strip()
    if line == 'Journal Papers':
        current_section = 'journal'
    elif line == 'Books Edited and Book Chapters':
        current_section = 'books'
    elif line == 'Conference Proceedings':
        current_section = 'conference'
    elif line and current_section == 'journal':
        journal_papers.append(line)
    elif line and current_section == 'books':
        books.append(line)
    elif line and current_section == 'conference':
        conferences.append(line)

def extract_year(text):
    """Extract year from publication text"""
    # Try to find year in format (YYYY)
    match = re.search(r'\((\d{4})\)', text)
    if match:
        return match.group(1)
    # Try to find year in different formats
    match = re.search(r',\s*(\d{4})', text)
    if match:
        return match.group(1)
    return '2024'

def extract_authors(text):
    """Extract authors from publication text"""
    # Authors are before the year
    match = re.match(r'^(.*?)\s*\(\d{4}\)', text)
    if match:
        authors_str = match.group(1).strip()
        # Replace common patterns
        authors_str = authors_str.replace(' and ', ', ')
        authors_str = authors_str.replace('Jeong, H. D.', 'admin')
        authors_str = authors_str.replace('Jeong, H.D.', 'admin')
        authors_str = authors_str.replace('Jeong, D.', 'admin')
        authors_str = authors_str.replace('Jeong, H. S.', 'admin')
        authors_str = authors_str.replace('Jeong, H.S.', 'admin')

        # Split by comma or 'and'
        authors = [a.strip() for a in re.split(r',\s*(?![^()]*\))', authors_str)]
        return authors
    return []

def extract_title(text):
    """Extract title from publication text"""
    # Title is usually after year and before journal/conference name
    match = re.search(r'\)\s+(.*?),\s+[A-Z]', text)
    if match:
        title = match.group(1).strip()
        # Remove quotes if present
        title = title.strip('"\'')
        return title
    return text[:100]

def extract_venue(text):
    """Extract journal/conference name"""
    # Look for pattern after title
    parts = text.split(',')
    if len(parts) >= 2:
        for i, part in enumerate(parts):
            if 'Journal' in part or 'Proceedings' in part or 'Conference' in part or 'ASCE' in part:
                return part.strip()
    return ''

def create_slug(authors, year):
    """Create a slug for the publication folder"""
    if authors:
        first_author = authors[0].split(',')[0].lower().replace(' ', '-').replace('.', '')
    else:
        first_author = 'unknown'
    return f"{year}-{first_author}"

def create_markdown(title, authors, year, venue, pub_type, text, doi=''):
    """Create markdown content for publication"""
    authors_list = '\n'.join([f"- {author}" for author in authors])

    md = f"""---
title: "{title}"
authors:
{authors_list}
date: "{year}-01-01T00:00:00Z"
doi: "{doi}"

publishDate: "{year}-01-01T00:00:00Z"

publication_types: ["{pub_type}"]

publication: "{venue}"
publication_short: ""

abstract: ""

summary: ""

tags: []

featured: false

url_pdf: ''
url_source: ''

projects: []
slides: ""
---

{text}
"""
    return md

# Create publication directories
pub_dir = Path('content/publication')

print(f"Processing {len(journal_papers)} journal papers...")
for i, paper in enumerate(journal_papers):
    if not paper.strip():
        continue

    year = extract_year(paper)
    authors = extract_authors(paper)
    title = extract_title(paper)
    venue = extract_venue(paper)

    # Extract DOI if present
    doi_match = re.search(r'https?://doi\.org/(.*?)(?:\s|$|<|,)', paper)
    doi = doi_match.group(1) if doi_match else ''

    slug = f"{year}-journal-{i+1:03d}"
    folder = pub_dir / slug
    folder.mkdir(parents=True, exist_ok=True)

    md_content = create_markdown(title, authors, year, venue, 'article-journal', paper, doi)

    with open(folder / 'index.md', 'w', encoding='utf-8') as f:
        f.write(md_content)

    if (i + 1) % 10 == 0:
        print(f"  Processed {i+1} journal papers...")

print(f"\nProcessing {len(books)} books...")
for i, book in enumerate(books):
    if not book.strip():
        continue

    year = extract_year(book)
    authors = extract_authors(book)
    title = extract_title(book)
    venue = extract_venue(book) or 'Book Chapter'

    slug = f"{year}-book-{i+1:03d}"
    folder = pub_dir / slug
    folder.mkdir(parents=True, exist_ok=True)

    md_content = create_markdown(title, authors, year, venue, 'book', book)

    with open(folder / 'index.md', 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"\nProcessing {len(conferences)} conference papers...")
for i, paper in enumerate(conferences):
    if not paper.strip():
        continue

    year = extract_year(paper)
    authors = extract_authors(paper)
    title = extract_title(paper)
    venue = extract_venue(paper) or 'Conference Proceedings'

    doi_match = re.search(r'https?://doi\.org/(.*?)(?:\s|$|<|,)', paper)
    doi = doi_match.group(1) if doi_match else ''

    slug = f"{year}-conf-{i+1:03d}"
    folder = pub_dir / slug
    folder.mkdir(parents=True, exist_ok=True)

    md_content = create_markdown(title, authors, year, venue, 'paper-conference', paper, doi)

    with open(folder / 'index.md', 'w', encoding='utf-8') as f:
        f.write(md_content)

    if (i + 1) % 20 == 0:
        print(f"  Processed {i+1} conference papers...")

print("\nDone! Generated publications.")
print(f"  Journal papers: {len(journal_papers)}")
print(f"  Books: {len(books)}")
print(f"  Conference papers: {len(conferences)}")
