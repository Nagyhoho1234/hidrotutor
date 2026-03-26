\newpage

# Appendix D: Glossary

This glossary defines technical terms used throughout *The State of Hidroinformatics in 2026*. Terms are organized alphabetically. Each entry includes the term in bold, the Hungarian equivalent in parentheses where applicable, a concise definition, and a reference to the chapter where the term is first introduced or most fully discussed. Terms drawn from the Arc Hydro Groundwater data model are noted with (AHGW).

---

**3D Elevation Program (3DEP)**. US federal programme administered by the USGS to provide complete, high-resolution LiDAR-derived elevation data for the entire United States. The 3DEP supersedes the National Elevation Dataset and aims for nationwide coverage at 1-metre resolution or better. Chapter 3.

**Agentic AI** (agentikus MI). A class of artificial intelligence systems in which a large language model is embedded in a plan-execute-evaluate-iterate loop, enabling autonomous multi-step reasoning and tool use. Unlike conventional machine learning, which maps inputs to outputs passively, agentic AI decomposes goals into subtasks, invokes external tools (model runners, data readers, statistical calculators), evaluates results, and iterates toward a solution. Chapter 24.

**AGREE method**. A DEM reconditioning technique that modifies an elevation grid to ensure that derived flow paths conform to an independently mapped stream network. The AGREE method burns the stream network into the DEM by lowering cells along the mapped channel and smoothing adjacent cells, while preserving the general topographic structure. Chapter 9.

**American Community Survey (ACS)** (Amerikai Kozossegi Felmeres). A continuous statistical survey conducted by the US Census Bureau that collects detailed socioeconomic data from approximately three million households per year. The ACS produces 7,731 variables covering income, education, employment, disability, and housing characteristics, released as 1-year and 5-year period estimates at geographies down to the block group level. Chapter 17.

**Analytic Element Method (AEM)** (analitikus elem modszer). A groundwater simulation approach in which aquifer features -- wells, rivers, recharge zones, and conductivity boundaries -- are represented as individual mathematical elements whose contributions are superimposed to produce an exact (within assumptions) solution at any point in the domain, without requiring a computational grid or mesh. The method was pioneered by Otto Strack, and the most widely known implementation is GFLOW. Chapter 21.

**Aquifer** (vizado reteg). A geologic formation, group of formations, or part of a formation that contains sufficient saturated permeable material to yield significant quantities of water to wells and springs. Aquifers are classified by confinement (unconfined, confined, semi-confined), by lithology (porous, karstic, fractured), and by scale (local, regional, principal). Chapters 18--19.

**Aquifer feature class**. (AHGW) A polygon feature class in the Arc Hydro Groundwater data model that represents the areal extent of an aquifer or a zone within an aquifer. Each polygon carries a HGUID attribute linking it to the HydrogeologicUnit table. Chapter 19.

**Arc Hydro**. A geographic data model for water resources, originally published by David Maidment in 2002, that defines a standard vocabulary and structure for representing hydrologic features -- watersheds, stream networks, monitoring points, and time series -- in a GIS geodatabase. Arc Hydro provides the information architecture upon which NHDPlus and the National Water Model were built. Chapter 1.

**Arc Hydro Groundwater (AHGW)**. The groundwater component of the Arc Hydro data model, extending the framework to represent three-dimensional subsurface features including wells, boreholes, aquifers, hydrogeologic units, cross-sections, and simulation model grids. Published as *Arc Hydro Groundwater: GIS for Hydrogeology*. Chapters 18--21.

**ArcGIS Pro**. The current-generation desktop GIS platform from Esri, featuring a 64-bit architecture, project-based organization, and tight integration with ArcGIS Online. ArcGIS Pro provides the Spatial Analyst extension for raster terrain analysis and the Arc Hydro toolset for hydrological data modeling. Chapter 4.

**ArcPy**. Esri's Python library for ArcGIS, providing programmatic access to every geoprocessing tool in ArcGIS Pro, plus capabilities for data management, cartography, and spatial analysis. ArcPy enables scripted automation of hydrological workflows. Chapter 12.

**Aspect** (kitettes, lejtesirany). The compass direction of the steepest downslope gradient at a point on a terrain surface, measured clockwise from north in degrees (0--360). Aspect determines the direction of surface flow and influences solar radiation receipt, evapotranspiration rates, and snow accumulation patterns. Chapter 7.

**Baseflow** (alapvizhoram). The component of streamflow that derives from groundwater discharge rather than direct surface runoff. Baseflow sustains rivers during dry periods and is controlled by aquifer properties and the hydraulic gradient between the water table and the stream. Chapters 11, 22.

**Bathymetric LiDAR** (batimetriai LiDAR). A specialized LiDAR technology that uses green-wavelength laser light (approximately 532 nm) capable of penetrating water to measure the elevation of river and lake beds. Conventional near-infrared LiDAR reflects off the water surface and cannot see the bottom. Chapter 13.

**Borehole** (furas, melyfaras). A hole drilled into the subsurface for the purpose of groundwater extraction, monitoring, geotechnical investigation, or mineral exploration. Boreholes provide the primary direct observational window into subsurface geology and hydrogeology. Chapters 18--19.

**BoreholeLog**. (AHGW) A table in the Arc Hydro Groundwater data model for representing vertical data along boreholes. The table stores formation contacts, lithological descriptions, geophysical measurements, and other data recorded at specific depths. Chapter 19.

**BorePoint and BoreLine**. (AHGW) Z-enabled point and line feature classes in the Arc Hydro Groundwater data model that represent borehole data as three-dimensional geometries. BorePoint features represent individual contacts or measurements; BoreLine features represent continuous intervals along the borehole. Chapter 18.

**Calibration** (kalibralci). The process of adjusting model parameters so that simulated outputs match observed measurements, typically quantified by objective functions such as Nash-Sutcliffe Efficiency or Kling-Gupta Efficiency. Calibration is necessary because model parameters cannot be directly measured at the scale at which models operate. Chapter 22.

**CARPATCLIM**. A high-resolution (0.1-degree) gridded climate dataset covering the Carpathian Basin region, produced through interpolation of dense station networks with quality-controlled observations from 1961 to 2010. Particularly valuable for Hungarian hydrological studies because of its high station density in the region. Chapter 8.

**Catchment** (vizgyujto terulet). The area of land draining to a specific point on a stream network. In the NHDPlus framework, each catchment corresponds to one stream reach and is the fundamental spatial unit for hydrological modeling. The terms catchment, watershed, and drainage basin are often used interchangeably, though they can imply different scales. Chapters 11, 16.

**Cell size** (cellameret, racsmeretek). The length of one side of a square grid cell in a raster dataset, measured in the coordinate system's units. Cell size determines spatial resolution, data volume, and the minimum feature size that can be resolved. Chapter 5.

**Census block** (szamlalokerulent). The finest geographic unit of the US Census, typically containing 30--40 housing units along one or two street segments. There are approximately 11 million census blocks in the United States. Chapter 17.

**Census tract** (szamlalokorzet). A geographic unit of the US Census designed to contain roughly 1,200 to 8,000 people. Census tracts are the primary unit for detailed socioeconomic analysis and serve as the building blocks for many demographic studies. Chapter 17.

**CHIRPS** (Climate Hazards Group InfraRed Precipitation with Station Data). A global gridded precipitation dataset combining satellite imagery with station observations to produce daily and pentad (5-day) estimates at 0.05-degree resolution from 1981 to the present. CHIRPS is a primary precipitation source for regions with sparse gauge networks, particularly sub-Saharan Africa and South Asia. Chapter 3.

**Cloud-optimized GeoTIFF (COG)**. A variant of the GeoTIFF raster format designed for efficient access over the internet. COGs store data in internally tiled blocks with overviews, allowing software to read only the portion of the file needed for a given view extent and zoom level, without downloading the entire file. Chapter 5.

**COMID** (Common Identifier). A unique numeric identifier assigned to each stream reach in the NHDPlus hydrographic framework. COMIDs serve as the primary key linking reaches to their catchments, attributes, and the National Water Model discharge forecasts. Chapters 11, 16.

**Computational hydrology** (szamitasi hidrologia). The branch of hydrology that uses mathematical models and computing to simulate and predict water movement through the hydrological cycle. Computational hydrology emerged in the 1960s with the Stanford Watershed Model and HEC-1, and has evolved to encompass continental-scale operational forecasting systems. Chapter 1.

**Conceptual model** (konceptualis modell). A set of ideas describing a subject that allows reasoning about it. In hydrology, a conceptual model describes how water moves through a system -- for example, the water cycle concept that precipitation falls, runs off or infiltrates, evaporates, and is recycled. Chapter 1.

**Confining unit** (vizazaro reteg). A geological layer of low-permeability material (typically clay, shale, or unfractured rock) that restricts vertical movement of groundwater between aquifer layers. Confining units separate aquifers and control the degree of hydraulic connection in multi-layered aquifer systems. Chapter 20.

**Copernicus DEM** (Kopernikusz digitalis domborzatmodell). The primary European digital elevation dataset, derived from the TanDEM-X radar satellite mission. Available in three variants: GLO-30 (30-metre resolution, global, free), GLO-90 (90-metre, global, free), and EEA-10 (10-metre, European coverage). The Copernicus DEM is a digital surface model, meaning it captures building and vegetation tops rather than bare ground. Chapter 3.

**Copernicus programme** (Kopernikusz program). The European Union's Earth observation programme, managed by the European Commission in partnership with the European Space Agency. Copernicus provides free, open data from the Sentinel satellite constellation and a suite of information services including the Emergency Management Service and the Climate Change Service. Chapter 3.

**Curve number (CN)** (lefolyas szam). A dimensionless empirical parameter in the NRCS (formerly SCS) rainfall-runoff method that characterizes the runoff potential of a soil-cover-condition combination. Values range from 30 (very low runoff potential) to 100 (impervious surface). The CN integrates soil type, land cover, antecedent moisture, and management practice into a single index. Chapter 22.

**D8 algorithm** (D8 algoritmus). The most widely used method for computing flow direction on a grid DEM, published by O'Callaghan and Mark in 1984. For each cell, D8 evaluates the slope to all eight neighbors and assigns flow to the single neighbor with the steepest downslope gradient. The algorithm constrains flow to one of eight discrete directions at 45-degree intervals. Chapter 10.

**D-infinity (D-inf) algorithm** (D-vegtelen algoritmus). A flow direction algorithm published by David Tarboton in 1997 that removes the directional constraint of D8 by fitting triangular facets to the eight neighbors of each cell and computing the steepest downslope direction as a continuous angle. Flow can be apportioned between two neighboring cells in proportion to the angle, producing smoother, more physically realistic flow paths. Chapters 7, 10.

**Data assimilation** (adatasszimilacio). The mathematical framework for combining model predictions with observations to produce a state estimate that is better than either source alone. Data assimilation methods -- including the Kalman filter, Ensemble Kalman Filter, and variational approaches -- continuously reconcile model forecasts with incoming sensor data in operational systems. Chapter 25.

**Data model** (adatmodell). A structured framework for describing a subject and storing data about it. In GIS, a data model defines what information is stored, how it is organized, and how its components relate to one another. Arc Hydro is a geographic data model for water resources. Chapter 1.

**Datum** (datum, geodeziai datum). An ellipsoid that has been positioned and oriented relative to the actual Earth, defining the reference frame in which coordinates have meaning. A datum anchors the mathematical surface of the ellipsoid to specific points on the physical Earth. Modern datums are geocentric (centered on Earth's center of mass); legacy datums are regional. Chapter 2.

**DDM-5** (Digitalis Domborzatmodell). Hungary's national digital elevation model at 5-metre resolution, produced by the Lechner Knowledge Centre in the EOV coordinate system (EPSG:23700). Derived from 1:10,000 topographic contour lines and stereophotogrammetry. The DDM-5 is the authoritative national elevation product for Hungary. Chapter 3.

**Delaunay triangulation** (Delaunay haromszogeles). A triangulation of a set of points in which no point lies inside the circumscribed circle of any triangle. The Delaunay triangulation is the geometric dual of Thiessen/Voronoi polygons and produces the most equilateral triangles possible, making it optimal for TIN-based surface representation. Chapter 8.

**DEM (Digital Elevation Model)** (digitalis domborzatmodell). A raster grid in which each cell stores the elevation of the terrain at that location. DEMs are the foundation of computational hydrology; from them, slope, aspect, flow direction, flow accumulation, stream networks, and watershed boundaries are derived. Chapters 3, 5.

**DEM conditioning** (DEM feltetelkondicionalo). The process of modifying a raw digital elevation model to enforce continuous downhill drainage from every cell to the domain boundary. DEM conditioning involves filling pits, resolving flat areas, and optionally burning in known stream networks. It is the essential first step in any terrain-based hydrological analysis. Chapter 9.

**Digital surface model (DSM)** (digitalis felszinmodell). An elevation model that represents the tops of all objects on the Earth's surface, including buildings, trees, and other vegetation. A DSM differs from a DEM or DTM in that it does not represent the bare ground. The Copernicus DEM is a DSM. Chapter 13.

**Digital twin** (digitalis iker). A virtual replica of a physical system that maintains a continuous, bidirectional connection with the real system through sensor data feeds, model updates, and -- at the highest maturity levels -- automated control actions. Digital twins for water systems span four maturity levels from static models to autonomous control. Chapter 25.

**Drainage density** (vizhaolzat-surusseg). The total length of all stream channels within a watershed divided by the watershed area, expressed in km per km squared. Drainage density is inversely related to mean hillslope length and directly affects the time water takes to reach the nearest channel. Chapter 11.

**DREAM** (Differential Evolution Adaptive Metropolis). A Bayesian Markov Chain Monte Carlo algorithm used for model calibration that explores the parameter space using multiple chains exchanging information, producing posterior probability distributions of parameters rather than a single optimum. Chapter 22.

**E-OBS**. A European gridded daily dataset of temperature and precipitation, produced by the European Climate Assessment and Dataset project at a resolution of 0.1 degrees (approximately 11 km). E-OBS is the standard gridded climate product for European hydrological studies and is based on the densest available station network. Chapter 8.

**EFAS (European Flood Awareness System)** (Europai Arviz Figyelmezteto Rendszer). The pan-European flood forecasting system operated by the Copernicus Emergency Management Service at ECMWF. EFAS provides medium-range ensemble flood forecasts for the entire European continent, using the LISFLOOD hydrological model driven by ECMWF weather forecasts. Chapters 1, 16.

**Ellipsoid** (ellipszoid, forgasi ellipszoid). Also called a spheroid. The three-dimensional surface generated by rotating an ellipse about its shorter (polar) axis, serving as the mathematical approximation of the Earth's shape for coordinate system definitions. An ellipsoid is defined by its semi-major axis and flattening. Chapter 2.

**Ensemble Kalman Filter (EnKF)** (Ensemble Kalman-szuro). A sequential data assimilation method that represents model uncertainty through an ensemble of 50--500 parallel model runs, each with slightly different initial conditions and parameters. The ensemble spread approximates the error covariance, and each member is adjusted when observations arrive. Chapter 25.

**EOV (Egyseges Orszagos Vetuleti rendszer)** (Egyseges Orszagos Vetuleti rendszer). Hungary's unified national projected coordinate system (EPSG:23700), based on the Hungarian Datum of 1972 (HD72) and the GRS 1967 ellipsoid. EOV uses a transverse Mercator projection with a central meridian at 19.0481 degrees east. EOV coordinates have Northing values in the range 0--400,000 and Easting values in the range 400,000--1,000,000. Chapter 2.

**Equifinality** (ekvifinalizas). The phenomenon in which multiple distinct parameter sets produce equally good (or equally poor) fits to observed data, making it impossible to identify a single "correct" parameterization. Equifinality is a fundamental challenge in model calibration and motivates the use of Bayesian methods that characterize parameter uncertainty rather than seeking a single optimum. Chapter 22.

**ERA5**. The fifth-generation atmospheric reanalysis dataset produced by the European Centre for Medium-Range Weather Forecasts (ECMWF), providing hourly estimates of atmospheric, land, and ocean variables from 1940 to the present at approximately 31 km horizontal resolution. ERA5-Land provides enhanced land surface variables at approximately 9 km resolution. Chapter 3.

**ETRS89 (European Terrestrial Reference System 1989)** (Europai Foldfelszini Referenciarendszer 1989). The official geodetic reference system for the European Union, realized through a network of permanent GNSS stations. ETRS89 is based on the GRS 1980 ellipsoid and is compatible with WGS84 at the centimetre level. It is the coordinate reference system required by the INSPIRE Directive for European spatial data. Chapter 2.

**EU-Hydro**. The European hydrographic dataset produced by the Copernicus programme, providing a pan-European river network and catchment delineation derived from high-resolution satellite imagery and the Copernicus DEM. EU-Hydro complements national hydrographic datasets by providing cross-border consistency. Chapter 16.

**Evapotranspiration (ET)** (evapotranszpiracio, parologas). The combined process of evaporation from soil and water surfaces and transpiration from vegetation. ET is a major component of the water balance, typically accounting for 40--80% of precipitation in temperate climates. It is driven by solar radiation, temperature, humidity, wind, and vegetation characteristics. Chapter 6.

**Extent** (terjedelem, kiterjedesek). The total geographic area covered by a raster grid, defined by its bounding coordinates (xmin, ymin, xmax, ymax). The extent must encompass the study area plus a buffer for watershed delineation to avoid edge effects. Chapter 5.

**Extrapolation** (extrapolacio). Estimation of values beyond the domain of known sample points, carrying substantially higher uncertainty than interpolation (estimation within the sample domain). In spatial analysis, extrapolation occurs when a raster extent extends beyond the outermost observation points. Chapter 8.

**FAIR principles** (FAIR elvek). A set of data management principles requiring that research data be Findable, Accessible, Interoperable, and Reusable. HydroShare, the CUAHSI-operated platform for sharing hydrologic data and models, implements FAIR principles for hydrologic research products. Chapter 1.

**Feature** (objektum, elem). A row in a feature class representing a spatial object, including its geometry (point, line, polygon, or multipatch) and associated attributes. Chapter 4.

**Feature class** (objektum osztaly, elem osztaly). A collection of features with the same geometry type, attributes, and relationships, stored as a table in a geodatabase with a Shape field defining the geometry. Feature classes are the fundamental unit of vector data storage in GIS. Chapter 4.

**Feature dataset** (objektum adat, elem adathalmaz). A container within a geodatabase for grouping spatially related feature classes that share the same coordinate system. Feature datasets also contain relationship classes, topology rules, and network classes. Chapters 4, 18.

**FEFLOW**. A commercial finite element groundwater modelling software developed by the DHI Group, widely used in Europe for simulating flow, mass, and heat transport in porous and fractured media. FEFLOW supports unstructured grids and complex 3D geological structures, and integrates with GIS through shapefile and geodatabase import/export. Chapter 21.

**Field** (mezo, folytonos mezo). In geographic information science, a quantity defined at every possible position in space -- a continuous phenomenon such as elevation, temperature, or soil moisture. Fields are represented digitally as raster grids, TINs, or contour-flowline models. Chapter 5.

**Finite difference method (FDM)** (veges differencia modszer). A numerical approach for solving partial differential equations by subdividing the model domain into a regular rectangular grid and approximating continuous derivatives with differences between neighboring cell values. MODFLOW is the most widely used finite difference groundwater model. Chapter 21.

**Finite element method (FEM)** (veges elem modszer). A numerical approach for solving partial differential equations by subdividing the domain into small geometric elements (triangles, tetrahedra, prisms) and approximating the solution with polynomial functions within each element. FEFLOW is the primary finite element code for groundwater modelling. Chapter 21.

**FIPS code** (FIPS kod). Federal Information Processing System code, a standardized numeric identifier for US geographic units. State codes are 2 digits (e.g., Texas = 48), county codes are 3 digits, tract codes are 6 digits, and block codes are 4 digits. FIPS codes enable programmatic joining of census boundaries to attribute tables. Chapter 17.

**Flattening** (laposodas). A parameter of an ellipsoid defined as $f = (a - b) / a$, where $a$ is the semi-major axis (equatorial radius) and $b$ is the semi-minor axis (polar radius). For the Earth, $f \approx 1/298.257$. Chapter 2.

**Flow accumulation** (vizgyujtesi vizhozam, lefolyas osszegyulesek). A raster grid in which each cell's value represents the number of upstream cells (or the total upstream drainage area) that drain through it, computed by tracing flow directions from every cell. Cells with high flow accumulation values lie on streams; cells with low values lie on hillslopes. Chapter 10.

**Flow direction** (aramlasi irany). A raster grid in which each cell's value indicates the direction water flows from that cell, determined by the topographic slope to neighbouring cells. Flow direction is the fundamental intermediate product between a conditioned DEM and derived stream networks, watersheds, and HAND surfaces. Chapter 10.

**Focal operation** (kornyezeti muvelet). A map algebra operation in which each output cell is computed from a window of surrounding cells in the input grid. Slope and aspect calculations are classic examples. Also called a neighbourhood operation. Chapter 6.

**Geocentric datum** (geocentrikus datum). A geodetic datum in which the centre of the reference ellipsoid coincides with the Earth's centre of mass. Modern datums such as WGS84 and ETRS89 are geocentric, providing globally consistent reference frames. Older national datums are not geocentric. Chapter 2.

**Geodatabase** (geoadatbazis). A repository of geographic information organized into structured datasets within a relational database system. Geodatabases enforce spatial integrity rules, maintain relationships between features, and support domains, subtypes, and topology. The Esri file geodatabase (.gdb) is the standard format for ArcGIS Pro. Chapters 4, 18.

**Geodesy** (geodezia). The science of measuring and representing the Earth's shape, orientation, and gravity field. Geodesy provides the reference surfaces (geoid and ellipsoid), coordinate systems, and datum transformations that underpin all spatial water data. Chapter 2.

**GeoArea**. (AHGW) A polygon feature class in the Arc Hydro Groundwater data model representing the two-dimensional footprint of a hydrogeologic unit. GeoArea polygons carry HGUID attributes linking them to the HydrogeologicUnit classification table. Chapter 20.

**Geographic data model** (foldrajzi adatmodell). A data model specifically designed for representing features and phenomena located on the Earth, using spatial datasets within a GIS. Arc Hydro is a geographic data model for water resources. Chapter 1.

**Geoid** (geoid). The equipotential surface of Earth's gravity field that best approximates mean sea level. The geoid is smooth but not regular -- it undulates due to variations in subsurface mass distribution. It is the natural reference for elevation because water flows from higher to lower gravitational potential. Chapter 2.

**Geoid undulation** (geoidhullam). The vertical separation between the geoid surface and the reference ellipsoid, typically denoted $N$. The relationship between ellipsoidal height $h$, orthometric height $H$, and geoid undulation is $h = H + N$. Chapter 2.

**Geoprocessing** (terfeldolgozas). The GIS function of performing spatial analysis operations on geographic data, producing new datasets as output. Geoprocessing tools include overlay, buffer, clip, dissolve, and the entire suite of raster terrain analysis operations fundamental to hydrology. Chapter 4.

**GeoRasters**. (AHGW) A raster catalog in the Arc Hydro Groundwater data model for storing and indexing raster datasets that describe properties of hydrogeologic units, such as top elevation surfaces, thickness maps, or hydraulic conductivity distributions. Chapter 20.

**GeoSection**. (AHGW) A multipatch feature class in the Arc Hydro Groundwater data model representing three-dimensional panels for constructing vertical geological cross-sections. Each GeoSection feature represents one hydrogeologic unit along one section line. Chapter 20.

**GeoVolume**. (AHGW) A multipatch feature class for representing hydrogeologic units as three-dimensional volume objects. GeoVolumes capture the full 3D geometry of subsurface formations. Chapter 20.

**Geoscientific Information Systems (GSIS)** (geotudomanyi informacios rendszerek). Specialized information systems designed for representing complex three-dimensional subsurface objects using surface representations or volume elements. GSIS differ from traditional GIS in their native support for 3D geological modelling. Chapter 18.

**GloFAS (Global Flood Awareness System)** (Globalis Arviz Figyelmezteto Rendszer). The global extension of EFAS, providing discharge forecasts for every major river on Earth. GloFAS is operated by the Copernicus Emergency Management Service and provides 30-day probabilistic forecasts for rivers worldwide. Chapter 16.

**Google Earth Engine (GEE)**. A cloud-based geospatial analysis platform providing free access to a multi-petabyte archive of satellite imagery and geospatial datasets, along with cloud computing infrastructure for processing them. GEE is transformative for water resources because it makes continental-scale analysis feasible without downloading data. Chapter 4.

**GRACE** (Gravity Recovery and Climate Experiment). A satellite mission (and its successor GRACE-FO) that measures changes in Earth's gravity field, enabling detection of large-scale changes in terrestrial water storage -- including groundwater depletion, ice mass loss, and seasonal water redistribution. GRACE provided the first satellite-based evidence of the 2011 Texas drought's impact on groundwater. Chapters 1, 2.

**Grid network** (racshalo, vizrajzi halozat). The directed graph formed when D8 flow directions are computed for every cell in a DEM, in which each cell has exactly one outgoing edge pointing to its downstream neighbor. The grid network is a forest of trees rooted at outlet cells and implicitly encodes the complete drainage structure of the landscape. Chapter 10.

**GR4J** (modele du Genie Rural a 4 parametres Journalier). A parsimonious conceptual rainfall-runoff model with only four parameters, developed at INRAE in France. Despite its simplicity, GR4J performs competitively with far more complex models and is frequently used as a benchmark in calibration studies. Chapter 22.

**Groundwater body** (felszin alatti viztest). An administrative-regulatory unit defined under the EU Water Framework Directive for groundwater management purposes. Hungary has delineated 185 groundwater bodies grouped into four main types: porous, karstic, combined, and thermal. Each body is assigned quantitative and chemical status. Chapter 19.

**Hallucination** (hallucinacio). In the context of large language models, the generation of plausible-sounding but factually incorrect information. Grounding mechanisms -- including real data, model outputs, and domain constraints -- are essential for mitigating hallucination in agentic AI systems applied to hydrological modelling. Chapter 24.

**HAND (Height Above Nearest Drainage)** (legkozelebbi vizfolyashoz viszonyitott magassag). A raster surface derived from a DEM in which each cell's value represents its vertical distance above the nearest stream channel, measured along the hydrologic flow path. HAND transforms absolute elevation into a stream-relative reference frame that directly indicates flood vulnerability. Chapter 14.

**HEC-HMS** (Hydrologic Engineering Center's Hydrologic Modeling System). A widely used rainfall-runoff model developed by the US Army Corps of Engineers. HEC-HMS provides modular options for loss estimation (SCS CN, Green-Ampt), transform (Clark, Snyder unit hydrograph), baseflow, and channel routing (Muskingum). Chapters 16, 22.

**HEC-RAS** (Hydrologic Engineering Center's River Analysis System). Standard hydraulic modelling software for one-dimensional and two-dimensional river flow analysis, steady and unsteady flow simulation, sediment transport, and water quality modelling. HEC-RAS uses surveyed cross-sections to characterize channel geometry. Chapter 15.

**Helmert transformation** (Helmert transzformacio). A seven-parameter coordinate transformation (three translations, three rotations, and a scale factor) used to convert between geodetic datums. Helmert parameters are specific to each pair of datums and are essential for correctly combining data from different national coordinate systems. Chapter 2.

**Hidroinformatics** (hidroinformatika). The discipline at the intersection of hydrology, geographic information science, computational modelling, and data science. The Hungarian-inflected spelling signals a perspective rooted in the Central European water management tradition, informed by the Hungarian experience of managing one of Europe's most complex river systems. Chapter 1.

**HorizonID** (horizont azonosito). An integer index in the Arc Hydro Groundwater data model that defines the vertical arrangement of hydrogeologic units in a depositional sequence. HorizonID values are assigned from bottom to top, with the smallest value given to the basal unit. Chapter 20.

**HRRR (High Resolution Rapid Refresh)** (nagy felbontasu gyors frissites). A convection-allowing atmospheric model operated by NOAA that assimilates radar, aircraft, satellite, and surface observations every hour to produce precipitation forecasts at 3 km resolution, up to 18 hours ahead. The HRRR provides the short-range weather input to the US National Water Model. Chapter 16.

**HydroCode**. A text attribute in the Arc Hydro data model serving as a permanent public identifier for a feature, providing linkage to external information systems (e.g., NHDPlus COMIDs, state aquifer codes). Chapter 19.

**Hydrogeologic framework** (hidrogeologiai keret). A simplified representation of the subsurface that classifies geological formations according to their hydraulic properties (aquifer, confining unit, aquitard) rather than their depositional history. The framework defines the units, their vertical arrangement, spatial extent, and three-dimensional boundaries. Chapter 20.

**HydrogeologicUnit table**. (AHGW) The central organizing table of the hydrogeologic framework in the Arc Hydro Groundwater data model. Each row defines a conceptual hydrogeologic unit with attributes including HydroID, HGUCode, HGUName, AquiferID, and HorizonID. All spatial representations of subsurface units reference this table. Chapter 20.

**HydroID**. An integer attribute in the Arc Hydro data model that uniquely identifies objects across an entire geodatabase, not just within a single feature class. HydroID differs from ObjectID in its geodatabase-wide uniqueness. Chapters 18--20.

**HydroSHEDS** (Hydrological Data and Maps Based on Shuttle Elevation Derivatives at Multiple Scales). A global dataset providing river networks, watershed boundaries, flow direction grids, and flow accumulation data derived from SRTM elevation data. HydroSHEDS covers the entire world and is the primary hydrographic reference for regions without national mapping infrastructure. Chapter 3.

**HydroShare**. A web-based system for sharing hydrologic data and models, operated by CUAHSI and developed by David Tarboton and colleagues. HydroShare implements the FAIR principles and enables researchers to publish data, models, and computational workflows with permanent DOIs. Chapter 1.

**IDW (Inverse Distance Weighting)** (forditott tavolsaggal sulyozott interpolacio). A spatial interpolation method that estimates values at unmeasured locations as a weighted average of surrounding sample points, with weights decreasing as an inverse power of the distance. The power parameter $p$ (commonly 2) controls how rapidly the influence decays with distance. Chapter 8.

**IGRAC** (International Groundwater Resources Assessment Centre). A UNESCO/WMO centre based in Delft, Netherlands, that maintains the Global Groundwater Information System (GGIS), a web-based platform aggregating national groundwater data into a searchable global database. Chapter 19.

**Infiltration** (beszivargozas). The process by which water enters the soil surface, governed by soil texture, structure, moisture content, and surface slope. The partitioning of precipitation between infiltration and surface runoff is one of the most important calculations in hydrology. Chapters 7, 22.

**INSPIRE Directive** (INSPIRE iranyelv). European Union directive (2007/2/EC) establishing an Infrastructure for Spatial Information in the European Community, requiring EU member states to publish spatial data through standardized web services using common data specifications. INSPIRE ensures interoperability of environmental and geographic data across Europe. Chapter 4.

**Interpolation** (interpolacio). The process of estimating values at unmeasured locations from a set of known sample points, producing a continuous surface. Principal methods include nearest neighbour (Thiessen polygons), inverse distance weighting, spline, and kriging. Chapter 8.

**Kalman filter** (Kalman-szuro). A sequential data assimilation method that combines model predictions with observations using optimal weighting based on their respective uncertainties. The Kalman filter maintains an estimate of the system state and its uncertainty, updating both each time a new observation arrives. Chapter 25.

**Karst** (karszt). A landscape formed by the dissolution of soluble rocks (limestone, dolomite, gypsum), characterized by sinkholes, caves, and underground drainage. Karst terrain presents special challenges for DEM conditioning because sinkholes are genuine closed depressions, not artefacts. Hungary's Aggtelek Karst is a UNESCO World Heritage Site. Chapter 9.

**KGE (Kling-Gupta Efficiency)** (Kling-Gupta hatekonysag). A model performance metric that decomposes into three components: correlation $r$ (timing accuracy), bias ratio $\beta$ (volume accuracy), and variability ratio $\gamma$ (spread accuracy). KGE values above 0.0 indicate the model outperforms a naive benchmark. KGE is increasingly preferred over NSE for calibration. Chapter 22.

**Kriging** (krigelesi interpolacio). A geostatistical interpolation method that uses the spatial correlation structure of the data (modelled through a variogram) to compute optimal weights for prediction, providing both estimates and prediction uncertainties. Kriging is the only interpolation method that explicitly models spatial dependence. Chapter 8.

**KSH (Kozponti Statisztikai Hivatal)** (Kozponti Statisztikai Hivatal). Hungary's Central Statistical Office, responsible for conducting the national census and producing demographic statistics. The most recent census (nepszamlalas 2022) was conducted in late 2022 using a combined online and traditional methodology. Chapter 17.

**Land surface model (LSM)** (felszini modell). A computational model representing the exchange of water and energy between the land surface and the atmosphere. LSMs partition precipitation among infiltration, runoff, and evapotranspiration, and are key components of weather forecasting and climate models. Noah-MP and ECLand are widely used LSMs. Chapter 22.

**LAS format** (LAS formatum). The standard file format for storing LiDAR point cloud data, defined by the American Society for Photogrammetry and Remote Sensing (ASPRS). Each point record contains x, y, z coordinates, intensity, return number, classification, and other attributes. Chapter 13.

**LiDAR (Light Detection and Ranging)** (LiDAR). A remote sensing technology that measures distances by emitting laser pulses and timing their return from targets. Airborne LiDAR produces three-dimensional point clouds with centimetre-level vertical accuracy, enabling the creation of high-resolution bare-earth DEMs essential for detailed flood mapping. Chapter 13.

**Linear mode LiDAR** (linearis modu LiDAR). The conventional LiDAR technology in which each pulse is emitted individually, reflected from a target, and detected by a single detector element whose response is proportional to the intensity of the incoming light. Linear mode systems record multiple returns per pulse and are the source of most existing LiDAR data. Chapter 13.

**Local operation** (helyi muvelet). A map algebra operation in which each output cell is computed solely from the corresponding cell(s) in one or more input grids, with no interaction between neighbouring cells. Arithmetic operations (adding two grids) are local operations. Chapter 6.

**LSTM (Long Short-Term Memory)** (LSTM). A type of recurrent neural network designed to learn long-range temporal dependencies through a gated cell architecture containing forget, input, and output gates. LSTMs have demonstrated the ability to predict streamflow at ungauged locations with accuracy comparable to or exceeding process-based models. Chapter 23.

**Manning's equation** (Manning egyenlet). The empirical equation relating mean flow velocity in an open channel to the hydraulic radius, channel slope, and Manning's roughness coefficient $n$. Manning's equation is the workhorse of open-channel hydraulics and underpins the conversion of discharge forecasts to water depths in HAND-based flood inundation mapping. Chapter 15.

**Map algebra** (terkepi algebra). A computational framework formalized by Dana Tomlin in which raster grids are treated as variables in algebraic expressions, with operations applied simultaneously to every cell. Map algebra operations are classified as local, focal, zonal, or global based on the spatial scope of the computation. Chapter 6.

**Map projection** (terkepi vetuleti rendszer). A mathematical transformation that converts locations on the curved surface of the Earth (defined by latitude and longitude on an ellipsoid) to locations on a flat map surface. Projections inevitably distort some property -- area, shape, distance, or direction -- and the choice of projection affects the accuracy of hydrological calculations. Chapter 2.

**Mathematical model** (matematikai modell). A representation of a conceptual model in equations and symbols. The water balance equation $P = Q + ET + \Delta S$ is a mathematical model of the hydrological cycle. Chapter 1.

**MBFSZ (Magyar Banyaszati es Foldtani Szolgalat)** (Magyar Banyaszati es Foldtani Szolgalat). The former Hungarian Mining and Geological Survey, now reorganized under SZTFH. MBFSZ maintained Hungary's national geological map database and borehole records. Chapter 18.

**Microsoft Planetary Computer**. A cloud-based geospatial analysis platform built on Azure infrastructure, providing access to environmental datasets through the STAC standard and a JupyterHub environment for Python-based analysis. Planetary Computer hosts Copernicus DEM, Sentinel imagery, ERA5 data, and many other datasets relevant to hydrology. Chapter 4.

**ModelBuilder** (ModelBuilder). ArcGIS Pro's graphical model builder that allows users to chain geoprocessing tools into automated workflows without writing code. ModelBuilder can export workflows as Python scripts, serving as a bridge between interactive GIS use and scripted automation. Chapter 12.

**MODFLOW** (MODFLOW). The modular finite-difference groundwater flow model developed by the USGS, and the most widely used groundwater simulation model worldwide. MODFLOW discretizes aquifer systems into three-dimensional grids of rectangular cells and solves the groundwater flow equation using finite differences. The latest generation, MODFLOW 6, supports unstructured grids. Chapters 21--22.

**Multipatch** (multipatch). A GIS geometry type composed of three-dimensional rings and triangles that represents objects occupying a 3D area or volume. In the groundwater data model, multipatches represent GeoVolume, GeoSection, and Cell3D features. Chapter 18.

**Multiple returns** (tobbszoros visszaverodesi). A feature of linear mode LiDAR in which a single laser pulse generates several distinct reflections from objects at different heights -- for example, tree canopy (first return), understory (intermediate returns), and ground surface (last return). Multiple returns enable LiDAR to produce bare-earth DEMs in forested areas. Chapter 13.

**Muskingum routing** (Muskingum aramlatatvezetesi). A storage-based channel routing method that relates outflow from a river reach to inflow and reach storage through parameters $K$ (travel time) and $x$ (attenuation weighting). The US National Water Model uses Muskingum routing (via the RAPID model) for all 2.7 million NHDPlus reaches. Chapter 16.

**Nash-Sutcliffe Efficiency (NSE)** (Nash-Sutcliffe hatekonysag). The most widely used performance metric for hydrological model evaluation, comparing the sum of squared errors between observed and simulated values to the variance of observations. NSE = 1.0 is a perfect match; NSE = 0.0 means the model is no better than predicting the observed mean. Chapter 22.

**National Elevation Dataset (NED)** (Nemzeti Szintkozmodell). The US national seamless DEM produced by the USGS, now being superseded by the 3DEP programme. The standard NED product is a 1/3 arc-second grid (approximately 10 metres). Chapter 3.

**National Water Model (NWM)** (Nemzeti Vizhozam Modell). The US operational hydrological forecasting system that produces discharge forecasts for 2.7 million NHDPlus stream reaches at hourly intervals. The NWM couples weather models (HRRR, GFS), the Noah-MP land surface model, and the RAPID channel routing model on NOAA supercomputing infrastructure. Chapter 16.

**NHDPlus (National Hydrography Dataset Plus)** (Nemzeti Hidrografiai Adatbazis Plusszavaz). The geospatial framework of the US National Water Model, providing 2.7 million stream reaches with unique identifiers (COMIDs), corresponding catchments, connectivity tables, and physical attributes. NHDPlus is the linchpin connecting weather data, land surface models, and channel routing in the US flood forecasting system. Chapters 3, 16.

**Noah-MP** (Noah-MP). The Noah Multi-Physics land surface model used in the US National Water Model and the WRF atmospheric model. Noah-MP partitions precipitation among interception, infiltration, runoff, and evapotranspiration using modular physics options, operating on a 1 km grid with four soil layers and a groundwater reservoir. Chapter 16.

**NODATA** (NODATA). A special value in a raster grid indicating that no data exists for a particular cell -- the cell is undefined rather than having a value of zero. Proper handling of NODATA is critical in map algebra: any arithmetic operation involving a NODATA cell produces NODATA in the output. Chapter 5.

**NSE** -- see **Nash-Sutcliffe Efficiency**.

**NUTS (Nomenclature of Territorial Units for Statistics)** (Statisztikai Cellu Teruletegysegek Nomenklaturaja). The European Union's hierarchical classification of statistical regions. Hungary has 7 NUTS-2 regions and 20 NUTS-3 units (19 counties plus Budapest). NUTS regions serve as the spatial framework for European demographic, economic, and environmental reporting. Chapter 17.

**Orthometric height** (ortometrikus magassag). The elevation of a point above the geoid, measured along the plumb line. Orthometric height corresponds to what is colloquially called "elevation above sea level." It differs from ellipsoidal height (measured above the mathematical ellipsoid) by the geoid undulation. Chapter 2.

**Overfitting** (tulillesztes). In machine learning, the condition in which a model learns the noise and idiosyncrasies of the training data rather than the underlying pattern, resulting in excellent training performance but poor generalization to new data. Overfitting is combated through regularization, dropout, early stopping, and proper data splitting. Chapter 23.

**OVF (Orszagos Vizugyi Foigazgatosag)** (Orszagos Vizugyi Foigazgatosag). Hungary's General Directorate of Water Management, responsible for national flood defense, water resource management, and operation of the hydrographic monitoring network. OVF operates the HYDROINFO real-time water level monitoring system and manages flood forecasting for the Danube and Tisza systems. Chapters 3, 16.

**Particle filter** (reszecskeszuro). A sequential data assimilation method that represents model uncertainty through weighted ensemble members (particles), assigning weights based on agreement with observations and resampling to concentrate computational effort on plausible states. Particle filters handle strongly nonlinear systems. Chapter 25.

**PEST** (Parameter ESTimation). A model-independent parameter estimation and uncertainty analysis software suite developed by John Doherty. PEST uses regularized inversion to calibrate models with spatially distributed parameters, and has become the standard tool for MODFLOW calibration using pilot point methods. Chapter 22.

**Pit** (melypont, bemelyleszitett medence). A cell or group of cells in a DEM that is completely surrounded by higher terrain, with no downslope neighbor to receive flow. Pits may be DEM artefacts (caused by measurement errors or data processing) or genuine topographic features (sinkholes, kettle holes). Removing artefact pits is the core task of DEM conditioning. Chapter 9.

**Point cloud** (pontfelho). The raw output of a LiDAR survey: a collection of millions to billions of individual three-dimensional measurements (x, y, z plus intensity, return number, and classification), stored in LAS or LAZ format. Point clouds are processed into gridded DEMs through classification (ground vs. non-ground) and interpolation. Chapter 13.

**PointZ, PolylineZ, PolygonZ** (PointZ, PolylineZ, PolygonZ). Z-enabled feature geometry types in a geodatabase that carry a vertical coordinate (z value) at every vertex, allowing features to exist in three-dimensional space. PointZ features represent borehole contacts, PolylineZ features represent borehole paths, and PolygonZ features define surfaces in 3D. Chapter 18.

**Pour point** (kifoly pont). The lowest cell on the rim enclosing a pit in a DEM -- the point where water would first overflow if the pit were slowly filled. In watershed delineation, a pour point is also the outlet location from which the upstream contributing area is traced. Chapters 9, 11.

**PRISM** (Parameter-elevation Regressions on Independent Slopes Model). A climate mapping system that creates high-resolution gridded estimates of precipitation and temperature using regression relationships with physiographic variables (elevation, slope orientation, proximity to coast). PRISM is the standard gridded climate product for the United States. Chapter 8.

**Processing Graphical Modeler** (Feldolgozo Grafikus Modellszerkeszto). QGIS's equivalent of ArcGIS ModelBuilder, allowing users to chain geoprocessing tools into automated workflows through a visual drag-and-connect interface. The Graphical Modeler can export workflows as Python scripts. Chapter 12.

**QGIS** (QGIS). The leading open-source desktop GIS platform, developed by a global community under the GNU General Public License. QGIS provides comprehensive vector and raster analysis, a plugin ecosystem including hydrological tools (GRASS, SAGA, WhiteboxTools), and Python scripting through PyQGIS. Chapter 4.

**RAPID** (Routing Application for Parallel computatIon of Discharge). The channel routing model used in the US National Water Model, propagating water through 2.7 million NHDPlus reaches using a Muskingum routing scheme. RAPID is designed for massive parallelism, decomposing the network for simultaneous processing on thousands of cores. Chapter 16.

**Raster** (raszter). A spatial data model that divides geographic space into a regular mesh of identically sized square cells, each holding a single numerical value. Raster grids are the dominant data structure for terrain analysis, precipitation fields, land cover, and virtually all continuous spatial phenomena in hydrology. Chapters 5--6.

**Raster Calculator** (raszterszamito). A GIS tool for performing map algebra operations by writing algebraic expressions that reference input raster layers. The Raster Calculator evaluates the expression cell by cell to produce an output raster. Available in ArcGIS Pro (Spatial Analyst) and QGIS (Processing). Chapter 6.

**Rating curve** (vizallas-vizhozam gorbe). A mathematical relationship between water stage (depth or level) and discharge at a specific stream location. In HAND-based flood mapping, synthetic rating curves are derived from the terrain geometry of each reach, enabling conversion of discharge forecasts to water depths without surveyed cross-sections. Chapter 15.

**Reach** (vizfoldajzi szakasz). A continuous segment of a stream network between junctions, defined during stream segmentation. Each reach has a unique identifier and associated catchment. The NHDPlus framework defines 2.7 million reaches across the United States. Chapter 11.

**Resampling** (ujramintavetelezesi). The process of recalculating cell values when a raster is transformed to a different cell size, extent, or coordinate system. Common methods include nearest neighbour (preserves original values), bilinear interpolation (weighted average of four nearest cells), and cubic convolution (weighted average of sixteen cells). Chapter 6.

**SCS Curve Number method** -- see **Curve number**.

**Semi-major axis** (nagy feltengelysugaras). The equatorial radius of an ellipsoid, denoted $a$. For the Earth, $a \approx 6{,}378{,}137$ metres. Chapter 2.

**Sentinel-2** (Sentinel-2). The European multispectral imaging mission of the Copernicus programme, providing global land surface imagery at 10--60 metre resolution with a 5-day revisit time. Sentinel-2 data are freely available and widely used for water body mapping, land cover classification, and vegetation monitoring. Chapter 3.

**Slope** (lejtesszog, meredekseg). The rate of change of elevation with respect to horizontal distance -- mathematically, the magnitude of the gradient of the elevation surface. Slope controls surface runoff velocity, erosion potential, infiltration opportunity time, and soil moisture distribution. It can be expressed as percent rise or degrees. Chapter 7.

**SoilGrids**. A global gridded soil property dataset at 250-metre resolution, providing estimates of soil texture, organic carbon, bulk density, pH, and other properties for multiple depth intervals. SoilGrids is the primary soil data source for regions without detailed national soil surveys. Chapter 3.

**Spatial interpolation** (terbeli interpolacio). The process of estimating values at unmeasured locations from known sample points to produce a continuous raster surface. Principal methods include nearest neighbour, inverse distance weighting, spline, and kriging, each embedding different assumptions about spatial continuity. Chapter 8.

**SRTM (Shuttle Radar Topography Mission)** (SRTM). A NASA/NGA mission that mapped Earth's surface between 60 N and 56 S in February 2000 using interferometric synthetic aperture radar. SRTM produced the first near-global DEM, freely available at 30-metre (1 arc-second) resolution. SRTM remains widely used for large-scale hydrological analysis. Chapter 3.

**Strahler stream order** (Strahler-rendszamu vizfolyasrendek). A hierarchical ordering system for stream networks in which the smallest headwater tributaries are order 1, the confluence of two order-1 streams produces an order-2 stream, and generally the confluence of two streams of order $n$ produces an order $n+1$ stream. Strahler order quantifies the relative size of streams within a network. Chapter 11.

**Stream burning** (vizfolyasbeegetes). A DEM reconditioning technique that lowers the elevation of cells along a mapped stream network, forcing the DEM-derived flow paths to follow known channel locations. Stream burning is a simpler alternative to the AGREE method. Chapter 9.

**Stream definition** (vizfolyasmeghatarozas). The process of classifying cells in a flow accumulation grid as stream or non-stream by applying a threshold. Cells whose accumulated upstream area exceeds the threshold are classified as channels. The threshold choice determines stream network density. Chapter 11.

**Stream segmentation** (vizfolyasszegmentalas). The process of dividing a continuous stream raster into individual reaches at junction points, producing discrete segments with unique identifiers. Each segment becomes the basis for a catchment in the watershed delineation. Chapter 11.

**Support area** (tamogato terulet). The minimum upstream drainage area required for a cell to be classified as a stream channel, also called the channelization threshold. The support area determines the density of the derived stream network and the partition between hillslope and channel processes. Chapter 11.

**SWAT (Soil and Water Assessment Tool)** (SWAT). The most widely used semi-distributed hydrological model globally, developed by the USDA Agricultural Research Service. SWAT divides watersheds into sub-basins containing hydrologic response units (HRUs) defined by unique combinations of land use, soil type, and slope class. Chapter 22.

**SZTFH (Szabalyozott Tevekenysegek Felugyeleti Hatosaga)** (Szabalyozott Tevekenysegek Felugyeleti Hatosaga). Hungary's Supervisory Authority for Regulatory Affairs, which absorbed the former Mining and Geological Survey (MBFSZ). SZTFH maintains the national geological map database, borehole records, and hydrogeological maps accessible through map.mbfsz.gov.hu. Chapter 19.

**TauDEM (Terrain Analysis Using Digital Elevation Models)** (TauDEM). An open-source suite of terrain analysis tools developed by David Tarboton, implementing D8, D-infinity, and generalized accumulation algorithms with parallel computing support. TauDEM is incorporated into ArcGIS and widely used for watershed delineation and HAND computation. Chapters 7, 10.

**Thiessen polygons** (Thiessen-poligonok). Also called Voronoi polygons or Dirichlet tessellations. A geometric partition of a plane in which each polygon contains all points closer to its associated sample point than to any other sample point. Used in hydrology for area-weighted averaging of precipitation from gauge networks. Chapter 8.

**TIN (Triangulated Irregular Network)** (TIN, szabalytalan haromszoghalo). A surface representation using irregularly spaced points connected into a mesh of non-overlapping triangles. TINs are storage-efficient for terrain representation because triangles can be concentrated in areas of high topographic complexity. However, they are less commonly used in hydrology than regular grids due to algorithmic complexity. Chapter 5.

**Topographic wetness index (TWI)** (topografiai vizboritas mutatoszam). A terrain attribute defined as $\ln(a / \tan \beta)$, where $a$ is the upslope contributing area per unit contour length and $\beta$ is the local slope angle. High TWI values indicate areas with large contributing areas and gentle slopes that are predicted to be saturated most frequently. TWI underpins the TOPMODEL family of hydrological models. Chapter 7.

**Transfer learning** (transzfer tanulas). A machine learning technique in which a model trained on one dataset or task is adapted for use on a different but related dataset or task. In hydrology, transfer learning enables LSTM models trained on data-rich catchments to make predictions at ungauged locations. Chapter 23.

**Upscaling problem** (felskalazas problema). The mismatch between point-scale measurable properties and grid-scale effective parameters required by models. For example, saturated hydraulic conductivity measured on a 10 cm soil core differs fundamentally from the effective value needed for a 1 km model grid cell. Chapter 22.

**Vector** (vektor). A spatial data model that represents geographic features as discrete geometric objects: points (wells, gauges), lines (streams, roads), and polygons (watersheds, aquifer boundaries). Vector features carry both geometry and attribute data. Chapter 4.

**Voronoi polygons** -- see **Thiessen polygons**.

**Water balance** (vizmerleg). The fundamental hydrological equation stating that precipitation equals the sum of evapotranspiration, runoff, and change in storage: $P = ET + R + \Delta S$. The water balance is applied at all scales from individual cells (via map algebra) to entire continents. Chapters 1, 6.

**Water Framework Directive (WFD)** (Viz Keretiranyelv). European Union directive (2000/60/EC) establishing a framework for the management and protection of European waters, including surface water, groundwater, estuaries, and coastal waters. The WFD established the goal of achieving "good ecological status" for all water bodies and requires member states to delineate and monitor groundwater bodies. Chapters 3, 19.

**Watershed** (vizgyujto terulet). The area of land from which all surface runoff drains to a common outlet point. Watershed delineation from DEMs is the most fundamental spatial operation in computational hydrology, performed by tracing flow directions upstream from a designated outlet. Also called a catchment or drainage basin. Chapter 11.

**Well** (kut). A human-made excavation or structure created in the ground to access groundwater for extraction, injection, or monitoring. Wells are represented as point features in GIS with attributes for depth, aquifer association, pumping rate, and water quality. Chapter 19.

**WGS84 (World Geodetic System 1984)** (Vilag Geodeziai Rendszer 1984). The global geocentric datum used by the GPS system, maintained by the US National Geospatial-Intelligence Agency. WGS84 is the de facto global standard for satellite-derived coordinate data and is nearly identical to ETRS89 for practical purposes. Chapter 2.

**WHYMAP** (World-wide Hydrogeological Mapping and Assessment Programme). A global initiative coordinated by Germany's BGR and UNESCO to produce consistent worldwide aquifer maps, including the Groundwater Resources Map of the World and the Transboundary Aquifer Map. Chapter 19.

**WorldPop**. A global gridded population dataset at approximately 100-metre resolution, produced by the University of Southampton. WorldPop estimates population distribution using machine learning applied to satellite imagery, settlement data, and census counts, providing high-resolution population data for countries with limited census infrastructure. Chapter 17.

**Zonal operation** (zonalis muvelet). A map algebra operation that computes a single summary value (mean, maximum, sum, etc.) for each group of cells sharing a common zone identifier. Computing the average elevation within each watershed polygon is a classic zonal operation. Chapter 6.

---

**Bloschl's scale triplet** (Bloschl-fele skala harem). A conceptual framework for characterizing spatial data and processes using three dimensions: extent (the total area covered), spacing (the distance between observations or grid cells), and support (the area or volume over which each measurement integrates). The scale triplet is essential for evaluating whether a dataset is appropriate for a given analytical purpose. Chapter 5.

**Cell3D**. (AHGW) A multipatch feature class in the Arc Hydro Groundwater data model representing three-dimensional cells and elements of a simulation model grid. Cell3D features store the full volumetric geometry of each model cell. Chapter 21.

**Clausius-Clapeyron relation** (Clausius-Clapeyron osszefugges). The thermodynamic relationship stating that the saturation vapour pressure of water increases by approximately seven percent for every degree Celsius of warming. This relationship explains why a warmer atmosphere produces more intense precipitation events and exacerbates both flooding and drought. Chapter 1.

**CUAHSI** (Consortium of Universities for the Advancement of Hydrologic Science, Inc.). A US-based consortium of universities that develops and operates shared infrastructure for hydrologic research, including the Hydrologic Information System (HIS) and HydroShare. Chapter 1.

**Darcy's law** (Darcy-torveny). The fundamental equation of groundwater flow, relating the volumetric flow rate through a porous medium to the hydraulic gradient and hydraulic conductivity: $Q = -KA(dh/dl)$, where $K$ is hydraulic conductivity, $A$ is cross-sectional area, and $dh/dl$ is the hydraulic gradient. Chapter 21.

**Destination Earth (DestinE)** (Celfold). A European Commission initiative launched in 2024 to build a high-resolution digital replica of the entire Earth system on European supercomputing infrastructure, with full operational capability planned for 2030. DestinE includes digital twins of the water cycle at unprecedented resolution. Chapter 25.

**Dropout** (dropout). A regularization technique in neural network training in which randomly selected neurons are temporarily removed during each training step, forcing the network to learn redundant representations and reducing overfitting. Dropout rates of 0.1--0.3 are typical for LSTM models in hydrology. Chapter 23.

**ECMWF (European Centre for Medium-Range Weather Forecasts)** (Kozepavu Idojaras-elorejelzes Europai Kozpontja). An intergovernmental organization operating some of the world's most advanced weather prediction systems. ECMWF produces the ERA5 reanalysis, operates the EFAS flood forecasting system, and develops the ECLand land surface model. Chapters 3, 16, 25.

**EGM2008** (Earth Gravitational Model 2008). A global geoid model providing the geoid height (separation between geoid and reference ellipsoid) on a grid with approximately 5 km resolution. EGM2008 serves as the vertical datum for the Copernicus DEM and many other global elevation products. Chapter 2.

**Encoder-decoder architecture** (kodolo-dekodolo architektura). A neural network design in which one network (encoder) compresses an input sequence into a fixed-length representation, and a second network (decoder) generates an output sequence from that representation. Used in LSTM flood forecasting for multi-step predictions. Chapter 23.

**Ensemble forecast** (ensemble elorejelzes). A forecasting approach that runs multiple simulations with slightly different initial conditions, model parameters, or forcing data to quantify prediction uncertainty. EFAS produces ensemble flood forecasts; the EnKF uses ensembles for data assimilation. Chapters 16, 25.

**Floodplain** (artter). The relatively flat area adjacent to a river channel that is periodically inundated during high-flow events. Floodplain extent is closely correlated with HAND values; cells with low HAND values lie within the floodplain. Chapter 14.

**Full waveform LiDAR** (teljes hullamforma LiDAR). A LiDAR technology that records the complete time history of the return signal rather than just discrete peaks. Full waveform data contains information about the vertical distribution of reflecting surfaces, improving ground detection under dense vegetation. Chapter 13.

**Geiger-mode LiDAR** (Geiger-modu LiDAR). An advanced LiDAR technology using single-photon-sensitive detectors that can register individual photons returning from the target. Geiger-mode systems achieve much higher point densities and wider swath widths than conventional linear-mode systems from the same altitude, enabling faster and more cost-effective national mapping programmes. Chapter 13.

**GeoPackage** (GeoPackage). An open, standards-based, platform-independent geodata format defined by the Open Geospatial Consortium. GeoPackage uses SQLite as its container and serves as the native spatial data format for QGIS. Chapter 4.

**Global operation** (globalis muvelet). A map algebra operation in which each output cell is computed using information from every cell in the input grid. Distance calculations and cost-surface analyses are examples of global operations. Chapter 6.

**Helmert transformation** -- see entry above.

**Hydraulic conductivity** (hidraulikus vezeto kepesseg). A measure of a porous medium's ability to transmit water under a hydraulic gradient, with units of length per time (m/s or m/day). Hydraulic conductivity depends on both the properties of the medium (grain size, porosity, connectivity) and the fluid (viscosity, density). It is one of the most important parameters in groundwater modelling. Chapter 21.

**Hydrologic Response Unit (HRU)** (hidrologiai valasz egyseg). A spatial unit in semi-distributed hydrological models (particularly SWAT) defined by a unique combination of land use, soil type, and slope class. HRUs are the basic computational elements to which process equations are applied. Chapter 22.

**HYDROINFO** (HYDROINFO). Hungary's real-time water level monitoring system operated by OVF, accessible at hydroinfo.hu. HYDROINFO displays water levels, discharge data, and forecasts for 98 river sections, serving as the primary public-facing flood information portal for Hungary. Chapter 16.

**IMU (Inertial Measurement Unit)** (inerciamero egyseghaz). A device containing accelerometers and gyroscopes that tracks the orientation and short-term position changes of an airborne LiDAR system at 200 Hz or more. The IMU, integrated with GPS via a Kalman filter, enables precise geolocation of each laser pulse. Chapter 13.

**JRC (Joint Research Centre)** (Kozos Kutatokozpont). The European Commission's science and knowledge service, based in Ispra, Italy. The JRC developed EFAS, produces the European Drought Observatory, and created the JRC Global Surface Water dataset mapping surface water dynamics from 1984 to the present. Chapters 1, 14.

**LandScan** (LandScan). A global population distribution dataset at approximately 1 km resolution, produced by Oak Ridge National Laboratory. LandScan estimates ambient (24-hour average) population distribution and is used for exposure assessment in global flood risk studies. Chapter 17.

**LISFLOOD** (LISFLOOD). The distributed hydrological model used by the European Flood Awareness System (EFAS), developed by the JRC. LISFLOOD simulates rainfall-runoff processes and channel routing across the European continent at 5 km resolution. Chapter 16.

**Lookback window** (visszatekintesi ablak). In LSTM and other recurrent neural network models, the number of preceding time steps provided as input to the model at each prediction step. For flood forecasting, typical lookback windows of 30--60 days capture both fast surface response and slow baseflow dynamics. Chapter 23.

**MERIT DEM** (Multi-Error-Removed Improved-Terrain DEM). A global elevation dataset at 3 arc-second (approximately 90 m) resolution, created by removing multiple error components (stripe noise, speckle, absolute bias, tree canopy height) from SRTM and AW3D data. MERIT provides improved hydrological analysis compared to raw SRTM. Chapter 3.

**MODFLOW Analyst**. A suite of ArcGIS tools developed as part of the Arc Hydro Groundwater tools, used for building and managing MODFLOW models through the Arc Hydro Groundwater and MODFLOW data models. Chapter 21.

**Node2D and Node3D**. (AHGW) Point feature classes in the Arc Hydro Groundwater data model representing computational nodes in 2D and 3D simulation model grids. Node3D features are Z-enabled. Chapter 21.

**Orographic precipitation** (orografikus csapadek). Rainfall caused by air masses being forced upward by terrain, producing enhanced precipitation on windward slopes and reduced precipitation (rain shadow) on leeward slopes. Orographic effects create systematic spatial patterns that simple distance-based interpolation methods cannot capture. Chapter 8.

**Pannonian Basin** (Pannon-medence). The large sedimentary basin encompassing most of Hungary and portions of neighbouring countries, filled with several kilometres of Neogene and Quaternary sediments. The Pannonian Basin contains multiple stacked aquifer systems, including shallow alluvial aquifers and deep thermal water-bearing formations that feed Hungary's famous thermal baths. Chapters 18--19.

**PBIAS (Percent Bias)** (szazalekos torzitas). A model performance metric that measures the average tendency of simulated values to be larger or smaller than observed values, expressed as a percentage. PBIAS = 0% indicates no systematic bias. PBIAS is sensitive to volume errors but insensitive to timing errors. Chapter 22.

**Sensitivity analysis** (erzekenysegelemzes). The systematic investigation of how model outputs change in response to changes in model parameters. Sensitivity analysis identifies which parameters have the greatest influence on model performance and guides the allocation of calibration effort. Chapter 22.

**Shapefile** (shapefile). A widely used vector data format developed by Esri, consisting of at least three files (.shp, .shx, .dbf) that together store geometry and attributes. Despite its limitations (2 GB file size limit, 10-character field names, no built-in coordinate system enforcement), the shapefile remains the most common data exchange format in GIS. Chapter 4.

**Spline interpolation** (spline interpolacio). A spatial interpolation method that fits a smooth mathematical surface through sample points by minimizing overall surface curvature. Spline interpolation produces smooth surfaces suitable for gently varying phenomena but can produce unrealistic oscillations (overshoot) near extreme values. Chapter 8.

**Subsurface Analyst**. A suite of ArcGIS tools developed as part of the Arc Hydro Groundwater tools for creating, editing, and managing 2D and 3D hydrogeologic data within ArcGIS, including borehole visualization, cross-section creation, and surface interpolation. Chapter 18.

**TimeSeries table**. (AHGW) A table in the Arc Hydro data model for storing single-variable time-series data, implementing a three-dimensional structure indexed by location (feature), time (TsTime), and variable (VarID). Chapter 19.

**Transmissivity** (transzmisszivitas). A measure of the ability of a full thickness of aquifer to transmit water, equal to the product of hydraulic conductivity and aquifer thickness ($T = Kb$), with units of area per time (m2/day). Transmissivity is the parameter directly estimated from pumping tests. Chapter 21.

**Universal Soil Loss Equation (USLE)** (Egyetemes Talajvesztesi Egyenlet). An empirical equation estimating long-term average soil erosion as a product of rainfall erosivity, soil erodibility, slope-length factor, cover-management factor, and conservation practice factor. The USLE's slope-length factor makes soil loss increase approximately as the square of slope steepness. Chapter 7.

**Variogram** (variogram). A function describing how the spatial correlation of a variable changes with distance, used in kriging interpolation. The variogram quantifies the principle that nearby values tend to be more similar than distant values, and its parameters (nugget, sill, range) control the interpolation behavior. Chapter 8.

**Water quality** (vizminoseg). The physical, chemical, and biological characteristics of water that determine its suitability for specific uses. Water quality concerns include nutrient pollution, contamination, salinity, temperature, and dissolved oxygen. The EU Water Framework Directive mandates "good ecological status" for all water bodies. Chapter 1.

*This glossary contains 225 entries spanning the six major domains covered by the book: GIS fundamentals, geodesy, surface hydrology, groundwater, AI/machine learning, and data systems. Terms are cross-referenced where appropriate. For definitions of additional Arc Hydro Groundwater data model elements, see the glossary in Strassberg, Jones, and Maidment (2011), Arc Hydro Groundwater: GIS for Hydrogeology.*
