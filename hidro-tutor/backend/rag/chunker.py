"""Section-aware chunker for Markdown chapter files.

Splits .md chapters by heading structure, preserving metadata
(chapter number, part, section, subsection, topics).
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import tiktoken

from backend.config import settings

# Book part assignments
CHAPTER_PARTS: dict[int, str] = {
    1: "Part I: Foundations", 2: "Part I: Foundations",
    3: "Part I: Foundations", 4: "Part I: Foundations",
    5: "Part II: Terrain Analysis", 6: "Part II: Terrain Analysis",
    7: "Part II: Terrain Analysis", 8: "Part II: Terrain Analysis",
    9: "Part III: Watershed Delineation", 10: "Part III: Watershed Delineation",
    11: "Part III: Watershed Delineation", 12: "Part III: Watershed Delineation",
    13: "Part IV: Flood Hazard", 14: "Part IV: Flood Hazard",
    15: "Part IV: Flood Hazard", 16: "Part IV: Flood Hazard",
    17: "Part IV: Flood Hazard",
    18: "Part V: Groundwater", 19: "Part V: Groundwater",
    20: "Part V: Groundwater", 21: "Part V: Groundwater",
    22: "Part VI: AI and the Future", 23: "Part VI: AI and the Future",
    24: "Part VI: AI and the Future", 25: "Part VI: AI and the Future",
}

# Chapter titles (extracted from the actual files)
CHAPTER_TITLES: dict[int, str] = {
    1: "Why Hidroinformatics Matters",
    2: "Mapping Water: From Paper to Pixels",
    3: "Where the Data Lives",
    4: "GIS as a Water Tool",
    5: "The Grid: How Computers See Terrain",
    6: "Calculating with Maps",
    7: "Slope, Aspect, and the Shape of the Land",
    8: "Measuring Rain Where It Falls",
    9: "Preparing the Digital Landscape",
    10: "Which Way Does Water Flow?",
    11: "Drawing Watersheds from Data",
    12: "Automating the Workflow",
    13: "Seeing the Ground in 3D: LiDAR",
    14: "How High Above the River?",
    15: "Mapping Where Floods Go",
    16: "Forecasting Floods in Real Time",
    17: "Who Lives in the Flood Zone?",
    18: "Seeing Underground: 3D Subsurface GIS",
    19: "Wells, Boreholes, and Aquifer Maps",
    20: "Building a Picture of the Underground",
    21: "Simulating Groundwater Flow",
    22: "When Models Meet Data",
    23: "AI as a Hydrologist's Assistant",
    24: "Agentic AI: The Autonomous Modeler",
    25: "The Future of Water Intelligence",
}


@dataclass
class Chunk:
    """A chunk of book text with full metadata."""
    text: str
    chapter: int
    chapter_title: str
    part: str
    section: str = ""
    subsection: str = ""
    chunk_type: str = "theory"  # theory, definition, example, exercise, figure_caption, code
    token_count: int = 0
    chunk_id: str = ""
    metadata: dict = field(default_factory=dict)


def count_tokens(text: str) -> int:
    """Count tokens using tiktoken (cl100k_base)."""
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def classify_chunk_type(text: str) -> str:
    """Heuristic classification of chunk content type."""
    lower = text.lower()

    if re.search(r"```python|```r|```sql|```bash", text):
        return "code"
    if re.search(r"\*\*figure \d+", lower):
        return "figure_caption"
    if "exercise" in lower or "problem" in lower and ("calculate" in lower or "compute" in lower):
        return "exercise"
    if re.search(r"\*\*definition\*\*|is defined as|we define", lower):
        return "definition"
    if re.search(r"for example|consider the case|a practical illustration", lower):
        return "example"
    return "theory"


def split_large_chunk(text: str, max_tokens: int, overlap_tokens: int) -> list[str]:
    """Split a text block that exceeds max_tokens at paragraph boundaries."""
    paragraphs = re.split(r"\n\n+", text)
    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = count_tokens(para)
        if current_tokens + para_tokens > max_tokens and current:
            chunks.append("\n\n".join(current))
            # Keep last paragraph(s) as overlap
            overlap: list[str] = []
            overlap_count = 0
            for p in reversed(current):
                t = count_tokens(p)
                if overlap_count + t > overlap_tokens:
                    break
                overlap.insert(0, p)
                overlap_count += t
            current = overlap
            current_tokens = overlap_count

        current.append(para)
        current_tokens += para_tokens

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def parse_chapter(filepath: Path, chapter_num: int) -> list[Chunk]:
    """Parse a Markdown chapter file into chunks.

    Strategy:
    - Split at ## (section) and ### (subsection) headings
    - If a section exceeds max_tokens, split at paragraph boundaries
    - Each chunk carries full metadata
    """
    text = filepath.read_text(encoding="utf-8")

    # Remove \newpage directives
    text = text.replace("\\newpage", "").strip()

    # Remove HTML comments (figure prompts)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    chapter_title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")
    part = CHAPTER_PARTS.get(chapter_num, "Unknown")

    max_tokens = settings.chunk_max_tokens
    overlap_tokens = settings.chunk_overlap_tokens

    # Split by headings (## and ###)
    # Pattern captures the heading line and the text until the next heading
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)

    sections: list[tuple[str, str, str]] = []  # (heading_level, heading_text, body)
    matches = list(heading_pattern.finditer(text))

    for i, match in enumerate(matches):
        level = match.group(1)
        heading = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()

        if body:  # Skip empty sections
            sections.append((level, heading, body))

    # If no headings found, treat entire text as one section
    if not sections:
        sections = [("#", chapter_title, text)]

    chunks: list[Chunk] = []
    current_section = ""
    current_subsection = ""
    chunk_counter = 0

    for level, heading, body in sections:
        # Track section hierarchy
        if level == "#":
            # Chapter-level heading, skip (title)
            continue
        elif level == "##":
            current_section = heading
            current_subsection = ""
        elif level == "###":
            current_subsection = heading

        # Check if body needs splitting
        tokens = count_tokens(body)
        if tokens > max_tokens:
            sub_texts = split_large_chunk(body, max_tokens, overlap_tokens)
        else:
            sub_texts = [body]

        for sub_text in sub_texts:
            chunk_counter += 1
            chunk = Chunk(
                text=sub_text,
                chapter=chapter_num,
                chapter_title=chapter_title,
                part=part,
                section=current_section,
                subsection=current_subsection,
                chunk_type=classify_chunk_type(sub_text),
                token_count=count_tokens(sub_text),
                chunk_id=f"ch{chapter_num:02d}_{chunk_counter:03d}",
                metadata={
                    "chapter": chapter_num,
                    "chapter_title": chapter_title,
                    "part": part,
                    "section": current_section,
                    "subsection": current_subsection,
                    "chunk_type": classify_chunk_type(sub_text),
                },
            )
            chunks.append(chunk)

    return chunks


def parse_all_chapters(chapters_dir: Optional[Path] = None) -> list[Chunk]:
    """Parse all 25 chapters and return all chunks."""
    if chapters_dir is None:
        chapters_dir = settings.resolve_path(settings.chapters_path)

    all_chunks: list[Chunk] = []

    for ch_num in range(1, 26):
        filepath = chapters_dir / f"ch{ch_num:02d}.md"
        if filepath.exists():
            chapter_chunks = parse_chapter(filepath, ch_num)
            all_chunks.extend(chapter_chunks)

    return all_chunks
