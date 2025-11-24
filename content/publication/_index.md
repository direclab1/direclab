---
title: Publications
date: 2024-01-01

type: landing

sections:
  # Journal Papers Section
  - block: collection
    id: journal-papers
    content:
      title: Journal Papers
      text: ""
      filters:
        folders:
          - publication
        publication_type: 'article-journal'
      count: 10
      sort_by: 'Date'
      sort_ascending: false
      archive:
        enable: true
        text: See all journal papers
        link: journal-papers/
    design:
      view: citation
      columns: '1'

  # Books and Book Chapters Section
  - block: collection
    id: books
    content:
      title: Books and Book Chapters
      text: ""
      filters:
        folders:
          - publication
        publication_type: 'book'
      count: 10
      sort_by: 'Date'
      sort_ascending: false
      archive:
        enable: true
        text: See all books and chapters
        link: books-chapters/
    design:
      view: citation
      columns: '1'

  # Conference Proceedings Section
  - block: collection
    id: conference
    content:
      title: Conference Proceedings
      text: ""
      filters:
        folders:
          - publication
        publication_type: 'paper-conference'
      count: 10
      sort_by: 'Date'
      sort_ascending: false
      archive:
        enable: true
        text: See all conference papers
        link: conference-proceedings/
    design:
      view: citation
      columns: '1'
---
