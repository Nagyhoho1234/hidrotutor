# Gap Analysis: gis-tutor vs hidro-tutor

**Generated**: 2026-03-25
**Reference**: `C:\gis-konyv2025\gis-tutor\` (mature, production-deployed)
**Target**: `C:\maidment_hidroGIS\hidro-tutor\` (early scaffold)

---

## 1. Feature Comparison Table

| Feature | gis-tutor | hidro-tutor | Status |
|---------|-----------|-------------|--------|
| **DATA LAYER** | | | |
| Book chunks (JSON) | 550 chunks, `chunks.json` | 1,115 chunks, `chunks_index.json` | HAVE (more chunks) |
| Chunk metadata fields | text, metadata.part, chapter, chapter_num, section, heading_level, chunk_type, tokens, sub_chunk | chunk_id, text, chapter, section, subsection, chunk_type, token_count | PARTIAL -- missing part, heading_level, sub_chunk tracking |
| Table of Contents (`toc.json`) | Structured: parts > chapters > sections with page_start, section IDs | None | MISSING |
| Concept graph (`concept_graph.json`) | 24 nodes, 64 edges; per-node: name, chapter_num, difficulty, topics[] | Script exists (`seed_concept_graph.py`) but no data file generated | MISSING (data) |
| Question bank (`question_bank.json`) | 7,339 pre-generated questions across all 24 chapters; types: mcq, true_false, fill_blank, essay | None | MISSING |
| Chapter images | 100+ figure PNGs (`fig_X_Y.png`) | None | MISSING |
| Raw book chapters | 24 `.md` files | `data/raw/` directory exists (contents unknown) | PARTIAL |
| **BACKEND AGENTS** | | | |
| Orchestrator | Intent classification + agent routing | Present | HAVE |
| RAG agent | Retrieval + answer generation | Present | HAVE |
| Quiz agent | Bank-first (zero cost), LLM fallback, adaptive difficulty via mastery, essay grading, multi-chapter selection, question type filtering | Basic LLM-only generation, no bank, no adaptive difficulty, no essay grading | PARTIAL -- needs major upgrade |
| Socratic agent | Guided discovery | Present | HAVE |
| Code Lab agent (`code_lab_agent.py`) | Interactive code exercises | None | MISSING |
| Book content server (`book_content.py`) | Serves chapter text for in-app reading | None | MISSING |
| **BACKEND INFRASTRUCTURE** | | | |
| Gemini client with model routing | Flash-Lite > Flash > Pro cascade, quota tracking | Present | HAVE |
| Rate limiter | Token bucket per model | Present | HAVE |
| Response cache | SQLite-backed semantic cache | Present | HAVE |
| Knowledge tracer | Bayesian KT, per-chapter mastery | Present | HAVE |
| Session management | SQLite persistence | Present | HAVE |
| **FRONTEND COMPONENTS** | | | |
| Chat | Conversational interface | Present | HAVE |
| Sidebar | Chapter navigation | Present | HAVE |
| Progress bar | Mastery visualization | Present | HAVE |
| Quiz panel | Full-featured: chapter multi-select, question type toggles, question count, one-at-a-time flow, per-question results, PDF export, "Answers in Book" link | Basic: receives questions as prop, simple MCQ flow, no chapter selection, no type filtering, no export | PARTIAL -- needs rewrite |
| Concept map (`ConceptMap.jsx`) | Interactive SVG DAG with color-coded parts, hover highlighting, click-to-open chapter, legend, topological layout | None | MISSING |
| Flashcards / SRS (`Flashcards.jsx`) | SM-2 spaced repetition, localStorage persistence, due/new/learned counts, keyboard shortcuts, 4-level rating (again/hard/good/easy), interval prediction | None | MISSING |
| Book reader (`BookReader.jsx`) | In-app chapter reading with search highlight | None | MISSING |
| Quiz results (`QuizResults.jsx`) | Dedicated results view | None | MISSING |
| Search bar (`SearchBar.jsx`) | Full-text search across book | None | MISSING |
| Settings (`Settings.jsx`) | User preferences | None | MISSING |
| Quota bar (`QuotaBar.jsx`) | API quota usage display | None | MISSING |
| Error boundary (`ErrorBoundary.jsx`) | React error boundary | None | MISSING |
| Custom hooks (`useChat`, `useMobile`, `useSession`) | Chat state, mobile detection, session management | None (logic inline) | MISSING |
| **BILINGUAL SUPPORT** | | | |
| Hungarian + English UI | Full `lang` prop threading, all strings in both languages | English only | MISSING (English-only is fine for this book, but no lang toggle) |
| **DEVOPS** | | | |
| Docker (backend + frontend) | `Dockerfile.backend`, `frontend/Dockerfile`, `docker-compose.yml`, `nginx.conf` | None | MISSING |
| Production build (`frontend/dist/`) | Pre-built with KaTeX font assets | None | MISSING |
| Start scripts (`start.bat`, `start.sh`) | One-click launch | None | MISSING |
| Tests | `test_api.py`, `test_retriever.py`, `conftest.py` | Empty `tests/` directory | MISSING |
| CITATION / Zenodo | `.zenodo.json`, `CITATION.cff` | None | MISSING (not urgent) |
| Question bank generation scripts | 15+ scripts for batch question generation | None | MISSING |

---

## 2. What We Need to Add

### Critical (blocks core tutoring functionality)

1. **Question bank** -- Generate 2,000+ pre-made questions across all 25 chapters (MCQ, true/false, fill-in-blank, essay). This eliminates API cost for quizzes and enables offline operation. Port the bank generation scripts from gis-tutor.

2. **Concept graph data** -- Run `seed_concept_graph.py` or create `data/chunks/concept_graph.json` with 25 nodes (one per chapter), difficulty levels, topic lists, and prerequisite edges. The script exists; the data does not.

3. **TOC data** -- Create `data/chunks/toc.json` with the 6-part, 25-chapter structure including section IDs. Needed for chapter selection UI and book navigation.

4. **Quiz agent upgrade** -- Rewrite `quiz_agent.py` to match gis-tutor's capabilities:
   - Bank-first strategy (pick from pre-generated questions, zero API cost)
   - Multi-chapter selection
   - Question type filtering
   - Adaptive difficulty based on student mastery
   - Essay grading via LLM
   - UUID assignment to questions

5. **Quiz panel rewrite** -- Replace the basic QuizPanel with gis-tutor's full version:
   - Chapter multi-select with All/None toggles
   - Question type toggle buttons
   - Configurable question count (1-20)
   - One-question-at-a-time navigation with progress bar
   - Per-question result display with explanations
   - PDF export
   - Score summary with percentage

### High Priority (significant learning value)

6. **SRS Flashcards component** -- Port `Flashcards.jsx` with SM-2 algorithm, localStorage persistence, and keyboard shortcuts. This is the single highest-impact learning feature after quizzes.

7. **Concept map component** -- Port `ConceptMap.jsx` for interactive chapter dependency visualization. Adapt part colors and chapter groupings for the 25-chapter hidroinformatics structure.

8. **Book reader component** -- Add `BookReader.jsx` so students can read chapters in-app with search highlighting, instead of needing a separate PDF/file viewer.

### Medium Priority (polish and usability)

9. **Search bar** -- Full-text search across all chunks, showing results with chapter/section context.

10. **Error boundary** -- Wrap the app in a React error boundary to prevent white-screen crashes.

11. **Quota bar** -- Display remaining Gemini API quota so users know when they're approaching limits.

12. **Custom hooks** -- Extract chat logic, session management, and mobile detection into reusable hooks (`useChat.js`, `useSession.js`, `useMobile.js`).

13. **Quiz results component** -- Dedicated results view that can be opened from chat ("show me where I went wrong").

14. **Settings component** -- Dark/light mode toggle, language preference, session reset.

### Low Priority (deployment and maintenance)

15. **Docker deployment** -- `Dockerfile.backend`, `frontend/Dockerfile`, `docker-compose.yml`, `nginx.conf`.

16. **Start scripts** -- `start.bat` and `start.sh` for one-click local launch.

17. **Tests** -- Port `test_api.py` and `test_retriever.py`, adapt for hidroinformatics content.

18. **Chapter images** -- Generate or source 5 figures per chapter (125 total) for visual learning.

19. **Code Lab agent** -- Interactive Python/GIS code exercises (gis-tutor has this, but it is domain-specific and needs full rewrite for hydrology).

---

## 3. Priority Ranking

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P0 | Question bank generation (2,000+ questions) | HIGH | Eliminates API cost for quizzes, enables offline |
| P0 | Quiz agent rewrite (bank-first + adaptive) | MEDIUM | Core learning loop depends on this |
| P0 | Quiz panel rewrite (full UI) | MEDIUM | Current UI is too basic to use |
| P1 | Concept graph data generation | LOW | Run existing script + manual review |
| P1 | TOC data file | LOW | 1 hour manual creation |
| P1 | SRS Flashcards component | MEDIUM | Highest-impact learning feature after quizzes |
| P1 | Concept map component | MEDIUM | Visual navigation, motivation |
| P2 | Book reader component | MEDIUM | In-app reading convenience |
| P2 | Search bar | LOW | Quick lookup |
| P2 | Error boundary | LOW | 15-minute task |
| P2 | Quota bar | LOW | User awareness |
| P2 | Custom hooks refactor | LOW | Code quality |
| P3 | Docker deployment | MEDIUM | Production readiness |
| P3 | Start scripts | LOW | Developer convenience |
| P3 | Tests | MEDIUM | Maintenance safety |
| P3 | Chapter images | HIGH | Nice-to-have visual content |
| P3 | Code Lab agent | HIGH | Domain-specific, full rewrite needed |

---

## 4. Summary

The hidro-tutor has a solid backend skeleton (Gemini client, rate limiter, cache, RAG pipeline, knowledge tracer, 1,115 chunks ingested) but is missing the **content and UI features** that make gis-tutor an effective learning tool. The three most impactful gaps are:

1. **No question bank** -- every quiz costs API tokens and has no quality control
2. **Primitive quiz UI** -- no chapter selection, no type filtering, no results review
3. **No spaced repetition** -- the single most effective study technique is absent

The recommended build order is: question bank generation -> quiz agent rewrite -> quiz panel rewrite -> concept graph + TOC data -> flashcards -> concept map -> book reader -> everything else.
