# Hidroinformatics — Textbook Project

## Project Purpose
Building an international hydroinformatics textbook from multiple sources: Maidment's "GIS in Water Resources" lectures, Arc Hydro Groundwater book, and the Handbook of HydroInformatics (3 volumes). Target audience: Hungarian university students + international students from Asia, Middle East, Africa.

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

## Directory Structure
- `chapters_v2/` — 25 final English chapter markdown files (ch01-ch25)
- `chapters_hu/` — 25 Hungarian translations (ch01-ch25)
- `lecture_notes/` — 19 original chapter markdown files (ch01-ch19), restructured from lectures
- `transcript/` — 35 TurboScribe transcriptions from lecture videos
- `audio/` — 35 MP3 audio tracks (mono 16kHz 64kbps)
- `originalMaterials/` — Original lecture PPTs and PDFs from Maidment's course
- `originalMaterials/extracted_text/` — Text extracted from PPTs and PDFs
- `books/arc_hydro_gw/` — Arc Hydro Groundwater book (9 chapters + glossary, markdown)
- `books/kazmer_glossary.md` — 17,192-term geological dictionary (Kazmer 2005)
- `hydroAI/` — Handbook of HydroInformatics source PDFs (3 volumes)
- `hydroAI/extracted/` — Extracted text from all 3 volumes (53 files, ~4 MB)
- `hidro-tutor/` — Multi-agent adaptive learning app (FastAPI + React)
- `Hungarian_EU_Data_Sources.md` — 30 verified Hungarian/EU data sources
- `international_data_sources.md` — 38 verified global data sources
- `INTERNATIONALIZATION_PROMPT.md` — Master prompt for internationalizing all chapters

## Source Materials
- **Lecture videos**: 35 MP4s, ~39 hours, `Y:\Fehér Zsolt\Tananyagok\_Maidment_ GIS in Water Resources\Youtube\`
- **Original slides**: 20 PPTXs + 12 PDFs in `originalMaterials/`
- **Arc Hydro Groundwater**: Strassberg, Jones & Maidment (2011), 178 pages
- **Handbook of HydroInformatics**: Eslamian & Eslamian (2023), 3 volumes, ~1326 pages
  - Vol I: Classical & ML Techniques (484 pp, 26 chapters)
  - Vol II: Advanced ML Techniques (420 pp, ~25 chapters)
  - Vol III: Water Data Management (422 pp, ~25 chapters)
  - NOTE: PDF text extraction loses equations/Greek letters. Use extractions for topic indexing only; read original PDFs visually for equations.
- **Marton (2009)**: "Alkalmazott hidrogeologia" — Hungarian applied hydrogeology textbook
- **Kazmer (2005)**: Geological dictionary — 17,192 English-Hungarian geological terms (`books/kazmer_glossary.md`)

## Completed Work
- **25 English chapters** written and finalized (chapters_v2/)
- **25 Hungarian translations** completed (chapters_hu/)
- **Hungarian appendices** translated (preface, exercises, glossary, data_sources, software)
- **GPT-5.4 Hungarian lector pass** — chunked API-based review of all 25 chapters + appendices (~2,450 fixes total). Used Kázmer (2005) glossary for consistent geological/hydrological terminology and Marton (2009) "Alkalmazott hidrogeológia" for Hungarian academic style reference.
- **10,000 English questions** + **10,000 Hungarian questions** (25 × 400 per chapter)
- **Hidro-Tutor app** — multi-agent adaptive learning system (FastAPI + React)

## Pending Tasks
1. Hungarian RAG reindexing — create separate ChromaDB collection for HU chapters
2. Figure images — 168 figures need sourcing/generation
3. Deploy to production server

## Tools
- **ffmpeg 8.1** — `C:\Users\de8xh\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\`
- **python-pptx** — installed in user site-packages
- **TurboScribe** — user's online transcription subscription
- **OpenAI API (GPT-5.4)** — used for Hungarian language lector pass (run_lector_api.py, 200-line chunks, JSON fix format)

## Parallelization
- **Always launch 8-10 agents in parallel** — this is the optimal concurrency for this machine and subscription
- Never batch conservatively (4 at a time) when 8-10 is possible
- The user has ample weekly token budget — use it aggressively

## Conventions
- Chapter files: `chNN.md` in `chapters_v2/` (English) and `chapters_hu/` (Hungarian)
- Hungarian EOV coordinates identified by value range (Northing 0-400k, Easting 400k-1M), not headers
- Transcription done externally via TurboScribe, not locally
