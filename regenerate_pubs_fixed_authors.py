#!/usr/bin/env python3
"""
Regenerate publications with fixed author parsing
"""
import os
import re
from pathlib import Path
import shutil

# Read pub.txt
with open('pub.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_section = None
journal_papers = []
books = []
conferences = []

for line in lines:
    line_stripped = line.strip()
    if line_stripped == 'Journal Papers':
        current_section = 'journal'
    elif line_stripped == 'Books Edited and Book Chapters':
        current_section = 'books'
    elif line_stripped == 'Conference Proceedings':
        current_section = 'conference'
    elif line_stripped and current_section == 'journal':
        journal_papers.append(line_stripped)
    elif line_stripped and current_section == 'books':
        books.append(line_stripped)
    elif line_stripped and current_section == 'conference':
        conferences.append(line_stripped)

def extract_year(text):
    match = re.search(r'\((\d{4})\)', text)
    if match:
        return match.group(1)
    match = re.search(r',\s*(\d{4})[,\.]', text)
    if match:
        return match.group(1)
    return '2024'

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:50]

def extract_doi(text):
    match = re.search(r'(?:https?://)?(?:dx\.)?doi\.org/(10\.\S+)', text)
    if match:
        doi = match.group(1)
        doi = doi.rstrip('.,;:)')
        return doi
    return ''

def parse_authors(authors_text):
    """
    Parse author string like: "Ko, T., Le, C., Jeong, H. D., and Choi, K."
    Returns: ['Ko, T.', 'Le, C.', 'admin', 'Choi, K.']
    """
    # Remove ' and '
    authors_text = authors_text.replace(' and ', ', ')

    # Split by looking for pattern: ", [CapitalLetter]"
    # But we need to avoid splitting within initials like "H. D."

    # Strategy: find all "Lastname, Initial(s)" patterns
    authors = []

    # Pattern: Word(s), followed by initials/letters, followed by comma or end
    # Example: "Ko, T." or "Jeong, H. D." or "Rybkowski, Z. K."
    pattern = r'([A-Z][A-Za-z\-\']+(?:\s+[A-Z][A-Za-z\-\']+)*),\s*([A-Z]\.?(?:\s*[A-Z]\.?)*)'

    matches = re.finditer(pattern, authors_text)

    for match in matches:
        lastname = match.group(1).strip()
        initials = match.group(2).strip()
        full_name = f"{lastname}, {initials}"

        # Check if this is Jeong
        if 'Jeong' in lastname and any(init in initials for init in ['H. D', 'H.D', 'D.', 'H. S', 'H.S']):
            authors.append('admin')
        else:
            authors.append(full_name)

    return authors if authors else ['Unknown']

def parse_journal_paper(text):
    year = extract_year(text)
    doi = extract_doi(text)

    # Extract title
    title_match = re.search(r'\('+year+r'\)\s+(.*?)(?:,\s*(?:Journal|ASCE|Automation|Construction|Transportation|International|Water|IEEE))', text)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title_match = re.search(r'\('+year+r'\)\s+([^,]+)', text)
        title = title_match.group(1).strip() if title_match else 'Untitled'

    # Extract authors
    authors_match = re.search(r'^(.*?)\s*\('+year, text)
    authors_text = authors_match.group(1).strip() if authors_match else ''
    authors = parse_authors(authors_text)

    # Extract venue
    venue = ''
    venue_match = re.search(r'(?:,\s*)(Journal[^,]*|Automation[^,]*|Construction[^,]*|Transportation[^,]*|Water[^,]*|IEEE[^,]*)', text)
    if venue_match:
        venue = venue_match.group(1).strip()

    return {
        'title': title,
        'authors': authors,
        'year': year,
        'venue': venue,
        'doi': doi,
        'full_text': text
    }

def parse_conference_paper(text):
    year = extract_year(text)
    doi = extract_doi(text)

    # Conference papers often have quotes around title
    title_match = re.search(r'"([^"]+)"', text)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title_match = re.search(r'\('+year+r'\)\s+(.*?)(?:,\s*(?:Proceedings|Conference|ASCE|International))', text, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title_match = re.search(r'\('+year+r'\)\s+([^,]+)', text)
            title = title_match.group(1).strip() if title_match else 'Untitled'

    # Extract authors
    authors_match = re.search(r'^(.*?)\s*\('+year, text)
    authors_text = authors_match.group(1).strip() if authors_match else ''
    authors = parse_authors(authors_text)

    # Extract conference name
    venue = ''
    venue_patterns = [
        r'Proceedings of[^,]*',
        r'(?:International |ASCE |CIB )?Conference[^,]*',
        r'(?:International )?Symposium[^,]*'
    ]
    for pattern in venue_patterns:
        venue_match = re.search(pattern, text, re.IGNORECASE)
        if venue_match:
            venue = venue_match.group().strip()
            break

    if not venue:
        parts = text.split(',')
        if len(parts) > 2:
            venue = parts[-3].strip()

    return {
        'title': title,
        'authors': authors,
        'year': year,
        'venue': venue,
        'doi': doi,
        'full_text': text
    }

def parse_book(text):
    year = extract_year(text)

    title_match = re.search(r'\('+year+r'\)\s*([^,\.]+)', text)
    title = title_match.group(1).strip() if title_match else 'Untitled'

    authors_match = re.search(r'^(.*?)\s*\('+year, text)
    authors_text = authors_match.group(1).strip() if authors_match else ''
    authors = parse_authors(authors_text)

    venue = 'Book Chapter'
    if 'Encyclopedia' in text:
        venue = 'Encyclopedia'
    elif 'Proceedings' in text:
        venue = 'Conference Proceedings'

    return {
        'title': title,
        'authors': authors,
        'year': year,
        'venue': venue,
        'doi': '',
        'full_text': text
    }

def create_markdown(pub_data, pub_type):
    authors_list = '\n'.join([f"- {author}" for author in pub_data['authors']])

    url_source = ''
    if pub_data['doi']:
        url_source = f"https://doi.org/{pub_data['doi']}"

    md = f"""---
title: "{pub_data['title']}"
authors:
{authors_list}
date: "{pub_data['year']}-01-01T00:00:00Z"
doi: "{pub_data['doi']}"

publishDate: "{pub_data['year']}-01-01T00:00:00Z"

publication_types: ["{pub_type}"]

publication: "{pub_data['venue']}"
publication_short: ""

abstract: ""

summary: ""

tags: []

featured: false

url_source: '{url_source}'
---

{pub_data['full_text']}
"""
    return md

# Clear old generated publications (keep manually created ones)
pub_dir = Path('content/publication')
manual_pubs = ['2015-host-country', '2023-risk-decision', '2024-best-paper', '_index.md']

for folder in pub_dir.iterdir():
    if folder.is_dir() and folder.name not in manual_pubs:
        shutil.rmtree(folder)

print(f"Processing {len(journal_papers)} journal papers...")
for i, paper in enumerate(journal_papers):
    if not paper.strip():
        continue

    try:
        pub_data = parse_journal_paper(paper)
        year = pub_data['year']
        slug = slugify(pub_data['title'])
        folder_name = f"{year}-journal-{slug}"

        folder = pub_dir / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        md_content = create_markdown(pub_data, 'article-journal')

        with open(folder / 'index.md', 'w', encoding='utf-8') as f:
            f.write(md_content)

        if (i + 1) % 10 == 0:
            print(f"  Processed {i+1} journal papers...")
    except Exception as e:
        print(f"  Error processing journal paper {i+1}: {e}")

print(f"\nProcessing {len(books)} books...")
for i, book in enumerate(books):
    if not book.strip():
        continue

    try:
        pub_data = parse_book(book)
        year = pub_data['year']
        slug = slugify(pub_data['title'])
        folder_name = f"{year}-book-{slug}"

        folder = pub_dir / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        md_content = create_markdown(pub_data, 'book')

        with open(folder / 'index.md', 'w', encoding='utf-8') as f:
            f.write(md_content)
    except Exception as e:
        print(f"  Error processing book {i+1}: {e}")

print(f"\nProcessing {len(conferences)} conference papers...")
for i, paper in enumerate(conferences):
    if not paper.strip():
        continue

    try:
        pub_data = parse_conference_paper(paper)
        year = pub_data['year']
        slug = slugify(pub_data['title'])
        folder_name = f"{year}-conf-{slug}"

        folder = pub_dir / folder_name
        folder.mkdir(parents=True, exist_ok=True)

        md_content = create_markdown(pub_data, 'paper-conference')

        with open(folder / 'index.md', 'w', encoding='utf-8') as f:
            f.write(md_content)

        if (i + 1) % 20 == 0:
            print(f"  Processed {i+1} conference papers...")
    except Exception as e:
        print(f"  Error processing conference paper {i+1}: {e}")

print("\nDone! Generated publications with fixed author formatting.")
print(f"  Journal papers: {len(journal_papers)}")
print(f"  Books: {len(books)}")
print(f"  Conference papers: {len(conferences)}")
