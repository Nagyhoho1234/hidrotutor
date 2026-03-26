\newpage

# Appendix C: Software Guide

This appendix provides a comprehensive reference to every software tool, platform, library, and data service mentioned in *The State of Hidroinformatics in 2026*. For each entry, we list the software type, where to obtain it, its license model, its key capabilities for water resources work, and the chapters in which it appears. The guide is organized by functional category, from desktop GIS through cloud platforms, terrain analysis tools, hydrologic and groundwater modeling systems, programming environments, data management, machine learning frameworks, and visualization libraries. The appendix concludes with Windows installation guidance and a recommended learning path for beginners.

A note on versions: software evolves rapidly. The URLs and version numbers listed here were current as of early 2026. When a link breaks, the software name plus "download" in any search engine will locate the current release.

---

## C.1 GIS Software

Geographic information systems form the foundational platform for nearly every workflow described in this book. Whether you are visualizing a digital elevation model, delineating watersheds, or overlaying flood maps with census data, a GIS provides the environment in which spatial data are loaded, explored, analyzed, and mapped. Four platforms dominate the 2026 hydroinformatics landscape, each occupying a distinct niche.

### ArcGIS Pro

| Attribute | Detail |
|---|---|
| **Type** | Desktop application (Windows only) |
| **URL** | https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview |
| **License** | Commercial; free for students through the Esri Education Site License program; many universities hold institutional licenses |
| **Current version** | 3.4 (as of early 2026) |

**Key capabilities for hydroinformatics.** ArcGIS Pro is the most widely used commercial GIS in water resources engineering. It provides a complete environment for vector and raster analysis, 3D visualization, geoprocessing automation, and cartographic production. Its Spatial Analyst extension includes the core raster hydrology tools -- Fill, Flow Direction, Flow Accumulation, Snap Pour Point, Watershed -- that form the backbone of Chapters 9 through 11. The 3D Analyst extension supports the subsurface visualization workflows described in Chapter 18. ArcGIS Pro's tight integration with ArcPy (see Section C.5) makes it the natural choice for the scripting workflows of Chapter 12, and its ModelBuilder visual programming environment offers a code-free alternative for automating multi-step geoprocessing chains.

ArcGIS Pro also provides direct access to Esri's cloud services through ArcGIS Online, including hosted feature layers, web maps, and the Living Atlas of the World -- a curated collection of authoritative basemaps and reference layers. For organizations already invested in the Esri ecosystem, ArcGIS Pro is the path of least resistance.

**Limitations.** The commercial license cost can be a barrier for individual researchers and organizations in lower-income countries. ArcGIS Pro runs only on Windows, which excludes Linux-based high-performance computing environments. Some advanced extensions (Spatial Analyst, 3D Analyst, Geostatistical Analyst) require separate licenses beyond the base software.

**Chapters where used:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17, 18, 19, 20, 21, 25.

---

### QGIS

| Attribute | Detail |
|---|---|
| **Type** | Desktop application (Windows, macOS, Linux) |
| **URL** | https://qgis.org/download/ |
| **License** | Free and open-source (GNU GPL v2) |
| **Current version** | 3.40 LTR (as of early 2026) |

**Key capabilities for hydroinformatics.** QGIS is the leading open-source desktop GIS and the primary free alternative to ArcGIS Pro. It supports vector and raster data in all common formats (Shapefile, GeoPackage, GeoTIFF, NetCDF, and dozens of others through the GDAL/OGR library). For hydrology, the most important capabilities come through its plugin ecosystem: the QGIS Processing framework integrates GRASS GIS, SAGA GIS, and GDAL tools into a unified interface, giving users access to pit filling, flow direction, flow accumulation, and watershed delineation without leaving the QGIS window. The WhiteboxTools plugin (see Section C.2) provides TauDEM-equivalent terrain hydrology tools directly within QGIS.

QGIS supports Python scripting through PyQGIS (see Section C.5), enabling automation of any workflow that can be performed through the graphical interface. Its print layout system produces publication-quality maps, and its 3D map view supports terrain visualization for the subsurface workflows of Part V. The cross-platform nature of QGIS makes it the default choice for Linux-based computing environments and for organizations that cannot afford commercial GIS licenses.

**Limitations.** Some specialized hydrologic tools available in ArcGIS Pro (particularly the Arc Hydro toolset) have no direct QGIS equivalent, though open-source alternatives exist for most individual operations. Performance on very large rasters (billions of cells) can lag behind ArcGIS Pro, though this gap has narrowed significantly in recent versions.

**Chapters where used:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 17, 18, 19, 20, 21, 25.

---

### Google Earth Engine (GEE)

| Attribute | Detail |
|---|---|
| **Type** | Cloud platform (browser-based) |
| **URL** | https://earthengine.google.com/ |
| **License** | Free for research, education, and nonprofit use; commercial use requires a paid subscription through Google Cloud |
| **Access** | Requires a Google account and project registration |

**Key capabilities for hydroinformatics.** Google Earth Engine is a planetary-scale geospatial analysis platform that hosts petabytes of satellite imagery and geospatial datasets on Google's cloud infrastructure. For hydroinformatics, its most important holdings include the complete Landsat and Sentinel-2 archives, global DEMs (SRTM, ALOS, Copernicus DEM), precipitation datasets (CHIRPS, GPM, ERA5), land cover products (Dynamic World, ESA WorldCover), and soil moisture observations (SMAP). Users write analysis scripts in JavaScript (through the Code Editor) or Python (through the Earth Engine Python API), and all computation runs on Google's servers -- meaning a user with a laptop and a browser can process terabytes of imagery that would overwhelm any desktop machine.

For the workflows described in this book, GEE is particularly relevant for Chapter 3 (accessing global datasets), Chapter 4 (cloud-based GIS paradigm), Chapter 6 (map algebra at continental scale), Chapter 7 (global slope and aspect computation), Chapter 9 (DEM conditioning for large regions), Chapter 11 (continental watershed delineation), and Chapters 23 and 25 (machine learning on satellite data for hydrological prediction). The Earth Engine machine learning module (ee.Classifier, ee.Reducer) supports random forest classification, gradient boosting, and clustering directly on satellite imagery stacks.

**Limitations.** GEE requires an internet connection and depends on Google's infrastructure. Export of large results can be slow. The JavaScript-centric Code Editor has a learning curve for users accustomed to Python. Some advanced hydrologic operations (D-infinity flow direction, HAND computation) are not natively available and require custom implementations.

**Chapters where used:** 1, 3, 4, 6, 7, 9, 11, 12, 23, 25.

---

### Microsoft Planetary Computer

| Attribute | Detail |
|---|---|
| **Type** | Cloud platform (browser-based and API-accessible) |
| **URL** | https://planetarycomputer.microsoft.com/ |
| **License** | Free for research and educational use |
| **Access** | Requires a Microsoft account; compute provided through hosted JupyterHub |

**Key capabilities for hydroinformatics.** Microsoft Planetary Computer hosts a large catalog of environmental datasets through a STAC (SpatioTemporal Asset Catalog) API, including Sentinel-2, Landsat, Copernicus DEM, NAIP aerial imagery, and numerous climate and land cover products. Unlike Google Earth Engine, which uses a custom API and server-side computation, Planetary Computer provides a standard Python environment (JupyterHub with xarray, rasterio, geopandas, and dask) that runs on Azure infrastructure. This makes it particularly attractive for users who prefer to work in standard Python rather than learning a platform-specific API.

For the workflows in this book, Planetary Computer is relevant for accessing global DEM data (Chapters 3, 5), performing cloud-based raster analysis (Chapters 4, 6), working with Copernicus datasets (Chapters 7, 9), and large-scale terrain processing (Chapters 11, 12). Its integration with the broader Azure ecosystem makes it a natural choice for organizations already using Microsoft cloud services.

**Limitations.** The compute environment is more constrained than GEE for very large-scale analyses. The platform is younger than GEE and has a smaller user community, meaning fewer tutorials and code examples are available. Some datasets available in GEE are not yet mirrored on Planetary Computer.

**Chapters where used:** 3, 4, 6, 7, 9, 11, 12, 25.

---

## C.2 Terrain Analysis

Terrain analysis -- computing flow directions, accumulating contributing areas, delineating watersheds, extracting stream networks -- is the computational engine of DEM-based hydrology. The following tools provide the algorithms that power Part III of the book and support the HAND and flood inundation workflows of Part IV.

### TauDEM (Terrain Analysis Using Digital Elevation Models)

| Attribute | Detail |
|---|---|
| **Type** | Command-line tools and ArcGIS Pro toolbox |
| **URL** | https://hydrology.usu.edu/taudem/taudem5/ |
| **License** | Free and open-source (MIT License) |
| **Developer** | David Tarboton, Utah State University |

**Key capabilities for hydroinformatics.** TauDEM is the gold standard for research-grade terrain analysis in hydrology. Developed by David Tarboton -- one of the pioneers of digital terrain hydrology -- TauDEM implements the D8 and D-infinity (Dinf) flow direction algorithms, along with a complete suite of derived products: flow accumulation, stream network extraction, watershed delineation, stream order computation, distance to streams, and the foundational algorithms behind the HAND index. TauDEM's key technical advantage is its use of MPI (Message Passing Interface) for parallel computation, allowing it to process very large DEMs across multiple CPU cores or even multiple machines in a cluster.

TauDEM is the primary terrain analysis engine for Chapters 9 (DEM conditioning with PitRemove), 10 (D8 and Dinf flow direction, flow accumulation), 11 (stream network delineation, watershed extraction), 12 (automated batch processing via command-line calls from Python scripts), 13 (LiDAR DEM processing), and 14 (HAND computation using DinfDistDown). Its command-line interface makes it ideal for scripting, and its ArcGIS Pro toolbox provides a graphical interface for interactive use.

**Installation on Windows.** TauDEM requires Microsoft MPI (MS-MPI) to be installed first. Download MS-MPI from Microsoft's website, then download the TauDEM Windows installer from the project page. The installer places executables in `C:\Program Files\TauDEM\TauDEM5Exe` and registers the ArcGIS toolbox. After installation, add the TauDEM executable directory to the system PATH environment variable to enable command-line use from any directory.

**Chapters where used:** 1, 7, 9, 10, 11, 12, 13, 14, 25.

---

### WhiteboxTools

| Attribute | Detail |
|---|---|
| **Type** | Command-line tools with QGIS and Python interfaces |
| **URL** | https://www.whiteboxgeo.com/download-whiteboxtools/ |
| **License** | Free open-source edition (MIT License); WhiteboxTools Pro (extended features) is commercial |
| **Developer** | John Lindsay, University of Guelph |

**Key capabilities for hydroinformatics.** WhiteboxTools provides over 550 geospatial analysis tools written in Rust, making it one of the fastest terrain analysis packages available. For hydrology, it offers pit filling (breach depressions and fill), flow direction (D8, Dinf, FD8, MDinf), flow accumulation, stream network extraction, watershed delineation, and HAND computation. Its breach depressions algorithm is particularly noteworthy -- rather than filling pits (which can create large flat areas), it carves channels through barriers, producing more hydrologically realistic flow paths.

WhiteboxTools integrates with QGIS through the WhiteboxTools for QGIS plugin, with Python through the whitebox package (installable via pip), and with R through the whitebox R package. This flexibility makes it the terrain analysis tool of choice for users working outside the ArcGIS ecosystem.

**Chapters where used:** 4, 9, 10, 12, 14, 25.

---

### GRASS GIS

| Attribute | Detail |
|---|---|
| **Type** | Desktop application and command-line tools (Windows, macOS, Linux) |
| **URL** | https://grass.osgeo.org/ |
| **License** | Free and open-source (GNU GPL v2) |
| **Current version** | 8.4 (as of early 2026) |

**Key capabilities for hydroinformatics.** GRASS GIS is one of the oldest and most powerful open-source GIS platforms, with a particularly strong raster analysis engine. Its hydrologic modules include `r.watershed` (a memory-efficient watershed delineation algorithm that can process very large DEMs), `r.stream.*` (stream network extraction and analysis), `r.drain` (flow path tracing), and `r.terraflow` (massive terrain analysis). GRASS also provides comprehensive raster map algebra through `r.mapcalc`, interpolation through `v.surf.rst` (regularized spline with tension), and terrain analysis through `r.slope.aspect`.

GRASS GIS is accessible from within QGIS through the Processing framework, from Python through the grass.script library, and from the command line. Its location/mapset data management model enforces consistent coordinate reference systems, which prevents a common source of errors in hydrologic analysis.

**Chapters where used:** 4, 5, 6, 8, 9, 10, 12, 13, 14, 18, 25.

---

### Arc Hydro

| Attribute | Detail |
|---|---|
| **Type** | ArcGIS Pro toolbox and geodatabase schema |
| **URL** | https://www.esri.com/en-us/industries/water-resources/arc-hydro |
| **License** | Free download; requires ArcGIS Pro license |
| **Developer** | Esri, originally developed in collaboration with David Maidment at UT Austin |

**Key capabilities for hydroinformatics.** Arc Hydro is not just a set of tools -- it is a data model and a philosophy for organizing water resources information in a GIS. The Arc Hydro data model defines a standardized geodatabase schema for storing drainage networks, watersheds, monitoring points, time series, and cross-sections. The Arc Hydro Tools provide a streamlined workflow for DEM-based hydrology: terrain preprocessing, flow direction, flow accumulation, stream definition, stream segmentation, catchment delineation, drainage line processing, and adjoint catchment generation.

Arc Hydro's particular strength lies in its integration of the hydrologic network with the underlying GIS database structure. When you delineate watersheds with Arc Hydro, the results are stored in a structured geodatabase with topological relationships intact -- each stream segment knows its upstream and downstream neighbors, each catchment knows which stream it drains to, and these relationships support network tracing and hydrologic connectivity analysis.

The Arc Hydro Groundwater (AHGW) extension, described in detail in Part V of this book, extends the surface water data model into three dimensions, providing tools for borehole visualization, cross-section construction, aquifer volume representation, and integration with MODFLOW.

**Chapters where used:** 1, 4, 6, 9, 11, 12, 18, 19, 20, 21, 25.

---

## C.3 Hydrologic and Hydraulic Modeling

The models in this section transform spatial data -- terrain, land cover, soils, precipitation -- into predictions of water movement: how much runoff a storm generates, where a river floods, how groundwater responds to pumping.

### HEC-HMS (Hydrologic Engineering Center -- Hydrologic Modeling System)

| Attribute | Detail |
|---|---|
| **Type** | Desktop application (Windows; runs on macOS/Linux via compatibility layers) |
| **URL** | https://www.hec.usace.army.mil/software/hec-hms/ |
| **License** | Free (public domain, developed by the U.S. Army Corps of Engineers) |
| **Current version** | 4.12 (as of early 2026) |

**Key capabilities for hydroinformatics.** HEC-HMS is the most widely used rainfall-runoff model in the United States and is extensively applied worldwide. It simulates precipitation-runoff processes for watershed systems ranging from small urban catchments to large river basins. HEC-HMS includes multiple methods for loss estimation (SCS Curve Number, Green-Ampt, deficit-constant), unit hydrograph transform (SCS, Clark, Snyder, ModClark), baseflow, and channel routing (Muskingum, Muskingum-Cunge, lag, modified Puls). The ModClark method supports gridded precipitation input, enabling direct use of radar rainfall or satellite precipitation products.

HEC-HMS is the primary hydrologic model used in the calibration examples of Chapter 22 and the agentic AI demonstration of Chapter 24, where an autonomous agent iteratively calibrates HEC-HMS parameters for a Hungarian catchment. It also appears in the flood forecasting discussion of Chapter 15 (as the model behind many rating curve systems) and Chapter 25 (as a benchmark against which machine learning models are compared).

**Installation on Windows.** Download the installer from the HEC website. The installation is straightforward and does not require administrative privileges. HEC-HMS includes a built-in GIS module (HEC-GeoHMS functionality is being integrated into the main application) for importing terrain-derived watershed parameters.

**Chapters where used:** 1, 4, 7, 8, 13, 14, 15, 22, 24, 25.

---

### HEC-RAS (Hydrologic Engineering Center -- River Analysis System)

| Attribute | Detail |
|---|---|
| **Type** | Desktop application (Windows) |
| **URL** | https://www.hec.usace.army.mil/software/hec-ras/ |
| **License** | Free (public domain) |
| **Current version** | 6.6 (as of early 2026) |

**Key capabilities for hydroinformatics.** HEC-RAS is the standard hydraulic modeling tool for river flood analysis. It performs one-dimensional steady and unsteady flow calculations, two-dimensional unsteady flow modeling, sediment transport, and water quality analysis. For flood inundation mapping (Chapter 15), HEC-RAS is the tool of choice: it takes a river geometry (cross-sections or a 2D mesh derived from LiDAR terrain data), flow boundary conditions (from HEC-HMS or a forecast model), and produces water surface elevation profiles and inundation extent maps. The RAS Mapper module provides integrated GIS functionality for terrain processing and result visualization.

**Chapters where used:** 1, 4, 13, 14, 15, 22, 23, 25.

---

### SWAT (Soil and Water Assessment Tool)

| Attribute | Detail |
|---|---|
| **Type** | Desktop application with GIS interfaces (ArcSWAT for ArcGIS, QSWAT for QGIS) |
| **URL** | https://swat.tamu.edu/ |
| **License** | Free (public domain) |
| **Developer** | USDA Agricultural Research Service, Texas A&M University |

**Key capabilities for hydroinformatics.** SWAT is a semi-distributed, continuous-time watershed model designed for predicting the impact of land management practices on water, sediment, and agricultural chemical yields. It operates on a daily time step and divides watersheds into sub-basins and hydrologic response units (HRUs) based on unique combinations of land use, soil type, and slope class. SWAT is the world's most widely published watershed model, with thousands of peer-reviewed applications across every continent.

For the workflows in this book, SWAT represents the class of complex, physically based models that require extensive calibration (Chapter 22) and that stand to benefit most from AI-assisted parameter optimization (Chapter 24). Its GIS interfaces (ArcSWAT and QSWAT) demonstrate the tight coupling between GIS and hydrologic modeling that is a central theme of Chapter 4.

**Chapters where used:** 1, 4, 22, 24.

---

### MODFLOW

| Attribute | Detail |
|---|---|
| **Type** | Command-line program with various graphical interfaces |
| **URL** | https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model |
| **License** | Free (public domain, developed by the U.S. Geological Survey) |
| **Current version** | MODFLOW 6.5 (as of early 2026) |

**Key capabilities for hydroinformatics.** MODFLOW is the world's most widely used groundwater flow model. It solves the three-dimensional groundwater flow equation using the finite-difference method on a structured or unstructured grid. MODFLOW 6, the current generation, supports multiple models within a single simulation (allowing coupled surface water-groundwater modeling), unstructured grids (DISV and DISU packages), and a modular package system for representing wells, recharge, rivers, drains, evapotranspiration, and dozens of other boundary conditions.

MODFLOW is the central modeling tool of Chapter 21 (Simulating Groundwater Flow), where its application is demonstrated for the Danube gravel terrace aquifer system. It also appears in Chapter 18 (as the target for 3D subsurface GIS frameworks), Chapter 20 (receiving hydrogeologic framework models as input), Chapter 22 (calibration of groundwater models), Chapter 24 (as a candidate for agentic AI calibration), and Chapter 25 (digital twin applications).

MODFLOW's Python interface, FloPy (see Section C.5), has transformed groundwater modeling practice by enabling programmatic model construction, parameter sweeps, and integration with optimization and machine learning workflows.

**Chapters where used:** 1, 4, 18, 20, 21, 22, 23, 24, 25.

---

### FEFLOW

| Attribute | Detail |
|---|---|
| **Type** | Desktop application (Windows, Linux) |
| **URL** | https://www.mikepoweredbydhi.com/products/feflow |
| **License** | Commercial; academic licenses available at reduced cost |
| **Developer** | DHI (Danish Hydraulic Institute) |

**Key capabilities for hydroinformatics.** FEFLOW solves groundwater flow and contaminant transport equations using the finite-element method, which allows it to use triangular and tetrahedral meshes that conform to irregular geological boundaries more naturally than MODFLOW's structured grids. FEFLOW provides a sophisticated graphical interface for model construction, including direct import of borehole data, 3D geological model integration, and automatic mesh generation. Its visualization capabilities are particularly strong for three-dimensional subsurface problems.

FEFLOW is the primary commercial alternative to MODFLOW for groundwater modeling. It is particularly popular in Europe, where DHI has a strong presence, and for projects requiring detailed representation of complex geological structures.

**Chapters where used:** 18, 20, 21, 25.

---

### Noah-MP (Noah Multi-Parameterization Land Surface Model)

| Attribute | Detail |
|---|---|
| **Type** | Fortran source code, typically compiled and run within WRF or the National Water Model framework |
| **URL** | https://ral.ucar.edu/solutions/products/noah-multiparameterization-land-surface-model-noah-mp |
| **License** | Free and open-source |
| **Developer** | NCAR (National Center for Atmospheric Research) |

**Key capabilities for hydroinformatics.** Noah-MP is the land surface model at the heart of the U.S. National Water Model (NWM), which is the operational continental-scale flood forecasting system described in Chapter 16. Noah-MP computes the energy and water balance at the land surface: how much precipitation infiltrates, how much runs off, how much evaporates, and how snow accumulates and melts. Its "multi-parameterization" design allows users to select among different representations of vegetation, soil, runoff generation, and groundwater, making it a flexible framework for exploring model structural uncertainty.

For the workflows in this book, Noah-MP represents the land surface modeling component of the operational forecasting chain. Understanding its role is essential for interpreting National Water Model outputs and for the calibration discussions of Chapter 22.

**Chapters where used:** 1, 11, 16, 22.

---

### LISFLOOD

| Attribute | Detail |
|---|---|
| **Type** | Distributed hydrological model (command-line, Python integration) |
| **URL** | https://ec-jrc.github.io/lisflood-model/ |
| **License** | Free and open-source (EUPL License) |
| **Developer** | European Commission Joint Research Centre (JRC) |

**Key capabilities for hydroinformatics.** LISFLOOD is the hydrological model underlying the European Flood Awareness System (EFAS) and the Global Flood Awareness System (GloFAS), both described in Chapter 16. It is a spatially distributed, physically based rainfall-runoff and routing model that operates on a regular grid (typically 1 km or 5 km resolution). LISFLOOD simulates snow accumulation and melt, soil moisture dynamics, groundwater recharge, surface runoff, and channel routing. Its LISFLOOD-FP variant is a dedicated two-dimensional flood inundation model used for detailed floodplain mapping.

LISFLOOD is the European counterpart to the U.S. National Water Model -- the operational engine that produces the flood forecasts used by European member states, including Hungary's flood warning services.

**Chapters where used:** 1, 3, 11, 13, 14, 15, 16, 22.

---

## C.4 Operational Forecasting Systems

These are not software packages you install locally, but operational systems that consume and produce the data described in this book.

### National Water Model (NWM)

| Attribute | Detail |
|---|---|
| **Type** | Operational forecasting system (cloud-hosted, outputs accessible via API) |
| **URL** | https://water.noaa.gov/about/nwm |
| **Operator** | NOAA / National Weather Service |

**Key capabilities.** The NWM produces streamflow forecasts for 2.7 million river reaches across the contiguous United States, plus forecasts of soil moisture, snowpack, and other land surface variables. It runs on NOAA's supercomputers and produces analysis, short-range (18-hour), medium-range (10-day), and long-range (30-day) forecasts. Outputs are distributed in NetCDF format through NOAA's cloud services and are accessible through the HydroShare THREDDS server.

**Chapters where used:** 1, 3, 6, 8, 10, 11, 12, 13, 14, 15, 16, 22, 25.

### EFAS / GloFAS (European / Global Flood Awareness System)

| Attribute | Detail |
|---|---|
| **Type** | Operational forecasting system (outputs accessible via Copernicus Climate Data Store) |
| **URL** | https://www.efas.eu/ and https://www.globalfloods.eu/ |
| **Operator** | Copernicus Emergency Management Service / European Commission JRC |

**Key capabilities.** EFAS provides flood forecasts for European river basins at 5 km resolution with lead times up to 10 days. GloFAS extends this globally at coarser resolution. Both systems are built on the LISFLOOD model and produce probabilistic flood forecasts based on ensemble weather predictions. Outputs include exceedance probabilities for flood thresholds, making them directly useful for flood warning.

**Chapters where used:** 1, 2, 3, 6, 8, 10, 11, 14, 15, 16, 17, 22, 25.

---

## C.5 Programming Languages and Libraries

Programming has become an essential skill in hydroinformatics. The shift from menu-driven GIS to scripted, reproducible workflows is one of the defining trends of the 2026 practice, and Python is overwhelmingly the language of choice.

### Python

| Attribute | Detail |
|---|---|
| **Type** | General-purpose programming language |
| **URL** | https://www.python.org/ or via Anaconda/Miniconda (https://docs.conda.io/) |
| **License** | Free and open-source (PSF License) |
| **Current version** | 3.12 (as of early 2026) |

**Key capabilities for hydroinformatics.** Python is the lingua franca of modern hydroinformatics. It connects every component of the workflow: GIS operations (through ArcPy and PyQGIS), raster processing (through GDAL/OGR and rasterio), data analysis (through pandas and NumPy), machine learning (through scikit-learn, PyTorch, and TensorFlow), groundwater modeling (through FloPy), and visualization (through matplotlib and folium). Chapter 12 is devoted entirely to Python-based automation of hydrologic workflows, and Python appears in nearly every subsequent chapter.

The recommended way to install Python for hydroinformatics on Windows is through Miniconda or Anaconda, which provides the `conda` package manager. Conda handles the complex binary dependencies of geospatial libraries (GDAL, PROJ, GEOS) far more reliably than pip alone.

**Chapters where used:** 3, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 25.

---

### ArcPy

| Attribute | Detail |
|---|---|
| **Type** | Python library (ships with ArcGIS Pro) |
| **URL** | Included with ArcGIS Pro installation |
| **License** | Requires ArcGIS Pro license |

**Key capabilities.** ArcPy provides Python access to every geoprocessing tool in ArcGIS Pro, enabling scripted automation of GIS workflows. It is the backbone of Chapter 12, where batch watershed delineation is demonstrated by calling ArcPy functions in a loop. ArcPy also provides access to the mapping module (arcpy.mp) for automated cartographic production and the data access module (arcpy.da) for reading and writing geodatabase features and tables.

**Chapters where used:** 4, 6, 9, 12, 17, 23.

---

### PyQGIS

| Attribute | Detail |
|---|---|
| **Type** | Python library (ships with QGIS) |
| **URL** | Included with QGIS installation |
| **License** | Free and open-source (GNU GPL v2) |

**Key capabilities.** PyQGIS provides Python access to QGIS functionality, paralleling ArcPy for the open-source ecosystem. It allows users to automate any QGIS operation, create custom processing algorithms, build plugins, and generate maps programmatically. For users who cannot access ArcGIS Pro, PyQGIS combined with GDAL/OGR provides a fully capable alternative scripting environment.

**Chapters where used:** 4, 12.

---

### GDAL/OGR

| Attribute | Detail |
|---|---|
| **Type** | C/C++ libraries with Python bindings (and bindings for many other languages) |
| **URL** | https://gdal.org/ |
| **License** | Free and open-source (MIT License) |

**Key capabilities.** GDAL (Geospatial Data Abstraction Library) reads and writes over 200 raster formats; OGR (part of the same library) handles over 100 vector formats. Together, they form the foundation of virtually every open-source geospatial tool: QGIS, GRASS GIS, rasterio, geopandas, and even parts of ArcGIS Pro all use GDAL/OGR internally. For hydroinformatics scripting, the Python bindings (`from osgeo import gdal, ogr`) provide low-level access to raster and vector data, coordinate transformations, and format conversions. The command-line utilities (`gdalinfo`, `gdal_translate`, `gdalwarp`, `ogr2ogr`) are indispensable for data preparation.

**Chapters where used:** 4, 6, 9, 12, 17, 23.

---

### FloPy

| Attribute | Detail |
|---|---|
| **Type** | Python library |
| **URL** | https://github.com/modflowpy/flopy |
| **License** | Free and open-source (CC0 public domain) |

**Key capabilities.** FloPy is the Python interface for MODFLOW and related USGS groundwater modeling programs. It allows users to construct, run, and post-process MODFLOW models entirely from Python scripts, eliminating the need for graphical model-building interfaces. FloPy supports all MODFLOW 6 packages and provides utilities for model visualization, grid generation, and parameter manipulation. It is essential for the groundwater modeling workflows of Chapter 21 and for any programmatic approach to groundwater model calibration (Chapters 22, 24).

**Chapters where used:** 18, 21, 25.

---

### Key Python Libraries for Hydroinformatics

The following libraries appear repeatedly throughout the book and form the core Python toolkit for water resources work:

| Library | Purpose | Install | Key chapters |
|---|---|---|---|
| **NumPy** | Numerical arrays and mathematics | `conda install numpy` | 6, 12, 21, 23 |
| **pandas** | Tabular data analysis and time series | `conda install pandas` | 3, 4, 12, 17, 21, 23, 25 |
| **geopandas** | Geospatial vector data in DataFrames | `conda install geopandas` | 4, 6, 12, 17, 23 |
| **rasterio** | Pythonic raster data I/O (built on GDAL) | `conda install rasterio` | 6, 12, 23 |
| **xarray** | Multi-dimensional labeled arrays (NetCDF) | `conda install xarray` | 3, 12, 21, 25 |
| **matplotlib** | 2D plotting and visualization | `conda install matplotlib` | 12, 21, 23 |
| **folium** | Interactive Leaflet maps from Python | `pip install folium` | 17, 25 |
| **shapely** | Geometric operations | `conda install shapely` | 4, 12 |
| **pyproj** | Coordinate reference system transformations | `conda install pyproj` | 2, 4, 12 |

---

### Jupyter

| Attribute | Detail |
|---|---|
| **Type** | Interactive computing environment (browser-based) |
| **URL** | https://jupyter.org/ |
| **License** | Free and open-source (BSD License) |

**Key capabilities for hydroinformatics.** Jupyter notebooks combine executable code, explanatory text, equations, and visualizations in a single document. For hydroinformatics, this means a complete analysis -- from data loading through processing to final maps and hydrographs -- can be captured in one reproducible, shareable file. JupyterLab (the current generation of the interface) supports multiple kernels, file browsing, terminal access, and extension plugins.

Jupyter is the computing environment of choice for the interactive examples suggested throughout the book, and it is the native interface of Microsoft Planetary Computer. Many of the code workflows in Chapter 12 and the machine learning examples in Chapter 23 are best executed in Jupyter notebooks.

**Chapters where used:** 3, 4, 6, 12, 25.

---

## C.6 Data Management

Hydroinformatics projects generate and consume large volumes of spatial data. The following tools and formats provide the storage and sharing infrastructure.

### PostGIS

| Attribute | Detail |
|---|---|
| **Type** | Spatial database extension for PostgreSQL |
| **URL** | https://postgis.net/ |
| **License** | Free and open-source (GNU GPL v2) |

**Key capabilities for hydroinformatics.** PostGIS adds spatial data types (geometry, geography, raster) and hundreds of spatial functions to the PostgreSQL relational database. For large-scale hydroinformatics projects -- those managing thousands of watersheds, millions of stream reaches, or decades of monitoring data -- PostGIS provides the scalability, query performance, and data integrity that file-based formats cannot match. It supports spatial indexing (R-tree), topological relationships, network routing, raster algebra, and 3D geometry.

PostGIS is the standard backend for enterprise-scale water information systems, including many of the data portals described in Chapter 3. The NHDPlus dataset, for example, is most efficiently queried and analyzed when loaded into PostGIS.

**Chapters where used:** 4, 5, 18.

---

### GeoPackage

| Attribute | Detail |
|---|---|
| **Type** | Open file format (SQLite-based) |
| **URL** | https://www.geopackage.org/ |
| **License** | Open standard (OGC) |

**Key capabilities.** GeoPackage is a modern, portable, open file format for geospatial data that stores vector features, raster tiles, and attribute data in a single SQLite database file. It is replacing the aging Shapefile format as the default exchange format for geospatial data. Both ArcGIS Pro and QGIS fully support GeoPackage reading and writing. Unlike Shapefile, GeoPackage supports long field names, multiple geometry types in a single file, coordinate reference system metadata, and file sizes well beyond 2 GB.

**Chapters where used:** 3, 4, 12, 17, 18.

---

### HydroShare

| Attribute | Detail |
|---|---|
| **Type** | Web-based data sharing platform |
| **URL** | https://www.hydroshare.org/ |
| **License** | Free (funded by NSF through CUAHSI) |

**Key capabilities.** HydroShare is a repository for sharing hydrologic data and models. It provides persistent DOIs for datasets, supports collaborative workspaces, and hosts JupyterHub computing environments (CUAHSI JupyterHub) for running analyses on shared data. HydroShare resources can include time series, geographic features, raster grids, MODFLOW models, SWAT models, and any other file type. For reproducible hydroinformatics research, HydroShare provides a complete platform: store data, run analysis, share results.

**Chapters where used:** 1, 3, 25.

---

### ChromaDB

| Attribute | Detail |
|---|---|
| **Type** | Vector database (embedded or client-server) |
| **URL** | https://www.trychroma.com/ |
| **License** | Free and open-source (Apache 2.0) |

**Key capabilities.** ChromaDB is a vector database designed for storing and querying embedding vectors, making it a key component in retrieval-augmented generation (RAG) systems. In the context of this book, ChromaDB is relevant to Chapter 18's discussion of how AI systems can index and retrieve subsurface geological descriptions, and more broadly to the book's own RAG architecture (described in the Book Concept document) that enables readers to ask questions and receive answers with citations from specific chapters.

**Chapters where used:** 18.

---

## C.7 AI and Machine Learning

Machine learning has moved from the research frontier to operational deployment in hydroinformatics. The following frameworks and libraries power the applications described in Chapters 22 through 25.

### scikit-learn

| Attribute | Detail |
|---|---|
| **Type** | Python library |
| **URL** | https://scikit-learn.org/ |
| **License** | Free and open-source (BSD License) |

**Key capabilities for hydroinformatics.** scikit-learn provides the standard implementations of classical machine learning algorithms: random forests, gradient boosting, support vector machines, k-nearest neighbors, linear and logistic regression, clustering (k-means, DBSCAN), and dimensionality reduction (PCA). For hydroinformatics, these algorithms are used for land cover classification from satellite imagery, regression-based streamflow prediction, anomaly detection in sensor networks, and feature selection for hydrologic model parameterization.

scikit-learn is the starting point for Chapter 23's discussion of practical ML applications in hydrology. Its consistent API (fit, predict, score) makes it easy to compare algorithms, and its integration with pandas DataFrames allows seamless transition from data preparation to model training.

**Chapters where used:** 23, 25.

---

### PyTorch

| Attribute | Detail |
|---|---|
| **Type** | Python library (with C++ backend) |
| **URL** | https://pytorch.org/ |
| **License** | Free and open-source (BSD License) |
| **GPU support** | CUDA (NVIDIA), ROCm (AMD), MPS (Apple Silicon) |

**Key capabilities for hydroinformatics.** PyTorch is the dominant deep learning framework in hydrologic research as of 2026. It provides the tensor computation and automatic differentiation engine used to build and train neural networks, including the LSTM (Long Short-Term Memory) networks that have revolutionized streamflow prediction. PyTorch's dynamic computation graph makes it particularly well-suited for research, where model architectures evolve rapidly.

In this book, PyTorch underpins the LSTM rainfall-runoff models discussed in Chapter 23, the NeuralHydrology framework (see below), and the transformer-based architectures mentioned in Chapter 25 as the next frontier in hydrologic prediction.

**Chapters where used:** 23, 25.

---

### TensorFlow

| Attribute | Detail |
|---|---|
| **Type** | Python library (with C++ backend) |
| **URL** | https://www.tensorflow.org/ |
| **License** | Free and open-source (Apache 2.0) |
| **GPU support** | CUDA (NVIDIA), oneDNN (Intel) |

**Key capabilities for hydroinformatics.** TensorFlow is Google's machine learning framework and the engine behind many production ML systems. While PyTorch has become the preferred framework for research-oriented hydrology, TensorFlow remains important for deployment (through TensorFlow Lite and TensorFlow Serving), for integration with Google Earth Engine's ML capabilities, and for organizations with existing TensorFlow infrastructure. TensorFlow's Keras API provides a high-level interface for building neural networks that is accessible to scientists without deep ML expertise.

**Chapters where used:** 23, 25.

---

### NeuralHydrology

| Attribute | Detail |
|---|---|
| **Type** | Python library (built on PyTorch) |
| **URL** | https://neuralhydrology.readthedocs.io/ |
| **License** | Free and open-source (BSD License) |
| **Developer** | Frederik Kratzert and collaborators, Google Research / Johannes Kepler University Linz |

**Key capabilities for hydroinformatics.** NeuralHydrology is a purpose-built framework for training deep learning models on hydrological time series data. It provides standardized data loading for the CAMELS dataset (and its international variants: CAMELS-GB, CAMELS-CL, CAMELS-DE, LamaH-CE), implementations of LSTM, EA-LSTM (Entity-Aware LSTM), and other architectures specifically designed for catchment-scale prediction, and evaluation metrics standard in hydrology (NSE, KGE, alpha-NSE decomposition).

NeuralHydrology is the framework behind the landmark results showing that a single LSTM trained on 531 U.S. catchments outperforms individual calibrated Sacramento models in each catchment. Chapter 23 describes these results in detail and demonstrates how to use NeuralHydrology for flood prediction on Hungarian catchments.

**Chapters where used:** 23.

---

### Google Earth Engine ML

| Attribute | Detail |
|---|---|
| **Type** | Server-side ML within the GEE platform |
| **URL** | https://developers.google.com/earth-engine/guides/machine-learning |
| **License** | Same as GEE (free for research/education) |

**Key capabilities.** GEE provides built-in classifiers (random forest, gradient boosting, SVM, CART) and clustering algorithms that operate directly on satellite imagery stacks without downloading data locally. This is particularly powerful for land cover classification, change detection, and water body mapping at continental to global scales. The `ee.Classifier` API trains models on labeled point data and applies them to entire image collections.

**Chapters where used:** 4, 6, 23, 25.

---

## C.8 Visualization

Modern hydroinformatics increasingly delivers results through interactive web maps rather than static PDF maps. The following JavaScript libraries power the web-based visualization discussed in the book.

### Leaflet

| Attribute | Detail |
|---|---|
| **Type** | JavaScript library for web maps |
| **URL** | https://leafletjs.com/ |
| **License** | Free and open-source (BSD License) |

**Key capabilities.** Leaflet is the most widely used open-source library for interactive web maps. It is lightweight (42 KB of JavaScript), mobile-friendly, and extensible through hundreds of plugins. For hydroinformatics, Leaflet provides the base mapping capability for web-based flood warning dashboards, watershed information systems, and data portals. The Python library folium generates Leaflet maps from Python code, enabling direct integration with Jupyter notebook workflows.

**Chapters where used:** Referenced in discussions of web-based water information systems (Chapters 17, 25).

---

### MapLibre GL JS

| Attribute | Detail |
|---|---|
| **Type** | JavaScript library for vector tile web maps |
| **URL** | https://maplibre.org/ |
| **License** | Free and open-source (BSD License) |

**Key capabilities.** MapLibre GL JS renders vector tile maps using WebGL, providing smooth zooming, rotation, and 3D terrain visualization in the browser. It is the open-source fork of Mapbox GL JS and is used by organizations that need high-performance web mapping without commercial licensing constraints. For hydroinformatics, MapLibre's 3D terrain rendering is particularly valuable for visualizing flood inundation, watershed topography, and subsurface geology in web applications.

**Chapters where used:** Referenced in discussions of modern web mapping (Chapter 25).

---

### CesiumJS

| Attribute | Detail |
|---|---|
| **Type** | JavaScript library for 3D geospatial visualization |
| **URL** | https://cesium.com/platform/cesiumjs/ |
| **License** | Free and open-source (Apache 2.0) |

**Key capabilities.** CesiumJS provides full 3D globe visualization in the browser, including terrain rendering, 3D building models, point clouds, and time-dynamic data. For hydroinformatics, CesiumJS is relevant for visualizing LiDAR point clouds (Chapter 13), 3D subsurface geological models (Chapter 18), and time-animated flood inundation sequences. Its 3D Tiles standard enables efficient streaming of massive 3D datasets to web browsers.

**Chapters where used:** 18.

---

## C.9 Installation Guide for Windows

Most readers of this book will be working on Windows, which is the primary platform for ArcGIS Pro, HEC-HMS, HEC-RAS, and many other tools in the hydroinformatics stack. The following guide provides a recommended installation sequence that minimizes conflicts and sets up a productive working environment.

### Step 1: Install a Python Environment Manager

Before installing anything else, set up a proper Python environment manager. This prevents the common problem of conflicting library versions when different tools need different versions of the same dependency.

1. Download **Miniconda** from https://docs.conda.io/en/latest/miniconda.html (choose the 64-bit Windows installer).
2. Run the installer. Accept the defaults, but check the box to "Add Miniconda to my PATH environment variable" if you plan to use conda from the Windows Command Prompt or PowerShell. If you prefer to keep things isolated, leave it unchecked and use the Anaconda Prompt instead.
3. Open a terminal (Anaconda Prompt or your preferred shell) and verify: `conda --version`.
4. Create a dedicated environment for hydroinformatics work:

```
conda create -n hydro python=3.12
conda activate hydro
conda install numpy pandas geopandas rasterio xarray matplotlib jupyterlab
pip install whitebox flopy folium
```

This gives you a clean Python environment with all the core libraries. You can create additional environments for specific projects (e.g., `conda create -n ml python=3.12 pytorch scikit-learn` for machine learning work).

### Step 2: Install GIS Software

**ArcGIS Pro** (if you have a license):
1. Download from your organization's Esri portal or https://www.esri.com/en-us/arcgis/products/arcgis-pro/trial.
2. Run the installer. ArcGIS Pro installs its own conda-based Python environment (`arcgispro-py3`). You can clone this environment to add additional packages without risking the base installation.
3. After installation, open ArcGIS Pro, sign in with your Esri account, and verify that the Spatial Analyst extension is enabled (Settings > Licensing > Configure your licensing options).

**QGIS:**
1. Download the standalone installer (MSI) from https://qgis.org/download/.
2. Use the Long Term Release (LTR) version for stability, or the latest release for newest features.
3. QGIS includes its own Python installation and GRASS GIS. After installation, access the Python console from Plugins > Python Console.

### Step 3: Install Terrain Analysis Tools

**TauDEM:**
1. Download and install **Microsoft MPI** (MS-MPI) from https://learn.microsoft.com/en-us/message-passing-interface/microsoft-mpi -- install both `msmpisetup.exe` and `msmpisdk.msi`.
2. Download the TauDEM 5.3.7+ Windows installer from https://hydrology.usu.edu/taudem/taudem5/downloads.html.
3. Run the installer.
4. Add `C:\Program Files\TauDEM\TauDEM5Exe` to your system PATH:
   - Open Settings > System > About > Advanced system settings > Environment Variables.
   - Under System variables, find `Path`, click Edit, click New, and paste the path.
5. Verify from a new command prompt: `mpiexec -n 4 pitremove -h` should show the PitRemove help text.

**WhiteboxTools:**
1. From your conda environment: `pip install whitebox`.
2. The first time you import the library in Python (`import whitebox`), it will download the WhiteboxTools binary automatically.
3. Alternatively, download the standalone binary from https://www.whiteboxgeo.com/ and add it to your PATH.

### Step 4: Install Hydrologic and Groundwater Models

**HEC-HMS:**
1. Download from https://www.hec.usace.army.mil/software/hec-hms/downloads.aspx.
2. Run the installer. HEC-HMS is self-contained and does not require additional dependencies.

**HEC-RAS:**
1. Download from https://www.hec.usace.army.mil/software/hec-ras/download.aspx.
2. Run the installer. For 2D modeling, ensure your machine has a capable GPU and install the appropriate NVIDIA or AMD drivers.

**MODFLOW 6:**
1. Download from https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model.
2. Extract the zip file to a permanent location (e.g., `C:\MODFLOW\mf6.5`).
3. Add the `bin` directory to your system PATH.
4. Verify: `mf6 --version` from a command prompt.
5. For Python integration, install FloPy: `conda activate hydro && pip install flopy`.

### Step 5: Install Machine Learning Frameworks

**For CPU-only (sufficient for most hydroinformatics work):**
```
conda create -n hydro-ml python=3.12
conda activate hydro-ml
conda install scikit-learn
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install neuralhydrology
```

**For GPU-accelerated training (NVIDIA GPU required):**
```
conda create -n hydro-ml-gpu python=3.12
conda activate hydro-ml-gpu
conda install scikit-learn
conda install pytorch pytorch-cuda=12.4 -c pytorch -c nvidia
pip install neuralhydrology
```

Verify GPU availability: `python -c "import torch; print(torch.cuda.is_available())"` should return `True`.

### Step 6: Install Jupyter and Connect Environments

```
conda activate hydro
conda install jupyterlab
python -m ipykernel install --user --name hydro --display-name "Hydro Python"
conda activate hydro-ml
python -m ipykernel install --user --name hydro-ml --display-name "Hydro ML"
```

Launch JupyterLab from any environment: `jupyter lab`. You can switch between kernels (and therefore between installed package sets) within a single JupyterLab session.

---

## C.10 Getting Started: A Recommended Path for Beginners

For readers new to hydroinformatics -- perhaps a water resources engineer who has worked with spreadsheets and manual methods, or a graduate student beginning their research -- the variety of tools listed above can be overwhelming. Here is a recommended learning path that builds skills progressively, with each stage building on the previous one.

### Stage 1: Learn to See Spatial Data (Weeks 1--2)

**Goal:** Open, explore, and visualize spatial datasets.

**Tools:** QGIS (free, cross-platform, zero cost barrier).

**Activities:**
- Install QGIS and open a DEM of your study area (download from OpenTopography or the Copernicus DEM).
- Load a vector dataset (country boundaries, river network from HydroSHEDS, or your local hydrographic dataset).
- Practice changing symbology, setting coordinate reference systems, and creating a simple map layout.
- Read Chapters 2 and 4 of this book alongside these exercises.

**Why QGIS first:** Even if you will eventually use ArcGIS Pro, starting with QGIS removes the licensing barrier and teaches you GIS concepts rather than Esri-specific workflows. The skills transfer directly.

### Stage 2: Understand Terrain Hydrology (Weeks 3--4)

**Goal:** Perform a complete watershed delineation from a DEM.

**Tools:** QGIS with WhiteboxTools plugin, or ArcGIS Pro with Spatial Analyst.

**Activities:**
- Download a DEM for a small watershed you know well (10--100 km^2 is ideal).
- Follow the workflow from Chapters 9--11: fill pits, compute flow direction, compute flow accumulation, define stream network, delineate the watershed.
- Compare your delineated watershed boundary with the official boundary from your national hydrographic dataset.
- Compute the HAND grid (Chapter 14) and identify flood-prone areas.

**Why this second:** Terrain hydrology is the bread and butter of hydroinformatics. Once you can go from a raw DEM to a delineated watershed, you understand the core spatial processing chain that underpins everything else.

### Stage 3: Start Scripting (Weeks 5--8)

**Goal:** Automate a GIS workflow with Python.

**Tools:** Python (via Miniconda), Jupyter, GDAL/OGR or ArcPy.

**Activities:**
- Install Miniconda and set up a hydro environment (see Step 1 above).
- Work through Chapter 12, translating the manual GIS workflow from Stage 2 into a Python script.
- Start with simple tasks: read a raster with rasterio, compute basic statistics, write a result to a new GeoTIFF.
- Progress to calling TauDEM from Python using `subprocess.run()` or using WhiteboxTools through the whitebox Python package.
- Build a script that processes multiple watersheds in a loop.

**Why Python:** The ability to script transforms you from a GIS user into a GIS practitioner. It is the single most valuable skill investment in hydroinformatics.

### Stage 4: Connect Models to Data (Weeks 9--12)

**Goal:** Set up and run a hydrologic model, and begin to understand calibration.

**Tools:** HEC-HMS for surface water, or FloPy + MODFLOW for groundwater.

**Activities:**
- For surface water: install HEC-HMS, import the watershed parameters you derived in Stage 2, add a precipitation event, and run a rainfall-runoff simulation. Compare the simulated hydrograph with an observed record.
- For groundwater: install MODFLOW 6 and FloPy, build a simple 2D aquifer model (Chapter 21 provides a step-by-step example), run it, and visualize the head distribution.
- Read Chapter 22 to understand why calibration matters and how it works.

### Stage 5: Explore Machine Learning (Weeks 13--16)

**Goal:** Train a simple ML model to predict a hydrological variable.

**Tools:** scikit-learn, then PyTorch and NeuralHydrology.

**Activities:**
- Start with scikit-learn: train a random forest to predict daily streamflow from precipitation and temperature inputs for a single catchment.
- Progress to NeuralHydrology: train an LSTM on CAMELS data following the tutorials at https://neuralhydrology.readthedocs.io/.
- Compare the LSTM predictions with the HEC-HMS calibration from Stage 4.
- Read Chapter 23 for context on what these results mean and where ML currently outperforms (and underperforms) physical models.

### Stage 6: Go Cloud (Ongoing)

**Goal:** Run analyses at scales impossible on a desktop.

**Tools:** Google Earth Engine, Microsoft Planetary Computer.

**Activities:**
- Sign up for both platforms.
- Reproduce a familiar analysis (e.g., compute NDVI for your study area from Sentinel-2) on GEE to learn the platform.
- Explore the Planetary Computer's catalog and run a Jupyter notebook on their hosted JupyterHub.
- Apply what you have learned to a large-scale problem: delineate every watershed in your country, classify land cover across an entire river basin, or extract precipitation time series for thousands of catchments.

---

## C.11 Quick Reference Table

The following table summarizes all major software tools, their license model, and the primary chapters in which they appear.

| Software | Type | License | Primary Chapters |
|---|---|---|---|
| ArcGIS Pro | Desktop GIS | Commercial | 4, 6, 7, 9, 10, 11, 12, 18 |
| QGIS | Desktop GIS | Free/Open-source | 4, 6, 9, 10, 12, 18 |
| Google Earth Engine | Cloud GIS | Free (research) | 3, 4, 6, 11, 23, 25 |
| Planetary Computer | Cloud GIS | Free (research) | 3, 4, 6, 11, 25 |
| TauDEM | Terrain analysis | Free/Open-source | 9, 10, 11, 12, 14 |
| WhiteboxTools | Terrain analysis | Free/Open-source | 9, 10, 12, 14 |
| GRASS GIS | GIS + terrain analysis | Free/Open-source | 4, 6, 10, 12, 14 |
| Arc Hydro | GIS toolbox | Free (requires ArcGIS) | 4, 9, 11, 18, 19, 20, 21 |
| HEC-HMS | Rainfall-runoff model | Free | 15, 22, 24 |
| HEC-RAS | Hydraulic model | Free | 15, 22, 25 |
| SWAT | Watershed model | Free | 4, 22, 24 |
| MODFLOW | Groundwater model | Free | 18, 20, 21, 22, 24 |
| FEFLOW | Groundwater model | Commercial | 18, 20, 21 |
| Noah-MP | Land surface model | Free/Open-source | 16, 22 |
| LISFLOOD | Distributed hydrology | Free/Open-source | 15, 16, 22 |
| NWM | Forecast system | Free (outputs) | 11, 15, 16, 22 |
| EFAS / GloFAS | Forecast system | Free (outputs) | 11, 15, 16, 22 |
| Python | Programming language | Free/Open-source | 4, 6, 12, 21, 23, 24 |
| ArcPy | Python GIS library | Requires ArcGIS | 4, 12 |
| PyQGIS | Python GIS library | Free/Open-source | 4, 12 |
| GDAL/OGR | Data translation | Free/Open-source | 4, 6, 12 |
| FloPy | MODFLOW Python API | Free/Open-source | 21, 25 |
| Jupyter | Notebook environment | Free/Open-source | 4, 12, 25 |
| PostGIS | Spatial database | Free/Open-source | 4, 18 |
| GeoPackage | File format | Open standard | 4, 12, 18 |
| HydroShare | Data repository | Free | 1, 3, 25 |
| ChromaDB | Vector database | Free/Open-source | 18 |
| scikit-learn | Classical ML | Free/Open-source | 23, 25 |
| PyTorch | Deep learning | Free/Open-source | 23, 25 |
| TensorFlow | Deep learning | Free/Open-source | 23, 25 |
| NeuralHydrology | Hydrologic ML | Free/Open-source | 23 |
| Leaflet | Web mapping | Free/Open-source | 17, 25 |
| MapLibre GL JS | Web mapping | Free/Open-source | 25 |
| CesiumJS | 3D visualization | Free/Open-source | 18 |

---

## C.12 A Note on Reproducibility

One of the most significant shifts in hydroinformatics practice between 2015 and 2026 has been the growing expectation of reproducibility. When a published study claims that an LSTM outperforms a calibrated HEC-HMS model for a particular catchment, the community now expects to see the code, the data, and the trained model weights -- not just a table of NSE values. The tools listed in this appendix make reproducibility practical:

- **Python + Jupyter** capture the entire analysis workflow in executable documents.
- **conda environments** (exported via `conda env export > environment.yml`) lock the exact package versions used in an analysis, so someone else can recreate the same environment months or years later.
- **HydroShare** provides persistent, citable storage for datasets and model files.
- **Git** (with platforms like GitHub or GitLab) tracks every change to code and configuration files.
- **Docker** containers can package an entire computing environment -- operating system, libraries, models, and data -- into a portable image that runs identically on any machine.

For any analysis described in this book, we encourage readers to adopt this reproducibility stack from the beginning. The investment is small compared to the frustration of trying to recreate an analysis six months later when a package update has changed the default behavior of a function you relied on.

---

## C.13 Staying Current

Software versions, URLs, and best practices evolve. The following resources provide up-to-date information on the tools described in this appendix:

- **QGIS documentation:** https://docs.qgis.org/ -- updated with each release, includes tutorials and API reference.
- **Esri community and documentation:** https://community.esri.com/ and https://pro.arcgis.com/ -- active forums and comprehensive help system.
- **TauDEM GitHub:** https://github.com/dtarb/TauDEM -- issues and releases track current development.
- **MODFLOW 6 documentation:** https://modflow6.readthedocs.io/ -- official user guide and examples.
- **NeuralHydrology tutorials:** https://neuralhydrology.readthedocs.io/en/latest/tutorials/ -- step-by-step guides for training hydrologic deep learning models.
- **Google Earth Engine developer documentation:** https://developers.google.com/earth-engine -- API reference, tutorials, and community scripts.
- **Awesome-GIS:** https://github.com/sshuair/awesome-gis -- curated list of GIS resources, regularly updated.
- **CUAHSI HydroInformatics:** https://www.cuahsi.org/ -- training workshops, webinars, and the HydroShare platform.

The best way to stay current is to subscribe to the mailing lists or RSS feeds of the tools you use regularly, and to attend the annual conferences where new versions are announced: the AGU Fall Meeting, the EGU General Assembly, and the Esri User Conference for GIS-focused work; the MODFLOW and More conference for groundwater modeling; and the NeurIPS and ICML workshops on AI for Earth Sciences for machine learning applications.
