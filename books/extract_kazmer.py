"""
Extract Kázmer English-Hungarian Geological Dictionary from PDF to markdown.
"""
import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\maidment_hidroGIS\books\Kazmer_1995_English-Hungarian_Geological_Dictionary.pdf'
out_path = r'C:\maidment_hidroGIS\books\kazmer_glossary.md'

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Dictionary pages start around page 10 (0-indexed) — after intro/abbreviations
# Let's find where entries actually begin by looking for numbered entries
START_PAGE = 15  # Dictionary entries begin at page 15 (0-indexed)
END_PAGE = 554   # Page 554 starts Magyar-angol mutató (Chapter 5), stop before it

# Collect all text from dictionary pages
all_lines = []
for page_num in range(START_PAGE, END_PAGE):
    page = doc[page_num]
    text = page.get_text()
    for line in text.split('\n'):
        line = line.strip()
        if line:
            all_lines.append(line)

doc.close()
print(f"Collected {len(all_lines)} raw lines")

# Filter out headers/footers
skip_patterns = [
    r'^Created by XMLmind',
    r'^Angol-magyar szótár$',
    r'^Tájékoztató$',
    r'^\d+$',  # bare page numbers
    r'^XSL-FO Converter',
]

filtered = []
for line in all_lines:
    skip = False
    for pat in skip_patterns:
        if re.match(pat, line):
            skip = True
            break
    if not skip:
        filtered.append(line)

print(f"After filtering: {len(filtered)} lines")

# Now parse entries. Format: "english_term hungarian_translation number"
# The entry number is at the end: a sequence of digits
# Some entries span continuation from previous line if they don't have a number

entries = []
# Join all filtered lines into one big text block, then split by entry numbers
# Actually, let's try line by line: most entries are single lines ending with a number

# Strategy: each line ending with a number is a complete entry (or end of a multi-line entry)
# Lines NOT ending with a number are continuations

buffer = ""
for line in filtered:
    buffer = (buffer + " " + line).strip() if buffer else line
    # Check if line ends with a number (entry ID)
    if re.search(r'\d+\s*$', buffer):
        entries.append(buffer)
        buffer = ""

# Don't forget leftover
if buffer:
    entries.append(buffer)

print(f"Raw entries: {len(entries)}")

# Now parse each entry: strip trailing number, split English | Hungarian
# The challenge: where does English end and Hungarian begin?
# Looking at the data, the English term is at the start, followed by Hungarian.
# In the PDF, bold text = English headword. But in plain text extraction we lose that.
#
# Strategy: The entry number is stripped. Then we need to find the boundary.
# Looking at examples:
#   "aragonite compensation depth aragonitkompenzációs mélység (ACD) 1118"
#   "arc ív; (spektr) fényív, ív, ívfény; (mat) ív, arkusz 1125"
#   "abandoned mine felhagyott bánya 1"
#
# The English headword and Hungarian translation are separated implicitly.
# We can use the fact that Hungarian words contain diacritics or known Hungarian patterns.
# But some translations are Latin/international (like "aragonit").
#
# Better approach: use PyMuPDF to extract bold spans vs regular spans.

# Let me re-extract using span-level formatting info
print("\nRe-extracting with formatting info...")

doc = fitz.open(pdf_path)

entries_parsed = []
current_english = ""
current_hungarian = ""

for page_num in range(START_PAGE, END_PAGE):
    page = doc[page_num]
    blocks = page.get_text("dict", sort=True)["blocks"]

    for block in blocks:
        if "lines" not in block:
            continue
        for line_data in block["lines"]:
            spans = line_data["spans"]
            if not spans:
                continue

            # Build full line text to check if it's a header/footer
            full_text = "".join(s["text"] for s in spans).strip()

            # Skip headers/footers
            skip = False
            for pat in skip_patterns:
                if re.match(pat, full_text):
                    skip = True
                    break
            if skip:
                continue

            # Now process spans: bold = English, regular = Hungarian
            # Bold fonts typically have "Bold" in the font name
            line_english_parts = []
            line_hungarian_parts = []
            found_non_bold = False

            for span in spans:
                text = span["text"]
                font = span["font"]
                flags = span["flags"]  # bit 4 (16) = bold
                is_bold = bool(flags & (1 << 4)) or "Bold" in font or "bold" in font

                if is_bold and not found_non_bold:
                    line_english_parts.append(text)
                else:
                    found_non_bold = True
                    line_hungarian_parts.append(text)

            eng = "".join(line_english_parts).strip()
            hun = "".join(line_hungarian_parts).strip()

            if eng:
                # If we have a previous entry, save it
                if current_english:
                    entries_parsed.append((current_english, current_hungarian))
                current_english = eng
                current_hungarian = hun
            elif hun and current_english:
                # Continuation line (no bold = continuation of Hungarian)
                current_hungarian += " " + hun

# Don't forget last entry
if current_english:
    entries_parsed.append((current_english, current_hungarian))

doc.close()

print(f"Entries with formatting: {len(entries_parsed)}")

# Clean up entries: strip trailing entry numbers from Hungarian text
cleaned = []
for eng, hun in entries_parsed:
    # Strip trailing entry number
    hun = re.sub(r'\s+\d+\s*$', '', hun)
    # Also strip entry number that might be at end of english (shouldn't happen but just in case)
    eng = eng.strip()
    hun = hun.strip()

    # Skip empty entries
    if not eng or not hun:
        continue

    # Skip if english looks like a page number or header
    if re.match(r'^\d+$', eng):
        continue
    if eng in ('Angol-magyar szótár', 'Created by XMLmind XSL-FO Converter.', 'Tájékoztató'):
        continue

    # Clean up pipe characters that would break markdown table
    eng = eng.replace('|', '/')
    hun = hun.replace('|', '/')

    cleaned.append((eng, hun))

print(f"Cleaned entries: {len(cleaned)}")

# Write markdown
with open(out_path, 'w', encoding='utf-8') as f:
    f.write("# Kázmer English-Hungarian Geological Dictionary\n")
    f.write("## Extracted from Kázmer (2005), {:,} terms\n\n".format(len(cleaned)))
    f.write("| English | Magyar |\n")
    f.write("|---------|--------|\n")
    for eng, hun in cleaned:
        f.write(f"| {eng} | {hun} |\n")

print(f"\nDone! Wrote {len(cleaned):,} entries to {out_path}")

# Show some samples
print("\nFirst 10 entries:")
for e, h in cleaned[:10]:
    print(f"  {e} | {h}")

print("\nMiddle entries (around 8000):")
for e, h in cleaned[8000:8010]:
    print(f"  {e} | {h}")

print("\nLast 10 entries:")
for e, h in cleaned[-10:]:
    print(f"  {e} | {h}")
