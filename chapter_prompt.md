# Chapter Development Prompt — "The State of Hidroinformatics in 2026"

**Author**: Fehér Zsolt Zoltán

---

## Context

We are writing an English-language professional book titled **"The State of Hidroinformatics in 2026"** (author: Fehér Zsolt Zoltán), in 25 chapters across 6 parts. This is not a textbook — it is a standalone book accessible to anyone interested in hydroinformatics: water engineers, environmental scientists, researchers, decision-makers, or professionals from other fields. The reader is treated as an intelligent, motivated adult. Basic understanding of hydrology and familiarity with GIS concepts can be assumed, but NOT programming expertise.

### The source material

The existing lecture notes (C:/maidment_hidroGIS/lecture_notes/) contain the first draft derived from Maidment's lectures, enriched with original PPT content. These notes are **a starting point, not the final product** — they are often too technical, US-centric, and lecture-style rather than book-style. Additional source materials:
- Arc Hydro Groundwater book (C:/maidment_hidroGIS/books/arc_hydro_gw/) — for Part V
- Handbook of HydroInformatics extractions (C:/maidment_hidroGIS/hydroAI/extracted/) — for Part VI
- International data sources (C:/maidment_hidroGIS/Hungarian_EU_Data_Sources.md, international_data_sources.md)
- Internationalization guide (C:/maidment_hidroGIS/INTERNATIONALIZATION_PROMPT.md)

### The international thread

This book serves Hungarian university students as primary audience and international students (Asia, Middle East, Africa) as secondary. Every chapter must include:
- **US examples** (retained from original — they are well-documented)
- **Hungarian/EU examples** (primary parallel — Hungary is the "home" example)
- **Global alternatives** (for international readers)

When introducing datasets, systems, or case studies, use the three-tier approach: US → Hungary/EU → Global.

### The application thread

Every concept is presented through the lens of solving a real water problem. Not abstract GIS theory, but: "Here's a water crisis. Here's what data exists. Here's how we solve it today."

---

## Lessons from gis-konyv2025 v1 — AVOID THESE

### 1. The 5-line subsection problem
Every subsection (###) that has its own heading deserves at least 300-500 words of exposition. If you can't write 300 words about a topic, don't give it a standalone heading — merge it into the neighboring subsection.

### 2. The unexpanded list problem
Every list item that carries SUBSTANTIVE content should be expanded with 2-4 sentences explaining HOW, WHY, and giving a concrete example. Lists that are genuinely just lists (software names, band specifications) can stay as lists.

### 3. The embedded technical elements problem
REST API URLs, CLI commands, file format structures — give them dedicated code blocks, not embedded in prose.

### 4. The worked example problem
A good worked example contains: (a) the input data explicitly stated, (b) the formula with actual values substituted, (c) intermediate steps, (d) the result with units, (e) interpretation ("this means that...").

### 5. The US-centrism problem
**CRITICAL for this book**: Never present US data/systems as the default without immediately offering the European/Hungarian and global equivalents. Use equivalence tables or inline three-tier references.

---

## Writing Rules

### Style

Professional book. Flowing prose paragraphs, logical transitions, narrative flow. The tone: an experienced colleague explaining to an intelligent peer. Not dry, not condescending. Every concept is logically introduced: problem → solution → connection to the next topic.

### Structure and markdown formatting — CRITICAL

**Required heading hierarchy:**

```markdown
# Chapter X: Chapter Title          ← EXACTLY ONE per file

## X.Y Subsection Title              ← main topic within chapter

### X.Y.Z Sub-subsection Title       ← subtopic

#### Minor Detail Title              ← rarely
```

**Rules:**
- EXACTLY ONE `#` heading per file
- Numbering: `## X.Y`, `### X.Y.Z` — NEVER omit
- References: `## References` (## level)
- Every `#` chapter heading preceded by `\newpage`

**The elaboration method:**
1. First decompose the chapter into `##` level subsections
2. Break each `##` into `###` level sub-subsections
3. Develop each `###` sub-subsection **independently, minimum 300-500 words**
4. If a `###` topic cannot sustain 300 words, merge it into its neighbor

### Length — NO UPPER LIMIT

**There is NO word limit.** Write as much as the topic demands. A rich chapter (e.g., flood forecasting, groundwater modeling) may be 15,000-20,000 words. A more compact chapter may be 6,000. **The minimum is 8,000 words/chapter** unless the topic genuinely cannot sustain it.

### Depth

Where the lecture notes list, you **elaborate**. Every substantive list item gets 2-4 sentences — how, why, when, what trade-offs. Where there's a formula, provide the full derivation or at least the physical interpretation, and a **fully worked numerical example**.

### Mathematics

Embed formulas in text, explain the terms. LaTeX: `$inline$`, `$$display$$`. Consistent notation.

**Worked examples**: full development. Input data → formula substitution → intermediate steps → result with units → interpretation of the result.

### Tables and Lists

Every table must have a number and caption:
```markdown
**Table X.Y**: Description of what the table shows

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| data     | data     | data     |
```

### Figures and Illustrations — MANDATORY PLACEHOLDERS

Every chapter must contain **at least 5-8 figure placeholders**. Format:

```markdown
<!-- FIGURE X.Y:
PROMPT FOR IMAGE GENERATION (English): "Create a technical diagram showing [detailed description].
Style: clean vector illustration, white background, labeled axes."
-->

**Figure X.Y**: [Caption describing what the figure shows and what the reader should notice]
```

### International Content — MANDATORY

Every chapter must include at least ONE of:
- An equivalence table (US / Hungary-EU / Global datasets)
- A Hungarian case study or worked example
- A "Global Perspective" box or section

Use the verified data sources from:
- `C:/maidment_hidroGIS/Hungarian_EU_Data_Sources.md`
- `C:/maidment_hidroGIS/international_data_sources.md`

### Modern Context

2025/2026 state of practice, organically integrated. For rapidly changing topics, avoid specific version numbers.

### References

At chapter end, `## References`, 5-15 entries. **Only real, existing sources.** Do NOT invent books or URLs.

### Cross-references

Reference other chapters where appropriate. The chapters:

**Part I: The Water Information Landscape**
1. Why Hidroinformatics Matters
2. Mapping Water: From Paper to Pixels
3. Where the Data Lives
4. GIS as a Water Tool

**Part II: Reading the Landscape**
5. The Grid: How Computers See Terrain
6. Calculating with Maps
7. Slope, Aspect, and the Shape of the Land
8. Measuring Rain Where It Falls

**Part III: Following the Water Downhill**
9. Preparing the Digital Landscape
10. Which Way Does Water Flow?
11. Drawing Watersheds from Data
12. Automating the Workflow

**Part IV: When Water Becomes Dangerous**
13. Seeing the Ground in 3D: LiDAR
14. How High Above the River?
15. Mapping Where Floods Go
16. Forecasting Floods in Real Time
17. Who Lives in the Flood Zone?

**Part V: The Hidden Water**
18. Seeing Underground: 3D Subsurface GIS
19. Wells, Boreholes, and Aquifer Maps
20. Building a Picture of the Underground
21. Simulating Groundwater Flow

**Part VI: The Intelligent Water System**
22. When Models Meet Data
23. AI as a Hydrologist's Assistant
24. Agentic AI: The Autonomous Modeler
25. The Future of Water Intelligence

### DO NOT

- Do not write learning objectives, summaries, or review questions
- Do not write empty introductory paragraphs
- Do not reference the PPT or original lecture notes
- Do not use emoji
- Do not invent non-existent references
- Do not leave 5-line subsections — elaborate everything substantively
- Do not leave unexpanded lists about substantive topics
- Do not embed technical elements (URLs, commands) in flowing prose
- Do not leave tables without numbers and captions
- Do not present US systems as the only option without international equivalents

---

## Usage Schema

```
{this prompt}

CHAPTER-SPECIFIC INSTRUCTION:
- Chapter number and title: [Chapter X: ...]
- Source material (v1, read as starting point): [C:/maidment_hidroGIS/lecture_notes/chXX.md]
- Additional sources: [list any Arc Hydro GW chapters, Handbook parts, etc.]
- Output file: [C:/maidment_hidroGIS/chapters_v2/chXX.md]
- Content description (from BOOK_CONCEPT_2026.md): [...]
- Environmental/application thread: [...]

TASK:
1. Read the v1 version as a starting point — don't copy, develop further
2. Read the BOOK_CONCEPT_2026.md for the full chapter description
3. Read the internationalization guide for this chapter's specific requirements
4. Write the v2 version to chapters_v2/
5. Check: any 5-line subsections? Unexpanded lists? Unnumbered tables? Figure placeholders? International content?
```
