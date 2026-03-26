# Appendix B: Exercises

This appendix provides exercises for each chapter of *The State of Hidroinformatics in 2026*. Exercises are drawn from and adapted from the original course materials developed by David R. Maidment and David G. Tarboton at the University of Texas at Austin and Utah State University, supplemented with new problems reflecting the international scope of this book and developments through 2026.

Each exercise is tagged with a difficulty level:

- **Basic** -- Recall and comprehension; suitable for all readers.
- **Intermediate** -- Application and analysis; requires GIS software or moderate calculation.
- **Advanced** -- Synthesis and evaluation; open-ended or research-oriented problems.

Where calculation problems are given, expected answers appear in *italics* at the end of the exercise.

---

## Part I: Foundations (Chapters 1--4)

### Chapter 1 Exercises: Why Hidroinformatics Matters

1. **(Basic)** Define hidroinformatics in your own words. How does it differ from traditional hydrology, and how does it differ from plain GIS analysis? Provide at least three specific examples of problems that require both hydrological knowledge and geospatial information technology.

2. **(Basic)** The original Maidment course at UT Austin was called "GIS in Water Resources." Explain why this book uses the term "hidroinformatics" instead. What additional dimensions does the newer term capture that the older title did not?

3. **(Intermediate)** Choose a river basin you are familiar with (the Danube, Tisza, Nile, Mekong, Colorado, or any other). List the key data sources that a hidroinformatics study of that basin would require: topographic data, hydrographic networks, land cover, precipitation, streamflow observations, and forecasting services. For each data type, identify whether a national or global dataset exists and name it. Compare your list to the datasets available for the United States (NHDPlus, NED, NLCD, USGS NWIS, National Water Model).

4. **(Intermediate)** The text describes how Hurricane Harvey (2017) demonstrated the need for real-time flood prediction coupled with geospatial data. Research a comparable flood disaster outside the US (e.g., the 2013 Danube floods in Central Europe, the 2021 Ahr Valley flood in Germany, or the 2010 Pakistan floods). Write a one-page summary describing: (a) what geospatial data was available before the event, (b) what forecasting systems were operational, and (c) what improvements have been implemented since.

5. **(Advanced)** The chapter argues that hidroinformatics is converging with artificial intelligence. Identify three specific tasks in water resources management where AI has already been deployed (as of 2026) and three tasks where human expert judgment remains essential. Justify your classification for each task.

---

### Chapter 2 Exercises: Mapping Water -- From Paper to Pixels

1. **(Basic)** Explain the difference between a geographic coordinate system and a projected coordinate system. Why is the distinction important for hydrological applications? Give an example of a situation where using geographic coordinates for area calculation would produce a significant error.

2. **(Basic)** A point is located at latitude 47.4979 N, longitude 19.0402 E (Budapest, Hungary). Convert these decimal degree coordinates to degrees-minutes-seconds format. *Expected answer: 47 degrees 29 minutes 52.4 seconds N, 19 degrees 2 minutes 24.7 seconds E.*

3. **(Intermediate)** Calculate the ground distance represented by a 1-arc-second grid cell at the latitude of Budapest (47.5 N). Assume a spherical Earth with radius R = 6370 km. Report the north-south length, east-west length, and cell area.

   *Expected answers: N-S length = 6370 x (1/3600) x (pi/180) = 30.87 m. E-W length = 6370 x (1/3600) x (pi/180) x cos(47.5) = 20.85 m. Area = 30.87 x 20.85 = 643.6 m^2.*

4. **(Intermediate)** The Hungarian Unified National Projection (EOV) uses a Transverse Mercator projection with the following parameters: latitude of origin 47 degrees 8 minutes 39.8174 seconds N; central meridian 19 degrees 2 minutes 54.8584 seconds E; false easting 650,000 m; false northing 200,000 m. A point has EOV coordinates Y = 238,400 m (northing) and X = 649,500 m (easting). Explain what the false easting and false northing accomplish, and estimate the approximate geographic coordinates of this point. *Hint: the point is very close to the projection origin, so it lies near Budapest.*

5. **(Advanced)** You receive a CSV file with coordinate columns labeled "X" and "Y." The values in the X column range from 450,000 to 900,000 and in the Y column from 50,000 to 350,000. Based on the value ranges described in this book's guidelines for EOV coordinates, which column is easting and which is northing? Explain the logic. Why can header labels not be trusted for EOV data, and what rule of thumb should you always apply?

   *Expected answer: Easting values in EOV range from ~400,000 to ~1,000,000, so the X column (450k--900k) contains eastings. Northing values range from ~0 to ~400,000, so the Y column (50k--350k) contains northings. Headers are often swapped or mislabeled in legacy Hungarian datasets; always identify by value range.*

---

### Chapter 3 Exercises: Where the Data Lives

1. **(Basic)** Name the four primary US national datasets that compose NHDPlus (National Elevation Dataset, National Hydrography Dataset, National Land Cover Dataset, Watershed Boundary Dataset). For each, describe what type of geospatial data it provides (raster or vector, and what features it represents).

2. **(Basic)** The Watershed Boundary Dataset uses a hierarchical coding system (HUC). A subwatershed has HUC-12 code 121002030101. Parse this code into its hierarchical components: Region, Subregion, Basin, Subbasin, Watershed, Subwatershed, and give the numeric value for each level. *Expected answer: Region 12, Subregion 10, Basin 02, Subbasin 03, Watershed 01, Subwatershed 01.*

3. **(Intermediate)** NHDPlus Version 2.1 contains approximately 2.7 million reach-catchments in the US, with an average catchment area of about 3 km^2 and an average reach length of about 2 km. Calculate the drainage density implied by these averages. Compare this to a typical drainage density you would expect for a humid temperate region.

   *Expected answer: Drainage density = reach length / catchment area = 2 km / 3 km^2 = 0.67 km^-1. Typical humid region drainage density ranges from 0.5 to 3.0 km^-1, so NHDPlus captures the medium-resolution stream network.*

4. **(Intermediate)** The EU Water Framework Directive requires member states to report on the ecological status of water bodies. Investigate and describe the European equivalent datasets to NHDPlus: the EU-Hydro river network and the ECRINS (European Catchments and Rivers Network System). Compare their spatial resolution and attribute completeness with NHDPlus. What are the key gaps?

5. **(Advanced)** You need to build a base dataset for the Tisza River basin (which spans five countries: Ukraine, Romania, Slovakia, Hungary, Serbia). Identify the global and European datasets you would need for: (a) river network and catchment boundaries, (b) elevation data, (c) land cover, (d) streamflow observations. Discuss the challenges of data harmonization across national boundaries and how transboundary hidroinformatics projects address these challenges.

---

### Chapter 4 Exercises: GIS as a Water Tool

*Adapted from Maidment Exercise 1 (Introduction to ArcGIS) and Exercise 2 (Building a Watershed Base Map).*

1. **(Basic)** Explain the difference between a shapefile, a geodatabase feature class, and a feature dataset. When would you use each? What are the advantages of organizing multiple feature classes within a single feature dataset?

2. **(Basic)** In a GIS geodatabase, what is the difference between the "Remove" and "Delete" operations on a layer? Why is this distinction critical for data management in a multi-user project?

3. **(Intermediate)** Using any GIS platform (ArcGIS Pro, QGIS, or a cloud-based GIS), build a base map of a watershed of your choice. Your map should include: (a) watershed boundary polygon, (b) stream network with line widths proportional to mean annual flow or stream order, (c) at least three labeled stream gage locations created from a table of coordinates, (d) a properly formatted layout with title, scale bar, north arrow, and legend. Document your workflow with screenshots or a written procedure.

   *Hungarian parallel: Build a base map of the Zagyva catchment in Hungary using data from vizugy.hu and the EU-Hydro dataset. Include the catchment boundary, main channel and tributaries, and at least two gauging stations. Compare the catchment boundary from EU-Hydro with the one from the Hungarian Water Directorate (VIZITERV).*

4. **(Intermediate)** The San Marcos Basin (HUC-8 = 12100203) in Texas contains 32 HUC-12 subwatersheds grouped into 5 HUC-10 watersheds. Using the NLCD land cover data, the basin's land cover was classified and summarized. Suppose you extracted the land cover for a basin and obtained the following cell counts (30 m cells): Forest = 142,000 cells; Developed = 38,000 cells; Agriculture = 95,000 cells; Shrubland = 67,000 cells; Water/Wetland = 8,000 cells. Calculate the area in km^2 and percentage for each class.

   *Expected answers: Each cell = 30 x 30 = 900 m^2 = 0.0009 km^2. Forest: 142,000 x 0.0009 = 127.8 km^2 (40.6%); Developed: 38,000 x 0.0009 = 34.2 km^2 (10.9%); Agriculture: 95,000 x 0.0009 = 85.5 km^2 (27.1%); Shrubland: 67,000 x 0.0009 = 60.3 km^2 (19.1%); Water/Wetland: 8,000 x 0.0009 = 7.2 km^2 (2.3%). Total: 315.0 km^2.*

5. **(Advanced)** The National Water Model provides streamflow forecasts for every NHDPlus reach. A forecast for the Blanco River near Wimberley (COMID 1630223) shows 85 m^3/s, while the most downstream segment of the San Marcos Basin (COMID 1632017) shows 210 m^3/s. The drainage areas are 920 km^2 and 2170 km^2, respectively. Calculate the ratio of forecast flows and the ratio of drainage areas. Discuss whether the relationship between flow and drainage area is linear and what factors could cause deviations.

   *Expected answers: Flow ratio = 210/85 = 2.47. Area ratio = 2170/920 = 2.36. The ratios are similar, suggesting an approximately linear scaling, but factors such as spatial rainfall variability, land cover differences, karst geology (significant in the San Marcos area), and baseflow contributions from the Edwards Aquifer can cause deviations from linearity.*

---

## Part II: Terrain and Spatial Analysis (Chapters 5--8)

### Chapter 5 Exercises: The Grid -- How Computers See Terrain

1. **(Basic)** Explain the difference between an integer raster grid and a floating-point raster grid. Give an example of hydrological data that would be stored in each type.

2. **(Basic)** A DEM has a cell size of 9.259 x 10^-5 degrees. At a latitude of 42 degrees N, calculate the cell size in meters in both the N-S and E-W directions. Assume a spherical Earth with radius 6370 km.

   *Expected answers: N-S: 6370 x 9.259e-5 x (pi/180) = 10.29 m. E-W: 6370 x 9.259e-5 x (pi/180) x cos(42) = 7.65 m. Cell area = 10.29 x 7.65 = 78.7 m^2.*

3. **(Intermediate)** A merged DEM covering the Logan River basin (Utah) has 9,498 columns and 10,798 rows of 10 m cells. The minimum elevation is 1,380 m and the maximum is 2,960 m. Calculate the total area covered by this DEM in km^2. Estimate the relief ratio (max elevation minus min elevation divided by the square root of the area).

   *Expected answer: Area = 9498 x 10798 x 100 m^2 = 10,255 km^2 (approximately, as the DEM extends beyond the basin). Relief = 2960 - 1380 = 1580 m. Relief ratio = 1580 / sqrt(10255) = 15.6 m/km^0.5.*

4. **(Intermediate)** You download two 1-degree DEM tiles from a national mapping service. The tiles are named n42w112 (covering 41-42 N, 111-112 W) and n43w112 (covering 42-43 N, 111-112 W). Using the Mosaic to New Raster tool, you merge them into a single raster. What parameters must you specify for pixel type and number of bands? Why?

   *Expected answer: Pixel type = 32-bit float (elevation values are continuous real numbers). Number of bands = 1 (single elevation value per cell). These must match the source DEM properties.*

5. **(Advanced)** Compare the SRTM 30 m global DEM, the Copernicus DEM (GLO-30), and the ALOS World 3D DEM for a mountain watershed of your choice. Discuss differences in vertical accuracy, horizontal resolution, data vintage, and coverage. Which would you recommend for a hidroinformatics study in (a) the Hungarian Great Plain, (b) the Carpathian Mountains, (c) sub-Saharan Africa?

---

### Chapter 6 Exercises: Calculating with Maps

1. **(Basic)** Explain the concept of "map algebra" as applied to raster data. Give three examples of raster calculator operations relevant to hydrology.

2. **(Basic)** When performing raster arithmetic on two grids with different cell sizes and extents, what three settings must be specified to ensure consistent results? Explain what "analysis extent," "cell size," and "snap raster" accomplish.

3. **(Intermediate)** A raster grid named `precip` contains mean annual precipitation in mm for a watershed, and a raster grid named `et` contains mean annual evapotranspiration in mm. Write the raster calculator expression to compute the mean annual runoff depth. If the watershed has an area of 450 km^2, the spatial mean of `precip` is 820 mm, and the spatial mean of `et` is 610 mm, calculate the mean annual runoff volume in cubic meters and in million cubic meters.

   *Expected answer: Runoff = precip - et. Mean runoff depth = 820 - 610 = 210 mm. Volume = 0.210 m x 450 x 10^6 m^2 = 94.5 x 10^6 m^3 = 94.5 million m^3.*

4. **(Intermediate)** The Extract by Mask tool is used to clip a raster dataset to a polygon boundary. You extract a land cover raster (30 m cells) to a basin boundary and obtain an integer grid. The attribute table shows: Value 41 (Deciduous Forest), Count = 52,300; Value 42 (Evergreen Forest), Count = 31,200; Value 81 (Pasture), Count = 44,100; Value 82 (Cropland), Count = 18,500; Value 21 (Developed Open Space), Count = 12,400. Calculate the total basin area and the percentage in each class.

   *Expected answer: Total cells = 158,500. Area per cell = 900 m^2. Total area = 142.65 km^2. Deciduous Forest = 33.0%; Evergreen Forest = 19.7%; Pasture = 27.8%; Cropland = 11.7%; Developed = 7.8%.*

5. **(Advanced)** Design a raster-based workflow (using map algebra and geoprocessing tools) to compute a simple soil moisture index for a watershed. Your inputs are: a precipitation raster, a potential ET raster, a soil available water capacity raster, and a land cover raster. Describe each step, the raster calculator expressions, and what assumptions you make. Discuss the limitations of a steady-state raster approach compared to a time-stepping model.

---

### Chapter 7 Exercises: Slope, Aspect, and the Shape of the Land

*Adapted from Maidment Exercise 3 (Spatial Analysis), Part 1.*

1. **(Basic)** Define slope and aspect as computed from a DEM. What are the units of slope when expressed as percent rise versus degrees? Convert a slope of 45% to degrees. *Expected answer: arctan(0.45) = 24.2 degrees.*

2. **(Intermediate)** Given the following 3x3 grid of elevations (cell size = 10 m), calculate the slope at the center cell using the ArcGIS "surface slope" method (the 3rd-order finite difference method):

   ```
   25.1  25.8  26.8
   25.0  26.0  26.4
   25.4  26.1  27.0
   ```

   The method computes dz/dx = ((c - a) + 2(f - d) + (i - g)) / (8 x cellsize) and dz/dy = ((g - a) + 2(h - b) + (i - c)) / (8 x cellsize), where the 3x3 window is labeled a through i left-to-right, top-to-bottom.

   *Expected answer: Using the labeling convention where a=25.1, b=25.8, c=26.8, d=25.0, e=26.0, f=26.4, g=25.4, h=26.1, i=27.0: dz/dx = ((26.8-25.1) + 2(26.4-25.0) + (27.0-25.4))/(8 x 10) = (1.7 + 2.8 + 1.6)/80 = 6.1/80 = 0.07625. dz/dy = ((25.4-25.1) + 2(26.1-25.8) + (27.0-26.8))/(8 x 10) = (0.3 + 0.6 + 0.2)/80 = 1.1/80 = 0.01375. Slope = sqrt(0.07625^2 + 0.01375^2) = sqrt(0.005814 + 0.000189) = sqrt(0.006003) = 0.0775 = 7.75%.*

3. **(Intermediate)** Using the same grid, calculate the D8 flow direction at the center cell. Express your answer both as the coded direction value (1, 2, 4, 8, 16, 32, 64, 128) and as a compass direction. Also calculate the hydrologic slope (steepest descent to one of the 8 neighbors).

   *Hint: compare drops to each of the 8 neighbors, dividing diagonal drops by sqrt(2) x cellsize and cardinal drops by cellsize.*

4. **(Intermediate)** Explain the difference between the D8 flow direction algorithm and the D-infinity (DINF) algorithm. Why is D8 preferred for stream network delineation, while DINF is preferred for calculating overland flow paths (such as HAND)?

5. **(Advanced)** Build a ModelBuilder workflow (or equivalent Python/QGIS graphical model) that takes an ASCII grid file as input and produces six outputs: the imported raster, slope (percent rise), aspect, D8 flow direction, D8 percentage drop, and DINF flow direction. Run it on two different DEMs and compare the results. Document your model with a screenshot or diagram. *(Adapted from Ex3, Part 1.3.)*

---

### Chapter 8 Exercises: Measuring Rain Where It Falls

*Adapted from Maidment Exercise 3 (Spatial Analysis), Part 2.*

1. **(Basic)** Explain the Thiessen polygon method for estimating areal average precipitation from point measurements. Under what conditions does it work well, and when does it fail?

2. **(Intermediate)** Five rain gauges surround a small watershed. Their Thiessen polygon areas within the watershed and measured annual precipitation are:

   | Station | Thiessen Area (km^2) | Annual Precip (mm) |
   |---------|---------------------|--------------------|
   | A       | 12.3                | 780                |
   | B       | 8.7                 | 920                |
   | C       | 15.1                | 850                |
   | D       | 6.4                 | 1,020              |
   | E       | 9.5                 | 690                |

   Calculate the Thiessen-weighted mean annual precipitation for the watershed.

   *Expected answer: Total area = 52.0 km^2. Weighted sum = (12.3 x 780 + 8.7 x 920 + 15.1 x 850 + 6.4 x 1020 + 9.5 x 690) = 9,594 + 8,004 + 12,835 + 6,528 + 6,555 = 43,516. Mean = 43,516 / 52.0 = 836.8 mm.*

3. **(Intermediate)** The same watershed is divided into three HUC-12 subwatersheds. Using the GIS "Intersect" tool, you overlay the Thiessen polygons on the subwatershed boundaries. Describe step by step how you would use the intersected feature class to compute the mean annual precipitation for each subwatershed individually.

4. **(Intermediate)** Compare three spatial interpolation methods for precipitation: Thiessen polygons, Inverse Distance Weighting (IDW), and ordinary kriging. For each, describe the underlying assumption, one advantage, and one limitation. Which is most appropriate when the rain gauge network is sparse?

5. **(Advanced)** You have mean annual precipitation at 15 stations in and around a mountain watershed. Elevation strongly influences precipitation in this region. Design a workflow to create a precipitation surface using: (a) simple IDW interpolation, (b) a regression of precipitation on elevation followed by residual interpolation (sometimes called "detrended kriging" or "regression-kriging"). Compute the mean precipitation over three subwatersheds using each method and discuss the differences.

   *Hungarian parallel: Use precipitation station data from the Balaton catchment (available from the Hungarian Meteorological Service, OMSZ) and the EU-DEM to perform this analysis. Discuss whether elevation is a strong predictor of precipitation in this relatively flat region.*

---

## Part III: Watershed Delineation and Hydrologic Terrain Analysis (Chapters 9--11)

### Chapter 9 Exercises: Preparing the Digital Landscape

*Adapted from Maidment Exercise 4 (Watershed and Stream Network Delineation), initial steps.*

1. **(Basic)** Explain what "pit filling" does to a DEM and why it is necessary for hydrologic analysis. Give one example of a pit that represents a real topographic feature and one that is an artifact.

   *Example: Peter Sink in the Logan River basin (Utah) is a real topographic depression. An isolated low cell caused by DEM interpolation error is an artifact.*

2. **(Basic)** What is the purpose of creating a buffer around a watershed boundary before extracting a DEM? What problems could arise if you do not buffer?

3. **(Intermediate)** A DEM is provided in geographic coordinates (decimal degrees). You need to project it to a UTM coordinate system (meters). List the sequence of GIS operations required to: (a) extract the DEM to your study area, (b) project it to UTM, and (c) verify the result. What information do you need to select the correct UTM zone?

   *Expected answer: Determine the central longitude of the study area and select the UTM zone accordingly (zone = floor((longitude + 180)/6) + 1). Use Extract by Mask to clip to a buffered boundary. Use Project Raster to reproject. Verify by checking the coordinate system properties, cell size in meters, and spatial alignment with vector data.*

4. **(Intermediate)** After filling a DEM, you compute the difference (filled DEM minus original DEM) and find that the maximum fill depth is 22 m. Using contour lines at 20 m intervals, you identify this location. Describe how you would determine whether this deep sink is a real feature or an artifact, and what the consequences would be for hydrologic analysis if you fill a real depression.

5. **(Advanced)** The USGS delivered DEM tiles for a watershed in 1-degree blocks. You need to merge, extract, and project these tiles for terrain analysis. Design a complete workflow from raw DEM tiles to a hydrologically conditioned DEM ready for flow direction computation. Include: mosaic, buffer, extract by mask, project raster, and fill. Write this as pseudocode or a ModelBuilder diagram.

---

### Chapter 10 Exercises: Which Way Does Water Flow?

*Adapted from Maidment Exercise 4, Steps 2--3.*

1. **(Basic)** Draw a 3x3 grid and label the D8 flow direction codes for all eight directions. Given the following 3x3 DEM with 10 m cell size, determine the D8 flow direction and hydrologic slope at the center cell:

   ```
   180  175  170
   185  190  172
   188  182  178
   ```

   *Expected answer: The center cell (190) is higher than all neighbors. Steepest drop is to the NE cell (170): drop = 20 m over diagonal distance = 14.14 m. Slope = 20/14.14 = 1.414 (141.4%). D8 code for NE = 2 (using ESRI convention: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128). Note: verify against the convention used in your GIS; ArcGIS uses: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128.*

2. **(Basic)** Explain the concept of a flow accumulation grid. If a cell has a flow accumulation value of 5,000 and the cell size is 10 m, what is the drainage area upstream of that cell in km^2? *Expected answer: 5000 x (10 x 10) m^2 = 500,000 m^2 = 0.5 km^2.*

3. **(Intermediate)** A flow accumulation grid for the Logan River basin has a value of 55,386,000 at the outlet cell. The cell size is 10 m. Calculate the drainage area in km^2. The USGS reports the drainage area as 554 km^2 (214 sq mi). Compare and discuss reasons for any difference.

   *Expected answer: 55,386,000 x 100 m^2 = 5,538.6 km^2. Wait -- this seems too large. Recheck: 55,386,000 x 100 = 5.539 x 10^9 m^2 = 5,539 km^2. This is much larger than 554 km^2, so the flow accumulation value should be approximately 5,540,000 for 554 km^2. The exercise teaches students to verify their calculations against known values. If flow accumulation = 5,540,000, then area = 5,540,000 x 100 = 554 x 10^6 m^2 = 554 km^2. Differences arise from DEM resolution, pit filling extending the basin boundary, and definition of the outlet location.*

4. **(Intermediate)** Explain how to define a stream network from a flow accumulation grid using a threshold. If you use a threshold of 1000 cells (cell size = 10 m), what minimum contributing area defines a stream headwater? What happens to stream density as you decrease the threshold? What happens as you increase it?

   *Expected answer: Minimum contributing area = 1000 x 100 = 100,000 m^2 = 0.1 km^2. Decreasing the threshold creates more stream headwaters and a denser network. Increasing it creates fewer, larger streams.*

5. **(Advanced)** A watershed has a total channel length (from all streams delineated at a given threshold) of 320 km and a total basin area of 480 km^2. Calculate the drainage density. Using the relationship that average overland flow distance = 1/(2 x Dd), calculate the average distance water must travel over the hillslope before reaching a stream. Discuss what this means for the basin's hydrologic response.

   *Expected answer: Dd = 320/480 = 0.667 km^-1. Average overland flow distance = 1/(2 x 0.667) = 0.75 km = 750 m. This means that on average, rain falling on the hillslope travels 750 m before reaching a channel, which influences the time of concentration and peak flow timing.*

---

### Chapter 11 Exercises: Drawing Watersheds from Data

*Adapted from Maidment Exercise 4, Steps 4--8, and comparison with NHDPlus.*

1. **(Basic)** Describe the relationship between a stream link grid, a drainageline feature class, a catchment grid, and a catchment polygon feature class. What is the unique identifier that links these four data products together?

   *Expected answer: The stream link grid assigns a unique integer to each stream segment between junctions. The drainageline is the vector version of the stream links. The catchment grid assigns each grid cell the same value as the stream link it drains to. The catchment polygon is the vector version of the catchment grid. The stream link value (grid code) is the common identifier that relationally associates all four.*

2. **(Intermediate)** After delineating a watershed from a 10 m DEM, you compare the boundary with the one produced by an online watershed delineation service. You find a discrepancy at the northern edge of the basin amounting to approximately 3 km of boundary offset over a length of 8 km. Estimate the area of this discrepancy (using a simple trapezoidal approximation) and discuss the causes.

   *Expected answer: Approximate area = average offset x length = 1.5 km x 8 km = 12 km^2 (rough estimate, depends on shape). Causes include: different DEMs used (resolution, vintage), different pit-filling algorithms, different snap distances for outlet points, and the inherent ambiguity of watershed boundaries in flat terrain.*

3. **(Intermediate)** You delineate streams from a DEM and also have NHDPlus flowlines for the same basin. The DEM-derived network has 185 stream segments; the NHDPlus network has 210 flowlines within the same area. Explain why these numbers differ. What does this tell you about the segmentation rules used by each method?

4. **(Intermediate)** Using NHDPlus data for the Logan River basin: the total NHDPlus stream length is 340 km, the main stem (Logan River) length is 65 km, and the basin area is 554 km^2. Calculate: (a) drainage density, (b) the ratio of main stem length to total stream length, and (c) the average overland flow distance.

   *Expected answers: (a) Dd = 340/554 = 0.614 km^-1. (b) Ratio = 65/340 = 19.1%. (c) Average overland flow distance = 1/(2 x 0.614) = 0.814 km = 814 m.*

5. **(Advanced)** Perform a complete terrain analysis workflow for a watershed of your choice: DEM acquisition, mosaic (if needed), extraction, projection, fill, flow direction, flow accumulation, stream definition, stream links, catchment delineation, and vector conversion. Compare your DEM-derived stream network to a published hydrography dataset (NHDPlus, EU-Hydro, or national equivalent). Prepare a layout showing both networks and discuss the differences.

---

## Part IV: Automation and Advanced Sensing (Chapters 12--13)

### Chapter 12 Exercises: Automating the Workflow

1. **(Basic)** Explain what ModelBuilder is and how it differs from writing a Python script for geoprocessing. What are two advantages of each approach?

2. **(Basic)** In ModelBuilder, what is the difference between a "tool," a "variable" (input/output data), and a "parameter"? Sketch a simple model that takes a DEM as input and produces a slope grid and a flow direction grid as outputs.

3. **(Intermediate)** Write a Python script (using arcpy or an equivalent library such as PyQGIS or WhiteboxTools) that: (a) reads a DEM raster, (b) fills pits, (c) computes flow direction, (d) computes flow accumulation, and (e) saves all outputs to a specified folder. Include error handling for missing input files.

4. **(Intermediate)** You need to repeat the same terrain analysis for 12 sub-basins. Describe how you would automate this using: (a) a ModelBuilder iterator, (b) a Python loop. Which approach is more flexible? Which is easier for a non-programmer?

5. **(Advanced)** Design an automated workflow that downloads DEM data from an online service (e.g., OpenTopography API or Copernicus DEM), clips it to a user-specified bounding box, fills pits, computes flow direction and accumulation, delineates a watershed to a user-specified outlet point, and exports a summary report with drainage area, mean elevation, and drainage density. Write pseudocode or a flowchart.

---

### Chapter 13 Exercises: Seeing the Ground in 3D -- LiDAR

1. **(Basic)** Explain the difference between a Digital Elevation Model (DEM), a Digital Surface Model (DSM), and a Digital Terrain Model (DTM). Which is most appropriate for hydrologic analysis and why?

2. **(Basic)** LiDAR point cloud data is typically classified into categories such as ground, vegetation, buildings, and water. Why is ground classification essential before creating a hydrologic DEM from LiDAR?

3. **(Intermediate)** A LiDAR survey delivers a DTM at 1 m resolution for a 50 km^2 floodplain. Calculate the number of grid cells and the approximate file size (assuming 32-bit floating point, uncompressed). How does this compare to a 10 m DEM of the same area?

   *Expected answer: 1 m DEM: 50 x 10^6 cells (50 km^2 / 1 m^2). File size = 50 x 10^6 x 4 bytes = 200 MB. 10 m DEM: 500,000 cells. File size = 2 MB. The LiDAR DEM is 100 times larger.*

4. **(Intermediate)** Discuss how LiDAR-derived DEMs improve flood inundation mapping compared to 10 m or 30 m DEMs. Reference the HAND method (Chapter 14) and explain why vertical accuracy is particularly important for low-gradient floodplains.

5. **(Advanced)** Hungary has recently acquired nationwide airborne LiDAR coverage. Discuss the implications for: (a) urban flood mapping in Budapest, (b) agricultural drainage analysis on the Great Plain, (c) levee condition assessment along the Tisza. For each application, estimate what DEM resolution is needed and what LiDAR point density would achieve it.

---

## Part V: Flood Analysis (Chapters 14--17)

### Chapter 14 Exercises: How High Above the River?

*Adapted from Maidment Exercise 5 (HAND/Flood Inundation Analysis), computational steps.*

1. **(Basic)** Define HAND (Height Above Nearest Drainage). Explain conceptually how it is computed from a DEM and a stream raster. Why is the value exactly zero on mapped streams and increasing as you move away?

2. **(Basic)** Explain why D-infinity flow direction is preferred over D8 for computing HAND across hillslopes, while D8 is used for delineating the stream network itself.

3. **(Intermediate)** In the Onion Creek catchment (Exercise 5), a HAND analysis of one catchment polygon yielded the following for a stage height of 1 m: 658 grid cells below 1 m, cell size 10 m, mean inundation depth 0.713 m. Calculate: (a) the flooded surface area, (b) the flood volume, (c) the cross-sectional area of the channel if the stream reach length through the catchment is 4,308 m.

   *Expected answers: (a) Surface area = 658 x 100 = 65,800 m^2. (b) Volume = 0.713 x 65,800 = 46,915 m^3. (c) Cross-sectional area = Volume / Length = 46,915 / 4,308 = 10.9 m^2.*

4. **(Intermediate)** Using Manning's equation Q = (1/n) x A x R^(2/3) x S^(1/2), calculate the discharge for the Onion Creek reach described above. Given: A = 10.9 m^2, wetted perimeter P = 15.29 m (from bed area / reach length), S = 0.001617, n = 0.05.

   *Expected answer: R = A/P = 10.9/15.29 = 0.713 m. Q = (1/0.05) x 10.9 x 0.713^(2/3) x 0.001617^(1/2) = 20 x 10.9 x 0.798 x 0.04021 = 20 x 10.9 x 0.0321 = 7.0 m^3/s = 247 ft^3/s.*

5. **(Advanced)** Repeat the HAND hydraulic property calculation (as in problem 3-4 above) for stage heights of 6 m, 10 m, and 14 m. The number of inundated cells, mean depths, and bed slopes are to be extracted from the HAND raster for each stage. Plot a synthetic rating curve (stage vs. discharge). If the estimated flood flow for this reach is 98,231 ft^3/s (2,782 m^3/s), interpolate the corresponding flood stage from your rating curve. Discuss the uncertainties in this approach.

   *Note: This requires GIS computation. Students should fill in a table similar to the one in Exercise 5 and produce a rating curve plot. The flood stage for 98,231 ft^3/s should be approximately 12--13 m based on typical Onion Creek HAND analysis results.*

---

### Chapter 15 Exercises: Mapping Where Floods Go

*Adapted from Maidment Exercise 5, inundation and impact steps.*

1. **(Basic)** Describe how a flood inundation map is created from a HAND raster and a flood stage height. What raster calculator operation is used?

   *Expected answer: Inundation depth = stage height - HAND, for all cells where HAND is less than the stage height. Cells with HAND >= stage are not inundated.*

2. **(Basic)** Explain why DEM-derived catchment boundaries (CatchPoly) sometimes do not align perfectly with NHDPlus catchment boundaries. What implications does this have for HAND-based flood mapping?

3. **(Intermediate)** A flood inundation analysis identifies 2,400 grid cells (10 m resolution) with HAND values less than 8 m in a catchment. The mean HAND value for these cells is 3.2 m. If the flood stage is 8 m, calculate: (a) the total inundated area, (b) the mean inundation depth, (c) the total flood volume in this catchment.

   *Expected answers: (a) 2,400 x 100 = 240,000 m^2 = 0.24 km^2. (b) Mean depth = 8 - 3.2 = 4.8 m. (c) Volume = 4.8 x 240,000 = 1,152,000 m^3 = 1.15 million m^3.*

4. **(Intermediate)** Using the "Extract Values to Points" tool, you overlay address points on a HAND raster and find the following distribution of HAND values for 150 addresses in a catchment: 5 addresses with HAND < 3 m, 12 with 3--6 m, 25 with 6--9 m, 38 with 9--12 m, 70 with HAND > 12 m. If the flood stage is estimated at 9 m, how many addresses are subject to flooding? What fraction of the total?

   *Expected answer: Addresses with HAND < 9 m: 5 + 12 + 25 = 42 addresses. Fraction = 42/150 = 28%.*

5. **(Advanced)** Design a complete HAND-based flood risk assessment for a reach in your country. Steps should include: DEM acquisition and conditioning, stream network delineation, HAND computation, rating curve derivation using Manning's equation, flood stage estimation for a design discharge (e.g., 100-year flood), inundation mapping, and overlay with building footprints or address points. Document each step and discuss sources of uncertainty.

   *Hungarian parallel: Apply this workflow to a reach of the Hernad River near Miskolc, using the Hungarian LiDAR DEM. Compare your HAND-derived inundation map with the official flood hazard map (arvizveszelyes terulet) from OVF (National Water Directorate).*

---

### Chapter 16 Exercises: Forecasting Floods in Real Time

1. **(Basic)** Describe the four forecasting horizons of the US National Water Model (Analysis and Assimilation, Short Range, Medium Range, Long Range). For each, state the cycling frequency, forecast duration, and primary use case.

2. **(Basic)** The National Water Model produces forecasts for every NHDPlus reach in the United States. How many reaches are there, approximately? What spatial resolution is used for the land surface model component?

3. **(Intermediate)** Access the European Flood Awareness System (EFAS) at https://www.efas.eu and compare it with the US National Water Model. Discuss similarities and differences in: (a) spatial coverage, (b) spatial resolution, (c) forecast horizons, (d) forcing data, and (e) public accessibility of forecasts.

4. **(Intermediate)** A streamflow forecast shows the following 5-day hydrograph for a river reach: Day 1 = 45 m^3/s, Day 2 = 120 m^3/s, Day 3 = 310 m^3/s, Day 4 = 185 m^3/s, Day 5 = 80 m^3/s. Estimate the total volume of flow over these 5 days (assume constant flow within each day). If the flood threshold for this reach is 200 m^3/s, on which day(s) is flooding expected?

   *Expected answer: Volume = (45 + 120 + 310 + 185 + 80) x 86,400 = 740 x 86,400 = 63.94 million m^3. Flooding expected on Day 3 (310 > 200).*

5. **(Advanced)** The National Water Model uses a process-based hydrological model (Noah-MP land surface model coupled with channel routing). Discuss the advantages and limitations of this approach compared to a purely data-driven machine learning model for flood forecasting. Reference Google's flood forecasting initiative and other AI-based approaches as of 2026.

---

### Chapter 17 Exercises: Who Lives in the Flood Zone?

1. **(Basic)** Explain the difference between a flood hazard map and a flood risk map. Why does flood risk require information beyond just the inundation extent?

2. **(Intermediate)** A 100-year flood inundation map identifies 850 residential buildings in the flood zone. The average building value is EUR 180,000, and the expected damage factor at the predicted flood depth is 35%. Calculate the expected annual damage (EAD) assuming only this single return period event. Discuss why a full risk analysis would require multiple return periods.

   *Expected answer: Total damage for the 100-year event = 850 x 180,000 x 0.35 = EUR 53.55 million. Annual exceedance probability = 1/100 = 0.01. EAD (simplified, single event) = 53.55 x 0.01 = EUR 535,500. A full analysis integrates the damage-probability curve over all return periods.*

3. **(Intermediate)** Using census or population density data for your area, estimate the number of people living within the area identified as flood-prone (HAND < 5 m) along a 10 km river reach. If the flood-prone area is 2.5 km^2 and the population density is 1,200 persons/km^2, how many people are potentially exposed?

   *Expected answer: 2.5 x 1,200 = 3,000 people.*

4. **(Intermediate)** Describe how you would use GIS overlay analysis to combine a flood inundation map with: (a) building footprints, (b) critical infrastructure locations (hospitals, schools, power stations), (c) road networks. What output would you produce for emergency planners?

5. **(Advanced)** Design a socio-hydrological flood risk analysis for a district in Budapest along the Danube. Your analysis should include: flood hazard (from HAND or official flood maps), exposure (building footprints and census data), and vulnerability (building type, floor level, socioeconomic indicators). Propose a GIS workflow and discuss data availability in the Hungarian context.

---

## Part VI: Groundwater (Chapters 18--21)

### Chapter 18 Exercises: Seeing Underground -- 3D Subsurface GIS

1. **(Basic)** Explain why representing subsurface geology in GIS is fundamentally different from representing surface topography. What additional dimensions and data types are needed?

2. **(Basic)** Define the following terms as used in hydrogeological GIS: borehole log, stratigraphic layer, voxel model, cross-section. How do they relate to each other?

3. **(Intermediate)** You have borehole logs from 25 wells in an alluvial aquifer. Each log records the depth to the top and bottom of a gravel layer (the aquifer). Describe how you would use GIS interpolation tools to create: (a) a surface representing the top of the aquifer, (b) a surface representing the bottom, (c) a thickness map. What interpolation method would you choose and why?

4. **(Intermediate)** A 3D voxel model of a 10 km x 10 km area has a horizontal resolution of 100 m and a vertical resolution of 5 m, covering a depth range of 0 to 200 m. Calculate the total number of voxels. What file size would this require if each voxel stores one 32-bit floating-point value?

   *Expected answer: Horizontal: 100 x 100 = 10,000 columns/rows. Vertical: 200/5 = 40 layers. Total voxels = 10,000 x 40 = 400,000... Wait -- 10 km / 100 m = 100 in each horizontal direction. So 100 x 100 x 40 = 400,000 voxels. File size = 400,000 x 4 bytes = 1.6 MB. This is quite manageable.*

5. **(Advanced)** Compare two approaches for 3D subsurface modeling in GIS: (a) stacked 2D surfaces (one raster per geological horizon), and (b) true 3D voxel models. Discuss the advantages and limitations of each for: aquifer property mapping, groundwater flow modeling, and visualization. Which approach is supported by your GIS software?

---

### Chapter 19 Exercises: Wells, Boreholes, and Aquifer Maps

1. **(Basic)** What information is typically recorded in a well completion report or borehole log? List at least six data fields that are relevant for hidroinformatics.

2. **(Intermediate)** You have water level measurements from 30 monitoring wells in an unconfined aquifer. Describe the steps to create a potentiometric surface (water table map) using GIS. What interpolation method would you use? What are the boundary conditions?

3. **(Intermediate)** A monitoring well network shows the following water levels (meters above sea level) at four wells: Well 1 (X=500, Y=300): 125.3 m; Well 2 (X=800, Y=300): 122.1 m; Well 3 (X=500, Y=600): 124.7 m; Well 4 (X=800, Y=600): 121.5 m. Estimate the hydraulic gradient magnitude and direction using a planar fit.

   *Expected answer: dh/dx = ((122.1 - 125.3) + (121.5 - 124.7)) / (2 x 300) = (-3.2 + -3.2)/600 = -0.01067. dh/dy = ((124.7 - 125.3) + (121.5 - 122.1)) / (2 x 300) = (-0.6 + -0.6)/600 = -0.002. Gradient magnitude = sqrt(0.01067^2 + 0.002^2) = 0.01086. Direction = atan(0.002/0.01067) = 10.6 degrees south of east (flow is generally eastward with a slight southward component).*

4. **(Intermediate)** Hungarian borehole databases (e.g., from MBFSZ, the Mining and Geological Survey) often contain thousands of records with inconsistent coordinate systems. Describe a QA/QC workflow in GIS to: (a) identify records with swapped X/Y coordinates (using the EOV value range rule), (b) detect duplicate records, (c) flag records with impossible depth values.

5. **(Advanced)** Design a GIS-based aquifer vulnerability assessment using the DRASTIC method (Depth to water, net Recharge, Aquifer media, Soil media, Topography, Impact of vadose zone, hydraulic Conductivity). Describe what data layers are needed, how they are reclassified and weighted, and how the final vulnerability index is computed using raster overlay. Apply this conceptually to the Danube gravel aquifer near Budapest.

---

### Chapter 20 Exercises: Building a Picture of the Underground

1. **(Basic)** Explain the concept of "hydrostratigraphic units" and how they differ from lithostratigraphic units. Why is this distinction important for groundwater modeling?

2. **(Intermediate)** You have a set of geological cross-sections drawn by a geologist. Describe how you would digitize these into a GIS and use them to constrain a 3D geological model. What challenges arise when cross-sections from different sources do not agree?

3. **(Intermediate)** A geophysical survey (electrical resistivity tomography) has mapped the depth to bedrock along a river valley transect. The results are provided as a series of (X, Y, depth_to_bedrock) points. Describe how you would integrate this data with borehole logs to improve your aquifer thickness map.

4. **(Advanced)** Compare two software platforms for 3D geological modeling that can integrate with GIS (e.g., Leapfrog, GemPy, GSLIB + QGIS). For each, describe the modeling approach (implicit vs. explicit surfaces, geostatistical simulation), data input requirements, and ability to export results to a groundwater flow model.

5. **(Advanced)** The Great Hungarian Plain (Alfold) has a complex multi-layered aquifer system. Using publicly available data from MBFSZ, design a workflow to build a hydrogeological model of a 50 km x 50 km area. Describe what data you would need, what GIS operations you would perform, and how you would validate your model.

---

### Chapter 21 Exercises: Simulating Groundwater Flow

1. **(Basic)** Explain Darcy's Law in words and as an equation. What are the units of hydraulic conductivity, hydraulic gradient, and specific discharge?

2. **(Basic)** Describe the general steps to set up a numerical groundwater flow model (using MODFLOW or equivalent). What GIS data layers are needed as inputs?

3. **(Intermediate)** A simple confined aquifer has transmissivity T = 500 m^2/day, width W = 2 km, and hydraulic gradient i = 0.003. Calculate the volumetric flow rate through a cross-section of this aquifer using Darcy's Law.

   *Expected answer: Q = T x W x i = 500 x 2000 x 0.003 = 3,000 m^3/day = 34.7 L/s.*

4. **(Intermediate)** Describe how GIS-based preprocessing tools (such as FloPy's model grid generation or ModelMuse) convert raster and vector GIS layers into MODFLOW input files. What spatial operations are involved (resampling, zonal statistics, polygon-to-grid assignment)?

5. **(Advanced)** Set up a simple 2D steady-state groundwater flow model for a rectangular domain (5 km x 3 km) with: constant head boundaries on the east and west sides (100 m and 95 m), no-flow boundaries on the north and south, homogeneous K = 10 m/day, and one pumping well at the center extracting 500 m^3/day. Use MODFLOW (via FloPy or ModelMuse) or an analytical solution to compute the head distribution. Prepare a GIS map of the potentiometric surface with flow vectors.

---

## Part VII: Data-Model Integration and AI (Chapters 22--25)

### Chapter 22 Exercises: When Models Meet Data

1. **(Basic)** Explain the concept of model calibration. Why is it necessary, and what is the danger of overfitting?

2. **(Basic)** Define the Nash-Sutcliffe Efficiency (NSE) coefficient. Write the formula and explain what values of NSE = 1, NSE = 0, and NSE < 0 indicate about model performance.

   *Expected answer: NSE = 1 - [sum of (observed - simulated)^2 / sum of (observed - mean_observed)^2]. NSE = 1 means perfect fit. NSE = 0 means the model is as good as using the observed mean. NSE < 0 means the model is worse than the mean.*

3. **(Intermediate)** You calibrate a rainfall-runoff model and obtain the following observed (O) and simulated (S) monthly streamflows (m^3/s): O = [12, 15, 45, 80, 55, 30, 18, 10, 8, 15, 25, 20]; S = [14, 18, 40, 72, 60, 28, 20, 12, 10, 13, 22, 18]. Calculate the NSE, RMSE, and percent bias (PBIAS).

   *Expected answers: Mean O = 27.75. Sum (O-S)^2 = 4+9+25+64+25+4+4+4+4+4+9+4 = 160. Sum (O-mean)^2 = 248.06+162.56+297.56+2730.06+742.56+5.06+95.06+315.06+390.06+162.56+7.56+60.06 = 5216.2. NSE = 1 - 160/5216.2 = 0.969. RMSE = sqrt(160/12) = 3.65 m^3/s. PBIAS = 100 x (333 - 327)/333 = 1.8%. The model performs very well.*

4. **(Intermediate)** Explain the split-sample test for model validation. How would you divide a 20-year daily streamflow record into calibration and validation periods? What additional test would you perform if the record contains both wet and dry years?

5. **(Advanced)** Discuss the "equifinality" problem in hydrological modeling: multiple parameter sets can produce similarly good fits to observed data. How does this affect decision-making in water resources management? Describe at least two approaches to address equifinality (e.g., multi-objective calibration, Bayesian uncertainty analysis, regularization).

---

### Chapter 23 Exercises: AI as a Hydrologist's Assistant

1. **(Basic)** Explain the difference between a process-based hydrological model and a machine learning model. Give one example of each that is used in streamflow prediction.

2. **(Basic)** What is a Long Short-Term Memory (LSTM) neural network? Why is it particularly well-suited for hydrological time series prediction?

3. **(Intermediate)** You train an LSTM model to predict daily streamflow at a gauged catchment using inputs of daily precipitation, temperature, and antecedent streamflow. The model achieves NSE = 0.92 on the test period. However, when you apply it to a neighboring ungauged catchment, performance drops to NSE = 0.55. Discuss possible reasons and propose at least two strategies to improve transferability.

4. **(Intermediate)** Compare the performance and interpretability of the following ML approaches for flood forecasting: (a) Random Forest regression, (b) LSTM neural network, (c) a hybrid model combining a conceptual rainfall-runoff model with ML post-processing. Which would you recommend for operational use and why?

5. **(Advanced)** Google's flood forecasting system (as of 2025-2026) uses a combination of hydrological models and machine learning to provide flood warnings in data-scarce regions. Research and describe: (a) the key innovation in their approach, (b) how it handles ungauged basins, (c) what countries it covers, and (d) its limitations. Propose how a similar system could be deployed for the Tisza River basin, identifying the specific data challenges.

---

### Chapter 24 Exercises: Agentic AI -- The Autonomous Modeler

1. **(Basic)** Define "agentic AI" in the context of hidroinformatics. How does an AI agent differ from a traditional script or workflow?

2. **(Basic)** Describe three tasks in a typical hidroinformatics workflow where an AI agent could autonomously make decisions: data selection, parameter tuning, and result interpretation. For each, identify the risks of autonomous operation.

3. **(Intermediate)** An AI agent is tasked with calibrating a MODFLOW groundwater model. It has access to observed head data from 20 wells and can modify hydraulic conductivity in 5 zones. Describe the optimization loop the agent would follow. What stopping criteria should be defined? What guardrails should prevent the agent from producing physically unreasonable results (e.g., negative hydraulic conductivity)?

4. **(Intermediate)** Compare "code-generating AI" (e.g., an LLM that writes Python scripts for GIS processing) with "tool-using AI" (e.g., an agent that calls GIS functions directly). What are the advantages and risks of each approach for hidroinformatics workflows? Give a concrete example.

5. **(Advanced)** Design an agentic AI system for real-time flood early warning. The agent should: (a) ingest weather forecast data, (b) run a hydrological model, (c) compute HAND-based inundation maps, (d) identify threatened infrastructure using GIS overlay, and (e) generate a warning bulletin. Draw an architecture diagram showing the components, data flows, decision points, and human oversight requirements. Discuss what can go wrong and how to mitigate it.

---

### Chapter 25 Exercises: The Future of Water Intelligence

1. **(Basic)** Identify three emerging technologies (beyond those covered in earlier chapters) that you believe will significantly impact hidroinformatics in the next decade. For each, write two sentences explaining the technology and its potential application.

2. **(Intermediate)** The concept of a "digital twin" for a river basin involves a continuously updated virtual replica that mirrors real-time conditions. Describe what data streams would feed such a twin, what models would run within it, and what decisions it could support. Identify the biggest technical and institutional barriers to implementation.

3. **(Intermediate)** Climate change is altering hydrological regimes worldwide. Discuss how hidroinformatics tools and methods need to adapt. Specifically address: (a) the stationarity assumption in flood frequency analysis, (b) the need for dynamic land cover and land use data, (c) the role of ensemble climate projections in water resources planning.

4. **(Advanced)** Write a 500-word essay on the ethical implications of AI-driven water management. Consider: (a) who benefits and who might be harmed by automated decision-making in flood warning, water allocation, or drought response, (b) issues of algorithmic transparency and accountability, (c) the digital divide between data-rich and data-poor countries or communities.

5. **(Advanced)** Propose a 5-year research agenda for hidroinformatics at a national level (choose your own country or Hungary). Identify: (a) the three most pressing water challenges, (b) the specific hidroinformatics capabilities needed to address them, (c) the data infrastructure investments required, (d) the human capacity building (education, training) needed. Present your proposal as a structured one-page summary suitable for a funding agency.

---

## Answer Key Notes

For calculation problems, expected answers are provided inline with each exercise. For open-ended and essay-type questions, grading should emphasize:

- Correct application of concepts from the relevant chapter
- Logical reasoning and clear communication
- Appropriate use of units and significant figures in calculations
- Demonstration of practical GIS skills where applicable
- Ability to adapt US-centric examples to international contexts

For exercises requiring GIS software, acceptable platforms include ArcGIS Pro, QGIS, Google Earth Engine, or any platform supporting the required spatial analysis operations. Where original exercises referenced ArcGIS-specific tools, equivalent operations exist in all major GIS platforms.

---

## Practical GIS Exercises (Adapted from Maidment's Course)

The five exercises below were originally developed by David R. Maidment (University of Texas at Austin) and David G. Tarboton (Utah State University) for the graduate course *GIS in Water Resources* (Fall 2018). They form a progressive sequence: from basic GIS skills through watershed delineation to flood inundation analysis. Each exercise is presented in three variants:

- **Original (US)** -- Uses the original American datasets and study areas exactly as designed.
- **International** -- Adapts the exercise for students outside the US, using freely available global data.
- **Hungarian** -- Adapts the exercise for the Hungarian/Central European context, using national datasets and local watersheds.

Students should complete the variant most relevant to their location, or ideally attempt both the Original and their regional variant to appreciate the differences in data infrastructure across countries.

**Software requirements.** All exercises were originally written for ArcGIS Pro 2.2+. Equivalent workflows exist in QGIS 3.x (free and open source). Where ArcGIS-specific tools are mentioned, the QGIS equivalent is noted in brackets. Python alternatives (WhiteboxTools, PyQGIS, arcpy) are also acceptable.

---

### Exercise 1: Introduction to GIS for Water Resources

*Based on Maidment & Tarboton, Exercise 1 (2018). Estimated time: 3--4 hours.*

**Learning objectives.** (1) Create a GIS project and organize data in a geodatabase. (2) Add vector and raster data layers to a map. (3) Modify symbology, reorder layers, and interpret attribute tables. (4) Explore coordinate systems, projections, and spatial properties. (5) Perform basic geoprocessing: Select by Attributes, Select by Location, Project, Clip, spatial joins.

#### Variant A: Original (US -- Texas)

**Study area.** State of Texas with pan evaporation stations and county boundaries.

**Data.** Three shapefiles provided with the original exercise data:

- `Texas.shp` -- outline of the State of Texas
- `Counties.shp` -- all Texas county boundaries (254 counties)
- `Evap.shp` -- pan evaporation stations across Texas (point features with annual evaporation data)

Original data download: `http://hydrology.usu.edu/dtarb/giswr/2018/Ex1Data.zip`

**Procedure.**

1. **Create a new project.** Open ArcGIS Pro (or QGIS), create a blank project named `Ex1Project`. Save it in a working directory.
2. **Add data.** Use the Add Data button to load all three shapefiles into the map.
3. **Reorder layers.** Arrange drawing order so that Counties appears above Texas, and Evap (points) appears on top. The point layer should not be hidden behind polygons.
4. **Modify symbology.** Set Texas to a transparent fill with a green outline (width 2 pt). Set Counties to a light green fill with grey outlines. Set Evap points to red circles, size 6 pt.
5. **Store data in a geodatabase.** Export (Copy Features) each shapefile into the project geodatabase (`Ex1Project.gdb`). Remove the original shapefiles from the map and work from the geodatabase copies.
6. **Examine properties.** Open the Properties of the Evap feature class. Record the coordinate system (should be GCS_North_American_1983), geometry type (Point), and number of features.
7. **Attribute exploration.** Open the Evap attribute table. Identify the field containing annual pan evaporation values. Sort by this field to find the station with the highest and lowest evaporation.
8. **Select by Attributes.** Select all evaporation stations with annual evaporation > 70 inches. Record how many stations are selected and observe their spatial distribution.
9. **Select by Location.** Select all counties that contain at least one evaporation station. How many counties have stations? What fraction of all Texas counties is this?
10. **Labeling.** Label the evaporation stations with their annual evaporation value. Label counties with their name.
11. **Create a map layout.** Insert a layout with title "Texas Pan Evaporation", scale bar, north arrow, and legend. Export as PDF.

**Deliverables.** (a) PDF map layout showing Texas counties with evaporation stations. (b) Answers: number of stations with evaporation > 70 inches; number of counties containing stations; station names with highest and lowest evaporation.

#### Variant B: International

**Study area.** Choose any country or region you are familiar with.

**Data sources (all free).**

- Country and administrative boundaries: Natural Earth (https://www.naturalearthdata.com/) -- 1:10m Admin 0 and Admin 1 shapefiles.
- Climate stations: Global Historical Climatology Network (GHCN-Daily) via NOAA (https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily). Download station metadata as CSV, then display as XY points.
- Alternative: ERA5-Land monthly averaged data from Copernicus Climate Data Store (https://cds.climate.copernicus.eu/) -- extract potential evaporation raster for your region.

**Procedure.**

1. Create a new project. Download the Natural Earth Admin 0 (country outline) and Admin 1 (provinces/states) shapefiles for your chosen country.
2. Download GHCN station metadata for your country. Filter for stations reporting evaporation or precipitation. Save as CSV with latitude/longitude columns.
3. Add the CSV as XY point data using the *Add XY Data* tool [QGIS: *Add Delimited Text Layer*]. Set the coordinate system to WGS 1984 (EPSG:4326).
4. Follow steps 3--11 from Variant A, substituting your national data for the Texas data.
5. **Additional task.** Identify which provinces/states have no climate stations. Discuss the implications for spatial interpolation of climate variables.

**Deliverables.** Same as Variant A, adapted for your region. Additionally: a brief paragraph discussing data availability compared to the US.

#### Variant C: Hungarian

**Study area.** Hungary, with meteorological stations and county (megye) boundaries.

**Data sources.**

- Country and county boundaries: KSH (Central Statistical Office) via data.gov.hu, or the EuroGlobalMap dataset from EuroGeographics. Shapefiles in EOV (HD72/EOV, EPSG:23700) or WGS84.
- Meteorological stations: OMSZ (Hungarian Meteorological Service) station list. A publicly available list of synoptic and climatological stations with coordinates can be obtained from https://www.met.hu/. Alternatively, use the E-OBS gridded dataset (https://www.ecad.eu/download/ensembles/download.php) for precipitation or temperature.
- Evaporation data: If station-level evaporation data is not available, use mean annual temperature from OMSZ stations as a proxy variable, or download ERA5-Land potential evaporation for Hungary from the Copernicus CDS.

**Procedure.**

1. Create a new project named `Gy1Projekt` (Gy = Gyakorlat, exercise).
2. Add the Hungary country boundary and county boundary shapefiles. Verify the coordinate system -- if the data is in EOV (EPSG:23700), note the false easting (650,000 m) and false northing (200,000 m). If coordinates look wrong, check for swapped X/Y using the EOV value range rule (Northing: 0--400,000; Easting: 400,000--1,000,000).
3. Add meteorological station point data. If working from a CSV, use the appropriate coordinate fields. If stations are in WGS84, project them to EOV using the *Project* tool [QGIS: *Reproject Layer*].
4. Follow steps 3--11 from Variant A using Hungarian data.
5. **Additional task.** Select all meteorological stations within Borsod-Abauj-Zemplen county (the county containing the Sajo and Hernad rivers). How many stations are there? What is the station density (stations per 1000 km^2)?

**Deliverables.** Same as Variant A, adapted for Hungary. Additionally: a comparison of station density between Hungary and Texas.

---

### Exercise 2: Building a Watershed Base Map

*Based on Maidment & Tarboton, Exercise 2 (2018). Estimated time: 4--6 hours.*

**Learning objectives.** (1) Download hydrographic data from national web services. (2) Create a feature dataset with a defined coordinate system. (3) Select features by attribute and export subsets. (4) Dissolve polygon boundaries to create basin outlines. (5) Add point features from a table of coordinates. (6) Access and display forecast data from a national water model.

#### Variant A: Original (US -- San Marcos Basin, Texas)

**Study area.** San Marcos River Basin, South Texas (HUC-8 = 12100203), within USGS Water Resources Region 12 (Texas-Gulf).

**Data.**

- NFIEGeo_12.gdb -- geodatabase containing subwatersheds, catchments, flowlines, waterbodies, and stream gages for Region 12. Download from HydroShare: https://www.hydroshare.org/resource/1d78964652034876b1c190647b21a77d/
- Stream gage coordinates for USGS gages in the San Marcos basin (from NWIS: https://waterdata.usgs.gov/nwis)
- National Water Model forecasts from HydroShare or NOAA

**Procedure.**

1. **Get the data.** Download and unzip NFIEGeo_12.gdb. Open ArcGIS Pro, create a new blank project named `Exercise2`.
2. **Add data.** Add the Geographic feature dataset from NFIEGeo_12.gdb to your map. Five feature classes appear: StreamGage, Flowline, Waterbody, Subwatershed, Catchment.
3. **Symbolize subwatersheds.** Turn off all layers except Subwatershed. Symbolize by Unique Values using the HUC_8 field. You should see over 100 distinct HUC-8 subbasins colored differently.
4. **Select the San Marcos Basin.** Open the Subwatershed attribute table. Use Select by Attributes: `HUC_8 = '12100203'`. This selects 32 HUC-12 subwatersheds within the San Marcos subbasin.
5. **Create a feature dataset.** In the project geodatabase (`Exercise2.gdb`), create a new Feature Dataset named `SanMarcos` with coordinate system GCS_North_American_1983.
6. **Export selected features.** With the 32 subwatersheds selected, use Data > Export Features to copy them into the SanMarcos feature dataset. Name the output `Subwatershed`. Clear the selection.
7. **Remove the Region 12 data** from the map. Turn on the San Marcos Subwatershed layer and symbolize by HUC_10 (Unique Values). You should see 5 HUC-10 watersheds.
8. **Create a basin boundary.** Use the Dissolve tool [QGIS: *Dissolve*] on the Subwatershed feature class with HUC_8 as the dissolve field. Name the output `Basin`. Symbolize it with no fill, green outline, width 2.
9. **Add land cover.** Download the National Land Cover Database (NLCD) 2019 for your area from MRLC (https://www.mrlc.gov/). Clip it to the basin boundary using Extract by Mask. Compute cell counts for each land cover class.
10. **Repeat for Flowlines.** Select and export the flowlines within the San Marcos Basin (use Select by Location with the Basin polygon).
11. **Create a point feature class from gage coordinates.** Find the coordinates of USGS gages 08170500 (San Marcos River at Luling) and 08171000 (Blanco River at Wimberley) from the NWIS website. Enter them in an Excel spreadsheet (columns: SiteID, LatDD, LongDD). Add this as XY data, set coordinate system to NAD83, and export to the SanMarcos feature dataset as `StreamGages`.
12. **Map layout.** Create a layout showing the San Marcos Basin with subwatersheds colored by HUC-10, flowlines, stream gages labeled, and the basin boundary.

**Deliverables.** (a) Map layout of the San Marcos Basin. (b) Table: number of HUC-12 subwatersheds, number of HUC-10 watersheds, total basin area (from dissolve), number of flowlines, land cover class percentages. (c) Screen capture of the SanMarcos feature dataset in the Catalog pane showing all feature classes.

#### Variant B: International

**Study area.** Choose a river basin of 500--5000 km^2 in any country.

**Data sources (all free).**

- HydroSHEDS / HydroBASINS (https://www.hydrosheds.org/) -- global watershed boundaries at multiple Pfafstetter levels. Download the level-12 basins shapefile for your continent.
- HydroRIVERS (https://www.hydrosheds.org/products/hydrorivers) -- global river network derived from HydroSHEDS. Includes stream order and upstream drainage area attributes.
- Global land cover: ESA WorldCover 10 m (https://esa-worldcover.org/) or Copernicus Global Land Cover 100 m (https://land.copernicus.eu/global/).
- Stream gage locations: GRDC (Global Runoff Data Centre, https://www.bafg.de/GRDC/) station catalog (free registration required).

**Procedure.**

1. Download HydroBASINS level-12 for your continent. Add to a new GIS project.
2. Identify the sub-basins that compose your study watershed. Select them using a basin identifier or by location (draw a polygon around the watershed outlet and select upstream).
3. Export the selected sub-basins and dissolve to create a single basin boundary.
4. Download and clip HydroRIVERS to the basin boundary.
5. Download ESA WorldCover or Copernicus land cover for the basin. Clip and compute land cover statistics.
6. Find stream gage locations from GRDC or a national hydrological service. Create a point feature class.
7. Create a map layout equivalent to Variant A.

**Additional task.** Compare the HydroBASINS boundary with any national watershed boundary dataset available for your country. Discuss discrepancies and their causes.

**Deliverables.** Same structure as Variant A.

#### Variant C: Hungarian

**Study area.** Sajo river basin (Sajo vizgyujto), approximately 12,700 km^2 total (Hungarian portion ~6,400 km^2), draining through Borsod-Abauj-Zemplen county to the Tisza.

**Data sources.**

- Watershed boundaries: OVF (Orszagos Vizugyi Foigazgatosag / National Water Directorate) -- sub-basin boundaries (reszvigyujto-hatarok) available via the national water management geoportal (https://geoportal.vizugy.hu/) or upon request. Alternative: use HydroBASINS level-12 clipped to the Sajo basin.
- River network: EU-Hydro river network (https://land.copernicus.eu/imagery-in-situ/eu-hydro) or HydroRIVERS for Hungary.
- Land cover: CORINE Land Cover 2018 (https://land.copernicus.eu/pan-european/corine-land-cover) or the Hungarian DDM-5 topographic database.
- Stream gages: OVF station list. Key gages on the Sajo include Sajo at Felsozsolca, Hernad at Hidasnemeti, Bodva at Szendrolare.
- Coordinate system: EOV (EPSG:23700). All Hungarian official data is in EOV.

**Procedure.**

1. Create a new project named `Gy2Sajo`. Set the map coordinate system to HD72/EOV (EPSG:23700).
2. Add the Sajo sub-basin boundaries. If using HydroBASINS (in WGS84), reproject to EOV.
3. Select the sub-basins composing the Sajo watershed (upstream of the confluence with the Tisza at Tisza-Sajo torkolat). Export and dissolve to create a single basin polygon.
4. Add the EU-Hydro or HydroRIVERS river network. Clip to the basin boundary.
5. Download CORINE Land Cover 2018 for Hungary. Clip to the basin and compute class statistics. Key classes to report: Agricultural land (CLC 2xx), Forest (CLC 3xx), Urban (CLC 1xx), Water bodies (CLC 5xx).
6. Create a stream gage point feature class. Enter the coordinates of at least 3 gages: Sajo at Felsozsolca (EOV Y~306,000, X~780,000), Hernad at Hidasnemeti (EOV Y~340,000, X~790,000), Bodva at Szendrolare (EOV Y~337,000, X~770,000). *Remember: verify EOV coordinates by value range, not by header labels.*
7. Create a map layout with the basin boundary, sub-basins, rivers, gages, and CORINE land cover.

**Additional tasks.**

- Compare the total basin area from your dissolve with the official value reported by OVF.
- Identify which sub-basins are in Slovakia (the Sajo rises in Slovakia as the Slana). Discuss the implications of transboundary data for hidroinformatics.

**Deliverables.** Same structure as Variant A, plus a brief discussion of transboundary data issues.

---

### Exercise 3: Spatial Analysis -- Slope, Aspect, and Flow Direction

*Based on Tarboton & Maidment, Exercise 3 (2018). Estimated time: 5--7 hours.*

**Learning objectives.** (1) Compute slope, aspect, and flow direction from a DEM using multiple algorithms (ESRI surface slope, D8, D-infinity). (2) Compare hand calculations with GIS-computed values. (3) Build a ModelBuilder workflow to automate a sequence of geoprocessing tools. (4) Perform spatial interpolation and compute watershed-average precipitation. (5) Use raster calculator for hydrologic water balance computations.

#### Variant A: Original (US)

**Study area.** Two parts: (1) A small synthetic DEM for hand calculations; (2) the San Marcos Basin for interpolation and water balance.

**Data.** Download from: `http://hydrology.usu.edu/dtarb/giswr/2018/Ex3Data.zip`

- `elev.asc` -- a 5-column x 4-row ASCII grid (cell size 10 m) for hand calculation exercises
- `demo.asc` -- a larger ASCII grid for testing the ModelBuilder workflow
- San Marcos Basin data from Exercise 2

**Part 1: Slope Calculations (hand + GIS).**

1. Given the following 5x4 grid of elevations (cell size 10 m):

   ```
   25.4  26.1  27.0  28.6  27.7
   25.0  26.0  26.4  27.9  27.4
   25.1  25.8  26.8  28.6  27.6
   27.5  28.0  27.7  30.6  28.3
   ```

   Calculate by hand the slope and aspect at the cell marked A (value 26.4, row 2 col 3) using three methods:
   - (i) The ESRI surface slope function (3rd-order finite difference, slides 41-44 of Maidment's Spatial Analysis lecture)
   - (ii) The D8 (8-direction pour point) model
   - (iii) The D-infinity algorithm

   Compare the three methods and comment on which provides a better approximation of water flow direction.

2. Save the grid as `elev.asc` in ASCII raster format. Import into ArcGIS Pro [QGIS: just drag-and-drop the .asc file]. Compute Slope (percent rise) and Aspect using Spatial Analyst tools [QGIS: *Raster > Analysis > Slope/Aspect*]. Click on cell A and verify your hand calculations.

3. Compute Flow Direction (D8) with Output Drop raster. Verify the flow direction and percentage drop at cell A against your hand calculations. Repeat with DINF flow direction type.

**Part 1.3: ModelBuilder.**

4. Build a ModelBuilder workflow [QGIS: *Processing > Graphical Modeler*] that chains: ASCII to Raster > Flow Direction (D8) > Slope > Aspect > Flow Direction (DINF). Set the ASCII input file and all outputs as parameters.
5. Run the model on `demo.asc`. Record the min/max values of each output. Export a screenshot of the model diagram.

**Part 2: Spatial Interpolation and Water Balance (San Marcos Basin).**

6. Access the ArcGIS Living Atlas elevation service or download NED/3DEP data for the San Marcos Basin. Extract elevation within the basin boundary. Compute mean elevation using Zonal Statistics.
7. Obtain precipitation station data for the basin area (from NOAA GHCN or PRISM). Interpolate using IDW to create a continuous precipitation surface over the basin. Compute mean annual precipitation using Zonal Statistics.
8. Use the Raster Calculator to compute the runoff ratio: `Runoff = Precipitation - Evapotranspiration` and `Runoff Ratio = Runoff / Precipitation`. Discuss the spatial pattern.

**Deliverables.** (a) Hand calculations of slope at point A (three methods) with comments. (b) Table of GIS-computed slope, aspect, flow direction, and percentage drop at cells A and B. (c) ModelBuilder screenshot. (d) Map of interpolated precipitation and table of watershed-average values.

#### Variant B: International

**Study area.** Any watershed of 500--5000 km^2.

**Data sources.**

- Copernicus DEM GLO-30 (30 m global DEM): https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model (free registration). Download GeoTIFF tiles for your area.
- Alternative: SRTM 30 m from OpenTopography (https://opentopography.org/) or USGS EarthExplorer (https://earthexplorer.usgs.gov/).
- Precipitation: ERA5-Land monthly data from Copernicus CDS, or CHIRPS (https://www.chc.ucsb.edu/data/chirps) for tropical/subtropical regions.
- Potential evapotranspiration: ERA5-Land PET or Global Aridity Index (https://cgiarcsi.community/).

**Procedure.**

1. Complete Part 1 (hand calculations) exactly as in Variant A -- the synthetic grid is location-independent.
2. For Part 1.3, build the same ModelBuilder workflow but apply it to a clipped Copernicus DEM tile of your study area.
3. For Part 2, download the Copernicus DEM for your basin. Clip, compute mean elevation.
4. Download ERA5-Land monthly total precipitation for your basin. Compute mean annual precipitation. Create a precipitation map using the raster data directly (no interpolation needed since ERA5 is gridded).
5. Download ERA5-Land PET. Compute runoff depth = precipitation minus PET. Compute runoff ratio.

**Deliverables.** Same as Variant A, adapted for your region. Discuss differences in DEM resolution and precipitation data density compared to the US.

#### Variant C: Hungarian

**Study area.** (1) Synthetic grid for hand calculations; (2) Hernad sub-basin of the Sajo watershed for spatial analysis.

**Data sources.**

- DDM-5 (5 m resolution DEM of Hungary): Available from Lechner Tudastar (https://www.lechner.hu/) or FOLDMERO (https://www.foldmero.hu/). This is Hungary's highest-resolution national DEM. For coarser work, the EU-DEM v1.1 (25 m, https://www.eea.europa.eu/data-and-maps/data/copernicus-land-monitoring-service-eu-dem) is freely available.
- Precipitation: OMSZ station data or the CARPATCLIM gridded dataset (http://www.carpatclim-eu.org/) which provides 0.1-degree gridded daily meteorological data for the Carpathian Basin (1961--2010).
- Potential evapotranspiration: CARPATCLIM PET grids or ERA5-Land.
- Coordinate system: EOV (EPSG:23700).

**Procedure.**

1. Complete Part 1 (hand calculations) exactly as in Variant A.
2. For Part 1.3, apply the ModelBuilder workflow to a DDM-5 tile covering the Hernad valley near Miskolc.
3. For Part 2:
   - Download the EU-DEM or DDM-5 for the Hernad sub-basin. Clip to the basin boundary. Compute mean elevation using Zonal Statistics.
   - Download CARPATCLIM mean annual precipitation grid for the area. Clip to the basin. Compute basin-average precipitation.
   - Download CARPATCLIM PET. Compute runoff = precipitation minus PET. Compute runoff ratio.
   - Compare your computed runoff with the observed mean annual discharge at the Hernad at Hidasnemeti gage (available from OVF yearbooks, approximately 15--20 m^3/s mean annual flow for a drainage area of ~5,400 km^2).

**Additional task.** The Hernad basin is transboundary (Hornad in Slovakia). Discuss how you would obtain and merge the Slovak portion of the DEM and climate data to complete the full-basin analysis. What coordinate system issues arise when combining Hungarian EOV data with Slovak S-JTSK (EPSG:5514)?

**Deliverables.** Same as Variant A, plus a comparison of computed vs. observed runoff and a paragraph on transboundary data challenges.

---

### Exercise 4: Watershed and Stream Network Delineation

*Based on Tarboton & Maidment, Exercise 4 (2018). Estimated time: 6--8 hours.*

**Learning objectives.** (1) Use online and GIS tools for watershed delineation. (2) Download and merge DEM tiles from national data services. (3) Perform the complete hydrologic terrain analysis sequence: Fill > Flow Direction > Flow Accumulation > Stream Definition > Stream Links > Catchments. (4) Compare DEM-derived drainage networks with published hydrography datasets. (5) Compute drainage area, stream length, and drainage density.

#### Variant A: Original (US -- Logan River Basin, Utah)

**Study area.** Logan River above State Dam, near Logan, Utah. USGS Gage 10109000. Drainage area approximately 554 km^2 (214 sq mi). Latitude 41.7443 N, Longitude 111.7819 W.

**Data.**

- Stream gage coordinates from USGS NWIS (https://waterdata.usgs.gov/nwis)
- DEM tiles from The National Map (https://apps.nationalmap.gov/download/): USGS NED 1/3 arc-second tiles n42w112 and n43w112
- NHDPlus data from HydroShare or directly from the USGS
- Backup data: `http://www.caee.utexas.edu/prof/maidment/giswr2018/Ex4/Ex4data.zip`

**Procedure.**

**Part 1: Online Watershed Delineation.**

1. Create a point feature class at the gage location (41.7443 N, -111.7819 W) using XY Table to Point. Set coordinate system to GCS_North_American_1927 (NAD27) as reported by USGS.
2. Use the ArcGIS Online Watershed tool (Portal > Ready-To-Use Tools > Hydrology > Watershed) with Data Source Resolution = FINEST. This delineates the basin using a pre-processed global flow direction grid.
3. Create a 1 km buffer around the basin boundary for DEM extraction.

**Part 2: DEM Acquisition and Preparation.**

4. Download two 1/3 arc-second DEM tiles (n42w112 and n43w112) from The National Map.
5. Merge tiles using Mosaic to New Raster (pixel type = 32-bit float, 1 band).
6. Create a feature dataset `Basemap` in the project geodatabase with coordinate system NAD_1983_UTM_Zone_12N.
7. Export the gage and basin features into Basemap (this reprojects them to UTM).
8. Buffer the basin by 1 km. Extract by Mask the merged DEM to the buffer. Project the clipped DEM to UTM Zone 12N with cubic convolution resampling and 10 m cell size.

**Part 3: Hydrologic Terrain Analysis.**

9. **Fill** the projected DEM to remove pits.
10. **Flow Direction** (D8) on the filled DEM.
11. **Flow Accumulation** on the flow direction grid.
12. Define a **stream threshold**: use a threshold that produces a drainage density similar to the NHDPlus network (experiment with values around 1000--5000 cells).
13. **Stream Link** to assign unique IDs to each stream segment.
14. **Watershed** (catchments) using the stream link grid as pour points.
15. **Stream to Feature** to convert the stream raster to a polyline feature class.
16. **Raster to Polygon** to convert catchments to a polygon feature class.

**Part 4: Comparison with NHDPlus.**

17. Download NHDPlus flowlines and catchments for the Logan River basin.
18. Overlay DEM-derived streams on NHDPlus flowlines. Discuss differences in network geometry, number of segments, and alignment.
19. Compare DEM-derived basin boundary with the online-delineated boundary.

**Deliverables.** (a) Map of the Logan River basin showing DEM hillshade, DEM-derived streams, and NHDPlus flowlines for comparison. (b) Table: drainage area (from flow accumulation at outlet), number of stream segments, total stream length, drainage density. Compare with the USGS-reported 554 km^2 drainage area. (c) Discussion of discrepancies between DEM-derived and NHDPlus networks.

#### Variant B: International

**Study area.** Choose a mountain watershed of 200--1000 km^2 with a known gage.

**Data sources.**

- DEM: Copernicus DEM GLO-30 (https://spacedata.copernicus.eu/) or SRTM 30 m from OpenTopography.
- Online watershed delineation: HydroSHEDS (https://www.hydrosheds.org/) provides pre-computed flow direction grids, or use the USGS StreamStats tool for US basins. For any global location, use WhiteboxTools `Watershed` function with the Copernicus DEM.
- Published hydrography: HydroRIVERS (https://www.hydrosheds.org/products/hydrorivers) for comparison.

**Procedure.**

1. Download Copernicus DEM tiles for your area. Merge if necessary using `gdal_merge.py` or the Mosaic tool.
2. Skip the online delineation step (or use the HydroSHEDS pre-delineated basins as a reference boundary).
3. Choose a UTM zone appropriate for your study area. Project the DEM to UTM.
4. Follow steps 9--16 from Variant A.
5. Compare your DEM-derived streams with HydroRIVERS. Discuss resolution differences (HydroRIVERS is based on SRTM 3 arc-second, ~90 m, while your DEM is 30 m).

**Additional task.** If you have access to a higher-resolution national DEM (e.g., 5 m LiDAR), repeat the analysis and compare network density and basin boundary precision with the 30 m result.

**Deliverables.** Same as Variant A.

#### Variant C: Hungarian

**Study area.** Bodva river basin (Bodva vizgyujto), a tributary of the Sajo, approximately 900 km^2 in the Aggtelek karst region and Cserehát hills. Gage: Bodva at Szendrolare.

**Data sources.**

- DEM: DDM-5 (5 m) from Lechner Tudastar, or EU-DEM v1.1 (25 m). The DDM-5 is ideal but requires a data license. For free access, use the Copernicus DEM GLO-30 or EU-DEM.
- Published hydrography: EU-Hydro river network, or the 1:100,000 Hungarian hydrographic database (vizrajzi adatbazis) from OVF.
- Coordinate system: EOV (EPSG:23700).

**Procedure.**

1. Create a point feature class at the Bodva at Szendrolare gage location. Convert coordinates to EOV if necessary.
2. Download and prepare the DEM. If using EU-DEM (WGS84/ETRS89), reproject to EOV. If using DDM-5, it is already in EOV.
3. Extract the DEM to a buffered basin boundary. The Bodva basin rises in Slovakia (as Bodva), so you may need to include terrain north of the border.
4. **Fill, Flow Direction, Flow Accumulation, Stream Definition, Stream Link, Watershed, Stream to Feature, Raster to Polygon** -- follow the same sequence as Variant A.
5. Compare DEM-derived streams with EU-Hydro or the Hungarian hydrographic database.
6. **Karst considerations.** The Bodva basin includes the Aggtelek karst, where surface drainage and subsurface drainage diverge significantly. Identify areas where the DEM-derived network fails to represent the true drainage pattern. Discuss why DEM-based terrain analysis has fundamental limitations in karst regions.

**Additional tasks.**

- Compute the drainage area at the Szendrolare gage from flow accumulation. Compare with the official OVF drainage area.
- Identify the transboundary portion of the basin (in Slovakia). What fraction of the total drainage area lies outside Hungary?

**Deliverables.** Same as Variant A, plus a discussion of karst hydrology limitations for terrain analysis.

---

### Exercise 5: Height Above Nearest Drainage and Flood Inundation Analysis

*Based on Tarboton, Exercise 5 (2018). Estimated time: 6--8 hours.*

**Learning objectives.** (1) Compute the HAND raster from a DEM. (2) Derive stream reach hydraulic properties (cross-sectional area, wetted perimeter, bed slope) from HAND. (3) Apply Manning's equation to construct a synthetic rating curve (stage vs. discharge). (4) Create a flood inundation map for a given discharge. (5) Assess flood impact on buildings and infrastructure using GIS overlay.

#### Variant A: Original (US -- Onion Creek, Texas)

**Study area.** Onion Creek watershed, a tributary of the Colorado River near Austin, Texas. This area experienced severe flooding in October 2013 and May 2015.

**Data.** Download from: `http://www.caee.utexas.edu/prof/maidment/giswr2018/Ex5/Ex5Data.zip`

- `OnionHand.gdb` -- geodatabase containing NHDPlus flowlines, catchments, stream gages, and address points, all projected to UTM Zone 14N.
- `Onion3.tif` -- a 10 m DEM extracted to a 2 km buffer around the watershed, projected to UTM Zone 14N, hydrologically conditioned using TauDEM.

**Part 1: Compute HAND.**

1. Add the DEM, NHDFlowlines, and Catchments to a new map.
2. **Identify stream source points.** Use Feature Vertices to Points with Point Type = Dangling Vertex on the NHDFlowline layer. This identifies the upstream end of each stream segment.
3. **Rasterize source points.** Use Feature to Raster with field = StartFlag, cell size = 10, snapped to Onion3.tif. Reclassify NoData to 0 to create `Startrc.tif`.
4. **Hydrologic terrain analysis sequence:**
   - Fill the DEM
   - Flow Direction (D8) -- for stream delineation
   - Flow Accumulation with Startrc as weight raster (integer output)
   - Con tool: create stream raster where weighted accumulation >= 1
   - Flow Direction (DINF) -- for HAND computation
   - Flow Distance with DINF, distance type = Vertical, using the stream raster as target. **This produces the HAND raster.**
   - Stream Link, Watershed (catchments), Stream to Feature, Raster to Polygon

5. **Visualize HAND.** Symbolize the HAND raster using 5 classes with manual breaks at 2, 5, 10 m. Color the low HAND values (high flood risk) prominently.

**Part 2: Hydraulic Properties and Rating Curve.**

6. Select a specific NHDPlus catchment (FeatureID = 5781733, which was affected by severe flooding).
7. Identify the corresponding DEM-derived catchment polygon (CatchPoly). Export the HAND raster clipped to this polygon as `CatchHand.tif`.
8. For stage heights h = 1, 2, 4, 6, 8, 10, 12, 14 m, compute from the HAND raster:
   - Number of inundated cells (HAND < h)
   - Surface area = cells x 100 m^2
   - Volume = sum of (h - HAND) for all inundated cells x 100 m^2
   - Mean inundation depth = Volume / Surface area
   - Wetted perimeter from bed area and reach length
   - Cross-sectional area = Volume / Reach length
   - Hydraulic radius R = Cross-sectional area / Wetted perimeter
9. Compute discharge for each stage using Manning's equation: Q = (1/n) x A x R^(2/3) x S^(1/2), where n = 0.05 and S = bed slope from the DEM.
10. Plot the synthetic rating curve (stage vs. discharge).

**Part 3: Flood Inundation Mapping.**

11. From the rating curve, determine the flood stage corresponding to the estimated flood discharge for the October 2013 event (approximately 98,231 ft^3/s = 2,782 m^3/s at this reach).
12. Create a flood inundation depth raster: `Depth = Stage - HAND` for all cells where HAND < Stage.
13. Overlay the flood inundation map with the AddressPt feature class. Count the number of addresses inundated. Report the fraction of addresses affected.

**Deliverables.** (a) HAND raster map with classified symbology. (b) Table of hydraulic properties for each stage height. (c) Rating curve plot. (d) Flood inundation map for the design flood. (e) Count of affected addresses and flood impact assessment.

#### Variant B: International

**Study area.** A river reach in a flood-prone area of your country. Ideally choose a location where recent flooding has occurred and reference data (official flood maps, observed flood extents) are available for comparison.

**Data sources.**

- DEM: Copernicus DEM GLO-30 or, ideally, a national high-resolution DEM (LiDAR-derived, 1--5 m). The 30 m global DEM will work for a demonstration but is too coarse for detailed flood mapping.
- River network: HydroRIVERS or national hydrographic dataset.
- Building footprints: OpenStreetMap buildings (download via Geofabrik: https://download.geofabrik.de/), or Microsoft/Google open building footprints.
- Reference flood data: Copernicus Emergency Management Service (https://emergency.copernicus.eu/) provides rapid mapping products for recent flood events, including observed flood extents from satellite imagery.

**Procedure.**

1. Download and prepare the DEM. If using a 30 m DEM, note that HAND-based flood mapping will be approximate -- the method works best with DEMs of 10 m or finer.
2. Delineate streams from the DEM (use the procedure from Exercise 4).
3. Compute HAND using the same Fill > D8 Flow Direction > D8 Flow Accumulation (with stream seeds) > Stream Raster > DINF Flow Direction > DINF Flow Distance (Vertical) sequence.
4. Select a flood-prone reach. Compute hydraulic properties and a rating curve as in Variant A.
5. Estimate a design flood discharge (e.g., from published flood frequency analyses or regional regression equations). Determine the corresponding stage from the rating curve.
6. Create the flood inundation map. Overlay with building footprints from OpenStreetMap.
7. If available, compare your HAND-derived inundation extent with a satellite-observed flood extent from Copernicus EMS.

**Deliverables.** Same as Variant A, plus a comparison with observed/official flood maps if available.

#### Variant C: Hungarian

**Study area.** Sajo river near Miskolc, specifically the reach between Felsozsolca and the Tisza confluence. This area experienced severe flooding in June 2010 and May 2013.

**Data sources.**

- DEM: DDM-5 (5 m) from Lechner Tudastar is ideal. If unavailable, use the Copernicus DEM GLO-30 or EU-DEM (25 m) as a fallback.
- River network: EU-Hydro or OVF hydrographic database.
- Building footprints: OpenStreetMap buildings for Hungary (download from Geofabrik: https://download.geofabrik.de/europe/hungary.html). Use `osmfilter` or QGIS to extract building polygons.
- Official flood hazard maps: OVF publishes flood risk maps (arvizi kockazati terkepes) as required by the EU Floods Directive (2007/60/EC). These are available through the national water management geoportal.
- Coordinate system: EOV (EPSG:23700).
- Manning's n: For Hungarian lowland rivers, typical values are 0.03--0.05 for the main channel and 0.05--0.10 for floodplains.

**Procedure.**

1. Prepare the DEM. If using DDM-5 (already in EOV), extract to a 2 km buffer around the study reach. If using EU-DEM, reproject to EOV and resample to 10 m.
2. Identify stream sources and create a stream seed raster, following the same procedure as Variant A. Use the EU-Hydro or OVF flowline data to identify dangling vertices.
3. **Hydrologic terrain analysis:** Fill > D8 Flow Direction > D8 Flow Accumulation (with stream seeds) > Stream Raster (Con) > DINF Flow Direction > DINF Flow Distance (Vertical = HAND).
4. Classify HAND: 0--2 m (extremely high flood risk), 2--5 m (high), 5--10 m (moderate), >10 m (low). Overlay on a hillshade derived from the DEM.
5. Select a flood-prone reach (e.g., near Felsozsolca, where the Hernad joins the Sajo). Extract the HAND raster for this catchment.
6. Compute hydraulic properties for stage heights h = 1, 2, 3, 4, 5, 6, 8, 10 m. Apply Manning's equation with n = 0.04 and bed slope estimated from the DEM. Plot the rating curve.
7. For the design flood (e.g., the 2010 Sajo flood, estimated peak discharge ~1,200 m^3/s at Felsozsolca), determine the flood stage and create the inundation map.
8. Overlay with OpenStreetMap building footprints. Count affected structures.
9. **Comparison with official data.** Overlay your HAND-derived flood extent with the OVF official flood hazard map (arvizi kockazati terulet). Discuss agreements and discrepancies.

**Additional tasks.**

- Compute the HAND value at the Miskolc Water Treatment Plant (Miskolci Viztisztito Telep, approximately EOV Y~310,000, X~775,000). What flood stage would be required to inundate this critical infrastructure?
- The 2010 flood required emergency levee construction near Felsozsolca. Identify the levee locations on the DEM and discuss how levees affect HAND-based flood mapping.

**Deliverables.** (a) HAND raster map with classified symbology for the Sajo near Miskolc. (b) Table of hydraulic properties and rating curve. (c) Flood inundation map for the 2010 design flood. (d) Count of affected buildings. (e) Comparison with OVF official flood hazard map. (f) Discussion of HAND limitations in leveed floodplains.

---

### Summary of Data Sources by Variant

| Data Type | US (Original) | International | Hungarian |
|-----------|---------------|---------------|-----------|
| Administrative boundaries | US Census TIGER | Natural Earth | KSH / data.gov.hu |
| Watershed boundaries | NHDPlus WBD / HydroShare | HydroBASINS | OVF / HydroBASINS |
| River network | NHDPlus flowlines | HydroRIVERS | EU-Hydro / OVF |
| DEM | USGS 3DEP (1/3 arc-sec) | Copernicus GLO-30 / SRTM | DDM-5 / EU-DEM |
| Land cover | NLCD 30 m | ESA WorldCover 10 m | CORINE 100 m |
| Precipitation | NOAA GHCN / PRISM | ERA5-Land / CHIRPS | OMSZ / CARPATCLIM |
| Stream gages | USGS NWIS | GRDC | OVF |
| Flood forecasts | National Water Model | EFAS (Europe), GloFAS (global) | EFAS / OVF |
| Building footprints | Census address points | OpenStreetMap / MS Buildings | OpenStreetMap |
| Official flood maps | FEMA flood maps | National equivalents | OVF arvizi kockazati terkep |
| Coordinate system | NAD83 / UTM | WGS84 / UTM | HD72/EOV (EPSG:23700) |
