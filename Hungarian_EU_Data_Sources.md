# Hungarian and EU/Copernicus Data Sources for Hydrologic/Geographic Analysis

**Compiled: 2026-03-25**
**Purpose: Equivalents to US hydrologic/geographic data systems for Hungarian watershed modeling**

> URL verification performed via WebFetch on 2026-03-25.
> Status legend: OK = accessible and returns content; PARTIAL = loads but content limited (e.g., JS-only app); FAIL = HTTP error or unreachable.

---

## 1. DEM / Elevation Data

### 1.1 DDM-5 (Digitalis Domborzatmodell) -- Hungarian National DEM
| Field | Value |
|-------|-------|
| **URL** | https://lechnerkozpont.hu/oldal/domborzatmodell (HU) / https://lechnerkozpont.hu/en/oldal/spatial-data (EN) |
| **URL Status** | OK |
| **Provider** | Lechner Tudaskoezpont (formerly FOMI) |
| **Description** | National 5 m x 5 m grid DEM in EOV projection, derived from 1:10,000 topographic contour lines and stereophotogrammetry. Updated in 2000, 2005, 2015, 2022 for major terrain changes (highways, mines). |
| **Format** | Raster grid (EOV / EPSG:23700) |
| **Access** | Order via geoshop.hu or contact Lechner data services; WMS/WMTS also available |
| **US Equivalent** | USGS 3DEP (National Elevation Dataset / NED) |
| **Notes** | Highest-resolution national DEM for Hungary. Not freely downloadable -- must be ordered. |

### 1.2 Copernicus DEM (EEA-10, GLO-30, GLO-90)
| Field | Value |
|-------|-------|
| **URL** | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM |
| **URL Status** | OK |
| **Provider** | ESA / Copernicus |
| **Description** | Digital Surface Model from TanDEM-X (2011-2015). Three instances: EEA-10 (10 m, 39 European countries, restricted access), GLO-30 (30 m, global, free), GLO-90 (90 m, global, free). GeoTIFF and DTED formats. |
| **Format** | GeoTIFF, DTED |
| **Access** | Free registration at dataspace.copernicus.eu; bulk download via S3/OData API |
| **US Equivalent** | USGS 3DEP / NED 10m & 30m |
| **Notes** | Replaces the old EU-DEM (no longer maintained). EEA-10 is the best free option for Hungary at 10 m if you qualify for access. GLO-30 is universally free. |

### 1.3 SRTM (Shuttle Radar Topography Mission)
| Field | Value |
|-------|-------|
| **URL** | https://portal.opentopography.org/raster?opentopoID=OTSRTM.082015.4326.1 |
| **URL Status** | OK |
| **Alt URLs** | https://dwtkns.com/srtm30m/ (tile selector), https://earthexplorer.usgs.gov/ |
| **Provider** | NASA / USGS |
| **Description** | 1 arc-second (~30 m) and 3 arc-second (~90 m) global DEM. Hungary is fully covered (lat 45-49N). |
| **Format** | SRTMHGT, GeoTIFF, Arc ASCII |
| **Access** | Free; some sources require NASA Earthdata login |
| **US Equivalent** | Same dataset (SRTM is a US product used globally) |
| **Notes** | Year-2000 data. Good for quick analyses but superseded by Copernicus DEM for accuracy. |

### 1.4 Hungarian LiDAR Data
| Field | Value |
|-------|-------|
| **URL** | https://lechnerkozpont.hu/en/oldal/spatial-data |
| **URL Status** | OK |
| **Provider** | Lechner Tudaskoezpont, various national park authorities |
| **Description** | No comprehensive nationwide LiDAR program like the US 3DEP. LiDAR surveys exist for specific areas (e.g., Aggtelek Karst at 2 pts/m2, various flood-prone valleys). Available through Lechner or project-specific portals. |
| **US Equivalent** | USGS 3DEP LiDAR |
| **Notes** | Coverage is fragmented. For project-specific areas, contact Lechner or relevant national parks/water directorates. |

---

## 2. Hydrologic Networks

### 2.1 OVF Hydrographic Database (data.vizugy.hu)
| Field | Value |
|-------|-------|
| **URL** | https://data.vizugy.hu |
| **URL Status** | PARTIAL (Angular app, loads but content requires browser) |
| **Alt URL** | https://www.ovf.hu/en/hydrography-water-quality/hydrographic-data (OK) |
| **Provider** | OVF (Orszagos Vizugyi Foigazgatosag / General Directorate of Water Management) |
| **Description** | Central Hydrographic Database (VRA). Water level, discharge, water temperature from surface stations; groundwater levels from monitoring wells; precipitation from hydromet network. Free and open since July 2024. |
| **Format** | Web interface, downloadable time series |
| **Access** | Free, no restrictions, attribution to OVF required |
| **US Equivalent** | NHDPlus + USGS NWIS combined |
| **Notes** | The closest Hungarian equivalent to NHDPlus for river network topology + NWIS for gauge data. |

### 2.2 HYDROINFO (Hydrological Forecasting Service)
| Field | Value |
|-------|-------|
| **URL** | https://www.hydroinfo.hu |
| **URL Status** | OK |
| **Provider** | OVF / National Water Forecasting Service |
| **Description** | Real-time water levels and forecasts for 98 sections of the Danube, Tisza, and Drava-Mura catchments. Flood warnings, ice conditions, navigation info, small watershed alerts. |
| **Format** | Web interface, mobile app |
| **Access** | Free, public |
| **US Equivalent** | USGS WaterWatch + NWS AHPS (Advanced Hydrologic Prediction Service) |
| **Notes** | Operational forecasting portal -- ideal for real-time monitoring, not bulk historical downloads. |

### 2.3 WISE (Water Information System for Europe)
| Field | Value |
|-------|-------|
| **URL** | https://water.europa.eu/ |
| **URL Status** | OK |
| **Provider** | EEA + European Commission (DG Environment, JRC, Eurostat) |
| **Description** | Pan-European water portal. Interactive maps, charts, indicators. Links to WFD reporting data including surface water body status, groundwater body status, pressures, and impacts. |
| **Format** | Web interface, downloadable thematic data |
| **Access** | Free |
| **US Equivalent** | EPA WATERS GeoViewer + How's My Waterway |

### 2.4 WISE Water Framework Directive Database
| Field | Value |
|-------|-------|
| **URL** | https://www.eea.europa.eu/data-and-maps/data/wise-wfd |
| **URL Status** | OK |
| **Alt URL** | https://discodata.eea.europa.eu (database explorer) |
| **Provider** | EEA |
| **Description** | River Basin Management Plan data reported by EU member states under WFD Article 13. Surface water bodies (ecological/chemical status, pressures), groundwater bodies (quantitative/chemical status). Data from 2000 onward, latest 2022 reporting cycle. |
| **Format** | Database explorer, downloadable tables |
| **Access** | Free |
| **US Equivalent** | EPA 305(b)/303(d) Integrated Report data |

---

## 3. Land Cover

### 3.1 CORINE Land Cover (CLC)
| Field | Value |
|-------|-------|
| **URL** | https://land.copernicus.eu/en/products/corine-land-cover |
| **URL Status** | OK |
| **Provider** | Copernicus Land Monitoring Service / EEA |
| **Description** | Pan-European land cover inventory with 44 thematic classes. Available for 1990, 2000, 2006, 2012, 2018 + change layers. Next update (2020-2024 reference) expected Q4 2025. Vector and 100 m raster. |
| **Format** | Shapefile, GeoTIFF (100 m) |
| **Access** | Free, full open access |
| **US Equivalent** | NLCD (National Land Cover Database) |
| **Notes** | THE standard land cover dataset for European hydrologic modeling. 44 classes vs. NLCD's 16 -- more detailed classification. |

### 3.2 Copernicus Land Monitoring Service (CLMS) -- Full Portfolio
| Field | Value |
|-------|-------|
| **URL** | https://land.copernicus.eu/en |
| **URL Status** | OK |
| **Provider** | Copernicus / EEA |
| **Description** | Comprehensive land monitoring: CLC, High Resolution Layers (imperviousness, tree cover, grassland, wetness, water), bio-geophysical variables (LAI, FAPAR, soil moisture), ground motion, satellite mosaics. Pan-European and global products. |
| **Format** | Various (GeoTIFF, NetCDF, Shapefile) |
| **Access** | Free, all products |
| **US Equivalent** | Combined: NLCD + MODIS land products + USGS land cover products |

---

## 4. Weather / Climate

### 4.1 OMSZ (Hungarian Meteorological Service)
| Field | Value |
|-------|-------|
| **URL** | https://www.met.hu/en/eghajlat/ |
| **URL Status** | OK |
| **Provider** | Orszagos Meteorologiai Szolgalat (HungaroMet Zrt.) |
| **Description** | Climate data series 1901-2020 for major cities (Budapest, Debrecen, Pecs, Szeged, Szombathely). 136 stations providing 10-minute data: precipitation, temperature, humidity, solar radiation, wind speed/direction. Monthly/decadal/centurial climate reports. |
| **Format** | Web interface; data requests by contact |
| **Access** | Climate summaries free on website; detailed station data may require data request |
| **US Equivalent** | NOAA NCEI (National Centers for Environmental Information) / NWS |
| **Notes** | Also provides agromet products (growing season March-September). |

### 4.2 Copernicus Climate Data Store (CDS) / ERA5
| Field | Value |
|-------|-------|
| **URL** | https://cds.climate.copernicus.eu/ |
| **URL Status** | OK |
| **Provider** | ECMWF / Copernicus Climate Change Service (C3S) |
| **Description** | ERA5: 5th-generation ECMWF reanalysis, 1940-present. ~31 km global grid, hourly. Single levels, pressure levels, ERA5-Land (9 km). Hundreds of atmospheric, land, and oceanic variables. Also hosts seasonal forecasts, projections, satellite-derived products. |
| **Format** | GRIB, NetCDF |
| **Access** | Free registration; API (cdsapi) and web download |
| **US Equivalent** | NCEP/NCAR Reanalysis + NARR + PRISM combined |
| **Notes** | THE workhorse reanalysis for European hydrologic modeling. ERA5-Land at 9 km is excellent for catchment-scale work in Hungary. |

### 4.3 E-OBS Gridded Dataset
| Field | Value |
|-------|-------|
| **URL** | https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php |
| **URL Status** | OK |
| **Alt URL** | https://cds.climate.copernicus.eu/datasets/insitu-gridded-observations-europe |
| **Provider** | KNMI / ECA&D / Copernicus |
| **Description** | Daily gridded observations for Europe, 1950-present (v32.0e, Nov 2025). Variables: Tmean, Tmin, Tmax, precipitation, sea level pressure, humidity, wind speed, global radiation. 0.1 deg and 0.25 deg grids. 20-member ensemble with uncertainty. |
| **Format** | NetCDF-4 |
| **Access** | Free download with registration |
| **US Equivalent** | PRISM / Daymet / Livneh |
| **Notes** | Station-based interpolation -- complementary to ERA5 (model-based). Best observation-based gridded dataset for Hungary. |

### 4.4 CARPATCLIM
| Field | Value |
|-------|-------|
| **URL** | https://surfobs.climate.copernicus.eu/dataaccess/access_carpatclim.php |
| **URL Status** | OK |
| **Alt URL** | https://www.met.hu/en/rolunk/palyazatok_projektek/carpatclim/ |
| **Provider** | JRC + OMSZ-led consortium (9 countries) |
| **Description** | High-resolution (0.1 deg) daily gridded climate data for the Greater Carpathian Region, 1961-2010. Variables: T2M, Tmin, Tmax, precipitation + 30+ derived indices. Homogenized and harmonized across 9 countries. |
| **Format** | NetCDF (gzipped) |
| **Access** | Free download |
| **US Equivalent** | No direct equivalent -- regional climate atlas |
| **Notes** | Specifically covers Hungary and surroundings. Excellent for historical climate analysis. Period limited to 1961-2010. |

---

## 5. Water Level / Discharge Monitoring

### 5.1 OVF / data.vizugy.hu (Hydrographic Database)
| Field | Value |
|-------|-------|
| **URL** | https://data.vizugy.hu |
| **URL Status** | PARTIAL (Angular app) |
| **Alt URL** | https://www.ovf.hu/en/hydrography-water-quality/hydrographic-data (OK) |
| **Provider** | OVF |
| **Description** | Central database of Hungarian hydrographic observations. Water level, discharge, water temperature at surface stations. Groundwater well data. Precipitation from hydromet network. Systematic records from early 20th century. Free since July 2024. |
| **Format** | Web interface, downloadable time series |
| **Access** | Free, open data |
| **US Equivalent** | USGS NWIS (National Water Information System) |

### 5.2 HYDROINFO Real-time Monitoring
| Field | Value |
|-------|-------|
| **URL** | https://www.hydroinfo.hu |
| **URL Status** | OK |
| **Provider** | OVF National Water Forecasting Service |
| **Description** | Real-time water levels and forecasts for Danube, Tisza, Drava-Mura. 98 forecast sections. Flood warnings, ice monitoring, navigation. |
| **US Equivalent** | USGS WaterWatch + NWS River Forecast Centers |

### 5.3 GRDC (Global Runoff Data Centre)
| Field | Value |
|-------|-------|
| **URL** | https://grdc.bafg.de/ |
| **URL Status** | OK |
| **Provider** | BfG (German Federal Institute of Hydrology) under WMO |
| **Description** | World's largest quality-assured river discharge collection. 9,800+ stations globally, ~435,000 station-years. Daily and monthly discharge. Hungarian stations included. WaterML2, CSV formats. |
| **Format** | WaterML2, CSV |
| **Access** | Free for non-commercial use; registration + terms acceptance required |
| **US Equivalent** | No direct US equivalent (this IS the global equivalent) |
| **Notes** | Useful for cross-border rivers (Danube, Tisza) where Hungarian data alone is insufficient. |

---

## 6. Flood Mapping

### 6.1 Hungarian Flood Risk Maps (OVF / EU Floods Directive)
| Field | Value |
|-------|-------|
| **URL** | https://geoportal.vizugy.hu |
| **URL Status** | FAIL (HTTP 403 -- requires authentication or internal network) |
| **Alt URL** | https://vizeink.hu (flood risk management plans) |
| **Provider** | OVF |
| **Description** | Flood hazard and risk maps per EU Floods Directive 2007/60/EC. Shows flood extent for various return periods. First revision completed 2022. Available by planning area unit. |
| **US Equivalent** | FEMA NFHL (National Flood Hazard Layer) / Flood Insurance Rate Maps |
| **Notes** | The geoportal may require specific access. Try the INSPIRE geoportal alternative below. |

### 6.2 JRC River Flood Hazard Maps (Europe)
| Field | Value |
|-------|-------|
| **URL** | https://data.jrc.ec.europa.eu/collection/id-0054 |
| **URL Status** | OK |
| **Provider** | JRC (Joint Research Centre) |
| **Description** | River flood hazard maps for Europe: 10-year to 500-year return periods. Plus satellite-derived flood event catalogue (2015-2024) from Copernicus Global Flood Monitoring. Based on EFAS/GloFAS hydrological modeling. |
| **Format** | GeoTIFF, downloadable datasets |
| **Access** | Free |
| **US Equivalent** | FEMA flood maps + USGS flood inundation mapping |

### 6.3 EFAS (European Flood Awareness System)
| Field | Value |
|-------|-------|
| **URL** | https://european-flood.emergency.copernicus.eu/efas_frontend/ |
| **URL Status** | PARTIAL (web viewer, requires partner login for real-time data) |
| **Provider** | Copernicus Emergency Management Service / ECMWF |
| **Description** | Pan-European flood forecasting. Probabilistic medium-range forecasts, flash flood indicators, seasonal outlooks, soil moisture, runoff, snow. Archived data publicly available; real-time data for EFAS partners only (national hydrological services). |
| **Format** | Web viewer, WMS, SOS, data archive |
| **Access** | Archives: public; Real-time: EFAS partners only |
| **US Equivalent** | NWS River Forecast Centers + NOAA National Water Model |

### 6.4 Copernicus Emergency Management Service (EMS)
| Field | Value |
|-------|-------|
| **URL** | https://emergency.copernicus.eu/ |
| **URL Status** | OK |
| **Alt URL** | https://mapping.emergency.copernicus.eu/ (on-demand mapping) |
| **Provider** | Copernicus / European Commission |
| **Description** | On-demand rapid mapping for disasters (floods, fires, earthquakes). European & Global Drought Observatories. Includes EFAS and GloFAS. Risk and Recovery Mapping for flood events. |
| **Format** | Vector/raster maps, reports |
| **Access** | Free; on-demand mapping activated by authorized users (civil protection) |
| **US Equivalent** | FEMA + USGS Emergency Response imagery |

---

## 7. Soil Data

### 7.1 ESDAC (European Soil Data Centre)
| Field | Value |
|-------|-------|
| **URL** | https://esdac.jrc.ec.europa.eu |
| **URL Status** | OK |
| **Alt URL** | https://esdac.jrc.ec.europa.eu/resource-type/soil-data-maps |
| **Provider** | JRC (European Commission) |
| **Description** | THE European soil data hub. European Soil Database (1 km raster), LUCAS soil point data, topsoil properties, soil erosion maps, organic carbon, hydraulic properties, heavy metals. Thematic layers on erosion, compaction, contamination, sealing, landslides. |
| **Format** | Shapefile, ESRI GRID, GeoTIFF, IDRISI |
| **Access** | Some datasets free; others require registration and data request |
| **US Equivalent** | USDA SSURGO / STATSGO / gSSURGO |
| **Notes** | The primary source for soil hydraulic properties needed in hydrologic modeling in Europe. |

### 7.2 SoilGrids 250m (ISRIC)
| Field | Value |
|-------|-------|
| **URL** | https://soilgrids.org/ |
| **URL Status** | PARTIAL (requires JavaScript; REST API currently paused) |
| **Alt URL** | https://isric.org/explore/soilgrids |
| **Provider** | ISRIC -- World Soil Information |
| **Description** | Global 250 m soil property maps using machine learning. 14 properties at 6 depth intervals: pH, organic carbon, bulk density, texture (sand/silt/clay), CEC, nitrogen. CC-BY 4.0. |
| **Format** | VRT (WebDAV), Google Earth Engine, WCS |
| **Access** | Free; WebDAV for bulk download; also on Google Earth Engine |
| **US Equivalent** | POLARIS / SSURGO (but global coverage) |
| **Notes** | REST API has been intermittently down. WebDAV and GEE access remain functional. |

---

## 8. Satellite Data

### 8.1 Copernicus Data Space Ecosystem (Sentinel-1/2/3)
| Field | Value |
|-------|-------|
| **URL** | https://dataspace.copernicus.eu/ |
| **URL Status** | OK |
| **Alt URL** | https://browser.dataspace.copernicus.eu/ (visual browser) |
| **Provider** | ESA / European Commission |
| **Description** | Free access to all Sentinel missions: Sentinel-1 (SAR), Sentinel-2 (optical 10 m), Sentinel-3 (ocean/land monitoring), Sentinel-5P (atmosphere). Plus Copernicus Contributing Missions. Replaced the old Open Access Hub (scihub.copernicus.eu) in Oct 2023. |
| **Format** | SAFE, GeoTIFF, NetCDF via APIs |
| **Access** | Free registration; Sentinel Hub APIs, openEO, STAC, OData, S3 |
| **US Equivalent** | USGS EarthExplorer + NASA Earthdata (Landsat, MODIS) |
| **Notes** | Sentinel-2 at 10 m optical is comparable to Landsat at 30 m but higher resolution and 5-day revisit. Essential for land use monitoring in Hungary. |

### 8.2 GRACE / GRACE-FO (Gravity Recovery and Climate Experiment)
| Field | Value |
|-------|-------|
| **URL** | https://grace.jpl.nasa.gov/data/get-data/ |
| **URL Status** | OK |
| **Alt URL** | https://gravis.gfz.de/gws (European G3P groundwater product) |
| **Provider** | NASA/JPL (GRACE) + GFZ Potsdam (G3P European product) |
| **Description** | Monthly terrestrial water storage anomalies from satellite gravity. G3P (Global Gravity-based Groundwater Product) separates groundwater from total storage. GravIS provides time series and gridded products for Europe. Monthly resolution, April 2002 - present. |
| **Format** | NetCDF, CSV |
| **Access** | Free; NASA Earthdata login for GRACE; GravIS/G3P open access |
| **US Equivalent** | Same dataset (GRACE is US-German joint mission) |
| **Notes** | GravIS at https://gravis.gfz.de/gws is particularly useful -- European-focused, separates groundwater component. OK status confirmed. |

---

## 9. Census / Demographics

### 9.1 KSH (Hungarian Central Statistical Office)
| Field | Value |
|-------|-------|
| **URL** | https://www.ksh.hu/?lang=en |
| **URL Status** | OK |
| **Alt URLs** | https://nepszamlalas2022.ksh.hu/en/database/ (Census 2022), https://data.ksh.hu/ (API) |
| **Provider** | Kozponti Statisztikai Hivatal |
| **Description** | Hungary's official statistics: population, GDP, inflation, employment, agriculture, energy, health, housing. Census 2022 with thematic maps at region/county/district/municipality level. STADAT summary tables. High-Value Datasets API (data.ksh.hu). |
| **Format** | Excel, CSV, API (JSON), interactive maps |
| **Access** | Free |
| **US Equivalent** | US Census Bureau + Bureau of Economic Analysis |

### 9.2 Eurostat + GISCO
| Field | Value |
|-------|-------|
| **URL** | https://ec.europa.eu/eurostat/web/gisco/geodata |
| **URL Status** | OK |
| **Alt URL** | https://ec.europa.eu/eurostat/ (main Eurostat portal) |
| **Provider** | European Commission / Eurostat |
| **Description** | Pan-European geodata: administrative boundaries (NUTS regions, LAU), population grids, census units, transport networks, coastlines. Multiple projections available. Also an R package (giscoR) for programmatic access. |
| **Format** | Shapefile, GeoJSON, TopoJSON, XML metadata |
| **Access** | Free for non-commercial use |
| **US Equivalent** | US Census TIGER/Line shapefiles + American Community Survey |

---

## 10. Coordinate Systems

### 10.1 HD72/EOV (Egyseges Orszagos Vetuleti rendszer)
| Field | Value |
|-------|-------|
| **URL** | https://epsg.io/23700 |
| **URL Status** | OK |
| **EPSG Code** | 23700 |
| **Datum** | Hungarian Datum 1972 (HD72) |
| **Ellipsoid** | GRS 1967 |
| **Projection** | Hotine Oblique Mercator (variant B) |
| **Parameters** | Lat center: 47.1444 deg, Lon center: 19.0486 deg, Azimuth: 90 deg, Scale: 0.99993, False E: 650,000 m, False N: 200,000 m |
| **Coordinate Ranges** | Easting (Y): ~421,000 - 950,000; Northing (X): ~44,000 - 367,000 |
| **US Equivalent** | State Plane Coordinate System (concept) |
| **Notes** | **CRITICAL**: Hungarian data labels often swap X/Y. Identify by VALUE RANGE: Northing 0-400,000; Easting 400,000-1,000,000. Most Hungarian national datasets (DDM, cadastral, water management) use EOV natively. |

### 10.2 HD72 to ETRS89 Transformation
| Field | Value |
|-------|-------|
| **URL** | https://epsg.io/1449 |
| **URL Status** | OK |
| **EPSG Code** | 1449 (transformation) |
| **Description** | 7-parameter Helmert transformation from HD72 to ETRS89. Needed when combining Hungarian national data (EOV) with EU/Copernicus data (typically in ETRS89/LAEA or WGS84). |
| **Target CRS** | ETRS89 (EPSG:4258) or ETRS89/LAEA (EPSG:3035 -- standard EU grid projection) |
| **US Equivalent** | NAD27-to-NAD83 datum transformation (concept) |
| **Notes** | PROJ provides accurate parametrization. For sub-meter work, use the Hungarian-specific grid shift file if available from Lechner. |

---

## Quick Reference: US-to-Hungarian/EU Dataset Mapping

| US Dataset | Hungarian Equivalent | EU/Global Equivalent |
|-----------|---------------------|---------------------|
| USGS 3DEP / NED | DDM-5 (Lechner) | Copernicus DEM (EEA-10, GLO-30) |
| NHDPlus | OVF river network (data.vizugy.hu) | EU-Hydro (Copernicus) |
| USGS NWIS | data.vizugy.hu | GRDC |
| NWS AHPS | HYDROINFO | EFAS |
| NLCD | -- | CORINE Land Cover |
| PRISM / Daymet | OMSZ station data | E-OBS, CARPATCLIM |
| NCEP Reanalysis | -- | ERA5 (CDS) |
| SSURGO / STATSGO | Hungarian soil survey (ESDAC) | ESDAC, SoilGrids |
| FEMA Flood Maps | OVF flood risk maps | JRC Flood Hazard Maps |
| Landsat / MODIS | -- | Sentinel-1/2/3 (Copernicus) |
| US Census TIGER | KSH | Eurostat GISCO |
| State Plane / NAD83 | HD72/EOV (EPSG:23700) | ETRS89 (EPSG:4258) |
| GRACE | -- | GRACE + G3P (GravIS) |

---

## URL Verification Summary

| # | Source | URL | Status |
|---|--------|-----|--------|
| 1 | Lechner Spatial Data | https://lechnerkozpont.hu/en/oldal/spatial-data | OK |
| 2 | data.vizugy.hu | https://data.vizugy.hu | PARTIAL (JS app) |
| 3 | OVF Hydrographic Data | https://www.ovf.hu/en/hydrography-water-quality/hydrographic-data | OK |
| 4 | HYDROINFO | https://www.hydroinfo.hu | OK |
| 5 | OMSZ Climate | https://www.met.hu/en/eghajlat/ | OK |
| 6 | Copernicus DEM | https://dataspace.copernicus.eu/.../COP-DEM | OK |
| 7 | SRTM (OpenTopography) | https://portal.opentopography.org/... | OK |
| 8 | CDS / ERA5 | https://cds.climate.copernicus.eu/ | OK |
| 9 | E-OBS | https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php | OK |
| 10 | CARPATCLIM | https://surfobs.climate.copernicus.eu/dataaccess/access_carpatclim.php | OK |
| 11 | CORINE Land Cover | https://land.copernicus.eu/en/products/corine-land-cover | OK |
| 12 | CLMS | https://land.copernicus.eu/en | OK |
| 13 | WISE | https://water.europa.eu/ | OK |
| 14 | WISE WFD Database | https://www.eea.europa.eu/data-and-maps/data/wise-wfd | OK |
| 15 | ESDAC | https://esdac.jrc.ec.europa.eu | OK |
| 16 | SoilGrids | https://soilgrids.org/ | PARTIAL (JS-only, API paused) |
| 17 | Copernicus Data Space | https://dataspace.copernicus.eu/ | OK |
| 18 | GRACE (NASA) | https://grace.jpl.nasa.gov/data/get-data/ | OK |
| 19 | GravIS / G3P | https://gravis.gfz.de/gws | OK |
| 20 | GRDC | https://grdc.bafg.de/ | OK |
| 21 | EFAS | https://european-flood.emergency.copernicus.eu/efas_frontend/ | PARTIAL (partner login) |
| 22 | Copernicus EMS | https://emergency.copernicus.eu/ | OK |
| 23 | JRC Flood Hazard | https://data.jrc.ec.europa.eu/collection/id-0054 | OK |
| 24 | OVF Flood Geoportal | https://geoportal.vizugy.hu | FAIL (403) |
| 25 | KSH | https://www.ksh.hu/?lang=en | OK |
| 26 | KSH Census 2022 | https://nepszamlalas2022.ksh.hu/en/database/ | OK |
| 27 | KSH API | https://data.ksh.hu/ | OK |
| 28 | Eurostat GISCO | https://ec.europa.eu/eurostat/web/gisco/geodata | OK |
| 29 | EPSG:23700 (EOV) | https://epsg.io/23700 | OK |
| 30 | HD72-ETRS89 transform | https://epsg.io/1449 | OK |

**Result: 25 OK, 4 PARTIAL, 1 FAIL (geoportal.vizugy.hu -- may require VPN or institutional access)**
