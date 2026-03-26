\newpage

# A. függelék: Adatforrások gyorskézikönyve

Ez a függelék a könyvben említett összes adatforrás átfogó jegyzékét tartalmazza, adattípusonként rendezve. Minden bejegyzés tartalmazza a forrás nevét, URL-jét, földrajzi lefedettségét, térbeli vagy időbeli felbontását, hozzáférési feltételeit és azokat a fejezeteket, ahol a forrás a leglényegesebb. A táblázatok amerikai, EU/magyar és globális alszekciókra tagolódnak, hogy az olvasók gyorsan megtalálhassák a régiójuknak megfelelő adatkészleteket.

Minden URL-t 2026-03-25-én ellenőriztünk. Állapotkódok: **OK** — az oldal betöltődik és tartalmat szolgáltat; **Részleges** — az oldal betöltődik, de a teljes funkcionalitáshoz JavaScript-támogatású böngésző vagy partneri bejelentkezés szükséges; **Korlátozott** — a hozzáférés intézményi jogosultságot vagy hivatalos adatkérést igényel.

---

## 1. Domborzat / Digitális domborzatmodellek

A domborzati adatok szinte minden hidroinformatikai elemzés alapját képezik. A vízgyűjtő-lehatárolástól (9–11. fejezet) az árvíztérképezésig (15. fejezet) a DEM megválasztása határozza meg az összes származtatott eredmény térbeli felbontását és vertikális pontosságát. Ez a szakasz a rendelkezésre álló DEM-ek teljes spektrumát lefedi, a nemzeti nagy felbontású termékektől a szabadon hozzáférhető globális adatkészletekig.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| USGS 3DEP (National Elevation Dataset) | https://www.usgs.gov/3d-elevation-program | Összefüggő USA, Alaszka, Hawaii, területek | 1 m (LiDAR), 10 m, 30 m | Ingyenes; USGS EarthExplorer vagy The National Map | 5, 7, 9, 10, 11, 13 |
| USGS EarthExplorer | https://earthexplorer.usgs.gov/ | USA és globális | Változó | Ingyenes; Earthdata bejelentkezés | 3, 5, 9 |
| OpenTopography | https://portal.opentopography.org/ | Globális (gondozott LiDAR- és DEM-gyűjtemények) | 1 m LiDAR – 90 m SRTM | Ingyenes; egyes adatkészletekhez bejelentkezés szükséges | 5, 13 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| DDM-5 (Magyar Országos DEM) | https://lechnerkozpont.hu/oldal/domborzatmodell | Magyarország | 5 m | Rendelés a geoshop.hu-n vagy a Lechner adatszolgáltatáson keresztül; WMS/WMTS elérhető | 5, 7, 9, 10, 11 |
| Magyar LiDAR-adatok | https://lechnerkozpont.hu/en/oldal/spatial-data | Részleges lefedettség (kijelölt területek) | 0,5–2 m (felmérésenként változó) | Kapcsolatfelvétel a Lechnerrel vagy a releváns vízügyi igazgatóságokkal | 13, 14 |
| Copernicus DEM EEA-10 | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | 39 európai ország | 10 m | Ingyenes; korlátozott hozzáférés (minősített intézmények) | 5, 9, 10, 11 |
| Copernicus DEM GLO-30 | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | Globális | 30 m | Ingyenes; Copernicus Data Space regisztráció | 5, 9, 10, 11, 15 |
| Copernicus DEM GLO-90 | (mint fent) | Globális | 90 m | Ingyenes | 5, 9 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| SRTM (Shuttle Radar Topography Mission) | https://www.earthdata.nasa.gov/data/instruments/srtm | 60°É–56°D (~szárazföld 80%-a) | 30 m (1 ívmp), 90 m (3 ívmp) | Ingyenes; NASA Earthdata bejelentkezés | 5, 9, 10, 11 |
| ALOS World 3D (AW3D30) | https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm | Globális | 30 m | Ingyenes; JAXA regisztráció | 5 |
| ASTER GDEM v3 | https://asterweb.jpl.nasa.gov/gdem.asp | 83°É–83°D | 30 m | Ingyenes; NASA Earthdata bejelentkezés | 5 |
| MERIT DEM | https://global-hydrodynamics.github.io/MERIT_DEM/ | Globális szárazföld, 90°É–60°D | 90 m (3 ívmp) | Ingyenes; CC-BY-NC 4.0 licenc | 5, 9, 10 |
| TanDEM-X 90m | https://geoservice.dlr.de/web/dataguide/tdm90/ | Globális | 90 m | Tudományos felhasználásra ingyenes; DLR regisztráció | 5 |

---

## 2. Vízfolyáshálózatok / Hidrográfia

A vízfolyáshálózati adatok a vízgyűjtő digitális vázát képviselik. Az amerikai rendszerben a National Hydrography Dataset (NHDPlus) egységes, attribútumokkal ellátott vízfolyáshálózatot biztosít. Magyarországon az OVF Hidrográfiai Adatbázisa szolgál hasonló célra. Globális tanulmányokhoz a HydroSHEDS termékcsalád kínál összefüggő lefedettséget. Ezek az adatkészletek központi szerepet játszanak a 9–12. fejezetben, ahol a vízgyűjtő-lehatárolást és a vízfolyáshálózat-kinyerést tárgyaljuk részletesen.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| NHDPlus (National Hydrography Dataset Plus) | https://www.usgs.gov/national-hydrography/nhdplus-high-resolution | Összefüggő USA | 1:24 000 méretarány | Ingyenes; The National Map letöltés | 2, 3, 9, 10, 11, 12 |
| USGS NWIS (National Water Information System) | https://waterdata.usgs.gov/nwis | USA | Állomásalapú | Ingyenes; webszolgáltatások és tömeges letöltés | 3, 8, 16, 22 |
| NWS AHPS (Advanced Hydrologic Prediction Service) | https://water.weather.gov/ahps/ | USA | Előrejelzési pontok | Ingyenes | 16 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| OVF Hidrográfiai Adatbázis (data.vizugy.hu) | https://data.vizugy.hu | Magyarország | Állomásalapú + vektor-hálózat | Ingyenes (2024 júliusa óta nyílt); OVF forrásmegjelölés szükséges | 2, 3, 9, 11, 16, 22 |
| HYDROINFO (Valós idejű figyelés) | https://www.hydroinfo.hu | Magyarország (Duna, Tisza, Dráva-Mura) | 98 előrejelzési szelvény | Ingyenes | 16 |
| WISE (Water Information System for Europe) | https://water.europa.eu/ | Páneurópai | Változó | Ingyenes | 3, 22 |
| WISE WFD adatbázis | https://www.eea.europa.eu/data-and-maps/data/wise-wfd | EU tagállamok | Víztest szint | Ingyenes | 3, 22 |
| EFAS (Európai Árvíz-figyelmeztető Rendszer) | https://european-flood.emergency.copernicus.eu/efas_frontend/ | Páneurópai | 5 km | Archívumok nyilvánosak; valós idejű adatok EFAS partnerek számára | 15, 16 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| HydroSHEDS / HydroRIVERS / HydroBASINS | https://www.hydrosheds.org/ | Globális | 3–15 ívmp | Ingyenes | 9, 10, 11, 12 |
| GRDC (Global Runoff Data Centre) | https://grdc.bafg.de/ | Globális (9800+ állomás) | Állomásalapú; napi és havi | Nem kereskedelmi célra ingyenes; regisztráció szükséges | 3, 16, 22 |
| GloFAS (Globális Árvíz-figyelmeztető Rendszer) | https://global-flood.emergency.copernicus.eu/ | Globális | 0,05 fok (~5 km) | Ingyenes | 15, 16 |
| GEMStat (Globális Vízminőség) | https://gemstat.org/ | Globális (állomásalapú) | Pontmérések | Ingyenes | 22 |
| Nile Basin Initiative | https://nilebasin.org/ | Nílus-medence (10 ország) | Változó | Egyes adatok ingyenesek; egyéb adatokhoz intézményi kérés szükséges | 3 |
| Niger Basin Authority | https://www.abn.ne/index.php/en/ | Niger-medence (9 ország) | Változó | Intézményi kérés | 3 |
| Mekong River Commission | https://www.mrcmekong.org/ | Mekong-medence (4 ország + 2 párbeszédes partner) | Változó | Adatportál; egyes adatkészletekhez kérés szükséges | 3 |

---

## 3. Felszínborítás

A felszínborítás-osztályozás határozza meg, hogyan oszlik meg a csapadék beszivárgásra, lefolyásra és evapotranszspirációra. A hidrológiai modellezésben a felszínborítási adatkészlet megválasztása közvetlenül befolyásolja a lefolyási számokat, a Manning-érdességi együtthatókat és a vízzáróság-becsléseket. A 6. fejezet bevezeti a térképi algebra műveleteket a felszínborítási rácsokon, míg a 9. és a 15. fejezet alkalmazza a felszínborítási adatokat a vízgyűjtő- és az árvízmodellezésben.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| NLCD (National Land Cover Database) | https://www.mrlc.gov/ | Összefüggő USA, Alaszka, Hawaii | 30 m | Ingyenes | 6, 9, 15 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| CORINE Land Cover (CLC) | https://land.copernicus.eu/en/products/corine-land-cover | Páneurópai (39 ország) | 100 m raszter / vektor | Ingyenes | 6, 9, 15 |
| Copernicus Land Monitoring Service (CLMS) | https://land.copernicus.eu/en | Páneurópai és globális | Változó (10 m – 1 km) | Ingyenes | 6, 9 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| ESA WorldCover | https://esa-worldcover.org/ | Globális | 10 m | Ingyenes | 6, 9, 15 |
| MODIS Land Cover (MCD12Q1) | https://modis.gsfc.nasa.gov/data/dataprod/mod12.php | Globális | 500 m | Ingyenes; NASA Earthdata | 6 |
| GlobeLand30 | https://www.globeland30.org/ | Globális | 30 m | Ingyenes; regisztráció szükséges (szakaszos elérhetőség) | 6 |
| Dynamic World (Google) | https://dynamicworld.app/ | Globális | 10 m | Ingyenes; Google Earth Engine | 6, 23 |

---

## 4. Talaj

A talaj hidraulikai tulajdonságai — telített vezetőképesség, porozitás, szántóföldi vízkapacitás, hervadáspont — minden csapadék-lefolyás modell alapvető bemeneti adatai. Az európai talajadatokat az ESDAC központosítja a Közös Kutatóközpontban, míg az Egyesült Államok a USDA által kezelt SSURGO/STATSGO rendszerre támaszkodik. Globális lefedettséghez a SoilGrids és a Harmonized World Soil Database gépi tanuláson alapuló és szakértők által összeállított talajtulajdonság-térképeket biztosít. Ezeket az adatkészleteket kiterjedten alkalmazzuk a 9., 15. és 21. fejezetben.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| USDA SSURGO / gSSURGO | https://www.nrcs.usda.gov/resources/data-and-reports/gridded-soil-survey-geographic-gssurgo-database | Összefüggő USA | ~10 m (megyei szintű felmérések) | Ingyenes | 9, 15, 21 |
| USDA STATSGO2 | https://www.nrcs.usda.gov/resources/data-and-reports/description-of-statsgo2-database | Összefüggő USA | ~1 km | Ingyenes | 9 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| ESDAC (European Soil Data Centre) | https://esdac.jrc.ec.europa.eu | Páneurópai | 1 km (European Soil Database) + pontadatok (LUCAS) | Ingyenes; egyes adatkészletekhez regisztráció és kérés szükséges | 9, 15, 21 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| SoilGrids 250m (ISRIC) | https://soilgrids.org/ | Globális | 250 m | Ingyenes; WebDAV, WCS, Google Earth Engine | 9, 21 |
| HWSD v2.0 (Harmonized World Soil Database) | https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/ | Globális | 1 km (30 ívmp) | Ingyenes | 9 |
| FAO/UNESCO Digital Soil Map of the World | https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/faounesco-soil-map-of-the-world/en/ | Globális | 1:5 000 000 méretarány | Ingyenes | 9 |

---

## 5. Időjárás / Éghajlat

Az időjárási és éghajlati adatok vezérlik az összes hidrológiai szimulációt. A csapadék az elsődleges bemenet; a hőmérséklet, a páratartalom, a szél és a sugárzás az evapotranszspirációt szabályozza. Az állomási megfigyelések, a rácsos interpolációs termékek, a műholdas becslések és a reanalízis adatkészletek közötti választás a vizsgálati régiótól és az igényelt időbeli felbontástól függ. A 8. fejezet részletesen tárgyalja a csapadékmérést, míg a 15. és 16. fejezet alkalmazza az időjárási adatokat az árvízmodellezésben és -előrejelzésben.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| NOAA NCEI (National Centers for Environmental Information) | https://www.ncei.noaa.gov/ | USA és globális | Állomásalapú | Ingyenes | 8 |
| PRISM | https://prism.oregonstate.edu/ | Összefüggő USA | 4 km, napi/havi | Ingyenes | 8 |
| Daymet | https://daymet.ornl.gov/ | Észak-Amerika | 1 km, napi | Ingyenes | 8 |
| NCEP/NCAR Reanalysis | https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html | Globális | ~210 km (T62 rács), 6 óránkénti | Ingyenes | 8 |
| NOAA National Water Model | https://water.noaa.gov/ | Összefüggő USA | ~1 km, óránkénti | Ingyenes | 16 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| OMSZ (Országos Meteorológiai Szolgálat) | https://www.met.hu/en/eghajlat/ | Magyarország (136 állomás) | Állomásalapú; 10 perces intervallumok | Éghajlati összegzések ingyenesek; részletes adatok kérésre | 8 |
| OMSZ Open Data Portál (odp.met.hu) | https://odp.met.hu/ | Magyarország | Állomás- és rácsalapú | Ingyenes; nyílt adatportál | 8, 16 |
| ERA5 (Copernicus Climate Data Store) | https://cds.climate.copernicus.eu/ | Globális | 31 km (~0,25 fok), óránkénti | Ingyenes; CDS regisztráció | 8, 15, 16, 22 |
| ERA5-Land | https://cds.climate.copernicus.eu/ | Globális | 9 km (~0,1 fok), óránkénti | Ingyenes; CDS regisztráció | 8, 15 |
| E-OBS rácsos adatkészlet | https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php | Európa | 0,1 fok és 0,25 fok, napi | Ingyenes; regisztráció | 8 |
| CARPATCLIM | https://surfobs.climate.copernicus.eu/dataaccess/access_carpatclim.php | Kárpát-régió (9 ország) | 0,1 fok, napi | Ingyenes | 8 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| CHIRPS (Climate Hazards Group) | https://www.chc.ucsb.edu/data/chirps | 50°D–50°É (kvázi-globális) | 5 km, napi/havi | Ingyenes | 8 |
| GPM / IMERG (NASA/JAXA) | https://gpm.nasa.gov/ | 67°D–67°É (mag), kiterjesztve 90°D–90°É | 10 km, félóránkénti | Ingyenes; NASA Earthdata | 8 |
| CRU TS (Climate Research Unit) | https://crudata.uea.ac.uk/cru/data/hrg/ | Globális szárazföld (Antarktisz nélkül) | 0,5 fok, havi | Ingyenes | 8 |
| APHRODITE (Ázsiai csapadék) | https://www.chikyu.ac.jp/precip/english/ | Monszun-Ázsia, Közel-Kelet, Oroszország | 0,25 fok, napi | Ingyenes; regisztráció | 8 |
| IMD (India Meteorological Department) | https://mausam.imd.gov.in/ | India | Állomásalapú és 0,25 fokos rács | Részben ingyenes; kutatási adatok kérésre | 8 |

---

## 6. Vízhozam / Vízszint

A vízhozam- és vízszint-megfigyelések jelentik azt a referenciaigazságot, amelyhez minden hidrológiai modellt kalibrálnak és validálnak. Magyarországon az OVF rendszere biztosítja a történeti és valós idejű vízhozam-adatokat; az Egyesült Államokban a USGS NWIS hálózat az arany standard. Határon átnyúló és globális tanulmányokhoz a GRDC nélkülözhetetlen. Ezek az adatkészletek a könyv egészében megjelennek, de legkritikusabbak a 16. fejezetben (valós idejű előrejelzés) és a 22. fejezetben (modellkalibráció).

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| USGS NWIS | https://waterdata.usgs.gov/nwis | USA (~13 000 vízhozammérő állomás) | Pillanatnyi (15 perces), napi, havi | Ingyenes | 3, 16, 22 |
| USGS WaterWatch | https://waterwatch.usgs.gov/ | USA | Valós idejű térképek | Ingyenes | 16 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| OVF / data.vizugy.hu | https://data.vizugy.hu | Magyarország | Napon belüli – havi (történeti adatok a 20. sz. elejétől) | Ingyenes (2024 júliusa óta nyílt) | 3, 16, 22 |
| HYDROINFO | https://www.hydroinfo.hu | Magyarország (Duna, Tisza, Dráva-Mura) | Valós idejű + 98 előrejelzési szelvény | Ingyenes | 16 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| GRDC | https://grdc.bafg.de/ | Globális (9800+ állomás, ~435 000 állomás-év) | Napi, havi | Nem kereskedelmi célra ingyenes; regisztráció + feltételek | 3, 16, 22 |
| FAO AQUASTAT | https://www.fao.org/aquastat/en/ | Globális (országszintű) | Országos és szubnacionális statisztikák | Ingyenes | 3 |
| India WRIS | https://indiawris.gov.in/wris/ | India | Állomásalapú | Ingyenes (szakaszos elérhetőség) | 3 |

---

## 7. Árvíztérképezés

Az árvíztérképek a hidrológiai modellkimeneteket cselekvésre alkalmas térbeli információvá alakítják: mely területek kerülnek víz alá, milyen mélységben és milyen visszatérési időre vonatkozóan. Az Egyesült Államokban a FEMA kezeli a National Flood Hazard Layer-t; az EU-ban az Árvízi irányelv előírja a tagállamok számára az egyenértékű árvízveszély- és kockázati térképek elkészítését. A műholdas árvízfigyelés közel valós idejű megfigyelésekkel egészíti ki ezeket a termékeket az események során. Ezek az adatkészletek központi szerepet játszanak a 14–17. fejezetben.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| FEMA NFHL (National Flood Hazard Layer) | https://msc.fema.gov/portal/home | USA | Parcellaszintű | Ingyenes | 14, 15, 17 |
| USGS Flood Inundation Mapping Program | https://www.usgs.gov/mission-areas/water-resources/science/flood-inundation-mapping-fim-program | USA (kiválasztott települések) | Változó | Ingyenes | 14, 15 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| Magyar Árvízkockázati Térképek (OVF) | https://geoportal.vizugy.hu | Magyarország | Tervezési területi egység | Korlátozott (VPN vagy intézményi hozzáférés szükséges lehet) | 15, 17 |
| Árvízkockázat-kezelési Tervek (vizeink.hu) | https://vizeink.hu | Magyarország | Tervezési területi egység | Ingyenes | 15, 17 |
| JRC folyóárvíz-veszélytérképek | https://data.jrc.ec.europa.eu/collection/id-0054 | Európa | GeoTIFF raszter | Ingyenes | 15 |
| EFAS (Európai Árvíz-figyelmeztető Rendszer) | https://european-flood.emergency.copernicus.eu/efas_frontend/ | Páneurópai | 5 km | Archívumok nyilvánosak; valós idejű adatok partnerek számára | 15, 16 |
| Copernicus Veszélyhelyzet-kezelési Szolgálat | https://emergency.copernicus.eu/ | Európai és globális | Eseményspecifikus | Ingyenes; igény szerinti térképezés felhatalmazott felhasználók által | 15, 16 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| GloFAS | https://global-flood.emergency.copernicus.eu/ | Globális | 0,05 fok (~5 km) | Ingyenes | 15, 16 |
| Dartmouth Flood Observatory | https://floodobservatory.colorado.edu/ | Globális | Eseményalapú | Ingyenes | 15 |
| DesInventar Sendai (UNDRR) | https://www.desinventar.net/ | Globális (82 ország) | Táblázatos katasztrófanyilvántartás | Ingyenes; nyílt forráskódú | 15, 17 |
| African Flood and Drought Monitor | https://hydrology.soton.ac.uk/apps/afdm/ | Afrika | 5 km | Ingyenes | 15, 16 |

---

## 8. Demográfia / Népesség

A népességi és társadalmi-gazdasági adatok lehetővé teszik a sérülékenységi értékelést: ki van veszélyben árvíz esetén, és milyen infrastruktúra van kitéve. A 17. fejezet kifejezetten az árvízkockázati kitettség elemzésével foglalkozik, az árvíztérképeket népszámlálási és népesség-adatokkal kombinálva. Az amerikai Census TIGER/Line rendszer, a magyar KSH és az Eurostat GISCO rendszere biztosítja a demográfiai attribútumokkal ellátott közigazgatási határokat több léptéken.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| US Census Bureau / TIGER/Line | https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html | USA | Számlálókerülettől országosig | Ingyenes | 17 |
| American Community Survey | https://www.census.gov/programs-surveys/acs | USA | Számlálókörzet | Ingyenes | 17 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| KSH (Központi Statisztikai Hivatal) | https://www.ksh.hu/?lang=en | Magyarország | Településtől országosig | Ingyenes | 17 |
| KSH Népszámlálás 2022 | https://nepszamlalas2022.ksh.hu/en/database/ | Magyarország | Település, járás, megye, régió | Ingyenes | 17 |
| KSH Open Data API (data.ksh.hu) | https://data.ksh.hu/ | Magyarország | Változó | Ingyenes; JSON API | 17 |
| Eurostat / GISCO | https://ec.europa.eu/eurostat/web/gisco/geodata | Páneurópai (NUTS, LAU régiók) | Közigazgatási egységek, 1 km-es népességi rács | Nem kereskedelmi célra ingyenes | 17 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| WorldPop | https://www.worldpop.org/ | Globális (hangsúly Afrikán, Ázsián, Latin-Amerikán) | 100 m és 1 km | Ingyenes | 17 |
| LandScan (ORNL) | https://landscan.ornl.gov/ | Globális | ~1 km | Kutatási célra ingyenes; regisztráció | 17 |
| UN World Population Prospects | https://population.un.org/wpp/ | Globális (országszintű) | Országos és regionális | Ingyenes | 17 |
| GADM (Global Administrative Areas) | https://gadm.org/ | Globális (minden ország) | Nagy felbontású határok, minden közigazgatási szint | Ingyenes | 17 |

---

## 9. Műholdképek

A műholdképek a modern hidroinformatika megfigyelési gerincét biztosítják. Az optikai szenzorok (Sentinel-2, Landsat) a felszínborítást és a felszíni víz kiterjedését térképezik; a szintetikus apertúrájú radar (Sentinel-1) felhőkön áthatolva észleli az árvizeket; a termális szenzorok az evapotranszspirációt mérik; a gravitációs műholdak (GRACE) a teljes vízkészlet-változásokat mutatják ki. A felhőszámítási platformok, mint a Google Earth Engine és a Copernicus Data Space, átalakították az adatok hozzáférését, lehetővé téve, hogy a korábban hetes letöltést és előfeldolgozást igénylő elemzéseket percek alatt lehessen elvégezni. A műholdas adatok kiemelkedően jelennek meg a 2., 6., 13., 15. és 23. fejezetben.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| NASA Earthdata | https://earthdata.nasa.gov/ | Globális (178+ PB) | Változó (Landsat, MODIS, GPM, GRACE, SRTM stb.) | Ingyenes; Earthdata bejelentkezés | 2, 3, 5, 8, 13 |
| Landsat (USGS/NASA) | https://www.usgs.gov/landsat-missions | Globális | 30 m optikai, 15 m pankromatikus, 100 m termál | Ingyenes | 2, 6 |
| MODIS (NASA) | https://modis.gsfc.nasa.gov/ | Globális | 250 m – 1 km | Ingyenes; NASA Earthdata | 6, 8 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| Copernicus Data Space Ecosystem | https://dataspace.copernicus.eu/ | Globális (Sentinel-1, -2, -3, -5P + közreműködő missziók) | 10 m (S2 optikai), 5x20 m (S1 SAR), 300 m (S3) | Ingyenes; regisztráció szükséges | 2, 6, 13, 15 |
| Copernicus Browser | https://browser.dataspace.copernicus.eu/ | Globális | Változó | Ingyenes; vizuális böngésző Sentinel adatokhoz | 2 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| Google Earth Engine (GEE) | https://earthengine.google.com/ | Globális (több petabájtos katalógus) | Változó (Landsat, Sentinel, MODIS, DEM-ek, éghajlati adatok stb.) | Akadémiai/kutatási célra ingyenes; kereskedelmi licencelés elérhető | 2, 6, 12, 23 |

---

## 10. Felszín alatti víz

A felszín alatti vízkészletek a felszínről láthatatlanok, de kúthálózatokon, geofizikai méréseken és műholdas gravitációmérésen keresztül megfigyelhetők. Magyarországon az OVF kiterjedt megfigyelő kúthálózatot tart fenn, amely a data.vizugy.hu-n keresztül érhető el. A GRACE műholdmisszió az egyetlen eszköz a nagyszabású felszín alatti vízkészlet-változások űrből történő kimutatásához. Ezek az adatforrások elengedhetetlenek a 18–21. fejezetekhez, amelyek a 3D felszín alatti térinformatikát, a kútadatkezelést, a vízadó réteg-jellemzést és a felszín alatti víz áramlási szimulációt tárgyalják.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| USGS NWIS Groundwater | https://waterdata.usgs.gov/nwis/gw | USA | Pontállomások (megfigyelőkutak) | Ingyenes | 19, 20, 21 |
| USGS National Water Dashboard | https://dashboard.waterdata.usgs.gov/ | USA | Valós idejű kútszintek | Ingyenes | 19 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| OVF felszín alatti víz adatok (data.vizugy.hu) | https://data.vizugy.hu | Magyarország (megfigyelőkutak) | Pontállomások | Ingyenes (2024 júliusa óta nyílt) | 19, 20, 21 |
| WISE WFD felszín alatti víztestek | https://www.eea.europa.eu/data-and-maps/data/wise-wfd | EU tagállamok | Felszín alatti víztest szint | Ingyenes | 19, 21 |
| GravIS / G3P (európai felszín alatti víz GRACE-ből) | https://gravis.gfz.de/gws | Európai fókusz (globális elérhető) | ~300 km, havi | Ingyenes | 19, 21 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| GRACE / GRACE-FO | https://grace.jpl.nasa.gov/ | Globális | ~300 km (mascon-megoldások magasabb effektív felbontást biztosítanak), havi | Ingyenes; NASA Earthdata bejelentkezés | 19, 21 |
| IGRAC (International Groundwater Resources Assessment Centre) | https://www.un-igrac.org/ | Globális | Változó | Ingyenes; egyes adatkészletekhez kérés szükséges | 19 |

---

## 11. Földtani térképek

A földtani térképek a felszín alatti víz modellezés keretét biztosítják: a kőzettan határozza meg a hidraulikus vezetőképességet, a formációhatárok definiálják a vízadó réteg-határokat, és a szerkezeti elemek (vetők, redők) irányítják az áramlási útvonalakat. Magyarországon az MBFSZ kezeli a nemzeti földtani térképszolgálatot. Ezek az adatok leginkább a 18–21. fejezetek szempontjából relevánsak.

### Amerikai források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| USGS National Geologic Map Database | https://ngmdb.usgs.gov/ | USA | Változó (1:24 000 – 1:500 000) | Ingyenes | 18, 20 |
| USGS 3D Hydrogeologic Framework Models | https://www.usgs.gov/programs/groundwater-and-streamflow-information-program | Kiválasztott amerikai vízadó rendszerek | Modellspecifikus | Ingyenes | 18, 20, 21 |

### EU / Magyar források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| MBFSZ (Magyar Bányászati és Földtani Szolgálat) | https://map.mbfsz.gov.hu/ | Magyarország | 1:100 000 és nagyobb | Ingyenes; interaktív térképnézegető | 18, 19, 20 |
| OneGeology Europe | https://www.onegeology.org/ | Páneurópai és globális | Változó | Ingyenes; WMS szolgáltatások | 18, 20 |
| EGDI (European Geological Data Infrastructure) | https://www.europe-geology.eu/ | Páneurópai | Változó (harmonizált földtani térképek) | Ingyenes | 18, 20 |

### Globális források

| Név | URL | Lefedettség | Felbontás | Hozzáférés | Fejezetek |
|-----|-----|-------------|-----------|------------|-----------|
| OneGeology Portal | https://portal.onegeology.org/ | Globális (résztvevő földtani szolgálatok) | Országfüggő | Ingyenes; WMS szolgáltatások | 18 |
| CGMW (Commission for the Geological Map of the World) | https://www.ccgm.org/ | Globális | 1:5 000 000 és kisebb | Egyes térképek ingyenesek; mások megvásárolhatók | 18 |

---

## Koordináta-vonatkoztatási rendszerek gyors áttekintése

Az amerikai, magyar és EU-adatkészletek közötti munkavégzés során a koordináta-rendszer-eltérések a hibák egyik leggyakoribb forrásai. Ez a táblázat a könyvben előforduló legfontosabb koordináta-vonatkoztatási rendszereket foglalja össze.

| Koordinátarendszer | EPSG-kód | Felhasználás | Koordinátatartomány | Megjegyzés |
|-------------------|----------|-------------|---------------------|------------|
| HD72/EOV | EPSG:23700 | Magyar országos adatkészletek | Északi: 0–400 000; Keleti: 400 000–1 000 000 | **Az értéktartomány alapján azonosítandó, nem a fejlécek alapján** — a magyar fejlécek gyakran felcserélik az X/Y-t |
| ETRS89 (földrajzi) | EPSG:4258 | EU-szintű földrajzi koordináták | Szél./Hossz. fokban | Szabványos EU földrajzi vonatkoztatási rendszer |
| ETRS89/LAEA | EPSG:3035 | EU-szintű vetített (területtartó) | Metrikus, Európára központosított | Szabványos a páneurópai raszteradatokhoz |
| WGS84 | EPSG:4326 | Globális GPS-koordináták, legtöbb műholdas adat | Szél./Hossz. fokban | Gyakorlati célokra szinte azonos az ETRS89-cel |
| NAD83 | EPSG:4269 | Amerikai országos adatkészletek | Szél./Hossz. fokban | Az ETRS89 amerikai megfelelője |
| UTM 34. zóna É (WGS84) | EPSG:32634 | Magyarország az UTM 34. északi zónába esik | Metrikus | Alternatíva az EOV-hoz helyi metrikus munkákhoz |

A HD72–ETRS89 transzformáció (EPSG:1449) hétparaméteres Helmert-transzformációt alkalmaz. Szubméteres pontossághoz a Lechner Tudásközponttól elérhető magyar specifikus rácseltolási fájl használandó. A PROJ helyesen kezeli ezt a transzformációt a https://epsg.io/1449 címen dokumentált paraméterekkel.

---

## Magyar vízügyi adatportálok útmutatója

Magyarország jelentős előrelépést tett a vízügyi és környezeti adatok nyilvános hozzáférhetővé tételében. Öt kulcsfontosságú portál biztosítja a vízügyi kutató számára szükséges adatok zömét. Ez a szakasz lépésről lépésre szóló útmutatókat nyújt az egyes portálok eléréséhez, olyan felhasználók számára írva, akik esetleg először találkoznak ezekkel a rendszerekkel. Az összes portál alapértelmezés szerint magyar nyelvű, de a legtöbb legalább részleges angol felületet kínál. Ahol az angol nem elérhető, a böngészőalapú fordítóeszközök jól működnek.

### 1. portál: data.vizugy.hu — A központi hidrográfiai adatbázis

**Tartalma.** Ez a portál nagyjából a USGS NWIS magyar megfelelője. Történeti és aktuális idősorokat biztosít a felszíni vízszintekhez, a folyóvízhozamhoz, a vízhőmérséklethez, a figyelőkutak talajvízszint-adataihoz és a hidrometeorológiai állomáshálózat csapadékadataihoz. Az adatok 2024 júliusa óta korlátozás nélkül szabadon hozzáférhetők — ez mérföldkő jelentőségű döntés, amely összhangba hozta Magyarországot a nemzetközi nyílt adatokra vonatkozó legjobb gyakorlatokkal.

**Lépésről lépésre hozzáférési eljárás.**

1. **Navigáljon a portálra.** Nyissa meg a https://data.vizugy.hu oldalt egy modern böngészőben (Chrome, Firefox vagy Edge). Az oldal Angular egyoldalas alkalmazásként épül fel, ezért a JavaScriptet engedélyezni kell. Hagyjon néhány másodpercet az alkalmazás teljes betöltődéséhez.

2. **Ismerje meg a felület elrendezését.** A főoldalon Magyarország térképe jelenik meg, amelyen a megfigyelőállomások színes pontokként láthatók. A felszíni vízügyi állomások jellemzően kékek, a felszín alatti víz megfigyelőkutak zöldek vagy sárgák, a csapadékállomásokat pedig eltérően jelölik. Egy oldalsáv vagy eszköztár szűrési lehetőségeket biztosít.

3. **Válasszon állomást.** Kattinthat közvetlenül egy állomáspontra a térképen, vagy használhatja a keresőfunkciót egy állomás név vagy azonosító szerinti kereséséhez. A főbb folyók (Duna, Tisza, Dráva, Rába, Sajó, Hernád, Körös, Maros, Zala) állomásai a felső szakasztól az alsó szakaszig vannak felsorolva.

4. **Válassza ki a paramétert és az időtartományt.** Az állomás kiválasztása után a portál megjeleníti az adott állomáshoz elérhető paramétereket. A gyakori paraméterek közé tartozik a vízállás (vízállás), a vízhozam (vízhozam), a vízhőmérséklet (vízhőmérséklet) és a megfigyelőkutak esetében a talajvízszint (talajvízszint). Válassza ki a paramétert, majd adja meg az idősor kezdő- és végdátumát.

5. **Tekintse meg és töltse le az adatokat.** A portál interaktív diagramon jeleníti meg az idősort. A diagram alatt vagy egy letöltés gombbal exportálhatja az adatokat. A gyakori formátumok a CSV és az Excel. Figyeljen az időbélyeg formátumára (jellemzően közép-európai idő) és a mértékegységekre (vízállás cm-ben a helyi mércedátum felett, vízhozam m³/s-ban).

6. **Forrásmegjelölés.** Az adatok publikációkban történő felhasználásakor hivatkozza az OVF-et (Országos Vízügyi Főigazgatóság) mint adatszolgáltatót, az állomás nevével és a paraméterrel együtt.

**Tippek és gyakori problémák.**

- Az Angular alkalmazás régebbi böngészőkben nem mindig jelenik meg megfelelően. Használja a Chrome vagy Firefox legújabb verzióját.
- Ha a térkép nem töltődik be, próbálja meg törölni a böngésző gyorsítótárát vagy letiltani a hirdetésblokkoló bővítményeket.
- Nagyon hosszú idősorok (több évtized) esetén a letöltés több percet is igénybe vehet. Legyen türelmes.
- A https://www.ovf.hu/en/hydrography-water-quality/hydrographic-data alternatív URL hagyományosabb HTML-oldalt biztosít adatletöltési linkekkel, és hasznos tartalékként szolgál, ha az Angular alkalmazás nem reagál.
- Az állomás-metaadatok (koordináták, nullponti magasság, folyókilométer) általában az állomás részletező oldalán elérhetők. Vegye figyelembe, hogy a koordináták EOV-ban (EPSG:23700) vannak megadva — az északi értéket (0–400 000) és a keleti értéket (400 000–1 000 000) az értéktartomány alapján azonosítsa, mivel a címkék néha felcserélődnek.

---

### 2. portál: hydroinfo.hu — Valós idejű vízszintfigyelés és árvíz-előrejelzések

**Tartalma.** A HYDROINFO Magyarország operatív vízelőrejelzési portálja, amely az Egyesült Államok NWS Advanced Hydrologic Prediction Service-ének felel meg. Aktuális vízszinteket, árvízfigyelmeztetéseket, jégviszonyokat, hajózási információkat és rövid távú előrejelzéseket biztosít a Duna, a Tisza és a Dráva-Mura vízgyűjtőinek 98 szelvényére. Tartalmaz egy kisvízfolyások villámárvíz-riasztó rendszert is.

**Lépésről lépésre hozzáférési eljárás.**

1. **Navigáljon a portálra.** Nyissa meg a https://www.hydroinfo.hu oldalt bármely böngészőben. Az oldal alapértelmezésben magyarul jelenik meg. Keresse a nyelv-választót (jellemzően egy zászló ikont vagy „EN" linket) a jobb felső sarokban az angol változathoz.

2. **Fedezze fel a térképnézetet.** A főoldal jellemzően Magyarország áttekintő térképét mutatja, amelyen a folyószakaszok az árvízi riasztási szint szerint vannak színkódolva: zöld a normál állapothoz, sárga az elsőfokú riasztáshoz, narancssárga a másodfokúhoz, és piros a harmadfokú (legmagasabb) riasztáshoz. Kattintson bármely folyószakaszra vagy állomásra a részletek megtekintéséhez.

3. **Tekintse meg az állomásadatokat.** Egy állomásra kattintva részletes oldal jelenik meg az aktuális vízszinttel, a tendenciával (emelkedő, csökkenő vagy stabil), az adott állomás riasztási küszöbértékeivel és egy hidrográffal, amely a közelmúlt vízszintváltozását mutatja. Egyes állomások vízhozambecsléseket is mutatnak.

4. **Tekintse meg az árvíz-előrejelzéseket.** Az előrejelzési rész valószínűségi vízszint-előrejelzéseket biztosít a következő napokra. A Dunára jellemzően 5–7 napos előrejelzések érhetők el; a kisebb folyóknál rövidebb előrejelzési időtáv lehet. Az előrejelzések konfidencia-sávokkal ellátott hidrográfokként jelennek meg.

5. **Mobil elérés.** A HYDROINFO mobil alkalmazást kínál Android és iOS rendszerre egyaránt. A mobilalkalmazás push értesítéseket küld árvízfigyelmeztetésekről, ami hasznos a terepi kampányok során.

**Tippek és gyakori problémák.**

- Ez a portál valós idejű megfigyelésre és aktuális viszonyok megjelenítésére van optimalizálva, nem tömeges történeti adatok letöltésére. Történeti idősorokhoz a data.vizugy.hu használandó.
- Nagyobb árvízi események során az oldal nagy forgalmat tapasztalhat. A mobilalkalmazás ezekben az időszakokban gyakran megbízhatóbb.
- A kisvízfolyások riasztórendszere a radari csapadékbecsléseken alapuló villámárvíz-figyelmeztetéseket biztosít a nem mérőállomásos vízgyűjtőkre. Ez különösen értékes a fő előrejelzési hálózat által nem lefedett mellékfolyókra.
- Az egyes állomásokon a riasztási küszöbértékek (I., II., III. fokozat) konkrét vízszinteknek felelnek meg, amelyek a területi vízügyi igazgatóságok operatív beavatkozásait indítják el. Ezek a küszöbértékek az állomás-metaadatokban érhetők el.

---

### 3. portál: odp.met.hu — OMSZ Open Data Portál (Országos Meteorológiai Szolgálat)

**Tartalma.** Az OMSZ Open Data Portál hozzáférést biztosít Magyarország nemzeti meteorológiai szolgálatának (HungaroMet Zrt., korábban OMSZ) megfigyeléseihez és termékeihez. Tartalmaz állomási megfigyeléseket (hőmérséklet, csapadék, légnedvesség, szél, sugárzás), rácsos időjárási termékeket, éghajlati összegzéseket, radarképeket és levegőminőségi adatokat. A 136 állomásból álló szinoptikus hálózat 10 perces időközönként szolgáltat adatokat.

**Lépésről lépésre hozzáférési eljárás.**

1. **Navigáljon a portálra.** Nyissa meg a https://odp.met.hu/ oldalt böngészőjében. Ha a nyílt adatportál nem elérhető vagy nem tartalmazza a szükséges terméket, a https://www.met.hu/en/eghajlat/ fő éghajlati oldal alternatív belépési pontként szolgál a nagyobb városok éghajlati összegzéseivel.

2. **Böngéssze az elérhető adatkészleteket.** A portál kategóriákba rendezi az adatokat: aktuális megfigyelések, történeti éghajlati adatok, időjárási figyelmeztetések és származtatott termékek. Keresse a történeti vagy éghajlati adatok részt a kutatásra alkalmas adatkészletekhez.

3. **Válasszon állomásadatokat.** Az állomási megfigyelésekhez név, helyszín vagy paraméter alapján kereshet. Az öt fő, hosszú adatsorral rendelkező állomás Budapest, Debrecen, Pécs, Szeged és Szombathely, amelyek éghajlati sorai 1901-ig nyúlnak vissza. Sok további állomás az 1950-es évektől rendelkezik adatsorral.

4. **Válasszon paramétereket és időszakokat.** Az elérhető paraméterek közé tartozik a napi maximum és minimum hőmérséklet, a napi csapadékösszeg, a relatív légnedvesség, az átlagos szélsebesség, a széllökések, a napsütéses órák száma és a globális sugárzás. A szinoptikus állomások 10 perces adataihoz szükség lehet az OMSZ közvetlen megkeresésére az adatkérő űrlapon keresztül.

5. **Töltse le az adatokat.** A portál CSV vagy Excel formátumban biztosít adatokat. Az éghajlati összegzések (havi átlagok, éves összegek, szélsőértékek) PDF-jelentésekként is elérhetők.

6. **Rácsos termékek elérése.** Az OMSZ rácsos csapadék- és hőmérsékletelemzéseket készít Magyarországra az állomáshálózat felhasználásával. Ezek a termékek a portálon vagy közvetlen kéréssel érhetők el.

**Tippek és gyakori problémák.**

- Az ingyenes és díjköteles termékek közötti határvonal az idők során változott. 2024–2025-re a legtöbb történeti éghajlati adat Magyarország nyílt adatokra vonatkozó irányelvei szerint térítésmentesen elérhető, de egyes speciális termékek (nagy felbontású rácsos elemzések, óra alatti adatok) továbbra is hivatalos adatkérést igényelhetnek.
- A Magyarországot lefedő, hézagmentes csapadék- és hőmérséklet-adatokhoz az E-OBS adatkészlet (a Copernicus éghajlati szolgáltatásoktól elérhető) és a CARPATCLIM kiváló alternatívák, amelyek az OMSZ állomásadatait a szomszédos országok megfigyeléseivel kombinálják.
- Az agrometeorológiai termékek (tenyészidőszak-adatok, fagydátumok, hőösszegek) minden évben márciustól szeptemberig érhetők el, és hasznosak lehetnek a mezőgazdasági vízigény becslésénél.
- A radarhálózat hozzávetőleg 5 percenkénti csapadékintenzitás-kompozit képeket biztosít. Ezek képként elérhetők a fő met.hu oldalon, és kvantitatív formátumban az adatportálon vagy kérésre.

---

### 4. portál: map.mbfsz.gov.hu — Magyar Bányászati és Földtani Szolgálat térképnézegető

**Tartalma.** Az MBFSZ (Szabályozott Tevékenységek Felügyeleti Hatósága, korábban MFGI) biztosítja Magyarország hivatalos földtani térképadatait. Az interaktív térképnézegető hozzáférést nyújt a felszíni földtani térképekhez, a hidrogeológiai térképekhez, a geotermikus adatokhoz, az ásványi nyersanyag-térképekhez és a fúrásnaplókhoz. A felszín alatti víz modellezéshez (18–21. fejezet) ez nélkülözhetetlen forrás a felszín alatti kőzettan és vízadó réteg-geometria megértéséhez.

**Lépésről lépésre hozzáférési eljárás.**

1. **Navigáljon a portálra.** Nyissa meg a https://map.mbfsz.gov.hu/ oldalt egy modern böngészőben. A felület webalapú térinformatikai nézegető (jellemzően OpenLayers vagy Leaflet alapú). Hagyja, hogy teljesen betöltődjön.

2. **Fedezze fel az elérhető térképrétegeket.** A rétegek panel (jellemzően a bal oldalon vagy egy rétegek gombbal elérhető) felsorolja az elérhető tematikus térképeket. A víztudományi szakemberek számára kulcsfontosságú rétegek:
   - **Felszíni földtan** (felszíni földtani térkép): a felszíni geológiai képződményeket mutatja, jellemzően 1:100 000 méretarányban.
   - **Hidrogeológia** (vízföldtani térkép): vízadó réteg-rendszerek, kúthozam-zónák és felszín alatti víz sérülékenységi térképek.
   - **Fúrásadatbázis** (fúrásadatbázis): a Magyarország területén lefúrt fúrások helyszínei és naplói.
   - **Geotermikus adatok**: hőmérsékletgradiensek és termálvíz-források.

3. **Navigáljon a térképen.** Használja a szokásos mozgatási és nagyítási vezérlőelemeket. A térkép egész Magyarországot lefedi. Kereshet helyszínt név vagy koordináta (EOV vagy WGS84) alapján.

4. **Kérdezze le az elemeket.** Kattintson a térképre a földtani egységek azonosításához, fúrásnaplók megtekintéséhez vagy attribútumok lekérdezéséhez. Az azonosító eszköz (gyakran „i" ikon) a kattintott helyen a látható rétegek attribútumadatait adja vissza.

5. **Adatletöltés.** Egyes rétegek shapefile vagy GeoTIFF formátumban letölthetők. Mások csak WMS (csak megtekintés) szolgáltatásként érhetők el. Tömeges letöltésekhez vagy speciális adatkérésekhez lépjen kapcsolatba közvetlenül az MBFSZ-szel. A WMS szolgáltatás URL-jei hozzáadhatók a QGIS-hez vagy az ArcGIS-hez a saját projektadatokkal történő integráláshoz.

6. **Fúrásnaplók elérése.** A fúrásadatbázis kőzettani leírásokat, szerkezeti részleteket és egyes esetekben vízszintméréseket tartalmaz. Kattintson egy fúrás helyszínére a napló megtekintéséhez. Ez az információ kritikus a 3D földtani modellek építéséhez (18. fejezet) és a felszín alatti víz áramlási modellek paraméterezéséhez (21. fejezet).

**Tippek és gyakori problémák.**

- A felület elsősorban magyar nyelvű, és a földtani terminológia speciális lehet. Tartson kéznél magyar geológiai szótárat, vagy használjon böngészőfordítást. Kulcsfogalmak: homok = sand, kavics = gravel, agyag = clay, mész = limestone, dolomit = dolomite, víz = water.
- A WMS szolgáltatások csúcsidőben lassúak lehetnek. Ha a nézegető nem reagál, próbálja meg a WMS rétegeket közvetlenül a QGIS-ben elérni, amely lehetővé teszi a renderelés vezérlését és a csempék helyi gyorsítótárazását.
- A határon átnyúló földtani kontinuitáshoz (fontos a Duna-medencéhez) az EGDI (European Geological Data Infrastructure, https://www.europe-geology.eu/) harmonizált földtani térképeket biztosít, amelyek Magyarországot a tágabb európai kontextusban tartalmazzák.
- A fúrásnaplók minősége és részletessége nagymértékben változik attól függően, mikor és miért fúrták a fúrást. Az ipari fúrások (bányászat, geotermia) jellemzően részletesebb naplókkal rendelkeznek, mint a mezőgazdasági vagy megfigyelőkutak.

---

### 5. portál: data.ksh.hu — KSH Open Data API (Központi Statisztikai Hivatal)

**Tartalma.** A KSH biztosítja Magyarország hivatalos demográfiai, gazdasági és társadalmi statisztikáit. A víztudományi szakemberek számára a legrelevánsabb adatkészletek a településenkénti népességszámok és -sűrűség (árvízi kitettségelemzéshez, 17. fejezet), a földhasználati statisztikák és a mezőgazdasági adatok (öntözés, vízhasználat). A 2022. évi népszámlálási adatok a legfrissebb átfogó népesség-adatkészlet.

**Lépésről lépésre hozzáférési eljárás.**

1. **Navigáljon a portálra.** A legfelhasználóbarátabb élményhez kezdje a https://www.ksh.hu/?lang=en oldalon (a KSH fő weboldala angol felülettel). Programozott hozzáféréshez használja a https://data.ksh.hu/ címen elérhető API-t. A 2022. évi népszámlálási adatokhoz konkrétan a https://nepszamlalas2022.ksh.hu/en/database/ oldalra navigáljon.

2. **Böngéssze a STADAT-táblázatokat.** A KSH fő weboldala STADAT (Statisztikai Adatok) összefoglaló táblázatokat biztosít téma szerinti rendezésben. Az árvízkockázat-becslés szempontjából releváns demográfiai adatokhoz navigáljon a „Népesség, népmozgalom" vagy a „Területi statisztikák" részhez.

3. **2022. évi népszámlálási adatok elérése.** A 2022. évi népszámlálási portál tematikus térképeket és letölthető táblázatokat biztosít több földrajzi szinten: régió, megye, járás és település. A népességszámok, a korösszetétel, a lakásadatok és a foglalkoztatási adatok mind elérhetők.

4. **API használata (data.ksh.hu).** Automatizált adatlekérdezéshez:
   - Az API dokumentációja a portálon érhető el.
   - A végpontok JSON-formátumú válaszokat adnak.
   - Specifikus mutatókat kérdezhet le földrajzi egység és időszak szerint.
   - Ez a leghatékonyabb megközelítés a népesség-adatok térinformatikai munkafolyamatokba történő integrálásához, mivel szkriptelheti az adatlekérdezést és közvetlenül a közigazgatási határ-shapefile-okhoz csatlakoztathatja.

5. **Közigazgatási határok letöltése.** A KSH-statisztikák térképezéséhez szüksége van a megfelelő közigazgatási határ-shapefile-okra. Ezek a következő helyekről érhetők el:
   - Eurostat GISCO (https://ec.europa.eu/eurostat/web/gisco/geodata) a NUTS régiókhoz és a LAU-khoz (helyi közigazgatási egységek).
   - A KSH maga is biztosít néha határ-fájlokat a népszámlálási adatokkal.
   - A GADM (https://gadm.org/) Magyarország közigazgatási határait minden szinten biztosítja.

6. **Statisztikák és geometria összekapcsolása.** A szokásos munkafolyamat: (a) töltse le a statisztikai táblázatot földrajzi azonosítóval (településkód vagy LAU-kód), (b) töltse le a megfelelő határ-shapefile-t, (c) végezzen tábla-összekapcsolást a térinformatikai szoftverben a közös azonosító felhasználásával, és (d) készítsen tematikus térképeket a népességsűrűséget, növekedési ütemet vagy más mutatókat árvízveszélyzónákkal átfedve.

**Tippek és gyakori problémák.**

- A magyar településkódok a közigazgatási átszervezések miatt az idők során változtak. Győződjön meg arról, hogy a határ-fájl és a statisztikai táblázat ugyanazt a kódrendszer-évjáratot használja. A 2022. évi népszámlálás a legújabb közigazgatási struktúrát használja.
- A KSH weboldal lassú lehet nagy egyedi táblázatok generálásakor. Az előre elkészített STADAT táblázatok sokkal gyorsabban töltődnek le, mint az egyedi lekérdezések.
- Az R programozási környezethez a `giscoR` csomag közvetlen hozzáférést biztosít az Eurostat/GISCO közigazgatási határaihoz, az `eurostat` csomag pedig Eurostat-statisztikákat kérdez le — együtt egyszerűsített munkafolyamatot kínálnak a magyar demográfiai adatok EU-kontextusban történő térképezéséhez.
- A települési szintű népesség-adatok az árvízveszélytérképekkel összekapcsolhatók az árvízveszélyes területeken élő lakosság számának becsléséhez — ez az EU Árvízi irányelv szabványos követelménye.

---

## Portálok közötti integrációs munkafolyamat

Egy tipikus magyarországi vízgyűjtő-tanulmányhoz egyszerre több portál adataira lesz szükség. Az ajánlott munkafolyamat:

1. **Határozza meg a vizsgálati területet** a KSH/GISCO/GADM közigazgatási határaival vagy a DEM-ből lehatárolt vízgyűjtő-határokkal.

2. **Szerezze be a domborzati adatokat.** Kezdje a Copernicus DEM GLO-30-cal (ingyenes 30 m-es lefedettség). Ha nagyobb felbontás szükséges és a költségvetés lehetővé teszi, rendelje meg a DDM-5-öt a Lechnertől.

3. **Szerezze be az időjárási meghajtó adatokat.** Töltse le az ERA5-Land-et (9 km) a Copernicus Climate Data Store-ból modellmeghajtáshoz. Egészítse ki az OMSZ állomásadataival az odp.met.hu-ról validációhoz és helyi kalibrációhoz.

4. **Gyűjtse össze a vízhozam-adatokat** a data.vizugy.hu-ról a vízgyűjtőn belüli és az alatta lévő kalibrációs mérőállomásokhoz. Ellenőrizze a GRDC-t a szomszédos országokban lévő felsőbb állomásokra, ha a vízgyűjtő határon átnyúló.

5. **Szerezze be a felszínborítási adatokat** a CORINE Land Cover-ből (páneurópai, 100 m) vagy az ESA WorldCover-ből (globális, 10 m).

6. **Szerezze be a talajtulajdonságokat** az ESDAC-tól vagy a SoilGrids-ből a hidraulikai paraméterekhez.

7. **Kérdezze le a földtani információkat** a map.mbfsz.gov.hu-ról, ha a tanulmány felszín alatti vizet érint.

8. **Töltse le a népesség-adatokat** a data.ksh.hu-ról, ha a tanulmány árvízkockázatot vagy kitettségelemzést érint.

9. **Harmonizálja a koordináta-rendszereket.** Alakítson minden adatkészletet közös vonatkoztatási rendszerbe. Magyarországi helyi munkához az EOV (EPSG:23700) a szabványos. Páneurópai elemzéshez az ETRS89/LAEA (EPSG:3035) az előnyös. Használja a PROJ-t vagy a térinformatikai szoftver vetületi transzformációs eszközeit, és ellenőrizze a HD72–ETRS89 transzformációt az EPSG:1449-cel.

---

## Adatlicencelési összefoglaló

Az adatlicencelés megértése elengedhetetlen mind a tudományos publikációkhoz, mind az operatív alkalmazásokhoz. Az alábbi táblázat összefoglalja a függelékben felsorolt fő adatforrások licencfeltételeit.

| Licenctípus | Adatkészletek | Főbb feltételek |
|-------------|---------------|-----------------|
| Teljesen nyílt (korlátozás nélkül) | SRTM, Copernicus GLO-30/GLO-90, ERA5, E-OBS, CORINE, CLMS, ESA WorldCover, WISE, JRC Flood Hazard, data.vizugy.hu (2024 óta), HYDROINFO, CHIRPS, GPM/IMERG, CRU TS, GloFAS, EFAS archívumok, Dynamic World, WorldPop | Bármely felhasználásra ingyenes; forrásmegjelölés jellemzően szükséges |
| Ingyenes regisztrációval | NASA Earthdata termékek, Copernicus Data Space, Google Earth Engine (akadémiai), CDS, SoilGrids, GRDC, LandScan, ALOS AW3D30, APHRODITE | Ingyenes fiók szükséges; egyes felhasználási feltételek korlátozhatják a kereskedelmi alkalmazást |
| Ingyenes adatkéréssel | ESDAC (egyes rétegek), OMSZ részletes állomásadatok, MBFSZ speciális termékek | Kapcsolatfelvétel az adatszolgáltatóval; indoklás és adathasználati megállapodás szükséges lehet |
| Korlátozott / Intézményi | Copernicus EEA-10 DEM, EFAS valós idejű adatok, OVF árvízi geoportál, DDM-5, Magyar LiDAR-adatok | Minősített intézmény, partnerstátusz vagy megvásárlás szükséges |
| CC-BY-NC | MERIT DEM, egyes ISRIC termékek | Nem kereskedelmi felhasználásra ingyenes; forrásmegjelölés szükséges; kereskedelmi felhasználás tilos |

---

## Gyakran előforduló fájlformátumok

A térbeli adatelemzésben újonc olvasók számos fájlformátummal találkoznak ezeken a portálokon. Ez az áttekintés a leggyakoribbakat fedi le.

| Formátum | Kiterjesztés | Leírás | Gyakori források |
|----------|-------------|--------|-----------------|
| GeoTIFF | .tif, .tiff | Georeferált raszterkép; a rácsos adatok univerzális csereformátuma | DEM-ek, felszínborítás, műholdképek, talajtérképek |
| NetCDF | .nc | Önleíró tömbformátum többdimenziós adatokhoz; éghajlati és időjárási adatok szabványa | ERA5, E-OBS, CARPATCLIM, CHIRPS, CRU TS |
| GRIB / GRIB2 | .grib, .grib2 | WMO szabvány időjárási modellkimenetekhez; kompakt bináris formátum | ERA5 (natív), ECMWF előrejelzések, NWP modellkimenetek |
| Shapefile | .shp (+.shx, .dbf, .prj) | Korábbi vektoros formátum; korlátai (2 GB max, 10 karakteres mezőnevek) ellenére széles körben használt | Közigazgatási határok, vízfolyáshálózatok, CORINE CLC |
| GeoPackage | .gpkg | Modern, SQLite-alapú vektor/raszter konténer; egyetlen fájl, nincs méretkorlát | Egyre inkább felváltja a shapefile-okat; GADM, egyes EU termékek |
| GeoJSON | .geojson | JSON-alapú vektoros formátum; ember által olvasható, webbarát | Eurostat GISCO, web API-k |
| CSV | .csv | Egyszerű szöveges táblázatos adat; univerzálisan támogatott | Állomási idősorok (data.vizugy.hu, GRDC, KSH) |
| WaterML2 | .xml | OGC szabvány hidrológiai idősoradatokhoz | GRDC |
| SAFE | .SAFE (könyvtár) | Sentinel műholdtermék-formátum (GeoTIFF-et, XML-metaadatokat tartalmaz) | Copernicus Data Space (Sentinel-1, -2, -3) |
| HGT | .hgt | Nyers bináris domborzati csempék az SRTM-hez | SRTM letöltések |
| VRT | .vrt | GDAL virtuális raszter; XML-mutató távoli csempékre, streaming hozzáférést tesz lehetővé | SoilGrids WebDAV |

---

## Regisztrációs ellenőrzőlista

Projekt megkezdése előtt regisztráljon ezekre az ingyenes fiókokra. Az egyes regisztrációs folyamatok hozzávetőleg 2–5 percet vesznek igénybe. Ha minden fiók kész van a kezdés előtt, elkerülhetők a késedelmek az adatletöltés során.

| Prioritás | Szolgáltatás | Regisztrációs URL | Mit kap |
|-----------|-------------|-------------------|---------|
| 1 | NASA Earthdata | https://urs.earthdata.nasa.gov/users/new | Hozzáférés: SRTM, Landsat, MODIS, GPM, GRACE, ASTER GDEM |
| 2 | Copernicus Data Space | https://dataspace.copernicus.eu/ | Hozzáférés: Sentinel-1/2/3/5P, Copernicus DEM, API-k |
| 3 | Copernicus Climate Data Store | https://cds.climate.copernicus.eu/ | Hozzáférés: ERA5, ERA5-Land, E-OBS, szezonális előrejelzések |
| 4 | Google Earth Engine | https://earthengine.google.com/ | Felhőszámítás + több petabájtos adatkatalógus |
| 5 | GRDC | https://grdc.bafg.de/ | Globális folyóvízhozam-adatok |
| 6 | ISRIC SoilGrids | https://soilgrids.org/ | Globális talajtulajdonság-térképek (WebDAV/WCS hozzáférés) |
| 7 | Eurostat/GISCO | https://ec.europa.eu/eurostat/web/gisco/geodata | Európai közigazgatási határok és népességi rácsok |

---

## Fejezet–adatforrás keresztreferencia

Ez a fordított index megmutatja, mely adatforrások a leglényegesebbek az egyes fejezetekhez, segítve az olvasókat az elemzés minden szakaszához megfelelő adatok megtalálásában.

| Fejezet | Cím | Elsődleges adatforrások |
|---------|-----|------------------------|
| 1 | Miért fontos a hidroinformatika | (koncepcionális — nincs specifikus adatforrás) |
| 2 | A víz térképezése: papírtól a pixelekig | NHDPlus, data.vizugy.hu, Copernicus Data Space, Landsat, NASA Earthdata |
| 3 | Hol élnek az adatok | Minden portál (áttekintő fejezet); data.vizugy.hu, USGS NWIS, GRDC, WISE, NASA Earthdata |
| 4 | A térinformatika mint vízügyi eszköz | (eszközközpontú — több forrásból származó példaadatokat használ) |
| 5 | A rács: hogyan látják a számítógépek a terepet | 3DEP, DDM-5, Copernicus DEM, SRTM, AW3D30, ASTER GDEM, MERIT DEM, TanDEM-X |
| 6 | Számítás térképekkel | NLCD, CORINE, ESA WorldCover, Dynamic World, MODIS Land Cover, Sentinel-2 |
| 7 | Lejtés, kitettség és a táj alakja | 3DEP, DDM-5, Copernicus DEM |
| 8 | Az eső mérése, ahol esik | OMSZ, ERA5, E-OBS, CARPATCLIM, CHIRPS, GPM/IMERG, CRU TS, APHRODITE, PRISM, Daymet |
| 9 | A digitális táj előkészítése | DEM-ek (mind), CORINE/WorldCover, SSURGO/ESDAC/SoilGrids, HydroSHEDS |
| 10 | Merre folyik a víz? | DEM-ek (mind), HydroSHEDS, NHDPlus, data.vizugy.hu |
| 11 | Vízgyűjtők rajzolása adatokból | DEM-ek (mind), NHDPlus, data.vizugy.hu, HydroBASINS |
| 12 | A munkafolyamat automatizálása | (a 9–11. fejezetek adatait használja; Google Earth Engine felhőfeldolgozáshoz) |
| 13 | A talaj háromdimenziós látása: LiDAR | 3DEP LiDAR, Magyar LiDAR (Lechner), OpenTopography, Copernicus Data Space |
| 14 | Milyen magasan a folyó felett? | FEMA NFHL, OVF árvíztérképek, DEM-ek, LiDAR |
| 15 | Az árvíz útjának térképezése | FEMA, JRC Flood Hazard, EFAS, GloFAS, Copernicus EMS, DEM-ek, felszínborítás, talaj |
| 16 | Árvíz-előrejelzés valós időben | HYDROINFO, EFAS, GloFAS, USGS NWIS, NWS AHPS, data.vizugy.hu, ERA5, GRDC |
| 17 | Ki él az ártéren? | FEMA NFHL, OVF árvíztérképek, KSH, Census, Eurostat/GISCO, WorldPop, LandScan, GADM, DesInventar |
| 18 | A felszín alatti világ: 3D térinformatika | MBFSZ, USGS földtani térképek, OneGeology, EGDI |
| 19 | Kutak, fúrások és vízadó réteg-térképek | data.vizugy.hu (felszín alatti víz), USGS NWIS GW, MBFSZ fúrások, GRACE/G3P |
| 20 | A felszín alatti világ képének felépítése | MBFSZ, data.vizugy.hu, USGS földtani térképek, EGDI, fúrásadatbázisok |
| 21 | A felszín alatti víz áramlásának szimulálása | data.vizugy.hu, USGS NWIS GW, SoilGrids, ESDAC, GRACE/GRACE-FO, WISE WFD GW |
| 22 | Amikor a modellek találkoznak az adatokkal | data.vizugy.hu, USGS NWIS, GRDC, ERA5, GEMStat, WISE WFD |
| 23 | A MI mint a hidrológus segítőtársa | Google Earth Engine, Dynamic World, Copernicus Data Space, ERA5 |
| 24 | Agentikus MI: az autonóm modellező | (az összes korábbi fejezet adatait használja; automatizált adatlekérdezésre helyezi a hangsúlyt) |
| 25 | A vízi intelligencia jövője | (előretekintő — formálódó adatrendszerekre hivatkozik) |

---

*Ez a függelék 2026-03-25-én került összeállításra és ellenőrzésre. Az URL-ek és hozzáférési feltételek idővel változnak. Ha egy URL nem működik, először ellenőrizze a Copernicus Data Space (https://dataspace.copernicus.eu/) és a NASA Earthdata (https://earthdata.nasa.gov/) portálokat, mivel ezek összevont átjáróként szolgálnak az itt felsorolt legtöbb műholdas és éghajlati adatkészlethez. A magyar-specifikus adatokhoz az OVF weboldala (https://www.ovf.hu/) és a Lechner Tudásközpont (https://lechnerkozpont.hu/) tartja karban az adatszolgáltatásaik aktuális linkjeit.*
