"""Build the final book markdown from chapters_v2/, with all fixes applied.
Self-contained — no external dependencies beyond Python stdlib.
Copy the entire project folder to any machine and run: python build_book.py
"""
import os, re, sys

# --- Configuration (all paths relative to this script) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTER_DIR = os.path.join(SCRIPT_DIR, "chapters_v2")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "full_book.md")

YAML_FRONT_MATTER = r"""---
title: "The State of Hidroinformatics in 2026"
author: "Fehér Zsolt Zoltán"
date: "2026"
geometry: "a4paper,margin=2.5cm"
fontsize: 11pt
mainfont: "Times New Roman"
sansfont: "Arial"
monofont: "Courier New"
lang: en
toc: true
toc-depth: 2
numbersections: false
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\small\leftmark}
  - \fancyhead[R]{}
  - \fancyfoot[L]{\small\textit{The State of Hidroinformatics in 2026}}
  - \fancyfoot[R]{\small Fehér Zsolt Zoltán}
  - \fancyfoot[C]{\thepage}
  - \setlength{\headheight}{14pt}
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{longtable}
  - \usepackage{booktabs}
  - \usepackage{tabularx}
  - \widowpenalty=10000
  - \clubpenalty=10000
  - \brokenpenalty=10000
  - \predisplaypenalty=10000
  - \postdisplaypenalty=150
---
"""

PARTS = [
    ("Part I: The Water Information Landscape", [1, 2, 3, 4]),
    ("Part II: Reading the Landscape", [5, 6, 7, 8]),
    ("Part III: Following the Water Downhill", [9, 10, 11, 12]),
    ("Part IV: When Water Becomes Dangerous", [13, 14, 15, 16, 17]),
    ("Part V: The Hidden Water", [18, 19, 20, 21]),
    ("Part VI: The Intelligent Water System", [22, 23, 24, 25]),
]

APPENDICES = [
    "appendix_data_sources.md",
    "appendix_exercises.md",
    "appendix_software.md",
    "appendix_glossary.md",
]

PREFACE = "ch00_preface.md"


def read_chapter(ch_num):
    """Read a chapter file, trying multiple naming patterns."""
    patterns = [
        f"ch{ch_num:02d}.md",
        f"ch{ch_num:02d}_*.md",
    ]
    for pattern in patterns:
        if '*' in pattern:
            import glob
            matches = glob.glob(os.path.join(CHAPTER_DIR, pattern))
            if matches:
                with open(matches[0], 'r', encoding='utf-8') as f:
                    return f.read()
        else:
            path = os.path.join(CHAPTER_DIR, pattern)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
    return None


def fix_content(text):
    """Apply standard fixes to chapter content."""
    # Remove any duplicate YAML front matter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    # Ensure proper newlines before headings
    text = re.sub(r'([^\n])\n(#{1,4} )', r'\1\n\n\2', text)
    # Fix double blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()


def build():
    """Assemble the full book from chapter files."""
    if not os.path.isdir(CHAPTER_DIR):
        print(f"ERROR: Chapter directory not found: {CHAPTER_DIR}")
        print(f"Create it and add chapter files (ch01.md, ch02.md, ...)")
        sys.exit(1)

    parts_content = []
    total_words = 0
    missing = []

    # Add preface
    preface_path = os.path.join(CHAPTER_DIR, PREFACE)
    if os.path.exists(preface_path):
        with open(preface_path, 'r', encoding='utf-8') as f:
            preface_text = fix_content(f.read())
        words = len(preface_text.split())
        total_words += words
        parts_content.append(f"\n\\newpage\n\n{preface_text}\n\n")
        print(f"  Preface: {words:6,} words")
    else:
        print("  Preface: MISSING")

    for part_title, chapter_nums in PARTS:
        part_md = f"\n\\newpage\n\n# {part_title}\n\n"
        for ch_num in chapter_nums:
            text = read_chapter(ch_num)
            if text is None:
                missing.append(ch_num)
                part_md += f"\n\\newpage\n\n# Chapter {ch_num}: [TO BE WRITTEN]\n\n"
                continue

            text = fix_content(text)
            words = len(text.split())
            total_words += words
            part_md += f"\n\\newpage\n\n{text}\n\n"
            print(f"  Ch {ch_num:2d}: {words:6,} words")

        parts_content.append(part_md)

    # Add appendices
    appendix_content = "\n\\newpage\n\n# Appendices\n\n"
    for app_file in APPENDICES:
        app_path = os.path.join(CHAPTER_DIR, app_file)
        if os.path.exists(app_path):
            with open(app_path, 'r', encoding='utf-8') as f:
                app_text = fix_content(f.read())
            words = len(app_text.split())
            total_words += words
            appendix_content += f"\n\\newpage\n\n{app_text}\n\n"
            print(f"  {app_file}: {words:6,} words")
        else:
            print(f"  {app_file}: MISSING")
    parts_content.append(appendix_content)

    # Assemble
    full = YAML_FRONT_MATTER + "\n".join(parts_content)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full)

    print(f"\n{'='*50}")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Total words: {total_words:,}")
    if missing:
        print(f"Missing chapters: {missing}")
    else:
        print("All chapters present!")
    print(f"{'='*50}")

    # Also try to build PDF if pandoc is available
    try:
        import shutil
        if shutil.which('pandoc'):
            pdf_file = OUTPUT_FILE.replace('.md', '.pdf')
            print(f"\nBuilding PDF with pandoc...")
            os.system(f'pandoc "{OUTPUT_FILE}" -o "{pdf_file}" --pdf-engine=xelatex --lua-filter=no-split-tables.lua 2>&1')
            if os.path.exists(pdf_file):
                size_mb = os.path.getsize(pdf_file) / 1024 / 1024
                print(f"PDF created: {pdf_file} ({size_mb:.1f} MB)")
        else:
            print("\nNote: pandoc not found. Install pandoc + xelatex for PDF generation.")
    except Exception as e:
        print(f"\nPDF build skipped: {e}")


if __name__ == '__main__':
    build()
