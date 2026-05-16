import os
import re
import bibtexparser

BIB_FILE = "publications.bib"  # Name of your exported BibTeX file
OUTPUT_DIR = "content/publications"


def clean_value(text):
    """Removes LaTeX curly brackets and extra whitespace."""
    if not text:
        return ""
    return re.sub(r'[\{\}]', '', text).strip()


def parse_authors(author_str):
    """Formats 'Last, First and Last2, First2' into clean strings."""
    if not author_str:
        return []
    raw_authors = clean_value(author_str).split(" and ")
    cleaned = []
    for author in raw_authors:
        if "," in author:
            parts = author.split(",")
            cleaned.append(f"{parts[1].strip()} {parts[0].strip()}")
        else:
            cleaned.append(author.strip())
    return cleaned


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        # Create the section header index file for the /publications/ listing layout
        with open(os.path.join(OUTPUT_DIR, "_index.md"), "w", encoding='utf-8') as f:
            f.write("---\ntitle: \"Publications\"\nlayout: \"list\"\n---\n")

    with open(BIB_FILE, encoding='utf-8') as bibtex_file:
        db = bibtexparser.load(bibtex_file)

    for entry in db.entries:
        # Generate a safe folder name from the citekey
        citekey = re.sub(r'[^a-zA-Z0-9_-]', '', entry.get('ID', 'pub'))
        title = clean_value(entry.get('title', 'Untitled Publication'))
        year = entry.get('year', '2026')
        date_str = f"{year}-01-01"

        # Determine publishing venue
        venue = entry.get('journal', entry.get('booktitle', entry.get('howpublished', '')))
        venue = clean_value(venue)

        authors = parse_authors(entry.get('author', ''))
        abstract = clean_value(entry.get('abstract', ''))
        doi = clean_value(entry.get('doi', ''))

        # Prepare folder structure for Hugo Page Bundles
        bundle_path = os.path.join(OUTPUT_DIR, citekey)
        os.makedirs(bundle_path, exist_ok=True)

        # Build Blowfish front matter and body markdown
        md_content = f"""---
title: "{title}"
date: {date_str}
description: "{venue if venue else 'Research Paper'}"
showDate: false
showAuthor: false
showReadingTime: false
tags: ["{year}"]
---

**Authors:** {', '.join(authors)}

**Venue:** *{venue}* ({year})
"""
        if doi:
            md_content += f"\n**DOI:** [{doi}](https://doi.org{doi})\n"

        if abstract:
            md_content += f"\n### Abstract\n{abstract}\n"

        with open(os.path.join(bundle_path, "index.md"), "w", encoding='utf-8') as f:
            f.write(md_content)

    print(f"Successfully processed {len(db.entries)} publications into {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
