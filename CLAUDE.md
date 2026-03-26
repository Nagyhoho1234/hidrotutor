# Hidroinformatics — Textbook Project

## Project Purpose
Building an international hydroinformatics textbook from multiple sources: Maidment's "GIS in Water Resources" lectures, Arc Hydro Groundwater book, and the Handbook of HydroInformatics (3 volumes). Target audience: Hungarian university students + international students from Asia, Middle East, Africa.

## GitHub & DOI
- **Repository**: https://github.com/Nagyhoho1234/hidrotutor
- **Zenodo DOI**: 10.5281/zenodo.19238897
- **License**: MIT

## Current Book Structure (25 chapters, 6 parts)

### Part I: Foundations (Ch 1-4)
1. Why Hidroinformatics Matters
2. Mapping Water: From Paper to Pixels
3. Where the Data Lives
4. GIS as a Water Tool

### Part II: Terrain Analysis (Ch 5-8)
5. The Grid: How Computers See Terrain
6. Calculating with Maps
7. Slope, Aspect, and the Shape of the Land
8. Measuring Rain Where It Falls

### Part III: Watershed Delineation (Ch 9-12)
9. Preparing the Digital Landscape
10. Which Way Does Water Flow?
11. Drawing Watersheds from Data
12. Automating the Workflow

### Part IV: Flood Hazard (Ch 13-17)
13. Seeing the Ground in 3D: LiDAR
14. How High Above the River?
15. Mapping Where Floods Go
16. Forecasting Floods in Real Time
17. Who Lives in the Flood Zone?

### Part V: Groundwater (Ch 18-21)
18. Seeing Underground: 3D Subsurface GIS
19. Wells, Boreholes, and Aquifer Maps
20. Building a Picture of the Underground
21. Simulating Groundwater Flow

### Part VI: AI and the Future (Ch 22-25)
22. When Models Meet Data
23. AI as a Hydrologist's Assistant
24. Agentic AI: The Autonomous Modeler
25. The Future of Water Intelligence

## Directory Structure (GitHub repo — auxiliary data excluded)
- `chapters_v2/` — 25 English chapters + preface + 4 appendices
- `chapters_hu/` — 25 Hungarian chapters + preface + 4 appendices
- `hidro-tutor/` — Bilingual interactive learning app (FastAPI + React)
  - `data/qbank_parts/` — 10,000 English questions (25 × 400)
  - `data/qbank_parts_hu/` — 10,000 Hungarian questions (25 × 400)
- `books/arc_hydro_gw/` — Arc Hydro Groundwater book (9 chapters + glossary, markdown)
- `books/kazmer_glossary.md` — 17,192-term geological dictionary (Kázmer 2005)
- `images/book/` — 84 figure images from original lectures
- `images/figure_captions_all.md` — 168 figure captions with AI generation prompts
- `lector_fixes/` — GPT lector JSON fix files (per chapter)

## Auxiliary Data (local only, not on GitHub)
- `audio/` — 35 MP3 audio tracks
- `transcript/` — 35 TurboScribe transcriptions
- `originalMaterials/` — Original lecture PPTs and PDFs
- `hydroAI/` — Handbook of HydroInformatics PDFs (3 volumes)
- `lecture_notes/` — 19 original chapter markdown files (superseded by chapters_v2/)

## Source Materials
- **Maidment, D.R.** — "GIS in Water Resources" lectures, UT Austin (35 videos, 20 PPTXs, 12 PDFs)
- **Strassberg, Jones & Maidment** (2011) — Arc Hydro Groundwater, ESRI Press
- **Eslamian & Eslamian** (2023) — Handbook of HydroInformatics, 3 volumes
- **Marton, L.** (2009) — "Alkalmazott hidrogeológia", ELTE Eötvös Kiadó
- **Kázmer, M.** (2005) — English-Hungarian Geological Dictionary, Hantken Kiadó

## Completed Work
- 25 English + 25 Hungarian chapters (all lected for language quality)
- 5 appendices in both languages (preface, exercises, glossary, data sources, software)
- Maidment Ex1-5 exercises with US/International/Hungarian variants
- Groundwater chapters (18-21) enriched from Marton (2009)
- 10,000 EN + 10,000 HU quiz questions (MCQ, T/F, fill-blank, essay)
- Bilingual hidro-tutor app with EN/HU toggle
- Hungarian RAG index (1,237 chunks in separate ChromaDB collection)
- Kázmer glossary extracted (17,192 terms)
- Published on GitHub with MIT license, CITATION.cff, Zenodo DOI

## Pending Tasks
1. Figure images — 168 figures need sourcing/generation
2. Deploy to production server
3. Update DOI badges in other GitHub repos (gis-tutor, gslib-reborn, GISChat, QGISChat, SNAPChat)

## Tools
- **ffmpeg 8.1** — audio extraction
- **python-pptx** — PPT text extraction
- **TurboScribe** — online transcription service
- **OpenAI API** — Hungarian language lector (run_lector_api.py)

## Parallelization
- **Always launch 8-10 agents in parallel** — optimal for AMD 9950X / 96GB RAM
- Never batch conservatively (4 at a time) when 8-10 is possible
- When quota is low, limit to 3 agents

## Conventions
- Chapter files: `chNN.md` in `chapters_v2/` (English) and `chapters_hu/` (Hungarian)
- Hungarian text: always proper diacritics (á, é, í, ó, ö, ő, ú, ü, ű) — never ASCII substitutes
- Hungarian EOV coordinates identified by value range (Northing 0-400k, Easting 400k-1M), not headers
- App title: "The State of Hidroinformatics in 2026" / "A hidroinformatika helyzete 2026-ban"
- Default page: preface (chapter 0)
