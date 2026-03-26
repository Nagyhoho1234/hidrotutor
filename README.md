# The State of Hidroinformatics in 2026 / A hidroinformatika helyzete 2026-ban

**Bilingual (EN/HU) AI-powered interactive learning platform for hydroinformatics**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Languages: EN/HU](https://img.shields.io/badge/Languages-EN%20%7C%20HU-red.svg)](#)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://react.dev)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19238897.svg)](https://doi.org/10.5281/zenodo.19238897)

> **AI-Generated Content Disclosure**
>
> Both the textbook content (25 chapters, ~700 pages) and the majority of this application's
> source code were generated using **large language models (LLMs)**. The textbook illustrations
> were also AI-generated. This material has not been independently peer-reviewed and should be
> treated as an **educational technology demonstration**, not as an authoritative hydroinformatics reference.

---

## Overview

An interactive learning platform built around a 25-chapter **bilingual** university textbook
on hydroinformatics (*"The State of Hidroinformatics in 2026"*). Based on David Maidment's
"GIS in Water Resources" lectures at UT Austin, enriched with Hungarian hydrogeology from
Marton (2009) and the Arc Hydro Groundwater book.

Students can read the book in English or Hungarian, ask questions about specific passages,
take self-assessment quizzes, study with spaced-repetition flashcards, and explore chapter
dependencies — all with a bilingual interface.

### Key Numbers

| Metric | Count |
|--------|-------|
| Chapters | 25 (EN) + 25 (HU) |
| Appendices | 5 (preface, exercises, glossary, data sources, software) |
| Quiz questions | 10,000 EN + 10,000 HU |
| Question types | MCQ, True/False, Fill-in-blank, Essay |
| Book images | 84 from original lectures |
| Figure captions | 168 with AI generation prompts |
| Kázmer glossary | 17,192 geological terms (EN→HU) |
| RAG chunks | 1,115 EN + 1,237 HU |

---

## Features

| Feature | Description |
|---|---|
| **Book Reader** | 25-chapter textbook with markdown, LaTeX equations, tables, images |
| **EN/HU Toggle** | Full bilingual support — chapters, quiz, UI, sidebar |
| **AI Chat** | RAG-powered Q&A grounded in textbook content (both languages) |
| **Text Selection** | Highlight any passage and ask questions about it |
| **Quiz System** | 20,000 pre-generated questions, local grading, PDF export |
| **Flashcards** | SM-2 spaced repetition with 4-level quality rating |
| **Concept Map** | Interactive SVG dependency graph of all 25 chapters |
| **Chapter Summary** | AI-generated bullet-point summaries (cached) |
| **Full-Text Search** | Search across all chapters with highlighted excerpts |
| **Cross-References** | Clickable chapter links in text |
| **3-Level TOC** | Sidebar with Part / Chapter / Section navigation |
| **Dark Mode** | Light/dark theme |
| **Mobile Layout** | Responsive design for phone/tablet |

---

## Book Structure (25 Chapters, 6 Parts)

### Part I: Foundations
1. Why Hidroinformatics Matters
2. Mapping Water: From Paper to Pixels
3. Where the Data Lives
4. GIS as a Water Tool

### Part II: Terrain Analysis
5. The Grid: How Computers See Terrain
6. Calculating with Maps
7. Slope, Aspect, and the Shape of the Land
8. Measuring Rain Where It Falls

### Part III: Watershed Delineation
9. Preparing the Digital Landscape
10. Which Way Does Water Flow?
11. Drawing Watersheds from Data
12. Automating the Workflow

### Part IV: Flood Hazard
13. Seeing the Ground in 3D: LiDAR
14. How High Above the River?
15. Mapping Where Floods Go
16. Forecasting Floods in Real Time
17. Who Lives in the Flood Zone?

### Part V: Groundwater
18. Seeing Underground: 3D Subsurface GIS
19. Wells, Boreholes, and Aquifer Maps
20. Building a Picture of the Underground
21. Simulating Groundwater Flow

### Part VI: AI and the Future
22. When Models Meet Data
23. AI as a Hydrologist's Assistant
24. Agentic AI: The Autonomous Modeler
25. The Future of Water Intelligence

---

## Architecture

```
┌─────────────┐     ┌──────────────────────────────────┐
│   Browser    │     │        Backend (FastAPI)          │
│              │     │                                    │
│  React +     │◄───►│  /chat      — RAG Q&A (EN/HU)    │
│  Vite +      │     │  /quiz/*    — 20K question bank   │
│  TailwindCSS │     │  /book/*    — Bilingual chapters  │
│  KaTeX       │     │  /concepts  — Dependency graph    │
│              │     │                                    │
│  localStorage│     │  ChromaDB   — Vector search (2    │
│  (SRS state, │     │              collections: EN/HU)  │
│   lang pref) │     │  SQLite     — Student state       │
│              │     │  sentence-transformers (local)     │
└─────────────┘     └──────────────────────────────────┘
```

---

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+

### Backend

```bash
cd hidro-tutor
pip install -r requirements.txt
cd ..
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --app-dir hidro-tutor
```

### Frontend

```bash
cd hidro-tutor/frontend
npm install
npx vite --host 0.0.0.0 --port 5173
```

Open **http://localhost:5173** in your browser.

---

## Source Materials

- **Maidment, D.R.** — "GIS in Water Resources" lecture series, University of Texas at Austin
- **Maidment, D.R.** (2002) — *Arc Hydro: GIS for Water Resources*, ESRI Press
- **Strassberg, Jones & Maidment** (2011) — *Arc Hydro Groundwater*, ESRI Press
- **Marton, L.** (2009) — *Alkalmazott hidrogeológia* (Applied Hydrogeology), ELTE Eötvös Kiadó
- **Kázmer, M.** (2005) — *Angol-magyar geológiai szótár*, Hantken Kiadó (17,192 terms)
- **Eslamian & Eslamian** (2023) — *Handbook of HydroInformatics*, 3 volumes

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Citation

See [CITATION.cff](CITATION.cff) for BibTeX-compatible citation information.

---

## Author

**Fehér Zsolt Zoltán**
University of Debrecen, Department of Environmental Sciences
ORCID: [0009-0007-6659-4197](https://orcid.org/0009-0007-6659-4197)
