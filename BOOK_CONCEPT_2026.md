# The State of Hidroinformatics in 2026

## Vision
A comprehensive, application-centric **online knowledge base** (~600 pages) for scientists, engineers, water managers, students, and decision-makers. Not an AI textbook. Not a GIS manual. A practical guide showing **how modern tools solve real water problems**, with AI as one tool among many.

The reader should finish each chapter understanding: "Here's a water problem. Here's what data exists. Here's how we solve it today."

## Format: Interactive Online Asset
- **RAG-enabled** — readers can ask questions about any chapter, get answers with citations
- **Searchable TOC** with cross-linked chapters and concepts
- **Interactive navigation** — topic index, concept map, chapter dependencies
- **Embedded resources** — links to live data portals, downloadable datasets, video lectures
- **Layered depth** — summary boxes for quick readers, expandable deep-dive sections for specialists
- **~600 pages** equivalent, ~25 pages per chapter average
- **Living document** — updatable as data sources and tools evolve

## Guiding Principles
- **Problem-first, tool-second** — every chapter starts with a real water challenge
- **Layered content** — executive summary → practical walkthrough → technical deep-dive
- **International** — Hungary as primary example, US as reference, global alternatives
- **2026 state of practice** — what's operational today, not theoretical
- **AI where it helps** — agentic AI for parameterization as a practical capability, not as the main topic
- **Self-contained** — every chapter works standalone for RAG retrieval

## Proposed Structure (25 chapters)

### PART I: The Water Information Landscape
1. **Why Hidroinformatics Matters** — water crises (floods, drought, groundwater depletion), why spatial data + computing changed everything, the Maidment/Tarboton legacy
2. **Mapping Water: From Paper to Pixels** — coordinate systems, projections, how maps work (accessible version of geodesy)
3. **Where the Data Lives** — global tour of water data: US (USGS, NHDPlus), EU (Copernicus, EFAS), Hungary (OVF, OMSZ), Asia/Africa (HydroSHEDS, CHIRPS)
4. **GIS as a Water Tool** — what GIS does for hydrology, from desktop to cloud, the three views (geodatabase, visualization, processing)

### PART II: Reading the Landscape
5. **The Grid: How Computers See Terrain** — raster fundamentals, DEMs, resolution trade-offs
6. **Calculating with Maps** — map algebra, combining layers, the precipitation-minus-infiltration paradigm
7. **Slope, Aspect, and the Shape of the Land** — how terrain derivatives drive water movement
8. **Measuring Rain Where It Falls** — interpolation, rain gauges vs. radar vs. satellite, watershed averaging

### PART III: Following the Water Downhill
9. **Preparing the Digital Landscape** — DEM conditioning (pit filling, stream burning) — why raw DEMs don't work for hydrology
10. **Which Way Does Water Flow?** — flow direction, flow accumulation, the digital river network
11. **Drawing Watersheds from Data** — automated watershed delineation, stream networks, comparison with mapped rivers
12. **Automating the Workflow** — scripting with Python, processing thousands of watersheds

### PART IV: When Water Becomes Dangerous
13. **Seeing the Ground in 3D: LiDAR** — how laser scanning revolutionized terrain mapping
14. **How High Above the River?** — the HAND concept, flood-prone terrain identification
15. **Mapping Where Floods Go** — inundation mapping, rating curves, damage estimation
16. **Forecasting Floods in Real Time** — NWM, EFAS, GloFAS, Hungarian systems — operational flood forecasting today
17. **Who Lives in the Flood Zone?** — population exposure, building databases, emergency response

### PART V: The Hidden Water
18. **Seeing Underground: 3D Subsurface GIS** — representing geology and aquifers in 3D
19. **Wells, Boreholes, and Aquifer Maps** — groundwater data collection and management
20. **Building a Picture of the Underground** — hydrogeologic framework modeling
21. **Simulating Groundwater Flow** — MODFLOW and finite-difference modeling in practice

### PART VI: The Intelligent Water System
22. **When Models Meet Data** — the calibration problem, why hydrological models need tuning, traditional approaches (manual, SCE-UA, DREAM)
23. **AI as a Hydrologist's Assistant** — practical ML applications: flood prediction with LSTM, groundwater level forecasting, satellite-based ET estimation — application examples, not theory
24. **Agentic AI: The Autonomous Modeler** — how AI agents run models, evaluate results, and optimize parameters autonomously. Practical demonstration: an agent calibrating a rainfall-runoff model for a Hungarian catchment. What this means for water management in 2026.
25. **The Future of Water Intelligence** — digital twins, real-time data assimilation, climate adaptation, open science, the convergence of sensors + models + AI

### Appendices
- A. **Data Source Quick Reference** — table of all datasets mentioned, with URLs
- B. **Software Guide** — ArcGIS, QGIS, TauDEM, HEC-HMS, MODFLOW, Python
- C. **Hungarian Water Data Portal Guide** — step-by-step for data.vizugy.hu, OMSZ, KSH
- D. **Glossary**

---

## Chapter Design Template
Each chapter follows this pattern:
1. **The Problem** (1 page) — a real-world water challenge, with a photo/map
2. **The Science** (3-5 pages) — accessible explanation of the underlying concepts
3. **The Practice** (3-5 pages) — how it's done today, with real examples and results
4. **Hungarian Example** (1-2 pages) — applied to a Hungarian watershed or dataset
5. **Global Perspective** (1 page) — how this applies in Asia, Africa, Middle East
6. **Key Takeaways** (half page) — bullet summary

---

## What Changes from Current State

| Current (19 chapters) | New (25 chapters) | Change |
|---|---|---|
| Ch 1-4: Foundations | Part I (Ch 1-4): Water Information Landscape | Rewritten for general public, less technical |
| Ch 5-8: Raster Analysis | Part II (Ch 5-8): Reading the Landscape | Same content, accessible titles/language |
| Ch 9-12: Terrain Hydrology | Part III (Ch 9-12): Following the Water | Same content, accessible framing |
| Ch 13-17: Flood Analysis | Part IV (Ch 13-17): When Water Becomes Dangerous | Same content + EFAS/Hungarian systems |
| Ch 18-19: Water Info | Absorbed into other chapters | Ch 18 → Part I; Ch 19 → Part II/VI |
| — | Part V (Ch 18-21): The Hidden Water | NEW from Arc Hydro GW |
| — | Part VI (Ch 22-25): The Intelligent Water System | NEW: AI/ML applications + Agentic AI |

## Content Depth — No Limits
Size is unlimited. Each chapter grows to whatever depth the topic needs. Some chapters may be 10 pages, others 50. The online format has no printing constraints.

This allows:
- Rich worked examples with real data
- Hungarian + international case studies in every chapter
- Detailed figures, maps, and result visualizations
- "Try it yourself" interactive boxes with data download links
- Further reading sections linking to the Handbook of HydroInformatics for ML deep-dives
- Full derivations where they matter, skippable for casual readers via layered depth

## RAG Architecture Notes
- Each chapter should be **self-contained** with its own context (definitions, data source references)
- Use consistent **metadata tags** per chapter: topic, methods, datasets, regions, difficulty level
- Include a **concept index** that maps questions to chapters (e.g., "How do I delineate a watershed?" → Ch 11)
- Every data source mention should include a **structured reference block** (name, URL, coverage, format, access) for RAG extraction

## Key Design Decisions

1. **Ch 24 (Agentic AI)** — Practical demonstration, not theory. Show an agent calibrating a model step by step. Use a Hungarian catchment (e.g., Zala River). Include results and workflow diagrams, not raw code.

2. **Tone** — Accessible to a water manager or MSc student, not just GIS specialists. Minimize jargon. Define every acronym. Use analogies. Layer complexity (summary → detail → deep-dive).

3. **Interactive features** — Embedded links to live data portals, downloadable sample datasets, video lecture clips from Maidment's course where relevant.

4. **Updatability** — Design chapters as modular units. When a data portal URL changes or a new tool emerges, only one chapter needs updating.
