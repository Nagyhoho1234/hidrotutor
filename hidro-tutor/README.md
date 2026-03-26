# Hidro-Tutor

RAG-based AI tutoring system for **"The State of Hidroinformatics in 2026"** by Feher Zsolt Zoltan.

Multi-agent architecture using Google Gemini free tier, ChromaDB, local embeddings, and adaptive learning.

## Architecture

```
Student  -->  FastAPI Backend  -->  Orchestrator  -->  RAG Agent (book answers)
                |                                 -->  Quiz Agent (adaptive quizzes)
                |                                 -->  Socratic Agent (guided discovery)
                |
                +--> ChromaDB (25 chapters, embedded locally)
                +--> SQLite (student state, cache, analytics)
                +--> Gemini API (free tier, rate-limited)
```

**Zero cost to operate.** All LLM calls use Gemini free tier. Embeddings are local (sentence-transformers). Data stays on your machine.

## Quick Start

### 1. Prerequisites

- Python 3.11+
- Node.js 18+
- A free Gemini API key from https://aistudio.google.com/apikey

### 2. Backend Setup

```bash
cd hidro-tutor

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure
copy .env.example .env
# Edit .env and paste your GEMINI_API_KEY
```

### 3. Ingest the Book

```bash
# From hidro-tutor directory (with venv active)
python -m scripts.ingest_book
```

This reads all 25 chapters from `../chapters_v2/`, chunks them by section, computes embeddings locally, and stores everything in ChromaDB. Takes 2-5 minutes depending on hardware.

To verify the concept graph:
```bash
python -m scripts.seed_concept_graph
```

### 4. Start the Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

Test it:
- http://localhost:8000/health
- http://localhost:8000/quota-status
- http://localhost:8000/concepts
- http://localhost:8000/test-generate?prompt=What+is+HAND

### 5. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 in your browser.

## Project Structure

```
hidro-tutor/
  backend/
    main.py              # FastAPI app with all endpoints
    config.py            # Settings from .env
    agents/
      orchestrator.py    # Intent classification + routing
      rag_agent.py       # Book Q&A with retrieval
      quiz_agent.py      # Adaptive quiz generation
      socratic_agent.py  # Guided discovery
    rag/
      chunker.py         # Markdown -> chunks with metadata
      ingest.py          # Chunks -> embeddings -> ChromaDB
      retriever.py       # Query -> relevant chunks
      concept_graph.py   # 35 concepts with prerequisites
    models/
      gemini_client.py   # API wrapper with model routing
      rate_limiter.py    # RPM + RPD limits per model
      cache.py           # Semantic response cache
    student/
      knowledge_tracer.py  # Bayesian Knowledge Tracing
      session.py           # Conversation persistence
    db/
      database.py        # SQLite schema
  frontend/
    src/
      App.jsx            # Main layout
      components/
        Chat.jsx         # Chat interface with markdown rendering
        Sidebar.jsx      # Book table of contents navigation
        ProgressBar.jsx  # API quota indicator
        QuizPanel.jsx    # Interactive quiz UI
  scripts/
    ingest_book.py       # CLI: chapters -> vector store
    seed_concept_graph.py # CLI: display concept graph
  data/
    chroma_db/           # Vector store (generated)
    chunks/              # Chunk index JSON (generated)
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/quota-status` | GET | Gemini API quota status |
| `/cache-stats` | GET | Response cache statistics |
| `/chat` | POST | Main chat (auto-routes to agents) |
| `/quiz` | POST | Generate quiz questions |
| `/quiz/answer` | POST | Submit quiz answer, update BKT |
| `/concepts` | GET | Full concept dependency graph |
| `/student/{id}/mastery` | GET | Student mastery summary |
| `/student/{id}/weak-topics` | GET | Topics needing review |
| `/student/{id}/history` | GET | Conversation history |
| `/test-generate` | GET | Test Gemini API connectivity |

## Gemini Model Routing

| Complexity | Model | RPM | RPD |
|-----------|-------|-----|-----|
| Low (definitions, lookups) | gemini-2.5-flash-lite | 15 | 1000 |
| Medium (explanations) | gemini-2.5-flash | 10 | 250 |
| High (synthesis, comparison) | gemini-2.5-pro | 5 | 100 |

When a model's quota is exhausted, the system falls back to the next lower tier. When all quotas are gone, it serves cached answers and raw book excerpts.

## Book Coverage

25 chapters organized in 6 parts:

- **Part I (Ch 1-4):** Foundations -- water crisis, CRS, data sources, GIS basics
- **Part II (Ch 5-8):** Terrain Analysis -- DEMs, map algebra, slope/aspect, rainfall
- **Part III (Ch 9-12):** Watersheds -- pit filling, flow direction, delineation, Python automation
- **Part IV (Ch 13-17):** Flood Hazard -- LiDAR, HAND, inundation mapping, forecasting, exposure
- **Part V (Ch 18-21):** Groundwater -- 3D GIS, wells, hydrogeologic modeling, MODFLOW
- **Part VI (Ch 22-25):** AI -- calibration, ML in hydrology, agentic AI, digital twins
