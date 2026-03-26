# Hidro-Tutor — Multi-Agent Adaptive Learning System

## Project Overview
An AI-powered hidroinformatics tutoring system built on Gemini's free API tier, using RAG
over "The State of Hidroinformatics in 2026" / "A hidroinformatika helyzete 2026-ban"
(25 chapters) by Feher Zsolt Zoltan.
Bilingual support: full English and Hungarian content (chapters, question banks, UI).
The system uses multiple specialized agents coordinated by an orchestrator, with adaptive
learning, intelligent caching, and model routing to stay within free tier limits.
Default landing page is the preface (chapter 0). Sidebar shows 3 levels: Part / Chapter / Section, plus appendices.

## Architecture

### Core Principle: ZERO COST TO OPERATOR
- All LLM calls go through Google Gemini free tier API (no billing account)
- Model routing: Flash-Lite (1000 RPD) -> Flash (250 RPD) -> Pro (100 RPD)
- Aggressive response caching to minimize API calls
- Graceful degradation when daily quota is exhausted

### Stack
- **Backend**: FastAPI (Python 3.11+)
- **LLM**: Google Gemini API (free tier) — gemini-2.5-flash-lite, gemini-2.5-flash, gemini-2.5-pro
- **Embeddings**: Local — sentence-transformers (all-MiniLM-L6-v2)
- **Vector DB**: ChromaDB (local, file-based, no server needed)
- **Database**: SQLite (student state, cache, analytics)
- **Frontend**: React + Vite + TailwindCSS
- **Book content**: 25 Markdown chapters in chapters_v2/ (EN) and chapters_hu/ (HU)
- **Bilingual chapters**: Backend `lang` query param switches between EN/HU content

### Directory Structure
```
hidro-tutor/
├── CLAUDE.md
├── backend/
│   ├── main.py                  # FastAPI entry point
│   ├── config.py                # Settings, API keys, model config
│   ├── agents/
│   │   ├── orchestrator.py      # Intent classification + routing
│   │   ├── rag_agent.py         # Retrieval + answer generation
│   │   ├── quiz_agent.py        # Adaptive quiz generation
│   │   └── socratic_agent.py    # Guided discovery through questions
│   ├── rag/
│   │   ├── ingest.py            # Markdown chapters -> chunks -> embeddings -> ChromaDB
│   │   ├── chunker.py           # Section-aware chunking with metadata
│   │   ├── retriever.py         # Query -> relevant chunks
│   │   └── concept_graph.py     # Topic dependency graph
│   ├── models/
│   │   ├── gemini_client.py     # Gemini API wrapper with rate limiting + routing
│   │   ├── rate_limiter.py      # Token bucket per model, daily counters
│   │   └── cache.py             # Semantic response cache (SQLite-backed)
│   ├── student/
│   │   ├── models.py            # Pydantic models
│   │   ├── knowledge_tracer.py  # Bayesian Knowledge Tracing
│   │   └── session.py           # Session management
│   ├── db/
│   │   └── database.py          # SQLite setup
│   └── utils/
│       └── text.py              # Text processing helpers
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── Chat.jsx
│   │   │   ├── QuizPanel.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   └── Sidebar.jsx
│   │   ├── hooks/
│   │   └── api/
│   │       └── client.js
│   └── index.html
├── data/
│   ├── raw/                     # Symlink or copy chapter .md files here
│   ├── chunks/                  # Processed chunks (JSON)
│   ├── chroma_db/               # ChromaDB persistent storage
│   ├── qbank_parts/             # 10,000 English questions (25 x 400 per chapter)
│   └── qbank_parts_hu/          # 10,000 Hungarian questions (25 x 400 per chapter)
├── scripts/
│   ├── ingest_book.py           # CLI: process chapters into vector store
│   └── seed_concept_graph.py    # CLI: initialize topic dependencies
├── tests/
├── requirements.txt
└── .env.example
```

## Book Structure (25 chapters, 6 parts)
- **Part I: Foundations** (Ch 1-4):
  1. Why Hidroinformatics Matters
  2. Mapping Water: From Paper to Pixels
  3. Where the Data Lives
  4. GIS as a Water Tool
- **Part II: Terrain Analysis** (Ch 5-8):
  5. The Grid: How Computers See Terrain
  6. Calculating with Maps
  7. Slope, Aspect, and the Shape of the Land
  8. Measuring Rain Where It Falls
- **Part III: Watershed Delineation** (Ch 9-12):
  9. Preparing the Digital Landscape
  10. Which Way Does Water Flow?
  11. Drawing Watersheds from Data
  12. Automating the Workflow
- **Part IV: Flood Hazard** (Ch 13-17):
  13. Seeing the Ground in 3D: LiDAR
  14. How High Above the River?
  15. Mapping Where Floods Go
  16. Forecasting Floods in Real Time
  17. Who Lives in the Flood Zone?
- **Part V: Groundwater** (Ch 18-21):
  18. Seeing Underground: 3D Subsurface GIS
  19. Wells, Boreholes, and Aquifer Maps
  20. Building a Picture of the Underground
  21. Simulating Groundwater Flow
- **Part VI: AI and the Future** (Ch 22-25):
  22. When Models Meet Data
  23. AI as a Hydrologist's Assistant
  24. Agentic AI: The Autonomous Modeler
  25. The Future of Water Intelligence

## Coding Standards
- Python: type hints everywhere, pydantic models for all data structures
- Async: use async/await for all I/O
- Error handling: never let an API failure crash the system — always degrade gracefully
- Logging: structured logging, log every LLM call with token counts
- Frontend: functional components, hooks
- Language: content bilingual (EN/HU), UI bilingual
- Comments: English

## Critical Design Decisions
1. **Embeddings are LOCAL** — never use Gemini for embeddings (wastes quota)
2. **Cache aggressively** — identical or semantically similar questions return cached responses
3. **Rate limiter is the gatekeeper** — every LLM call goes through rate_limiter.py
4. **Student model persists** — SQLite stores all student progress across sessions
5. **Book structure metadata** — every chunk carries chapter/section/subsection info
6. **Concept graph** — topics have prerequisites; system won't quiz on advanced topics before basics
7. **Fallback mode** — when quota exhausted: serve cached answers, static content, concept graph navigation
8. **Markdown source** — chapters are .md files with clear heading structure (# Chapter, ## Section, ### Subsection)
9. **Bilingual support** — EN/HU toggle, backend `lang` query param, separate question banks per language
10. **Question bank serving** — Pre-generated questions served from JSON files, no LLM needed for quiz/flashcards
11. **Local quiz evaluation** — /quiz/evaluate endpoint grades MCQ/TF/fill-blank locally without LLM
12. **GPT-5.4 lector pipeline** — Hungarian chapter quality ensured via run_lector_api.py (200-line chunks, JSON fix format, ~2,450 fixes across all chapters + appendices). Kázmer glossary for terminology, Marton (2009) for style.

## Known Issues
- Hungarian RAG index not yet created — search/chat returns English results when in HU mode (HU collection exists but chat language routing may need testing)
