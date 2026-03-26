\newpage

# Appendix A: Data Source Quick Reference

This appendix provides a comprehensive directory of every data source mentioned in this book, organized by data type. Each entry includes the source name, URL, geographic coverage, spatial or temporal resolution, access conditions, and the chapters where the source is most relevant. The tables are subdivided into US, EU/Hungarian, and Global sections to help readers quickly locate equivalent datasets for their region of interest.

All URLs were verified on 2026-03-25. Status codes: **OK** means the site loads and provides content; **Partial** means the site loads but requires a JavaScript-enabled browser or partner login for full functionality; **Restricted** means access requires institutional credentials or a formal data request.

---

## 1. Elevation / Digital Elevation Models

Elevation data underpins nearly every analysis in hidroinformatics. From watershed delineation (Chapters 9--11) to flood mapping (Chapter 15), the choice of DEM determines the spatial resolution and vertical accuracy of all downstream results. This section covers the full spectrum of available DEMs, from national high-resolution products to freely available global datasets.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| USGS 3DEP (National Elevation Dataset) | https://www.usgs.gov/3d-elevation-program | Conterminous US, Alaska, Hawaii, territories | 1 m (LiDAR), 10 m, 30 m | Free; USGS EarthExplorer or The National Map | 5, 7, 9, 10, 11, 13 |
| USGS EarthExplorer | https://earthexplorer.usgs.gov/ | US and global | Various | Free; Earthdata login | 3, 5, 9 |
| OpenTopography | https://portal.opentopography.org/ | Global (curated LiDAR and DEM collections) | 1 m LiDAR to 90 m SRTM | Free; some datasets require login | 5, 13 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| DDM-5 (Hungarian National DEM) | https://lechnerkozpont.hu/oldal/domborzatmodell | Hungary | 5 m | Order via geoshop.hu or Lechner data services; WMS/WMTS available | 5, 7, 9, 10, 11 |
| Hungarian LiDAR Data | https://lechnerkozpont.hu/en/oldal/spatial-data | Fragmented coverage (selected areas) | 0.5--2 m (varies by survey) | Contact Lechner or relevant water directorates | 13, 14 |
| Copernicus DEM EEA-10 | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | 39 European countries | 10 m | Free; restricted access (qualifying institutions) | 5, 9, 10, 11 |
| Copernicus DEM GLO-30 | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | Global | 30 m | Free; Copernicus Data Space registration | 5, 9, 10, 11, 15 |
| Copernicus DEM GLO-90 | (same as above) | Global | 90 m | Free | 5, 9 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| SRTM (Shuttle Radar Topography Mission) | https://www.earthdata.nasa.gov/data/instruments/srtm | 60N to 56S (~80% of land) | 30 m (1 arc-sec), 90 m (3 arc-sec) | Free; NASA Earthdata login | 5, 9, 10, 11 |
| ALOS World 3D (AW3D30) | https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm | Global | 30 m | Free; JAXA registration | 5 |
| ASTER GDEM v3 | https://asterweb.jpl.nasa.gov/gdem.asp | 83N to 83S | 30 m | Free; NASA Earthdata login | 5 |
| MERIT DEM | https://global-hydrodynamics.github.io/MERIT_DEM/ | Global land areas, 90N--60S | 90 m (3 arc-sec) | Free; CC-BY-NC 4.0 license | 5, 9, 10 |
| TanDEM-X 90m | https://geoservice.dlr.de/web/dataguide/tdm90/ | Global | 90 m | Free for scientific use; DLR registration | 5 |

---

## 2. River Networks / Hydrography

River network data represents the digital skeleton of a watershed. In the US system, the National Hydrography Dataset (NHDPlus) provides a unified, attributed stream network. In Hungary, the OVF Hydrographic Database serves an equivalent role. For global studies, the HydroSHEDS family of products offers seamless coverage. These datasets are central to Chapters 9 through 12, where watershed delineation and stream network extraction are covered in detail.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| NHDPlus (National Hydrography Dataset Plus) | https://www.usgs.gov/national-hydrography/nhdplus-high-resolution | Conterminous US | 1:24,000 scale | Free; The National Map download | 2, 3, 9, 10, 11, 12 |
| USGS NWIS (National Water Information System) | https://waterdata.usgs.gov/nwis | US | Point stations | Free; web services and bulk download | 3, 8, 16, 22 |
| NWS AHPS (Advanced Hydrologic Prediction Service) | https://water.weather.gov/ahps/ | US | Forecast points | Free | 16 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| OVF Hydrographic Database (data.vizugy.hu) | https://data.vizugy.hu | Hungary | Station-based + vector network | Free (open since July 2024); attribution to OVF required | 2, 3, 9, 11, 16, 22 |
| HYDROINFO (Real-time Monitoring) | https://www.hydroinfo.hu | Hungary (Danube, Tisza, Drava-Mura) | 98 forecast sections | Free | 16 |
| WISE (Water Information System for Europe) | https://water.europa.eu/ | Pan-European | Various | Free | 3, 22 |
| WISE WFD Database | https://www.eea.europa.eu/data-and-maps/data/wise-wfd | EU member states | Water body level | Free | 3, 22 |
| EFAS (European Flood Awareness System) | https://european-flood.emergency.copernicus.eu/efas_frontend/ | Pan-European | 5 km | Archives public; real-time for EFAS partners | 15, 16 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| HydroSHEDS / HydroRIVERS / HydroBASINS | https://www.hydrosheds.org/ | Global | 3--15 arc-sec | Free | 9, 10, 11, 12 |
| GRDC (Global Runoff Data Centre) | https://grdc.bafg.de/ | Global (9,800+ stations) | Station-based; daily and monthly | Free for non-commercial; registration required | 3, 16, 22 |
| GloFAS (Global Flood Awareness System) | https://global-flood.emergency.copernicus.eu/ | Global | 0.05 deg (~5 km) | Free | 15, 16 |
| GEMStat (Global Water Quality) | https://gemstat.org/ | Global (station-based) | Point measurements | Free | 22 |
| Nile Basin Initiative | https://nilebasin.org/ | Nile Basin (10 countries) | Various | Some data free; institutional request for others | 3 |
| Niger Basin Authority | https://www.abn.ne/index.php/en/ | Niger River Basin (9 countries) | Various | Institutional request | 3 |
| Mekong River Commission | https://www.mrcmekong.org/ | Mekong Basin (4 countries + 2 dialogue partners) | Various | Data portal; some datasets require request | 3 |

---

## 3. Land Cover

Land cover classification determines how rainfall partitions into infiltration, runoff, and evapotranspiration. In hydrologic modeling, the choice of land cover dataset directly affects curve numbers, Manning's roughness coefficients, and imperviousness estimates. Chapter 6 introduces map algebra operations on land cover grids, while Chapters 9 and 15 apply land cover data in watershed and flood modeling contexts.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| NLCD (National Land Cover Database) | https://www.mrlc.gov/ | Conterminous US, Alaska, Hawaii | 30 m | Free | 6, 9, 15 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| CORINE Land Cover (CLC) | https://land.copernicus.eu/en/products/corine-land-cover | Pan-European (39 countries) | 100 m raster / vector | Free | 6, 9, 15 |
| Copernicus Land Monitoring Service (CLMS) | https://land.copernicus.eu/en | Pan-European and global | Various (10 m to 1 km) | Free | 6, 9 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| ESA WorldCover | https://esa-worldcover.org/ | Global | 10 m | Free | 6, 9, 15 |
| MODIS Land Cover (MCD12Q1) | https://modis.gsfc.nasa.gov/data/dataprod/mod12.php | Global | 500 m | Free; NASA Earthdata | 6 |
| GlobeLand30 | https://www.globeland30.org/ | Global | 30 m | Free; registration required (intermittent availability) | 6 |
| Dynamic World (Google) | https://dynamicworld.app/ | Global | 10 m | Free; Google Earth Engine | 6, 23 |

---

## 4. Soil

Soil hydraulic properties -- saturated conductivity, porosity, field capacity, wilting point -- are fundamental inputs to any rainfall-runoff model. European soil data is centralized through ESDAC at the Joint Research Centre, while the US relies on the SSURGO/STATSGO system maintained by the USDA. For global coverage, SoilGrids and the Harmonized World Soil Database provide machine-learning-based and expert-compiled soil property maps, respectively. These datasets are used extensively in Chapters 9, 15, and 21.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| USDA SSURGO / gSSURGO | https://www.nrcs.usda.gov/resources/data-and-reports/gridded-soil-survey-geographic-gssurgo-database | Conterminous US | ~10 m (county-level surveys) | Free | 9, 15, 21 |
| USDA STATSGO2 | https://www.nrcs.usda.gov/resources/data-and-reports/description-of-statsgo2-database | Conterminous US | ~1 km | Free | 9 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| ESDAC (European Soil Data Centre) | https://esdac.jrc.ec.europa.eu | Pan-European | 1 km (European Soil Database) + point data (LUCAS) | Free; some datasets require registration and request | 9, 15, 21 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| SoilGrids 250m (ISRIC) | https://soilgrids.org/ | Global | 250 m | Free; WebDAV, WCS, Google Earth Engine | 9, 21 |
| HWSD v2.0 (Harmonized World Soil Database) | https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/ | Global | 1 km (30 arc-sec) | Free | 9 |
| FAO/UNESCO Digital Soil Map of the World | https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/faounesco-soil-map-of-the-world/en/ | Global | 1:5,000,000 scale | Free | 9 |

---

## 5. Weather / Climate

Weather and climate data drive every hydrologic simulation. Precipitation is the primary input; temperature, humidity, wind, and radiation control evapotranspiration. The choice between station observations, gridded interpolation products, satellite-derived estimates, and reanalysis datasets depends on the study region and the temporal resolution required. Chapter 8 covers precipitation measurement in depth, while Chapters 15 and 16 apply weather data to flood modeling and forecasting.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| NOAA NCEI (National Centers for Environmental Information) | https://www.ncei.noaa.gov/ | US and global | Station-based | Free | 8 |
| PRISM | https://prism.oregonstate.edu/ | Conterminous US | 4 km, daily/monthly | Free | 8 |
| Daymet | https://daymet.ornl.gov/ | North America | 1 km, daily | Free | 8 |
| NCEP/NCAR Reanalysis | https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html | Global | ~210 km (T62 grid), 6-hourly | Free | 8 |
| NOAA National Water Model | https://water.noaa.gov/ | Conterminous US | ~1 km, hourly | Free | 16 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| OMSZ (Hungarian Meteorological Service) | https://www.met.hu/en/eghajlat/ | Hungary (136 stations) | Station-based; 10-minute intervals | Climate summaries free; detailed data by request | 8 |
| OMSZ Open Data Portal (odp.met.hu) | https://odp.met.hu/ | Hungary | Station and gridded | Free; open data portal | 8, 16 |
| ERA5 (Copernicus Climate Data Store) | https://cds.climate.copernicus.eu/ | Global | 31 km (~0.25 deg), hourly | Free; CDS registration | 8, 15, 16, 22 |
| ERA5-Land | https://cds.climate.copernicus.eu/ | Global | 9 km (~0.1 deg), hourly | Free; CDS registration | 8, 15 |
| E-OBS Gridded Dataset | https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php | Europe | 0.1 deg and 0.25 deg, daily | Free; registration | 8 |
| CARPATCLIM | https://surfobs.climate.copernicus.eu/dataaccess/access_carpatclim.php | Carpathian Region (9 countries) | 0.1 deg, daily | Free | 8 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| CHIRPS (Climate Hazards Group) | https://www.chc.ucsb.edu/data/chirps | 50S--50N (quasi-global) | 5 km, daily/monthly | Free | 8 |
| GPM / IMERG (NASA/JAXA) | https://gpm.nasa.gov/ | 67S--67N (core), extends to 90S--90N | 10 km, half-hourly | Free; NASA Earthdata | 8 |
| CRU TS (Climate Research Unit) | https://crudata.uea.ac.uk/cru/data/hrg/ | Global land (excl. Antarctica) | 0.5 deg, monthly | Free | 8 |
| APHRODITE (Asian Precipitation) | https://www.chikyu.ac.jp/precip/english/ | Monsoon Asia, Middle East, Russia | 0.25 deg, daily | Free; registration | 8 |
| IMD (India Meteorological Department) | https://mausam.imd.gov.in/ | India | Station-based and 0.25 deg gridded | Some free; research data by request | 8 |

---

## 6. Discharge / Water Level

Streamflow and water level observations are the ground truth against which all hydrologic models are calibrated and validated. In Hungary, the OVF system provides historical and real-time discharge data; in the US, the USGS NWIS network is the gold standard. For cross-border and global studies, the GRDC is indispensable. These datasets appear throughout the book but are most critical in Chapters 16 (real-time forecasting) and 22 (model calibration).

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| USGS NWIS | https://waterdata.usgs.gov/nwis | US (~13,000 streamflow stations) | Instantaneous (15-min), daily, monthly | Free | 3, 16, 22 |
| USGS WaterWatch | https://waterwatch.usgs.gov/ | US | Real-time maps | Free | 16 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| OVF / data.vizugy.hu | https://data.vizugy.hu | Hungary | Sub-daily to monthly (historical records from early 20th century) | Free (open since July 2024) | 3, 16, 22 |
| HYDROINFO | https://www.hydroinfo.hu | Hungary (Danube, Tisza, Drava-Mura) | Real-time + 98 forecast sections | Free | 16 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| GRDC | https://grdc.bafg.de/ | Global (9,800+ stations, ~435,000 station-years) | Daily, monthly | Free for non-commercial; registration + terms | 3, 16, 22 |
| FAO AQUASTAT | https://www.fao.org/aquastat/en/ | Global (country-level) | Country and sub-national statistics | Free | 3 |
| India WRIS | https://indiawris.gov.in/wris/ | India | Station-based | Free (intermittent availability) | 3 |

---

## 7. Flood Mapping

Flood maps translate hydrologic model outputs into actionable spatial information: which areas are inundated, at what depth, and for what return period. In the US, FEMA maintains the National Flood Hazard Layer; in the EU, the Floods Directive requires member states to produce equivalent flood hazard and risk maps. Satellite-based flood monitoring complements these products with near-real-time observations during events. These datasets are central to Chapters 14 through 17.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| FEMA NFHL (National Flood Hazard Layer) | https://msc.fema.gov/portal/home | US | Parcel-level | Free | 14, 15, 17 |
| USGS Flood Inundation Mapping Program | https://www.usgs.gov/mission-areas/water-resources/science/flood-inundation-mapping-fim-program | US (selected communities) | Various | Free | 14, 15 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| Hungarian Flood Risk Maps (OVF) | https://geoportal.vizugy.hu | Hungary | Planning area unit | Restricted (may require VPN or institutional access) | 15, 17 |
| Flood Risk Management Plans (vizeink.hu) | https://vizeink.hu | Hungary | Planning area unit | Free | 15, 17 |
| JRC River Flood Hazard Maps | https://data.jrc.ec.europa.eu/collection/id-0054 | Europe | GeoTIFF raster | Free | 15 |
| EFAS (European Flood Awareness System) | https://european-flood.emergency.copernicus.eu/efas_frontend/ | Pan-European | 5 km | Archives public; real-time for partners | 15, 16 |
| Copernicus Emergency Management Service | https://emergency.copernicus.eu/ | European and global | Event-specific | Free; on-demand mapping by authorized users | 15, 16 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| GloFAS | https://global-flood.emergency.copernicus.eu/ | Global | 0.05 deg (~5 km) | Free | 15, 16 |
| Dartmouth Flood Observatory | https://floodobservatory.colorado.edu/ | Global | Event-based | Free | 15 |
| DesInventar Sendai (UNDRR) | https://www.desinventar.net/ | Global (82 countries) | Tabular disaster records | Free; open source | 15, 17 |
| African Flood and Drought Monitor | https://hydrology.soton.ac.uk/apps/afdm/ | Africa | 5 km | Free | 15, 16 |

---

## 8. Demographics / Population

Population and socioeconomic data enable vulnerability assessment: who is at risk when floods strike, and what infrastructure is exposed. Chapter 17 specifically addresses flood risk exposure analysis, combining flood maps with census and population data. The US Census TIGER/Line system, Hungary's KSH, and the Eurostat GISCO system provide administrative boundaries with demographic attributes at multiple scales.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| US Census Bureau / TIGER/Line | https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html | US | Census block to national | Free | 17 |
| American Community Survey | https://www.census.gov/programs-surveys/acs | US | Census tract | Free | 17 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| KSH (Hungarian Central Statistical Office) | https://www.ksh.hu/?lang=en | Hungary | Municipality to national | Free | 17 |
| KSH Census 2022 | https://nepszamlalas2022.ksh.hu/en/database/ | Hungary | Municipality, district, county, region | Free | 17 |
| KSH Open Data API (data.ksh.hu) | https://data.ksh.hu/ | Hungary | Various | Free; JSON API | 17 |
| Eurostat / GISCO | https://ec.europa.eu/eurostat/web/gisco/geodata | Pan-European (NUTS, LAU regions) | Administrative units, 1 km population grid | Free for non-commercial | 17 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| WorldPop | https://www.worldpop.org/ | Global (emphasis on Africa, Asia, Latin America) | 100 m and 1 km | Free | 17 |
| LandScan (ORNL) | https://landscan.ornl.gov/ | Global | ~1 km | Free for research; registration | 17 |
| UN World Population Prospects | https://population.un.org/wpp/ | Global (country-level) | Country and regional | Free | 17 |
| GADM (Global Administrative Areas) | https://gadm.org/ | Global (all countries) | High-resolution boundaries, all admin levels | Free | 17 |

---

## 9. Satellite Imagery

Satellite imagery provides the observational backbone of modern hidroinformatics. Optical sensors (Sentinel-2, Landsat) map land cover and surface water extent; synthetic aperture radar (Sentinel-1) penetrates clouds to detect flooding; thermal sensors monitor evapotranspiration; and gravity satellites (GRACE) measure total water storage changes. Cloud computing platforms like Google Earth Engine and the Copernicus Data Space have transformed access to these data, enabling analyses that previously required weeks of downloading and preprocessing to be completed in minutes. Satellite data features prominently in Chapters 2, 6, 13, 15, and 23.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| NASA Earthdata | https://earthdata.nasa.gov/ | Global (178+ PB) | Various (Landsat, MODIS, GPM, GRACE, SRTM, etc.) | Free; Earthdata login | 2, 3, 5, 8, 13 |
| Landsat (USGS/NASA) | https://www.usgs.gov/landsat-missions | Global | 30 m optical, 15 m pan, 100 m thermal | Free | 2, 6 |
| MODIS (NASA) | https://modis.gsfc.nasa.gov/ | Global | 250 m to 1 km | Free; NASA Earthdata | 6, 8 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| Copernicus Data Space Ecosystem | https://dataspace.copernicus.eu/ | Global (Sentinel-1, -2, -3, -5P + contributing missions) | 10 m (S2 optical), 5x20 m (S1 SAR), 300 m (S3) | Free; registration required | 2, 6, 13, 15 |
| Copernicus Browser | https://browser.dataspace.copernicus.eu/ | Global | Various | Free; visual browser for Sentinel data | 2 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| Google Earth Engine (GEE) | https://earthengine.google.com/ | Global (multi-petabyte catalog) | Various (hosts Landsat, Sentinel, MODIS, DEMs, climate, etc.) | Free for academic/research; commercial licensing available | 2, 6, 12, 23 |

---

## 10. Groundwater

Groundwater resources are invisible from the surface but can be monitored through well networks, geophysical surveys, and satellite gravimetry. In Hungary, the OVF maintains an extensive monitoring well network accessible through data.vizugy.hu. The GRACE satellite mission provides the only means of detecting large-scale groundwater storage changes from space. These data sources are essential for Chapters 18 through 21, which cover 3D subsurface GIS, well data management, aquifer characterization, and groundwater flow simulation.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| USGS NWIS Groundwater | https://waterdata.usgs.gov/nwis/gw | US | Point stations (monitoring wells) | Free | 19, 20, 21 |
| USGS National Water Dashboard | https://dashboard.waterdata.usgs.gov/ | US | Real-time well levels | Free | 19 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| OVF Groundwater Data (data.vizugy.hu) | https://data.vizugy.hu | Hungary (monitoring wells) | Point stations | Free (open since July 2024) | 19, 20, 21 |
| WISE WFD Groundwater Bodies | https://www.eea.europa.eu/data-and-maps/data/wise-wfd | EU member states | Groundwater body level | Free | 19, 21 |
| GravIS / G3P (European Groundwater from GRACE) | https://gravis.gfz.de/gws | European focus (global available) | ~300 km, monthly | Free | 19, 21 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| GRACE / GRACE-FO | https://grace.jpl.nasa.gov/ | Global | ~300 km (mascon solutions provide higher effective resolution), monthly | Free; NASA Earthdata login | 19, 21 |
| IGRAC (International Groundwater Resources Assessment Centre) | https://www.un-igrac.org/ | Global | Various | Free; some datasets require request | 19 |

---

## 11. Geologic Maps

Geologic maps provide the subsurface framework for groundwater modeling: lithology determines hydraulic conductivity, formation contacts define aquifer boundaries, and structural features (faults, folds) control flow paths. In Hungary, the Mining and Geological Survey (MBFSZ) maintains the national geologic map service. These data are most relevant to Chapters 18 through 21.

### US Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| USGS National Geologic Map Database | https://ngmdb.usgs.gov/ | US | Various (1:24,000 to 1:500,000) | Free | 18, 20 |
| USGS 3D Hydrogeologic Framework Models | https://www.usgs.gov/programs/groundwater-and-streamflow-information-program | Selected US aquifer systems | Model-specific | Free | 18, 20, 21 |

### EU / Hungarian Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| MBFSZ (Hungarian Mining and Geological Survey) | https://map.mbfsz.gov.hu/ | Hungary | 1:100,000 and larger | Free; interactive map viewer | 18, 19, 20 |
| OneGeology Europe | https://www.onegeology.org/ | Pan-European and global | Various | Free; WMS services | 18, 20 |
| EGDI (European Geological Data Infrastructure) | https://www.europe-geology.eu/ | Pan-European | Various (harmonized geological maps) | Free | 18, 20 |

### Global Sources

| Name | URL | Coverage | Resolution | Access | Chapters |
|------|-----|----------|------------|--------|----------|
| OneGeology Portal | https://portal.onegeology.org/ | Global (participating geological surveys) | Country-dependent | Free; WMS services | 18 |
| CGMW (Commission for the Geological Map of the World) | https://www.ccgm.org/ | Global | 1:5,000,000 and smaller | Some maps free; others for purchase | 18 |

---

## Coordinate Reference Systems Quick Reference

When working across US, Hungarian, and EU datasets, coordinate system mismatches are one of the most common sources of error. This table summarizes the key coordinate reference systems encountered in this book.

| CRS | EPSG Code | Use | Coordinate Range | Notes |
|-----|-----------|-----|------------------|-------|
| HD72/EOV | EPSG:23700 | Hungarian national datasets | Northing: 0--400,000; Easting: 400,000--1,000,000 | **Identify by value range, not header labels** -- Hungarian headers often swap X/Y |
| ETRS89 (Geographic) | EPSG:4258 | EU-wide geographic coordinates | Lat/Lon in degrees | Standard EU geographic CRS |
| ETRS89/LAEA | EPSG:3035 | EU-wide projected (equal area) | Metric, centered on Europe | Standard for pan-European raster data |
| WGS84 | EPSG:4326 | Global GPS coordinates, most satellite data | Lat/Lon in degrees | Near-identical to ETRS89 for practical purposes |
| NAD83 | EPSG:4269 | US national datasets | Lat/Lon in degrees | US equivalent of ETRS89 |
| UTM Zone 34N (WGS84) | EPSG:32634 | Hungary falls in UTM zone 34N | Metric | Alternative to EOV for local metric work |

The HD72 to ETRS89 transformation (EPSG:1449) uses a 7-parameter Helmert transformation. For sub-meter accuracy, use the Hungarian-specific grid shift file available from Lechner Tudaskoezpont. PROJ handles this transformation correctly with the parameters documented at https://epsg.io/1449.

---

## Hungarian Water Data Portal Guide

Hungary has made remarkable progress in opening its water and environmental data to the public. Five key portals provide the bulk of the data a water scientist needs. This section provides step-by-step instructions for accessing each one, written for users who may be encountering these systems for the first time. All portals are in Hungarian by default, but most offer at least partial English interfaces. Where English is not available, browser-based translation tools work well.

### Portal 1: data.vizugy.hu -- The Central Hydrographic Database

**What it contains.** This is Hungary's equivalent of the USGS NWIS. It provides historical and recent time series for surface water levels, river discharge, water temperature, groundwater levels from monitoring wells, and precipitation from the hydromet station network. The data became freely available without restrictions in July 2024, a landmark decision that aligned Hungary with international open-data best practices.

**Step-by-step access procedure.**

1. **Navigate to the portal.** Open https://data.vizugy.hu in a modern browser (Chrome, Firefox, or Edge). The site is built as a single-page Angular application, so JavaScript must be enabled. Allow the application a few seconds to fully load.

2. **Understand the interface layout.** The main page presents a map of Hungary showing monitoring stations as colored dots. Surface water stations are typically blue, groundwater wells are green or yellow, and precipitation stations are marked differently. A sidebar or toolbar provides filtering options.

3. **Select a station.** You can either click directly on a station dot on the map, or use the search function to find a station by name or identifier. Major rivers (Danube, Tisza, Drava, Raba, Sajo, Hernad, Koros, Maros, Zala) have stations listed along their length from upstream to downstream.

4. **Choose the parameter and time range.** After selecting a station, the portal presents the available parameters for that station. Common parameters include water level (vizallas), discharge (vizhozam), water temperature (vizhomerseklet), and for groundwater wells, groundwater level (talajvizszint). Select your parameter, then specify the start and end dates for your time series.

5. **View and download data.** The portal displays the time series as an interactive chart. Below the chart or via a download button, you can export the data. Common formats include CSV and Excel. Pay attention to the timestamp format (typically Central European Time) and the units (water level in cm above a local gauge datum, discharge in m3/s).

6. **Attribution.** When using the data in publications, cite OVF (Orszagos Vizugyi Foigazgatosag / General Directorate of Water Management) as the data provider, along with the station name and parameter.

**Tips and common issues.**

- The Angular application may not render correctly in older browsers. Use the latest version of Chrome or Firefox.
- If the map fails to load, try clearing your browser cache or disabling ad-blocking extensions.
- For very long time series (multiple decades), the download may take several minutes. Be patient.
- The alternative URL https://www.ovf.hu/en/hydrography-water-quality/hydrographic-data provides a more traditional HTML page with links to data downloads and is useful as a fallback if the Angular app is unresponsive.
- Station metadata (coordinates, zero-point elevation, river km) is typically available on the station detail page. Note that coordinates are in EOV (EPSG:23700) -- identify Northing (0--400,000) and Easting (400,000--1,000,000) by value range, as labels are sometimes swapped.

---

### Portal 2: hydroinfo.hu -- Real-Time Water Level Monitoring and Flood Forecasts

**What it contains.** HYDROINFO is Hungary's operational water forecasting portal, analogous to the NWS Advanced Hydrologic Prediction Service in the US. It provides current water levels, flood warnings, ice conditions, navigation information, and short-term forecasts for 98 sections of the Danube, Tisza, and Drava-Mura catchments. It also includes a small watershed flash flood alert system.

**Step-by-step access procedure.**

1. **Navigate to the portal.** Open https://www.hydroinfo.hu in any browser. The site loads in Hungarian by default. Look for a language selector (typically a flag icon or "EN" link) in the upper-right corner for the English version.

2. **Explore the map view.** The main page typically shows an overview map of Hungary with river reaches color-coded by flood alert level: green for normal, yellow for first-degree alert, orange for second-degree, and red for third-degree (highest) alert. Click on any river reach or station to see details.

3. **View station data.** Clicking a station brings up a detail page showing the current water level, the trend (rising, falling, or stable), the alert thresholds for that station, and a hydrograph showing recent water level history. Some stations also show discharge estimates.

4. **Access flood forecasts.** The forecasting section provides probabilistic water level forecasts for the next several days. The Danube typically has 5--7 day forecasts; smaller rivers may have shorter lead times. The forecasts are displayed as hydrographs with confidence bands.

5. **Mobile access.** HYDROINFO offers a mobile application for both Android and iOS. The mobile app provides push notifications for flood warnings, which is useful for field campaigns.

**Tips and common issues.**

- This portal is optimized for real-time monitoring and current conditions, not for downloading bulk historical data. For historical time series, use data.vizugy.hu instead.
- During major flood events, the site may experience high traffic. The mobile app is often more reliable during these periods.
- The small watershed alert system (kisvizfolyasok) provides flash flood warnings for ungauged catchments based on radar rainfall estimates. This is particularly valuable for tributaries not covered by the main forecasting network.
- Alert thresholds (I, II, III) at each station correspond to specific water levels that trigger operational responses by the regional water directorates. These thresholds are available in the station metadata.

---

### Portal 3: odp.met.hu -- OMSZ Open Data Portal (Hungarian Meteorological Service)

**What it contains.** The OMSZ Open Data Portal provides access to meteorological observations and products from Hungary's national weather service (HungaroMet Zrt., formerly OMSZ). This includes station observations (temperature, precipitation, humidity, wind, radiation), gridded weather products, climate summaries, radar imagery, and air quality data. The 136-station synoptic network provides data at 10-minute intervals.

**Step-by-step access procedure.**

1. **Navigate to the portal.** Open https://odp.met.hu/ in your browser. If the open data portal is unavailable or does not have the specific product you need, the main climate page at https://www.met.hu/en/eghajlat/ provides an alternative entry point with climate summaries for major cities.

2. **Browse available datasets.** The portal organizes data into categories: current observations, historical climate data, weather warnings, and derived products. Look for the section on historical or climate data for research-grade datasets.

3. **Select station data.** For station observations, you can search by station name, location, or parameter. The five major long-record stations are Budapest, Debrecen, Pecs, Szeged, and Szombathely, with climate series extending back to 1901. Many additional stations have records from the 1950s onward.

4. **Choose parameters and time periods.** Available parameters include daily maximum and minimum temperature, daily precipitation totals, relative humidity, mean wind speed, wind gusts, sunshine duration, and global radiation. For the 10-minute data from synoptic stations, you may need to contact OMSZ directly via the data request form.

5. **Download data.** The portal provides data in CSV or Excel format. Climate summaries (monthly means, annual totals, extremes) are also available as PDF reports.

6. **Access gridded products.** OMSZ produces gridded precipitation and temperature analyses for Hungary using their station network. These products may be available through the portal or by direct request.

**Tips and common issues.**

- The distinction between free and fee-based products has shifted over time. As of 2024--2025, most historical climate data is available without charge under Hungary's open data policies, but some specialized products (high-resolution gridded analyses, sub-hourly data) may still require a formal data request.
- For gap-free precipitation and temperature data covering Hungary, the E-OBS dataset (available from the Copernicus climate services) and CARPATCLIM are excellent alternatives that combine OMSZ station data with observations from neighboring countries.
- Agromet products (growing season data, frost dates, heat sums) are available from March through September each year and can be useful for agricultural water demand estimation.
- The radar network provides composite images of precipitation intensity at approximately 5-minute intervals. These are available as images on the main met.hu site and may be available in quantitative format through the data portal or by request.

---

### Portal 4: map.mbfsz.gov.hu -- Hungarian Mining and Geological Survey Map Viewer

**What it contains.** The MBFSZ (Szabalyozott Tevekenysegeink Felugyeleti Hatosaga, formerly MFGI) provides Hungary's official geologic map data. The interactive map viewer offers access to surface geologic maps, hydrogeologic maps, geothermal data, mineral resource maps, and borehole logs. For groundwater modeling (Chapters 18--21), this is an essential resource for understanding subsurface lithology and aquifer geometry.

**Step-by-step access procedure.**

1. **Navigate to the portal.** Open https://map.mbfsz.gov.hu/ in a modern browser. The interface is a web-based GIS viewer (typically based on OpenLayers or Leaflet). Allow it to load fully.

2. **Explore available map layers.** The layer panel (usually on the left side or accessible via a layers button) lists the available thematic maps. Key layers for water scientists include:
   - **Surface geology** (felszini foldtani terkep): shows the geologic formations at the surface, typically at 1:100,000 scale.
   - **Hydrogeology** (vizfoldtani terkep): maps of aquifer systems, well yield zones, and groundwater vulnerability.
   - **Borehole database** (furasadatbazis): locations and logs of boreholes drilled across Hungary.
   - **Geothermal data**: temperature gradients and thermal water resources.

3. **Navigate the map.** Use standard pan and zoom controls. The map covers all of Hungary. You can search for a location by name or coordinates (EOV or WGS84).

4. **Query features.** Click on the map to identify geologic units, view borehole logs, or query attributes. The identify tool (often an "i" icon) returns attribute data for visible layers at the clicked location.

5. **Download data.** Some layers are available for download as shapefiles or GeoTIFFs. Others are served only as WMS (view-only) services. For bulk downloads or specialized data requests, contact MBFSZ directly. The WMS service URLs can be added to QGIS or ArcGIS for integration with your own project data.

6. **Access borehole logs.** The borehole database contains lithologic descriptions, construction details, and in some cases water level measurements. Click on a borehole location to view its log. This information is critical for building 3D geologic models (Chapter 18) and parameterizing groundwater flow models (Chapter 21).

**Tips and common issues.**

- The interface is primarily in Hungarian, and geologic terminology can be specialized. Keep a Hungarian geological dictionary or use browser translation. Key terms: homok = sand, kavics = gravel, agya = clay, mesz = limestone, dolomit = dolomite, viz = water.
- The WMS services can be slow during peak hours. If the viewer is unresponsive, try accessing the WMS layers directly in QGIS, which allows you to control rendering and cache tiles locally.
- For cross-border geologic continuity (important for the Danube Basin), the EGDI (European Geological Data Infrastructure) at https://www.europe-geology.eu/ provides harmonized geologic maps that include Hungary within the broader European context.
- Borehole logs vary greatly in quality and detail, depending on when and why the borehole was drilled. Industrial boreholes (mining, geothermal) tend to have more detailed logs than agricultural or monitoring wells.

---

### Portal 5: data.ksh.hu -- KSH Open Data API (Hungarian Central Statistical Office)

**What it contains.** The KSH provides Hungary's official demographic, economic, and social statistics. For water scientists, the most relevant datasets are population counts and density by municipality (used in flood exposure analysis, Chapter 17), land use statistics, and agricultural data (irrigation, water use). The 2022 Census data is the most current comprehensive population dataset.

**Step-by-step access procedure.**

1. **Navigate to the portal.** For the most user-friendly experience, start at https://www.ksh.hu/?lang=en (the main KSH website with English interface). For programmatic access, use the API at https://data.ksh.hu/. For Census 2022 data specifically, go to https://nepszamlalas2022.ksh.hu/en/database/.

2. **Browse STADAT tables.** The main KSH website provides STADAT (Statistical Data) summary tables organized by topic. Navigate to the "Population, vital events" or "Regional statistics" section for demographic data relevant to flood risk assessment.

3. **Access Census 2022 data.** The Census 2022 portal provides thematic maps and downloadable tables at multiple geographic levels: region (regio), county (megye), district (jaras), and municipality (telepules). Population counts, age structure, housing, and employment data are all available.

4. **Use the API (data.ksh.hu).** For automated data retrieval:
   - The API documentation is available at the portal.
   - Endpoints return JSON-formatted responses.
   - You can query specific indicators by geographic unit and time period.
   - This is the most efficient approach for integrating population data into GIS workflows, as you can script the data retrieval and join it directly to administrative boundary shapefiles.

5. **Download administrative boundaries.** To map KSH statistics, you need the corresponding administrative boundary shapefiles. These are available from:
   - Eurostat GISCO (https://ec.europa.eu/eurostat/web/gisco/geodata) for NUTS regions and LAU (Local Administrative Units).
   - The KSH itself sometimes provides boundary files with Census data.
   - GADM (https://gadm.org/) provides administrative boundaries for Hungary at all levels.

6. **Join statistics to geography.** The standard workflow is: (a) download the statistical table with a geographic identifier (municipality code or LAU code), (b) download the corresponding boundary shapefile, (c) perform a table join in your GIS software using the shared identifier, and (d) create thematic maps showing population density, growth rates, or other indicators overlaid with flood hazard zones.

**Tips and common issues.**

- Hungarian municipality codes have changed over time due to administrative reorganizations. Ensure your boundary file and statistical table use the same vintage of codes. The 2022 Census uses the latest administrative structure.
- The KSH website can be slow when generating large custom tables. Pre-built STADAT tables download much faster than custom queries.
- For the R programming environment, the `giscoR` package provides direct access to Eurostat/GISCO administrative boundaries, and the `eurostat` package retrieves Eurostat statistics -- together they offer a streamlined workflow for mapping Hungarian demographics within the EU context.
- Population data at the municipality level can be joined to flood hazard maps to estimate the number of people living in flood-prone areas, a standard requirement under the EU Floods Directive.

---

## Cross-Portal Integration Workflow

For a typical Hungarian watershed study, you will need data from multiple portals simultaneously. The recommended workflow is:

1. **Define your study area** using administrative boundaries from KSH/GISCO/GADM or catchment boundaries delineated from a DEM.

2. **Obtain elevation data.** Start with the Copernicus DEM GLO-30 for free 30 m coverage. If higher resolution is needed and budget allows, order the DDM-5 from Lechner.

3. **Get weather forcing.** Download ERA5-Land (9 km) from the Copernicus Climate Data Store for model forcing. Supplement with OMSZ station data from odp.met.hu for validation and local calibration.

4. **Collect streamflow data** from data.vizugy.hu for calibration gauges within and downstream of your catchment. Check GRDC for upstream gauges in neighboring countries if your catchment is transboundary.

5. **Obtain land cover** from CORINE Land Cover (pan-European, 100 m) or ESA WorldCover (global, 10 m).

6. **Get soil properties** from ESDAC or SoilGrids for hydraulic parameters.

7. **Retrieve geologic information** from map.mbfsz.gov.hu if your study involves groundwater.

8. **Download population data** from data.ksh.hu if your study involves flood risk or exposure assessment.

9. **Harmonize coordinate systems.** Convert all datasets to a common CRS. For local work in Hungary, EOV (EPSG:23700) is standard. For pan-European analysis, ETRS89/LAEA (EPSG:3035) is preferred. Use PROJ or your GIS software's reprojection tools, and verify the HD72-to-ETRS89 transformation with EPSG:1449.

---

## Data Licensing Summary

Understanding data licensing is essential for both academic publications and operational applications. The table below summarizes the licensing terms for the major data sources listed in this appendix.

| License Type | Datasets | Key Terms |
|-------------|----------|-----------|
| Fully Open (no restrictions) | SRTM, Copernicus GLO-30/GLO-90, ERA5, E-OBS, CORINE, CLMS, ESA WorldCover, WISE, JRC Flood Hazard, data.vizugy.hu (since 2024), HYDROINFO, CHIRPS, GPM/IMERG, CRU TS, GloFAS, EFAS archives, Dynamic World, WorldPop | Free for any use; attribution typically required |
| Free with registration | NASA Earthdata products, Copernicus Data Space, Google Earth Engine (academic), CDS, SoilGrids, GRDC, LandScan, ALOS AW3D30, APHRODITE | Free account required; some have terms of use restricting commercial application |
| Free with data request | ESDAC (some layers), OMSZ detailed station data, MBFSZ specialized products | Contact the data provider; may require justification and data use agreement |
| Restricted / Institutional | Copernicus EEA-10 DEM, EFAS real-time data, OVF flood geoportal, DDM-5, Hungarian LiDAR | Requires qualifying institution, partner status, or purchase |
| CC-BY-NC | MERIT DEM, some ISRIC products | Free for non-commercial use; attribution required; commercial use prohibited |

---

## Frequently Encountered File Formats

Readers new to geospatial data analysis will encounter many file formats across these portals. This reference covers the most common ones.

| Format | Extension | Description | Common Sources |
|--------|-----------|-------------|----------------|
| GeoTIFF | .tif, .tiff | Georeferenced raster image; the universal exchange format for gridded data | DEMs, land cover, satellite imagery, soil maps |
| NetCDF | .nc | Self-describing array format for multidimensional data; standard for climate and weather data | ERA5, E-OBS, CARPATCLIM, CHIRPS, CRU TS |
| GRIB / GRIB2 | .grib, .grib2 | WMO standard for weather model output; compact binary format | ERA5 (native), ECMWF forecasts, NWP model output |
| Shapefile | .shp (+.shx, .dbf, .prj) | Legacy vector format; still widely used despite limitations (2 GB max, 10-char field names) | Administrative boundaries, river networks, CORINE CLC |
| GeoPackage | .gpkg | Modern SQLite-based vector/raster container; single file, no size limit | Increasingly replacing shapefiles; GADM, some EU products |
| GeoJSON | .geojson | JSON-based vector format; human-readable, web-friendly | Eurostat GISCO, web APIs |
| CSV | .csv | Plain text tabular data; universally supported | Station time series (data.vizugy.hu, GRDC, KSH) |
| WaterML2 | .xml | OGC standard for hydrological time series data | GRDC |
| SAFE | .SAFE (directory) | Sentinel satellite product format (contains GeoTIFF, XML metadata) | Copernicus Data Space (Sentinel-1, -2, -3) |
| HGT | .hgt | Raw binary elevation tiles used by SRTM | SRTM downloads |
| VRT | .vrt | GDAL virtual raster; XML pointer to remote tiles, enables streaming access | SoilGrids WebDAV |

---

## Registration Checklist

Before beginning a project, register for these free accounts. The registration process for each takes approximately 2--5 minutes. Having all accounts ready before you start avoids delays during data download.

| Priority | Service | Registration URL | What You Get |
|----------|---------|-----------------|--------------|
| 1 | NASA Earthdata | https://urs.earthdata.nasa.gov/users/new | Access to SRTM, Landsat, MODIS, GPM, GRACE, ASTER GDEM |
| 2 | Copernicus Data Space | https://dataspace.copernicus.eu/ | Access to Sentinel-1/2/3/5P, Copernicus DEM, APIs |
| 3 | Copernicus Climate Data Store | https://cds.climate.copernicus.eu/ | Access to ERA5, ERA5-Land, E-OBS, seasonal forecasts |
| 4 | Google Earth Engine | https://earthengine.google.com/ | Cloud computing + multi-petabyte data catalog |
| 5 | GRDC | https://grdc.bafg.de/ | Global river discharge data |
| 6 | ISRIC SoilGrids | https://soilgrids.org/ | Global soil property maps (WebDAV/WCS access) |
| 7 | Eurostat/GISCO | https://ec.europa.eu/eurostat/web/gisco/geodata | European administrative boundaries and population grids |

---

## Chapter-to-Data-Source Cross-Reference

This reverse index shows which data sources are most relevant to each chapter, helping readers locate the right data for each stage of their analysis.

| Chapter | Title | Primary Data Sources |
|---------|-------|---------------------|
| 1 | Why Hidroinformatics Matters | (conceptual -- no specific data sources) |
| 2 | Mapping Water: From Paper to Pixels | NHDPlus, data.vizugy.hu, Copernicus Data Space, Landsat, NASA Earthdata |
| 3 | Where the Data Lives | All portals (overview chapter); data.vizugy.hu, USGS NWIS, GRDC, WISE, NASA Earthdata |
| 4 | GIS as a Water Tool | (tool-focused -- uses example data from multiple sources) |
| 5 | The Grid: How Computers See Terrain | 3DEP, DDM-5, Copernicus DEM, SRTM, AW3D30, ASTER GDEM, MERIT DEM, TanDEM-X |
| 6 | Calculating with Maps | NLCD, CORINE, ESA WorldCover, Dynamic World, MODIS Land Cover, Sentinel-2 |
| 7 | Slope, Aspect, and the Shape of the Land | 3DEP, DDM-5, Copernicus DEM |
| 8 | Measuring Rain Where It Falls | OMSZ, ERA5, E-OBS, CARPATCLIM, CHIRPS, GPM/IMERG, CRU TS, APHRODITE, PRISM, Daymet |
| 9 | Preparing the Digital Landscape | DEMs (all), CORINE/WorldCover, SSURGO/ESDAC/SoilGrids, HydroSHEDS |
| 10 | Which Way Does Water Flow? | DEMs (all), HydroSHEDS, NHDPlus, data.vizugy.hu |
| 11 | Drawing Watersheds from Data | DEMs (all), NHDPlus, data.vizugy.hu, HydroBASINS |
| 12 | Automating the Workflow | (uses data from Chs. 9--11; Google Earth Engine for cloud processing) |
| 13 | Seeing the Ground in 3D: LiDAR | 3DEP LiDAR, Hungarian LiDAR (Lechner), OpenTopography, Copernicus Data Space |
| 14 | How High Above the River? | FEMA NFHL, OVF flood maps, DEMs, LiDAR |
| 15 | Mapping Where Floods Go | FEMA, JRC Flood Hazard, EFAS, GloFAS, Copernicus EMS, DEMs, land cover, soil |
| 16 | Forecasting Floods in Real Time | HYDROINFO, EFAS, GloFAS, USGS NWIS, NWS AHPS, data.vizugy.hu, ERA5, GRDC |
| 17 | Who Lives in the Flood Zone? | FEMA NFHL, OVF flood maps, KSH, Census, Eurostat/GISCO, WorldPop, LandScan, GADM, DesInventar |
| 18 | Seeing Underground: 3D Subsurface GIS | MBFSZ, USGS geologic maps, OneGeology, EGDI |
| 19 | Wells, Boreholes, and Aquifer Maps | data.vizugy.hu (groundwater), USGS NWIS GW, MBFSZ boreholes, GRACE/G3P |
| 20 | Building a Picture of the Underground | MBFSZ, data.vizugy.hu, USGS geologic maps, EGDI, borehole databases |
| 21 | Simulating Groundwater Flow | data.vizugy.hu, USGS NWIS GW, SoilGrids, ESDAC, GRACE/GRACE-FO, WISE WFD GW |
| 22 | When Models Meet Data | data.vizugy.hu, USGS NWIS, GRDC, ERA5, GEMStat, WISE WFD |
| 23 | AI as a Hydrologist's Assistant | Google Earth Engine, Dynamic World, Copernicus Data Space, ERA5 |
| 24 | Agentic AI: The Autonomous Modeler | (uses data from all previous chapters; emphasizes automated retrieval) |
| 25 | The Future of Water Intelligence | (forward-looking -- references emerging data systems) |

---

*This appendix was compiled and verified on 2026-03-25. URLs and access conditions change over time. When a URL fails, check the Copernicus Data Space (https://dataspace.copernicus.eu/) and NASA Earthdata (https://earthdata.nasa.gov/) portals first, as they serve as consolidated gateways for most of the satellite and climate datasets listed here. For Hungarian-specific data, the OVF website (https://www.ovf.hu/) and Lechner Tudaskoezpont (https://lechnerkozpont.hu/) maintain current links to their data services.*
