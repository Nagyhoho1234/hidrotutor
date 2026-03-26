\newpage

# D. függelék: Szójegyzék

Ez a szójegyzék a *Hidroinformatika helyzete 2026-ban* című könyvben használt szakkifejezéseket definiálja. A bejegyzések betűrendben szerepelnek. Minden bejegyzés tartalmazza a félkövér angol kifejezést, zárójelben a magyar megfelelőt (ahol van), tömör definíciót és hivatkozást arra a fejezetre, ahol a kifejezés először megjelenik vagy a legrészletesebben tárgyaljuk. Az Arc Hydro Groundwater adatmodellből származó kifejezéseket (AHGW) jelöléssel láttuk el.

---

**3D Elevation Program (3DEP)** — A USGS által irányított amerikai szövetségi program, amelynek célja az Egyesült Államok teljes területének nagy felbontású, LiDAR-ből származtatott domborzati adatokkal való lefedése. A 3DEP a korábbi National Elevation Dataset helyébe lépett, és országos, legalább 1 méteres felbontású lefedettségre törekszik. 3. fejezet.

**Agentic AI** (agentikus MI) — A mesterséges intelligencia rendszerek egy osztálya, amelyben egy nagy nyelvi modellt tervezés-végrehajtás-kiértékelés-iterálás hurokba ágyaznak, így önálló, többlépcsős gondolkodásra és eszközhasználatra is képes. A hagyományos gépi tanulástól eltérően, amely bemeneteket passzívan képez le kimenetekre, az agentikus MI célokat részszeladatokra bont, külső eszközöket hív meg (modellfuttatók, adatolvasók, statisztikai kalkulátorok), kiértékeli az eredményeket és iterál a megoldás felé. 24. fejezet.

**AGREE method** (AGREE módszer) — DEM-kondicionálási technika, amely úgy módosítja a domborzati rácsot, hogy az abból származtatott folyásutak megfeleljenek egy függetlenül térképezett vízfolyáshálózatnak. Az AGREE módszer beégeti a vízfolyáshálózatot a DEM-be úgy, hogy lealacsonyítja a cellák magasságát a térképezett meder mentén, és simítja a szomszédos cellákat, miközben megőrzi az általános topográfiai szerkezetet. 9. fejezet.

**American Community Survey (ACS)** (Amerikai Közösségi Felmérés) — Az Egyesült Államok Népszámlálási Hivatala (US Census Bureau) által végzett folyamatos statisztikai felmérés, amely évente mintegy hárommillió háztartástól gyűjt részletes társadalmi-gazdasági adatokat. Az ACS 7731 változót tartalmaz a jövedelem, iskolázottság, foglalkoztatottság, fogyatékosság és lakásviszonyok témaköreiben, amelyeket 1 és 5 éves becsléseként, egészen a blokkcsoportok szintjéig publikálnak. 17. fejezet.

**Analytic Element Method (AEM)** (analitikus elem módszer) — Felszín alatti víz szimulációs megközelítés, amelyben a vízadó réteg elemeit — kutakat, folyókat, utánpótlási zónákat és vezetőképesség-határokat — egyedi matematikai elemekként jelenítik meg, amelyek hozzájárulásait szuperponálva a tartomány bármely pontjában pontos (a feltevések keretein belül) megoldás kapható számítási rács vagy háló nélkül. A módszer úttörője Otto Strack volt, legismertebb megvalósítása a GFLOW. 21. fejezet.

**Aquifer** (vízadó réteg) — Olyan geológiai képződmény, képződménycsoport vagy képződményrész, amely elegendő telített, áteresztő anyagot tartalmaz ahhoz, hogy jelentős mennyiségű vizet szolgáltasson kutaknak és forrásoknak. A vízadó rétegeket bezártság (szabad, nyomás alatti, félig zárt), kőzettan (porózus, karszt, repedezett) és lépték (helyi, regionális, fő) szerint osztályozzák. 18–19. fejezet.

**Aquifer feature class** (vízadó réteg objektumosztály) — (AHGW) Poligon objektumosztály az Arc Hydro Groundwater adatmodellben, amely egy vízadó réteg vagy annak egy zónája területi kiterjedését ábrázolja. Minden poligon HGUID attribútummal rendelkezik, amely a HydrogeologicUnit táblához kapcsolja. 19. fejezet.

**Arc Hydro** — A vízkészlet-gazdálkodás földrajzi adatmodellje, amelyet eredetileg David Maidment publikált 2002-ben. Szabványos szókincset és struktúrát határoz meg a hidrológiai elemek — vízgyűjtők, vízfolyáshálózatok, megfigyelőpontok és idősorok — térinformatikai geoadatbázisban történő ábrázolásához. Az Arc Hydro az az információs architektúra, amelyre az NHDPlus és a Nemzeti Vízmodell (National Water Model) épült. 1. fejezet.

**Arc Hydro Groundwater (AHGW)** — Az Arc Hydro adatmodell felszín alatti víz komponense, amely kiterjeszti a keretrendszert háromdimenziós felszín alatti elemek ábrázolására, beleértve a kutakat, fúrásokat, vízadó rétegeket, hidrogeológiai egységeket, szelvényeket és szimulációs modellrácsokat. Az *Arc Hydro Groundwater: GIS for Hydrogeology* című munkában publikált. 18–21. fejezet.

**ArcGIS Pro** — Az Esri jelenlegi generációs asztali térinformatikai platformja, amely 64 bites architektúrát, projektalapú szervezést és szoros integrációt kínál az ArcGIS Online-nal. Az ArcGIS Pro biztosítja a Spatial Analyst kiterjesztést a raszter-terepanalízishez és az Arc Hydro eszközkészletet a hidrológiai adatmodellezéshez. 4. fejezet.

**ArcPy** — Az Esri Python-könyvtára az ArcGIS-hez, amely programozott hozzáférést biztosít az ArcGIS Pro minden téradat-feldolgozó eszközéhez, valamint adatkezelési, kartográfiai és térbeli elemzési funkciókat. Az ArcPy lehetővé teszi a hidrológiai munkafolyamatok szkriptelt automatizálását. 12. fejezet.

**Aspect** (kitettség, lejtésirány) — A legmeredekebb lefelé irányuló gradiens iránytűiránya a terepfelszín egy adott pontján, északtól az óramutató járásával megegyezően mérve fokban (0–360). A kitettség meghatározza a felszíni áramlás irányát, és befolyásolja a napsugárzás fogadását, az evapotranszspirációs rátát és a hó felhalmozódási mintázatát. 7. fejezet.

**Baseflow** (alapvízhozam) — A vízhozam azon összetevője, amely a felszín alatti víz megcsapolásából származik, nem pedig a közvetlen felszíni lefolyásból. Az alapvízhozam tartja fenn a folyókat száraz időszakokban, és a vízadó réteg tulajdonságai, valamint a talajvízszint és a vízfolyás közötti hidraulikus gradiens szabályozza. 11., 22. fejezet.

**Bathymetric LiDAR** (batimetriai LiDAR) — Speciális LiDAR-technológia, amely zöld hullámhosszú lézerfényt (körülbelül 532 nm) használ, amely képes áthatolni a vízen, és megmérni a folyó- és tómedrek szintjét. A hagyományos közeli infravörös LiDAR a vízfelszínről verődik vissza, és nem lát a fenékig. 13. fejezet.

**Borehole** (fúrás, mélyfúrás) — A felszín alá fúrt lyuk felszín alatti víz kinyerése, megfigyelése, geotechnikai vizsgálat vagy ásványi kutatás céljából. A fúrások jelentik az elsődleges közvetlen megfigyelési ablakot a felszín alatti geológia és hidrogeológia számára. 18–19. fejezet.

**BoreholeLog** (fúrásnapló) — (AHGW) Tábla az Arc Hydro Groundwater adatmodellben, amely a fúrások mentén mért vertikális adatokat tárolja. A tábla formációhatárokat, kőzettani leírásokat, geofizikai méréseket és más, adott mélységben rögzített adatokat tárol. 19. fejezet.

**BorePoint and BoreLine** (fúráspont és fúrásvonal) — (AHGW) Z-értékkel rendelkező pont- és vonal-objektumosztályok az Arc Hydro Groundwater adatmodellben, amelyek fúrási adatokat háromdimenziós geometriaként ábrázolnak. A BorePoint elemek egyes kontaktusokat vagy méréseket, a BoreLine elemek a fúrás menti folyamatos intervallumokat képviselik. 18. fejezet.

**Calibration** (kalibráció) — A modellparaméterek módosításának folyamata annak érdekében, hogy a szimulált kimenetek egyezzenek a megfigyelt mérésekkel. Az egyezést jellemzően célfüggvényekkel számszerűsítik, mint a Nash–Sutcliffe-hatékonyság vagy a Kling–Gupta-hatékonyság. Kalibrálásra azért van szükség, mert a modellparaméterek nem mérhetők közvetlenül azon a léptéken, amelyen a modellek működnek. 22. fejezet.

**CARPATCLIM** — Nagy felbontású (0,1 fokos) rácsos éghajlati adatkészlet a Kárpát-medence régiójára, amelyet sűrű állomáshálózat minőségellenőrzött megfigyeléseinek interpolálásával állítottak elő az 1961–2010 közötti időszakra. A régiós nagy állomássűrűség miatt különösen értékes a magyar hidrológiai tanulmányok számára. 8. fejezet.

**Catchment** (vízgyűjtő terület) — Az a földterület, amelyről a víz egy vízfolyáshálózat meghatározott pontjára csorog le. Az NHDPlus keretrendszerben minden egyes vízgyűjtő egy vízfolyásszakasznak felel meg, és a hidrológiai modellezés alapvető térbeli egysége. A vízgyűjtő, a vízgyűjtő terület és a lefolyási medence kifejezéseket gyakran felcserélhetően használják, bár eltérő léptékre utalhatnak. 11., 16. fejezet.

**Cell size** (cellaméret, rácsméret) — Egy raszteradat négyzet alakú rácscellájának egy oldalának hossza, amelyet a koordinátarendszer egységeiben mérnek. A cellaméret határozza meg a térbeli felbontást, az adatmennyiséget és a feloldható legkisebb elem méretét. 5. fejezet.

**Census block** (számlálókerület) — Az amerikai népszámlálás legfinomabb földrajzi egysége, amely jellemzően 30–40 lakóegységet tartalmaz egy-két utcaszakasz mentén. Az Egyesült Államokban mintegy 11 millió számlálókerület van. 17. fejezet.

**Census tract** (számlálókörzet) — Az amerikai népszámlálás azon földrajzi egysége, amelyet hozzávetőleg 1200–8000 fő befogadására terveztek. A számlálókörzetek a részletes társadalmi-gazdasági elemzés elsődleges egységei, és számos demográfiai tanulmány építőelemei. 17. fejezet.

**CHIRPS** (Climate Hazards Group InfraRed Precipitation with Station Data) — Globális rácsos csapadékadatkészlet, amely műholdas képeket és állomási megfigyeléseket kombinálva napi és ötnapos (pentád) becsléseket állít elő 0,05 fokos felbontásban 1981-től napjainkig. A CHIRPS elsődleges csapadékforrás a ritka állomáshálózattal rendelkező régiók, különösen Szubszaharai Afrika és Dél-Ázsia számára. 3. fejezet.

**Cloud-optimized GeoTIFF (COG)** (felhőoptimalizált GeoTIFF) — A GeoTIFF raszterformátum egy változata, amelyet az interneten keresztüli hatékony hozzáférésre terveztek. A COG-ok belső csempékben és áttekintő szintekben tárolják az adatokat, lehetővé téve, hogy a szoftver csak a szükséges részletet olvassa be egy adott nézeti kiterjedéshez és nagyítási szinthez anélkül, hogy a teljes fájlt le kellene tölteni. 5. fejezet.

**COMID** (Common Identifier — közös azonosító) — Az NHDPlus hidrográfiai keretrendszerben minden egyes vízfolyásszakaszhoz rendelt egyedi számértékű azonosító. A COMID-ok az elsődleges kulcsok, amelyek összekapcsolják a szakaszokat a vízgyűjtőikkel, attribútumaikkal és a Nemzeti Vízmodell (National Water Model) vízhozam-előrejelzéseivel. 11., 16. fejezet.

**Computational hydrology** (számítási hidrológia) — A hidrológia azon ága, amely matematikai modelleket és számítástechnikát használ a víz hidrológiai cikluson belüli mozgásának szimulálásához és előrejelzéséhez. A számítási hidrológia az 1960-as években jelent meg a Stanford Watershed Model és a HEC-1 modellekkel, és azóta kontinentális léptékű operatív előrejelző rendszerekké fejlődött. 1. fejezet.

**Conceptual model** (koncepcionális modell) — Egy tárgy vagy jelenség leírására szolgáló gondolatrendszer, amely lehetővé teszi az arról való gondolkodást. A hidrológiában a koncepcionális modell leírja, hogyan mozog a víz egy rendszeren keresztül — például a vízkörforgás azon fogalma, hogy a csapadék lehull, lefolyik vagy beszivárog, elpárolog és újrahasznosul. 1. fejezet.

**Confining unit** (vízzáró réteg) — Alacsony áteresztőképességű geológiai réteg (jellemzően agyag, pala vagy repedésmentes kőzet), amely korlátozza a felszín alatti víz függőleges mozgását a vízadó rétegek között. A vízzáró rétegek elválasztják a vízadó rétegeket és szabályozzák a hidraulikai kapcsolat mértékét a többrétegű vízadó rendszerekben. 20. fejezet.

**Copernicus DEM** (Kopernikusz digitális domborzatmodell) — Az elsődleges európai digitális domborzati adatkészlet, amely a TanDEM-X radar műholdmisszióból származik. Három változatban érhető el: GLO-30 (30 méteres felbontás, globális, ingyenes), GLO-90 (90 méteres, globális, ingyenes) és EEA-10 (10 méteres, európai lefedettség). A Copernicus DEM digitális felszínmodell, ami azt jelenti, hogy az épületek és a növényzet tetejét rögzíti, nem a csupasz talajfelszínt. 3. fejezet.

**Copernicus programme** (Kopernikusz program) — Az Európai Unió Földmegfigyelési programja, amelyet az Európai Bizottság irányít az Európai Űrügynökséggel (ESA) együttműködve. A Kopernikusz ingyenes, nyílt adatokat biztosít a Sentinel műholdflottából, valamint információs szolgáltatásokat, beleértve a Veszélyhelyzet-kezelési Szolgálatot és az Éghajlatváltozási Szolgálatot. 3. fejezet.

**Curve number (CN)** (lefolyási szám) — Dimenzió nélküli empirikus paraméter az NRCS (korábban SCS) csapadék-lefolyás módszerében, amely egy talaj-felszínborítás-állapot kombináció lefolyási potenciálját jellemzi. Az értékek 30-tól (nagyon alacsony lefolyási potenciál) 100-ig (vízzáró felszín) terjednek. A CN egyetlen indexbe integrálja a talajtípust, a felszínborítást, az előzetes nedvességtartalmat és a kezelési gyakorlatot. 22. fejezet.

**D8 algorithm** (D8 algoritmus) — A legszélesebb körben használt módszer a folyásirány számítására rácsos DEM-en, amelyet O'Callaghan és Mark publikált 1984-ben. Minden cellánál a D8 kiértékeli a lejtést mind a nyolc szomszéd felé, és a legmeredekebb lefelé irányuló gradiensű szomszédnak rendeli a folyást. Az algoritmus a folyást nyolc diszkrét irány egyikére korlátozza 45 fokos lépésközönként. 10. fejezet.

**D-infinity (D-inf) algorithm** (D-végtelen algoritmus) — David Tarboton által 1997-ben publikált folyásirány-algoritmus, amely kiküszöböli a D8 iránykorlátját azáltal, hogy háromszögelemeket illeszt az egyes cellák nyolc szomszédjára, és a legmeredekebb lefelé irányuló irányt folytonos szögként számítja ki. A folyás két szomszédos cella között az arányuknak megfelelően osztható el, simább és fizikailag reálisabb folyásutakat eredményezve. 7., 10. fejezet.

**Data assimilation** (adatasszimiláció) — Matematikai keretrendszer, amely modellelőrejelzéseket és megfigyeléseket kombinálva olyan állapotbecslést eredményez, amely jobb, mint bármelyik forrás önmagában. Az adatasszimilációs módszerek — beleértve a Kálmán-szűrőt, az Ensemble Kálmán-szűrőt és a variációs megközelítéseket — folyamatosan egyeztetik a modell-előrejelzéseket a beérkező szenzoros adatokkal az operatív rendszerekben. 25. fejezet.

**Data model** (adatmodell) — Strukturált keretrendszer egy tárgy leírására és adatainak tárolására. A térinformatikában az adatmodell meghatározza, milyen információkat tárolunk, hogyan szervezzük azokat és hogyan kapcsolódnak egymáshoz az elemei. Az Arc Hydro a vízkészlet-gazdálkodás földrajzi adatmodellje. 1. fejezet.

**Datum** (dátum, geodéziai dátum) — Egy ellipszoid, amely a valós Földhöz viszonyítva van pozicionálva és orientálva, meghatározva azt a vonatkoztatási keretet, amelyben a koordinátáknak jelentésük van. A dátum a matematikai ellipszoidfelszínt rögzíti a fizikai Föld meghatározott pontjaihoz. A modern dátumok geocentrikusak (a Föld tömegközéppontjára központosítottak); a korábbi dátumok regionálisak. 2. fejezet.

**DDM-5** (Digitális Domborzatmodell) — Magyarország országos digitális domborzatmodellje 5 méteres felbontásban, amelyet a Lechner Tudásközpont készített az EOV koordináta-rendszerben (EPSG:23700). Az 1:10 000 méretarányú topográfiai szintvonalakból és sztereo-fotogrammetriából származtatott. A DDM-5 a hiteles országos domborzati termék Magyarország számára. 3. fejezet.

**Delaunay triangulation** (Delaunay-háromszögelés) — Ponthalmaz háromszögelése, amelyben egyetlen pont sem esik a háromszögek köréírt körének belsejébe. A Delaunay-háromszögelés a Thiessen/Voronoi-poligonok geometriai duálisa, és a lehető legszabályosabb háromszögeket állítja elő, ami optimálissá teszi a TIN-alapú felszínábrázoláshoz. 8. fejezet.

**DEM (Digital Elevation Model)** (digitális domborzatmodell) — Raszterrács, amelyben minden cella a terep adott helyen mért magassági értékét tárolja. A DEM-ek a számítási hidrológia alapjai; belőlük származtatják a lejtést, a kitettséget, a folyásirányt, az összegyülekezést, a vízfolyáshálózatokat és a vízgyűjtő-határokat. 3., 5. fejezet.

**DEM conditioning** (DEM-kondicionálás) — A nyers digitális domborzatmodell módosításának folyamata annak érdekében, hogy minden cellából a tartomány határáig folyamatos lefelé irányuló lefolyás érvényesüljön. A DEM-kondicionálás magában foglalja a mélypontok kitöltését, a sík területek feloldását és opcionálisan az ismert vízfolyáshálózatok beégetését. Ez minden terep-alapú hidrológiai elemzés elengedhetetlen első lépése. 9. fejezet.

**Digital surface model (DSM)** (digitális felszínmodell) — Olyan domborzatmodell, amely a Föld felszínén lévő összes objektum — épületek, fák és egyéb növényzet — tetejét ábrázolja. A DSM abban különbözik a DEM-től vagy a DTM-től, hogy nem a csupasz talajt képviseli. A Copernicus DEM egy DSM. 13. fejezet.

**Digital twin** (digitális iker) — Egy fizikai rendszer virtuális másolata, amely folyamatos, kétirányú kapcsolatot tart fenn a valós rendszerrel szenzoros adatcsatornákon, modellfrissítéseken és — a legmagasabb érettségi szinten — automatizált vezérlési tevékenységeken keresztül. A vízrendszerek digitális ikrei a statikus modellektől az autonóm vezérlésig négy érettségi szintet fognak át. 25. fejezet.

**Drainage density** (vízhálózat-sűrűség) — A vízgyűjtő területen belüli összes vízfolyásmeder teljes hossza osztva a vízgyűjtő területtel, km/km² egységben kifejezve. A vízhálózat-sűrűség fordítottan arányos az átlagos domboldalhosszal, és közvetlenül befolyásolja azt az időt, amely alatt a víz a legközelebbi mederhez ér. 11. fejezet.

**DREAM** (Differential Evolution Adaptive Metropolis) — Bayesi Markov-lánc Monte Carlo algoritmus modellkalibráláshoz, amely a paraméterteret több, egymással információt cserélő lánc segítségével járja be, és a paraméterek utólagos valószínűségi eloszlását állítja elő egyetlen optimum helyett. 22. fejezet.

**E-OBS** — Európai rácsos napi hőmérséklet- és csapadékadatkészlet, amelyet az Európai Éghajlat-felmérési és Adatkészlet projekt készített 0,1 fokos (hozzávetőleg 11 km-es) felbontásban. Az E-OBS az európai hidrológiai tanulmányok szabványos rácsos éghajlati terméke, és a rendelkezésre álló legsűrűbb állomáshálózatra épül. 8. fejezet.

**EFAS (European Flood Awareness System)** (Európai Árvíz-figyelmeztető Rendszer) — A páneurópai árvíz-előrejelző rendszer, amelyet a Copernicus Veszélyhelyzet-kezelési Szolgálat üzemeltet az ECMWF-nél. Az EFAS középtávú ensemble árvíz-előrejelzéseket biztosít az egész európai kontinensre, a LISFLOOD hidrológiai modellt használva az ECMWF időjárás-előrejelzései alapján. 1., 16. fejezet.

**Ellipsoid** (ellipszoid, forgási ellipszoid) — Más néven szferoid. Az a háromdimenziós felszín, amely egy ellipszis rövidebb (poláris) tengelye körüli forgatásával jön létre, és a Föld alakjának matematikai közelítéseként szolgál a koordinátarendszer-definíciókhoz. Az ellipszoidot a fél-nagytengely és a lapultság definiálja. 2. fejezet.

**Ensemble Kalman Filter (EnKF)** (Ensemble Kálmán-szűrő) — Szekvenciális adatasszimilációs módszer, amely a modell bizonytalanságát 50–500 párhuzamos modellfuttatásból álló ensemble-lel ábrázolja, amelyek mindegyike kissé eltérő kezdeti feltételekkel és paraméterekkel rendelkezik. Az ensemble szórása közelíti a hiba-kovarianciát, és a megfigyelések beérkezésekor minden egyes tagot módosítanak. 25. fejezet.

**EOV (Egységes Országos Vetületi rendszer)** — Magyarország egységes országos vetületi koordináta-rendszere (EPSG:23700), amely a Magyar Datum 1972-re (HD72) és a GRS 1967 ellipszoidra épül. Az EOV tranzverzális Mercator-vetületet alkalmaz 19,0481 fokos keleti középmeridiannal. Az EOV koordináták északi értékei a 0–400 000 tartományba, keleti értékei a 400 000–1 000 000 tartományba esnek. 2. fejezet.

**Equifinality** (ekvifinalitás) — Az a jelenség, amelyben több különböző paraméterkészlet egyformán jó (vagy egyformán rossz) illeszkedést eredményez a megfigyelt adatokhoz, lehetetlenné téve egyetlen „helyes" paraméterezés azonosítását. Az ekvifinalitás a modellkalibráció alapvető kihívása, és motiválja a Bayesi módszerek használatát, amelyek a paraméter-bizonytalanságot jellemzik egyetlen optimum keresése helyett. 22. fejezet.

**ERA5** — Az Európai Középtávú Időjárás-előrejelzési Központ (ECMWF) által készített ötödik generációs légköri reanalízis adatkészlet, amely óránkénti becsléseket biztosít légköri, szárazföldi és óceáni változókról 1940-tól napjainkig, hozzávetőleg 31 km-es vízszintes felbontásban. Az ERA5-Land fokozott felbontású felszíni változókat biztosít hozzávetőleg 9 km-es felbontásban. 3. fejezet.

**ETRS89 (European Terrestrial Reference System 1989)** (Európai Földfelszíni Referenciarendszer 1989) — Az Európai Unió hivatalos geodéziai vonatkoztatási rendszere, amelyet állandó GNSS-állomások hálózatával valósítanak meg. Az ETRS89 a GRS 1980 ellipszoidra épül, és centiméter szinten kompatibilis a WGS84-gyel. Az INSPIRE irányelv által előírt koordináta-vonatkoztatási rendszer az európai térbeli adatokhoz. 2. fejezet.

**EU-Hydro** — A Copernicus program által készített európai hidrográfiai adatkészlet, amely páneurópai vízfolyáshálózatot és vízgyűjtő-lehatárolást biztosít nagy felbontású műholdképek és a Copernicus DEM alapján. Az EU-Hydro kiegészíti a nemzeti hidrográfiai adatkészleteket a határon átnyúló konzisztencia biztosításával. 16. fejezet.

**Evapotranspiration (ET)** (evapotranszspiráció, párolgás) — A talaj- és vízfelszínről történő párolgás és a növényzet transszspirációjának együttes folyamata. Az evapotranszspiráció a vízháztartás egyik fő összetevője, amely mérsékelt éghajlaton jellemzően a csapadék 40–80%-át teszi ki. A napsugárzás, a hőmérséklet, a légnedvesség, a szél és a növényzet tulajdonságai vezérlik. 6. fejezet.

**Extent** (kiterjedés) — Raszterrács által lefedett teljes földrajzi terület, amelyet határoló koordinátái (xmin, ymin, xmax, ymax) definiálnak. A kiterjedésnek a vizsgálati területet és egy pufferzónát kell magában foglalnia a vízgyűjtő-lehatároláshoz, a szélhatások elkerülése érdekében. 5. fejezet.

**Extrapolation** (extrapoláció) — Értékek becslése az ismert mintapontok tartományán kívül, amely lényegesen nagyobb bizonytalansággal jár, mint az interpoláció (becslés a mintavételi tartományon belül). Térbeli elemzésben extrapoláció akkor fordul elő, amikor a raszter kiterjedése túlnyúlik a legszélső megfigyelési pontokon. 8. fejezet.

**FAIR principles** (FAIR elvek) — Adatkezelési elvek, amelyek megkövetelik, hogy a kutatási adatok legyenek Megtalálhatók (Findable), Hozzáférhetők (Accessible), Interoperábilisak (Interoperable) és Újrahasznosíthatók (Reusable). A CUAHSI által üzemeltetett HydroShare platform a FAIR elveket valósítja meg a hidrológiai kutatási termékek számára. 1. fejezet.

**Feature** (objektum, elem) — Egy objektumosztály egy sora, amely egy térbeli objektumot képvisel geometriájával (pont, vonal, poligon vagy multipatch) és kapcsolódó attribútumaival együtt. 4. fejezet.

**Feature class** (objektumosztály) — Azonos geometriatípusú, attribútumú és relációjú elemek gyűjteménye, amelyet a geoadatbázisban táblázatként tárolnak, a geometriát definiáló Shape mezővel. Az objektumosztályok a vektoros adattárolás alapvető egységei a térinformatikában. 4. fejezet.

**Feature dataset** (elem-adathalmaz) — Tároló a geoadatbázison belül a térben összefüggő, azonos koordináta-rendszerű objektumosztályok csoportosítására. Az elem-adathalmaz relációosztályokat, topológiai szabályokat és hálózati osztályokat is tartalmaz. 4., 18. fejezet.

**FEFLOW** — A DHI Group által fejlesztett kereskedelmi végeselem-alapú felszín alatti víz modellező szoftver, amelyet Európában széles körben alkalmaznak áramlás, anyagtranszport és hőtranszport szimulációjára porózus és repedezett közegben. A FEFLOW nem strukturált rácsokat és összetett 3D geológiai szerkezeteket támogat, és shapefile- és geoadatbázis-import/export révén integrálható a térinformatikával. 21. fejezet.

**Field** (mező, folytonos mező) — A térinformatikában: a tér minden lehetséges pontján definiált mennyiség — folytonos jelenség, mint a magasság, a hőmérséklet vagy a talajnedvesség. A mezőket digitálisan raszterrácsokkal, TIN-ekkel vagy szintvonal–folyásvonal modellekkel ábrázolják. 5. fejezet.

**Finite difference method (FDM)** (véges differencia módszer) — Numerikus megközelítés parciális differenciálegyenletek megoldására, amely a modelltartományt szabályos négyszögletes rácsra osztja fel, és a folytonos deriváltakat a szomszédos cellaértékek közötti különbségekkel közelíti. A MODFLOW a legszélesebb körben használt véges differencia felszín alatti víz modell. 21. fejezet.

**Finite element method (FEM)** (végeselem-módszer) — Numerikus megközelítés parciális differenciálegyenletek megoldására, amely a tartományt kis geometriai elemekre (háromszögek, tetraéderek, prizmák) osztja fel, és a megoldást polinomfüggvényekkel közelíti minden elemen belül. A FEFLOW az elsődleges végeselem-kód felszín alatti víz modellezéshez. 21. fejezet.

**FIPS code** (FIPS-kód) — Federal Information Processing System kód, az amerikai földrajzi egységek szabványos numerikus azonosítója. Az államkódok 2 számjegyűek (pl. Texas = 48), a megyekódok 3 számjegyűek, a számlálókörzet-kódok 6 számjegyűek, a blokkkódok 4 számjegyűek. A FIPS-kódok lehetővé teszik a népszámlálási határok és az attribútumtáblák programozott összekapcsolását. 17. fejezet.

**Flattening** (lapultság) — Az ellipszoid paramétere, amelyet $f = (a - b) / a$ képlettel definiálnak, ahol $a$ a fél-nagytengely (egyenlítői sugár) és $b$ a fél-kistengely (poláris sugár). A Föld esetében $f \approx 1/298,257$. 2. fejezet.

**Flow accumulation** (összegyülekezés) — Raszterrács, amelyben minden cella értéke a rajta keresztül lefolyó felső cellák számát (vagy a teljes felső vízgyűjtő területet) jelöli, amelyet az összes cella folyásirányainak nyomkövetésével számítanak ki. A nagy összegyülekezési értékű cellák vízfolyásokon helyezkednek el; az alacsony értékű cellák domboldalon. 10. fejezet.

**Flow direction** (folyásirány) — Raszterrács, amelyben minden cella értéke a víz áramlási irányát jelöli az adott cellából, amelyet a szomszédos cellák felé irányuló topográfiai lejtés határoz meg. A folyásirány az alapvető közbenső termék a kondicionált DEM és a származtatott vízfolyáshálózatok, vízgyűjtők és HAND-felszínek között. 10. fejezet.

**Focal operation** (környezeti művelet) — Térképi algebrai művelet, amelyben minden kimeneti cellát a bemeneti rács körülötte lévő cellaablakából számítanak ki. A lejtés- és kitettségszámítás klasszikus példa. Szomszédsági műveletnek is nevezik. 6. fejezet.

**Geocentric datum** (geocentrikus dátum) — Geodéziai dátum, amelyben a vonatkoztatási ellipszoid középpontja egybeesik a Föld tömegközéppontjával. A modern dátumok, mint a WGS84 és az ETRS89, geocentrikusak, globálisan konzisztens vonatkoztatási kereteket nyújtva. A régebbi nemzeti dátumok nem geocentrikusak. 2. fejezet.

**Geodatabase** (geoadatbázis) — Földrajzi információk strukturált adatkészletekbe szervezett tárháza egy relációs adatbázis-rendszeren belül. A geoadatbázis térbeli integritási szabályokat érvényesít, relációkat tart fenn az elemek között, és tartományokat, altípusokat és topológiát támogat. Az Esri fájl-geoadatbázis (.gdb) az ArcGIS Pro szabványos formátuma. 4., 18. fejezet.

**Geodesy** (geodézia) — A Föld alakjának, orientációjának és gravitációs terének mérésével és ábrázolásával foglalkozó tudomány. A geodézia adja a vonatkoztatási felszíneket (geoid és ellipszoid), koordináta-rendszereket és dátum-transzformációkat, amelyek minden térbeli vízügyi adat alapját képezik. 2. fejezet.

**GeoArea** — (AHGW) Poligon-objektumosztály az Arc Hydro Groundwater adatmodellben, amely egy hidrogeológiai egység kétdimenziós vetületi lenyomatát ábrázolja. A GeoArea poligonok HGUID attribútumokkal rendelkeznek, amelyek a HydrogeologicUnit osztályozási táblához kapcsolják őket. 20. fejezet.

**Geographic data model** (földrajzi adatmodell) — A Föld felszínén található elemek és jelenségek ábrázolására tervezett adatmodell, térbeli adatkészletek felhasználásával a térinformatikán belül. Az Arc Hydro a vízkészlet-gazdálkodás földrajzi adatmodellje. 1. fejezet.

**Geoid** (geoid) — A Föld gravitációs terének ekvipotenciális felszíne, amely legjobban közelíti az átlagos tengerszintet. A geoid sima, de nem szabályos — a felszín alatti tömegeloszlás változásai miatt hullámzik. Ez a magasság természetes vonatkoztatási felülete, mert a víz a nagyobb gravitációs potenciáltól az alacsonyabb felé áramlik. 2. fejezet.

**Geoid undulation** (geoidhullám) — A geoidfelszín és a vonatkoztatási ellipszoid közötti függőleges eltérés, jellemzően $N$-nel jelölve. Az ellipszoidmagasság $h$, az ortometrikus magasság $H$ és a geoidhullám közötti összefüggés: $h = H + N$. 2. fejezet.

**Geoprocessing** (téradat-feldolgozás) — A térinformatika azon funkciója, amely térbeli elemzési műveleteket végez földrajzi adatokon, új adatkészleteket állítva elő kimenetként. A téradat-feldolgozó eszközök közé tartozik a fedvényezés, a pufferelés, a vágás, az összevonás és a raszter-terepanalízis teljes eszköztára, amely a hidrológia alapja. 4. fejezet.

**GeoRasters** — (AHGW) Raszterkatalógus az Arc Hydro Groundwater adatmodellben a hidrogeológiai egységek tulajdonságait leíró raszteradatkészletek tárolására és indexelésére, mint például tetőszint-felszínek, vastagságtérképek vagy hidraulikus vezetőképesség-eloszlások. 20. fejezet.

**GeoSection** — (AHGW) Multipatch-objektumosztály az Arc Hydro Groundwater adatmodellben, amely háromdimenziós paneleket ábrázol függőleges geológiai szelvények szerkesztéséhez. Minden GeoSection elem egy hidrogeológiai egységet képvisel egy szelvényvonal mentén. 20. fejezet.

**GeoVolume** — (AHGW) Multipatch-objektumosztály a hidrogeológiai egységek háromdimenziós térfogati objektumokként való ábrázolására. A GeoVolume-ok rögzítik a felszín alatti képződmények teljes 3D geometriáját. 20. fejezet.

**Geoscientific Information Systems (GSIS)** (geotudományi információs rendszerek) — Összetett háromdimenziós felszín alatti objektumok felszín- vagy térfogat-ábrázolással történő megjelenítésére tervezett speciális információs rendszerek. A GSIS a hagyományos térinformatikától a 3D geológiai modellezés natív támogatásában különbözik. 18. fejezet.

**GloFAS (Global Flood Awareness System)** (Globális Árvíz-figyelmeztető Rendszer) — Az EFAS globális kiterjesztése, amely a Föld minden nagyobb folyójára vízhozam-előrejelzéseket biztosít. A GloFAS-t a Copernicus Veszélyhelyzet-kezelési Szolgálat üzemelteti, és 30 napos valószínűségi előrejelzéseket nyújt világszerte. 16. fejezet.

**Google Earth Engine (GEE)** — Felhőalapú térbeli elemzési platform, amely ingyenes hozzáférést biztosít több petabájtos műholdas kép- és térbeli adattárhoz, valamint felhő-számítástechnikai infrastruktúrához ezek feldolgozásához. A GEE átalakító hatású a vízkészlet-gazdálkodásra, mert kontinentális léptékű elemzést tesz lehetővé adatletöltés nélkül. 4. fejezet.

**GRACE** (Gravity Recovery and Climate Experiment) — Műholdas misszió (és utódja, a GRACE-FO), amely a Föld gravitációs terének változásait méri, lehetővé téve a szárazföldi vízkészlet-változások nagyszabású kimutatását — beleértve a felszín alatti víz fogyását, a jégtömeg csökkenését és a szezonális víz-újraelosztást. A GRACE biztosította az első műholdas bizonyítékot a 2011-es texasi aszály felszín alatti vízre gyakorolt hatásáról. 1., 2. fejezet.

**Grid network** (rácshálózat) — Az az irányított gráf, amely akkor jön létre, amikor a D8 folyásirányokat a DEM minden cellájára kiszámítják. Ebben minden cella pontosan egy kimenő éllel rendelkezik, amely a lefolyási irányban a szomszéd cella felé mutat. A rácshálózat a kifolyási cellákban gyökerező fák erdeje, és implicit módon kódolja a táj teljes lefolyási szerkezetét. 10. fejezet.

**GR4J** (modèle du Génie Rural à 4 paramètres Journalier) — Takarékos paraméterezésű koncepcionális csapadék-lefolyás modell mindössze négy paraméterrel, amelyet az INRAE fejlesztett Franciaországban. Egyszerűsége ellenére a GR4J versenyképes teljesítményt nyújt jóval összetettebb modellekkel szemben, és gyakran használják referenciamodellként kalibrálási tanulmányokban. 22. fejezet.

**Groundwater body** (felszín alatti víztest) — Az EU Víz Keretirányelv keretében a felszín alatti víz kezelési céljaira meghatározott igazgatási-szabályozási egység. Magyarország 185 felszín alatti víztestet határolt le, amelyeket négy fő típusba sorolnak: porózus, karszt, vegyes és termális. Minden víztesthez mennyiségi és kémiai állapotot rendelnek. 19. fejezet.

**Hallucination** (hallucináció) — A nagy nyelvi modellek kontextusában: hihetően hangzó, de tényszerűen helytelen információ generálása. A megalapozási mechanizmusok — beleértve a valós adatokat, modellkimeneteket és szakterületi korlátokat — elengedhetetlenek a hallucináció csökkentéséhez a hidrológiai modellezésre alkalmazott ágensalapú MI-rendszerekben. 24. fejezet.

**HAND (Height Above Nearest Drainage)** (legközelebbi vízfolyáshoz viszonyított magasság) — DEM-ből származtatott raszterfelszín, amelyben minden cella értéke a legközelebbi vízfolyás meder feletti függőleges távolságát jelöli, a hidrológiai folyásút mentén mérve. A HAND az abszolút magasságot vízfolyáshoz viszonyított vonatkoztatási keretté alakítja, amely közvetlenül jelzi az árvízveszélyeztetettséget. 14. fejezet.

**HEC-HMS** (Hydrologic Engineering Center's Hydrologic Modeling System) — Széles körben használt csapadék-lefolyás modell, amelyet az Egyesült Államok Hadseregének Mérnöki Karának Hidrológiai Mérnöki Központja fejlesztett. A HEC-HMS moduláris opciókat kínál a veszteségbecsléshez (SCS CN, Green–Ampt), a transzformációhoz (Clark, Snyder egységhidrográf), az alapvízhozamhoz és a mederben történő hullámtérterjedéshez (Muskingum). 16., 22. fejezet.

**HEC-RAS** (Hydrologic Engineering Center's River Analysis System) — Egydimenziós és kétdimenziós folyóáramlás-elemzés, állandó és nem állandósult áramlásszimulálás, hordaléktranszport és vízminőségi modellezés szabványos hidraulikai modellező szoftvere. A HEC-RAS felmért keresztszelvényeket használ a medergeometria jellemzésére. 15. fejezet.

**Helmert transformation** (Helmert-transzformáció) — Hétparaméteres koordináta-transzformáció (három eltolás, három forgatás és egy méretarány-tényező), amelyet geodéziai dátumok közötti átváltásra használnak. A Helmert-paraméterek dátumpáronként specifikusak, és elengedhetetlenek a különböző nemzeti koordináta-rendszerekből származó adatok helyes kombinálásához. 2. fejezet.

**Hidroinformatics** (hidroinformatika) — A hidrológia, a térinformatika, a számítási modellezés és az adattudomány metszéspontjában álló diszciplína. A magyar ihletésű írásmód a közép-európai vízgazdálkodási hagyományban gyökerező szemléletet jelöl, amelyet a magyar tapasztalat formált Európa egyik legösszetettebb folyórendszerének kezelése során. 1. fejezet.

**HorizonID** (horizontazonosító) — Egész szám típusú index az Arc Hydro Groundwater adatmodellben, amely a hidrogeológiai egységek függőleges elrendezését határozza meg egy üledéklerakódási sorrendben. A HorizonID értékeit alulról felfelé rendelik hozzá, a legkisebb értéket az alapi egység kapja. 20. fejezet.

**HRRR (High Resolution Rapid Refresh)** (nagy felbontású gyors frissítés) — A NOAA által üzemeltetett konvekciófelbontó légköri modell, amely óránként asszimilálja a radar-, repülőgép-, műholdas és felszíni megfigyeléseket, és 3 km-es felbontásban, 18 órás előrejelzéseket állít elő. A HRRR biztosítja a rövid távú időjárási bemenetet az amerikai Nemzeti Vízmodell számára. 16. fejezet.

**HydroCode** — Szöveges attribútum az Arc Hydro adatmodellben, amely egy elem állandó nyilvános azonosítójaként szolgál, biztosítva a kapcsolódást külső információs rendszerekhez (pl. NHDPlus COMID-ok, állami vízadó réteg-kódok). 19. fejezet.

**Hydrogeologic framework** (hidrogeológiai keretmodell) — A felszín alatti rétegek egyszerűsített ábrázolása, amely a geológiai képződményeket hidraulikai tulajdonságaik (vízadó réteg, vízzáró réteg, félig áteresztő réteg) szerint osztályozza, nem pedig üledéklerakódási történetük alapján. A keretmodell meghatározza az egységeket, függőleges elrendezésüket, térbeli kiterjedésüket és háromdimenziós határaikat. 20. fejezet.

**HydrogeologicUnit table** (HydrogeologicUnit tábla) — (AHGW) Az Arc Hydro Groundwater adatmodell hidrogeológiai keretének központi szervező táblája. Minden sor egy koncepcionális hidrogeológiai egységet definiál, HydroID, HGUCode, HGUName, AquiferID és HorizonID attribútumokkal. A felszín alatti egységek összes térbeli ábrázolása erre a táblára hivatkozik. 20. fejezet.

**HydroID** — Egész szám típusú attribútum az Arc Hydro adatmodellben, amely az objektumokat a teljes geoadatbázisban egyedileg azonosítja, nem csupán egyetlen objektumosztályon belül. A HydroID az ObjectID-tól a geoadatbázis-szintű egyediségében különbözik. 18–20. fejezet.

**HydroSHEDS** (Hydrological Data and Maps Based on Shuttle Elevation Derivatives at Multiple Scales) — Globális adatkészlet, amely vízfolyáshálózatokat, vízgyűjtő-határokat, folyásirány-rácsokat és összegyülekezési adatokat biztosít az SRTM domborzati adatokból. A HydroSHEDS az egész világot lefedi, és a nemzeti térképezési infrastruktúrával nem rendelkező régiók elsődleges hidrográfiai referenciája. 3. fejezet.

**HydroShare** — Webalapú rendszer hidrológiai adatok és modellek megosztására, amelyet a CUAHSI üzemeltet, és amelyet David Tarboton és munkatársai fejlesztettek. A HydroShare megvalósítja a FAIR elveket, és lehetővé teszi a kutatók számára adatok, modellek és számítási munkafolyamatok állandó DOI-val történő publikálását. 1. fejezet.

**IDW (Inverse Distance Weighting)** (fordított távolsággal súlyozott interpoláció) — Térbeli interpolációs módszer, amely a nem mért helyeken az értékeket a környező mintapontok súlyozott átlagaként becsüli, a súlyokat a távolság fordított hatványaként csökkentve. A $p$ hatványparaméter (általában 2) szabályozza, milyen gyorsan csökken a hatás a távolsággal. 8. fejezet.

**IGRAC** (International Groundwater Resources Assessment Centre) — UNESCO/WMO központ Delftben (Hollandia), amely a Globális Felszín Alatti Víz Információs Rendszert (GGIS) tartja fenn — egy webalapú platformot, amely a nemzeti felszín alatti víz adatokat kereshető globális adatbázisba aggregálja. 19. fejezet.

**Infiltration** (beszivárgás) — A víz talajfelszínbe történő belépésének folyamata, amelyet a talaj textúrája, szerkezete, nedvességtartalma és a felszíni lejtés szabályoz. A csapadék beszivárgás és felszíni lefolyás közötti megoszlása a hidrológia egyik legfontosabb számítása. 7., 22. fejezet.

**INSPIRE Directive** (INSPIRE irányelv) — Az Európai Unió irányelve (2007/2/EK), amely az Európai Közösség térbeli információs infrastruktúráját (INSPIRE) hozza létre. Előírja, hogy az EU tagállamok a térbeli adataikat szabványosított webszolgáltatásokon keresztül, közös adatspecifikációk alkalmazásával tegyék közzé. Az INSPIRE biztosítja a környezeti és földrajzi adatok interoperabilitását Európa-szerte. 4. fejezet.

**Interpolation** (interpoláció) — Ismert mintapontokból nem mért helyeken történő értékbecslés folyamata, amely folytonos felszínt eredményez. A fő módszerek közé tartozik a legközelebbi szomszéd (Thiessen-poligonok), a fordított távolsággal súlyozott interpoláció, a spline és a krigelés. 8. fejezet.

**Kalman filter** (Kálmán-szűrő) — Szekvenciális adatasszimilációs módszer, amely a modell-előrejelzéseket és a megfigyeléseket a bizonytalanságaikra épülő optimális súlyozással kombinálja. A Kálmán-szűrő a rendszer állapotát és annak bizonytalanságát tartja fenn, és mindkettőt frissíti, valahányszor új megfigyelés érkezik. 25. fejezet.

**Karst** (karszt) — Oldható kőzetek (mészkő, dolomit, gipsz) oldódásával kialakult felszínforma, amelyet víznyelők, barlangok és földalatti vízhálózat jellemez. A karszt-terep különleges kihívásokat jelent a DEM-kondicionálásban, mert a víznyelők valódi zárt mélyedések, nem műtermékek. A magyarországi Aggteleki-karszt az UNESCO Világörökség része. 9. fejezet.

**KGE (Kling–Gupta Efficiency)** (Kling–Gupta-hatékonyság) — Modellteljesítmény-mutató, amely három komponensre bomlik: korreláció $r$ (időzítési pontosság), torzítási arány $\beta$ (térfogati pontosság) és változékonysági arány $\gamma$ (szóródási pontosság). A 0,0 feletti KGE-értékek azt jelzik, hogy a modell felülmúl egy naiv referenciamodellt. A KGE-t egyre inkább előnyben részesítik az NSE-vel szemben kalibráláskor. 22. fejezet.

**Kriging** (krigelési interpoláció) — Geostatisztikai interpolációs módszer, amely az adatok térbeli korrelációs szerkezetét (variogramon keresztül modellezve) használja az előrejelzéshez optimális súlyok számítására, mind becsléseket, mind előrejelzési bizonytalanságokat szolgáltatva. A krigelés az egyetlen interpolációs módszer, amely kifejezetten modellezi a térbeli függőséget. 8. fejezet.

**KSH (Központi Statisztikai Hivatal)** — Magyarország Központi Statisztikai Hivatala, amely a népszámlálás végrehajtásáért és a demográfiai statisztikák előállításáért felelős. A legutóbbi népszámlálás (2022. évi népszámlálás) 2022 végén zajlott, kombinált online és hagyományos módszertannal. 17. fejezet.

**Land surface model (LSM)** (felszíni modell) — A szárazföldi felszín és a légkör közötti víz- és energiacserét ábrázoló számítási modell. A felszíni modellek a csapadékot beszivárgásra, lefolyásra és evapotranszspirációra osztják szét, és az időjárás-előrejelzési és klímamodellek kulcsfontosságú elemei. A Noah-MP és az ECLand széles körben használt felszíni modellek. 22. fejezet.

**LAS format** (LAS-formátum) — Az Amerikai Fotogrammetriai és Távérzékelési Társaság (ASPRS) által meghatározott szabványos fájlformátum LiDAR-pontfelhő adatok tárolására. Minden pontrekord tartalmazza az x, y, z koordinátákat, az intenzitást, a visszaverődés számát, az osztályozást és egyéb attribútumokat. 13. fejezet.

**LiDAR (Light Detection and Ranging)** — Távérzékelési technológia, amely lézerimpulzusok kibocsátásával és a célobjektumokról való visszaverődés idejének mérésével határozza meg a távolságokat. A légi LiDAR háromdimenziós pontfelhőket állít elő centiméteres vertikális pontossággal, lehetővé téve a részletes árvíztérképezéshez elengedhetetlen nagy felbontású, csupasz talajfelszínű DEM-ek létrehozását. 13. fejezet.

**Linear mode LiDAR** (lineáris módú LiDAR) — A hagyományos LiDAR-technológia, amelyben minden impulzust egyedileg bocsátanak ki, a célról visszaverődik, és egyetlen detektorelem érzékeli, amelynek válasza arányos a bejövő fény intenzitásával. A lineáris módú rendszerek impulzusonként több visszaverődést rögzítenek, és a legtöbb meglévő LiDAR-adat forrásai. 13. fejezet.

**Local operation** (helyi művelet) — Térképi algebrai művelet, amelyben minden kimeneti cellát kizárólag a megfelelő bemeneti cella(k)ból számítanak ki, a szomszédos cellák közötti kölcsönhatás nélkül. Az aritmetikai műveletek (két rács összeadása) helyi műveletek. 6. fejezet.

**LSTM (Long Short-Term Memory)** — Visszacsatolásos neurális hálózat egy típusa, amelyet hosszú távú időbeli függőségek tanulására terveztek, kapuzott cellaarchitektúrával, amely felejtési, bemeneti és kimeneti kapukat tartalmaz. Az LSTM-hálózatok képesek a vízhozamot nem mérőállomásos helyeken is a kalibrált folyamatalapú modellekkel összehasonlítható vagy azokat meghaladó pontossággal előrejelezni. 23. fejezet.

**Manning's equation** (Manning-egyenlet) — Empirikus egyenlet, amely az átlagos áramlási sebességet nyílt mederben a hidraulikus sugárral, a mederlejtéssel és a Manning-féle $n$ érdességi együtthatóval kapcsolja össze. A Manning-egyenlet a nyílt medri hidraulika alapeszköze, és megalapozza a vízhozam-előrejelzések vízmélységekre történő átváltását a HAND-alapú árvízi elöntéstérképezésben. 15. fejezet.

**Map algebra** (térképi algebra) — Dana Tomlin által formalizált számítási keretrendszer, amelyben a raszterrácsokat algebrailag kezeljük: a műveleteket egyidejűleg alkalmazzuk minden cellára. A térképi algebrai műveleteket helyi, környezeti, zonális és globális kategóriába sorolják a számítás térbeli hatóköre alapján. 6. fejezet.

**Map projection** (térképi vetületi rendszer) — Matematikai transzformáció, amely a Föld görbült felszínén lévő helyeket (szélességi és hosszúsági fokokban, ellipszoidon definiálva) sík térképfelszínen lévő helyekké alakítja. A vetületek elkerülhetetlenül torzítják valamelyik tulajdonságot — terület, alak, távolság vagy irány —, és a vetületválasztás befolyásolja a hidrológiai számítások pontosságát. 2. fejezet.

**Mathematical model** (matematikai modell) — Egy koncepcionális modell ábrázolása egyenletekben és szimbólumokban. A vízháztartási egyenlet $P = Q + ET + \Delta S$ a hidrológiai ciklus matematikai modellje. 1. fejezet.

**MBFSZ (Magyar Bányászati és Földtani Szolgálat)** — A korábbi Magyar Bányászati és Földtani Szolgálat, amelyet az SZTFH keretében szerveztek újra. Az MBFSZ tartotta fenn Magyarország országos földtani térképadatbázisát és fúrási nyilvántartásait. 18. fejezet.

**Microsoft Planetary Computer** — Azure-infrastruktúrára épülő felhőalapú térbeli elemzési platform, amely az STAC szabványon keresztül biztosít hozzáférést környezeti adatkészletekhez és JupyterHub környezetet a Python-alapú elemzéshez. A Planetary Computer tárolja a Copernicus DEM-et, a Sentinel műholdképeket, az ERA5 adatokat és sok más, a hidrológia szempontjából releváns adatkészletet. 4. fejezet.

**ModelBuilder** — Az ArcGIS Pro grafikus modellszerkesztője, amely lehetővé teszi a téradat-feldolgozó eszközök automatizált munkafolyamatokba láncolását kódírás nélkül. A ModelBuilder képes a munkafolyamatokat Python-szkriptekké exportálni, hidat képezve az interaktív térinformatikai használat és a szkriptelt automatizálás között. 12. fejezet.

**MODFLOW** — Az USGS által kifejlesztett moduláris véges differencia felszín alatti víz áramlási modell, és a világ legszélesebb körben használt felszín alatti víz szimulációs modellje. A MODFLOW a vízadó réteg-rendszereket háromdimenziós, négyszögletes cellákból álló rácsokra diszkretizálja, és véges differenciák módszerével oldja meg a felszín alatti víz áramlási egyenletét. A legújabb generáció, a MODFLOW 6, nem strukturált rácsokat is támogat. 21–22. fejezet.

**Multipatch** (multipatch) — Térinformatikai geometriatípus, amely háromdimenziós gyűrűkből és háromszögekből áll, és háromdimenziós területet vagy térfogatot elfoglaló objektumokat ábrázol. A felszín alatti víz adatmodellben a multipatch-ek a GeoVolume, GeoSection és Cell3D elemeket képviselik. 18. fejezet.

**Multiple returns** (többszörös visszaverődés) — A lineáris módú LiDAR azon jellemzője, amelyben egyetlen lézerimpulzus több különálló visszaverődést generál különböző magasságú objektumokról — például a lombkoronáról (első visszaverődés), az aljnövényzetről (közbenső visszaverődés) és a talajfelszínről (utolsó visszaverődés). A többszörös visszaverődés lehetővé teszi, hogy a LiDAR erdős területeken is csupasz talajfelszínű DEM-eket állítson elő. 13. fejezet.

**Muskingum routing** (Muskingum-hullámtérterjedés) — Tározás-alapú mederben történő hullámterjedési módszer, amely a folyószakaszból kilépő vízhozamot a bemenő vízhozammal és a szakasz tározásával kapcsolja össze a $K$ (futási idő) és az $x$ (csillapítási súlyozás) paramétereken keresztül. Az amerikai Nemzeti Vízmodell a Muskingum-hullámtérterjedést alkalmazza (a RAPID modellen keresztül) mind a 2,7 millió NHDPlus szakaszra. 16. fejezet.

**Nash–Sutcliffe Efficiency (NSE)** (Nash–Sutcliffe-hatékonyság) — A hidrológiai modellek értékelésének legszélesebb körben alkalmazott teljesítménymutatója, amely a megfigyelt és szimulált értékek közötti négyzetes eltérések összegét veti össze a megfigyelések szórásnégyzetével. NSE = 1,0 a tökéletes egyezés; NSE = 0,0 azt jelenti, hogy a modell nem jobb, mint a megfigyelt átlag előrejelzése. 22. fejezet.

**National Elevation Dataset (NED)** (Nemzeti Szintközmodell) — Az Egyesült Államok országos összefüggő DEM-je, amelyet a USGS állít elő, és amelyet a 3DEP program vált fel. A standard NED-termék 1/3 ívmásodsperces rács (hozzávetőleg 10 méter). 3. fejezet.

**National Water Model (NWM)** (Nemzeti Vízmodell) — Az Egyesült Államok operatív hidrológiai előrejelző rendszere, amely 2,7 millió NHDPlus vízfolyásszakaszra óránkénti vízhozam-előrejelzéseket állít elő. A NWM időjárási modelleket (HRRR, GFS), a Noah-MP felszíni modellt és a RAPID mederben történő hullámterjedési modellt csatolja a NOAA szuperszámítógépes infrastruktúráján. 16. fejezet.

**NHDPlus (National Hydrography Dataset Plus)** (Nemzeti Hidrográfiai Adatbázis Plus) — Az amerikai Nemzeti Vízmodell térinformatikai keretrendszere, amely 2,7 millió, egyedi azonosítóval (COMID) ellátott vízfolyásszakaszt biztosít a megfelelő vízgyűjtőkkel, kapcsolódási táblázatokkal és fizikai attribútumokkal. Az NHDPlus az összekötő kapocs az időjárási adatok, a felszíni modellek és a mederben történő hullámterjedés között az amerikai árvíz-előrejelző rendszerben. 3., 16. fejezet.

**Noah-MP** — A Noah Multi-Physics felszíni modell, amelyet az amerikai Nemzeti Vízmodell és a WRF légköri modell alkalmaz. A Noah-MP a csapadékot lehullási visszatartásra, beszivárgásra, lefolyásra és evapotranszspirációra osztja szét moduláris fizikai opciókkal, 1 km-es rácson, négy talajréteggel és egy felszín alatti víztározóval működve. 16. fejezet.

**NODATA** — Speciális érték egy raszterrácsban, amely azt jelzi, hogy az adott cellához nem tartozik adat — a cella meghatározatlan, nem pedig nulla értékű. A NODATA helyes kezelése kritikus a térképi algebrában: bármely NODATA cellát érintő aritmetikai művelet NODATA-t eredményez a kimenetben. 5. fejezet.

**NSE** — lásd **Nash–Sutcliffe Efficiency**.

**NUTS (Nomenclature of Territorial Units for Statistics)** (Statisztikai Célú Területi Egységek Nómenklatúrája) — Az Európai Unió statisztikai régiók hierarchikus osztályozási rendszere. Magyarország 7 NUTS-2 régióval és 20 NUTS-3 egységgel (19 megye plusz Budapest) rendelkezik. A NUTS régiók az európai demográfiai, gazdasági és környezeti jelentéstétel térbeli keretrendszereként szolgálnak. 17. fejezet.

**Orthometric height** (ortometrikus magasság) — Egy pont geoid feletti magassága, a függőón mentén mérve. Az ortometrikus magasság megfelel annak, amit köznyelven „tengerszint feletti magasságnak" nevezünk. Az ellipszoidmagasságtól (amely a matematikai ellipszoid felett van mérve) a geoidhullám értékével tér el. 2. fejezet.

**Overfitting** (túlillesztés) — A gépi tanulásban az az állapot, amelyben a modell a betanító adatok zaját és sajátosságait tanulja meg az alapvető mintázat helyett, és kiváló betanítási teljesítményt, de gyenge általánosítóképességet eredményez új adatokon. A túlillesztés ellen regularizációval, dropouttal, korai leállítással és megfelelő adatszétosztással védekezünk. 23. fejezet.

**OVF (Országos Vízügyi Főigazgatóság)** — Magyarország Országos Vízügyi Főigazgatósága, amely az országos árvízvédelemért, a vízgazdálkodásért és a hidrográfiai megfigyelőhálózat üzemeltetéséért felelős. Az OVF üzemelteti a HYDROINFO valós idejű vízszintfigyelő rendszert és irányítja az árvíz-előrejelzést a Duna és a Tisza rendszerére. 3., 16. fejezet.

**Particle filter** (részecskeszűrő) — Szekvenciális adatasszimilációs módszer, amely a modell bizonytalanságát súlyozott ensemble-tagokkal (részecskékkel) ábrázolja, a súlyokat a megfigyelésekkel való egyezés alapján rendelve hozzá, majd újramintavételezéssel a valószínű állapotokra koncentrálva a számítási kapacitást. A részecskeszűrők erősen nemlineáris rendszereket kezelnek. 25. fejezet.

**PEST** (Parameter ESTimation) — Modell-független paraméter-becslő és bizonytalanság-elemző szoftvercsomag, amelyet John Doherty fejlesztett. A PEST regularizált inverziót alkalmaz térben elosztott paraméterekkel rendelkező modellek kalibrálásához, és a MODFLOW-kalibráció standard eszközévé vált pilótapont-módszerek alkalmazásával. 22. fejezet.

**Pit** (mélypont) — Cella vagy cellacsoport a DEM-ben, amelyet minden oldalról magasabb terep vesz körül, és nincs lefelé irányuló szomszédja a lefolyás befogadására. A mélypontok lehetnek DEM-műtermékek (mérési hibák vagy adatfeldolgozás miatt) vagy valódi topográfiai elemek (víznyelők, üstmélyedések). A műtermék-mélypontok eltávolítása a DEM-kondicionálás fő feladata. 9. fejezet.

**Point cloud** (pontfelhő) — A LiDAR-felmérés nyers kimenete: millió–milliárd egyedi háromdimenziós mérés (x, y, z plusz intenzitás, visszaverődési szám és osztályozás) gyűjteménye, LAS vagy LAZ formátumban tárolva. A pontfelhőket rácsos DEM-ekké osztályozással (talaj és nem-talaj) és interpolációval dolgozzák fel. 13. fejezet.

**PointZ, PolylineZ, PolygonZ** — Z-értékkel rendelkező geometriatípusok a geoadatbázisban, amelyek minden csúcspontjukon vertikális koordinátát (z értéket) hordoznak, lehetővé téve az elemek háromdimenziós térben való létezését. A PointZ elemek fúrási kontaktusokat, a PolylineZ elemek fúrási útvonalakat, a PolygonZ elemek pedig felszíneket definiálnak háromdimenziósban. 18. fejezet.

**Pour point** (kifolyási pont) — A DEM-ben lévő mélypont peremének legalacsonyabb cellája — az a pont, ahol a víz először túlfolyik, ha a mélypontot lassan feltöltjük. A vízgyűjtő-lehatárolásban a kifolyási pont az a helyzet is, ahonnan a felső hozzájáruló területet visszafelé nyomkövetik. 9., 11. fejezet.

**PRISM** (Parameter-elevation Regressions on Independent Slopes Model) — Éghajlat-térképező rendszer, amely nagy felbontású, rácsos csapadék- és hőmérséklet-becsléseket állít elő a fiziográfiai változókkal (tengerszint feletti magasság, lejtésorientáció, tengerpart-közelség) való regressziós összefüggések segítségével. A PRISM az Egyesült Államok szabványos rácsos éghajlati terméke. 8. fejezet.

**Processing Graphical Modeler** (Feldolgozó Grafikus Modellszerkesztő) — A QGIS megfelelője az ArcGIS ModelBuilder-ének, amely lehetővé teszi a téradat-feldolgozó eszközök automatizált munkafolyamatokba láncolását vizuális „fogd és csatlakoztasd" felületen. A Grafikus Modellszerkesztő a munkafolyamatokat Python-szkriptekké is exportálhatja. 12. fejezet.

**QGIS** — A vezető nyílt forráskódú asztali térinformatikai platform, amelyet globális közösség fejleszt a GNU General Public License keretében. A QGIS átfogó vektor- és raszter-elemzést, bővítményökoszisztémát — beleértve a hidrológiai eszközöket (GRASS, SAGA, WhiteboxTools) — és Python-szkriptelést kínál a PyQGIS-en keresztül. 4. fejezet.

**RAPID** (Routing Application for Parallel computatIon of Discharge) — Az amerikai Nemzeti Vízmodellben alkalmazott mederben történő hullámterjedési modell, amely Muskingum-hullámterjedési séma alkalmazásával vezeti a vizet 2,7 millió NHDPlus szakaszon. A RAPID masszív párhuzamosításra készült: a hálózatot több ezer mag egyidejű feldolgozásához bontja szét. 16. fejezet.

**Raster** (raszter) — Térbeli adatmodell, amely a földrajzi teret azonos méretű négyzet alakú cellák szabályos hálójára osztja, ahol minden cella egyetlen számértéket tárol. A raszterrácsok a domináns adatstruktúra a terepanalízis, a csapadékmezők, a felszínborítás és gyakorlatilag minden folytonos térbeli jelenség számára a hidrológiában. 5–6. fejezet.

**Raster Calculator** (raszterkalkulátor) — Térinformatikai eszköz térképi algebrai műveletek végrehajtásához, amely a bemeneti raszterrétegekre hivatkozó algebrai kifejezéseket celláról cellára kiértékelve kimeneti rasztert állít elő. Az ArcGIS Pro-ban (Spatial Analyst) és a QGIS-ben (Processing) egyaránt elérhető. 6. fejezet.

**Rating curve** (vízállás–vízhozam görbe) — Matematikai összefüggés a vízszint (mélység vagy szint) és a vízhozam között egy adott vízfolyásszelvényben. A HAND-alapú árvíztérképezésben szintetikus vízállás–vízhozam görbéket származtatnak az egyes szakaszok terepgeometriájából, lehetővé téve a vízhozam-előrejelzések vízmélységekre való átváltását felmért keresztszelvények nélkül. 15. fejezet.

**Reach** (vízfolyásszakasz) — A vízfolyáshálózat egy folytonos szegmense két csomópont között, amelyet a vízfolyás-szegmentálás során határoznak meg. Minden szakasz egyedi azonosítóval és hozzárendelt vízgyűjtővel rendelkezik. Az NHDPlus keretrendszer 2,7 millió szakaszt definiál az Egyesült Államok területén. 11. fejezet.

**Resampling** (újramintavételezés) — A cellaértékek újraszámításának folyamata, amikor egy rasztert más cellaméretre, kiterjedésre vagy koordináta-rendszerre transzformálnak. A gyakori módszerek közé tartozik a legközelebbi szomszéd (megőrzi az eredeti értékeket), a bilineáris interpoláció (a négy legközelebbi cella súlyozott átlaga) és a köbös konvolúció (tizenhat cella súlyozott átlaga). 6. fejezet.

**SCS Curve Number method** — lásd **Curve number**.

**Semi-major axis** (fél-nagytengely) — Az ellipszoid egyenlítői sugara, jelölése $a$. A Föld esetében $a \approx 6\,378\,137$ méter. 2. fejezet.

**Sentinel-2** — A Copernicus program európai multispektrális képalkotó missziója, amely globális felszíni képalkotást biztosít 10–60 méteres felbontásban, 5 napos visszatérési idővel. A Sentinel-2 adatai szabadon hozzáférhetők, és széles körben alkalmazzák víztest-térképezésre, felszínborítás-osztályozásra és növényzet-monitorozásra. 3. fejezet.

**Slope** (lejtésszög, meredekség) — A magasság vízszintes távolsághoz viszonyított változásának mértéke — matematikailag a magassági felszín gradiensének nagysága. A lejtés szabályozza a felszíni lefolyás sebességét, az eróziós potenciált, a beszivárgási időt és a talajnedvesség eloszlását. Százalékos emelkedésben vagy fokban fejezhető ki. 7. fejezet.

**SoilGrids** — Globális rácsos talajtulajdonság-adatkészlet 250 méteres felbontásban, amely a talajtextúrára, a szerves szénre, a térfogattömegre, a pH-ra és más tulajdonságokra ad becslést több mélységi intervallumra. A SoilGrids a részletes nemzeti talajfelmérésekkel nem rendelkező régiók elsődleges talajadatforrása. 3. fejezet.

**Spatial interpolation** (térbeli interpoláció) — Ismert mintapontokból nem mért helyeken értékek becslésének folyamata, amely folytonos raszterfelszínt eredményez. A fő módszerek közé tartozik a legközelebbi szomszéd, a fordított távolsággal súlyozott interpoláció, a spline és a krigelés, amelyek mindegyike eltérő feltevéseket tartalmaz a térbeli folytonosságról. 8. fejezet.

**SRTM (Shuttle Radar Topography Mission)** — NASA/NGA misszió, amely 2000 februárjában interferometrikus szintetikus apertúrájú radar segítségével térképezte a Föld felszínét 60°É és 56°D között. Az SRTM készítette az első közel-globális DEM-et, amely szabadon hozzáférhető 30 méteres (1 ívmásodperces) felbontásban. Ma is széles körben alkalmazzák nagyszabású hidrológiai elemzésekhez. 3. fejezet.

**Strahler stream order** (Strahler-féle vízfolyásrend) — Hierarchikus rendszám-rendszer a vízfolyáshálózatokhoz, amelyben a legkisebb forráságak az 1. rendűek, két 1. rendű vízfolyás összefolyása 2. rendű vízfolyást eredményez, és általában két azonos $n$ rendű vízfolyás összefolyása $n+1$ rendű vízfolyást hoz létre. A Strahler-rendszám a vízfolyások relatív méretét számszerűsíti a hálózaton belül. 11. fejezet.

**Stream burning** (vízfolyás-beégetés) — DEM-kondicionálási technika, amely lealacsonyítja a cellák magasságát a térképezett vízfolyáshálózat mentén, hogy a DEM-ből származtatott folyásutak az ismert medervonalakat kövessék. A vízfolyás-beégetés az AGREE módszer egyszerűbb alternatívája. 9. fejezet.

**Stream definition** (vízfolyás-meghatározás) — A folyamat, amelynek során az összegyülekezési rácsban a cellákat vízfolyásra vagy nem-vízfolyásra osztályozzák egy küszöbérték alkalmazásával. A küszöbértéknél nagyobb felhalmozott felső területtel rendelkező cellákat medernek minősítik. A küszöbérték megválasztása határozza meg a vízfolyáshálózat sűrűségét. 11. fejezet.

**Stream segmentation** (vízfolyás-szegmentálás) — Az összefüggő vízfolyásraszter egyedi szakaszokra történő felosztásának folyamata a csomópontoknál, amelynek eredményeként egyedi azonosítóval rendelkező diszkrét szegmensek keletkeznek. Minden szegmens egy vízgyűjtő alapjává válik a vízgyűjtő-lehatárolásban. 11. fejezet.

**Support area** (támogató terület) — A felső vízgyűjtő terület minimális mérete ahhoz, hogy egy cellát vízfolyásmedernek minősítsenek; a csatornásodási küszöbnek is nevezik. A támogató terület határozza meg a származtatott vízfolyáshálózat sűrűségét és a domboldali és a medri folyamatok közötti felosztást. 11. fejezet.

**SWAT (Soil and Water Assessment Tool)** — A világ legszélesebb körben használt félig elosztott hidrológiai modellje, amelyet az USDA Mezőgazdasági Kutatási Szolgálata (Agricultural Research Service) fejlesztett. A SWAT a vízgyűjtőket alvízgyűjtőkre osztja, amelyek a felszínborítás, a talajtípus és a lejtőosztály egyedi kombinációiból definiált hidrológiai válaszegységeket (HRU) tartalmaznak. 22. fejezet.

**SZTFH (Szabályozott Tevékenységek Felügyeleti Hatósága)** — Magyarország Szabályozott Tevékenységek Felügyeleti Hatósága, amely magába olvasztotta a korábbi Magyar Bányászati és Földtani Szolgálatot (MBFSZ). Az SZTFH kezeli az országos földtani térképadatbázist, a fúrási nyilvántartásokat és a map.mbfsz.gov.hu címen elérhető hidrogeológiai térképeket. 19. fejezet.

**TauDEM (Terrain Analysis Using Digital Elevation Models)** — David Tarboton által fejlesztett nyílt forráskódú terepanalízis eszközcsomag, amely a D8, a D-végtelen és az általánosított felhalmozási algoritmusokat valósítja meg párhuzamos számítási támogatással. A TauDEM az ArcGIS-be is integrálva van, és széles körben alkalmazzák vízgyűjtő-lehatároláshoz és HAND-számításhoz. 7., 10. fejezet.

**Thiessen polygons** (Thiessen-poligonok) — Más néven Voronoi-poligonok vagy Dirichlet-tesszelláció. Egy sík geometriai felosztása, amelyben minden poligon tartalmazza azokat a pontokat, amelyek a hozzá tartozó mintaponthoz közelebb vannak, mint bármely más mintaponthoz. A hidrológiában a csapadékmérő hálózatok területsúlyozott átlagolásához használják. 8. fejezet.

**TIN (Triangulated Irregular Network)** (TIN, szabálytalan háromszögháló) — Felszínábrázolás, amely szabálytalanul elhelyezkedő pontokat nem átfedő háromszögekből álló hálóvá kapcsol össze. A TIN-ek tárolási szempontból hatékonyak a terepábrázolásban, mert a háromszögek a nagy topográfiai összetettségű területekre koncentrálhatók. A szabályos rácsokhoz képest azonban ritkábban alkalmazzák a hidrológiában az algoritmikus komplexitás miatt. 5. fejezet.

**Topographic wetness index (TWI)** (topográfiai nedvességi index) — Terepattribútum, amelyet $\ln(a / \tan \beta)$ képlettel definiálnak, ahol $a$ a felső hozzájáruló terület egységnyi szintvonalhosszra vetítve és $\beta$ a helyi lejtésszög. A magas TWI-értékek nagy hozzájáruló területtel és enyhe lejtéssel rendelkező területeket jelölnek, amelyek várhatóan leggyakrabban telítettek. A TWI a TOPMODEL hidrológiai modellek családjának alapja. 7. fejezet.

**Transfer learning** (transzfertanulás) — Gépi tanulási technika, amelyben egy adatkészleten vagy feladaton betanított modellt egy másik, de rokon adatkészletre vagy feladatra alkalmaznak. A hidrológiában a transzfertanulás lehetővé teszi, hogy adatgazdag vízgyűjtőkön betanított LSTM-modellek nem mért helyszíneken is előrejelzéseket adjanak. 23. fejezet.

**Upscaling problem** (felskálázási probléma) — Az egyedi mérési ponton mérhető tulajdonságok és a modellek által igényelt rácsméretű effektív paraméterek közötti eltérés. Például a 10 cm-es talajmintán mért telített hidraulikus vezetőképesség alapvetően különbözik az 1 km-es modelrácscellához szükséges effektív értéktől. 22. fejezet.

**Vector** (vektor) — Térbeli adatmodell, amely földrajzi elemeket diszkrét geometriai objektumokként ábrázol: pontok (kutak, mérőállomások), vonalak (vízfolyások, utak) és poligonok (vízgyűjtők, vízadó réteg-határok). A vektorelemek geometriát és attribútumadatokat egyaránt hordoznak. 4. fejezet.

**Voronoi polygons** (Voronoi-poligonok) — lásd **Thiessen polygons**.

**Water balance** (vízháztartás, vízmérleg) — Az alapvető hidrológiai egyenlet, amely kimondja, hogy a csapadék egyenlő az evapotranszspiráció, a lefolyás és a tározásváltozás összegével: $P = ET + R + \Delta S$. A vízháztartási egyenletet minden léptéken alkalmazzák az egyedi celláktól (térképi algebra révén) a teljes kontinensekig. 1., 6. fejezet.

**Water Framework Directive (WFD)** (Víz Keretirányelv) — Az Európai Unió irányelve (2000/60/EK), amely az európai vizek — beleértve a felszíni vizeket, a felszín alatti vizeket, a torkolatokat és a parti vizeket — kezelésének és védelmének keretrendszerét hozza létre. A VKI azt a célt tűzte ki, hogy minden víztest érje el a „jó ökológiai állapotot", és előírja a tagállamok számára a felszín alatti víztestek lehatárolását és monitorozását. 3., 19. fejezet.

**Watershed** (vízgyűjtő terület) — Az a földterület, amelyről az összes felszíni lefolyás egy közös kifolyási pontra gyűlik össze. A DEM-ekből történő vízgyűjtő-lehatárolás a számítási hidrológia legalapvetőbb térbeli művelete, amelyet a kijelölt kifolyási ponttól a folyásirányok visszafelé történő nyomkövetésével végeznek. Összegyűjtési terület vagy lefolyási medence néven is ismert. 11. fejezet.

**Well** (kút) — Ember alkotta mélyedés vagy létesítmény a talajban, amelyet felszín alatti víz kinyerésére, besajtolására vagy megfigyelésére hoztak létre. A kutakat a térinformatikában pontelemekként ábrázolják a mélység, a vízadó réteg-hozzárendelés, a szivattyúzási hozam és a vízminőség attribútumaival. 19. fejezet.

**WGS84 (World Geodetic System 1984)** (Világ Geodéziai Rendszer 1984) — A GPS rendszer által használt globális geocentrikus dátum, amelyet az Egyesült Államok Nemzeti Térinformatikai-hírszerző Ügynöksége (NGA) tart fenn. A WGS84 a műholdas koordinátaadatok de facto globális szabványa, és gyakorlati célokra szinte azonos az ETRS89-cel. 2. fejezet.

**WHYMAP** (World-wide Hydrogeological Mapping and Assessment Programme) — Németország BGR és az UNESCO koordinálásával működő globális kezdeményezés egységes világszintű vízadó réteg-térképek előállítására, beleértve a Világ Felszín Alatti Vízkészlet-térképét és a Határon Átnyúló Vízadó Rétegek Térképét. 19. fejezet.

**WorldPop** — Globális rácsos népesség-adatkészlet hozzávetőleg 100 méteres felbontásban, amelyet a Southamptoni Egyetem készít. A WorldPop a műholdas képekre, települési adatokra és népszámlálási számokra alkalmazott gépi tanulás segítségével becsüli a népesség térbeli eloszlását, nagy felbontású népesség-adatokat nyújtva a korlátozott népszámlálási infrastruktúrával rendelkező országok számára. 17. fejezet.

**Zonal operation** (zonális művelet) — Térképi algebrai művelet, amely egyetlen összefoglaló értéket (átlag, maximum, összeg stb.) számít minden egyes azonos zónaazonosítóval rendelkező cellacsoport számára. Klasszikus példa az egyes vízgyűjtő-poligonok átlagos magasságának kiszámítása. 6. fejezet.

---

**Blöschl's scale triplet** (Blöschl-féle skálahármas) — Fogalmi keretrendszer a térbeli adatok és folyamatok jellemzésére három dimenzió mentén: kiterjedés (a lefedett teljes terület), lépésköz (a megfigyelések vagy rácscellák közötti távolság) és alátámasztás (az a terület vagy térfogat, amelyre az egyes mérések integrálnak). A skálahármas elengedhetetlen annak értékeléséhez, hogy egy adatkészlet megfelelő-e egy adott elemzési célra. 5. fejezet.

**Cell3D** — (AHGW) Multipatch-objektumosztály az Arc Hydro Groundwater adatmodellben, amely egy szimulációs modellrács háromdimenziós celláit és elemeit ábrázolja. A Cell3D elemek az egyes modellcellák teljes térfogati geometriáját tárolják. 21. fejezet.

**Clausius–Clapeyron relation** (Clausius–Clapeyron-összefüggés) — A termodinamikai összefüggés, amely kimondja, hogy a víz telítési gőznyomása Celsius-fokonként hozzávetőleg hét százalékkal növekszik. Ez az összefüggés magyarázza, miért okoz a melegebb légkör intenzívebb csapadékeseményeket, és miért súlyosbodik egyidejűleg az árvíz és az aszály. 1. fejezet.

**CUAHSI** (Consortium of Universities for the Advancement of Hydrologic Science, Inc.) — Egyesült Államok-beli egyetemi konzorcium, amely közös infrastruktúrát fejleszt és üzemeltet a hidrológiai kutatás számára, beleértve a Hydrologic Information System-et (HIS) és a HydroShare platformot. 1. fejezet.

**Darcy's law** (Darcy-törvény) — A felszín alatti víz áramlás alapvető egyenlete, amely a porózus közegen áthaladó térfogati áramlási sebességet a hidraulikus gradienshez és a hidraulikus vezetőképességhez kapcsolja: $Q = -KA(dh/dl)$, ahol $K$ a hidraulikus vezetőképesség, $A$ a keresztmetszeti terület és $dh/dl$ a hidraulikus gradiens. 21. fejezet.

**Destination Earth (DestinE)** (Célföld) — Az Európai Bizottság 2024-ben indított kezdeményezése, amelynek célja a teljes Föld-rendszer nagy felbontású digitális másolatának megépítése európai szuperszámítógépes infrastruktúrán, 2030-ra tervezett teljes operatív képességgel. A DestinE a vízkörforgás digitális ikreit is tartalmazza példátlan felbontásban. 25. fejezet.

**Dropout** (dropout) — Regularizációs technika a neurális hálózatok betanításában, amelyben véletlenszerűen kiválasztott neuronokat ideiglenesen eltávolítanak minden betanítási lépésben, ezzel kényszerítve a hálózatot redundáns reprezentációk megtanulására és csökkentve a túlillesztést. A hidrológiai LSTM-modelleknél a tipikus dropout arány 0,1–0,3. 23. fejezet.

**ECMWF (European Centre for Medium-Range Weather Forecasts)** (Középtávú Időjárás-előrejelzés Európai Központja) — Kormányközi szervezet, amely a világ legfejlettebb időjárás-előrejelző rendszereit üzemelteti. Az ECMWF készíti az ERA5 reanalízist, üzemelteti az EFAS árvíz-előrejelző rendszert, és fejleszti az ECLand felszíni modellt. 3., 16., 25. fejezet.

**EGM2008** (Earth Gravitational Model 2008) — Globális geoidmodell, amely a geoid-magasságot (a geoid és a vonatkoztatási ellipszoid közötti eltérést) hozzávetőleg 5 km-es felbontású rácson biztosítja. Az EGM2008 szolgál vertikális dátumként a Copernicus DEM és számos más globális domborzati termék számára. 2. fejezet.

**Encoder-decoder architecture** (kódoló-dekódoló architektúra) — Neurális hálózat terv, amelyben az egyik hálózat (kódoló) egy bemeneti sorozatot rögzített hosszúságú reprezentációba tömörít, a másik hálózat (dekódoló) pedig ebből a reprezentációból kimeneti sorozatot generál. Az LSTM árvíz-előrejelzésben többlépéses előrejelzésekhez használják. 23. fejezet.

**Ensemble forecast** (ensemble-előrejelzés) — Előrejelzési megközelítés, amely több szimulációt futtat kissé eltérő kezdeti feltételekkel, modellparaméterekkel vagy meghajtó adatokkal az előrejelzési bizonytalanság számszerűsítésére. Az EFAS ensemble árvíz-előrejelzéseket készít; az EnKF ensemble-eket alkalmaz az adatasszimilációhoz. 16., 25. fejezet.

**Floodplain** (ártér) — A folyómeder melletti viszonylag lapos terület, amelyet rendszeresen elönt a magas vízhozamú események során. Az ártér kiterjedése szorosan korrelál a HAND-értékekkel; az alacsony HAND-értékű cellák az ártéren belül helyezkednek el. 14. fejezet.

**Full waveform LiDAR** (teljes hullámformájú LiDAR) — LiDAR-technológia, amely a visszavert jel teljes időbeli lefolyását rögzíti, nem csupán a diszkrét csúcsokat. A teljes hullámformájú adatok információt tartalmaznak a visszaverő felszínek függőleges eloszlásáról, javítva a talajfelszín-detektálást sűrű növényzet alatt. 13. fejezet.

**Geiger-mode LiDAR** (Geiger-módú LiDAR) — Fejlett LiDAR-technológia, amely egyes fotonokra érzékeny detektorokat használ, amelyek képesek a célról visszatérő egyedi fotonok regisztrálására. A Geiger-módú rendszerek lényegesen nagyobb pontsűrűséget és szélesebb pásztaszélességet érnek el, mint a hagyományos lineáris módú rendszerek azonos magasságból, gyorsabb és költséghatékonyabb országos térképezési programokat téve lehetővé. 13. fejezet.

**GeoPackage** — Nyílt, szabványokon alapuló, platformfüggetlen geoadat-formátum, amelyet az Open Geospatial Consortium definiált. A GeoPackage az SQLite-ot használja konténerként, és a QGIS natív térbeli adatformátumaként szolgál. 4. fejezet.

**Global operation** (globális művelet) — Térképi algebrai művelet, amelyben minden kimeneti cellát a bemeneti rács összes cellájának felhasználásával számítanak ki. A távolságszámítás és a költségfelszín-elemzés a globális műveletek példái. 6. fejezet.

**Hydraulic conductivity** (hidraulikus vezetőképesség) — A porózus közeg azon képességének mértéke, amellyel hidraulikus gradiens hatására vizet képes átengedni; mértékegysége hossz/idő (m/s vagy m/nap). A hidraulikus vezetőképesség a közeg tulajdonságaitól (szemcseméret, porozitás, kapcsoltság) és a folyadék tulajdonságaitól (viszkozitás, sűrűség) egyaránt függ. A felszín alatti víz modellezés egyik legfontosabb paramétere. 21. fejezet.

**Hydrologic Response Unit (HRU)** (hidrológiai válaszegység) — Térbeli egység a félig elosztott hidrológiai modellekben (különösen a SWAT-ban), amelyet a felszínborítás, a talajtípus és a lejtőosztály egyedi kombinációja definiál. A HRU-k az alapvető számítási elemek, amelyekre a folyamategyenleteket alkalmazzák. 22. fejezet.

**HYDROINFO** — Magyarország valós idejű vízszintfigyelő rendszere, amelyet az OVF üzemeltet, és a hydroinfo.hu címen érhető el. A HYDROINFO vízszinteket, vízhozam-adatokat és előrejelzéseket jelenít meg 98 folyószakaszra, és az elsődleges nyilvános árvíz-információs portálként szolgál Magyarország számára. 16. fejezet.

**IMU (Inertial Measurement Unit)** (inerciamérő egység) — Gyorsulásmérőket és giroszkópokat tartalmazó eszköz, amely a légi LiDAR-rendszer irányultságát és rövid távú helyzetváltozásait 200 Hz-en vagy annál gyakrabban követi nyomon. Az IMU a GPS-szel integrálva Kálmán-szűrőn keresztül lehetővé teszi az egyes lézerimpulzusok pontos helymeghatározását. 13. fejezet.

**JRC (Joint Research Centre)** (Közös Kutatóközpont) — Az Európai Bizottság tudományos és tudásszolgálata, székhelye Ispra (Olaszország). A JRC fejlesztette az EFAS-t, készíti az Európai Aszályfigyelő Rendszert, és hozta létre a JRC Global Surface Water adatkészletet, amely 1984-től napjainkig térképezi a felszíni víz dinamikáját. 1., 14. fejezet.

**LandScan** — Globális népesség-eloszlási adatkészlet hozzávetőleg 1 km-es felbontásban, amelyet az Oak Ridge National Laboratory készít. A LandScan az ambient (24 órás átlagos) népesség-eloszlást becsüli, és a globális árvízkockázati tanulmányok kitettségbecsléseihez alkalmazzák. 17. fejezet.

**LISFLOOD** — Az Európai Árvíz-figyelmeztető Rendszer (EFAS) által alkalmazott elosztott hidrológiai modell, amelyet a JRC fejlesztett. A LISFLOOD a csapadék-lefolyási folyamatokat és a mederben történő hullámterjedést szimulálja az egész európai kontinensen 5 km-es felbontásban. 16. fejezet.

**Lookback window** (visszatekintési ablak) — Az LSTM és más visszacsatolásos neurális hálózati modellekben az előző időlépések száma, amelyet bemenetként adnak a modellnek minden egyes előrejelzési lépésnél. Árvíz-előrejelzésnél a jellemző 30–60 napos visszatekintési ablak mind a gyors felszíni választ, mind a lassú alapvízhozam-dinamikát megragadja. 23. fejezet.

**MERIT DEM** (Multi-Error-Removed Improved-Terrain DEM) — Globális domborzati adatkészlet 3 ívmásodperces (hozzávetőleg 90 m-es) felbontásban, amelyet az SRTM és az AW3D adatokból több hibakomponens (csíkzaj, szemcsézettség, abszolút eltérés, lombkoronamagasság) eltávolításával hoztak létre. A MERIT jobb hidrológiai elemzést biztosít a nyers SRTM-hez képest. 3. fejezet.

**MODFLOW Analyst** — Az Arc Hydro Groundwater eszközcsomag részeként fejlesztett ArcGIS eszközcsomag, amelyet MODFLOW modellek Arc Hydro Groundwater és MODFLOW adatmodelleken keresztül történő felépítéséhez és kezeléséhez használnak. 21. fejezet.

**Node2D and Node3D** (Node2D és Node3D) — (AHGW) Pont-objektumosztályok az Arc Hydro Groundwater adatmodellben, amelyek 2D és 3D szimulációs modellrácsok számítási csomópontjait ábrázolják. A Node3D elemek Z-értékkel rendelkeznek. 21. fejezet.

**Orographic precipitation** (orografikus csapadék) — A domborzat által felfelé kényszerített légtömegek által okozott csapadék, amely fokozott csapadékot eredményez a szélnek kitett lejtőkön és csökkent csapadékot (esőárnyékot) a szél elöl védett lejtőkön. Az orografikus hatások szisztematikus térbeli mintázatokat hoznak létre, amelyeket az egyszerű távolságalapú interpolációs módszerek nem képesek megragadni. 8. fejezet.

**Pannonian Basin** (Pannon-medence) — A nagy üledékes medence, amely Magyarország területének nagy részét és a szomszédos országok egyes területeit foglalja magában, és több kilométer vastagságú neogén és negyedidőszaki üledékkel van kitöltve. A Pannon-medence több egymásra települt vízadó rendszert tartalmaz, beleértve a sekély alluviális vízadó rétegeket és a Magyarország híres termálfürdőit tápláló mély termálvíz-tartó képződményeket. 18–19. fejezet.

**PBIAS (Percent Bias)** (százalékos torzítás) — Modellteljesítmény-mutató, amely a szimulált értékek megfigyelt értékekhez képesti átlagos eltérési tendenciáját méri, százalékban kifejezve. PBIAS = 0% jelzi a szisztematikus torzítás hiányát. A PBIAS érzékeny a térfogati hibákra, de érzéketlen az időzítési hibákra. 22. fejezet.

**Sensitivity analysis** (érzékenységelemzés) — A modellkimenetek modellparaméter-változásokra adott válaszának szisztematikus vizsgálata. Az érzékenységelemzés azonosítja azokat a paramétereket, amelyeknek a legnagyobb hatásuk van a modell teljesítményére, és irányítja a kalibrálási erőfeszítések elosztását. 22. fejezet.

**Shapefile** — Az Esri által kifejlesztett, széles körben használt vektoros adatformátum, amely legalább három fájlból áll (.shp, .shx, .dbf), amelyek együtt tárolják a geometriát és az attribútumokat. Korlátai (2 GB fájlméret-korlát, 10 karakteres mezőnevek, nincs beépített koordináta-rendszer-érvényesítés) ellenére a shapefile továbbra is a leggyakoribb adatcsere-formátum a térinformatikában. 4. fejezet.

**Spline interpolation** (spline-interpoláció) — Térbeli interpolációs módszer, amely sima matematikai felszínt illeszt a mintapontokra az összfelszíni görbület minimalizálásával. A spline-interpoláció sima felszíneket állít elő, amelyek alkalmasak enyhén változó jelenségekhez, de a szélsőértékek környezetében irreális oszcillációkat (túllövéseket) eredményezhet. 8. fejezet.

**Subsurface Analyst** — Az Arc Hydro Groundwater eszközcsomag részeként fejlesztett ArcGIS eszközkészlet 2D és 3D hidrogeológiai adatok létrehozásához, szerkesztéséhez és kezeléséhez az ArcGIS-en belül, beleértve a fúrás-megjelenítést, a szelvényszerkesztést és a felszíninterpolációt. 18. fejezet.

**TimeSeries table** (TimeSeries tábla) — (AHGW) Tábla az Arc Hydro adatmodellben egyváltozós idősor-adatok tárolására, háromdimenziós struktúrát megvalósítva, amelyet hely (objektum), idő (TsTime) és változó (VarID) indexel. 19. fejezet.

**Transmissivity** (transzmisszivitás) — A vízadó réteg teljes vastagságának vízáteresztő képességét mérő paraméter, amely a hidraulikus vezetőképesség és a vízadó réteg vastagságának szorzata ($T = Kb$), mértékegysége terület/idő (m²/nap). A transzmisszivitás az a paraméter, amelyet közvetlenül a próbaszivattyúzásokból becsülnek. 21. fejezet.

**Universal Soil Loss Equation (USLE)** (Egyetemes Talajvesztési Egyenlet) — Empirikus egyenlet, amely a hosszú távú átlagos talajeróziót a csapadék erozivitásának, a talaj erodibilitásának, a lejtőhossz-tényezőnek, a felszínborítás-kezelési tényezőnek és a talajvédelmi gyakorlati tényezőnek a szorzataként becsüli. Az USLE lejtőhossz-tényezője miatt a talajveszteség hozzávetőleg a lejtésmeredekség négyzetével arányosan növekszik. 7. fejezet.

**Variogram** (variogram) — Egy változó térbeli korrelációjának távolsággal való változását leíró függvény, amelyet a krigelési interpolációban használnak. A variogram számszerűsíti azt az elvet, hogy a közeli értékek hasonlóbbak a távoli értékeknél, és paraméterei (nugget, küszöb, hatótáv) szabályozzák az interpoláció viselkedését. 8. fejezet.

**Water quality** (vízminőség) — A víz fizikai, kémiai és biológiai jellemzői, amelyek meghatározzák alkalmasságát adott felhasználásra. A vízminőségi aggályok közé tartozik a tápanyagszennyezés, a szennyezés, a sótartalom, a hőmérséklet és az oldott oxigén. Az EU Víz Keretirányelv „jó ökológiai állapotot" ír elő minden víztest számára. 1. fejezet.

*Ez a szójegyzék 225 bejegyzést tartalmaz a könyv hat fő szakterületét felölelve: térinformatikai alapok, geodézia, felszíni hidrológia, felszín alatti víz, MI/gépi tanulás és adatrendszerek. A kifejezések szükség szerint kereszthivatkozásokkal vannak ellátva. További Arc Hydro Groundwater adatmodell-elemek definícióihoz lásd a Strassberg, Jones és Maidment (2011) Arc Hydro Groundwater: GIS for Hydrogeology című munka szójegyzékét.*
