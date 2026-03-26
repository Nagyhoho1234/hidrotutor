# Master Internationalization Prompt for "Hidroinformatics"

## Context

You are upgrading lecture notes (19 chapters, 5 parts) from a US-centric "GIS in Water Resources" course into an international textbook titled **"Hidroinformatics"**. The target audience is:

- **Primary**: Hungarian university students (Debreceni Egyetem, Környezettudományi Tanszék)
- **Secondary**: International students from Asia, Middle East, and Africa
- Hungary is an EU member state, so Copernicus/EU data infrastructure is native

## Guiding Principles

1. **EXTEND, don't replace.** Keep the US examples — they are well-documented and technically excellent. Add Hungarian/EU as the primary parallel, and global alternatives for international students.
2. **Three-tier approach** for every dataset/system mentioned:
   - **US original** (keep, label as "In the United States...")
   - **Hungarian/EU equivalent** (add as primary, label as "In Hungary and the EU...")
   - **Global alternative** (add for international students, label as "Globally...")
3. **Hungary as the worked example.** When the US text uses Austin/Texas/Logan/Utah as a case study, add a parallel Hungarian example (Tisza basin, Danube, Balaton, Zala River, etc.).
4. **Coordinate systems must be taught universally.** Don't just teach NAD83 — teach the concept with NAD83, ETRS89, HD72/EOV, and WGS84 as examples.
5. **Verify all URLs before inserting.** Use the reference documents (Hungarian_EU_Data_Sources.md, international_data_sources.md) which have pre-verified URLs.
6. **Don't bloat.** Add international content concisely. A table or a "International Equivalents" box at the end of a section is better than doubling every paragraph.

## Reference Documents (read these first)

- `C:\maidment_hidroGIS\Hungarian_EU_Data_Sources.md` — 30 verified Hungarian/EU data sources
- `C:\maidment_hidroGIS\international_data_sources.md` — 38 verified global data sources

## Chapter-by-Chapter Internationalization Guide

---

### Part I: Foundations

#### Chapter 1: Introduction to GIS in Water Resources
**NA density: HIGH (~25 items, 10 CORE)**

CORE replacements needed:
- NHDPlus (2.7M reaches) → Add EU-Hydro, HydroSHEDS as equivalents
- USGS gauge network (~7,000 stations) → Add OVF/data.vizugy.hu (HU), GRDC (global)
- NLDAS → Add ERA5, GLDAS
- HydroShare/CUAHSI → Keep but note Zenodo/PANGAEA as EU alternatives
- NAD27/NAD83 → Add ETRS89, HD72/EOV
- National Water Model → Add EFAS/GloFAS

ILLUSTRATIVE extensions:
- Texas 2011 drought case study → Add 2018 European drought or Hungarian drought monitoring (aszalymonitoring.vizugy.hu)
- Hurricane Harvey → Add 2013 Danube flood or 2010 Kolontár red sludge disaster
- UT Austin campus example → Add Debreceni Egyetem campus example
- Austin/Logan coordinates → Add Budapest (47.4979°N, 19.0402°E) EOV coordinates

#### Chapter 2: Working with GIS Software
**NA density: MODERATE (~10 items, 5 CORE)**

CORE replacements needed:
- NHDPlus download from National Map → Add EU-Hydro download from Copernicus, HydroSHEDS from hydrosheds.org
- HUC system (HUC8/10/12) → Add EU WFD catchment hierarchy, Hungarian vízgyűjtő codes
- EROM flow table → Add EU-Hydro flow attributes, or GRDC-based estimates

ILLUSTRATIVE extensions:
- Kissimmee watershed → Add Zala River / Balaton watershed
- Logan UTM zone → Add Budapest UTM Zone 34N
- Waller Creek at UT Austin → Add a small Debrecen-area stream

#### Chapter 3: Geodesy, Map Projections, and Coordinate Systems
**NA density: HIGH (~25 items, 14 CORE)**

This chapter needs the MOST structural work — it must teach coordinate systems universally.

CORE replacements/extensions:
- NAD27/NAD83 → Teach as one example; add ETRS89 (EU), HD72 (Hungary), WGS84 (global). Explain the concept of national vs. continental vs. global datums
- Clarke 1866 ellipsoid → Add GRS80, Bessel 1841 (HD72), IUGG 1967
- NGVD29/NAVD88 → Add Baltic Height System (Hungary), EGM2008 geoid
- CORS/HARN → Add EPN (European Permanent Network), Hungarian GNSSnet.hu
- State Plane system → Add Hungarian EOV (Egységes Országos Vetületi rendszer, EPSG:23700), British National Grid, Gauss-Krüger as examples of national grid systems
- VERTCON → Note that Hungary uses GEOID models for vertical transformation
- Albers Equal Area (US) → Add European Albers, EOV (Oblique Mercator)

ILLUSTRATIVE extensions:
- Austin/Logan/NYC UTM zones → Add Budapest (Zone 34N), Debrecen (Zone 34N), and an African/Asian city
- Salt Lake City to New York distance → Add Budapest to Debrecen (or Budapest to Vienna)
- Galveston/Charleston/Juneau tidal trends → Add Trieste, Amsterdam, or global tide gauge examples
- Hurricane Florence case → Add a European flood forecast case (EFAS example)
- Texas 5 State Plane zones → Explain that Hungary has ONE national projection (EOV) — contrast with multi-zone countries

**Add new section: "Hungarian EOV Coordinate System"**
- HD72 datum, GRS67 ellipsoid
- EOV projection: Oblique Mercator, central point at 47°08'20"N, 19°02'54.8584"E
- Northing: 0–400,000; Easting: 400,000–1,000,000
- EPSG:23700
- Practical note: many Hungarian datasets still use EOV; conversion to ETRS89 needed for EU interoperability

#### Chapter 4: Data Sources for Water Resources
**NA density: VERY HIGH (~50+ items, 35+ CORE)**

This is the most US-dependent chapter. Strategy: restructure as a universal framework with US, EU/Hungarian, and global tabs.

**Add new major section: "European and Hungarian Data Sources"**
Covering (from Hungarian_EU_Data_Sources.md):
- DEM: DDM-5 (Lechner), Copernicus DEM GLO-30/EEA-10
- Hydrology: data.vizugy.hu, hydroinfo.hu, EU-Hydro
- Land cover: CORINE Land Cover (CLC)
- Weather: OMSZ/odp.met.hu, ERA5, E-OBS, CARPATCLIM
- Soil: ESDAC, SoilGrids
- Discharge: OVF gauges, GRDC
- Flood: JRC flood hazard maps, EFAS
- Demographics: KSH (data.ksh.hu), Eurostat
- Satellite: Copernicus Data Space (dataspace.copernicus.eu)

**Add new major section: "Global Data Sources"**
Covering (from international_data_sources.md):
- DEM: SRTM, ALOS AW3D30, MERIT DEM, Copernicus GLO-30
- Hydrology: HydroSHEDS/HydroBASINS/HydroRIVERS
- Land cover: ESA WorldCover, Dynamic World
- Weather: CHIRPS, GPM, APHRODITE, CRU TS
- Soil: SoilGrids, HWSD
- Discharge: GRDC, GEMStat
- Flood: GloFAS, Dartmouth Flood Observatory
- Demographics: WorldPop, LandScan, GADM
- Satellite: NASA Earthdata, Google Earth Engine

**Restructure the practical workflow (Section 4.18):**
Keep the US NHDPlus workflow, then add a parallel "Building a Watershed Basemap for the Zala River (Hungary)" workflow using:
- Copernicus DEM for elevation
- EU-Hydro for stream network
- CORINE for land cover
- data.vizugy.hu for gauge data

---

### Part II: Spatial Analysis

#### Chapter 5: Raster Data and Grid Fundamentals
**NA density: VERY LOW (1 item)**
- NLCD reference → Add CORINE Land Cover as EU example, ESA WorldCover as global

#### Chapter 6: Map Algebra and Raster Calculations
**NA density: ZERO**
- No changes needed. All examples are abstract/generic.

#### Chapter 7: Topographic Slope and Aspect
**NA density: LOW (4 items, 2 CORE)**
- Section 7.8 (DEM Data Sources): Add Copernicus DEM, DDM-5, SRTM, ALOS as alternatives to NED
- USU slope handout: keep as reference (content is universal)

#### Chapter 8: Spatial Interpolation and Watershed Averaging
**NA density: MODERATE (8 items, 6 CORE)**
- PRISM → Add E-OBS, CARPATCLIM, WorldClim, CHIRPS as alternatives for gridded climate
- NED RMSE 2.34m → Add Copernicus DEM accuracy specs (LE90 < 4m global, ~1m in Europe)
- HUC10/12 watersheds → Add EU WFD catchments, HydroBASINS
- Albers Equal Area → Add EOV or European Albers
- Worked zonal stats example → Add parallel example using a Hungarian sub-catchment

---

### Part III: Terrain Analysis and Watershed Delineation

#### Chapter 9: Digital Elevation Models and Hydrologic Conditioning
**NA density: MODERATE (11 items, 4 CORE)**
- NED/3DEP → Add Copernicus DEM, DDM-5, SRTM
- NHD for stream burning → Add EU-Hydro, OpenStreetMap waterways
- Logan River case study → Add Zala River or Sajó River (Hungary) as parallel
- Peter Sinks karst → Add Aggtelek Karst (Hungary, UNESCO) as parallel example

#### Chapter 10: Flow Direction and Flow Accumulation
**NA density: LOW-MODERATE (7 items, 5 CORE)**
- NHDPlus COMID → Explain concept of reach identifiers generically; note US (COMID), EU (EU-Hydro ID), global (HydroSHEDS HYRIV_ID)
- Continental US HAND → Note that HAND can be computed for any region; mention GloFAS global HAND
- Onion Creek example → Keep; add note about computing HAND for a Hungarian catchment
- National Water Model → Add EFAS as European equivalent

#### Chapter 11: Stream Network and Watershed Delineation
**NA density: HIGH (24 items, 12 CORE)**
- NHDPlus (entire section 11.9.1) → Add parallel section on EU-Hydro and HydroSHEDS
- EPA Reach Files → Add EU river basin district delineations
- Logan River workflow → Add parallel workflow for a Hungarian watershed
- USGS gauge snapping → Add OVF gauge locations
- National Water Model section → Add EFAS/GloFAS section
- HRRR → Add ECMWF HRES, ALADIN (used in Hungary)

---

### Part IV: Flood Mapping and Emergency Response

#### Chapter 12: Height Above Nearest Drainage (HAND)
**NA density: MODERATE (mix of CORE and ILLUSTRATIVE)**
- NHD/NHDPlus stream definitions → Add EU-Hydro equivalent
- NED 10m → Add Copernicus DEM
- Continental US HAND → Mention European HAND computations (JRC)
- Onion Creek example → Keep; supplement with Tisza flood example
- Nobre/Amazon HAND origin → Already international! Highlight this.

#### Chapter 13: Flood Inundation Mapping
**NA density: HIGH**
- NWM discharge forecasts → Add EFAS forecasts
- NHDPlus COMIDs → Explain reach-based framework generically
- Texas address points → Add Hungarian address/building registry
- Onion Creek 2013 flood → Add 2013 Danube flood or 2010 Tisza flood
- Pre-computed inundation libraries → Note JRC approach for Europe

#### Chapter 14: Flood Emergency Response and the National Water Model
**NA density: VERY HIGH (most US-centric chapter)**

Strategy: Keep US NWM as a detailed case study of how a national system works, then add:

**New section: "European Flood Awareness System (EFAS)"**
- Architecture: ECMWF HRES/ENS → LISFLOOD model → EU-Hydro network
- Copernicus Emergency Management Service
- JRC flood hazard maps
- Contrast with NWM: pan-European vs. national, ensemble vs. deterministic

**New section: "Hungarian Flood Management"**
- OVF operational system
- Tisza flood history (2001, 2006, 2010)
- hydroinfo.hu real-time data
- Disaster management structure (Katasztrófavédelem)

**International examples:**
- Hurricane Harvey → Add 2013 Danube flood (largest since 1501 in Passau)
- NOAA Atlas 14 → Add EU IDF curves, Hungarian csapadék-intenzitás curves
- Jessica Hollis narrative → Add a European flood fatality case

---

### Part V: Advanced Topics

#### Chapter 15: LiDAR and High-Resolution Topographic Data
**NA density: HIGH**
- 3DEP → Add European national LiDAR programs (Netherlands AHN, UK EA LiDAR)
- Note Hungary has no nationwide LiDAR; DDM-5 is the best available
- JALBTCX → Add EU coastal LiDAR programs
- National HAND map → Note it could be computed for Hungary/EU using Copernicus DEM + EU-Hydro
- OpenTopography → Note it's increasingly international

#### Chapter 16: Extending GIS with Python Programming
**NA density: VERY LOW**
- Swap Little Bear/Logan/Onion Creek names → Add Hungarian watershed names as alternatives
- All code and methods are universal

#### Chapter 17: Water Information Sharing and Cyber Infrastructure
**NA density: MODERATE**
- CUAHSI → Add IAHS, EGU Hydrological Sciences division
- HydroShare → Keep (it accepts international data); add Zenodo, PANGAEA
- NWM Tethys Apps → Add EFAS web services
- iUtah project → Add a Hungarian/EU monitoring project example
- NSF RAPID grants → Add EU Horizon emergency funding

#### Chapter 18: Demography and Water Resources
**NA density: VERY HIGH (near-complete rewrite needed)**

Strategy: Teach the CONCEPTS using the US Census as one example, then add:

**New section: "Hungarian Census and KSH"**
- KSH népszámlálás 2022
- Geographic hierarchy: megye → járás → település → számlálókörzet
- KSH API (data.ksh.hu)
- NUTS codes (EU equivalent of FIPS)

**New section: "EU Demographics (Eurostat)"**
- Eurostat GISCO boundaries
- EU-SILC survey
- NUTS hierarchy (NUTS0-3, LAU)

**New section: "Global Population Data"**
- WorldPop (100m gridded)
- LandScan (1km)
- GADM administrative boundaries

Keep the analytical methods (clip, density-weight, zonal stats) as universal.

#### Chapter 19: Hydrologic Processes and Snow Modeling
**NA density: LOW**
- NEXRAD → Add OPERA/EUMETNET radar composites, OMSZ radar
- SNODAS → Add H-SAF snow products, GlobSnow
- Central Sierra Snow Lab → Add European snow research stations (Weissfluhjoch, Col de Porte)
- Reynolds Creek → Add European experimental watersheds
- UEB model → Keep (physics is universal); note SNOWPACK, CROCUS as European alternatives

---

## Formatting Guidelines

For each chapter, use one of these patterns to add international content:

### Pattern A: Inline extension (for small additions)
> In the United States, the National Elevation Dataset (NED) provides DEMs at 1/3 arc-second (~10 m) resolution. In Europe, the Copernicus DEM provides comparable coverage at 10 m (EEA-10) for EU/EEA countries and 30 m (GLO-30) globally. Hungary's DDM-5 offers 5 m resolution from the Lechner Knowledge Centre. Globally, SRTM (30 m) and ALOS AW3D30 (30 m) provide free DEM data for most of the Earth's land surface.

### Pattern B: Equivalence table (for sections with many datasets)
> | Dataset Type | United States | Hungary / EU | Global |
> |---|---|---|---|
> | DEM | NED / 3DEP (10 m) | DDM-5 (5 m) / Copernicus EEA-10 | SRTM (30 m) / ALOS AW3D30 |
> | Stream network | NHDPlus (2.7M reaches) | EU-Hydro / data.vizugy.hu | HydroSHEDS / HydroRIVERS |
> | Land cover | NLCD (30 m) | CORINE CLC (100 m) | ESA WorldCover (10 m) |

### Pattern C: Boxed sidebar (for extended examples)
> **Hungarian Example: The Zala River Watershed**
> The Zala River drains into Lake Balaton, the largest lake in Central Europe...

### Pattern D: New section (for major additions like EFAS, KSH)
> ## 14.X European Flood Awareness System (EFAS)
> ...

## Output Instructions

Process ONE chapter at a time. For each chapter:
1. Read the current lecture notes file
2. Read the relevant sections of Hungarian_EU_Data_Sources.md and international_data_sources.md
3. Apply the changes described above for that chapter
4. Write the updated file back
5. Do NOT remove any existing content — only extend

Work through chapters in order: 1, 2, 3, ..., 19.
