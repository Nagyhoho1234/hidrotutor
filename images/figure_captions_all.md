# Complete Figure Inventory

## Summary

| Metric | Count |
|--------|-------|
| Total figures | 168 |
| Figures with generation prompts | 168 |
| Figures without generation prompts | 0 |
| Figures with existing images in `images/book/` | 49 |
| Figures missing images | 119 |

---

## Chapter 1: Why Hidroinformatics Matters

*7 figures*

### Figure 1.1

**Caption:** Major global flood events (2000--2025). Circle size represents population affected; color intensity represents economic damage. The geographic distribution shows that no continent is immune, but low-lying river basins and coastal zones bear disproportionate risk.

**Generation prompt:** "Create a world map showing major flood events from 2000-2025, with color-coded circles indicating event severity (deaths, displacement, economic damage). Highlight the Danube Basin (2013), Ahr Valley Germany (2021), Pakistan (2010), Houston Texas (2017), and Bangladesh (2020). Include a legend showing circle size = people affected and color = economic damage. Style: clean vector illustration, white background, muted blue and red color palette, labeled locations."

**Existing image(s):** MISSING

### Figure 1.2

**Caption:** The four pillars of hidroinformatics. The discipline emerges at the intersection of hydrology, GIS, computational modeling, and data science/AI. Each pillar contributes essential capabilities; none is sufficient alone.

**Generation prompt:** "Create a Venn diagram showing four overlapping circles representing the four pillars of hidroinformatics: Hydrology (blue), GIS (green), Computational Modeling (orange), and Data Science/AI (purple). In the center overlap, place the word 'Hidroinformatics'. Around each circle, list 3-4 key capabilities: Hydrology (water balance, flow equations, precipitation-runoff, groundwater), GIS (spatial data, watershed delineation, mapping, geodatabases), Computational Modeling (simulation, forecasting, supercomputing, real-time systems), Data Science/AI (machine learning, big data, pattern recognition, automation). Style: clean vector illustration, white background, modern flat design, sans-serif labels."

**Existing image(s):** MISSING

### Figure 1.3

**Caption:** The three views of GIS. Left: the geodatabase organizes spatial data into structured, queryable collections. Center: geovisualization renders data as maps that reveal spatial patterns invisible in tabular form. Right: geoprocessing applies computational workflows to derive new datasets from existing ones.

**Generation prompt:** "Create a triptych illustration showing the three views of GIS. Left panel: 'Geodatabase' -- show a structured database icon with connected layers (rivers, watersheds, monitoring points) in an organized hierarchy. Center panel: 'Geovisualization' -- show a colorful interactive map with drought severity colors (green to red) over a country outline. Right panel: 'Geoprocessing' -- show a workflow diagram with input raster (DEM) flowing through processing steps (flow direction, flow accumulation, watershed delineation) to output polygons. Each panel should be labeled clearly. Style: clean vector illustration, white background, consistent color palette (blue, green, orange), minimal design."

**Existing image(s):** `fig_01_03_a.png, fig_01_03_b.png, fig_01_03_c.png`

### Figure 1.4

**Caption:** The four basic water problems and their interconnection through a unifying information framework. Each problem requires spatial data, modeling, and visualization -- capabilities provided by the GIS-based hidroinformatics approach.

**Generation prompt:** "Create a diagram showing the four basic water problems arranged around a central GIS/Information Framework hub. Four panels surround the center: Top-left: 'Too Much Water (Flooding)' with an icon of a flooded house and rising river. Top-right: 'Not Enough Water (Drought)' with an icon of cracked dry earth and a depleted reservoir. Bottom-left: 'Too Dirty (Pollution)' with an icon of contaminated water with warning symbols. Bottom-right: 'Ecosystem Health' with an icon of a healthy river with fish and riparian vegetation. Arrows connect all four panels to the central hub, and dashed lines connect them to each other, indicating interconnection. Style: clean vector illustration, white background, consistent blue/brown/green color palette, labeled clearly."

**Existing image(s):** `fig_01_04_a.jpg, fig_01_04_b.jpg, fig_01_04_c.jpg, fig_01_04_d.png`

### Figure 1.5

**Caption:** NDVI vegetation index for Texas in September 2010 (left, pre-drought) and September 2011 (right, peak drought). The dramatic shift from green to brown across the state reveals the spatial extent and severity of the drought's impact on vegetation.

**Generation prompt:** "Create a side-by-side comparison map of Texas showing NDVI (vegetation greenness) in September 2010 (left, mostly green) and September 2011 (right, mostly brown/red). Use a color scale from dark green (NDVI 0.7+, healthy vegetation) through yellow (0.4) to dark brown/red (NDVI <0.2, severe drought stress). Include a color bar legend. Show state boundaries and major rivers (Colorado, Brazos, Trinity, Rio Grande) as thin blue lines. Title each panel with its date. Style: clean cartographic illustration, white background, professional color ramp."

**Existing image(s):** `fig_01_05.png`

### Figure 1.6

**Caption:** Progression of the June 2013 Danube flood wave from Passau to Budapest. The flood wave traveled more than 700 km in approximately one week, with peak water levels exceeding historical records at multiple locations. The geographic scope of the event -- spanning four countries -- demonstrates why transboundary flood forecasting (EFAS) is essential.

**Generation prompt:** "Create a map of the Danube River basin from Germany to Hungary, showing the progression of the June 2013 flood wave. Mark key cities (Passau, Vienna, Bratislava, Budapest, Mohacs) with red circles sized by peak water level. Show the Danube as a thick blue line with tributaries (Inn, Drava, Tisza). Include a timeline arrow along the bottom showing flood wave travel: Passau (June 2-3), Vienna (June 5), Bratislava (June 6), Budapest (June 9-10). Color the upstream catchment area (Alps, Bohemia) in a blue wash indicating the rainfall source region. Style: clean cartographic illustration, white background, blue river features, red flood markers, timeline bar at bottom."

**Existing image(s):** MISSING

### Figure 1.7

**Caption:** Structure of the book. The six parts follow the logical progression from foundational concepts (Parts I--II) through surface water analysis (Parts III--IV) to groundwater (Part V) and artificial intelligence (Part VI). Each part builds on the capabilities developed in the preceding parts.

**Generation prompt:** "Create a visual roadmap of the book's six parts. Use a flow diagram moving from left to right (or top to bottom). Part I: 'The Water Information Landscape' (Chapters 1-4) shown as a foundation block in blue. Part II: 'Reading the Landscape' (Ch 5-8) shown above/right in green as a grid/raster block. Part III: 'Following the Water Downhill' (Ch 9-12) shown with a stream network icon in blue. Part IV: 'When Water Becomes Dangerous' (Ch 13-17) shown with a flood wave icon in red. Part V: 'The Hidden Water' (Ch 18-21) shown with an underground/subsurface cross-section icon in brown. Part VI: 'The Intelligent Water System' (Ch 22-25) shown with a brain/AI icon in purple. Arrows connect each part to the next, showing the logical progression. Style: clean vector illustration, white background, modern flat design, labeled parts and chapter ranges."

**Existing image(s):** MISSING

---

## Chapter 2: Mapping Water: From Paper to Pixels

*8 figures*

### Figure 2.1

**Caption:** The three reference surfaces of geodesy. The physical Earth surface is irregular. The geoid (blue dashed line) is the equipotential surface of gravity that approximates mean sea level. The ellipsoid (red line) is a smooth mathematical approximation. Orthometric height H is measured from the geoid; ellipsoidal height h is measured from the ellipsoid; the geoid undulation N is their difference (h = H + N).

**Generation prompt:** "Create a technical cross-section diagram showing three surfaces: the irregular physical Earth surface (mountains, valleys), the smooth but undulating geoid surface (dashed blue line labeled 'Geoid'), and the regular mathematical ellipsoid (smooth red line labeled 'Ellipsoid'). Show the geoid undulation N as the vertical distance between ellipsoid and geoid, and orthometric height H as the distance from geoid to Earth surface. Show ellipsoidal height h as the distance from ellipsoid to Earth surface. Label the relationship h = H + N. Style: clean vector illustration, white background, labeled dimensions."

**Existing image(s):** `fig_02_01.png`

### Figure 2.2

**Caption:** The global patchwork of geodetic datums. WGS84 (used by GPS) is global; regional and national datums provide higher local accuracy but must be transformed before data from different datums can be combined. The trend is toward geocentric datums compatible with WGS84.

**Generation prompt:** "Create a world map showing the approximate coverage areas of major geodetic datums: WGS84 (global, light overlay), NAD83 (North America, blue), ETRS89 (Europe, green), HD72 (Hungary, orange dot/small area), Pulkovo 1942 (former Soviet Union, pink), Indian datum (South Asia, yellow). Use a Robinson or Mollweide equal-area projection. Label each datum. Style: clean vector illustration, white background, political borders in light gray."

**Existing image(s):** MISSING

### Figure 2.3

**Caption:** Vertical datums across Europe. The Baltic Height System (used in Hungary) and the Amsterdam Ordnance Datum (NAP, used in the Netherlands) reference different tide gauges. The same physical point has different elevation values in each system. The European Vertical Reference Frame (EVRF) aims to unify these into a single consistent system.

**Generation prompt:** "Create a diagram showing the concept of vertical datums for different countries. Show a schematic cross-section from the Atlantic Ocean through Europe. Mark the Kronstadt tide gauge (Baltic Height System zero), the Amsterdam tide gauge (NAP zero), and a point in Hungary showing how the same physical elevation has different numerical values depending on which vertical datum is used. Show the geoid as a reference surface connecting the tide gauges. Style: clean vector illustration, white background, labeled components."

**Existing image(s):** `fig_02_03.png`

### Figure 2.4

**Caption:** The three families of map projections. Left: conic (cone intersects globe along standard parallels, best for mid-latitude east-west regions). Center: cylindrical in transverse orientation (cylinder tangent along a meridian, best for north-south strips). Right: azimuthal (plane tangent at a point, best for polar or circular regions). Each family produces characteristic distortion patterns.

**Generation prompt:** "Create a diagram showing the three main projection families side by side: (1) Conic - a cone placed over a globe, with two standard parallels marked; (2) Cylindrical - a cylinder wrapped around a globe in transverse orientation, tangent along a meridian; (3) Azimuthal - a flat plane tangent to the globe at the North Pole. Below each, show the resulting flat map shape when the surface is unrolled/flattened. Label each projection family. Style: clean vector illustration, white background, three panels in a row."

**Existing image(s):** `fig_02_04.png`

### Figure 2.5

**Caption:** The Hungarian EOV coordinate system (EPSG:23700). The projection center near Szolnok, the coordinate grid, and selected city locations are shown. Easting values range from about 421,000 to 950,000; Northing values from about 44,000 to 367,000. Note that Hungarian datasets may swap the X/Y labels -- always identify by value range.

**Generation prompt:** "Create a map of Hungary showing the EOV coordinate system grid. Show the country outline with major rivers (Danube, Tisza). Mark the projection center point at 47.14N, 19.05E (near Szolnok). Show a coordinate grid with Easting values from 400,000 to 950,000 on the x-axis and Northing values from 50,000 to 360,000 on the y-axis. Label Budapest, Debrecen, Szeged, and Szolnok with their approximate EOV coordinates. Include a note: 'EPSG:23700'. Style: clean vector illustration, white background, rivers in blue, grid lines in light gray."

**Existing image(s):** MISSING

### Figure 2.6

**Caption:** The GRACE satellite mission measures changes in Earth's gravity field to detect variations in water storage. Two satellites fly 220 km apart; their inter-satellite distance changes by micrometers as they pass over regions of higher or lower gravity (caused by variations in water mass). Monthly maps of terrestrial water storage anomalies reveal droughts, floods, and long-term groundwater depletion at continental scales.

**Generation prompt:** "Create a diagram showing the GRACE satellite mission concept. Show two satellites flying in tandem over the Earth at ~500 km altitude, with a microwave link between them. Below, show a cross-section of the Earth's surface with varying water storage (full aquifer causing higher gravity, depleted aquifer causing lower gravity). Use arrows to show how the inter-satellite distance changes as they pass over mass anomalies. Include a small inset showing a monthly GRACE terrestrial water storage anomaly map of Europe with color scale from -20 cm to +20 cm equivalent water height. Style: clean technical illustration, white background, satellites in gray, Earth surface in brown/green, water in blue."

**Existing image(s):** `fig_02_06.png`

### Figure 2.7

**Caption:** Practical workflow for combining spatial data from multiple sources with different coordinate systems. Every hydroinformatics project should begin with a coordinate system inventory, proceed through a deliberate choice of working CRS, reproject all data, and verify alignment before analysis.

**Generation prompt:** "Create a flowchart diagram showing the practical workflow for combining multi-source spatial data: Step 1: Inventory datasets and CRS (list of datasets with their EPSG codes). Step 2: Choose working CRS (decision: national analysis -> national CRS; continental -> continental CRS; global -> WGS84/UTM). Step 3: Reproject all data to working CRS (arrows showing transformations). Step 4: Verify alignment (overlay check). Step 5: Proceed with analysis. Use boxes for steps, arrows for flow, and color-coding for different source CRS types (national=orange, European=green, global=blue). Style: clean vector illustration, white background."

**Existing image(s):** MISSING

### Figure 2.8

**Caption:** Conceptual summary of Chapter 2. The three reference surfaces (physical surface, geoid, ellipsoid) are the foundation for geographic and projected coordinate systems, vertical datums, and satellite gravity missions. Every country implements these concepts through its own datum and projection choices.

**Generation prompt:** "Create a conceptual summary diagram for Chapter 2. Show the Earth at center with three concentric layers: the physical surface (outermost, irregular), the geoid (middle, smooth but undulating, blue), and the ellipsoid (innermost, perfectly smooth, red). Arrows point outward to four satellite boxes: (1) 'Geographic CRS' showing latitude/longitude grid, (2) 'Projected CRS' showing a flat map with grid, (3) 'Vertical datums' showing tide gauges and height measurements, (4) 'GRACE' showing satellites measuring gravity. Each box has small icons representing the concept. At the bottom, show three national flags (US, Hungary, EU) with their respective datum names (NAD83, HD72, ETRS89). Style: clean infographic, white background, professional colors."

**Existing image(s):** MISSING

---

## Chapter 3: Where the Data Lives

*6 figures*

### Figure 3.1

**Caption:** The three-tier water data landscape. US federal agencies (blue) provide the most comprehensive national coverage; EU programmes (green) offer continent-wide alternatives; global datasets (orange points) fill gaps elsewhere. The practical challenge for any project is knowing which tier to access for each data type.

**Generation prompt:** "Create a world map diagram showing the three tiers of water data infrastructure. The United States is highlighted in blue with labels for USGS, NOAA, NHDPlus. Europe is highlighted in green with labels for Copernicus, ECMWF, EEA. The rest of the world shows scattered points representing global datasets like HydroSHEDS, CHIRPS, GPM, SoilGrids. Arrows connect the tiers showing data flow. Style: clean vector illustration, white background, muted professional colors."

**Existing image(s):** MISSING

### Figure 3.2

**Caption:** River network representations at three scales of data infrastructure. Left: NHDPlus in the Little Bear Logan watershed (US), with ~2,700 reach catchments per HUC-8. Centre: EU-Hydro in the Zala River watershed (Hungary). Right: HydroRIVERS in the lower Mekong. All three datasets serve the same fundamental purpose but reflect different institutional traditions and source data.

**Generation prompt:** "Create a three-panel comparison showing river network data for the same approximate scale: Left panel: NHDPlus network in a US watershed (e.g., Little Bear River, Utah) showing dense blue stream lines with COMID labels. Center panel: EU-Hydro network in Hungary (e.g., Zala River watershed flowing into Lake Balaton) showing blue stream lines. Right panel: HydroSHEDS/HydroRIVERS network in a tropical watershed (e.g., Mekong delta) showing blue stream lines. Each panel has a title bar. Style: clean cartographic, white background, consistent scale bars."

**Existing image(s):** `fig_03_02.png`

### Figure 3.3

**Caption:** Four complementary precipitation datasets for Hungary, illustrating the trade-off between spatial resolution, temporal extent, and data source type. ERA5 (top-left) provides model-based global coverage. E-OBS (top-right) provides station-interpolated European coverage. CARPATCLIM (bottom-left) provides high-resolution regional coverage for 1961-2010. OMSZ stations (bottom-right) provide point observations at the highest temporal resolution.

**Generation prompt:** "Create a comparison panel showing four precipitation datasets covering Hungary. Top-left: ERA5 reanalysis at ~31 km grid showing smooth precipitation field over the Carpathian Basin. Top-right: E-OBS at 0.1 degree showing station-interpolated precipitation with more spatial detail. Bottom-left: CARPATCLIM at 0.1 degree showing the same region for historical period. Bottom-right: OMSZ station network showing 136 point locations over Hungary with a Thiessen polygon overlay. Each panel labeled with dataset name, resolution, and time coverage. Style: clean scientific figure, consistent color scale (blue gradient for precipitation), white background."

**Existing image(s):** MISSING

### Figure 3.4

**Caption:** The satellite data ecosystem for water resources. Satellites (top) produce raw observations; processing platforms (middle) provide access and computing; derived products (bottom) feed into hydrological analysis. Google Earth Engine bridges all sources, hosting data from both US and European missions.

**Generation prompt:** "Create a schematic diagram of the satellite data ecosystem for water resources. At the top, show satellite icons: Landsat, Sentinel-1, Sentinel-2, MODIS, GRACE, GPM. Below each, show the data type it provides (optical, SAR, gravity, precipitation). In the middle, show three processing platforms: NASA Earthdata (US), Copernicus Data Space (EU), Google Earth Engine (Global). At the bottom, show derived products: land cover, flood maps, soil moisture, water storage, precipitation grids. Arrows connect satellites to platforms to products. Style: clean flowchart, professional colors, white background."

**Existing image(s):** MISSING

### Figure 3.5

**Caption:** Completed watershed base maps for the Little Bear Logan watershed (US, left) and the Zala River watershed (Hungary, right). Both maps contain the same fundamental layers -- watershed boundary, sub-watersheds, stream network, and gauge locations -- assembled from different data sources but serving the same analytical purpose.

**Generation prompt:** "Create a side-by-side comparison of two watershed base maps. Left panel: Little Bear Logan watershed (Utah, USA) showing HUC-8 boundary (black outline), HUC-12 sub-watersheds (colored polygons), NHDPlus flow lines (blue, graduated width by flow), and USGS gauge locations (red triangles). Right panel: Zala River watershed (Hungary) showing watershed boundary (black outline), EU-Hydro stream network (blue, graduated width by stream order), Copernicus DEM hillshade background, Lake Balaton visible at the southeastern edge, and OVF gauge locations (red triangles). Both panels have scale bars, north arrows, and consistent styling. Style: clean cartographic, professional colors, white background."

**Existing image(s):** MISSING

### Figure 3.6

**Caption:** Decision flowchart for selecting water data sources by study area and data type. For each combination of region and data need, the recommended dataset is indicated. Google Earth Engine (bottom) provides a unified platform that hosts data from all three tiers.

**Generation prompt:** "Create a decision flowchart for selecting water data sources. Start with 'What is your study area?' branching to 'United States', 'Europe/Hungary', and 'Other'. Each branch leads to data type questions (DEM, river network, precipitation, etc.) with the recommended dataset for each combination. US branch points to NED/3DEP, NHDPlus, PRISM, etc. Europe branch points to Copernicus DEM, EU-Hydro, ERA5/E-OBS, etc. Other branch points to SRTM/GLO-30, HydroSHEDS, CHIRPS/GPM, etc. Final box at bottom: 'For any region: Google Earth Engine hosts most of these.' Style: clean flowchart, professional colors, white background."

**Existing image(s):** MISSING

---

## Chapter 4: GIS as a Water Tool

*6 figures*

### Figure 4.1

**Caption:** The three views of GIS applied to water resources. The geodatabase (left) organizes and stores spatial data with enforced relationships. Geovisualization (center) transforms data into interpretable maps and displays. Geoprocessing (right) performs spatial analysis to derive new information. The power of GIS lies in the seamless integration of all three views.

**Generation prompt:** "Create a triptych diagram showing the three views of GIS for water resources. Left panel labeled 'Geodatabase' shows a database schema icon with connected tables for streams, watersheds, gauges, and DEMs. Center panel labeled 'Geovisualization' shows a colorful watershed map with streams in blue, elevation shading, and gauge points. Right panel labeled 'Geoprocessing' shows a flowchart: DEM → Flow Direction → Flow Accumulation → Watershed. Arrows connect all three panels to show integration. Style: clean vector illustration, white background, blue-green color scheme, professional technical diagram."

**Existing image(s):** `fig_04_01_a.png, fig_04_01_b.png, fig_04_01_c.png`

### Figure 4.2

**Caption:** The GIS ecosystem for water resources in 2026. Desktop GIS (center) remains the analytical core, but server, cloud, and mobile platforms extend capabilities across the entire workflow -- from planetary-scale analysis in the cloud to georeferenced field data collection on a smartphone.

**Generation prompt:** "Create a diagram showing the GIS ecosystem for water resources in 2026. Four concentric rings: innermost ring labeled 'Desktop' showing ArcGIS Pro and QGIS icons with a computer monitor. Second ring labeled 'Server' showing database and web service icons. Third ring labeled 'Cloud' showing Google Earth Engine, Planetary Computer, and ArcGIS Online logos with cloud symbols. Outermost ring labeled 'Mobile' showing smartphone and tablet icons with GPS symbols. Arrows show data flow between all rings. A water drop icon sits at the center. Style: clean vector illustration, white background, blue gradient color scheme."

**Existing image(s):** MISSING

### Figure 4.3

**Caption:** Structure of a geodatabase for a water resources project. The feature dataset groups vector layers (streams, watersheds, gauges) under a common coordinate system. Raster datasets (DEM, land cover) are stored alongside. Tables hold non-spatial data (discharge records) linked to spatial features through relationships.

**Generation prompt:** "Create a hierarchical diagram showing the structure of a geodatabase for water resources. At the top, a cylinder labeled 'File Geodatabase'. Below it, three branches: (1) a 'Feature Dataset' box containing feature class icons for Streams (polyline), Watersheds (polygon), and Gauges (point); (2) standalone 'Raster Dataset' icons labeled DEM and Land Cover; (3) a 'Table' icon labeled Discharge Records. Dashed lines show relationships between Gauges and Discharge Records. Each feature class box shows sample attribute columns. Style: clean vector illustration, white background, labeled components, blue-green color scheme."

**Existing image(s):** `fig_04_03.png`

### Figure 4.4

**Caption:** The same watershed represented in vector format (left) and raster format (right). Vector features preserve geometric precision but require complex spatial algorithms. Raster representation approximates geometry with square cells but enables efficient cell-by-cell computation. Water resources analysis routinely converts between representations as workflows demand.

**Generation prompt:** "Create a side-by-side comparison showing the same watershed represented in vector and raster formats. Left panel (vector): shows a watershed polygon outline with internal stream lines in blue and gauge points as red dots, with clean geometric edges. Right panel (raster): shows the same watershed as a grid of colored cells -- watershed area in light green cells, stream cells in blue, gauge cells in red, with visible staircase edges along the boundary. Both panels labeled. A legend shows the feature types. An arrow between panels is labeled 'Convert'. Style: clean technical illustration, white background, clear grid lines on raster side."

**Existing image(s):** `fig_04_04_a.gif, fig_04_04_b.gif`

### Figure 4.5

**Caption:** A watershed base map of the Zala River catchment, western Hungary. The hillshaded DEM reveals terrain structure; blue stream lines (width proportional to order) show the drainage network; red triangles mark gauging stations; the thick black outline defines the watershed boundary. Lake Balaton is visible at the eastern outlet. This base map provides the geographic foundation for all subsequent hydrological analysis.

**Generation prompt:** "Create a watershed base map of the Zala River watershed in western Hungary. Show the watershed boundary as a thick black outline. Inside, display a hillshaded terrain background with subtle elevation coloring (green lowlands, brown hills). Overlay blue stream lines with varying widths representing stream order. Show 3-4 red triangle symbols for gauge stations with small labels. Lake Balaton should be visible as a large blue waterbody at the eastern edge. Include a small inset map showing Hungary with the watershed location highlighted. Add standard map elements: north arrow, scale bar, title 'Zala River Watershed'. Style: clean cartographic illustration, professional map layout, white border."

**Existing image(s):** MISSING

### Figure 4.6

**Caption:** The relationship between GIS and hydrological modeling. GIS platforms (bottom) provide spatial data management and analysis. Hydrological models (top) perform physical simulations. The data processing layer (middle) translates between them -- extracting model parameters from spatial data and visualizing model results as maps. Python scripting (right) provides automation that spans all layers.

**Generation prompt:** "Create a layered diagram showing the relationship between GIS and hydrological modeling. Bottom layer labeled 'GIS Platform' shows icons for ArcGIS Pro, QGIS, and Google Earth Engine. Middle layer labeled 'Data Processing' shows arrows representing terrain analysis, parameter extraction, and spatial overlay. Top layer labeled 'Hydrological Models' shows model names: HEC-HMS, HEC-RAS, SWAT, MODFLOW. Bidirectional arrows between layers labeled 'Inputs' (upward) and 'Results Visualization' (downward). A side column labeled 'Python Scripting' spans all three layers with a snake icon. Style: clean vector illustration, white background, blue-green professional color scheme."

**Existing image(s):** MISSING

---

## Chapter 5: The Grid: How Computers See Terrain

*8 figures*

### Figure 5.1

**Caption:** Three numerical representations of the same river valley terrain. The regular grid (left) uses uniform square cells, each storing an elevation value. The TIN (center) concentrates triangles where terrain is complex and spaces them widely on flat areas. The contour-flowline model (right) uses lines of constant elevation and perpendicular flow paths. For hydrological GIS, the regular grid dominates due to its computational simplicity and compatibility with standard analysis tools.

**Generation prompt:** "Create a technical diagram showing three representations of the same terrain surface side by side. Left panel: a regular grid (raster) with square cells colored by elevation using a blue-to-brown color ramp, showing a river valley running diagonally. Center panel: a triangulated irregular network (TIN) of the same terrain, with triangles denser along the valley and ridgeline, sparser on flat areas. Right panel: a contour-flowline model with contour lines (brown) and perpendicular flowlines (blue arrows) showing the same terrain. Labels: 'Regular Grid', 'TIN', 'Contour-Flowline'. Style: clean vector illustration, white background, labeled, professional technical diagram."

**Existing image(s):** `fig_05_01.png`

### Figure 5.2

**Caption:** The six defining elements of a grid data structure. Every grid is completely specified by its extent (bounding coordinates), cell size, number of rows and columns, anchor point coordinates, NODATA value, and data type. Understanding these elements is essential for creating, interpreting, and combining raster datasets.

**Generation prompt:** "Create an annotated diagram of a grid data structure showing all six defining elements. Show a rectangular grid of cells (approximately 8 columns x 6 rows) overlaid on a faint map background. Label the following: (1) 'Extent' with dimension arrows showing the bounding box, (2) 'Cell Size' with a magnified single cell showing its dimensions, (3) 'Rows and Columns' with index numbers along the edges, (4) 'Anchor Point' with a pin/marker at the lower-left corner showing (xmin, ymin) coordinates, (5) 'NODATA' cells shaded in gray along the bottom-right to represent an irregular study area boundary, (6) 'Cell Values' showing decimal numbers in a few cells (e.g., 234.7, 228.3, 215.1) representing elevation. Style: clean vector illustration, white background, blue and brown color scheme, professional technical diagram with clear labels and callout arrows."

**Existing image(s):** MISSING

### Figure 5.3

**Caption:** Three interpretations of grid cell values (after Goodchild, 1997). Left: the value represents the spatial average over the entire cell footprint. Center: the value is a point sample at the cell center. Right: the value is associated with grid nodes (cell corners). The correct interpretation affects how the data should be used in analysis and what resampling method is appropriate.

**Generation prompt:** "Create a diagram showing three panels illustrating different interpretations of raster cell values. Left panel labeled 'Spatial Average': show a 3x3 grid where each cell is uniformly shaded in a single color representing the average value, with the value written in the center. Center panel labeled 'Center Point Sample': show the same 3x3 grid but with dots at each cell center and the value next to each dot, with dashed lines suggesting the value varies across the cell. Right panel labeled 'Grid Node': show the same area but values are at the cell corners (intersections of grid lines), not centers. Below each panel, show a small cross-section diagram indicating how the true surface relates to the stored values. Style: clean vector illustration, white background, educational technical diagram."

**Existing image(s):** MISSING

### Figure 5.4

**Caption:** Two rules for converting vector polygons to raster format. The center point rule (left) assigns each cell based on which polygon contains its center, sometimes misrepresenting cells whose center falls in a narrow sliver. The largest share rule (right) assigns based on the polygon occupying the largest fraction of the cell, producing a more representative result but requiring more computation.

**Generation prompt:** "Create a diagram comparing the center-point rule and largest-share rule for rasterizing a polygon feature. Show a vector polygon (irregular shape, outlined in bold black) overlaid on a grid of 6x6 cells. Left panel labeled 'Center Point Rule': cells whose centers fall inside the polygon are shaded blue; cells whose centers fall outside are white. Some cells that are mostly inside the polygon but have centers outside are shown in white with an X marking the center. Right panel labeled 'Largest Share Rule': cells where more than 50% of the area is inside the polygon are shaded blue. Show the difference: some edge cells that were white in the left panel are blue in the right panel, and vice versa. Style: clean vector illustration, white background, educational technical diagram."

**Existing image(s):** MISSING

### Figure 5.5

**Caption:** Floating-point versus integer grids. The floating-point grid (left) stores continuous elevation values visualized with a color ramp. The integer grid (right) stores categorical land cover codes linked to a Value Attribute Table that provides descriptive labels and derived attributes. Both are valid raster representations, but they serve fundamentally different purposes.

**Generation prompt:** "Create a side-by-side comparison of a floating-point grid and an integer grid for the same area. Left panel labeled 'Floating-Point Grid (Elevation DEM)': show a 5x5 grid with decimal values (e.g., 234.7, 228.3, 215.1, etc.) colored with a continuous blue-green-brown elevation color ramp. No attribute table. Right panel labeled 'Integer Grid (Land Cover)': show the same 5x5 area with integer values (1, 2, 3, etc.) colored with distinct categorical colors (green for forest, yellow for cropland, gray for urban, blue for water). Below the right panel, show a small Value Attribute Table linking integers to land cover names and cell counts. Style: clean vector illustration, white background, professional technical diagram with clear labels."

**Existing image(s):** MISSING

### Figure 5.6

**Caption:** The scale triplet (after Bloschl, 1995). Extent is the total domain covered by the data. Spacing is the distance between successive measurements. Support is the footprint over which each measurement is representative. Together, these three properties determine what a dataset can and cannot tell us about the underlying phenomenon.

**Generation prompt:** "Create a diagram illustrating the three components of the scale triplet (Bloschl, 1995) applied to a spatial measurement series. Show a horizontal axis representing distance. Along this axis, place a series of evenly spaced measurement points. Label three quantities with arrows: (1) 'Extent' as a long double-headed arrow spanning the entire measurement series, (2) 'Spacing' as a shorter double-headed arrow between two adjacent measurement points, (3) 'Support' as a small shaded rectangle around each measurement point indicating the footprint of each measurement. Below, show a wavy line representing the true continuous field, with the measurement points sampling it. Show how the extent limits what can be observed, the spacing determines detail, and the support determines smoothing. Style: clean vector illustration, white background, educational technical diagram with clear labels."

**Existing image(s):** MISSING

### Figure 5.7

**Caption:** Evolution of raster formats in hydrological GIS. The GeoTIFF has become the universal standard for single-time-step spatial data, with the Cloud-Optimized GeoTIFF extending it for web and cloud access. NetCDF dominates for multi-dimensional and time-series data. Legacy formats (ESRI Grid, ASCII Grid) remain in use but are not recommended for new work.

**Generation prompt:** "Create a diagram showing the evolution and relationships between raster formats used in hydrology. Show a timeline from left to right: ESRI Grid (1980s-1990s) → ASCII Grid (simple interchange) → GeoTIFF (2000s standard) → Cloud-Optimized GeoTIFF (2020s cloud standard). In a parallel track below, show: HDF (NASA) → NetCDF (climate science) → NetCDF-4/HDF5 (converged). Arrows show the progression. Each format box contains a small icon: folder icon for ESRI Grid, text file icon for ASCII, image icon for GeoTIFF, cloud icon for COG, cube icon for NetCDF. Style: clean vector illustration, white background, timeline layout, professional technical diagram."

**Existing image(s):** MISSING

### Figure 5.8

**Caption:** The same Tisza River floodplain section represented at four DEM resolutions. At 90 meters, the floodplain appears almost featureless. At 30 meters, the river channel emerges. At 5 meters, levees and oxbow lakes become visible. At 1 meter, full engineering detail is captured. The choice of resolution must match the application: regional assessment (30-90 m), operational forecasting (5 m), or engineering design (1 m).

**Generation prompt:** "Create a multi-panel diagram showing the same stretch of Tisza River floodplain at different DEM resolutions. Four panels arranged in a 2x2 grid: Top-left: '90 m (GLO-90)' showing a very smooth, almost featureless floodplain with the river barely visible as a shallow depression. Top-right: '30 m (GLO-30)' showing the river channel more clearly and some suggestion of levees. Bottom-left: '5 m (DDM-5)' showing clear levees, oxbow lakes, and floodplain depressions. Bottom-right: '1 m (LiDAR)' showing full detail including levee crest, individual field boundaries, drainage ditches, and road embankments. Each panel should use the same blue-green-brown elevation color ramp. Style: clean illustration showing progressive terrain detail, white background between panels, professional technical diagram."

**Existing image(s):** MISSING

---

## Chapter 6: Calculating with Maps

*6 figures*

### Figure 6.1

**Caption:** The role of map algebra in distributed hydrological modeling. Multiple input grids representing spatially variable quantities -- precipitation, soil properties, land cover -- are combined through algebraic expressions to produce output grids such as runoff depth. These outputs can then feed downstream analyses like flow accumulation and discharge estimation.

**Generation prompt:** "Create a conceptual diagram showing the hydrological application of map algebra. Three input raster grids are shown at top: a Precipitation grid (blue color ramp), a Soil Infiltration Capacity grid (brown color ramp), and a Land Cover grid (green categorical colors). Arrows lead down to a central 'Map Algebra Engine' box containing the equation R = P - f(Soil, LandCover). An arrow leads from this box down to an output Runoff grid (red-to-blue color ramp). Below the runoff grid, another arrow leads to a 'Flow Accumulation' box, then to a 'Stream Discharge' map. Style: clean vector illustration, white background, labeled components, professional technical diagram."

**Existing image(s):** MISSING

### Figure 6.2

**Caption:** Two input grids with different cell sizes overlaid on the same geographic area. The precipitation grid (thick blue lines, 150 m cells) contains four cells, while the infiltration grid (thin red lines, 100 m cells) contains nine cells. Before any map algebra operation can proceed, the software must reconcile these grids to a common cell size.

**Generation prompt:** "Create a technical diagram showing two overlaid grids with different cell sizes. The larger grid (2x2, 150m cells) is drawn with thick blue lines and contains the values 4, 6, 3.1, 4 in its cells. The smaller grid (3x3, 100m cells) is drawn with thinner red lines and contains the values 2.2, 3, 4, 1.8, 2.5, 3.5, 1.5, 2, 2.7 in its cells. Both grids share the same lower-left corner at (0,0). The 150m grid extends to (300,300) and the 100m grid also extends to (300,300). Dimension labels show 150m and 100m cell sizes. The grids are semi-transparent so both are visible simultaneously. Style: clean vector illustration, white background, labeled dimensions and cell values, grid lines clearly distinguishable."

**Existing image(s):** MISSING

### Figure 6.3

**Caption:** The three critical analysis environment parameters. The analysis extent controls the geographic bounds of the calculation (defaulting to the intersection of inputs). The analysis cell size controls the output resolution (defaulting to the coarsest input). The snap raster controls cell alignment (ensuring output cells line up with a reference grid).

**Generation prompt:** "Create a diagram illustrating the three key analysis environment parameters for raster calculations. Show three panels arranged vertically. Panel 1 (Analysis Extent): two overlapping rectangles representing different input extents, with the intersection area highlighted in green and labeled 'default: intersection.' Panel 2 (Analysis Cell Size): two grids of different cell sizes side by side, with an arrow pointing to the coarser grid labeled 'default: maximum (coarsest).' Panel 3 (Snap Raster): two grids of the same cell size but with offset alignment, and a corrected version where they are aligned, labeled 'snap raster ensures alignment.' Style: clean vector illustration, white background, minimal colors (blue and green), labeled annotations."

**Existing image(s):** MISSING

### Figure 6.4

**Caption:** Bilinear resampling of the 150 m precipitation grid to 100 m resolution. Corner values are preserved, while intermediate values are linearly interpolated. The center value (4.275) is the distance-weighted average of all four original cells.

**Generation prompt:** "Create a side-by-side diagram showing bilinear resampling of a precipitation grid. Left panel: a 2x2 grid at 150m resolution with values 4, 6, 3.1, 4 displayed in each cell, labeled 'Original (150m).' Right panel: a 3x3 grid at 100m resolution with values 4, 5, 6, 3.55, 4.275, 5, 3.1, 3.55, 4 displayed in each cell, labeled 'Resampled (100m).' Between the two panels, curved arrows show how the corner values are preserved (4→4, 6→6, 3.1→3.1, 4→4) and how the intermediate values are interpolated (5.0 = average of 4 and 6, 3.55 = average of 3.1 and 4, 4.275 = average of all four). Use a blue color ramp in both grids where darker blue means higher values. Style: clean vector illustration, white background, clearly labeled values and dimensions."

**Existing image(s):** MISSING

### Figure 6.5

**Caption:** A complete map algebra workflow for the Zala River catchment in Hungary. Three input datasets at different resolutions and projections are reconciled to a common geometry before map algebra computes an excess precipitation grid. The catchment boundary serves as the analysis mask.

**Generation prompt:** "Create a workflow diagram showing a map algebra application for the Zala River catchment in Hungary. At the top, three input boxes: 'OMSZ Radar Precipitation (1 km, EOV)' with a blue rain icon, 'AGROTOPO Soil Map (100 m, EOV)' with a brown soil icon, and 'CORINE Land Cover (100 m, ETRS89)' with a green land icon. Arrows lead to a central box labeled 'Reconciliation: project to EOV, resample to 100 m, clip to catchment.' Below this, an arrow leads to 'Raster Calculator: Runoff = f(P, Soil, Land Cover).' Below that, an arrow leads to a final output: 'Excess Precipitation Grid (100 m, EOV)' overlaid on an outline of the Zala catchment with Lake Balaton at the bottom. Style: clean vector illustration, white background, professional diagram, labeled components."

**Existing image(s):** MISSING

### Figure 6.6

**Caption:** The complete raster calculation workflow, from question definition through documentation. Verification steps (6 and 8) include feedback loops for correcting issues discovered during inspection. The disciplined progression through these steps prevents the subtle errors that are common in multi-resolution raster analysis.

**Generation prompt:** "Create a vertical flowchart showing the complete raster calculation workflow with 9 steps. Each step is a rounded rectangle. Step 1: 'Define the Question' (light gray). Step 2: 'Assemble Inputs' (light blue). Step 3: 'Inspect Every Input' (light blue) with a side note listing 'CRS, cell size, extent, data type, NODATA, value range.' Step 4: 'Choose Target Geometry' (light green). Step 5: 'Reconcile Inputs' (light green) with a side note listing 'project, resample, snap, clip.' Step 6: 'Verify Reconciliation' (yellow). Step 7: 'Perform Calculation' (orange). Step 8: 'Verify Output' (yellow). Step 9: 'Document Everything' (light gray). Arrows connect each step to the next. Dashed feedback arrows go from Step 6 back to Step 5 and from Step 8 back to Step 7, labeled 'fix issues.' Style: clean vector illustration, white background, vertical layout, professional diagram."

**Existing image(s):** MISSING

---

## Chapter 7: Slope, Aspect, and the Shape of the Land

*6 figures*

### Figure 7.1

**Caption:** Slope and aspect representations. Left: slope expressed as percent rise (vertical rise divided by horizontal run, times 100) and as degrees (the angle of inclination from horizontal). Right: the gradient vector points in the direction of steepest ascent; aspect is defined as the direction of steepest descent (opposite to the gradient), measured clockwise from north.

**Generation prompt:** "Create a technical diagram showing slope representations. Left: a cross-section of a hillslope with vertical rise and horizontal run labeled, showing the angle theta from horizontal. A formula shows percent slope = (rise/run) x 100 and slope in degrees = arctan(rise/run). Right: a 3D perspective view of a hillslope surface with the gradient vector shown as an arrow pointing uphill, and the aspect arrow pointing downhill (opposite direction), with compass directions N, E, S, W labeled. Style: clean vector illustration, white background, labeled axes, blue-green color scheme."

**Existing image(s):** `fig_07_01.png`

### Figure 7.2

**Caption:** The ArcGIS aspect convention. Aspect is measured clockwise from north in the direction of steepest descent. The example shows an aspect of 145 degrees, indicating a south-southeast-facing slope.

**Generation prompt:** "Create a compass rose diagram showing the ArcGIS aspect convention. The diagram shows a circle with 0/360 degrees at the top (North), 90 degrees at the right (East), 180 degrees at the bottom (South), and 270 degrees at the left (West). An arrow from the center points toward approximately 145 degrees (south-southeast), labeled 'Aspect = 145 degrees'. The interior of the circle shows the clockwise direction of angle measurement. A small inset shows a tilted surface with a ball rolling in the 145-degree direction. Style: clean vector illustration, white background, compass directions clearly labeled."

**Existing image(s):** MISSING

### Figure 7.3

**Caption:** Worked example of the derivative slope method. The 3x3 elevation grid (values in meters, cell size 30 m) produces a slope of 40.1% (21.8 degrees) at the center cell, with aspect 145.2 degrees (south-southeast). The arrow indicates the direction of steepest descent.

**Generation prompt:** "Create a technical diagram showing the worked example of the derivative slope calculation. Display a 3x3 grid with elevation values (80, 74, 63 in top row; 69, 67, 56 in middle row; 60, 52, 48 in bottom row). Cell size = 30 m is labeled. An arrow from the center cell points at 145.2 degrees (south-southeast) showing the aspect direction. The slope value (40.1% / 21.8 degrees) is annotated near the arrow. Compass directions N, E, S, W are shown at the grid edges. The cells are colored with a gradient from dark (high elevation) to light (low elevation). Style: clean vector illustration, white background, labeled values in each cell."

**Existing image(s):** MISSING

### Figure 7.4

**Caption:** The D8 flow direction algorithm. Slope is computed from the center cell to each of its eight neighbors, accounting for the longer distance to diagonal neighbors ($\delta\sqrt{2}$ versus $\delta$ for cardinal neighbors). The flow direction is assigned to the neighbor with the steepest downhill slope.

**Generation prompt:** "Create a technical diagram showing the D8 flow direction concept. A center cell is shown with its eight neighbors arranged in a 3x3 grid. Arrows of different lengths point from the center to each lower neighbor, with the longest arrow (steepest slope) highlighted in blue and labeled 'D8 flow direction'. Cardinal distances are labeled as delta and diagonal distances as delta times sqrt(2). One formula shows S_i = (z_center - z_i) / d_i. The four cardinal neighbors are connected by solid lines of length delta, and the four diagonal neighbors by dashed lines of length delta*sqrt(2). Style: clean vector illustration, white background, labeled distances."

**Existing image(s):** `fig_07_04_a.png, fig_07_04_b.png`

### Figure 7.5

**Caption:** A triangular facet in the D-infinity method. The center cell ($z_0$), a cardinal neighbor ($z_1$, at distance $\delta$), and a diagonal neighbor ($z_2$, at distance $\delta\sqrt{2}$ from the center) define a plane. The steepest downslope direction on this plane makes angle $\alpha_1$ with the cardinal direction.

**Generation prompt:** "Create a technical 3D diagram showing a triangular facet used in the D-infinity method. Three points are shown: z0 (center cell, highest), z1 (cardinal neighbor, at distance delta along the x-axis), and z2 (diagonal neighbor, at distance delta*sqrt(2) from z0). A triangular plane is fitted through the three points. The local coordinate system shows x pointing from z0 to z1 and y perpendicular to x within the plane of the grid. An arrow on the triangular surface shows the steepest downslope direction, making angle alpha_1 with the x-axis. The angle alpha_1 is labeled. Below the 3D view, a plan view shows the same facet from above with the angle clearly marked. Style: clean vector illustration, white background, 3D perspective with grid lines, labeled vertices and angles."

**Existing image(s):** MISSING

### Figure 7.6

**Caption:** DEM data source selection for the Upper Tisza catchment. The Hungarian portion is best served by DDM-5 at 5-meter resolution, while the cross-border area in Ukraine requires Copernicus EEA-10 at 10-meter resolution. Mosaicking the two datasets provides seamless coverage of the full transboundary watershed.

**Generation prompt:** "Create a map diagram showing the Upper Tisza catchment in northeastern Hungary extending into Ukraine. The catchment boundary is shown as a bold black line. Inside the Hungarian portion, the area is shaded and labeled 'DDM-5 (5 m)'. Inside the Ukrainian portion, the area is shaded differently and labeled 'Copernicus EEA-10 (10 m)'. The Tisza River is shown as a blue line flowing from northeast (Ukraine) to southwest (into the Great Plain). Key cities are marked: Tiszabecs at the border crossing, Tokaj at the confluence with the Bodrog, and Szolnok downstream on the plain. An inset map shows Hungary with the study area highlighted. Style: clean cartographic illustration, muted terrain background, clear labels, scale bar."

**Existing image(s):** MISSING

---

## Chapter 8: Measuring Rain Where It Falls

*7 figures*

### Figure 8.1

**Caption:** Thiessen polygons constructed from eight rain gauge locations. Each polygon is assigned the precipitation value of its gauge (shades of blue). A watershed boundary (red) intersects the Thiessen polygons, creating sub-areas used for area-weighted averaging. The inset shows the one-dimensional analogy: a staircase function where each segment takes the value of the nearest gauge.

**Generation prompt:** "Create a technical diagram showing Thiessen polygons (Voronoi tessellation) constructed from 8 irregularly scattered rain gauge points on a map. Each polygon is filled with a different shade of blue proportional to the precipitation value at its gauge (values ranging from 10 to 45 mm, labeled). The polygon boundaries are shown as dashed black lines. A watershed boundary is overlaid as a thick red polygon, cutting across several Thiessen polygons. Show how the watershed intersects the Thiessen polygons to create sub-areas. Include a small inset showing the 1D staircase analogy with five points along a transect. Style: clean vector illustration, white background, labeled axes showing coordinates in km, legend for precipitation values."

**Existing image(s):** `fig_08_01.png`

### Figure 8.2

**Caption:** The kriging workflow. (a) Sample points with measured values. (b) The empirical semivariogram (dots) fitted with a spherical model (curve), showing the nugget, sill, and range. (c) The resulting kriged surface, providing the best linear unbiased estimate at every location. (d) The kriging standard error map, showing estimation uncertainty -- low near gauges (green), high in data-sparse areas (red). This uncertainty quantification is unique to kriging among interpolation methods.

**Generation prompt:** "Create a technical diagram showing the kriging workflow. Top-left panel: scatter plot of sample points with values labeled. Top-right panel: empirical semivariogram (blue dots) with a fitted spherical model (smooth red curve), axes labeled 'Lag distance h (km)' and 'Semivariance gamma(h)', with nugget, sill, and range clearly annotated with dotted lines and labels. Bottom-left panel: the resulting kriged surface shown as a smooth color-ramped raster (blues to reds). Bottom-right panel: the kriging standard error map showing low values (green) near sample points and high values (yellow-red) far from sample points. Arrows connect the panels to show the workflow sequence. Style: clean vector illustration, white background, professional technical diagram, labeled panels (a), (b), (c), (d)."

**Existing image(s):** MISSING

### Figure 8.3

**Caption:** The hypsometric method applied to the Zagyva watershed. Left: linear regression between station elevation and mean annual precipitation ($R^2 = 0.97$). Right: the regression applied to the watershed terrain profile, showing how precipitation increases with elevation from the Tisza floodplain to the Matra Mountains. The watershed-average precipitation (565 mm) accounts for the elevation distribution within the catchment.

**Generation prompt:** "Create a technical diagram showing the hypsometric method for precipitation estimation. Left panel: scatter plot of six stations (labeled with station names) with elevation (m) on x-axis and mean annual precipitation (mm) on y-axis, with a fitted linear regression line (P = 497 + 0.308h, R-squared = 0.97). Right panel: a cross-section view of the Zagyva watershed showing the terrain profile from the Matra Mountains (north, ~1000 m) down to the Tisza floodplain (south, ~80 m), with a color gradient representing the precipitation estimate from the regression (blue = wetter at higher elevations, yellow = drier at lower elevations). Show the watershed average line at 565 mm. Style: clean vector illustration, white background, labeled axes, dual-panel layout."

**Existing image(s):** MISSING

### Figure 8.4

**Caption:** The Thiessen polygon workflow for computing watershed-average precipitation. (a) Rain gauge locations with measured precipitation. (b) Thiessen polygons constructed from gauge positions. (c) Intersection of Thiessen polygons with the watershed boundary, creating fragments with known area and precipitation. (d) Area-weighted summary yielding the watershed-average precipitation.

**Generation prompt:** "Create a technical diagram showing the complete Thiessen polygon workflow in four panels. Panel 1: A map showing 6 rain gauge points (colored circles with precipitation values in mm) scattered across a region. Panel 2: The same map with Thiessen polygons constructed around each gauge (dashed boundaries), each polygon shaded by its gauge's precipitation value. Panel 3: A watershed boundary (thick red line) overlaid on the Thiessen polygons, showing how the intersection creates polygon fragments -- each fragment labeled with its area (km-squared) and precipitation value. Panel 4: A summary table showing the area-weighted calculation leading to the watershed average. Style: clean vector illustration, white background, four-panel layout (2x2), each panel labeled (a) through (d) with a title."

**Existing image(s):** `fig_08_04_a.png, fig_08_04_b.png, fig_08_04_c.png, fig_08_04_d.png, fig_08_04_e.png`

### Figure 8.5

**Caption:** Mean annual precipitation across the Upper Tisza Basin, showing the dramatic gradient from the Carpathian headwaters (>1,000 mm/year) to the Hungarian Great Plain (~500 mm/year). Rain gauge locations (dots) are concentrated in the Hungarian lowlands; the mountainous headwaters are poorly gauged. This spatial distribution makes simple interpolation from Hungarian gauges inadequate for the full basin -- products like CARPATCLIM that incorporate data from all riparian countries are essential.

**Generation prompt:** "Create a map of the Upper Tisza Basin spanning Hungary, Slovakia, Ukraine, and Romania. Show the basin boundary as a thick black outline. Color the basin interior using a precipitation gradient: blue (high, >1000 mm/year) in the Carpathian mountain headwaters (northeast), transitioning through green (~700 mm) in the foothills to yellow-orange (low, ~500 mm/year) on the Great Plain (southwest). Mark the location of Szolnok with a red triangle on the southern/western edge of the basin. Show country borders as thin gray dashed lines. Include scattered point symbols showing rain gauge locations -- dense clusters in Hungary, sparse in the mountain areas. Add a legend showing the precipitation color scale and a north arrow. Style: clean cartographic illustration, white background, standard map elements."

**Existing image(s):** MISSING

### Figure 8.6

**Caption:** The watershed water balance for the Zagyva River at Szolnok. Precipitation ($P = 565$ mm) enters the watershed; streamflow ($Q = 34.5$ mm), evapotranspiration ($ET$), and deep percolation ($G$) remove water. The runoff ratio $R_r = Q/P = 0.061$ indicates that only about 6% of precipitation becomes streamflow, with the remainder lost primarily to evapotranspiration over the agricultural lowlands.

**Generation prompt:** "Create a conceptual diagram showing the water balance of a watershed as a simple box model. Precipitation (P) enters from the top as blue arrows. The box represents the watershed. Streamflow (Q) exits from the bottom-right as a blue arrow into a river channel. Evapotranspiration (ET) exits upward as wavy red arrows. Deep percolation (G) exits downward as a dotted blue arrow. The equation P = Q + ET + G + delta-S is shown below the box. A side panel shows a bar chart comparing P (tall blue bar, 565 mm), ET (tall red bar, ~500 mm), Q (short blue bar, 34.5 mm), and G (very short gray bar). The runoff ratio R = Q/P = 0.061 is annotated. Style: clean vector illustration, white background, labeled elements, educational infographic style."

**Existing image(s):** MISSING

### Figure 8.7

**Caption:** The modern workflow for watershed precipitation estimation. Multiple data sources (gauges, satellites, models) feed into pre-computed gridded products that are then spatially averaged over watershed boundaries using zonal statistics. Validation against observed streamflow through the runoff ratio provides a physical consistency check. This workflow has largely replaced the traditional approach of interpolating directly from raw gauge data.

**Generation prompt:** "Create a flowchart-style diagram showing the modern precipitation estimation workflow for watershed hydrology. Start at top with three parallel input sources: 'Rain Gauge Network' (icon: rain gauge), 'Satellite Products' (icon: satellite with radar beam), and 'Numerical Weather Models' (icon: grid with wind arrows). These feed into a central box: 'Gridded Precipitation Product' (examples listed: PRISM, E-OBS, CARPATCLIM, CHIRPS, ERA5). An arrow leads down to 'Zonal Statistics over Watershed Boundaries' (icon: polygon with grid overlay). This produces 'Watershed-Average Precipitation'. A validation loop connects to 'Observed Streamflow (USGS NWIS / OVF / GRDC)' through a 'Runoff Ratio Check' diamond. Style: clean vector flowchart, white background, blue and green color scheme, labeled boxes and arrows, professional technical diagram."

**Existing image(s):** MISSING

---

## Chapter 9: Preparing the Digital Landscape

*6 figures*

### Figure 9.1

**Caption:** The terrain flow analysis framework. DEM conditioning (the first three steps, covered in this chapter) prepares the elevation data for the flow routing computations covered in Chapters 10 through 12. Each step depends on the output of the previous one, making the quality of DEM conditioning critical to the entire downstream analysis.

**Generation prompt:** "Create a vertical flowchart diagram showing the terrain flow analysis framework. Eight boxes connected by downward arrows in sequence: 'Raw DEM' → 'DEM Reconditioning (optional)' → 'Pit Removal / Fill Sinks' → 'Flow Direction' → 'Flow Accumulation' → 'Stream Definition' → 'Stream Segmentation + Catchment Delineation' → 'Vector Streams, Catchments, Outlets'. Each box includes a small thumbnail illustration: the first shows a colored elevation grid, the third shows a flat-bottomed filled depression, the fourth shows arrows in 8 directions, the fifth shows a blue stream pattern, and the last shows vector polygons and lines. A bracket on the left labels the first three steps as 'Chapter 9' and the remaining steps as 'Chapters 10-12'. Style: clean vector illustration, white background, blue-green color scheme, professional technical diagram."

**Existing image(s):** `fig_09_01.png`

### Figure 9.2

**Caption:** The effect of DEM pits on watershed delineation. Without conditioning (left), pits create isolated sub-watersheds that appear as holes in the computed drainage area. After pit removal (right), the watershed is continuous and the stream network is connected.

**Generation prompt:** "Create a side-by-side comparison showing the effect of pits on watershed delineation. Left panel: 'Before pit removal' shows a watershed boundary (thick red outline) with several irregular holes inside it (white areas with red outlines), representing isolated sub-watersheds that don't connect to the outlet. The stream network (blue lines) has visible gaps. Right panel: 'After pit removal' shows the same watershed with a complete boundary (no holes), a continuous stream network, and uniform drainage to the outlet (marked with a red triangle). Style: clean vector illustration, white background, green terrain shading, professional technical diagram."

**Existing image(s):** MISSING

### Figure 9.3

**Caption:** Cross-section comparison of pit filling and carving. Filling (middle) raises the pit interior to the pour point elevation, creating a flat area. Carving (bottom) lowers the barrier cells to create a drainage channel, preserving the original pit topography. The choice depends on whether the pit is an artifact (fill it) or the barrier is the artifact (carve it).

**Generation prompt:** "Create a cross-section diagram comparing pit filling and carving. Three panels stacked vertically. Top panel labeled 'Original DEM' shows a terrain cross-section with a depression (pit) in the center, with the pit floor labeled and the pour point on the rim labeled. Middle panel labeled 'After Filling' shows the same cross-section with the depression filled to the pour point elevation (shaded fill area). Bottom panel labeled 'After Carving' shows the original terrain with a narrow notch cut through the rim (shaded carved area). The middle panel labels 'Raised area (flat)' and the bottom panel labels 'Lowered area (channel)'. Style: clean technical cross-section, blue shading for modified areas, brown terrain line, white background."

**Existing image(s):** `fig_09_03.png`

### Figure 9.4

**Caption:** Cross-section comparison of the original DEM, simple stream burning, and the AGREE method. Stream burning creates an abrupt cliff at the stream channel; the AGREE method applies a smooth taper within a buffer zone, producing a more realistic terrain surface that maintains correct drainage without introducing artificial discontinuities.

**Generation prompt:** "Create a cross-section diagram comparing three DEM conditioning approaches across a stream channel. Three vertically stacked panels. Top panel labeled 'Original DEM' shows gentle terrain with a subtle valley. Middle panel labeled 'Stream Burning' shows the same terrain with a deep rectangular notch at the stream location, with steep cliffs on both sides, labeled 'Abrupt cliff'. Bottom panel labeled 'AGREE Method' shows the same terrain with a smooth, V-shaped depression centered on the stream, with a labeled 'Buffer distance (500 m)' spanning from the stream to where the modification ends, and a dashed line showing the original terrain for reference. The AGREE panel shows the taper zone clearly. Style: clean technical cross-section, three colors -- brown for original terrain, red for burned surface, blue for AGREE surface, white background."

**Existing image(s):** `fig_09_04.wmf`

### Figure 9.5

**Caption:** Fill-minus-DEM diagnostic for a karst landscape similar to the Aggtelek region. Each colored spot represents a depression that was filled during DEM conditioning. The color indicates fill depth: yellow for shallow fills (1-5 m, likely artifact pits) and red for deep fills (10-15 m, likely real karst dolines). This diagnostic map provides a valuable inventory of depressions and should always be examined after pit filling.

**Generation prompt:** "Create a map-style illustration showing the fill-minus-DEM diagnostic for a karst landscape. The image shows a plan view of a hillside with a river at the bottom. Most of the area is colored white or very light blue (zero or near-zero fill depth). Scattered across the upper portion are clusters of warm-colored spots (yellow to red) representing filled dolines of varying depths: a few large red spots labeled '10-15 m fill' and many smaller yellow-orange spots labeled '1-5 m fill'. A color ramp legend on the right shows Fill Depth from 0 (white) to 15 m (dark red). A label reads 'Karst doline zone'. The river is shown in blue at the bottom. Style: clean map illustration, white background, professional cartographic style."

**Existing image(s):** MISSING

### Figure 9.6

**Caption:** Recommended DEM conditioning workflow. The process begins with the raw DEM (with buffer), optionally reconditions using the AGREE method, fills pits, examines the fill-minus-DEM diagnostic for quality control, and produces a conditioned DEM ready for flow direction computation. The conditioned DEM should be used only for flow routing; terrain derivatives should be computed from the original DEM.

**Generation prompt:** "Create a workflow diagram showing the practical DEM conditioning process. A horizontal flow from left to right with five boxes: (1) 'Raw DEM + Buffer' showing a terrain grid with a dashed buffer line around the study area; (2) 'DEM Reconditioning (AGREE)' showing the stream network overlaid on the terrain; (3) 'Pit Filling' showing a flat-bottomed depression being filled; (4) 'Quality Check: Fill - DEM' showing a difference map with colored spots; (5) 'Conditioned DEM → Flow Direction (Ch. 10)' showing the final clean terrain with an arrow to the next chapter. Below the diagram, a warning box reads 'Common mistake: Do NOT use the conditioned DEM for slope/aspect analysis -- use the original DEM.' Style: clean vector flowchart, white background, labeled arrows between steps, professional technical diagram."

**Existing image(s):** MISSING

---

## Chapter 10: Which Way Does Water Flow?

*8 figures*

### Figure 10.1

**Caption:** The D8 flow direction concept. The center cell evaluates the slope to each of its eight neighbors. The slope is the elevation drop divided by the inter-cell distance, which is larger by a factor of $\sqrt{2}$ for diagonal neighbors. Flow is assigned to the single neighbor with the steepest positive slope (red arrow). Note that the steepest descent may not be toward the lowest neighbor.

**Generation prompt:** "Create a technical diagram showing a 3x3 grid of DEM cells with the center cell at elevation 100. Label all eight neighbors with elevations. Show arrows from the center cell to each neighbor, with slope values annotated along each arrow. Highlight the steepest-descent arrow in red. Include the formula S = (z0 - zi) / di. Show that cardinal distance = delta and diagonal distance = delta * sqrt(2). Style: clean vector illustration, white background, labeled cells with elevation values."

**Existing image(s):** `fig_10_01.png`

### Figure 10.2

**Caption:** The two dominant flow direction encoding conventions. ArcGIS (left) uses powers of two proceeding clockwise from east. TauDEM (right) uses sequential integers proceeding counterclockwise from east. A code of "2" means southeast in ArcGIS but northeast in TauDEM --- always confirm the convention before interpreting results.

**Generation prompt:** "Create a side-by-side comparison diagram of ArcGIS and TauDEM flow direction encoding. Left panel: a center cell surrounded by 8 neighbors, each labeled with the ArcGIS code (1, 2, 4, 8, 16, 32, 64, 128) in clockwise order from east, with compass directions. Right panel: the same layout but with TauDEM codes (1-8) in counterclockwise order from east. Use distinct colors for each direction. Title: 'ArcGIS vs TauDEM Flow Direction Encoding'. Style: clean vector illustration, white background, clear labels."

**Existing image(s):** `fig_10_02.png`

### Figure 10.3

**Caption:** Contributing area computed by D8 (left) and D-infinity (right) for the same DEM. The D8 map shows characteristic horizontal and diagonal streaking artifacts caused by flow being constrained to eight discrete directions. The D-infinity map produces smooth, continuous patterns that better represent the true convergence and divergence of topographic flow.

**Generation prompt:** "Create a side-by-side comparison of two contributing area maps of the same terrain. Left panel labeled 'D8 Contributing Area' shows visible horizontal and 45-degree streak artifacts with parallel lines of high values. Right panel labeled 'D-infinity Contributing Area' shows smooth, continuous contributing area patterns without streak artifacts. Both panels use the same terrain extent and a logarithmic color ramp from blue (low) to red (high). Style: scientific figure, labeled panels, shared color bar."

**Existing image(s):** `fig_10_03_a.png, fig_10_03_b.png`

### Figure 10.4

**Caption:** Stream networks extracted from the same DEM using three different flow accumulation thresholds. As the threshold increases from 100 cells (left) to 1,000 cells (center) to 5,000 cells (right), the network becomes progressively sparser, retaining only the larger channels. The choice of threshold depends on the application and should be calibrated against reference stream maps.

**Generation prompt:** "Create a figure showing three panels of the same terrain, each showing a stream network extracted with a different flow accumulation threshold. Left panel: threshold = 100 cells, very dense network with many headwater streams. Center panel: threshold = 1000 cells, moderate network density. Right panel: threshold = 5000 cells, only major streams remain. Each panel shows the stream network in blue over a gray hillshade background. Label each panel with its threshold value. Style: scientific figure with three panels, clean labels."

**Existing image(s):** `fig_10_04_a.png, fig_10_04_b.png, fig_10_04_c.png`

### Figure 10.5

**Caption:** The dependence function for a target cell (star). Colors indicate the fraction of flow from each cell that eventually reaches the target, from red (100% of flow reaches target) to blue (no flow reaches target). The dependence function identifies the "zone of contribution" for any point in the landscape --- essential for source water protection and contamination tracing.

**Generation prompt:** "Create a scientific diagram showing a dependence function map. Show a small DEM with a target cell (marked with a star) near a stream. Color the upstream cells using a gradient from red (dependence = 1.0, cells that send all their flow to the target) to blue (dependence = 0.0, cells that send no flow to the target). Show intermediate colors (orange, yellow, green) for partial dependence values. Include a color bar legend. Style: clean scientific illustration, white background, labeled target cell."

**Existing image(s):** `fig_10_05.png`

### Figure 10.6

**Caption:** Topographic wetness index (TWI) for a small watershed, computed using D-infinity contributing area and local slope. High TWI values (blue) identify flat, convergent areas where saturation is most likely --- typically valley bottoms and areas along the stream network. Low TWI values (brown) correspond to steep ridgelines and divergent hilltops. TWI is a key parameter in TOPMODEL and related distributed hydrologic models.

**Generation prompt:** "Create a scientific figure showing a topographic wetness index (TWI) map for a small watershed. Use a color ramp from brown (low TWI, dry ridges and steep slopes) through yellow and green to blue (high TWI, wet valley bottoms and flat convergent areas). Show the stream network overlaid in dark blue. Include a color bar labeled 'TWI' with values from approximately 4 to 16. Style: scientific map figure, labeled color bar, north arrow."

**Existing image(s):** `fig_10_06.png`

### Figure 10.7

**Caption:** The Height Above Nearest Drainage (HAND) concept. For each cell on the hillslope, HAND is the vertical distance between the cell elevation and the elevation of the stream cell it drains to (following the flow path, not the straight-line distance). Flooding occurs when the water depth in the stream exceeds the HAND value: cells with HAND less than the water depth are inundated. Chapter 14 develops the HAND methodology for flood mapping in full detail.

**Generation prompt:** "Create a cross-section diagram illustrating the HAND concept. Show a hillslope profile from ridgeline to stream channel, with the terrain surface drawn as an irregular line. Mark a point on the hillslope and show a vertical arrow from that point down to the stream elevation, labeled 'HAND'. Show the flow path as a curved arrow following the terrain surface from the hillslope point to the stream. Also show a water surface in the stream channel and indicate the flood condition where water depth exceeds HAND. Style: clean technical cross-section, labeled arrows, blue water surface."

**Existing image(s):** `fig_10_07.png`

### Figure 10.8

**Caption:** The DEM-to-drainage processing pipeline. Starting from a conditioned DEM, D8 and D-infinity flow directions are computed. D8 feeds into flow accumulation, stream definition, and watershed delineation (Chapter 11). D-infinity feeds into specific catchment area and TWI. Both contribute to HAND computation (Chapter 14). Weighted and generalized accumulation functions extend the basic framework to environmental applications.

**Generation prompt:** "Create a flowchart showing the DEM-to-drainage processing pipeline. Start with 'Conditioned DEM' at the top. Arrow to 'D8 Flow Direction' and 'D-infinity Flow Direction' (computed in parallel). From D8: arrow to 'Flow Accumulation', then to 'Stream Definition (threshold)', then to 'Watershed Delineation'. From D-infinity: arrow to 'Specific Catchment Area', then to 'TWI'. Both branches feed into 'HAND' at the bottom. Also show 'Weighted Accumulation' and 'Generalized Functions' as branches from the flow direction step. Style: clean flowchart, boxes with rounded corners, labeled arrows, professional layout."

**Existing image(s):** MISSING

---

## Chapter 11: Drawing Watersheds from Data

*5 figures*

### Figure 11.1

**Caption:** The effect of the support area threshold on stream network density. The same watershed DEM produces dramatically different networks depending on the threshold: $T = 100$ cells (left) yields a dense network capturing fine-scale drainage features; $T = 1{,}000$ cells (center) produces a moderate network; $T = 5{,}000$ cells (right) shows only major streams. The threshold determines the partition between hillslope and channel processes in the landscape.

**Generation prompt:** "Create a side-by-side comparison of three stream networks derived from the same watershed DEM using different support area thresholds. Left panel: T=100 cells, showing a very dense network with many fine headwater streams. Center panel: T=1000 cells, showing a moderate network. Right panel: T=5000 cells, showing a sparse network with only major streams. Each panel shows the same watershed outline in gray with blue stream lines. Label each panel with its threshold value and approximate drainage density. Style: clean vector illustration, white background, blue streams on light gray hillshade."

**Existing image(s):** `fig_11_01_a.png, fig_11_01_b.png, fig_11_01_c.png`

### Figure 11.2

**Caption:** The relationship between drainage density and hillslope length. Top: A simplified rectangular catchment shows that mean hillslope length $B$ equals $1/(2D_d)$. Bottom: Drainage density decreases as a power law with increasing support area threshold, consistent with the dimensional relationship between area (length$^2$) and inverse length.

**Generation prompt:** "Create a technical diagram showing a simplified rectangular watershed cross-section. A single stream channel runs horizontally along the center. On each side, arrows show overland flow traveling a distance B (hillslope length) perpendicular to the channel. The stream has length L. Labels show: A = 2BL (total area), D_d = L/(2BL) = 1/(2B), and B = 1/(2D_d). Below, show a log-log plot with 'Support area threshold T (cells)' on the x-axis and 'Drainage density D_d (km^-1)' on the y-axis, showing a power-law relationship with slope approximately -0.5. Style: clean technical diagram, labeled axes, professional quality."

**Existing image(s):** MISSING

### Figure 11.3

**Caption:** The stream drop t-test. Left: The t-statistic plotted against the support area threshold. The objective threshold is the smallest threshold where $|t|$ falls below 2 (dashed red lines), indicating that first-order stream drops are consistent with higher-order drops. Right: Histograms of stream drops at the selected threshold, showing that first-order and higher-order distributions overlap substantially -- the constant drop property is satisfied.

**Generation prompt:** "Create a two-panel technical plot. Left panel: t-statistic (y-axis) versus support area threshold in cells (x-axis, logarithmic scale). Plot shows a curve starting at approximately -4.2 at threshold 50, crossing through -2 at around threshold 150-200, and leveling off near 0 for larger thresholds. Draw a horizontal dashed red line at t = -2 and t = +2 (the critical values). Mark the crossing point with a red dot and label it 'Objective threshold'. Right panel: Two overlapping histograms showing the distribution of stream drops for first-order streams (hatched blue) and higher-order streams (solid green), with their means marked by vertical dashed lines. Style: clean scientific plot, labeled axes with units, white background, publication quality."

**Existing image(s):** MISSING

### Figure 11.4

**Caption:** The Peuker-Douglas algorithm for identifying valley cells. Each 2$\times$2 window of the DEM is examined, and the highest cell in each window is unflagged. After processing all windows, the remaining flagged cells (never the highest in any window) are identified as upward-curved valley cells. These cells tend to lie along valley bottoms and stream channels.

**Generation prompt:** "Create a step-by-step diagram illustrating the Peuker-Douglas algorithm. Top: Show a 4x3 grid of elevation values (example: 72, 68, 64, 59 / 75, 71, 56, 49 / 82, 78, 62, 51). Below the grid, show each 2x2 window highlighted in sequence, with the highest cell in each window circled and marked as 'unflagged'. Bottom: Show the resulting binary grid where unflagged cells (ridges/slopes) are white and remaining flagged cells (valleys) are shaded blue. Include arrows pointing to the valley cells with a label 'Upward-curved (valley) cells'. Style: clean technical diagram, grid cells clearly labeled with values, step-by-step progression."

**Existing image(s):** `fig_11_04.png`

### Figure 11.5

**Caption:** Strahler stream ordering. Headwater channels with no tributaries are first order (1). When two equal-order streams merge, the downstream stream increments by one order. When unequal-order streams merge, the downstream stream retains the higher order. The ordering provides a hierarchical classification of the drainage network that is fundamental to geomorphologic analysis.

**Generation prompt:** "Create a diagram of a stream network showing Strahler stream ordering. The network has several headwater streams labeled '1' (first order) in thin blue. Where two first-order streams meet, the downstream segment is labeled '2' (second order) in medium blue. Where two second-order streams meet, the downstream segment is labeled '3' (third order) in thick dark blue. Also show a case where a first-order stream joins a second-order stream, with the downstream remaining '2'. Number each junction clearly. Include a legend showing the three orders with increasing line thickness. Style: clean vector diagram, white background, blue color gradient from light (order 1) to dark (order 3)."

**Existing image(s):** `fig_11_05.png`

---

## Chapter 12: Automating the Workflow

*6 figures*

### Figure 12.1

**Caption:** The fundamental advantage of scripted workflows over manual GIS operations. A manual workflow that takes 20 minutes for one watershed becomes impractical at scale; the same workflow encoded as a script can process thousands of watersheds unattended.

**Generation prompt:** "Create a comparison diagram with two panels. Left panel labeled 'Manual Workflow' shows a stick figure at a computer clicking through 11 sequential tool dialog boxes, with a clock showing 8 hours and a sad face. Right panel labeled 'Scripted Workflow' shows the same stick figure typing a few lines of code, then a computer screen showing a progress bar at 97%, with a clock showing 20 minutes and a happy face. Below, an arrow labeled 'Scale' shows: Manual = 1 watershed, Scripted = 1000 watersheds. Style: clean vector illustration, white background, blue and orange accents, technical but friendly."

**Existing image(s):** `fig_12_01_a.png, fig_12_01_b.png`

### Figure 12.2

**Caption:** The recommended progression from manual GIS operations to automated scripting. Each step builds on the previous one, and at every stage the analyst has a working workflow.

**Generation prompt:** "Create a workflow diagram showing 6 steps in a vertical sequence connected by arrows. Step 1: 'Run tool manually' (icon of a mouse clicking a dialog box). Step 2: 'Copy Python from History' (icon of clipboard with code). Step 3: 'Add imports and settings' (icon of a code editor with highlighted header lines). Step 4: 'Test the script' (icon of a play button with a checkmark). Step 5: 'Parameterize inputs' (icon of variables x, y, z replacing file names). Step 6: 'Add loops and error handling' (icon of a circular arrow around multiple files). Label at bottom: 'From clicking to scripting in 6 steps.' Style: clean vector illustration, white background, blue accents, numbered steps."

**Existing image(s):** `fig_12_02.png`

### Figure 12.3

**Caption:** Batch processing of multiple watersheds using a parameterized Python script with a loop. Each watershed is processed independently; failures are logged and retried separately.

**Generation prompt:** "Create a diagram showing batch processing of multiple watersheds. At the top, a Python script icon with a loop symbol. Below it, three parallel processing lanes, each containing: a DEM raster, an arrow through processing steps (Fill, Flow Direction, Flow Accumulation, Watershed), and output products (watershed polygon, stream network). The three lanes are labeled 'Zagyva,' 'Raba,' and 'Sajo.' A clock icon shows 'Overnight run: 3 hours total.' At the bottom, a log file shows two green checkmarks and one red X with 'retry.' Style: clean vector illustration, white background, blue-green color scheme."

**Existing image(s):** MISSING

### Figure 12.4

**Caption:** TauDEM's three-layer architecture. Users interact through the ArcGIS toolbox or Python scripts. The Python wrapper translates parameters into command-line calls. The C++ core performs the computation using MPI parallelism, reading and writing open-standard GeoTIFF files.

**Generation prompt:** "Create an architecture diagram for TauDEM showing three layers. Top layer labeled 'User Interface' shows two options side by side: 'ArcGIS Toolbox' (with ESRI logo) and 'Python Script' (with Python logo). Middle layer labeled 'Python Wrapper' shows a box containing: 'Parameter validation, Command construction, subprocess.run(), Output handling.' Bottom layer labeled 'C++ Computational Core' shows a box with 'MPI Parallel Processing' containing icons for 8 CPU cores, and file I/O arrows pointing to GeoTIFF files on either side. Arrows connect the layers top to bottom. Style: clean technical architecture diagram, white background, three distinct color bands for each layer."

**Existing image(s):** `fig_12_04_a.png, fig_12_04_b.png`

### Figure 12.5

**Caption:** The overlap between commercial (ArcGIS) and open-source GIS ecosystems for hydrological scripting. Both support Python, open standard formats, and the same core algorithms. Many professionals work across both ecosystems depending on the task.

**Generation prompt:** "Create a Venn diagram with two overlapping circles. Left circle labeled 'ArcGIS Pro / ArcPy' contains: 'Enterprise geodatabase, Arc Hydro, ESRI support, Industry standard.' Right circle labeled 'Open Source (QGIS, GDAL, WhiteboxTools, TauDEM)' contains: 'Free, Linux/cloud, Transparent algorithms, Community-driven.' The overlap region contains: 'Python scripting, GeoTIFF/Shapefile, Watershed delineation, Same results.' Below the diagram: 'Most professionals work in the overlap.' Style: clean vector diagram, white background, blue for ArcGIS circle, green for open-source circle, purple overlap."

**Existing image(s):** MISSING

### Figure 12.6

**Caption:** The same Python scripting skills apply worldwide -- only the data sources and coordinate systems change. Global free datasets (SRTM, Copernicus, HydroSHEDS) ensure that automated watershed delineation is accessible to researchers in any country.

**Generation prompt:** "Create a world map showing three highlighted regions: the United States (blue), Hungary/EU (green), and a global tropical belt (orange). Each region has an annotation box. US box: 'USGS 3DEP, NHDPlus, ArcPy workflows.' Hungary/EU box: 'DDM-5, Copernicus DEM, OVF data, CCM catchments.' Global box: 'SRTM, Copernicus GLO-30, HydroSHEDS, Google Earth Engine.' At the bottom: 'Same Python skills, different data sources.' Style: clean vector map, white background, minimal country borders, colored highlights with annotation callouts."

**Existing image(s):** MISSING

---

## Chapter 13: Seeing the Ground in 3D: LiDAR

*7 figures*

### Figure 13.1

**Caption:** Principle of airborne LiDAR acquisition. A pulsing laser combined with a rotating or oscillating mirror sweeps measurements across a wide swath perpendicular to the flight path. GPS and an inertial measurement unit (IMU) continuously track the aircraft's position and orientation, enabling each pulse return to be geolocated in three dimensions. The resulting point cloud contains millions to billions of measurements describing the terrain and all objects upon it.

**Generation prompt:** "Create a technical diagram showing the operation of an airborne LiDAR system. Show an aircraft flying left to right with a laser instrument emitting pulses downward through a rotating mirror that sweeps left and right. Show the zigzag scan pattern on the ground below the aircraft, with individual laser pulse paths drawn as thin lines from the mirror to various ground points. Include a GPS satellite above and an inertial measurement unit symbol on the aircraft. Label: 'Laser emitter', 'Rotating mirror', 'GPS', 'IMU', 'Scan swath', 'Flight direction'. On the ground, show mixed terrain: some trees, a building, and bare ground, with colored dots representing the point cloud. Style: clean vector illustration, white background, professional technical diagram."

**Existing image(s):** MISSING

### Figure 13.2

**Caption:** Comparison of linear mode and Geiger mode LiDAR acquisition strategies. Linear mode (left) tracks individual pulses sequentially, requiring lower flying altitudes and producing moderate coverage rates. Geiger mode (right) uses a photon-counting detector array to capture thousands of measurements simultaneously, enabling higher altitudes, faster speeds, and dramatically greater coverage efficiency.

**Generation prompt:** "Create a technical comparison diagram of linear mode vs. Geiger mode LiDAR. Left panel: show an aircraft at lower altitude emitting individual laser pulses one at a time through a scanning mirror, with single return paths drawn to the ground. Right panel: show an aircraft at higher altitude emitting a wide illumination area that covers the ground, with a 2D detector array capturing photon returns from many angles simultaneously. Below each panel, show the resulting point cloud pattern on the ground. Labels: 'Linear Mode: one pulse at a time', 'Geiger Mode: photon-counting array', 'Lower altitude / slower', 'Higher altitude / faster', 'Moderate coverage rate', 'Very high coverage rate'. Style: clean vector illustration, white background, professional technical diagram."

**Existing image(s):** `fig_13_02_a.png, fig_13_02_b.png`

### Figure 13.3

**Caption:** Drone-based LiDAR (left) versus Structure from Motion photogrammetry (right) for a partially forested river corridor. LiDAR pulses penetrate canopy gaps to reach the ground, enabling bare-earth DEM extraction. SfM photogrammetry, using overlapping photographs, produces high-quality surface models in open areas but cannot see through vegetation to the ground.

**Generation prompt:** "Create a comparison diagram showing drone-based LiDAR versus drone-based photogrammetry (Structure from Motion). Left side: a quadcopter drone with a small LiDAR sensor flying over a partially forested river corridor, with laser pulses penetrating through tree canopy to reach the ground, producing a colored point cloud that shows both canopy and ground. Right side: the same drone with a camera flying over the same area, capturing overlapping photographs from multiple angles, with connecting lines between photos showing the overlapping coverage. Below, show the resulting 3D models: left shows a bare-earth model beneath trees, right shows only the canopy surface (DSM). Labels: 'Drone LiDAR: penetrates canopy', 'SfM Photogrammetry: sees only surface', 'Bare-earth DEM possible', 'Only DSM possible under trees'. Style: clean vector illustration, white background."

**Existing image(s):** MISSING

### Figure 13.4

**Caption:** The relationship between the Digital Surface Model (DSM), the bare-earth DEM, and the Canopy Height Model (CHM). First return points define the DSM (tops of trees and buildings); last return points, after classification, define the bare-earth DEM. The difference (nDSM or CHM) provides the height of above-ground features -- a valuable product for forestry, urban modeling, and ecology.

**Generation prompt:** "Create a technical diagram showing the relationship between a Digital Surface Model (DSM) and a bare-earth DEM, with the Canopy Height Model (CHM) as the difference. Show a cross-section view of terrain with trees and a building. Top line: DSM following the tops of trees and building roof. Bottom line: bare-earth DEM following the ground. The vertical gap between them is labeled 'CHM = DSM - DEM'. Show first return points (red dots) at the top of canopy/building and last return points (green dots) at the ground. On the right side, show how forest canopy height varies. Labels: 'DSM (first returns)', 'Bare-earth DEM (last returns)', 'CHM = DSM - DEM', 'Tree height', 'Building height'. Style: clean vector cross-section illustration, white background."

**Existing image(s):** `fig_13_04_a.tiff, fig_13_04_b.tiff`

### Figure 13.5

**Caption:** Principle of coastal topobathymetric LiDAR. Near-infrared laser pulses (red) measure land topography and the water surface. Green-wavelength pulses (green) penetrate the water, refracting at the air-water interface according to Snell's Law, and reflect from the seabed. The time difference between the surface return and the bottom return yields water depth. The result is a seamless elevation surface bridging land and underwater terrain.

**Generation prompt:** "Create a technical cross-section diagram showing bathymetric LiDAR operation at a coastal zone. Show an aircraft above, emitting two types of laser beams: a near-infrared beam (red) that reflects from the water surface, and a green beam (green) that penetrates through the water and reflects from the seabed. Show the water surface with a dotted line, the seabed as a sloped surface below. Indicate Snell's Law refraction at the air-water interface where the green beam bends toward vertical. Label the surface return and bottom return signals. On the left side show land topography measured by the infrared beam. Labels: 'Aircraft (400m altitude)', 'IR laser (1064 nm) - topography', 'Green laser (532 nm) - bathymetry', 'Water surface return', 'Bottom return', 'Refraction (Snell's Law)', 'Seamless topo-bathy surface'. Style: clean vector illustration, white background."

**Existing image(s):** `fig_13_05.jpg`

### Figure 13.6

**Caption:** The national HAND (Height Above Nearest Drainage) map for the conterminous United States, computed in a single day using supercomputing resources. Blue areas have small HAND values (close in elevation to the nearest stream) and are flood-prone. White areas have large HAND values (elevated well above the nearest stream) and are topographically protected from flooding. The continental-scale patterns -- low-lying Gulf Coast and Mississippi embayment versus mountainous Appalachians and Rockies -- are immediately apparent.

**Generation prompt:** "Create a map of the conterminous United States showing the national HAND (Height Above Nearest Drainage) values. Use a color ramp from deep blue (HAND = 0 meters, meaning at stream level) through green and yellow to white (HAND > 50 meters, meaning high above nearest stream). Show the Mississippi embayment, Gulf Coast of Texas, Florida coast, and Central Valley of California as prominently blue (low HAND) areas. Show the Appalachian Mountains, Rocky Mountains, and Cascade Range as white (high HAND) areas. Include a color bar legend labeled 'HAND (meters)' from 0 to 50+. Title: 'Continental US Height Above Nearest Drainage'. Style: clean cartographic map, white background outside US boundary."

**Existing image(s):** `fig_13_06.tiff`

### Figure 13.7

**Caption:** Evolution of topographic data availability for hydrological applications, from the first satellite-derived global DEMs (SRTM, 2000) through national LiDAR programs (3DEP, AHN) to the emerging capability for continental-scale LiDAR-resolution processing. Each generation of data has enabled new classes of hydrological analysis that were impossible with the previous generation.

**Generation prompt:** "Create a timeline diagram showing the evolution of topographic data sources for hydrology from 1990 to 2030. Show increasing resolution and accuracy on the vertical axis. Mark key milestones: SRTM (2000, 90m global), NED (2003, 10m US), early LiDAR (2005, 1m local), AHN2 Netherlands (2012), 3DEP initiation (2015), national HAND map (2016), AHN4 (2022), 3DEP >80% complete (2025), projected 1m national LiDAR processing (2028+). Use different colors for US programs, European programs, and global satellite missions. Style: clean infographic timeline, white background, professional."

**Existing image(s):** MISSING

---

## Chapter 14: How High Above the River?

*5 figures*

### Figure 14.1

**Caption:** The HAND concept illustrated in cross-section. Three points at different positions on the landscape have different HAND values depending on their vertical distance above the nearest stream. During a flood that raises water 5 metres above the channel, Point A (HAND = 2 m) is inundated to 3 m depth, Point B (HAND = 8 m) remains dry, and Point C (HAND = 45 m) faces no conceivable flood risk. Absolute elevation tells none of this story; only relative elevation above the stream does.

**Generation prompt:** "Create a technical cross-section diagram illustrating the HAND concept. Show a river channel in the center with water at normal level (blue). On both sides, show the land surface rising from the floodplain to hilltops. Mark three points: Point A on the floodplain (HAND = 2 m), Point B on a terrace (HAND = 8 m), Point C on a hilltop (HAND = 45 m). Draw vertical arrows from each point down to the stream level, labeled with the HAND value. Also show a dashed line for a flood level at +5 m, indicating that Point A would be submerged by 3 m, Point B would be just above the flood, and Point C is far above. Include axis labels: horizontal = distance from channel (m), vertical = elevation (m). Show both absolute elevation scale on left and HAND values annotated on the arrows. Style: clean vector illustration, white background, labeled axes, blue for water, green for land surface."

**Existing image(s):** `fig_14_01.png`

### Figure 14.2

**Caption:** The HAND algorithm illustrated step by step on a small grid. Starting from stream cells (HAND = 0), the algorithm sweeps upslope, computing each cell's HAND value as a weighted average of the accumulated height through its D-infinity flow partitions. The process terminates when all cells have been assigned values.

**Generation prompt:** "Create a step-by-step diagram showing the HAND algorithm on a small 5x5 grid. Panel 1: Show the grid with elevation values in each cell and stream cells highlighted in blue (HAND=0). Panel 2: Show the D-infinity flow direction arrows pointing from upslope cells toward the stream. Panel 3: Show the 'ready' cells (those immediately adjacent to stream cells) highlighted in yellow, with their HAND computation formula shown. Panel 4: Show the completed HAND grid with all values filled in, using a color gradient from dark blue (0) through green (5) to brown (20). Include annotations explaining each step. Style: clean vector illustration, white background, numbered panels, color-coded cells."

**Existing image(s):** `fig_14_02_a.png, fig_14_02_b.png`

### Figure 14.3

**Caption:** A HAND raster visualized with a blue colour ramp emphasizing low HAND values. The floodplain appears as a band of blue adjacent to the stream, widening in broad valleys and narrowing in constricted reaches. High-HAND areas are rendered transparent, allowing the underlying hillshade to show the topographic context. This visualization immediately communicates flood vulnerability without requiring hydraulic modeling.

**Generation prompt:** "Create a map visualization showing a HAND raster for a river floodplain area. Use a blue color ramp: dark blue for HAND 0-1 m, medium blue for 1-2 m, light blue for 2-5 m, pale blue for 5-10 m, and transparent/white for >10 m areas where the hillshade terrain shows through. Show a meandering river in the center with the floodplain visible as a blue band that widens in lowland areas and narrows in constricted valley sections. Include a legend showing the HAND classes and their flood risk interpretation. Include a scale bar. Style: realistic map rendering, clean legend, white background for the legend area."

**Existing image(s):** `fig_14_03.png`

### Figure 14.4

**Caption:** Continental-scale HAND computation for the United States at 10-metre resolution. Major river corridors (Mississippi, Missouri, Ohio, Columbia) appear as dark blue bands where HAND values are low. The floodplains of these rivers are clearly visible as blue zones extending away from the channels. Mountainous regions in the west and Appalachians in the east appear in warm colours where HAND values are high. This national product enables consistent flood vulnerability screening across the entire country.

**Generation prompt:** "Create a map showing the continental United States colored by HAND values. Use a blue-to-brown color ramp: dark blue along major rivers and their floodplains (HAND 0-5 m), light blue for moderate-HAND areas (5-20 m), green/yellow for intermediate areas (20-50 m), and brown for high-HAND areas (>50 m, mountains and uplands). Major rivers (Mississippi, Missouri, Ohio, Columbia, Colorado) should be clearly visible as dark blue corridors. Include state boundaries as thin grey lines. Include a small inset map showing a zoomed view of a floodplain area. Add a color bar legend. Style: clean cartographic rendering, white background, minimal labels."

**Existing image(s):** `fig_14_04.tiff`

### Figure 14.5

**Caption:** HAND raster for the middle Tisza near Szolnok, Hungary. The active floodplain between the levees (hullámtér) appears in deep blue with HAND values of 0-4 m. The protected floodplain (mentett ártér) beyond the levees shows HAND values of 3-8 m. The flat terrain of the Great Plain means that even small HAND differences (1-2 m) can correspond to the boundary between regular flooding and dry land. Szolnok, situated on a natural terrace, has HAND values of 5-8 m for most of the built-up area.

**Generation prompt:** "Create a map showing a HAND raster for a segment of the Tisza River in Hungary, in the flat Great Plain region. Show the river meandering through the center with a wide, flat floodplain. Use a detailed blue color ramp: dark blue for HAND 0-1 m (active floodplain), medium blue for 1-2 m, light blue for 2-3 m, pale blue for 3-5 m, and yellow for 5-8 m. Show levees as thin brown lines on both sides of the floodplain. Label the key features: 'Tisza' for the river, 'hullámtér' for the area between levees, 'mentett ártér' for the protected floodplain beyond the levees, and a town labeled 'Szolnok'. Include a north arrow, scale bar (5 km), and HAND legend. Style: clean cartographic rendering with subtle terrain shading."

**Existing image(s):** MISSING

---

## Chapter 15: Mapping Where Floods Go

*7 figures*

### Figure 15.1

**Caption:** The four-step flood inundation mapping pipeline. Each stage transforms data from one form to the next: a discharge value becomes a depth, the depth becomes a spatial flood map, and the flood map becomes an impact assessment. The entire pipeline can execute in minutes when intermediate products are pre-computed.

**Generation prompt:** "Create a horizontal pipeline diagram showing four connected stages of flood inundation mapping. Stage 1: 'Discharge Forecast' with an icon of a hydrograph (discharge vs. time). Stage 2: 'Depth Estimation' with an icon of a rating curve (depth vs. discharge). Stage 3: 'Inundation Mapping' with an icon of a cross-section showing water level compared to HAND values. Stage 4: 'Impact Assessment' with an icon of buildings partially submerged in blue water. Arrows connect the stages left to right. Below each stage, show the data source: NWM/EFAS/GloFAS, Manning's equation + HAND properties, HAND raster comparison, Address points + building data. Style: clean vector illustration, white background, blue water accents, labeled clearly."

**Existing image(s):** `fig_15_01_a.png, fig_15_01_b.png, fig_15_01_c.png, fig_15_01_d.png`

### Figure 15.2

**Caption:** Two approaches to characterising channel geometry. The cross-section approach (left) produces variable results depending on where the section is drawn. The HAND horizontal slicing approach (right) integrates over the entire reach at each depth, producing stable reach-averaged properties.

**Generation prompt:** "Create a comparison diagram with two panels. Left panel: 'Cross-Section Approach' -- a 3D view of a river reach with three vertical cross-section planes cutting through it, each showing a different channel shape, with arrows pointing to three different depth-discharge curves that vary erratically. Right panel: 'HAND Horizontal Slicing Approach' -- the same 3D river reach with three horizontal planes at depths 1m, 3m, and 5m slicing through the terrain, showing how each horizontal slice captures the entire reach geometry at once, with an arrow pointing to a single smooth depth-discharge curve. Style: clean technical illustration, blue for water, brown for terrain, white background."

**Existing image(s):** MISSING

### Figure 15.3

**Caption:** Reach-averaged hydraulic properties derived from the HAND raster. The three-dimensional quantities (surface area $A_s$, volume $V$, and bed area $A_b$) are divided by the channel length $L$ to produce the cross-sectional properties ($A_x$, $T$, $P$) used in Manning's equation.

**Generation prompt:** "Create a 3D perspective diagram of a river reach segment showing the HAND-derived hydraulic properties. The reach is shown as a sinuous channel with floodplain, partially flooded to a uniform depth d. Annotate the following: surface area A_s (the blue water surface viewed from above), volume V (the blue water body in 3D), bed area A_b (the brown terrain surface under the water, including sloped banks), channel length L (measured along the stream centerline), depth d (vertical arrow from stream bed to water surface), cross-section area A_x = V/L (shown as a translucent purple cross-section plane), top width T = A_s/L (shown as a horizontal line at the water surface on the cross-section), wetted perimeter P = A_b/L (shown as a red line along the channel bed on the cross-section). Style: clean technical 3D illustration, blue water, brown terrain, white background, clearly labeled."

**Existing image(s):** `fig_15_03.png`

### Figure 15.4

**Caption:** Flood inundation map for the Onion Creek watershed based on HAND analysis with reach-specific depth assignments corresponding to the October 2013 event. Different reaches carry different depths (Table 15.4), producing spatially varying flood extents. Red dots indicate address points within the inundated area.

**Generation prompt:** "Create a map of the Onion Creek watershed near Austin, Texas, showing flood inundation from the HAND method. The watershed boundary is shown as a thin black line. Inside, seven distinct catchment zones are visible, each with a different shade of blue indicating flood depth: lighter blue for 8-foot flooding in tributaries, progressively darker blue for 15-foot flooding along the main stem. The stream network is shown as dark blue lines. A legend shows flood depth from 0 to 15 feet in graduated blue shading. Small red dots represent flooded address points. The background shows a light topographic hillshade. Style: clean cartographic map, white background outside watershed, blue gradient for flood depths, clear legend."

**Existing image(s):** `fig_15_04.png`

### Figure 15.5

**Caption:** Global coverage of operational flood forecasting and inundation mapping systems. The United States has the most complete system with real-time HAND-based inundation maps. Europe combines EFAS forecasting with pre-computed JRC hazard maps and on-demand satellite mapping. The rest of the world relies on GloFAS threshold exceedance forecasts, with HAND-based inundation mapping still under development.

**Generation prompt:** "Create a world map showing the coverage of three flood forecasting and inundation mapping systems. The continental United States is highlighted in blue with the label 'NWM + HAND (2.7M reaches, hourly, 10m)'. Europe is highlighted in green with the label 'EFAS + JRC Hazard Maps (5km, 10-day forecast)'. The rest of the world is highlighted in orange with the label 'GloFAS (0.05 deg, 30-day forecast)'. Below the map, a table shows: US = real-time inundation maps, Europe = return-period hazard maps + satellite, Global = discharge thresholds only. Style: clean world map, Mercator projection, muted colours, clear labels, white background."

**Existing image(s):** MISSING

### Figure 15.6

**Caption:** The paradigm shift in flood inundation mapping: from site-specific detailed hydraulic models covering a fraction of the stream network to systematic HAND-based mapping covering every reach. The two approaches are complementary, not competing.

**Generation prompt:** "Create a conceptual diagram showing the evolution of flood inundation mapping over time. Left side (1990s): a small area with a single detailed HEC-RAS cross-section model, labeled 'Site-specific, expert-driven, months of work, high accuracy, limited coverage.' Right side (2020s): a continental map showing HAND-based flood mapping for millions of reaches, labeled 'Systematic, automated, hours of computation, moderate accuracy, complete coverage.' An arrow connects them labeled 'Paradigm shift.' Below, two numbers: '25% of streams mapped (HEC-RAS era)' and '100% of streams mapped (HAND era).' Style: clean conceptual diagram, blue and grey tones, white background."

**Existing image(s):** MISSING

### Figure 15.7

**Caption:** The HAND method for assessing building flood risk. A building's HAND value is its height above the nearest stream. Flooding occurs when the water depth in the stream exceeds the building's HAND value. The building flood depth equals the stream depth minus the HAND value.

**Generation prompt:** "Create a cross-section diagram showing the HAND method for building flood risk assessment. Show a river channel in the center with water at normal level. On the right bank, show a house at some distance from the channel, with its elevation clearly higher than the channel. Draw a horizontal dashed line from the house down to the stream level, labeled 'HAND = height of building above stream.' Show a second scenario with flood level (higher blue water) reaching partway up to the house, with the flood depth labeled 'd' and the remaining dry height labeled 'd_building = d - HAND.' Include annotations: 'Normal flow' at low water, 'Flood level' at high water, 'Flooding occurs when d > HAND.' Style: clean technical cross-section diagram, blue for water, brown for terrain, grey for house, clear labels, white background."

**Existing image(s):** MISSING

---

## Chapter 16: Forecasting Floods in Real Time

*7 figures*

### Figure 16.1

**Caption:** The Tisza River basin, spanning five countries from the Ukrainian Carpathians to the Serbian confluence with the Danube. The basin's transboundary nature means that floods originate far upstream of Hungary, requiring international cooperation for effective forecasting. The Great Plain (Alfold) section of the Tisza is particularly vulnerable due to its flat topography and extensive levee system.

**Generation prompt:** "Create a map of Central Europe showing the Tisza River basin spanning across Ukraine, Romania, Slovakia, Hungary, and Serbia. Highlight the Tisza main stem and major tributaries (Bodrog, Sajo, Zagyva, Koros, Maros/Mures). Mark Budapest and Szeged on the Danube/Tisza. Show national borders with dashed lines. Color the upstream catchment areas in the Carpathian Mountains in green-brown, and the Hungarian Great Plain (Alfold) floodplain areas in light blue. Include a small inset showing the location within Europe. Style: clean cartographic illustration, white background, labeled rivers and cities."

**Existing image(s):** MISSING

### Figure 16.2

**Caption:** Architecture of the US National Water Model. Weather forecasts from HRRR and GFS drive the Noah-MP land surface model, which produces gridded runoff. The runoff is transformed onto NHDPlus catchments and routed through 2.7 million stream reaches by the RAPID model, producing hourly discharge forecasts.

**Generation prompt:** "Create a schematic diagram of the US National Water Model architecture showing four linked components in a vertical flow: (1) Weather Models at top (HRRR at 3km hourly and GFS at 10-day), with arrow down to (2) Noah-MP Land Surface Model at 1km grid computing runoff, with arrow down to (3) Geographic Transformation showing gridded data being mapped onto irregular NHDPlus catchments, with arrow down to (4) RAPID Channel Routing through NHDPlus network producing discharge at 2.7 million reaches. Show the time horizons: Short-range 18hr (hourly update) and Medium-range 10 days (6-hourly update). Style: clean technical diagram, white background, blue arrows connecting components, labeled boxes."

**Existing image(s):** `fig_16_02_a.png, fig_16_02_b.png`

### Figure 16.3

**Caption:** Comparison of pre-landfall flood predictions (left) and actual building damage (right) during Hurricane Harvey. The NWM-based forecast correctly identified Houston (Region 2) as the overwhelmingly dominant impact zone more than 36 hours before peak flooding.

**Generation prompt:** "Create a side-by-side comparison map of Texas. Left map titled 'NWM Forecast (Friday 3PM, Aug 25)' shows predicted flood impact by disaster region, with Region 2 (Houston area) colored deep red indicating 238,000 addresses at risk, and other regions in lighter shades. Right map titled 'Actual Damage (TDEM Records)' shows 152,800 damaged buildings with similar geographic distribution. Both maps show Texas disaster region boundaries. An arrow between the maps indicates 'Forecast issued 36 hours before peak flooding.' Style: clean cartographic comparison, white background, red-orange color gradient for intensity."

**Existing image(s):** `fig_16_03_a.png, fig_16_03_b.png`

### Figure 16.4

**Caption:** Architectural comparison of the US National Water Model and the European Flood Awareness System. The most significant differences are in weather input philosophy (deterministic vs. ensemble), routing approach (vector network vs. grid-based), and uncertainty communication (single forecast vs. probabilistic).

**Generation prompt:** "Create a schematic diagram comparing the architectures of the US National Water Model (left) and the European Flood Awareness System (right) side by side. Left column: HRRR (deterministic, 3km, hourly) → Noah-MP (1km grid) → NHDPlus catchment transformation → RAPID vector routing → 2.7M reach forecasts. Right column: ECMWF Ensemble (51 members, 9km, twice daily) → LISFLOOD (5km grid, integrated) → Grid-based routing → Probabilistic flood forecasts. Highlight key differences: deterministic vs ensemble, vector vs grid routing, national vs multinational. Style: clean technical comparison diagram, white background, US side in blue, EU side in gold/yellow."

**Existing image(s):** MISSING

### Figure 16.5

**Caption:** Three major Tisza flood events in the 21st century. Each event tested the Hungarian flood defense system in different ways: the 2001 flood set records on the Upper Tisza, the 2006 flood was unprecedented in duration and geographic extent, and the 2010 flood coincided with simultaneous Danube flooding, stretching national resources.

**Generation prompt:** "Create a timeline chart showing three major Tisza flood events (2001, 2006, 2010). For each event, show a simplified hydrograph at a representative station (Vasarosnameny or Szolnok) with the three alert thresholds (I., II., III. fokozat) marked as horizontal dashed lines. Below each hydrograph, include key statistics: peak water level (cm), area inundated (km2), people evacuated, and damage (EUR millions). Show the record-setting 2001 peak at Vasarosnameny. Style: clean technical chart, white background, blue hydrographs, red dashed threshold lines, labeled annotations."

**Existing image(s):** MISSING

### Figure 16.6

**Caption:** The three-tier flood observation architecture. Higher tiers provide more measurements per station but at greater cost and lower spatial density. The combination of all three tiers provides both the accuracy (Tier 1) and the coverage (Tier 3) needed for comprehensive flood monitoring.

**Generation prompt:** "Create a diagram showing the three-tier flood observation architecture. Arrange three tiers vertically with Tier 1 (full gauging station) at top, Tier 2 (bridge radar sensor) in middle, and Tier 3 (simple water level sensor) at bottom. On the left vertical axis, show cost increasing upward. On the right vertical axis, show spatial density increasing downward. For each tier, show a small icon of the instrument type and list what it measures. Include example deployments (USGS for Tier 1, TxDOT bridge sensors for Tier 2, City flood alert for Tier 3). Style: clean infographic, white background, blue-green color scheme, labeled icons."

**Existing image(s):** `fig_16_06_a.png, fig_16_06_b.png, fig_16_06_c.png`

### Figure 16.7

**Caption:** Global coverage of operational flood forecasting systems. The US National Water Model and European EFAS provide the highest-resolution national/continental forecasts. GloFAS extends coverage globally at coarser resolution. Several countries operate additional national systems. Large areas of Africa, Central Asia, and the Pacific Islands depend entirely on GloFAS or have no operational flood forecasting.

**Generation prompt:** "Create a world map showing the coverage and spatial resolution of major operational flood forecasting systems. Color the continental US in dark blue (NWM, 1km / reach-level). Color Europe in gold (EFAS, 5km). Color the rest of the world in light green (GloFAS, 5km global). Overlay dots for national systems in countries that have their own operational capability (India, China, Japan, Australia, Brazil) in orange. Include a legend with system names and resolutions. Indicate regions with no operational capability in light gray. Style: clean cartographic illustration, Mercator or Robinson projection, white background, clear legend."

**Existing image(s):** MISSING

---

## Chapter 17: Who Lives in the Flood Zone?

*7 figures*

### Figure 17.1

**Caption:** The three components of flood risk and the data that feed each one. Hazard mapping (Chapters 14-16) provides the physical flood extent. Demographic data from census systems provide exposure and vulnerability. The intersection of all three determines who is at risk and how severely.

**Generation prompt:** "Create a conceptual diagram showing the Risk = Hazard x Exposure x Vulnerability equation. Three overlapping circles: (1) Hazard circle contains a flood inundation map, (2) Exposure circle contains building footprints and population counts, (3) Vulnerability circle contains icons for elderly, children, poverty, disability. The intersection of all three is labeled 'Flood Risk'. Below, show data sources for each component: Hazard = DEM + hydrological models, Exposure = Census + building registry, Vulnerability = socioeconomic data. Style: clean vector illustration, white background, blue for hazard, orange for exposure, red for vulnerability."

**Existing image(s):** MISSING

### Figure 17.2

**Caption:** Comparison of the US Census and Hungarian KSH geographic hierarchies. The US system is finer-grained at the bottom (11 million blocks vs. approximately 3,155 municipalities), but both follow the same nested principle. The Hungarian hierarchy maps onto the EU NUTS classification, enabling cross-border comparisons across all 27 EU member states.

**Generation prompt:** "Create a side-by-side comparison diagram of US and Hungarian census geographic hierarchies. Left side: US hierarchy from Nation down to Census Block, with example counts (50 states, 3200 counties, 74000 tracts, 220000 block groups, 11M blocks). Right side: Hungarian hierarchy from Orszag down to Szamlalokoorzet, with NUTS codes shown alongside (HU, HU1, HU33, etc.) and counts (19 megyek + Budapest, 174 jarasok, 3155 telepulesek). Color-code matching levels. Style: clean vector illustration, white background, two columns with connecting lines between comparable levels."

**Existing image(s):** `fig_17_02.png`

### Figure 17.3

**Caption:** The same region viewed through three population datasets at different resolutions. Municipality-level census data (left) assigns uniform population to large administrative polygons. LandScan at 1 km (centre) reveals the broad population pattern. WorldPop at 100 m (right) resolves individual settlements and urban density gradients. For hydrological analysis, finer resolution produces more accurate population estimates when clipping to irregular watershed boundaries.

**Generation prompt:** "Create a three-panel map comparison showing population data at different resolutions for the same region (a medium-sized European city and its surroundings). Left panel: census municipality polygons with population choropleth (coarse, blocky). Center panel: LandScan 1 km grid with population density (medium resolution, gridded). Right panel: WorldPop 100 m grid with population density (fine resolution, showing individual settlement clusters). Label each panel with dataset name and resolution. Style: clean cartographic illustration, sequential blue-to-red color ramp for population density, white background."

**Existing image(s):** MISSING

### Figure 17.4

**Caption:** The boundary mismatch problem in population estimation. Census blocks (gray) rarely align with watershed boundaries (blue). The naive clip method (centre) overestimates by including the full population of every intersecting block. The density-corrected method (right) allocates population proportionally to the clipped area.

**Generation prompt:** "Create a technical diagram illustrating the population clip problem. Left panel: a watershed boundary (irregular polygon, blue outline) overlaid on census block polygons (regular grid-like shapes with population counts inside). Some blocks are entirely inside the watershed, some entirely outside, and several straddle the boundary. Center panel: the naive clip approach -- all straddling blocks are fully included, with their population highlighted in red to show overestimation. Right panel: the density-corrected approach -- straddling blocks are proportionally allocated, with a formula showing Population = Density x Clipped Area. Style: clean vector diagram, white background, blue watershed outline, gray census blocks, red highlights for overestimation."

**Existing image(s):** `fig_17_04_a.png, fig_17_04_b.png, fig_17_04_c.png`

### Figure 17.5

**Caption:** Spatial patterns of demographic characteristics in Travis County, Texas. (A) Median household income reveals a sharp east-west divide. (B) Median age shows young populations near the university and older populations in western suburbs. (C) Population growth concentrates on the suburban periphery. (D) Mobile home concentrations in eastern areas indicate higher structural vulnerability to flooding.

**Generation prompt:** "Create a four-panel thematic map of Travis County, Texas. Panel A: Median household income by block group, with a diverging color ramp (red for low income, blue for high income), showing the east-west divide. Panel B: Median age by block group, showing young population near downtown and older population in western suburbs. Panel C: Population growth rate by tract, showing high growth in northern and eastern periphery. Panel D: Percent of housing units that are mobile homes, showing concentration in eastern Travis County. Each panel labeled A-D with a brief title. Style: clean cartographic maps, white background, consistent county outline, labeled major features (Colorado River, downtown Austin, Round Rock)."

**Existing image(s):** `fig_17_05_a.png, fig_17_05_b.png, fig_17_05_c.png, fig_17_05_d.png`

### Figure 17.6

**Caption:** Flood exposure by district in Borsod-Abauj-Zemplen megye. Districts along the Tisza-Bodrog confluence (Cigandi, Tokaji) have the highest proportions of population in the 100-year flood zone, while the largest absolute numbers of exposed people are in the Miskolci district along the Sajo River.

**Generation prompt:** "Create a thematic map of Borsod-Abauj-Zemplen county, Hungary, showing flood exposure by district. The county outline in black, district boundaries in thin gray lines. Major rivers (Sajo, Hernad, Bodrog, Tisza) shown as blue lines. Each district colored by percent of population in the 100-year flood zone, using a sequential yellow-to-red color ramp. Label the most affected districts (Cigandi, Tokaji, Szerencsi). Include an inset showing BAZ megye's location within Hungary. Label Miskolc as the county seat. Style: clean cartographic illustration, white background, north arrow and scale bar."

**Existing image(s):** MISSING

### Figure 17.7

**Caption:** Complete workflow for demographic flood exposure analysis, showing how hazard data (from flood mapping) and population data (from census systems or gridded datasets) combine through GIS overlay operations to produce population exposure counts, vulnerability profiles, and risk maps.

**Generation prompt:** "Create a workflow diagram for demographic flood exposure analysis. Show four horizontal swim lanes labeled 'Hazard Data', 'Population Data', 'GIS Analysis', and 'Results'. In the Hazard lane: icons for FEMA flood map, JRC flood map, and HAND-based flood map feeding into a 'Flood Zone Boundary' box. In the Population lane: icons for Census blocks, KSH municipality data, WorldPop grid, and LandScan feeding into a 'Population Layer' box. In the GIS Analysis lane: the two inputs merge into operations labeled 'Clip/Overlay', 'Density Correction', and 'Zonal Statistics'. In the Results lane: outputs include 'Exposed Population Count', 'Vulnerability Profile', and 'Risk Map'. Style: clean flowchart, white background, blue for hazard, orange for population, green for analysis, red for results."

**Existing image(s):** MISSING

---

## Chapter 18: Seeing Underground: 3D Subsurface GIS

*7 figures*

### Figure 18.1

**Caption:** Schematic geological cross-section through the Great Hungarian Plain, showing the layered structure that demands 3D representation. The shallow Quaternary aquifer, deep Pannonian thermal aquifer system, and crystalline basement each have distinct hydrogeological properties. Boreholes of varying depth provide the only direct observations of subsurface conditions.

**Generation prompt:** "Create a technical cross-section diagram showing the layered geology of the Great Hungarian Plain (Alfold). From top to bottom: thin Quaternary alluvium layer (yellow, 10-50m), thick Pannonian sediments with alternating sand (orange dots) and clay (brown) layers extending to 2000m depth, and pre-Neogene crystalline basement (dark gray with crosshatch). Show three boreholes of different depths penetrating the layers, with temperature annotations (15C near surface, 50C at 1000m, 90C at 2000m). Include the Tisza River at the surface. Style: clean geological cross-section, white background, labeled layers, vertical exaggeration noted as 50x."

**Existing image(s):** MISSING

### Figure 18.2

**Caption:** The three Z-enabled geometry types in geodatabases. PointZ features represent individual borehole contacts as discrete 3D points. PolylineZ features represent entire boreholes as continuous lines through 3D space. PolygonZ features define surfaces in 3D, such as the top of a geological formation. All three types store z coordinates at every vertex of the geometry.

**Generation prompt:** "Create a technical diagram showing the three Z-enabled geometry types used in subsurface GIS. Left panel: PointZ features showing a vertical stack of colored dots representing borehole contacts at different depths, with x,y,z coordinates labeled for each. Center panel: PolylineZ feature showing a borehole as a vertical line with vertices at contact depths, with small colored segments indicating different geological units. Right panel: PolygonZ feature showing a tilted polygon in 3D space representing the top of a geological formation, with vertices labeled with their x,y,z coordinates. Each panel includes a small coordinate axes indicator showing x, y, and z directions. Style: clean technical illustration, white background, consistent color scheme for geological units."

**Existing image(s):** MISSING

### Figure 18.3

**Caption:** Three methods for constructing multipatch volumes. Simple extrusion stretches a flat polygon vertically between two elevations (left). The "between two surfaces" approach creates a volume between undulating top and bottom surfaces, preserving variable thickness (center). Surface stitching connects two TIN surfaces with a perimeter skirt to form a closed solid (right).

**Generation prompt:** "Create a three-panel technical diagram showing multipatch construction methods. Left panel labeled 'Simple Extrusion': a flat polygon on a horizontal plane with arrows pointing upward to show it being extruded into a rectangular 3D block, with labels 'Base elevation' and 'Top elevation'. Center panel labeled 'Between Two Surfaces': two undulating surfaces (top and bottom, shown as wireframe meshes) with the volume between them filled with semi-transparent color, showing variable thickness. Right panel labeled 'Surface Stitching': a top TIN surface and bottom TIN surface being connected by vertical triangles around the perimeter to create a closed solid. Style: clean vector illustration, white background, blue for top surfaces, brown for bottom surfaces, semi-transparent fill for volumes."

**Existing image(s):** MISSING

### Figure 18.4

**Caption:** The extrusion workflow applied to the Quaternary aquifer near Hajduszoboszlo. Starting from borehole data (panel 1), surfaces representing the formation top and base are interpolated (panel 2), the volume between them is filled (panel 3), and the result is a 3D multipatch that captures the aquifer's variable thickness (panel 4).

**Generation prompt:** "Create a technical illustration showing the extrusion workflow for the Quaternary aquifer near Hajduszoboszlo, Hungary. Four sequential panels: (1) A map view showing 47 borehole locations as dots on a topographic background, with the study area boundary outlined. (2) Two stacked surfaces: the ground surface DEM (green-brown) above and the interpolated Quaternary base surface (orange) below, with vertical lines at borehole locations connecting the two surfaces. (3) The volume between the two surfaces filled as a semi-transparent blue block representing the aquifer, with thickness varying visibly across the area. (4) A 3D perspective view of the finished multipatch with the DEM draped on top, showing the aquifer volume from an oblique angle. Style: clean technical illustration, white background, labeled panels 1-4."

**Existing image(s):** MISSING

### Figure 18.5

**Caption:** The seven-step GSIS workflow for constructing a 3D geological model. The process moves from data compilation through interpretation and interpolation to a validated volumetric model ready for groundwater simulation.

**Generation prompt:** "Create a workflow diagram showing the seven steps of GSIS-based geological modeling. Arrange as a flowchart from left to right (or top to bottom) with small illustrative icons for each step: (1) Data compilation - icon of stacked documents and a borehole log; (2) Stratigraphic framework - icon of a vertical column with colored layers; (3) Borehole entry - icon of vertical lines with contact markers; (4) Cross-section construction - icon of a 2D cross-section with colored geological units and borehole lines; (5) Surface interpolation - icon of a wireframe surface with scattered data points; (6) Volume construction - icon of a 3D block model with colored volumes; (7) Validation and export - icon of a checklist and an arrow pointing to a computer running MODFLOW. Style: clean flowchart, white background, connecting arrows between steps, labeled boxes."

**Existing image(s):** MISSING

### Figure 18.6

**Caption:** A fence diagram showing intersecting cross-sections through a subsurface geological model. The colored layers represent distinct geological formations, and the consistency of colors at cross-section intersections demonstrates that the geological interpretation is internally consistent. The semi-transparent ground surface provides geographic context.

**Generation prompt:** "Create a 3D perspective illustration showing a fence diagram of a subsurface geological model. Show three or four intersecting vertical cross-section planes arranged in a grid pattern over a landscape surface. Each cross-section shows colored geological layers (yellow for sand, brown for clay, orange for limestone, gray for basement) with visible boreholes as vertical black lines with colored markers at formation contacts. The cross-sections intersect cleanly, showing consistent geology at intersection points. The ground surface is shown as a semi-transparent green terrain draped over the top of the fence diagram. Include a small human figure or scale bar for reference. Style: clean 3D technical illustration, white background, oblique aerial perspective, slight vertical exaggeration."

**Existing image(s):** MISSING

### Figure 18.7

**Caption:** A common error in 3D subsurface modeling: allowing interpolated formation surfaces to cross each other, creating geologically impossible negative-thickness zones (left). Properly constrained surfaces maintain positive thickness everywhere (right). Always check for surface intersections before building volume models.

**Generation prompt:** "Create a diagram showing two side-by-side 3D geological cross-sections. Left panel labeled 'Incorrect: Surfaces Cross' shows two interpolated formation surfaces (blue wireframe for top surface, red wireframe for bottom surface) that intersect each other in the middle of the model, creating an impossible negative-thickness zone highlighted with a red warning symbol. Right panel labeled 'Correct: Surfaces Constrained' shows the same two surfaces properly separated everywhere, with positive thickness throughout, and a green checkmark. Below each panel, a simple thickness map is shown: left has negative values (colored red), right has all positive values (colored blue-green). Style: clean technical illustration, white background, clear labeling."

**Existing image(s):** MISSING

---

## Chapter 19: Wells, Boreholes, and Aquifer Maps

*7 figures*

### Figure 19.1

**Caption:** The relationship between a geologic map (left) and an aquifer map (right) for the same region. Geologic formations are reclassified into hydrogeological units -- aquifers and confining layers -- based on their hydraulic properties. Outcrop zones (where the unit is exposed at the surface) and subcrop zones (where it is buried) are distinguished by different shading patterns.

**Generation prompt:** "Create a side-by-side comparison showing a generalized geologic map of a region on the left and the corresponding aquifer map on the right. Both maps cover the same geographic area. On the left, colored polygons represent different geologic formations (sandstone, limestone, shale, alluvium) with fault lines. On the right, the same area is reinterpreted as aquifer units (principal aquifer, minor aquifer, confining unit) with outcrop and subcrop zones distinguished by shading. Arrows connect corresponding formations to their aquifer classification. Style: clean vector illustration, white background, labeled legends."

**Existing image(s):** MISSING

### Figure 19.2

**Caption:** Major aquifer types of Hungary. The Great Plain (Alfold) is underlain by alluvial and Pannonian sand aquifers; the Transdanubian and Bukk Mountains contain karstic aquifer systems in Mesozoic carbonates; thermal water zones extend throughout the deep Pannonian Basin. The cross-section illustrates the vertical stacking of aquifer systems beneath the Great Plain.

**Generation prompt:** "Create a map of Hungary showing the major aquifer types: alluvial aquifers in the Great Plain (Alfold) in light blue, Pannonian sand aquifers in deeper blue, karstic aquifers in the Transdanubian Mountains and Bukk Mountains in green, and thermal water zones in red-orange. Include major city labels (Budapest, Debrecen, Szeged, Pecs, Miskolc). Show a cross-section line from west to east through the Great Plain. Below the map, include a simplified west-to-east geological cross-section showing the stacked aquifer systems (Quaternary alluvium, Pannonian sands, Mesozoic carbonates). Style: clean vector illustration, white background, labeled legends and axes."

**Existing image(s):** MISSING

### Figure 19.3

**Caption:** Distribution of thermal wells across Hungary, with circle size proportional to water temperature. The highest temperatures are found in the southeastern Great Plain (Alfold) where the Pannonian sedimentary fill is thickest and the geothermal gradient is highest. The inset histogram shows the temperature distribution of Hungarian thermal wells.

**Generation prompt:** "Create a map of Hungary showing the distribution of thermal wells as graduated circles (larger circles for higher temperature). Use a warm color gradient from yellow (30-40 C) through orange (40-60 C) to red (60-90+ C). Show major cities as labeled squares. Include an inset histogram showing the distribution of well temperatures. In the background, show a subtle heat-map gradient representing the geothermal gradient. Add a legend explaining the circle sizes and colors. Style: clean vector illustration, white background, geographic coordinate grid."

**Existing image(s):** MISSING

### Figure 19.4

**Caption:** The interpretation workflow from raw lithological log (left) to hydrostratigraphic classification (right). The driller's material descriptions are retained in the Material field, while the interpreted hydrogeologic unit assignments are stored in the HGUID and HGUCode fields. This dual representation preserves the primary data while enabling standardized classification for mapping and modeling.

**Generation prompt:** "Create a diagram showing the interpretation workflow from raw borehole log to hydrostratigraphic classification. On the left, show a borehole column with lithological descriptions (topsoil, clay, sand, gravel etc.) in different colors and patterns, with depth markings. In the middle, show arrows indicating the interpretation step with a geologist icon. On the right, show the same borehole reclassified into hydrostratigraphic units (Aquifer 1, Aquitard 1, Aquifer 2, Aquitard 2, Aquifer 3) with standardized colors. Below, show a table fragment representing the BoreholeLog table with Material and HGUID columns filled. Style: clean vector illustration, white background, labeled elements."

**Existing image(s):** MISSING

### Figure 19.5

**Caption:** Three-dimensional view of BoreLine features representing geological formations along five wells. Each vertical column is divided into colored segments corresponding to different lithological units. Dashed correlation lines suggest the lateral continuity of formations between wells -- a visual tool that guides the construction of three-dimensional geological models (Chapter 20).

**Generation prompt:** "Create a 3D perspective view showing five wells in a landscape. Each well is represented as a vertical column extending from the land surface downward, divided into colored segments representing different geological formations (sand in yellow, clay in brown, gravel in orange, limestone in blue, shale in gray). The land surface is shown as a semi-transparent terrain. Dashed lines connect correlated formation boundaries between adjacent wells. Include a legend mapping colors to formation names. Show depth labels on one well. Style: clean 3D vector illustration, white background, isometric perspective, labeled elements."

**Existing image(s):** MISSING

### Figure 19.6

**Caption:** Entity-relationship diagram showing the connections between feature classes in a groundwater geodatabase. The HGUID attribute provides a common key linking geological features, aquifer features, wells, and borehole data to the central HydrogeologicUnit table. Relationship cardinalities (1:M) are indicated along the connecting lines.

**Generation prompt:** "Create an entity-relationship diagram showing the connections between feature classes in a groundwater geodatabase. Show five boxes: GeologyArea (polygon), Aquifer (polygon), Well (point), BoreholeLog (table), and BorePoint/BoreLine (3D features). Draw relationship lines between them: GeologyArea links to Aquifer through HGUID, Aquifer links to Well through AquiferID-HydroID, Well links to BoreholeLog through HydroID-WellID, and BoreholeLog links to BorePoint/BoreLine as source data. All boxes also connect to a central HydrogeologicUnit table through HGUID. Use a clean UML-style diagram with cardinality notation (1:M, M:N). Style: clean vector illustration, white background, professional database diagram style."

**Existing image(s):** MISSING

### Figure 19.7

**Caption:** Transboundary aquifer systems of the Carpathian Basin. Hungary shares thermal water resources, alluvial aquifers, and karstic systems with all seven of its neighboring countries. The management of these shared resources requires international cooperation and standardized data exchange.

**Generation prompt:** "Create a map of central Europe centered on the Carpathian Basin, showing transboundary aquifer systems shared by Hungary with neighboring countries. Use colored polygons to show: Pannonian thermal water system (red-orange, covering most of the basin), Danube alluvial aquifer (light blue, along the Danube corridor), Drava-Mura alluvial aquifer (cyan, along the Drava/Mura rivers). Show country boundaries as dashed lines (Hungary, Slovakia, Romania, Serbia, Croatia, Slovenia, Austria, Ukraine). Label major rivers (Danube, Tisza, Drava, Mura). Include a legend. Style: clean vector illustration, white background, geographic coordinate grid."

**Existing image(s):** MISSING

---

## Chapter 20: Building a Picture of the Underground

*7 figures*

### Figure 20.1

**Caption:** Cross-section creation workflow. The left panel shows section lines drawn in plan view connecting borehole locations. The right panel shows the resulting vertical cross-section with GeoSection panels representing different hydrogeologic units. Each panel is a separate multipatch feature linked to its unit definition through HGUID.

**Generation prompt:** "Create a technical diagram showing the concept of geological cross-sections in a hydrogeologic framework. Left panel: plan view map showing three section lines (A-A', B-B', C-C') crossing a study area with borehole locations marked as dots. Right panel: a vertical cross-section view along line A-A' showing four colored hydrogeologic units (upper aquifer in blue, confining layer in brown, lower aquifer in green, basement in gray) with borehole logs projected onto the section plane. Labels show SectionLine features in plan view and GeoSection panels in cross-section view. Style: clean vector illustration, white background, labeled features, professional geological color scheme."

**Existing image(s):** MISSING

### Figure 20.2

**Caption:** Stacked raster surfaces from a GeoRasters catalog. Each surface represents the top of a hydrogeologic unit, indexed by HorizonID in depositional order. The volumes between successive surfaces define the three-dimensional extent of each unit.

**Generation prompt:** "Create a technical diagram showing a stack of semi-transparent raster surfaces representing formation tops in a hydrogeologic framework. Four raster grids are shown stacked vertically in a 3D perspective view, each with a different color (from bottom: gray for basement, green for lower aquifer top, brown for confining unit top, blue for upper aquifer top). Arrows on the right side indicate HorizonID values (0, 1, 2, 3) from bottom to top. A small inset shows the GeoRasters catalog table with rows for each surface. The space between surfaces is lightly shaded to suggest the volume of each hydrogeologic unit. Style: clean vector illustration, white background, 3D perspective, labeled axes (Easting, Northing, Elevation)."

**Existing image(s):** MISSING

### Figure 20.3

**Caption:** The XS2D coordinate transformation. The top panel shows the section line in plan view, curving through borehole locations. The bottom panel shows the same data in XS2D coordinates, with distance along the section line as the horizontal axis and elevation (with vertical exaggeration) as the vertical axis. PanelDivider features mark where the section line changes direction.

**Generation prompt:** "Create a technical diagram showing the XS2D coordinate transformation concept. Top panel: a plan view map with a curved section line A-A' passing through four borehole locations, with the line bending at two intermediate points. Bottom panel: the same information displayed in XS2D coordinates -- a rectangular cross-section with a horizontal axis labeled 'Distance along section (m)' and a vertical axis labeled 'Elevation (m a.s.l.)'. Four boreholes are shown as vertical columns with colored intervals representing different hydrogeologic units. Between the boreholes, colored polygon panels show the interpreted hydrogeologic units. Vertical dashed lines mark where the section line bends (PanelDivider features). Grid lines are shown in the background. An arrow from the top panel to the bottom panel indicates the coordinate transformation (x,y,z) -> (s, z*Ve). Style: clean vector illustration, white background, two-panel layout, labeled components."

**Existing image(s):** MISSING

### Figure 20.4

**Caption:** The workflow from borehole picks to three-dimensional volumes. Individual formation picks at boreholes (left) are interpolated to produce continuous raster surfaces (center-left), which are differenced to define unit thicknesses (center-right) and ultimately assembled into GeoVolume features representing the complete hydrogeologic framework (right).

**Generation prompt:** "Create a technical diagram showing the interpolation workflow from boreholes to surfaces and volumes. The diagram flows from left to right in four stages: (1) Scattered borehole locations shown as vertical lines on a terrain surface, with colored dots marking formation picks at different depths. (2) An interpolated raster surface (shown as a colored grid) representing the top of one formation, with the borehole picks shown as control points on the surface. (3) Two stacked raster surfaces with the space between them highlighted to show the volume of one hydrogeologic unit. (4) A 3D block model (GeoVolume) showing the complete hydrogeologic framework as colored solid blocks. Arrows connect each stage to the next, labeled 'Interpolation', 'Surface Differencing', 'Volume Construction'. Style: clean vector illustration, white background, four-panel horizontal layout, labeled stages."

**Existing image(s):** MISSING

### Figure 20.5

**Caption:** Schematic cross-section of the Pannonian Basin showing the major lithostratigraphic units and their hydrogeologic classification. The progressive filling of Lake Pannon created a characteristic clinoform architecture, with deep-water confining clays at the base grading upward into the deltaic sand-clay sequences that form the principal thermal aquifer system.

**Generation prompt:** "Create a schematic geological cross-section of the Pannonian Basin, oriented NW-SE across the Great Hungarian Plain. Show: (1) the pre-Neogene crystalline/carbonate basement as a rugged, faulted surface at the base, (2) Lower Pannonian deep-water marls (dark gray) overlying the basement, (3) the prograding shelf-margin clinoforms (light brown) dipping from NW to SE, representing the progressive filling of Lake Pannon, (4) Upper Pannonian delta/shelf sands (yellow) and interbedded clays (olive), showing the lateral variability of sand bodies, (5) Quaternary alluvium (light beige) at the top. On the right side, add a simplified hydrogeologic column showing the classification into: Deep Confining Unit, Thermal Aquifer System, Shallow Aquifer System. Label the major formations (Endrod Fm, Algyo Fm, Ujfalu Fm, Zagyva Fm, Quaternary). Add arrows showing thermal water flow from depth toward production wells. Horizontal scale: ~100 km. Vertical scale: 0 to -4000 m. Style: clean vector illustration, white background, professional geological cross-section style with formation colors and patterns."

**Existing image(s):** MISSING

### Figure 20.6

**Caption:** XS2D cross-section through Hajdu-Bihar County, Great Hungarian Plain. The section shows the five principal hydrogeologic units, with the dramatic basement relief of the Debrecen Trough controlling the thickness distribution of the overlying sedimentary fill. Temperature annotations illustrate the thermal gradient that makes this aquifer system one of Europe's most important geothermal resources.

**Generation prompt:** "Create a schematic 2D cross-section (XS2D style) through the Great Hungarian Plain, oriented NW-SE, approximately 80 km long. The horizontal axis is labeled 'Distance (km)' from 0 to 80. The vertical axis is labeled 'Elevation (m a.s.l.)' from -4000 to +200, with 20x vertical exaggeration noted. Show five hydrogeologic units as colored panels: (1) Pre-Neogene Basement in dark gray with a rugged, faulted top surface dropping to -4200 m in the center; (2) Lower Pannonian Confining Complex in dark olive/brown, thickening into the basin center; (3) Upper Pannonian Thermal Aquifer System in yellow/orange, relatively uniform thickness of ~700 m; (4) Pliocene-Pleistocene Transitional Zone in light brown, thin (50-100 m); (5) Quaternary Shallow Aquifer in light blue at the top, 50-150 m thick. Show 12 borehole columns as vertical lines with formation picks marked. Add temperature annotations: 10-15C at surface, 30-80C in the thermal aquifer, >100C at basement depth. PanelDivider lines at two locations where the section line bends. Style: clean vector illustration, white background, professional cross-section style with formation colors, labeled units and temperatures."

**Existing image(s):** MISSING

### Figure 20.7

**Caption:** Integration of multiple data sources into a hydrogeologic framework. Borehole logs, geological maps, geophysical surveys, remote sensing, and hydraulic test data all contribute to the framework, which is then represented through cross-sections, raster surfaces, and volume features.

**Generation prompt:** "Create a conceptual diagram showing the integration of multiple data sources into a hydrogeologic framework. At the center is a 3D block model of the subsurface showing colored hydrogeologic units. Around it, arrows point inward from five data sources: (1) Borehole logs (shown as vertical columns with colored intervals), (2) Geological maps (shown as a plan-view polygon map), (3) Geophysical surveys (shown as a seismic reflection profile), (4) Remote sensing (shown as a satellite with GRACE gravity anomaly map), (5) Pumping tests (shown as a well with drawdown cone). Below the block model, arrows point outward to three products: cross-sections, raster surfaces, and GeoVolume features. Label all components clearly. Style: clean vector illustration, white background, radial layout with central 3D model, labeled data sources and products."

**Existing image(s):** MISSING

---

## Chapter 21: Simulating Groundwater Flow

*7 figures*

### Figure 21.1

**Caption:** The three principal groundwater simulation methods. Left: the analytic element method represents aquifer features as mathematical elements (points, lines, polygons) with no grid. Center: the finite element method uses a flexible triangular mesh that conforms to boundaries and refines locally. Right: the finite difference method uses a regular rectangular grid where properties are assigned per cell.

**Generation prompt:** "Create a technical diagram showing three panels side by side comparing groundwater simulation methods. Left panel: Analytic Element Method showing a plan view with point wells, line rivers, and polygon zones superimposed analytically. Center panel: Finite Element Method showing a triangular mesh refined near a well, with irregular aquifer boundary. Right panel: Finite Difference Method showing a regular rectangular grid with cells colored by hydraulic conductivity. Each panel labeled clearly. Style: clean vector illustration, white background, labeled elements, muted color palette."

**Existing image(s):** MISSING

### Figure 21.2

**Caption:** The five feature classes of the simulation component and their relationships. Boundary defines the model extent. Cell2D and Node2D represent the model grid in plan view. Cell3D and Node3D extend the representation into three dimensions. Index fields link the 2D and 3D features.

**Generation prompt:** "Create a technical diagram showing the five feature classes of the groundwater simulation component. Top: a plan-view polygon labeled 'Boundary' showing a rectangular model extent with origin and rotation angle marked. Middle left: a grid of rectangular polygons labeled 'Cell2D' with dots at cell centers labeled 'Node2D'. Middle right: an exploded 3D view showing stacked hexahedral blocks labeled 'Cell3D' with 3D points labeled 'Node3D'. Arrows show relationships: Cell2D↔Node2D, Cell3D↔Node3D, Cell2D↔Cell3D, Node2D↔Node3D. Style: clean vector illustration, white background, light blue and gray color scheme, all labels clear."

**Existing image(s):** MISSING

### Figure 21.3

**Caption:** The MODFLOW data model workflow. Package tables are joined to Cell2D features through the CellIndex table, producing thematic map layers of model inputs and results. This join-based architecture allows any MODFLOW variable to be mapped using standard GIS tools.

**Generation prompt:** "Create a technical diagram showing the MODFLOW data model workflow. On the left, show a stack of MODFLOW package tables (LPFProperties, WEL, RIV, DRN, CHD) connected by arrows through a central CellIndex table. The CellIndex table connects via IJ field to Cell2D polygon features shown in the center as a grid map. On the right, show the resulting thematic maps: hydraulic conductivity map, head contour map, and drawdown map, each displayed as a colored grid. Arrows show the data flow from tables through joins to map layers. Style: clean vector illustration, white background, flowchart layout, labeled boxes and arrows."

**Existing image(s):** MISSING

### Figure 21.4

**Caption:** Building MODFLOW stress packages from GIS features. Well points, river polylines, recharge rasters, and drain features are overlaid with the Cell2D grid. The intersection produces records in the corresponding MODFLOW package tables with cell indices and stress parameters.

**Generation prompt:** "Create a technical diagram showing how GIS features are converted into MODFLOW stress packages. Left side shows four GIS layers stacked: well points (red dots), river polylines (blue lines), recharge raster (green gradient), and drain polylines (brown dashed lines). Center shows the Cell2D grid overlay with the GIS features intersecting grid cells. Right side shows the resulting MODFLOW package tables (WEL, RIV, RCH, DRN) with sample rows showing IJK indices and parameter values. Arrows flow from left to center to right. Style: clean vector illustration, white background, clear labels, semi-transparent overlay."

**Existing image(s):** MISSING

### Figure 21.5

**Caption:** The regional MODFLOW model of the Great Hungarian Plain. Cell2D features are colored by hydraulic conductivity, with high values (blue) in sandy areas deposited by ancestral river systems and low values (yellow) in clay-rich floodplain deposits. The Tisza River and its tributaries are represented by river (RIV) package cells. Monitoring wells (red dots) provide calibration targets.

**Generation prompt:** "Create a map of the Great Hungarian Plain showing a MODFLOW model grid overlaid on a simplified geological base map. The map shows Hungary's outline with the Great Plain (Alföld) highlighted. A zoomed inset shows the MODFLOW grid (500m cells) with Cell2D features colored by hydraulic conductivity (blue for high K in sandy areas, yellow for low K in clay areas). River features (Tisza, Körös) are shown as blue lines crossing the grid. Monitoring wells are shown as small red dots. A north arrow and scale bar are included. Style: clean cartographic illustration, white background, muted earth tones with blue water features."

**Existing image(s):** MISSING

### Figure 21.6

**Caption:** Global groundwater modeling maturity by region. Well-characterized regions (green) have extensive models and focus on maintenance and climate adaptation. Emerging regions (yellow/orange) are building capacity. Data-scarce regions (red) need fundamental investments in monitoring before reliable models can be constructed.

**Generation prompt:** "Create a world map showing the global distribution of groundwater modeling challenges. Color regions by primary challenge: green for 'well-characterized, model maintenance' (Western Europe, parts of North America), yellow for 'growing capability, data gaps' (Eastern Europe, parts of Asia), orange for 'limited data, emerging models' (Latin America, Southeast Asia), red for 'severe data scarcity' (Sub-Saharan Africa, parts of Central Asia). Include small icons: a computer for regions with advanced modeling, a well symbol for regions focused on basic monitoring, a question mark for regions with major data gaps. Style: clean cartographic illustration, white background, clear legend, no country borders emphasized."

**Existing image(s):** MISSING

### Figure 21.7

**Caption:** The evolution of groundwater modeling practice from 1984 to 2026. The trajectory moves from standalone text-file models on single computers to GIS-integrated, cloud-computed, AI-augmented modeling systems served through web interfaces.

**Generation prompt:** "Create a technical diagram showing the evolution of groundwater modeling from 1984 to 2026. Timeline format with four eras: '1984-1995: Desktop MODFLOW' showing a single PC with text files; '1995-2010: GUI Pre-processors' showing Visual MODFLOW and GMS interfaces; '2010-2020: GIS Integration' showing MODFLOW models embedded in geodatabases with map outputs; '2020-2026: Cloud + AI' showing cloud computing icons, Python scripts, ML surrogate models, and web dashboards. Arrows connect the eras showing progression. Style: clean timeline illustration, white background, icons representing each era, blue-gray color scheme."

**Existing image(s):** MISSING

---

## Chapter 22: When Models Meet Data

*7 figures*

### Figure 22.1

**Caption:** The fundamental scale mismatch between field measurements and model parameters. Point-scale measurements of soil hydraulic conductivity, vegetation properties, and channel roughness must be translated into grid-scale effective values that make the model equations work at a much larger spatial support. This upscaling is the root cause of the calibration problem.

**Generation prompt:** "Create a technical diagram showing the parameter problem in hydrology. Left side: a natural landscape with heterogeneous soils, vegetation, channels, and rain. Right side: a model grid with uniform cells, each containing a single parameter value. Arrows connect features in the landscape to their simplified model representations. A callout shows 'point measurement: Ks = 3.6e-6 m/s' at a borehole location, while the model grid cell shows 'effective Ks = ?' Labels emphasize the scale mismatch between measurement support and model resolution. Style: clean vector illustration, white background, split-panel layout, labeled features, professional color scheme with blue for water, brown for soil, green for vegetation."

**Existing image(s):** MISSING

### Figure 22.2

**Caption:** The SCE-UA algorithm concept. Panel A shows the initial population of points distributed across a two-dimensional parameter space with multiple optima, grouped into complexes. Panel B shows the competitive evolution step within one complex. Panel C shows the shuffling and reconstitution of complexes, allowing information exchange between groups and preventing premature convergence to local optima.

**Generation prompt:** "Create a technical diagram showing the SCE-UA algorithm concept. Panel A: A 2D parameter space contour plot showing an objective function with multiple local optima (darker = better). A population of points (colored dots) is scattered across the space, grouped into three complexes (red, blue, green). Panel B: Within one complex, show the competitive evolution step with a sub-simplex triangle, the reflection of the worst point, and the new candidate point. Panel C: After shuffling, show the points redistributed among complexes with mixed colors. An arrow indicates the progression from scattered initial population to converged final population near the global optimum. Style: clean vector illustration, white background, three-panel layout, contour lines in grayscale, complex points in distinct colors, arrows showing evolution direction."

**Existing image(s):** MISSING

### Figure 22.3

**Caption:** A two-objective Pareto front from multi-objective calibration of a rainfall-runoff model. Each point on the front represents a non-dominated parameter set offering a different trade-off between Nash-Sutcliffe Efficiency and percent bias. The modeler selects a solution based on the intended application. Gray dots represent dominated (suboptimal) solutions.

**Generation prompt:** "Create a technical diagram showing a two-objective Pareto front from hydrological model calibration. X-axis: 'NSE (higher is better)', range 0.5 to 0.9. Y-axis: 'Absolute PBIAS (lower is better)', range 0 to 25%. A curved Pareto front (thick blue line with points) extends from upper left (high PBIAS, high NSE) to lower right (low PBIAS, moderate NSE). Gray dots behind the front represent non-optimal solutions. Two specific points on the front are highlighted and labeled: 'Flood warning selection (NSE=0.85, PBIAS=12%)' and 'Water supply selection (NSE=0.72, PBIAS=2%)'. The region behind the front is shaded and labeled 'infeasible region' while the area in front is labeled 'feasible but suboptimal.' Style: clean vector illustration, white background, labeled axes, professional color scheme."

**Existing image(s):** MISSING

### Figure 22.4

**Caption:** The equifinality problem in hydrological calibration. Panel A shows a two-dimensional parameter space where multiple, widely separated regions achieve similarly high NSE values -- different parameter sets that all fit the data well. Panel B shows the corresponding simulated hydrographs, which are nearly indistinguishable from each other and from observations despite coming from very different parameter combinations.

**Generation prompt:** "Create a technical diagram showing the equifinality concept. Panel A: A 2D parameter space (X-axis: 'Curve Number CN', Y-axis: 'Baseflow recession constant k') with contour lines of NSE. Multiple distinct regions of high NSE (>0.7) are visible, connected by an elongated ridge. Three specific parameter sets are marked with stars and labeled 'Set A', 'Set B', 'Set C'. Panel B: Three overlaid hydrographs (observed as black dots, Set A as red line, Set B as blue line, Set C as green dashed line) that are nearly identical despite coming from different parameter sets. X-axis: 'Time (days)', Y-axis: 'Discharge (m3/s)'. Style: clean vector illustration, white background, two-panel layout, contour lines in grayscale, distinct colored lines for different parameter sets."

**Existing image(s):** MISSING

### Figure 22.5

**Caption:** The data assimilation cycle. At each time step, the model forecast (blue) is combined with the observation (red) to produce an analysis (green) that is closer to reality than either alone. The analysis serves as the initial condition for the next forecast. At the current time, the analysis initializes a forecast ensemble whose spread indicates prediction uncertainty, which grows with lead time.

**Generation prompt:** "Create a technical diagram showing the data assimilation cycle in hydrological forecasting. A timeline runs left to right showing time steps t-2, t-1, t, t+1, t+2. At each past time step, show a model forecast trajectory (blue line with uncertainty band) being pulled toward an observation (red dot with error bar) to produce an analysis (green dot). At the present time (t), the latest analysis provides the initial condition for a forecast ensemble (multiple blue trajectories diverging into the future). The area between the ensemble members is shaded to show the prediction uncertainty increasing with lead time. Label the forecast step and analysis step. Style: clean vector illustration, white background, horizontal timeline, blue for model, red for observations, green for analysis, shaded uncertainty bands."

**Existing image(s):** MISSING

### Figure 22.6

**Caption:** Calibration results for GR4J on the Hernad catchment at Hidasnemeti. The top panel shows observed and simulated daily discharge for a representative two-year period, with the 90% prediction uncertainty band from DREAM posterior sampling. The bottom panel shows the observed-vs-simulated scatter plot colored by season, with KGE and NSE performance statistics.

**Generation prompt:** "Create a technical diagram showing calibration results for a rainfall-runoff model. Top panel: Observed daily discharge (black line) vs. simulated discharge (blue line) with 90% prediction uncertainty band (light blue shading) for a 2-year period. X-axis: time from Jan 2013 to Dec 2014. Y-axis: discharge in m3/s (0 to 200). A few prominent flood peaks are visible. The uncertainty band widens during high flows. Below the main plot, a bar chart shows daily precipitation (inverted, blue bars hanging from top). Bottom panel: Scatter plot of observed vs. simulated daily discharge with 1:1 line, colored by season (blue = winter, green = spring, red = summer, orange = autumn). KGE = 0.82 and NSE = 0.79 shown as text. Style: clean vector illustration, white background, two-panel layout, time series in top panel, scatter in bottom panel, professional color scheme."

**Existing image(s):** MISSING

### Figure 22.7

**Caption:** Global coverage of large-sample hydrology datasets used for calibration research. The LamaH-CE dataset covers 859 catchments in Central Europe, including the entire Danube basin and all major Hungarian river systems. These standardized datasets enable systematic comparison of model performance and calibration strategies across diverse hydroclimatic conditions.

**Generation prompt:** "Create a map showing the coverage of major large-sample hydrology datasets. Background: world map in light gray. Overlay colored regions: CAMELS-US (671 catchments, blue dots in contiguous US), CAMELS-GB (671 catchments, green dots in Great Britain), CAMELS-BR (orange dots in Brazil), LamaH-CE (red dots in Central Europe including the Danube basin and Hungary highlighted). Include an inset zooming into Central Europe showing LamaH-CE catchment boundaries with the Tisza basin highlighted. Legend identifies each dataset by color and number of catchments. Style: clean vector illustration, white background, simplified world map, distinct colors per dataset, inset panel for Central Europe."

**Existing image(s):** MISSING

---

## Chapter 23: AI as a Hydrologist's Assistant

*8 figures*

### Figure 23.1

**Caption:** Observed versus LSTM-predicted daily discharge for the Tisza at Szolnok during a representative test year. The model captures the overall hydrograph shape and timing of peaks, but underestimates the magnitude of the largest spring flood event.

**Generation prompt:** "Create a time series plot showing observed (blue) and LSTM-predicted (red dashed) daily discharge for the Tisza River at Szolnok over a one-year test period. The x-axis shows months (Jan--Dec), the y-axis shows discharge in m3/s. Include a major flood peak in spring where the prediction slightly underestimates the observed peak. Add a gray shaded band showing the prediction uncertainty. Style: clean scientific plot, white background, labeled axes, legend in upper right."

**Existing image(s):** MISSING

### Figure 23.2

**Caption:** Comparison of MOD16 (left) and ML-estimated (right) monthly evapotranspiration for Hungary in July 2021. The ML model captures the elevated ET in irrigated areas of the Great Hungarian Plain that the physically based MOD16 product underestimates.

**Generation prompt:** "Create a comparison figure with two maps side by side showing monthly evapotranspiration over Hungary for July 2021. Left map: MOD16 product showing systematic underestimation in the Great Hungarian Plain. Right map: ML-estimated ET showing higher values in irrigated agricultural areas. Color scale from dark brown (low ET, 1 mm/day) through yellow-green to dark blue (high ET, 6 mm/day). Include major rivers (Danube, Tisza) as thin white lines. Style: clean cartographic presentation, white background, scale bar, north arrow."

**Existing image(s):** MISSING

### Figure 23.3

**Caption:** Groundwater level observations and 30-day-ahead predictions from three models at a monitoring well in the Great Hungarian Plain. The LSTM (red) most closely tracks the observed seasonal pattern and drought-related decline, though all models struggle with the rate of recovery after the drought.

**Generation prompt:** "Create a time series plot showing groundwater level observations (blue dots, weekly frequency) and three model predictions over a 2-year period: persistence (gray dashed), XGBoost (green), and LSTM (red). The x-axis shows months, the y-axis shows depth to water table in meters below surface (inverted, so shallower is higher on the plot). Show a clear seasonal pattern with spring recharge highs and summer lows, and a notable drought period where the LSTM prediction tracks the decline better than XGBoost. Style: clean scientific plot, white background, labeled axes, legend."

**Existing image(s):** MISSING

### Figure 23.4

**Caption:** ML-predicted mean annual nitrate-N concentration in Hungarian streams, validated against monitoring stations (colored circles). The spatial pattern reflects the dominance of agricultural land use in the Great Hungarian Plain as a driver of diffuse nitrate pollution.

**Generation prompt:** "Create a map of Hungary showing predicted mean annual nitrate-N concentration in streams, with monitored stations shown as colored circles (observed values) and the background showing the ML-predicted spatial pattern. Color scale from green (low, <10 mg/L) through yellow (moderate, 10-25 mg/L) to red (high, >50 mg/L). The Great Hungarian Plain shows higher predicted values (yellow-orange) due to intensive agriculture, while the Transdanubian Hills and Northern Mountains show lower values (green). Include county boundaries as thin gray lines and major rivers as blue lines. Style: clean cartographic map, white background, legend, scale bar."

**Existing image(s):** MISSING

### Figure 23.5

**Caption:** The U-Net architecture for land cover classification from Sentinel-2 imagery. The encoder path extracts multi-scale spatial features, the decoder path restores spatial resolution, and skip connections preserve fine detail. The input is a multi-band satellite image patch; the output is a per-pixel classification map.

**Generation prompt:** "Create a diagram showing the U-Net architecture for land cover classification. Show the encoder path (left side) with progressively smaller feature maps through conv+pool operations, the bottleneck at the bottom, and the decoder path (right side) with progressively larger feature maps through upsampling+conv operations. Show skip connections as horizontal arrows connecting encoder to decoder at matching resolutions. Label the input as 'Sentinel-2 patch (256x256, 10 bands)' and the output as 'Classification map (256x256, 8 classes)'. Use blue for encoder blocks, green for decoder blocks, and gray for skip connections. Style: clean technical diagram, white background."

**Existing image(s):** MISSING

### Figure 23.6

**Caption:** Transfer learning workflow for hydrologic prediction at ungauged catchments. A model pre-trained on hundreds of well-gauged catchments is transferred to a data-poor catchment and optionally fine-tuned with limited local data, substantially improving prediction accuracy compared to direct regionalization.

**Generation prompt:** "Create a conceptual diagram showing the transfer learning workflow for hydrology. On the left, show 'Source Domain' with icons for many gauged catchments (500+ catchments with long records) feeding into a large LSTM model. An arrow labeled 'Pre-trained weights' points to a smaller model in the center labeled 'Transfer'. On the right, show 'Target Domain' with a single ungauged catchment with limited data, and an arrow from the small transferred model to a prediction hydrograph. Below, show a bar chart comparing NSE for four scenarios: No model, Pre-trained only, Fine-tuned (1yr), Fine-tuned (3yr). Style: clean diagram with blue/green color scheme, white background."

**Existing image(s):** MISSING

### Figure 23.7

**Caption:** SHAP waterfall plot explaining a single flood discharge prediction. The upstream discharge two days ago and yesterday's precipitation are the dominant positive contributors, consistent with the physical flood wave propagation mechanism. Such instance-level explanations help hydrologists trust and debug ML predictions.

**Generation prompt:** "Create a SHAP (SHapley Additive exPlanations) waterfall plot for a single flood prediction. The y-axis lists input features: 'Upstream Q (lag 2d)', 'Precipitation (lag 1d)', 'Soil moisture', 'Temperature', 'Upstream Q (lag 5d)', 'Season (cos)', 'Base value'. The x-axis shows the contribution to the predicted discharge value. Red bars push the prediction higher (upstream Q lag 2d has the largest positive contribution), blue bars push it lower (temperature has a small negative contribution). The final predicted value is shown at the top. Style: clean bar chart, white background, red/blue color scheme, labeled axes."

**Existing image(s):** MISSING

### Figure 23.8

**Caption:** Integration of Google Earth Engine with the Python ML ecosystem for hydrologic applications. GEE provides planetary-scale data access and basic ML capabilities; Python tools provide advanced model training and interpretation. The hybrid workflow leverages the strengths of both platforms.

**Generation prompt:** "Create a workflow diagram showing the integration of Google Earth Engine with Python ML tools. On the left, show GEE cloud with icons for satellite imagery (Sentinel-2, MODIS), climate data (ERA5), and the GEE ML API (Random Forest, SVM). An arrow labeled 'Feature extraction / Export' points to the center, where Python tools are shown: scikit-learn, XGBoost, PyTorch. On the right, show outputs: land cover maps, ET maps, streamflow predictions. Below, show the alternative GEE-only path for planetary-scale classification. Style: clean flow diagram, blue/green/orange color scheme, white background."

**Existing image(s):** MISSING

---

## Chapter 24: Agentic AI: The Autonomous Modeler

*6 figures*

### Figure 24.1

**Caption:** The agentic AI loop. The large language model serves as the reasoning engine at the center, orchestrating a cycle of planning, tool execution, result evaluation, and iterative refinement. External tools (model runner, data reader, statistical evaluator, plotter) are called as needed. A human-in-the-loop pathway allows the agent to escalate decisions that exceed its confidence.

**Generation prompt:** "Create a technical diagram showing the agentic AI loop for hydrological model calibration. Show a circular workflow with four main phases: PLAN (brain icon with checklist), EXECUTE (gear icon running a model), EVALUATE (chart showing observed vs simulated hydrograph), and ITERATE (arrows showing parameter adjustment). In the center, show an LLM reasoning engine. Around the outside, show tool connections: model runner, data fetcher, optimizer, evaluator. Include a 'Human-in-the-loop' element connected by a dashed line for escalation. Style: clean vector illustration, white background, labeled components, professional technical diagram."

**Existing image(s):** MISSING

### Figure 24.2

**Caption:** Architecture of a hydrological modeling agent. The LLM reasoning engine orchestrates four core tools -- data reader, model runner, evaluator, and visualizer -- through iterative tool calls. Memory maintains the calibration history across iterations. The human operator can intervene through an escalation pathway.

**Generation prompt:** "Create a technical architecture diagram of a hydrological modeling agent. Show a central 'LLM Reasoning Engine' box connected to four tool boxes arranged around it: 'Data Reader' (with icons for shapefiles, CSV, raster), 'Model Runner' (with HEC-HMS, SWAT, GR4J logos), 'Evaluator' (with NSE, KGE, PBIAS labels), and 'Visualizer' (with a small hydrograph plot). Show arrows indicating data flow: goal input from top, tool calls going out, tool results coming back. Include a 'Memory / Context' database on the side and a 'Human Operator' figure connected by a dashed escalation line. Style: clean vector illustration, white background, labeled components, system architecture style."

**Existing image(s):** MISSING

### Figure 24.3

**Caption:** Calibration results for the Zala River GR4J model after six agent-driven iterations. Left: observed and simulated hydrographs for 2015-2016. Right: scatter plot of daily observed vs. simulated discharge with performance metrics. The agent achieved KGE = 0.78 in only six model runs.

**Generation prompt:** "Create a figure with two panels showing hydrological model calibration results. Left panel: observed (blue solid line) vs. simulated (red dashed line) daily discharge hydrograph for 2015-2016, showing good agreement for most events but slight underestimation of the largest peak. X-axis: date, Y-axis: discharge (m3/s). Right panel: scatter plot of observed vs. simulated daily discharge with a 1:1 line, showing points clustered around the line with slight spread at high flows. Include text annotations: NSE=0.74, KGE=0.78, PBIAS=-0.3%. Style: clean scientific plot, white background, legible labels, publication quality."

**Existing image(s):** MISSING

### Figure 24.4

**Caption:** Uncertainty quantification through agent-guided ensemble generation. The gray band represents the 5th-95th percentile range from a 40-member ensemble generated by the agent along identified equifinal parameter ridges. The observed discharge (blue dots) falls within the uncertainty band for the majority of time steps, including the largest flood peak (inset).

**Generation prompt:** "Create a figure showing uncertainty quantification from an agent-generated ensemble. Show a hydrograph for a 3-month period with: observed discharge as blue dots, the best calibration run as a red line, and a shaded gray band showing the 5th-95th percentile uncertainty from a 40-member ensemble. Include a zoomed inset of the largest flood peak showing how the observed value falls within the uncertainty band. Annotate with 'Ensemble: 40 runs' and 'Observed within 90% band'. Style: clean scientific plot, white background, publication quality, labeled axes (Date, Discharge m3/s)."

**Existing image(s):** MISSING

### Figure 24.5

**Caption:** The Zala River catchment upstream of Zalaegerszeg (930 km$^2$) in western Hungary. The catchment is predominantly agricultural (yellow-brown) with forested hills (green) in the upper portions. The gauge at Zalaegerszeg (red triangle) is located before the river enters the broad Zala valley leading to Lake Balaton. Inset shows the location within Hungary.

**Generation prompt:** "Create a map of the Zala River catchment in western Hungary showing: the catchment boundary (bold black line), the river network (blue lines), the Zalaegerszeg gauge location (red triangle), sub-catchment divisions, and a small inset map showing the location within Hungary (with Lake Balaton visible to the east). Include Corine Land Cover coloring: green for forest, yellow-brown for agricultural land, gray for urban areas. Label key features: Zala River, Zalaegerszeg, Gocs Hills, and Lake Balaton. Style: clean cartographic style, white background, scale bar, north arrow, labeled features."

**Existing image(s):** MISSING

### Figure 24.6

**Caption:** Evolution of hydrological model calibration methods. Each approach coexists with and complements the others rather than replacing them. Agentic AI (emerging 2024-2026) adds diagnostic reasoning and domain knowledge integration to the calibration toolkit, complementing the mathematical rigor of optimization and Bayesian methods.

**Generation prompt:** "Create a conceptual timeline diagram showing the evolution of hydrological model calibration from 1970 to 2030. Show four eras: 'Manual Trial and Error' (1970-1990, icon: person with calculator), 'Automatic Optimization (SCE-UA, DDS)' (1990-2010, icon: algorithm flowchart), 'Bayesian Methods (DREAM, GLUE)' (2005-2025, icon: probability distribution), and 'Agentic AI' (2024-2030, icon: LLM brain with tools). Show overlapping bars indicating that methods coexist rather than replace each other. Mark key milestones: 'Duan et al. 1992 (SCE-UA)', 'Vrugt et al. 2009 (DREAM)', 'LLM agents emerge 2024'. Style: clean timeline infographic, white background, four color-coded eras, labeled milestones."

**Existing image(s):** MISSING

---

## Chapter 25: The Future of Water Intelligence

*7 figures*

### Figure 25.1

**Caption:** The layered architecture of a water system digital twin. Data flows upward from the physical system through sensor networks, model engines, and assimilation algorithms to decision support. In mature implementations, a feedback loop allows automated decisions to act upon the physical system.

**Generation prompt:** "Create a technical diagram showing the layered architecture of a water system digital twin. Five horizontal layers stacked vertically: (1) Physical System at bottom showing river, sensors, infrastructure; (2) Data Layer showing sensor streams, satellite feeds, spatial databases; (3) Model Layer showing hydrological, hydraulic, and ML models; (4) Assimilation Layer showing data-model fusion; (5) Decision Layer at top showing dashboards, alerts, automated controls. Arrows flow upward from Physical System through layers, and a feedback arrow descends from Decision Layer back to Physical System. Style: clean vector illustration, white background, blue color scheme for water elements."

**Existing image(s):** MISSING

### Figure 25.2

**Caption:** The data assimilation cycle. A model forecast (blue) diverges from observations (red dots). At each analysis step, the model state is corrected to better match observations, and the updated forecast propagates forward with reduced error.

**Generation prompt:** "Create a technical diagram showing the data assimilation cycle in a hydrological forecasting system. Show a timeline from left to right with: (1) model forecast trajectory (solid blue line) diverging from (2) observed values (red dots with error bars) at gauge stations, then (3) analysis step where the model state is corrected (dashed blue line snaps toward observations), then (4) updated forecast trajectory continuing forward. Include labels: 'Forecast', 'Observation', 'Analysis', 'Updated Forecast'. Below the timeline, show a small map with a river network and sensor locations. Style: clean vector illustration, white background, labeled axes showing time (x) and water level (y)."

**Existing image(s):** MISSING

### Figure 25.3

**Caption:** The hydroinformatics toolkit in service of climate adaptation. Tools developed throughout this book directly support the four major domains of water-related climate adaptation: flood risk reassessment, drought management, urban water resilience, and transboundary cooperation.

**Generation prompt:** "Create a diagram showing how hydroinformatics tools from different chapters serve climate adaptation domains. Four columns representing adaptation domains: Flood Risk, Drought Management, Urban Water, Transboundary. For each column, show connected boxes listing relevant tools with chapter references: DEMs (Ch 5-7), Watershed Delineation (Ch 9-11), Flood Mapping (Ch 15), LiDAR (Ch 13), Groundwater (Ch 21), Remote Sensing (Ch 8), ML/AI (Ch 23-24). Lines connect tools to the domains they serve. Style: clean vector illustration, white background, color-coded columns."

**Existing image(s):** MISSING

### Figure 25.4

**Caption:** The convergence of four technology streams --- GIS, machine learning, IoT sensors, and cloud computing --- into the integrated intelligent water system. Each pairwise intersection creates distinct capabilities; the full convergence enables autonomous, adaptive water management.

**Generation prompt:** "Create a Venn diagram showing the convergence of four technology domains in modern hydroinformatics. Four overlapping circles labeled: GIS (green), Machine Learning (blue), IoT/Sensors (orange), Cloud Computing (purple). In the overlapping regions, show key integration points: 'Cloud-native GIS' (GIS+Cloud), 'Edge ML' (ML+IoT), 'Real-time spatial analytics' (GIS+IoT), 'Scalable model training' (ML+Cloud). In the center where all four overlap, write 'Intelligent Water System'. Style: clean vector illustration, white background, semi-transparent colored circles."

**Existing image(s):** MISSING

### Figure 25.5

**Caption:** The foundation model workflow for Earth observation in hydrology. A large model pre-trained on diverse satellite data is fine-tuned with small labeled datasets for specific tasks, enabling rapid deployment of new capabilities with minimal training data.

**Generation prompt:** "Create a diagram showing the foundation model workflow for hydrological applications. Three stages from left to right: (1) Pre-training: large box showing 'Petabytes of satellite imagery' (Sentinel-2, Landsat, SAR) feeding into a neural network labeled 'Foundation Model'; (2) Fine-tuning: smaller box showing 'Small labeled dataset' (e.g., 100 flood maps) adjusting the model; (3) Deployment: the fine-tuned model applied to three tasks: 'Flood Mapping', 'Drought Monitoring', 'Land Cover Classification'. Arrows show the flow. Style: clean vector illustration, white background, with satellite imagery thumbnails in stage 1."

**Existing image(s):** MISSING

### Figure 25.6

**Caption:** Global water challenges and the institutions addressing them. Transboundary basins (blue lines), water-stressed regions (red shading), and flood-prone areas (blue shading) together define the problem space for hydroinformatics worldwide. Key basin organizations are indicated.

**Generation prompt:** "Create a world map showing global water challenges addressed by hydroinformatics. Use color coding to highlight: (1) Transboundary river basins (thin blue lines for major rivers: Danube, Nile, Mekong, Amazon, Ganges); (2) Water-stressed regions (light red shading in North Africa, Middle East, Central Asia, parts of India and China); (3) Flood-prone regions (light blue shading along major river floodplains); (4) Icons for key institutions: ICPDR on the Danube, MRC on the Mekong, NBI on the Nile. Include a legend. Style: clean vector illustration, white background, pastel colors, labeled."

**Existing image(s):** MISSING

### Figure 25.7

**Caption:** Water intelligence as a public good. Achieving this vision requires simultaneous progress in open data, open models, global cooperation, ethical AI, capacity building, and digital twin infrastructure, all centered on the shared goal of sustainable water management for all.

**Generation prompt:** "Create an inspirational diagram showing 'Water Intelligence as a Public Good'. Central image: a stylized Earth with visible water cycle (clouds, rain, rivers, groundwater). Surrounding the Earth, six interconnected elements in a circle: 'Open Data' (database icon), 'Open Models' (code/gear icon), 'Global Cooperation' (handshake icon), 'Ethical AI' (scales of justice icon), 'Capacity Building' (graduation cap icon), 'Digital Twins' (mirror/twin icon). Arrows connect all elements to each other and to the central Earth. Style: clean vector illustration, white background, blue and green color scheme, professional but slightly visionary tone."

**Existing image(s):** MISSING

---
