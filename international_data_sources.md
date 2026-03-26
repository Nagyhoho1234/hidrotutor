# International Hydrologic and Geographic Data Sources

**For students from Asia, Middle East, and Africa**
Compiled: 2026-03-25

---

## 1. Global DEM (Digital Elevation Model) Sources

### SRTM -- Shuttle Radar Topography Mission
- **URL:** https://www.earthdata.nasa.gov/data/instruments/srtm
- **Status:** WORKING (via NASA Earthdata)
- **Description:** Near-global DEM collected during an 11-day Space Shuttle Endeavour mission in February 2000 using C-band and X-band radar interferometry. The most widely used free global DEM.
- **Coverage:** ~80% of Earth's land surface (60N to 56S latitude)
- **Resolution:** 1 arc-second (~30 m) globally; 3 arc-second (~90 m) version also available
- **Access:** Free; requires NASA Earthdata login. Also available via USGS EarthExplorer and OpenTopography.
- **Alt download:** https://dwtkns.com/srtm30m/ (interactive tile downloader)

### ALOS World 3D (AW3D30) -- JAXA
- **URL:** https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm
- **Status:** WORKING
- **Description:** Global digital surface model derived from the ALOS satellite PRISM optical stereo sensor. Current version 4.1 (March 2025). Higher quality than SRTM in many mountainous and tropical regions.
- **Coverage:** Global (~23,993 tiles)
- **Resolution:** 1 arc-second (~30 m)
- **Access:** Free; requires user registration at download portal. GeoTIFF format in 1x1 or 5x5 degree tiles.

### ASTER GDEM v3
- **URL:** https://asterweb.jpl.nasa.gov/gdem.asp
- **Status:** WORKING
- **Description:** Joint METI (Japan) and NASA product. Version 3 released August 2019. Covers 83N to 83S latitude from ASTER satellite stereo imagery. Includes companion ASTER Water Body Dataset.
- **Coverage:** Near-global (83N--83S)
- **Resolution:** 1 arc-second (~30 m)
- **Access:** Free download from NASA Earthdata and Japan Space Systems.

### MERIT DEM -- Multi-Error-Removed Improved-Terrain
- **URL:** https://global-hydrodynamics.github.io/MERIT_DEM/
- **Status:** WORKING (redirected from old University of Tokyo URL)
- **Description:** High-accuracy global DEM developed by removing major error components (stripe noise, absolute bias, speckle noise, tree height bias) from existing spaceborne DEMs. Developed by Dai Yamazaki, University of Tokyo.
- **Coverage:** Global land areas, 90N--60S
- **Resolution:** 3 arc-second (~90 m)
- **Access:** Free; requires registration and license agreement (CC-BY-NC 4.0 or ODbL). GeoTIFF tiles at 5x5 degrees.

### Copernicus DEM (GLO-30)
- **URL:** https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM
- **Status:** WORKING
- **Description:** Global digital surface model derived from TanDEM-X mission observations (2011--2015). High accuracy: vertical <4 m, horizontal <6 m (90% confidence). EGM2008 vertical datum.
- **Coverage:** Global, ~149 million km2
- **Resolution:** GLO-30 = 30 m; GLO-90 = 90 m (both freely available)
- **Access:** Free; registered users can download from Copernicus Data Space. Also on AWS, OpenTopography, Google Earth Engine, and Microsoft Planetary Computer.
- **Alt access:** https://portal.opentopography.org (OpenTopography bulk download)

### TanDEM-X 90m DEM
- **URL:** https://geoservice.dlr.de/web/dataguide/tdm90/
- **Status:** WORKING
- **Description:** Product derived from the TanDEM-X global DEM (originally 12 m posting), reduced to ~90 m. Absolute vertical accuracy ~1 m. Produced by DLR (German Aerospace Center). 19,389 global tiles.
- **Coverage:** Global land masses (~150 million km2)
- **Resolution:** 3 arc-second (~90 m)
- **Access:** Free for scientific use; requires self-registration and license agreement. Download via map interface or FTP.

---

## 2. Global Hydrologic Datasets

### HydroSHEDS / HydroBASINS / HydroRIVERS
- **URL:** https://www.hydrosheds.org/
- **Status:** WORKING
- **Description:** Suite of seamless global hydrographic data layers including drainage directions, river networks (HydroRIVERS), catchment boundaries (HydroBASINS), and lake databases. HydroSHEDS v2 is under development. Essential for watershed delineation and hydrologic modeling worldwide.
- **Coverage:** Global
- **Resolution:** 3--15 arc-seconds depending on product
- **Access:** Free download from website.

### GloFAS -- Global Flood Awareness System
- **URL:** https://global-flood.emergency.copernicus.eu/
- **Status:** WORKING (redirected from globalfloods.eu)
- **Description:** Operational global flood forecasting system implemented by the European Commission under Copernicus. Provides flood forecasts up to 30 days ahead and seasonal outlooks up to 4 months. Version 4.0 at 0.05-degree resolution.
- **Coverage:** Global
- **Resolution:** 0.05 degrees (~5 km)
- **Access:** Free; interactive map viewer and data download tools available.

### GRDC -- Global Runoff Data Centre
- **URL:** https://grdc.bafg.de/
- **Status:** WORKING (redirected from bafg.de/GRDC)
- **Description:** International data centre under WMO auspices (established 1988). Maintains the most comprehensive global collection of quality-assured river discharge data. Includes basin layers, freshwater flux data, and special regional datasets (Arctic, Baltic).
- **Coverage:** Global (station-based)
- **Resolution:** Point measurements (station data)
- **Access:** Free via Data Portal; registration required for some datasets.

### GEMStat -- Global Water Quality Database
- **URL:** https://gemstat.org/
- **Status:** WORKING
- **Description:** Global water quality database providing data on the state and trends of inland water quality. Operational part of the GEMS/Water Programme of UNEP. Hosted by GEMS/Water Data Centre in Koblenz, Germany.
- **Coverage:** Global (station-based)
- **Resolution:** Point measurements
- **Access:** Free; web-based query and download.

---

## 3. Global Land Cover

### ESA WorldCover
- **URL:** https://esa-worldcover.org/
- **Status:** WORKING
- **Description:** First global land cover products for 2020 and 2021 at 10 m resolution, derived from Sentinel-1 and Sentinel-2 satellite data. Produced by a European consortium (VITO, Brockmann Consult, etc.). Currently the highest-resolution freely available global land cover.
- **Coverage:** Global
- **Resolution:** 10 m
- **Access:** Free download from website and via Google Earth Engine.

### MODIS Land Cover (MCD12Q1)
- **URL:** https://modis.gsfc.nasa.gov/data/dataprod/mod12.php
- **Status:** WORKING
- **Description:** Land cover classification incorporating five different classification schemes via supervised decision-tree method. Available annually. PI: Mark Friedl. Stage 2 validation status.
- **Coverage:** Global
- **Resolution:** 500 m (MCD12Q1), 0.05 degrees (MCD12C1)
- **Access:** Free via NASA Earthdata / LP DAAC.

### GlobeLand30
- **URL:** https://www.globeland30.org/
- **Status:** UNCERTAIN (connection refused in test; may be intermittently available)
- **Description:** World's first 30 m resolution global land cover dataset, developed by China's National Geomatics Center. Contains 10 land cover types for years 2000, 2010, and 2020. Donated to the United Nations in 2014.
- **Coverage:** Global (land areas)
- **Resolution:** 30 m
- **Access:** Free; registration required. Alternative: https://gkhub.earthobservations.org/records/6jqzw-w2g68

### Dynamic World -- Google
- **URL:** https://dynamicworld.app/
- **Status:** WORKING
- **Description:** Near real-time AI-powered global land cover dataset developed jointly by Google and the World Resources Institute. Classifies 9 land use/cover types. Updated continuously with new Sentinel-2 imagery. Built on Google Earth Engine.
- **Coverage:** Global
- **Resolution:** 10 m
- **Access:** Free; accessible through Google Earth Engine and the Dynamic World web app.

---

## 4. Weather / Climate -- Global and Regional

### ERA5 (Copernicus Climate Data Store)
- **URL:** https://cds.climate.copernicus.eu/
- **Status:** WORKING
- **Description:** Fifth-generation ECMWF atmospheric reanalysis of global climate. The most comprehensive global reanalysis dataset, covering 1940 to present. Provides hourly data on many atmospheric, land, and oceanic variables. Essential for any climate or hydrologic study.
- **Coverage:** Global
- **Resolution:** 0.25 degrees (~31 km), hourly temporal
- **Access:** Free; requires CDS registration. Available via web portal, API, and JupyterHub.

### CHIRPS -- Climate Hazards Group InfraRed Precipitation with Station
- **URL:** https://www.chc.ucsb.edu/data/chirps
- **Status:** WORKING
- **Description:** 35+ year quasi-global rainfall dataset (1981--present) combining satellite imagery and ground station data. Designed for trend analysis and seasonal drought monitoring in data-sparse regions. CHIRPS v3 now available; v2 production ends December 2026.
- **Coverage:** 50S--50N (quasi-global, emphasis on Africa, Asia, Latin America)
- **Resolution:** 0.05 degrees (~5 km), daily and monthly
- **Access:** Free via Google Earth Engine, USGS, and CHC data portal.

### GPM -- Global Precipitation Measurement / IMERG
- **URL:** https://gpm.nasa.gov/
- **Status:** WORKING
- **Description:** International satellite mission (NASA/JAXA, launched 2014) measuring global rain and snowfall. IMERG (Integrated Multi-satellitE Retrievals for GPM) provides gridded precipitation estimates. Successor to TRMM.
- **Coverage:** Global (67S--67N for core, extends to 90S--90N for merged products)
- **Resolution:** 0.1 degrees (~10 km), half-hourly
- **Access:** Free via NASA Earthdata / GES DISC.

### CRU TS -- Climate Research Unit Time Series
- **URL:** https://crudata.uea.ac.uk/cru/data/hrg/
- **Status:** WORKING
- **Description:** High-resolution gridded monthly climate dataset from University of East Anglia. Current version CRU TS v4.09 (March 2025), covering 1901--2024. Variables include precipitation, temperature, cloud cover, vapor pressure, frost days, and more.
- **Coverage:** Global land areas (excluding Antarctica)
- **Resolution:** 0.5 degrees (~50 km), monthly
- **Access:** Free under Open Government Licence.

### IMD -- India Meteorological Department
- **URL:** https://mausam.imd.gov.in/
- **Status:** WORKING
- **Description:** India's national meteorological service under the Ministry of Earth Sciences. Provides current weather forecasts, warnings, and historical climatological data for India. Gridded rainfall datasets available for research.
- **Coverage:** India
- **Resolution:** Various (station-based and 0.25-degree gridded products)
- **Access:** Some data free; research-grade datasets may require formal request.

### APHRODITE -- Asian Precipitation Highly-Resolved Observational Data Integration
- **URL:** https://www.chikyu.ac.jp/precip/english/
- **Status:** WORKING
- **Description:** State-of-the-art daily precipitation datasets with high-resolution grids for Asia, created from rain-gauge observations. Collaboration between RIHN and Japan's MRI/JMA. APHRODITE-2 products available. The best gauge-based gridded precipitation for monsoon Asia.
- **Coverage:** Monsoon Asia, Middle East, Russia
- **Resolution:** 0.25 and 0.5 degrees, daily
- **Access:** Free; registration required. APHRODITE-2 available via separate portal.

---

## 5. Regional Water Data

### Middle East

#### FAO AQUASTAT
- **URL:** https://www.fao.org/aquastat/en/
- **Status:** LIKELY WORKING (page loads but WebFetch captured only CSS framework; FAO site is functional)
- **Description:** FAO's global information system on water resources and agricultural water management. Provides country-level statistics on water withdrawal, irrigation, water resources, and dams for all countries. Critical resource for MENA water assessments.
- **Coverage:** Global with detailed MENA coverage
- **Resolution:** Country and sub-national level statistics
- **Access:** Free online database and country profiles.

#### IWMI MENA Program
- **URL:** https://www.iwmi.org/where-we-work/mena/
- **Status:** WORKING (confirmed via search)
- **Description:** International Water Management Institute's Middle East and North Africa research program. Provides remote sensing data for water resources assessments, research publications, and datasets specific to the region.
- **Coverage:** Middle East and North Africa
- **Access:** Free research publications and some datasets.

#### Fanack Water -- MENA Water Portal
- **URL:** https://water.fanack.com/
- **Status:** WORKING (confirmed via search)
- **Description:** Comprehensive water information portal covering all 21 MENA countries with detailed country profiles on water resources, focusing on groundwater, surface water, and water governance.
- **Coverage:** 21 MENA countries
- **Access:** Free online access.

### Africa

#### Nile Basin Initiative
- **URL:** https://nilebasin.org/
- **Status:** WORKING
- **Description:** Intergovernmental partnership of 10 Nile Basin countries (Burundi, DR Congo, Egypt, Ethiopia, Kenya, Rwanda, South Sudan, Sudan, Tanzania, Uganda). Provides data systems, publications, and project information related to water management across the Nile Basin. Motto: "ONE RIVER ONE PEOPLE ONE VISION."
- **Coverage:** Nile Basin (10 countries)
- **Access:** Some data and publications freely available.

#### Niger Basin Authority
- **URL:** https://www.abn.ne/index.php/en/
- **Status:** WORKING (content confirmed via search; Joomla-based site)
- **Description:** Intergovernmental organization of 9 West African countries (Benin, Burkina Faso, Cameroon, Chad, Cote d'Ivoire, Guinea, Mali, Niger, Nigeria). Manages water resources monitoring, flow forecasting, and hydroclimatic data collection in the Niger Basin.
- **Coverage:** Niger River Basin (9 countries)
- **Access:** Information and project data available; some data requires institutional request.

#### African Flood and Drought Monitor (AFDM)
- **URL:** https://hydrology.soton.ac.uk/apps/afdm/
- **Status:** WORKING
- **Description:** Experimental early warning system for flood and drought conditions across Africa. Developed by Princeton Climate Institute, University of Southampton, and Princeton University. Updated daily (~1--2 day latency). Provides 7-day flood forecasts and 6-month drought outlooks.
- **Coverage:** Africa
- **Resolution:** 5 km
- **Access:** Free online viewer and data access.

### Asia

#### India WRIS -- Water Resources Information System
- **URL:** https://indiawris.gov.in/wris/
- **Status:** UNCERTAIN (connection refused in test; may be intermittently available or blocked outside India)
- **Description:** India's comprehensive water resources information system under the Ministry of Jal Shakti. Provides dashboards for rainfall, water levels, river discharge, water bodies, and groundwater levels.
- **Coverage:** India
- **Access:** Free. Alternative: https://wdo.indiawris.gov.in/ (Water Data Online) or https://nwic.gov.in/india-wris

#### China -- Hydrologic Data
- **URL:** No single public portal readily accessible to international users
- **Description:** China's hydrologic data remains largely managed by the Ministry of Water Resources (MWR). Data sharing has been historically restricted. A Nature Water article (2023) highlights ongoing efforts to make China's water data accessible.
- **Workaround datasets:**
  - CNRD v1.0: Chinese Natural Runoff Dataset (published in BAMS, 2021)
  - Global datasets (GRDC, HydroSHEDS) cover Chinese rivers
  - ERA5, CHIRPS, GPM provide precipitation coverage over China
- **Access:** Limited public access; institutional collaboration often required.

#### Mekong River Commission (MRC)
- **URL:** https://www.mrcmekong.org/
- **Status:** WORKING
- **Description:** Intergovernmental organization for Mekong River basin management. Provides hydrological monitoring data, water quality information, and environmental assessments for the Lower Mekong Basin (Cambodia, Laos, Thailand, Vietnam). China and Myanmar are dialogue partners.
- **Coverage:** Mekong River Basin
- **Access:** Data portal available; some datasets require request.

---

## 6. Global Soil Data

### SoilGrids -- ISRIC
- **URL:** https://soilgrids.org/
- **Status:** WORKING (SoilGrids 250m 2.0; requires JavaScript)
- **Description:** Global system for digital soil mapping providing predictions for standard soil properties (organic carbon, bulk density, pH, sand/silt/clay, CEC, nitrogen) at six standard depths. Produced by ISRIC -- World Soil Information.
- **Coverage:** Global
- **Resolution:** 250 m
- **Access:** Free; web map viewer and WCS/WMS services for programmatic access.

### HWSD v2.0 -- Harmonized World Soil Database
- **URL:** https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/
- **Status:** WORKING
- **Description:** Comprehensive global soil inventory with detailed soil properties (morphology, chemistry, physics). Version 2.0 released September 2023. Nearly 30,000 soil mapping units with seven depth layers (0--200 cm). Developed by IIASA and FAO with contributions from ISRIC, ESBN, and Chinese Academy of Sciences.
- **Coverage:** Global
- **Resolution:** 1 km (30 arc-seconds)
- **Access:** Free download (GIS viewer, attribute database, raster data, documentation).

### FAO/UNESCO Digital Soil Map of the World
- **URL:** https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/faounesco-soil-map-of-the-world/en/
- **Status:** WORKING
- **Description:** Classic global soil map at 1:5,000,000 scale, initiated in 1961 by FAO and UNESCO. Completed over 20 years of international collaboration. Available as regional PDF maps, JPG images, and reports in multiple languages. Digital version accessible through FAO GeoNetwork.
- **Coverage:** Global
- **Resolution:** 1:5,000,000 scale
- **Access:** Free; PDF downloads and digital version via FAO GeoNetwork.

---

## 7. Satellite Data Platforms

### NASA Earthdata
- **URL:** https://earthdata.nasa.gov/
- **Status:** WORKING
- **Description:** Official gateway to NASA Earth observation data. Provides open access to 178+ petabytes of Earth science data through multiple DAACs (Distributed Active Archive Centers). Includes Landsat, MODIS, GPM, GRACE, SRTM, and hundreds of other datasets. Tools include Earthdata Search and Worldview.
- **Coverage:** Global
- **Access:** Free; requires Earthdata login (free registration). Serves 10+ million users.

### Copernicus Data Space Ecosystem
- **URL:** https://dataspace.copernicus.eu/
- **Status:** WORKING
- **Description:** Open ecosystem providing free instant access to Copernicus Sentinel missions and contributing mission data. Includes Sentinel-1 (SAR), Sentinel-2 (optical), Sentinel-3 (ocean/land), Sentinel-5P (atmosphere). Tools include openEO, JupyterLab, Data Workspace, and Sentinel Hub.
- **Coverage:** Global
- **Access:** Free; registration required. Operated by European consortium (T-Systems, CloudFerro, Sinergise, VITO, DLR).

### Google Earth Engine (GEE)
- **URL:** https://earthengine.google.com/
- **Status:** WORKING
- **Description:** Planetary-scale platform for Earth science data and analysis. Combines a multi-petabyte catalog of satellite imagery and geospatial datasets with cloud computing capabilities. Hosts thousands of datasets including Landsat, Sentinel, MODIS, climate data, DEMs, and land cover.
- **Coverage:** Global
- **Access:** Free for academic and research use; commercial licensing available. Code Editor (JavaScript) and Python API.

### GRACE / GRACE-FO -- Gravity Recovery and Climate Experiment
- **URL:** https://grace.jpl.nasa.gov/
- **Status:** WORKING
- **Description:** NASA/DLR mission measuring Earth's gravity field to track water movement. Monitors changes in groundwater storage, lake/river water, soil moisture, ice sheets, and sea level. GRACE-FO (Follow-On) continues the record. Critical for groundwater depletion studies (e.g., Middle East, India, North Africa).
- **Coverage:** Global
- **Resolution:** ~300 km (mass concentration "mascon" solutions provide higher effective resolution)
- **Access:** Free; data products include JPL Mascons, LAND grids, and interactive data browsers.

---

## 8. Flood and Disaster Data

### GloFAS -- Global Flood Awareness System
- **URL:** https://global-flood.emergency.copernicus.eu/
- **Status:** WORKING
- **Description:** (See Section 2 above.) Operational global flood forecasting. Part of Copernicus Emergency Management Service.

### Copernicus Emergency Management Service (CEMS)
- **URL:** https://emergency.copernicus.eu/
- **Status:** WORKING
- **Description:** EU operational service for emergency response and disaster risk management. Components include on-demand mapping for emergencies, wildfire monitoring, flood forecasting (EFAS and GloFAS), drought monitoring (EDO and GDO), and exposure mapping for human settlements.
- **Coverage:** Global (GloFAS, GDO) and European (EFAS, EDO)
- **Access:** Free; open access to monitoring products.

### UNDRR / DesInventar Sendai
- **URL:** https://www.desinventar.net/
- **Status:** WORKING
- **Description:** United Nations disaster loss database covering 65 datasets across 82 countries. Standardized disaster records for monitoring under the Sendai Framework for Disaster Risk Reduction and SDGs. Open-source (Apache-2 license).
- **Coverage:** Global (82 countries, strong coverage in Asia, Africa, Latin America)
- **Access:** Free; open source. Analysis tools and data management capabilities included.
- **Note:** UNDRR main site (https://www.undrr.org/) returned 403 during test, but DesInventar works.

### Dartmouth Flood Observatory (DFO)
- **URL:** https://floodobservatory.colorado.edu/
- **Status:** WORKING
- **Description:** Now hosted at University of Colorado Boulder (formerly Dartmouth). Space-based measurement, mapping, and modeling of surface water. Monitors discharge data for 335+ stations using satellite observations. Maintains a global archive of large flood events since 1985.
- **Coverage:** Global
- **Access:** Free; online map viewer and downloadable data.

---

## 9. Demographics and Boundaries

### WorldPop
- **URL:** https://www.worldpop.org/
- **Status:** WORKING
- **Description:** Leading geospatial and population research project focused on providing high-quality population datasets for low- and middle-income countries. Produces gridded population estimates, age/sex structures, urban change, and migration datasets.
- **Coverage:** Global (emphasis on Africa, Asia, Latin America)
- **Resolution:** 100 m and 1 km
- **Access:** Free download.

### LandScan -- ORNL
- **URL:** https://landscan.ornl.gov/
- **Status:** WORKING (site loads; WebFetch only captured frontend code but site is functional)
- **Description:** Global population distribution dataset from Oak Ridge National Laboratory (ORNL). Uses advanced modeling to estimate ambient (24-hour average) population. Updated annually. Widely used for disaster impact assessment and infrastructure planning.
- **Coverage:** Global
- **Resolution:** ~1 km (30 arc-seconds)
- **Access:** Free for research; registration required.

### UN Population Division -- World Population Prospects
- **URL:** https://population.un.org/wpp/
- **Status:** WORKING
- **Description:** Official UN source for demographic estimates and projections. Provides population data by country, age, sex, and year from 1950 to 2100 (projections). Essential for any population-related analysis.
- **Coverage:** Global (country-level)
- **Resolution:** Country and regional aggregates
- **Access:** Free; web interface and bulk download.

### GADM -- Global Administrative Areas
- **URL:** https://gadm.org/
- **Status:** WORKING
- **Description:** Provides maps and spatial data for all countries and their sub-divisions (states, provinces, districts, etc.). Essential basemap for any spatial analysis. Available in multiple GIS formats.
- **Coverage:** Global
- **Resolution:** High-resolution boundaries for all administrative levels
- **Access:** Free download in shapefile, GeoPackage, KMZ, and R formats.

---

## Quick Reference: Data Access Checklist

| Need | Best Source | Resolution | Free? |
|------|-----------|-----------|-------|
| DEM (30 m) | Copernicus GLO-30, SRTM, AW3D30 | 30 m | Yes |
| DEM (90 m, high accuracy) | MERIT DEM, TanDEM-X 90m | 90 m | Yes |
| River networks | HydroSHEDS / HydroRIVERS | varies | Yes |
| Watershed boundaries | HydroBASINS | varies | Yes |
| River discharge | GRDC | station | Yes |
| Flood forecasting | GloFAS | 5 km | Yes |
| Land cover (latest) | ESA WorldCover, Dynamic World | 10 m | Yes |
| Precipitation (Africa) | CHIRPS | 5 km daily | Yes |
| Precipitation (Asia) | APHRODITE, GPM/IMERG | 25--10 km | Yes |
| Climate reanalysis | ERA5 | 31 km hourly | Yes |
| Soil properties | SoilGrids | 250 m | Yes |
| Groundwater trends | GRACE/GRACE-FO | ~300 km | Yes |
| Population | WorldPop, LandScan | 100 m--1 km | Yes |
| Admin boundaries | GADM | high-res | Yes |
| Satellite imagery | Copernicus Data Space, GEE | 10--30 m | Yes |
| Disaster records | DesInventar Sendai | tabular | Yes |

---

## Notes for Students

1. **Registration:** Most sources require free registration. Create accounts early -- NASA Earthdata, Copernicus CDS, and Google Earth Engine are the three most important ones.

2. **Google Earth Engine** is a one-stop shop: it hosts most of the datasets listed above (DEMs, land cover, precipitation, temperature, population) and provides cloud computing to process them without downloading.

3. **CHIRPS** is specifically designed for regions with sparse rain gauges (Africa, parts of Asia) and is superior to gauge-only products in those areas.

4. **GRACE/GRACE-FO** is the only way to monitor large-scale groundwater depletion from space -- particularly important for the Middle East, North India, and North Africa.

5. **China data limitation:** Direct access to Chinese hydrologic monitoring data remains difficult for international users. Use global datasets (GRDC, ERA5, GPM) as alternatives for Chinese river basins.

6. **Copernicus DEM GLO-30** is increasingly preferred over SRTM for new projects due to higher accuracy and more recent acquisition dates.
