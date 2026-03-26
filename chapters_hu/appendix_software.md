\newpage

# C. függelék: Szoftverútmutató

Ez a függelék átfogó referenciát nyújt a *Hidroinformatika helyzete 2026-ban* című könyvben említett minden szoftvereszközről, platformról, könyvtárról és adatszolgáltatásról. Minden bejegyzéshez megadjuk a szoftver típusát, beszerzési helyét, licencmodelljét, a vízkészlet-gazdálkodás szempontjából legfontosabb képességeit és azokat a fejezeteket, amelyekben szerepel. Az útmutató funkcionális kategóriák szerint tagolódik: asztali térinformatikától a felhőplatformokon, a terepanalízis eszközökön, a hidrológiai és felszín alatti víz modellező rendszereken, a programozási környezeteken, az adatkezelésen, a gépi tanulási keretrendszereken és a vizualizációs könyvtárakon át. A függelék Windows telepítési útmutatóval és a kezdők számára ajánlott tanulási útvonallal zárul.

Megjegyzés a verziókhoz: a szoftverek gyorsan fejlődnek. Az itt felsorolt URL-ek és verziószámok 2026 elejének megfelelőek. Amikor egy link nem működik, a szoftver neve plusz a „download" szó bármely keresőmotorban megtalálja az aktuális kiadást.

---

## C.1 Térinformatikai szoftverek

A térinformatikai rendszerek alkotják a könyvben leírt szinte minden munkafolyamat alapplatformját. Akár digitális domborzatmodellt jelenít meg, akár vízgyűjtőt határol le, akár árvíztérképet vet össze népszámlálási adatokkal — a térinformatika adja azt a környezetet, amelyben a térbeli adatokat betöltik, áttekintik, elemzik és térképezik. A 2026-os hidroinformatikai palettán négy platform dominál, mindegyik meghatározott szerepkörben.

### ArcGIS Pro

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás (csak Windows) |
| **URL** | https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview |
| **Licenc** | Kereskedelmi; diákok számára ingyenes az Esri Education Site License programon keresztül; sok egyetem intézményi licenccel rendelkezik |
| **Aktuális verzió** | 3.4 (2026 eleje) |

**Fő képességek a hidroinformatikában.** Az ArcGIS Pro a legszélesebb körben használt kereskedelmi térinformatikai rendszer a vízkészlet-gazdálkodási mérnöki munkában. Teljes környezetet biztosít a vektor- és raszterelemzéshez, a 3D vizualizációhoz, a téradat-feldolgozási automatizáláshoz és a kartográfiai termékelőállításhoz. A Spatial Analyst kiterjesztés tartalmazza a raszter-hidrológiai alapeszközöket — Fill, Flow Direction, Flow Accumulation, Snap Pour Point, Watershed —, amelyek a 9–11. fejezetek gerincét alkotják. A 3D Analyst kiterjesztés támogatja a 18. fejezetben ismertetett felszín alatti vizualizációs munkafolyamatokat. Az ArcGIS Pro szoros integrációja az ArcPy-vel (lásd C.5. rész) természetes választássá teszi a 12. fejezet szkriptelési munkafolyamataihoz, és a ModelBuilder vizuális programozási környezet kódmentes alternatívát kínál a többlépcsős téradat-feldolgozási láncok automatizálásához.

Az ArcGIS Pro közvetlen hozzáférést biztosít az Esri felhőszolgáltatásaihoz az ArcGIS Online-on keresztül is, beleértve a tárolt elem-rétegeket, webtérképeket és a Living Atlas of the World-öt — egy gondozott, hiteles alaptérképekből és referencia-rétegekből álló gyűjteményt. Azoknak a szervezeteknek, amelyek már elköteleződtek az Esri ökoszisztémája mellett az ArcGIS Pro a legegyszerűbb megoldás.

**Korlátok.** A kereskedelmi licencköltség akadályt jelenthet egyéni kutatók és alacsonyabb jövedelmű országok szervezetei számára. Az ArcGIS Pro csak Windowson fut, ami kizárja a Linux-alapú nagy teljesítményű számítási környezeteket. Egyes haladó kiterjesztések (Spatial Analyst, 3D Analyst, Geostatistical Analyst) az alapszoftveren felül külön licencet igényelnek.

**Fejezetek, amelyekben szerepel:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17, 18, 19, 20, 21, 25.

---

### QGIS

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás (Windows, macOS, Linux) |
| **URL** | https://qgis.org/download/ |
| **Licenc** | Ingyenes és nyílt forráskódú (GNU GPL v2) |
| **Aktuális verzió** | 3.40 LTR (2026 eleje) |

**Fő képességek a hidroinformatikában.** A QGIS a vezető nyílt forráskódú asztali térinformatikai rendszer és az ArcGIS Pro elsődleges ingyenes alternatívája. Minden elterjedt formátumban támogatja a vektor- és raszteradatokat (Shapefile, GeoPackage, GeoTIFF, NetCDF és még tucatnyi másikat a GDAL/OGR könyvtáron keresztül). A hidrológia szempontjából a legfontosabb képességek a bővítményökoszisztémán keresztül érhetők el: a QGIS Processing keretrendszer integrálja a GRASS GIS, SAGA GIS és GDAL eszközöket egységes felületbe, lehetővé téve a mélypontkitöltés, a folyásirány-számítás, az vízgyülekezés és a vízgyűjtő-lehatárolás végrehajtását a QGIS elhagyása nélkül. A WhiteboxTools bővítmény (lásd C.2. rész) a TauDEM-mel egyenértékű terep-hidrológiai eszközöket biztosít közvetlenül a QGIS-en belül.

A QGIS támogatja a Python-szkriptelést a PyQGIS-en keresztül (lásd C.5. rész), lehetővé téve bármely grafikus felületen végrehajtható munkafolyamat automatizálását. A nyomtatási elrendezés rendszer publikációs minőségű térképeket állít elő, a 3D térképnézet pedig támogatja a terepvizualizációt az V. rész felszín alatti munkafolyamataihoz. A QGIS platformfüggetlen jellege miatt sok esetben ez a természetes választás a Linux-alapú számítási környezetekhez és azoknak a szervezeteknek, amelyek nem engedhetik meg a kereskedelmi térinformatikai licenceket.

**Korlátok.** Az ArcGIS Pro-ban elérhető egyes speciális hidrológiai eszközöknek (különösen az Arc Hydro eszközkészletnek) nincs közvetlen QGIS megfelelőjük, bár nyílt forráskódú alternatívák a legtöbb egyedi művelethez léteznek. A nagyon nagy rasztereken (milliárd cellás) a teljesítmény elmaradhat az ArcGIS Pro-tól, bár ez a különbség a legutóbbi verziókban jelentősen csökkent.

**Fejezetek, amelyekben szerepel:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 17, 18, 19, 20, 21, 25.

---

### Google Earth Engine (GEE)

| Jellemző | Részletek |
|---|---|
| **Típus** | Felhőplatform (böngészőalapú) |
| **URL** | https://earthengine.google.com/ |
| **Licenc** | Kutatási, oktatási és nonprofit felhasználásra ingyenes; kereskedelmi felhasználáshoz fizetős előfizetés a Google Cloud-on keresztül |
| **Hozzáférés** | Google fiók és projekt-regisztráció szükséges |

**Fő képességek a hidroinformatikában.** A Google Earth Engine bolygóléptékű térbeli elemzési platform, amely petabájtnyi műholdas képet és térbeli adatkészletet tárol a Google felhőinfrastruktúráján. A hidroinformatika számára a legfontosabb adatállományok közé tartozik a teljes Landsat és Sentinel-2 archívum, globális DEM-ek (SRTM, ALOS, Copernicus DEM), csapadékadatkészletek (CHIRPS, GPM, ERA5), felszínborítási termékek (Dynamic World, ESA WorldCover) és talajnedvesség-megfigyelések (SMAP). A felhasználók JavaScript-ben (a Code Editor-on keresztül) vagy Python-ban (az Earth Engine Python API-n keresztül) írnak elemzési szkripteket, és minden számítás a Google szerverein fut — így a felhasználó már egy laptoppal és böngészővel is terabájtnyi képet dolgozhat fel, ami bármely asztali gépet túlterhelne.

**Korlátok.** A GEE internetkapcsolatot igényel és a Google infrastruktúrájától függ. A nagy eredmények exportálása lassú lehet. A JavaScript-központú Code Editornak van tanulási görbéje a Python-hoz szokott felhasználók számára. Egyes haladó hidrológiai műveletek (D-végtelen folyásirány, HAND-számítás) natívan nem érhetők el, és egyedi megvalósítást igényelnek.

**Fejezetek, amelyekben szerepel:** 1, 3, 4, 6, 7, 9, 11, 12, 23, 25.

---

### Microsoft Planetary Computer

| Jellemző | Részletek |
|---|---|
| **Típus** | Felhőplatform (böngésző- és API-alapú) |
| **URL** | https://planetarycomputer.microsoft.com/ |
| **Licenc** | Kutatási és oktatási felhasználásra ingyenes |
| **Hozzáférés** | Microsoft fiók szükséges; számítási kapacitás tárolt JupyterHub-on |

**Fő képességek a hidroinformatikában.** A Microsoft Planetary Computer környezeti adatkészletek nagy katalógusát tárolja STAC (SpatioTemporal Asset Catalog) API-n keresztül, beleértve a Sentinel-2-t, a Landsat-ot, a Copernicus DEM-et, a NAIP légifelvételeket és számos éghajlati és felszínborítási terméket. A Google Earth Engine-nel ellentétben, amely egyedi API-t és szerveroldali számítást alkalmaz, a Planetary Computer szabványos Python-környezetet biztosít (JupyterHub xarray-jel, rasterio-val, geopandas-szal és dask-kal), amely Azure infrastruktúrán fut. Ez különösen előnyös azoknak a felhasználóknak, akik inkább szabványos Pythonban dolgoznának, mint platformspecifikus API-t tanulnának.

**Korlátok.** A számítási környezet a GEE-nél korlátozottabb a nagyon nagyszabású elemzésekhez. A platform fiatalabb a GEE-nél és kisebb felhasználói közösséggel rendelkezik, ami kevesebb oktatóanyagot és kódpéldát jelent. A GEE-n elérhető egyes adatkészletek még nincsenek tükrözve a Planetary Computeren.

**Fejezetek, amelyekben szerepel:** 3, 4, 6, 7, 9, 11, 12, 25.

---

## C.2 Terepanalízis

A terepanalízis — a folyásirányok számítása, a hozzájáruló területek felhalmozása, a vízgyűjtők lehatárolása, a vízfolyáshálózatok kinyerése — a DEM-alapú hidrológia számítási motorja. A következő eszközök biztosítják a könyv III. részét és a IV. rész HAND- és árvízi elöntési munkafolyamatait meghajtó algoritmusokat.

### TauDEM (Terrain Analysis Using Digital Elevation Models)

| Jellemző | Részletek |
|---|---|
| **Típus** | Parancssori eszközök és ArcGIS Pro eszközkészlet |
| **URL** | https://hydrology.usu.edu/taudem/taudem5/ |
| **Licenc** | Ingyenes és nyílt forráskódú (MIT License) |
| **Fejlesztő** | David Tarboton, Utah State University |

**Fő képességek a hidroinformatikában.** A TauDEM a kutatási szintű terepanalízis arany standardja a hidrológiában. David Tarboton — a digitális terephidrológia egyik úttörője — által fejlesztett TauDEM megvalósítja a D8 és a D-végtelen (Dinf) folyásirány-algoritmusokat, valamint a származtatott termékek teljes készletét: összegyülekezés, vízfolyáshálózat-kinyerés, vízgyűjtő-lehatárolás, vízfolyásrend-számítás, vízfolyástól való távolság és a HAND-index mögötti alapalgoritmusok. A TauDEM fő technikai előnye az MPI (Message Passing Interface) párhuzamos számítás, amely lehetővé teszi nagyon nagy DEM-ek feldolgozását több processzormagra vagy akár fürtben több gépre elosztva.

**Windows telepítés.** A TauDEM telepítése előtt a Microsoft MPI-t (MS-MPI) kell telepíteni. Töltse le az MS-MPI-t a Microsoft webhelyéről, majd töltse le a TauDEM Windows telepítőt a projekt oldaláról. A telepítő a végrehajtható fájlokat a `C:\Program Files\TauDEM\TauDEM5Exe` mappába helyezi és regisztrálja az ArcGIS eszközkészletet. A telepítés után adja hozzá a TauDEM végrehajtható fájlok könyvtárát a rendszer PATH környezeti változójához a parancssori használat engedélyezéséhez bármely könyvtárból.

**Fejezetek, amelyekben szerepel:** 1, 7, 9, 10, 11, 12, 13, 14, 25.

---

### WhiteboxTools

| Jellemző | Részletek |
|---|---|
| **Típus** | Parancssori eszközök QGIS és Python felületekkel |
| **URL** | https://www.whiteboxgeo.com/download-whiteboxtools/ |
| **Licenc** | Ingyenes nyílt forráskódú kiadás (MIT License); WhiteboxTools Pro (bővített funkciók) kereskedelmi |
| **Fejlesztő** | John Lindsay, University of Guelph |

**Fő képességek a hidroinformatikában.** A WhiteboxTools több mint 550 térbeli elemzési eszközt biztosít Rust nyelven írva, ami az egyik leggyorsabb terepanalízis csomaggá teszi. A hidrológia számára mélypontkitöltést (breach depressions és fill), folyásirány-számítást (D8, Dinf, FD8, MDinf), összegyülekezést, vízfolyáshálózat-kinyerést, vízgyűjtő-lehatárolást és HAND-számítást kínál. A breach depressions algoritmus különösen figyelemre méltó — a mélypontok feltöltése helyett (ami nagy lapos területeket hozhat létre) csatornákat vág az akadályokon, hidrológiailag valósághűbb folyásutakat eredményezve.

**Fejezetek, amelyekben szerepel:** 4, 9, 10, 12, 14, 25.

---

### GRASS GIS

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás és parancssori eszközök (Windows, macOS, Linux) |
| **URL** | https://grass.osgeo.org/ |
| **Licenc** | Ingyenes és nyílt forráskódú (GNU GPL v2) |
| **Aktuális verzió** | 8.4 (2026 eleje) |

**Fő képességek a hidroinformatikában.** A GRASS GIS az egyik legrégebbi és legteljesítményesebb nyílt forráskódú térinformatikai platform, különösen erős raszter-elemzési motorral. Hidrológiai moduljai közé tartozik az `r.watershed` (memóriahatékony vízgyűjtő-lehatárolási algoritmus, amely nagyon nagy DEM-eket is képes feldolgozni), az `r.stream.*` (vízfolyáshálózat-kinyerés és -elemzés), az `r.drain` (folyásút-nyomkövetés) és az `r.terraflow` (masszív terepanalízis). A GRASS átfogó raszter-térképi algebrát biztosít az `r.mapcalc`-on keresztül, interpolációt a `v.surf.rst`-vel (regularizált spline feszítéssel) és terepanalízist az `r.slope.aspect`-tel.

**Fejezetek, amelyekben szerepel:** 4, 5, 6, 8, 9, 10, 12, 13, 14, 18, 25.

---

### Arc Hydro

| Jellemző | Részletek |
|---|---|
| **Típus** | ArcGIS Pro eszközkészlet és geoadatbázis-séma |
| **URL** | https://www.esri.com/en-us/industries/water-resources/arc-hydro |
| **Licenc** | Ingyenesen letölthető; ArcGIS Pro licenc szükséges |
| **Fejlesztő** | Esri, eredetileg David Maidmenttel közösen fejlesztve a UT Austin-on |

**Fő képességek a hidroinformatikában.** Az Arc Hydro nem csupán eszközkészlet — adatmodell és filozófia a vízkészlet-gazdálkodási információk térinformatikai szervezéséhez. Az Arc Hydro adatmodell szabványosított geoadatbázis-sémát határoz meg lefolyási hálózatok, vízgyűjtők, megfigyelőpontok, idősorok és szelvények tárolásához. Az Arc Hydro Tools egyszerűsített munkafolyamatot biztosít a DEM-alapú hidrológiához: terep-előfeldolgozás, folyásirány, összegyülekezés, vízfolyás-meghatározás, vízfolyás-szegmentálás, vízgyűjtő-lehatárolás, lefolyási vonal feldolgozás és szomszédos vízgyűjtők létrehozása.

Az Arc Hydro Groundwater (AHGW) kiterjesztés, amelyet a könyv V. részében tárgyalunk részletesen, a felszíni víz adatmodellt háromdimenziósra bővíti, fúrás-vizualizációs, szelvényszerkesztő, vízadó réteg-térfogatábrázoló és MODFLOW-integrációs eszközöket biztosítva.

**Fejezetek, amelyekben szerepel:** 1, 4, 6, 9, 11, 12, 18, 19, 20, 21, 25.

---

## C.3 Hidrológiai és hidraulikai modellezés

Az ebben a részben felsorolt modellek alakítják át a térbeli adatokat — terep, felszínborítás, talaj, csapadék — a vízmozgás előrejelzéseivé: mennyi lefolyást generál egy vihar, hol áraszt el egy folyó, hogyan reagál a felszín alatti víz a szivattyúzásra.

### HEC-HMS (Hydrologic Engineering Center — Hydrologic Modeling System)

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás (Windows; macOS/Linux-on kompatibilitási rétegekkel futtatható) |
| **URL** | https://www.hec.usace.army.mil/software/hec-hms/ |
| **Licenc** | Ingyenes (közkincs, az Egyesült Államok Hadseregének Mérnöki Kara fejlesztette) |
| **Aktuális verzió** | 4.12 (2026 eleje) |

**Fő képességek a hidroinformatikában.** A HEC-HMS a legszélesebb körben használt csapadék-lefolyás modell az Egyesült Államokban, és világszerte széles körben alkalmazzák. A Windows telepítése egyszerű és nem igényel rendszergazdai jogosultságot.

**Fejezetek, amelyekben szerepel:** 1, 4, 7, 8, 13, 14, 15, 22, 24, 25.

---

### HEC-RAS (Hydrologic Engineering Center — River Analysis System)

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás (Windows) |
| **URL** | https://www.hec.usace.army.mil/software/hec-ras/ |
| **Licenc** | Ingyenes (közkincs) |
| **Aktuális verzió** | 6.6 (2026 eleje) |

**Fő képességek a hidroinformatikában.** A HEC-RAS a folyóárvíz-elemzés szabványos hidraulikai modellező eszköze. Egydimenziós állandó és nem állandósult áramlásszámítást, kétdimenziós nem állandósult áramlásmodellezést, hordaléktranszportot és vízminőségi elemzést hajt végre.

**Fejezetek, amelyekben szerepel:** 1, 4, 13, 14, 15, 22, 23, 25.

---

### SWAT (Soil and Water Assessment Tool)

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás térinformatikai felületekkel (ArcSWAT az ArcGIS-hez, QSWAT a QGIS-hez) |
| **URL** | https://swat.tamu.edu/ |
| **Licenc** | Ingyenes (közkincs) |
| **Fejlesztő** | USDA Agricultural Research Service, Texas A&M University |

**Fő képességek a hidroinformatikában.** A SWAT félig elosztott, folytonos idejű vízgyűjtőmodell, amelyet a földgazdálkodási gyakorlatok víz-, üledék- és mezőgazdasági vegyszer-hozamra gyakorolt hatásának előrejelzésére terveztek. A szakirodalomban talán a legszélesebb körben tárgyalt vízgyűjtőmodell.

**Fejezetek, amelyekben szerepel:** 1, 4, 22, 24.

---

### MODFLOW

| Jellemző | Részletek |
|---|---|
| **Típus** | Parancssori program különféle grafikus felületekkel |
| **URL** | https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model |
| **Licenc** | Ingyenes (közkincs, a USGS fejlesztette) |
| **Aktuális verzió** | MODFLOW 6.5 (2026 eleje) |

**Fő képességek a hidroinformatikában.** A MODFLOW a világ legszélesebb körben használt felszín alatti víz áramlási modellje. A háromdimenziós felszín alatti víz áramlási egyenletet oldja meg véges differenciák módszerével strukturált vagy nem strukturált rácson. A Python-felülete, a FloPy (lásd C.5. rész) átalakította a felszín alatti víz modellezési gyakorlatot.

**Fejezetek, amelyekben szerepel:** 1, 4, 18, 20, 21, 22, 23, 24, 25.

---

### FEFLOW

| Jellemző | Részletek |
|---|---|
| **Típus** | Asztali alkalmazás (Windows, Linux) |
| **URL** | https://www.mikepoweredbydhi.com/products/feflow |
| **Licenc** | Kereskedelmi; akadémiai licencek csökkentett áron |
| **Fejlesztő** | DHI (Danish Hydraulic Institute) |

**Fő képességek a hidroinformatikában.** A FEFLOW végeselem-módszerrel oldja meg a felszín alatti víz áramlási és szennyezőanyag-transzport egyenleteit. Különösen népszerű Európában, és az összetett 3D geológiai szerkezetek részletes ábrázolását igénylő projekteknél.

**Fejezetek, amelyekben szerepel:** 18, 20, 21, 25.

---

### Noah-MP, LISFLOOD

A **Noah-MP** az amerikai Nemzeti Vízmodell szívében lévő felszíni modell (16., 22. fejezet). A **LISFLOOD** az EFAS és a GloFAS mögötti elosztott hidrológiai modell (15., 16., 22. fejezet). Mindkettő ingyenes és nyílt forráskódú.

---

## C.4 Operatív előrejelző rendszerek

Ezek nem helyben telepítendő szoftvercsomagok, hanem a könyvben leírt adatokat fogyasztó és előállító operatív rendszerek.

### National Water Model (NWM)

Az Egyesült Államok operatív hidrológiai előrejelző rendszere, amely 2,7 millió vízfolyásszakaszra készít vízhozam-előrejelzéseket. A NOAA szuperszámítógépein fut; kimenetei NetCDF formátumban hozzáférhetők.

### EFAS / GloFAS

Az európai és globális árvíz-figyelmeztető rendszerek, amelyeket a Copernicus Veszélyhelyzet-kezelési Szolgálat üzemeltet. A LISFLOOD modellre épülnek, és valószínűségi árvíz-előrejelzéseket készítenek ensemble időjárás-előrejelzések alapján.

---

## C.5 Programozási nyelvek és könyvtárak

A programozás a hidroinformatika elengedhetetlen készségévé vált. A menüvezérelt térinformatikáról a szkriptelt, reprodukálható munkafolyamatokra való áttérés a 2026-os gyakorlat egyik meghatározó trendje, és a Python messzemenően a választott nyelv.

### Python

| Jellemző | Részletek |
|---|---|
| **Típus** | Általános célú programozási nyelv |
| **URL** | https://www.python.org/ vagy Anaconda/Miniconda-n keresztül (https://docs.conda.io/) |
| **Licenc** | Ingyenes és nyílt forráskódú (PSF License) |
| **Aktuális verzió** | 3.12 (2026 eleje) |

**Fő képességek a hidroinformatikában.** A Python a modern hidroinformatika közös nyelve. Összekapcsolja a munkafolyamat minden elemét: térinformatikai műveletek (ArcPy és PyQGIS), raszterfeldolgozás (GDAL/OGR és rasterio), adatelemzés (pandas és NumPy), gépi tanulás (scikit-learn, PyTorch és TensorFlow), felszín alatti víz modellezés (FloPy) és vizualizáció (matplotlib és folium).

A hidroinformatikai Python Windows-os telepítéséhez a Miniconda vagy az Anaconda ajánlott, amely a `conda` csomagkezelőt biztosítja. A conda a térbeli könyvtárak (GDAL, PROJ, GEOS) összetett bináris függőségeit sokkal megbízhatóbban kezeli, mint a pip önmagában.

**Fejezetek, amelyekben szerepel:** 3, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 25.

---

### ArcPy, PyQGIS, GDAL/OGR, FloPy

Az **ArcPy** az Esri Python-könyvtára az ArcGIS-hez (ArcGIS Pro licenc szükséges). A **PyQGIS** a QGIS funkcionalitásához biztosít Python-hozzáférést. A **GDAL/OGR** 200+ raszter- és 100+ vektorformátumot olvas és ír — szinte minden nyílt forráskódú térbeli eszköz alapja. A **FloPy** a MODFLOW Python-felülete, amely lehetővé teszi modellek programozott felépítését, futtatását és utólagos feldolgozását.

### Python kulcskönyvtárak a hidroinformatikához

| Könyvtár | Cél | Telepítés | Kulcsfejezetek |
|---|---|---|---|
| **NumPy** | Numerikus tömbök és matematika | `conda install numpy` | 6, 12, 21, 23 |
| **pandas** | Táblázatos adatelemzés és idősorok | `conda install pandas` | 3, 4, 12, 17, 21, 23, 25 |
| **geopandas** | Térbeli vektoradatok DataFrame-ekben | `conda install geopandas` | 4, 6, 12, 17, 23 |
| **rasterio** | Pythonos raszter I/O (GDAL-ra épülő) | `conda install rasterio` | 6, 12, 23 |
| **xarray** | Többdimenziós címkézett tömbök (NetCDF) | `conda install xarray` | 3, 12, 21, 25 |
| **matplotlib** | 2D rajzolás és vizualizáció | `conda install matplotlib` | 12, 21, 23 |
| **folium** | Interaktív Leaflet térképek Python-ból | `pip install folium` | 17, 25 |
| **shapely** | Geometriai műveletek | `conda install shapely` | 4, 12 |
| **pyproj** | Koordináta-vonatkoztatási rendszer transzformációk | `conda install pyproj` | 2, 4, 12 |

### Jupyter

Interaktív számítási környezet (böngészőalapú), amely végrehajtható kódot, magyarázó szöveget, egyenleteket és vizualizációkat ötvöz egyetlen dokumentumban. A JupyterLab a jelenlegi generációs felület. A Microsoft Planetary Computer natív felülete.

---

## C.6 Adatkezelés

### PostGIS

Térbeli adatbázis-kiterjesztés a PostgreSQL-hez. Nagyszabású hidroinformatikai projektekhez — amelyek ezres nagyságrendű vízgyűjtőket, milliós vízfolyásszakaszokat vagy évtizedes monitorozási adatokat kezelnek — a PostGIS biztosítja azt a skálázhatóságot, lekérdezési teljesítményt és adatintegritást, amelyet a fájlalapú formátumok nem képesek nyújtani.

### GeoPackage

Modern, hordozható, nyílt fájlformátum térbeli adatokhoz, amely vektorelemeket, rasztercsempéket és attribútumadatokat egyetlen SQLite adatbázisfájlban tárol. A shapefile-formátumot váltja fel alapértelmezett csereformátumként.

### HydroShare

Webalapú hidrológiai adat- és modellmegosztó tárház (https://www.hydroshare.org/), amelyet a CUAHSI üzemeltet. Állandó DOI-kat biztosít az adatkészletekhez.

### ChromaDB

Vektor-adatbázis beágyazási vektorok tárolásához és lekérdezéséhez — fontos összetevője a visszakereséssel kiegészített szöveggeneráló (RAG) rendszereknek.

---

## C.7 MI és gépi tanulás

### scikit-learn

A klasszikus gépi tanulási algoritmusok szabványos megvalósítása: random forest, gradient boosting, support vector machine, k-legközelebbi szomszéd, lineáris és logisztikus regresszió, klaszterezés és dimenziósság-csökkentés. A 23. fejezet kiindulópontja.

### PyTorch

A domináns mélytanulási keretrendszer a hidrológiai kutatásban 2026-ban. Az LSTM hálózatokat meghajtó tenzor-számítási és automatikus differenciálási motor.

### TensorFlow

A Google gépi tanulási keretrendszere. Fontos a telepítéshez (TensorFlow Lite, TensorFlow Serving révén) és a Google Earth Engine gépi tanulási képességeivel való integrációhoz.

### NeuralHydrology

Célzottan épített keretrendszer mélytanulási modellek betanítására hidrológiai idősoradatokon (https://neuralhydrology.readthedocs.io/). A CAMELS adatkészletre és nemzetközi változataira szabványosított adatbetöltést biztosít, valamint LSTM, EA-LSTM és más, kifejezetten a vízgyűjtőszintű előrejelzésre tervezett architektúrákat valósít meg.

---

## C.8 Vizualizáció

### Leaflet

A legszélesebb körben használt nyílt forráskódú könyvtár interaktív webtérképekhez. A Python folium könyvtár Leaflet térképeket generál Python kódból.

### MapLibre GL JS

Vektoros csempe webtérképeket renderel WebGL-lel, sima nagyítással, forgatással és 3D terepvizualizációval a böngészőben. A Mapbox GL JS nyílt forráskódú forkja.

### CesiumJS

Teljes 3D földgömb-vizualizáció a böngészőben, beleértve a terepet, a 3D épületmodelleket, a pontfelhőket és az idődinamikus adatokat.

---

## C.9 Windows telepítési útmutató

A könyv legtöbb olvasója Windows-on dolgozik, amely az ArcGIS Pro, a HEC-HMS, a HEC-RAS és számos más eszköz elsődleges platformja. Az alábbi útmutató az ajánlott telepítési sorrendet mutatja be, amely a lehető legkevesebb ütközést okozza.

### 1. lépés: Python-környezetkezelő telepítése

1. Töltse le a **Miniconda**-t a https://docs.conda.io/en/latest/miniconda.html címről (válassza a 64 bites Windows telepítőt).
2. Futtassa a telepítőt. Hozzon létre egy dedikált környezetet:

```
conda create -n hydro python=3.12
conda activate hydro
conda install numpy pandas geopandas rasterio xarray matplotlib jupyterlab
pip install whitebox flopy folium
```

### 2. lépés: Térinformatikai szoftver telepítése

**ArcGIS Pro** (ha licenccel rendelkezik): Töltse le a szervezete Esri-portáljáról. Az ArcGIS Pro saját conda-alapú Python-környezetet telepít.

**QGIS:** Töltse le az önálló telepítőt (MSI) a https://qgis.org/download/ címről. A stabilitás érdekében a Long Term Release (LTR) verziót ajánljuk.

### 3. lépés: Terepanalízis eszközök telepítése

**TauDEM:**
1. Töltse le és telepítse a **Microsoft MPI**-t (MS-MPI).
2. Töltse le a TauDEM Windows telepítőt.
3. Adja hozzá a `C:\Program Files\TauDEM\TauDEM5Exe` könyvtárat a rendszer PATH-jához.
4. Ellenőrizze: `mpiexec -n 4 pitremove -h`

**WhiteboxTools:** `pip install whitebox`

### 4. lépés: Hidrológiai és felszín alatti víz modellek telepítése

**HEC-HMS és HEC-RAS:** Töltse le a HEC weboldaláról. Mindkettő önálló, további függőségek nélkül.

**MODFLOW 6:**
1. Töltse le és csomagolja ki egy állandó helyre (pl. `C:\MODFLOW\mf6.5`).
2. Adja hozzá a `bin` könyvtárat a rendszer PATH-jához.
3. Python integrációhoz: `pip install flopy`

### 5. lépés: Gépi tanulási keretrendszerek telepítése

**Csak CPU-ra (a legtöbb hidroinformatikai munkához elegendő):**
```
conda create -n hydro-ml python=3.12
conda activate hydro-ml
conda install scikit-learn
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install neuralhydrology
```

**GPU-gyorsított betanításhoz (NVIDIA GPU szükséges):**
```
conda create -n hydro-ml-gpu python=3.12
conda activate hydro-ml-gpu
conda install scikit-learn
conda install pytorch pytorch-cuda=12.4 -c pytorch -c nvidia
pip install neuralhydrology
```

### 6. lépés: Jupyter telepítése és környezetek összekapcsolása

```
conda activate hydro
conda install jupyterlab
python -m ipykernel install --user --name hydro --display-name "Hydro Python"
conda activate hydro-ml
python -m ipykernel install --user --name hydro-ml --display-name "Hydro ML"
```

---

## C.10 Útmutató kezdőknek: ajánlott tanulási útvonal

### 1. szakasz: A térbeli adatok megtekintése (1–2. hét)

**Cél:** Térbeli adatkészletek megnyitása, felfedezése és megjelenítése.
**Eszközök:** QGIS (ingyenes, platformfüggetlen, nulla költségkorlát).
**Tevékenységek:** Telepítse a QGIS-t, nyisson meg egy DEM-et, töltsön be egy vektoros adatkészletet, gyakorolja a jelölésváltoztatást és a térkép-elrendezés készítését. Olvassa a 2. és 4. fejezetet ezekhez a gyakorlatokhoz.

### 2. szakasz: A terephidrológia megértése (3–4. hét)

**Cél:** Teljes vízgyűjtő-lehatárolás végrehajtása DEM-ből.
**Eszközök:** QGIS WhiteboxTools bővítménnyel, vagy ArcGIS Pro Spatial Analyst-tel.
**Tevékenységek:** Kövesse a 9–11. fejezet munkafolyamatát: mélypontkitöltés, folyásirány, összegyülekezés, vízfolyáshálózat-meghatározás, vízgyűjtő-lehatárolás. Számítsa ki a HAND-rácsot (14. fejezet).

### 3. szakasz: Szkriptelés megkezdése (5–8. hét)

**Cél:** Térinformatikai munkafolyamat automatizálása Python-nal.
**Eszközök:** Python (Minicondán keresztül), Jupyter, GDAL/OGR vagy ArcPy.
**Tevékenységek:** Dolgozza fel a 12. fejezetet, a 2. szakasz kézi munkafolyamatát Python-szkriptté alakítva.

### 4. szakasz: Modellek és adatok összekapcsolása (9–12. hét)

**Cél:** Hidrológiai modell felállítása és futtatása, a kalibráció megértése.
**Eszközök:** HEC-HMS felszíni vízhez, vagy FloPy + MODFLOW felszín alatti vízhez.

### 5. szakasz: Gépi tanulás felfedezése (13–16. hét)

**Cél:** Egyszerű gépi tanulási modell betanítása hidrológiai változó előrejelzésére.
**Eszközök:** scikit-learn, majd PyTorch és NeuralHydrology.

### 6. szakasz: Áttérés a felhőalapú környezetekre (folyamatos)

**Cél:** Az asztalon lehetetlen léptékű elemzések futtatása.
**Eszközök:** Google Earth Engine, Microsoft Planetary Computer.

---

## C.11 Gyorshivatkozási táblázat

| Szoftver | Típus | Licenc | Fő fejezetek |
|---|---|---|---|
| ArcGIS Pro | Asztali térinformatika | Kereskedelmi | 4, 6, 7, 9, 10, 11, 12, 18 |
| QGIS | Asztali térinformatika | Ingyenes/Nyílt forráskódú | 4, 6, 9, 10, 12, 18 |
| Google Earth Engine | Felhő-térinformatika | Ingyenes (kutatás) | 3, 4, 6, 11, 23, 25 |
| Planetary Computer | Felhő-térinformatika | Ingyenes (kutatás) | 3, 4, 6, 11, 25 |
| TauDEM | Terepanalízis | Ingyenes/Nyílt forráskódú | 9, 10, 11, 12, 14 |
| WhiteboxTools | Terepanalízis | Ingyenes/Nyílt forráskódú | 9, 10, 12, 14 |
| GRASS GIS | Térinformatika + terepanalízis | Ingyenes/Nyílt forráskódú | 4, 6, 10, 12, 14 |
| Arc Hydro | Térinformatikai eszközkészlet | Ingyenes (ArcGIS szükséges) | 4, 9, 11, 18, 19, 20, 21 |
| HEC-HMS | Csapadék-lefolyás modell | Ingyenes | 15, 22, 24 |
| HEC-RAS | Hidraulikai modell | Ingyenes | 15, 22, 25 |
| SWAT | Vízgyűjtőmodell | Ingyenes | 4, 22, 24 |
| MODFLOW | Felszín alatti víz modell | Ingyenes | 18, 20, 21, 22, 24 |
| FEFLOW | Felszín alatti víz modell | Kereskedelmi | 18, 20, 21 |
| Noah-MP | Felszíni modell | Ingyenes/Nyílt forráskódú | 16, 22 |
| LISFLOOD | Elosztott hidrológia | Ingyenes/Nyílt forráskódú | 15, 16, 22 |
| NWM | Előrejelző rendszer | Ingyenes (kimenetek) | 11, 15, 16, 22 |
| EFAS / GloFAS | Előrejelző rendszer | Ingyenes (kimenetek) | 11, 15, 16, 22 |
| Python | Programozási nyelv | Ingyenes/Nyílt forráskódú | 4, 6, 12, 21, 23, 24 |
| ArcPy | Python térinformatikai könyvtár | ArcGIS szükséges | 4, 12 |
| PyQGIS | Python térinformatikai könyvtár | Ingyenes/Nyílt forráskódú | 4, 12 |
| GDAL/OGR | Adatfordítás | Ingyenes/Nyílt forráskódú | 4, 6, 12 |
| FloPy | MODFLOW Python API | Ingyenes/Nyílt forráskódú | 21, 25 |
| Jupyter | Notebook-környezet | Ingyenes/Nyílt forráskódú | 4, 12, 25 |
| PostGIS | Térbeli adatbázis | Ingyenes/Nyílt forráskódú | 4, 18 |
| GeoPackage | Fájlformátum | Nyílt szabvány | 4, 12, 18 |
| HydroShare | Adattárház | Ingyenes | 1, 3, 25 |
| ChromaDB | Vektor-adatbázis | Ingyenes/Nyílt forráskódú | 18 |
| scikit-learn | Klasszikus gépi tanulás | Ingyenes/Nyílt forráskódú | 23, 25 |
| PyTorch | Mélytanulás | Ingyenes/Nyílt forráskódú | 23, 25 |
| TensorFlow | Mélytanulás | Ingyenes/Nyílt forráskódú | 23, 25 |
| NeuralHydrology | Hidrológiai gépi tanulás | Ingyenes/Nyílt forráskódú | 23 |
| Leaflet | Webtérképezés | Ingyenes/Nyílt forráskódú | 17, 25 |
| MapLibre GL JS | Webtérképezés | Ingyenes/Nyílt forráskódú | 25 |
| CesiumJS | 3D vizualizáció | Ingyenes/Nyílt forráskódú | 18 |

---

## C.12 Megjegyzés a reprodukálhatóságról

A hidroinformatikai gyakorlat egyik legjelentősebb változása 2015 és 2026 között a reprodukálhatóság iránti növekvő elvárás. A függelékben felsorolt eszközök a reprodukálhatóságot gyakorlativá teszik:

- **Python + Jupyter** az egész elemzési munkafolyamatot végrehajtható dokumentumokba rögzíti.
- **conda környezetek** (`conda env export > environment.yml` segítségével exportálva) rögzítik a pontosan használt csomagverziókat.
- **HydroShare** állandó, hivatkozható tárolást biztosít az adatkészleteknek és modellfájloknak.
- **Git** (GitHub vagy GitLab platformokkal) nyomon követi a kód és a konfigurációs fájlok minden változását.
- **Docker** konténerek egy teljes számítási környezetet — operációs rendszert, könyvtárakat, modelleket és adatokat — csomagolnak egy hordozható képbe.

---

## C.13 Naprakészen maradás

A szoftververziók, URL-ek és legjobb gyakorlatok fejlődnek. A következő források naprakész tájékoztatást nyújtanak a függelékben leírt eszközökről:

- **QGIS dokumentáció:** https://docs.qgis.org/
- **Esri közösség és dokumentáció:** https://community.esri.com/ és https://pro.arcgis.com/
- **TauDEM GitHub:** https://github.com/dtarb/TauDEM
- **MODFLOW 6 dokumentáció:** https://modflow6.readthedocs.io/
- **NeuralHydrology oktatóanyagok:** https://neuralhydrology.readthedocs.io/en/latest/tutorials/
- **Google Earth Engine fejlesztői dokumentáció:** https://developers.google.com/earth-engine
- **Awesome-GIS:** https://github.com/sshuair/awesome-gis
- **CUAHSI HydroInformatics:** https://www.cuahsi.org/

A naprakészség legjobb módja az általánosan használt eszközök levelezőlistáira vagy RSS-csatornáira való feliratkozás, valamint az éves konferenciákon való részvétel: az AGU őszi ülés, az EGU általános közgyűlés, az Esri felhasználói konferencia a térinformatikai munkához; a MODFLOW and More konferencia a felszín alatti víz modellezéshez; és a NeurIPS és ICML MI a Földtudományokért workshopok a gépi tanulási alkalmazásokhoz.
