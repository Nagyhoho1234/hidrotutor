# B. Függelék: Feladatok

Ez a függelék a *Hidroinformatika 2026* tankönyv valamennyi fejezetéhez tartalmaz feladatokat. A feladatok David R. Maidment és David G. Tarboton eredeti kurzusanyagaiból (University of Texas at Austin, Utah State University) származnak, kiegészítve a könyv nemzetközi szemléletét és a 2026-os fejlesztéseket tükröző új feladatokkal.

Minden feladat nehézségi szinttel van megjelölve:

- **Alap** -- Visszaidézés és megértés; minden olvasó számára alkalmas.
- **Középhaladó** -- Alkalmazás és elemzés; GIS-szoftvert vagy közepes számítási ismereteket igényel.
- **Haladó** -- Szintézis és értékelés; nyílt végű vagy kutatás-orientált feladatok.

A számítási feladatoknál a várt eredményeket a feladat végén *dőlt betűvel* közöljük.

---

## I. rész: Alapok (1--4. fejezet)

### 1. fejezet feladatai: Miért fontos a hidroinformatika?

1. **(Alap)** Fogalmazza meg saját szavaival, mi a hidroinformatika. Miben különbözik a hagyományos hidrológiától, és miben a puszta térinformatikai elemzéstől? Adjon meg legalább három konkrét példát olyan problémákra, amelyek egyszerre igényelnek hidrológiai tudást és térinformatikai technológiát.

2. **(Alap)** Az eredeti Maidment-kurzus a „GIS in Water Resources" címet viselte. Miért használja helyette ez a könyv a „hidroinformatika" kifejezést? Milyen dimenziókat fed le az újabb fogalom, amelyeket a régebbi cím nem?

3. **(Középhaladó)** Válasszon egy ismert vízgyűjtőt (Duna, Tisza, Nílus, Mekong, Colorado vagy bármely más). Sorolja fel, milyen adatforrásokra lenne szükség egy hidroinformatikai tanulmányhoz: topográfiai adatok, vízrajzi hálózat, területhasználat, csapadék, vízhozam-megfigyelések, előrejelző rendszerek. Minden adattípushoz határozza meg, létezik-e nemzeti vagy globális adatbázis, és nevezze meg azt. Hasonlítsa össze listáját az Egyesült Államokban elérhető adatbázisokkal (NHDPlus, NED, NLCD, USGS NWIS, National Water Model).

4. **(Középhaladó)** A könyv leírja, hogyan mutatta meg a Harvey hurrikán (2017) hogy a valós idejű árvíz-előrejelzést össze kell kapcsolni a térinformatikai adatokkal. Keressen egy hasonló árvízkatasztrófát az Egyesült Államokon kívül (pl. a 2013-as dunai árvíz Közép-Európában, a 2021-es Ahr-völgyi árvíz Németországban vagy a 2010-es pakisztáni árvíz). Írjon egyoldalas összefoglalót: (a) milyen térinformatikai adatok álltak rendelkezésre az esemény előtt, (b) milyen előrejelző rendszerek működtek, (c) milyen fejlesztéseket vezettek be azóta.

5. **(Haladó)** A fejezet amellett érvel, hogy a hidroinformatika közeledik a mesterséges intelligenciához. Nevezzen meg három konkrét feladatot a vízgazdálkodásban, amelyekben az MI-t 2026-ig már alkalmazni kezdték, és hármat, ahol az emberi szakértői vélemény továbbra is elengedhetetlen. Indokolja besorolását minden feladatnál.

---

### 2. fejezet feladatai: Térképezés -- Papírtól a pixelekig

1. **(Alap)** Magyarázza el a földrajzi koordináta-rendszer és a vetületi koordináta-rendszer közötti különbséget. Miért fontos ez a különbség hidrológiai alkalmazásoknál? Adjon példát arra, amikor a földrajzi koordináták használata területszámításnál jelentős hibát okoz.

2. **(Alap)** Egy pont földrajzi koordinátái: szélesség 47,4979° É, hosszúság 19,0402° K (Budapest). Konvertálja ezeket fok-perc-másodperc formátumba. *Várt válasz: 47° 29' 52,4" É, 19° 2' 24,7" K.*

3. **(Középhaladó)** Számítsa ki egy 1 ívmásodperces rácscella méretét méterben Budapest szélességén (47,5° É). Feltételezzen gömb alakú Földet 6370 km sugárral. Adja meg az É-D irányú hosszat, a K-Ny irányú hosszat és a cella területét.

   *Várt válasz: É-D hossz = 6370 × (1/3600) × (π/180) = 30,87 m. K-Ny hossz = 6370 × (1/3600) × (π/180) × cos(47,5°) = 20,85 m. Terület = 30,87 × 20,85 = 643,6 m².*

4. **(Középhaladó)** Az Egységes Országos Vetületi rendszer (EOV) Transverse Mercator vetületet használ a következő paraméterekkel: szélességi eredőpont 47° 8' 39,8174" É; középső meridián 19° 2' 54,8584" K; Y-eltolás (false easting) 650 000 m; X-eltolás (false northing) 200 000 m. Egy pont EOV-koordinátái: Y = 238 400 m (északi irány), X = 649 500 m (keleti irány). Magyarázza el, milyen célt szolgál a hamis eltolás, és becsülje meg a pont közelítő földrajzi koordinátáit. *Segítség: a pont nagyon közel van a vetület eredetéhez, tehát Budapest közelében fekszik.*

5. **(Haladó)** Egy CSV-fájlban az „X" és „Y" nevű oszlopok értékei: X: 450 000--900 000; Y: 50 000--350 000. A könyvben leírt EOV-értéktartomány-szabály alapján melyik oszlop az Easting és melyik a Northing? Magyarázza el a logikát. Miért nem szabad megbízni az oszlopfejlécekben EOV-adatoknál, és milyen ökölszabályt kell mindig alkalmazni?

   *Várt válasz: EOV-ban az Easting értékek ~400 000-tól ~1 000 000-ig terjednek, tehát az X oszlop (450 000--900 000) tartalmazza az Easting értékeket. A Northing értékek ~0-tól ~400 000-ig terjednek, tehát az Y oszlop (50 000--350 000) tartalmazza a Northing értékeket. Az oszlopfejlécek gyakran felcseréltek vagy tévesen címkézettek a régi magyar adatbázisokban; mindig az értéktartomány alapján azonosítsunk.*

---

### 3. fejezet feladatai: Hol laknak az adatok?

1. **(Alap)** Nevezze meg az NHDPlus (National Hydrography Dataset Plus) négy alkotó amerikai nemzeti adatbázisát (NED, NHD, NLCD, WBD). Mindegyiknél írja le, milyen típusú térinformatikai adatot szolgáltat (raszter vagy vektor, és milyen elemeket tartalmaz).

2. **(Alap)** A WBD hierarchikus kódolási rendszert használ (HUC). Egy al-vízgyűjtő HUC-12 kódja: 121002030101. Bontsa a kódot hierarchikus összetevőire: Region, Subregion, Basin, Subbasin, Watershed, Subwatershed, és adja meg mindegyik szám értékét. *Várt válasz: Region 12, Subregion 10, Basin 02, Subbasin 03, Watershed 01, Subwatershed 01.*

3. **(Középhaladó)** Az NHDPlus 2.1 verzió az Egyesült Államokban mintegy 2,7 millió folyószakasz-vízgyűjtőt tartalmaz, átlagosan 3 km² vízgyűjtőterülettel és 2 km átlagos szakaszhosszal. Számítsa ki az ezekből adódó vízhálózati sűrűséget (drainage density). Hasonlítsa össze egy mérsékelt égövi nedves régió tipikus vízhálózati sűrűségével.

   *Várt válasz: Vízhálózati sűrűség = szakaszhossz / vízgyűjtőterület = 2 km / 3 km² = 0,67 km⁻¹. Nedves éghajlat tipikus értéke 0,5--3,0 km⁻¹, tehát az NHDPlus közepes felbontású hálózatot tartalmaz.*

4. **(Középhaladó)** Az EU Víz Keretirányelve megköveteli a tagállamoktól a víztestek ökológiai állapotáról szóló beszámolót. Vizsgálja meg és írja le az NHDPlus európai megfelelő adatbázisait: az EU-Hydro vízhálózatot és az ECRINS-t (European Catchments and Rivers Network System). Hasonlítsa össze térbeli felbontásukat és attribútum-teljességüket az NHDPlus-szal. Melyek a legfontosabb hiányosságok?

5. **(Haladó)** Össze kell állítania egy alapadatbázist a Tisza vízgyűjtőjéhez (amely öt országra terjed ki: Ukrajna, Románia, Szlovákia, Magyarország, Szerbia). Határozza meg a szükséges globális és európai adatbázisokat: (a) vízhálózat és vízgyűjtő-határok, (b) magassági adatok, (c) területhasználat, (d) vízállás- és vízhozam-megfigyelések. Tárgyalja a határokon átnyúló adatharmonizáció kihívásait.

---

### 4. fejezet feladatai: A GIS mint víztudományi eszköz

*Maidment 1. és 2. gyakorlatából adaptálva.*

1. **(Alap)** Magyarázza el a shapefile, a geodatabase feature class és a feature dataset közötti különbséget. Mikor melyiket célszerű használni? Milyen előnyei vannak annak, ha több feature class-t egyetlen feature dataset-ben szervezünk?

2. **(Alap)** Egy GIS geodatabase-ben mi a különbség az „Eltávolítás" (Remove) és a „Törlés" (Delete) művelet között? Miért kritikus ez a különbség az adatkezelésben?

3. **(Középhaladó)** Bármely GIS-platform (ArcGIS Pro, QGIS vagy felhőalapú GIS) segítségével állítson össze egy alaptérképet egy választott vízgyűjtőről. A térképnek tartalmaznia kell: (a) vízgyűjtő-határ poligont, (b) vízhálózatot, (c) legalább három feliratozott mérőállomás-pontot, (d) szabályos elrendezést címmel, aránymértékkel, észak-jelzéssel és jelmagyarázattal.

   *Magyar párhuzam: Készítse el a Zagyva vízgyűjtő alaptérképét a vizugy.hu és az EU-Hydro adatai alapján. Tartalmazza a vízgyűjtő-határt, a fő medret és mellékfolyókat, valamint legalább két vízmérő állomást. Hasonlítsa össze az EU-Hydro és a magyar Vízügyi Igazgatóság vízgyűjtő-határát.*

4. **(Középhaladó)** A San Marcos-medence (HUC-8 = 12100203) Texasban 32 HUC-12 al-vízgyűjtőt tartalmaz 5 HUC-10 vízgyűjtőben. Az NLCD területhasználati adatokból a következő cellastatisztikát kaptuk (30 m cellák): Erdő = 142 000 cella; Beépített = 38 000; Mezőgazdasági = 95 000; Cserjés = 67 000; Víz/vizes élőhely = 8 000. Számítsa ki mindegyik osztály területét km²-ben és százalékban.

   *Várt válasz: Egy cella = 30 × 30 = 900 m² = 0,0009 km². Erdő: 142 000 × 0,0009 = 127,8 km² (40,6%); Beépített: 34,2 km² (10,9%); Mezőgazdasági: 85,5 km² (27,1%); Cserjés: 60,3 km² (19,1%); Víz: 7,2 km² (2,3%). Összesen: 315,0 km².*

5. **(Haladó)** A National Water Model előrejelzése a Blanco-folyóra Wimberley közelében (COMID 1630223) 85 m³/s-ot, a San Marcos-medence legalsó szakaszára (COMID 1632017) 210 m³/s-ot mutat. A vízgyűjtőterületek 920 km² és 2170 km². Számítsa ki a vízhozam- és a területarányokat. Lineáris-e a kapcsolat a vízhozam és a vízgyűjtőterület között? Milyen tényezők okozhatnak eltérést?

   *Várt válasz: Vízhozamarány = 210/85 = 2,47. Területarány = 2170/920 = 2,36. Az arányok hasonlók, közel lineáris skálázásra utalnak, de a csapadék térbeli változékonysága, a területhasználati különbségek, a karszt geológia és az Edwards-víztartó talajvíz-hozzájárulása eltéréseket okozhat.*

---

## II. rész: Terep- és térelemzés (5--8. fejezet)

### 5. fejezet feladatai: A raszter -- Hogyan ábrázolja a számítógép a terepet

1. **(Alap)** Magyarázza el az egész számú (integer) és a lebegőpontos (floating-point) raszterhálózat közötti különbséget. Adjon példát mindkét típusra hidrológiai adatokkal.

2. **(Alap)** Egy DEM cellamérete 9,259 × 10⁻⁵ fok. 42° É szélességen számítsa ki a cella méretét méterben É-D és K-Ny irányban. Feltételezzen gömb alakú Földet 6370 km sugárral.

   *Várt válasz: É-D: 6370 × 9,259 × 10⁻⁵ × (π/180) = 10,29 m. K-Ny: 6370 × 9,259 × 10⁻⁵ × (π/180) × cos(42°) = 7,65 m. Cellaterület = 10,29 × 7,65 = 78,7 m².*

3. **(Középhaladó)** A Logan-folyó medencéjében (Utah) az egyesített DEM 9498 oszlopot és 10 798 sort tartalmaz 10 m-es cellákkal. A minimális magasság 1380 m, a maximális 2960 m. Számítsa ki a DEM által lefedett teljes területet km²-ben. Becsülje meg a relief-hányadost (max. magasság - min. magasság, osztva a terület négyzetgyökével).

   *Várt válasz: Terület = 9498 × 10 798 × 100 m² ≈ 10 255 km². Relief = 2960 - 1380 = 1580 m. Relief-hányados = 1580 / √10 255 = 15,6 m/km⁰·⁵.*

4. **(Középhaladó)** Két 1 fokos DEM-csempét tölt le. A csempék neve: n42w112 és n43w112. A Mosaic to New Raster eszközzel egyesíti őket. Milyen paramétereket kell megadni a pixeltípushoz és a sávok számához? Miért?

   *Várt válasz: Pixeltípus = 32 bites lebegőpontos (a magassági értékek folytonos valós számok). Sávszám = 1 (cellánként egyetlen magassági érték). Ezeknek meg kell egyezniük a forrásképek tulajdonságaival.*

5. **(Haladó)** Hasonlítsa össze az SRTM 30 m globális DEM-et, a Copernicus DEM-et (GLO-30) és az ALOS World 3D DEM-et egy választott hegyi vízgyűjtőre. Tárgyalja a függőleges pontosság, vízszintes felbontás, adatkészítés ideje és lefedettség különbségeit. Melyiket ajánlaná hidroinformatikai tanulmányhoz (a) a magyar Alföldön, (b) a Kárpátokban, (c) szubszaharai Afrikában?

---

### 6. fejezet feladatai: Számolás térképekkel

1. **(Alap)** Magyarázza el a „térképalgebra" fogalmát raszteradatokra alkalmazva. Adjon három, hidrológiai szempontból releváns raszterkalkulátor-műveletet.

2. **(Alap)** Ha két különböző cellaméretű és kiterjedésű raszteren végzünk raszteraritmetikát, milyen három beállítást kell megadnunk az egységes eredményekhez? Mi a szerepe az „elemzési kiterjedésnek", a „cellaméretnek" és a „snap raster"-nek?

3. **(Középhaladó)** A `csapadek` raszter az éves átlagos csapadékot tartalmazza mm-ben, az `et` raszter az éves átlagos evapotranszspirációt mm-ben. Írja fel a raszterkalkulátor-kifejezést az éves átlagos lefolyási mélységhez. Ha a vízgyűjtő területe 450 km², a `csapadek` térbeli átlaga 820 mm, az `et` átlaga 610 mm, számítsa ki az éves lefolyási térfogatot m³-ben.

   *Várt válasz: Lefolyás = csapadek - et. Átlagos lefolyási mélység = 820 - 610 = 210 mm. Térfogat = 0,210 m × 450 × 10⁶ m² = 94,5 × 10⁶ m³ = 94,5 millió m³.*

4. **(Középhaladó)** Az Extract by Mask eszközzel egy területhasználati rasztert (30 m cellák) vágott a vízgyűjtő-határra. Az attribútumtáblázat: Érték 41 (lombhullató erdő) = 52 300 cella; 42 (örökzöld erdő) = 31 200; 81 (legelő) = 44 100; 82 (szántó) = 18 500; 21 (beépített nyílt terület) = 12 400. Számítsa ki a vízgyűjtő teljes területét és az egyes osztályok százalékát.

   *Várt válasz: Összes cella = 158 500. Cella terület = 900 m². Összes terület = 142,65 km². Lombhullató = 33,0%; Örökzöld = 19,7%; Legelő = 27,8%; Szántó = 11,7%; Beépített = 7,8%.*

5. **(Haladó)** Tervezzen raszteralapú munkafolyamatot egy egyszerű talajnedvesség-index kiszámítására egy vízgyűjtőre. Bemeneti adatok: csapadékraszter, potenciális ET-raszter, talaj víztartó kapacitás raszter, területhasználati raszter. Írja le a lépéseket és a raszterkalkulátor-kifejezéseket.

---

### 7. fejezet feladatai: Lejtés, kitettség és a terep formája

*Maidment 3. gyakorlatából (Part 1) adaptálva.*

1. **(Alap)** Definiálja a lejtést és a kitettséget (aspektust) DEM-ből számítva. Mi a lejtés egysége százalékos emelkedés és fok formában? Alakítsa át a 45%-os lejtést fokokra. *Várt válasz: arctan(0,45) = 24,2°.*

2. **(Középhaladó)** Az alábbi 3×3-as magassági rácsból (10 m cellaméret) számítsa ki a központi cella lejtését az ArcGIS „felületi lejtés" módszerével (3. rendű véges differencia):

   ```
   25,1  25,8  26,8
   25,0  26,0  26,4
   25,4  26,1  27,0
   ```

   A módszer: dz/dx = ((c-a) + 2(f-d) + (i-g)) / (8 × cellaméret) és dz/dy = ((g-a) + 2(h-b) + (i-c)) / (8 × cellaméret), ahol a 3×3 ablak elemei a-tól i-ig balról jobbra, felülről lefelé vannak jelölve.

   *Várt válasz: a=25,1; b=25,8; c=26,8; d=25,0; e=26,0; f=26,4; g=25,4; h=26,1; i=27,0. dz/dx = (1,7 + 2,8 + 1,6)/80 = 0,07625. dz/dy = (0,3 + 0,6 + 0,2)/80 = 0,01375. Lejtés = √(0,07625² + 0,01375²) = 0,0775 = 7,75%.*

3. **(Középhaladó)** Ugyanabból a rácsból számítsa ki a D8 folyásirány-értéket a központi cellánál. Fejezze ki kódolt irányértékként (1, 2, 4, 8, 16, 32, 64, 128) és iránytű-irányként. Számítsa ki a hidrológiai lejtést is.

4. **(Középhaladó)** Magyarázza el a D8 és a D-végtelen (DINF) folyásirány-algoritmus közötti különbséget. Miért alkalmasabb a D8 a vízhálózat lehatárolásához, míg a DINF a lejtőn történő vízmozgás számításához (pl. HAND)?

5. **(Haladó)** Építsen egy ModelBuilder-munkafolyamatot (vagy azzal egyenértékű Python/QGIS modellt), amely egy ASCII raszterfájlt vesz bemenetként és hat kimenetet állít elő: importált raszter, lejtés (%), kitettség, D8 folyásirány, D8 százalékos esés, DINF folyásirány. Futtassa két különböző DEM-en és hasonlítsa össze az eredményeket. *(A 3. gyakorlat 1.3. részéből adaptálva.)*

---

### 8. fejezet feladatai: Az eső mérése ott, ahol esik

*Maidment 3. gyakorlatából (Part 2) adaptálva.*

1. **(Alap)** Magyarázza el a Thiessen-poligon módszert a területi átlagos csapadék becslésére pontmérésekből. Milyen feltételek mellett működik jól, és mikor nem megbízható?

2. **(Középhaladó)** Öt csapadékmérő állomás veszi körül a vízgyűjtőt. Thiessen-poligon területeik és éves csapadékértékeik:

   | Állomás | Thiessen-terület (km²) | Éves csapadék (mm) |
   |---------|------------------------|--------------------|
   | A       | 12,3                   | 780                |
   | B       | 8,7                    | 920                |
   | C       | 15,1                   | 850                |
   | D       | 6,4                    | 1 020              |
   | E       | 9,5                    | 690                |

   Számítsa ki a Thiessen-súlyozott éves átlagos csapadékot.

   *Várt válasz: Összes terület = 52,0 km². Súlyozott összeg = 9594 + 8004 + 12 835 + 6528 + 6555 = 43 516. Átlag = 43 516 / 52,0 = 836,8 mm.*

3. **(Középhaladó)** A vízgyűjtő három HUC-12 al-vízgyűjtőre oszlik. Az Intersect eszközzel a Thiessen-poligonokat az al-vízgyűjtő-határokra illeszti. Írja le lépésről lépésre, hogyan számítaná ki az átlagos éves csapadékot minden al-vízgyűjtőhöz.

4. **(Középhaladó)** Hasonlítson össze három térbeli interpolációs módszert csapadékra: Thiessen-poligon, inverz távolságsúlyozás (IDW), szokásos krigelés. Mindegyikhez írja le az alapfeltevést, egy előnyt és egy korlátot. Melyik a legalkalmasabb ritka csapadékmérő hálózat esetén?

5. **(Haladó)** Éves átlagos csapadékadatai vannak 15 állomásról egy hegyi vízgyűjtőben. Tervezzen munkafolyamatot a csapadékfelszín elkészítéséhez: (a) egyszerű IDW-interpoláció, (b) csapadék-magasság regresszió, majd maradék-interpoláció. Számítsa ki az átlagos csapadékot mindkét módszerrel három al-vízgyűjtőre.

   *Magyar párhuzam: Használja a Balaton-vízgyűjtő OMSZ állomásainak csapadékadatait és az EU-DEM-et. A Balaton környéke viszonylag lapos; tárgyalja, mennyire erős a magasság mint csapadék-előrejelző tényező ebben a régióban.*

---

## III. rész: Vízgyűjtő-lehatárolás és hidrológiai terepelemzés (9--11. fejezet)

### 9. fejezet feladatai: A digitális táj előkészítése

*Maidment 4. gyakorlatából adaptálva.*

1. **(Alap)** Magyarázza el, mit jelent a DEM „mélyedéskitöltés" (pit filling), és miért szükséges hidrológiai elemzéshez. Adjon egy példát valós topográfiai mélyedésre és egy műtermékre.

2. **(Alap)** Miért szükséges pufferzónát létrehozni a vízgyűjtő-határ körül a DEM kivágása előtt? Milyen problémák merülhetnek fel pufferzóna nélkül?

3. **(Középhaladó)** Egy DEM földrajzi koordinátákban (tizedfok) van megadva. UTM vetületre (méter) kell átvetíteni. Sorolja fel a szükséges GIS-műveletek sorrendjét: (a) DEM kivágás, (b) átvetítés, (c) ellenőrzés.

4. **(Középhaladó)** A DEM kitöltése után a kitöltött DEM és az eredeti közötti maximális különbség 22 m. Hogyan dönthető el, hogy ez valós mélyedés vagy műtermék? Mi a következménye, ha egy valós mélyedést kitöltünk?

5. **(Haladó)** Tervezzen teljes munkafolyamatot a nyers DEM-csempéktől a hidrológiailag kondicionált DEM-ig: mozaik, puffer, maszk, átvetítés, kitöltés.

---

### 10. fejezet feladatai: Merre folyik a víz?

*Maidment 4. gyakorlatából adaptálva.*

1. **(Alap)** Rajzoljon 3×3-as rácsot és jelölje a D8 folyásirány-kódokat mind a nyolc irányban. Határozza meg a D8 folyásirányt és a hidrológiai lejtést a következő DEM központi cellájánál (10 m cellaméret):

   ```
   180  175  170
   185  190  172
   188  182  178
   ```

   *Várt válasz: A központi cella (190) magasabb minden szomszédjánál. A legmeredekebb esés az ÉK cella (170) felé: esés = 20 m / 14,14 m = 1,414 (141,4%). D8 kód: 128 (ÉK).*

2. **(Alap)** Magyarázza el a lefolyás-akkumuláció (flow accumulation) rács fogalmát. Ha egy cella akkumulációs értéke 5000 és a cellaméret 10 m, mekkora a cella feletti vízgyűjtőterület km²-ben? *Várt válasz: 5000 × (10 × 10) = 500 000 m² = 0,5 km².*

3. **(Középhaladó)** A Logan-folyó medencéjének kifolyási cellájánál a lefolyás-akkumuláció értéke 5 540 000 (10 m cellaméret). Számítsa ki a vízgyűjtőterületet km²-ben. A USGS 554 km²-t közöl. Hasonlítsa össze és tárgyalja az eltérés okait.

4. **(Középhaladó)** Magyarázza el, hogyan definiálunk vízhálózatot a lefolyás-akkumulációs rácsból küszöbérték segítségével. 1000 cellás küszöb (10 m cellaméret) esetén mekkora a minimális forrásterület? Mi történik, ha csökkentjük vagy növeljük a küszöböt?

   *Várt válasz: Min. forrásterület = 1000 × 100 = 100 000 m² = 0,1 km². Alacsonyabb küszöb sűrűbb hálózatot, magasabb küszöb ritkábbat eredményez.*

5. **(Haladó)** Egy vízgyűjtő teljes vízhálózat-hossza 320 km, területe 480 km². Számítsa ki a vízhálózati sűrűséget és az átlagos lejtőhosszt (1/(2×Dd)). Tárgyalja a hidrológiai válasz-időre gyakorolt hatást.

   *Várt válasz: Dd = 320/480 = 0,667 km⁻¹. Átlagos lejtőhossz = 1/(2 × 0,667) = 0,75 km = 750 m.*

---

### 11. fejezet feladatai: Vízgyűjtők rajzolása adatokból

*Maidment 4. gyakorlatából adaptálva.*

1. **(Alap)** Írja le a stream link raszter, a vízfolyásszakasz-vonalréteg, a catchment raszter és a catchment poligon közötti kapcsolatot. Mi az az egyedi azonosító, amely összeköti e négy adatterméket?

2. **(Középhaladó)** Egy 10 m-es DEM-ből lehatárolt vízgyűjtő-határ és az online szolgáltatás által lehatárolt határ között 8 km hosszon ~3 km eltérést talál. Becsülje meg az eltérés területét és tárgyalja az okait.

3. **(Középhaladó)** A DEM-ből lehatárolt hálózat 185 szakaszt tartalmaz; az NHDPlus hálózat 210-et ugyanazon területen. Miért különböznek? Mit árul el ez a szegmentálási szabályokról?

4. **(Középhaladó)** A Logan-folyó medencéjének NHDPlus-adatai: teljes vízhálózat-hossz 340 km, főmeder-hossz 65 km, vízgyűjtőterület 554 km². Számítsa ki: (a) vízhálózati sűrűség, (b) főmeder-arány, (c) átlagos lejtőhossz.

   *Várt válasz: (a) Dd = 340/554 = 0,614 km⁻¹. (b) Arány = 65/340 = 19,1%. (c) Átlagos lejtőhossz = 1/(2 × 0,614) = 0,814 km.*

5. **(Haladó)** Végezze el a teljes terepelemzési munkafolyamatot egy választott vízgyűjtőre: DEM beszerzése, mozaik, kivágás, átvetítés, kitöltés, folyásirány, akkumuláció, vízhálózat, szakaszkód, vízgyűjtő-lehatárolás, vektorizálás. Hasonlítsa össze a DEM-ből lehatárolt hálózatot egy hivatalos vízhálózati adatbázissal.

---

## IV. rész: Automatizálás és fejlett érzékelés (12--13. fejezet)

### 12. fejezet feladatai: A munkafolyamat automatizálása

1. **(Alap)** Magyarázza el, mi a ModelBuilder, és miben különbözik a Python-szkripttől. Milyen két előnye van mindegyik megközelítésnek?

2. **(Alap)** A ModelBuilder-ben mi a különbség az „eszköz" (tool), a „változó" (input/output adat) és a „paraméter" között? Rajzoljon egy egyszerű modellt, amely egy DEM-et vesz bemenetként, és lejtő- valamint folyásirány-rácsot állít elő.

3. **(Középhaladó)** Írjon Python-szkriptet, amely: (a) beolvas egy DEM-rasztert, (b) kitölti a mélyedéseket, (c) kiszámítja a folyásirányt, (d) kiszámítja a lefolyás-akkumulációt, (e) mindent egy megadott mappába ment.

4. **(Középhaladó)** 12 al-vízgyűjtőre kell megismételnie ugyanazt a terepelemzést. Hogyan automatizálná (a) ModelBuilder-iterátorral, (b) Python-ciklussal? Melyik rugalmasabb? Melyik egyszerűbb nem programozó számára?

5. **(Haladó)** Tervezzen automatizált munkafolyamatot: DEM letöltés online szolgáltatásból, kivágás, kitöltés, folyásirány, akkumuláció, vízgyűjtő-lehatárolás egy megadott kifolyási pontra, összefoglaló jelentés (vízgyűjtőterület, átlagos magasság, vízhálózati sűrűség).

---

### 13. fejezet feladatai: A felszín 3D-ben -- LiDAR

1. **(Alap)** Magyarázza el a DEM, DSM és DTM közötti különbséget. Melyik a legalkalmasabb hidrológiai elemzéshez, és miért?

2. **(Alap)** A LiDAR-pontfelhő adatait jellemzően talaj, növényzet, épület és víz kategóriákba sorolják. Miért elengedhetetlen a talajpontos osztályozás a hidrológiai DEM létrehozása előtt?

3. **(Középhaladó)** Egy LiDAR-felmérés 1 m felbontású DTM-et ad egy 50 km²-es ártérre. Számítsa ki a rácscellák számát és a hozzávetőleges fájlméretet (32 bites lebegőpontos, tömörítetlen). Hasonlítsa össze egy 10 m-es DEM-mel.

   *Várt válasz: 1 m DEM: 50 × 10⁶ cella. Fájlméret = 200 MB. 10 m DEM: 500 000 cella, 2 MB. A LiDAR-DEM 100-szor nagyobb.*

4. **(Középhaladó)** Hogyan javítják a LiDAR-DEM-ek az árvízi elöntési térképezést a 10 m-es vagy 30 m-es DEM-ekhez képest? Hivatkozzon a HAND módszerre, és magyarázza el, miért különösen fontos a magassági pontosság alacsony esélyű ártereken.

5. **(Haladó)** Magyarország nemrégiben elkészítette az országos légi LiDAR-felmérést. Tárgyalja ennek következményeit: (a) városi árvíztérképezés Budapesten, (b) mezőgazdasági vízrendezési elemzés az Alföldön, (c) gátállapot-felmérés a Tisza mentén. Minden alkalmazáshoz becsülje meg a szükséges DEM-felbontást és LiDAR-pontsűrűséget.

---

## V. rész: Árvízelemzés (14--17. fejezet)

### 14. fejezet feladatai: Milyen magasan a folyó felett?

*Maidment 5. gyakorlatából adaptálva.*

1. **(Alap)** Definiálja a HAND-ot (Height Above Nearest Drainage). Fogalmi szinten magyarázza el, hogyan számítják egy DEM-ből és egy folyóraszterből. Miért pontosan nulla az értéke a térképezett folyókon, és miért nő, ahogy távolodunk?

2. **(Alap)** Miért részesítjük előnyben a DINF folyásirányt a D8-cal szemben a HAND lejtőkön történő számításánál, míg a D8-at a vízhálózat lehatárolásánál?

3. **(Középhaladó)** Az Onion Creek vízgyűjtőn (5. gyakorlat) egy vízgyűjtő-poligon HAND-elemzése h = 1 m vízszintre: 658 cella a küszöb alatt, cellaméret 10 m, átlagos elöntési mélység 0,713 m. Számítsa ki: (a) elöntött felületet, (b) elöntési térfogatot, (c) mederkeresztmetszetet, ha a szakaszhossz 4308 m.

   *Várt válasz: (a) 658 × 100 = 65 800 m². (b) 0,713 × 65 800 = 46 915 m³. (c) 46 915 / 4308 = 10,9 m².*

4. **(Középhaladó)** Manning-egyenlettel (Q = (1/n) × A × R²/³ × S¹/²) számítsa ki a vízhozamot: A = 10,9 m², nedvesített kerület P = 15,29 m, S = 0,001617, n = 0,05.

   *Várt válasz: R = 10,9/15,29 = 0,713 m. Q = 20 × 10,9 × 0,798 × 0,04021 = 7,0 m³/s.*

5. **(Haladó)** Ismételje meg a HAND-alapú hidraulikai számítást h = 6, 10, 14 m vízszintre. Rajzolja meg a szintetikus vízhozamgörbét (vízszint vs. vízhozam). 2782 m³/s-os árvízi vízhozam esetén interpolálja a megfelelő vízszintet. Tárgyalja a bizonytalanságokat.

---

### 15. fejezet feladatai: Az árvíz útvonalának térképezése

*Maidment 5. gyakorlatából adaptálva.*

1. **(Alap)** Írja le, hogyan készül árvízi elöntési térkép HAND-raszterből és vízszintből. Milyen raszterkalkulátor-művelet szükséges?

   *Várt válasz: Elöntési mélység = vízszint - HAND, minden cellára, ahol HAND < vízszint. A HAND ≥ vízszint cellákat nem önti el a víz.*

2. **(Alap)** Miért nem illeszkednek tökéletesen a DEM-ből lehatárolt vízgyűjtő-határok az NHDPlus vízgyűjtő-határokhoz? Mi ennek a következménye a HAND-alapú árvíztérképezésre?

3. **(Középhaladó)** Egy árvízi elemzés 2400 cellát (10 m) azonosít, ahol HAND < 8 m. Az átlagos HAND-érték 3,2 m. Számítsa ki: (a) elöntött területet, (b) átlagos mélységet, (c) elöntési térfogatot.

   *Várt válasz: (a) 240 000 m² = 0,24 km². (b) 8 - 3,2 = 4,8 m. (c) 4,8 × 240 000 = 1 152 000 m³.*

4. **(Középhaladó)** Az Extract Values to Points eszközzel 150 cím HAND-értékeit vizsgálja: 5 cím < 3 m, 12 cím 3--6 m, 25 cím 6--9 m, 38 cím 9--12 m, 70 cím > 12 m. Ha a becsült vízszint 9 m, hány cím kerül elöntés alá?

   *Várt válasz: HAND < 9 m: 5 + 12 + 25 = 42 cím. Arány = 42/150 = 28%.*

5. **(Haladó)** Tervezzen teljes HAND-alapú árvízi kockázatértékelést egy hazai folyószakaszra. A lépések: DEM beszerzés és kondicionálás, vízhálózat-lehatárolás, HAND-számítás, Manning-egyenletes vízhozamgörbe, árvízi vízszint meghatározása mértékadó árvízre, elöntési térkép, átfedés-elemzés épületekkel.

   *Magyar párhuzam: Alkalmazza a munkafolyamatot a Hernád egy szakaszára Miskolc közelében a magyar LiDAR-DEM felhasználásával. Hasonlítsa össze HAND-alapú térképét az OVF hivatalos árvízveszélyes területi térképével.*

---

### 16. fejezet feladatai: Árvíz-előrejelzés valós időben

1. **(Alap)** Írja le a US National Water Model négy előrejelzési időhorizontját. Mindegyikhez adja meg a frissítési gyakoriságot, az előrejelzési időtartamot és az elsődleges felhasználási célt.

2. **(Alap)** A National Water Model minden NHDPlus-szakaszra előrejelzést készít. Hozzávetőleg hány szakasz van? Milyen térbeli felbontást használ a felszíni modellkomponens?

3. **(Középhaladó)** Nyissa meg az EFAS-t (European Flood Awareness System, https://www.efas.eu/) és hasonlítsa össze a US National Water Modellel: (a) térbeli lefedettség, (b) felbontás, (c) előrejelzési horizontok, (d) meteorológiai meghajtó adatok, (e) nyilvános hozzáférhetőség.

4. **(Középhaladó)** Egy vízhozam-előrejelzés 5 napos hidrográfja: 1. nap = 45 m³/s, 2. = 120, 3. = 310, 4. = 185, 5. = 80 m³/s. Becsülje meg az 5 napos összes víztérfogatot. Ha az árvízi küszöb 200 m³/s, melyik napo(ko)n várható árvíz?

   *Várt válasz: Térfogat = 740 × 86 400 = 63,94 millió m³. Árvíz a 3. napon (310 > 200).*

5. **(Haladó)** A National Water Model folyamatalapú hidrológiai modellt használ. Tárgyalja ennek előnyeit és korlátait egy tisztán adatvezérelt gépi tanulási modellhez képest árvíz-előrejelzésnél.

---

### 17. fejezet feladatai: Ki lakik az ártéren?

1. **(Alap)** Mi a különbség az árvízveszélyi térkép és az árvízkockázati térkép között?

2. **(Középhaladó)** Egy 100 éves visszatérési idejű árvízi elöntési térkép 850 lakóépületet azonosít az ártéren. Az átlagos épületérték 180 000 EUR, a várható kárfaktor 35%. Számítsa ki az éves várható kárt (EAD). Miért szükséges több visszatérési időt figyelembe venni?

   *Várt válasz: Összes kár = 850 × 180 000 × 0,35 = 53,55 millió EUR. Éves túllépési valószínűség = 0,01. EAD = 535 500 EUR.*

3. **(Középhaladó)** Ha az ártéri terület (HAND < 5 m) 2,5 km² és a népsűrűség 1200 fő/km², hány ember van kitéve árvízveszélynek?

   *Várt válasz: 2,5 × 1200 = 3000 ember.*

4. **(Középhaladó)** Írja le, hogyan kombinálna GIS-átfedés-elemzéssel egy árvízi elöntési térképet: (a) épületkontúrokkal, (b) kritikus infrastruktúrával (kórházak, iskolák, erőművek), (c) úthálózattal. Milyen kimenetet készítene a katasztrófavédelmi tervezők számára?

5. **(Haladó)** Tervezzen szocio-hidrológiai árvízkockázati elemzést Budapest egy Duna menti kerületéhez: árvízveszély (HAND vagy hivatalos térkép), kitettség (épületek, népszámlálás), sérülékenység (épülettípus, szintek száma). Javasoljon GIS-munkafolyamatot, és tárgyalja az adatelérhetőséget magyar viszonyok között.

---

## VI. rész: Felszín alatti vizek (18--21. fejezet)

### 18. fejezet feladatai: Bepillantás a föld alá -- 3D felszín alatti GIS

1. **(Alap)** Miért alapvetően más a felszín alatti geológia GIS-ben történő ábrázolása, mint a felszíni topográfiáé?

2. **(Alap)** Definiálja a következő fogalmakat: fúrásprofil, rétegtani szint, voxelmodell, szelvény. Hogyan kapcsolódnak egymáshoz?

3. **(Középhaladó)** 25 kút fúrásnaplójából a kavicsréteg tetejét és alját kell interpolálnia. Hogyan készít GIS-interpolációval: (a) víztartó tetőfelszínt, (b) talpat, (c) vastagságtérképet? Milyen interpolációs módszert választana?

4. **(Középhaladó)** Egy 3D voxelmodell 10 km × 10 km területet fed le, 100 m vízszintes és 5 m függőleges felbontással, 0--200 m mélységig. Hány voxelt tartalmaz? Mekkora a fájlméret 32 bites lebegőpontos értékek esetén?

   *Várt válasz: 100 × 100 × 40 = 400 000 voxel. Fájlméret = 400 000 × 4 bájt = 1,6 MB.*

5. **(Haladó)** Hasonlítsa össze a halmozott 2D felszínes és a valódi 3D voxeles megközelítést felszín alatti modellezéshez.

---

### 19. fejezet feladatai: Kutak, fúrások és víztartó-térképek

1. **(Alap)** Milyen adatokat tartalmaznak jellemzően a kútfúrási dokumentációk? Soroljon fel legalább hat, hidroinformatikai szempontból releváns adatmezőt.

2. **(Középhaladó)** 30 megfigyelőkút vízszintadataiból piezometrikus felszínt (talajvíztérképet) kell készítenie. Írja le a GIS-lépéseket.

3. **(Középhaladó)** Négy kút vízszintadatai (m Bf.): Kút 1 (X=500, Y=300): 125,3 m; Kút 2 (X=800, Y=300): 122,1 m; Kút 3 (X=500, Y=600): 124,7 m; Kút 4 (X=800, Y=600): 121,5 m. Becsülje meg a hidraulikus gradiens nagyságát és irányát síkillesztéssel.

   *Várt válasz: dh/dx = -0,01067; dh/dy = -0,002. Gradiens = 0,01086. Irány: kelet felé, enyhe déli komponenssel.*

4. **(Középhaladó)** A magyar fúrásadatbázisok (MBFSZ) gyakran eltérő koordináta-rendszerű adatokat tartalmaznak. Írjon le egy minőség-ellenőrzési GIS-munkafolyamatot: (a) felcserélt X/Y koordináták felismerése az EOV-értéktartomány szabállyal, (b) duplikátumok szűrése, (c) lehetetlen mélységértékek jelölése.

5. **(Haladó)** Tervezzen GIS-alapú DRASTIC sérülékenység-értékelést. Milyen adatrétegek szükségesek? Hogyan osztályozza és súlyozza őket? Alkalmazza fogalmi szinten a Budapest melletti dunai kavicsvíztartóra.

---

### 20. fejezet feladatai: A felszín alatti kép felépítése

1. **(Alap)** Mi a „hidrosztratigráfiai egység" és miben különbözik a litosztratigráfiai egységtől?

2. **(Középhaladó)** Hogyan digitalizálná a geológus által rajzolt szelvényeket GIS-be? Milyen kihívásokat jelent, ha különböző forrásokból származó szelvények nem egyeznek?

3. **(Középhaladó)** Egy geofizikai felmérés (elektromos ellenállás tomográfia) az alapkőzetig terjedő mélységet térképezte egy folyóvölgyi szelvény mentén. Hogyan integrálná a fúrási adatokkal a víztartó-vastagság térkép javítására?

4. **(Haladó)** Hasonlítson össze két 3D geológiai modellezési szoftvert (pl. Leapfrog, GemPy). Mindegyikhez írja le a modellezési megközelítést, az adatigényeket és a felszín alatti áramlási modellbe történő exportálás lehetőségét.

5. **(Haladó)** Az Alföld összetett többrétegű víztartórendszerrel rendelkezik. Tervezzen munkafolyamatot egy 50 km × 50 km terület hidrogeológiai modelljéhez MBFSZ-adatok felhasználásával.

---

### 21. fejezet feladatai: Felszín alatti vízáramlás modellezése

1. **(Alap)** Fogalmazza meg Darcy törvényét szavakkal és képlettel. Mi a hidraulikus vezetőképesség, a hidraulikus gradiens és a fajlagos vízhozam egysége?

2. **(Alap)** Írja le a MODFLOW (vagy azzal egyenértékű) felszín alatti áramlási modell felállításának általános lépéseit. Milyen GIS-adatrétegek szükségesek bemenetként?

3. **(Középhaladó)** Egy egyszerű zárt víztartó: transzmisszivitás T = 500 m²/nap, szélesség W = 2 km, hidraulikus gradiens i = 0,003. Számítsa ki a térfogati vízhozamot Darcy törvényével.

   *Várt válasz: Q = 500 × 2000 × 0,003 = 3000 m³/nap = 34,7 l/s.*

4. **(Középhaladó)** Hogyan konvertálják a GIS-előfeldolgozó eszközök (FloPy, ModelMuse) a raszter- és vektor-GIS-rétegeket MODFLOW bemeneti fájlokká?

5. **(Haladó)** Állítson be egy egyszerű 2D állandósult áramlási modellt egy 5 km × 3 km téglalap alakú tartományra: állandó nyomásszint a keleti (100 m) és nyugati (95 m) oldalon, zárt határ északon és délen, homogén K = 10 m/nap, egy szivattyúzó kút a középpontban (500 m³/nap). Készítsen piezometrikus felszíntérképet.

---

## VII. rész: Adat-modell integráció és MI (22--25. fejezet)

### 22. fejezet feladatai: Amikor a modellek találkoznak az adatokkal

1. **(Alap)** Magyarázza el a modell-kalibrálás fogalmát. Miért szükséges, és mi a túlillesztés (overfitting) veszélye?

2. **(Alap)** Definiálja a Nash-Sutcliffe hatékonysági együtthatót (NSE). Írja fel a képletet és magyarázza el, mit jelent NSE = 1, NSE = 0 és NSE < 0.

3. **(Középhaladó)** Kalibrált csapadék-lefolyás modell havi mért (M) és szimulált (Sz) vízhozamai (m³/s): M = [12, 15, 45, 80, 55, 30, 18, 10, 8, 15, 25, 20]; Sz = [14, 18, 40, 72, 60, 28, 20, 12, 10, 13, 22, 18]. Számítsa ki az NSE-t, RMSE-t és százalékos eltérést (PBIAS).

   *Várt válasz: NSE = 0,969. RMSE = 3,65 m³/s. PBIAS = 1,8%.*

4. **(Középhaladó)** Magyarázza el az osztott mintás (split-sample) validálási tesztet. Hogyan osztaná fel egy 20 éves napi vízhozam-adatsort?

5. **(Haladó)** Tárgyalja az „ekvifinalitás" problémáját a hidrológiai modellezésben: többféle paraméterkészlet hasonlóan jó illeszkedést produkálhat. Hogyan hat ez a vízgazdálkodási döntéshozatalra? Írjon le legalább két megoldási megközelítést.

---

### 23. fejezet feladatai: MI mint a hidrológus segítőtársa

1. **(Alap)** Magyarázza el a folyamatalapú hidrológiai modell és a gépi tanulási modell közötti különbséget. Adjon egy-egy példát.

2. **(Alap)** Mi az LSTM (Long Short-Term Memory) neurális hálózat? Miért különösen alkalmas hidrológiai idősorok előrejelzésére?

3. **(Középhaladó)** Egy LSTM-modell NSE = 0,92-t ér el a tesztelési időszakban, de egy szomszédos, nem mért vízgyűjtőn csak NSE = 0,55-öt. Tárgyalja az okokat és javasoljon legalább két stratégiát az átvitel javítására.

4. **(Középhaladó)** Hasonlítsa össze a Random Forest, LSTM és hibrid (koncepcionális + ML) megközelítéseket árvíz-előrejelzésre. Melyiket ajánlaná operatív használatra?

5. **(Haladó)** A Google árvíz-előrejelző rendszere hidrológiai modelleket és gépi tanulást kombinál adatszegény régiókban. Kutassa és írja le: (a) a fő innovációt, (b) hogyan kezeli a nem mért vízgyűjtőket, (c) milyen országokat fed le, (d) korlátait. Javasolja, hogyan lehetne hasonló rendszert kiépíteni a Tisza vízgyűjtőjére.

---

### 24. fejezet feladatai: Ágensalapú MI -- Az önálló modellezés eszköze

1. **(Alap)** Definiálja az „ágens-MI"-t a hidroinformatika összefüggésében. Miben különbözik egy hagyományos szkripttől?

2. **(Alap)** Írjon le három feladatot, ahol egy MI-ágens önállóan hozhat döntéseket: adatválasztás, paraméterhangolás, eredményértelmezés. Mindegyiknél határozza meg a kockázatokat.

3. **(Középhaladó)** Egy MI-ágens feladata egy MODFLOW-modell kalibrálása 20 kút mért vízszintjéhez, 5 hidraulikus vezetőképesség-zóna módosításával. Írja le az optimalizálási hurkot, a leállítási kritériumokat és a fizikailag indokolatlan eredmények megelőzésének módját.

4. **(Középhaladó)** Hasonlítsa össze a „kódgeneráló MI"-t (LLM, amely Python-szkripteket ír) és az „eszközhasználó MI"-t (ágens, amely közvetlenül hívja a GIS-funkciókat). Milyen előnyei és kockázatai vannak mindegyiknek?

5. **(Haladó)** Tervezzen ágens-MI rendszert valós idejű árvízi riasztáshoz: (a) időjárás-előrejelzés fogadása, (b) hidrológiai modell futtatása, (c) HAND-alapú elöntési térkép, (d) érintett infrastruktúra azonosítása, (e) riasztási közlemény generálása. Rajzolja meg az architektúra-diagramot.

---

### 25. fejezet feladatai: A hidroinformatika jövője

1. **(Alap)** Azonosítson három feltörekvő technológiát, amelyek jelentősen hathatnak a hidroinformatikára a következő évtizedben. Mindegyikhez írjon két mondatot.

2. **(Középhaladó)** Mi a „digitális iker" egy vízgyűjtő esetében? Milyen adatfolyamok táplálnák, milyen modellek futnának benne, és milyen döntéseket támogathatna? Melyek a legnagyobb technikai és intézményi akadályok?

3. **(Középhaladó)** Az éghajlatváltozás hogyan befolyásolja a hidroinformatikai eszközöket? Tárgyalja: (a) a stacionaritás feltételezését az árvíz-gyakoriság elemzésben, (b) a dinamikus területhasználati adatok szükségességét, (c) az éghajlati ensemble-előrejelzések szerepét.

4. **(Haladó)** Írjon 500 szavas esszét az MI-vezérelt vízgazdálkodás etikai vonatkozásairól: (a) ki profitál és ki sérülhet, (b) algoritmikus átláthatóság és elszámoltathatóság, (c) a digitális szakadék adatgazdag és adatszegény országok között.

5. **(Haladó)** Javasoljon 5 éves kutatási programot a hidroinformatika számára nemzeti szinten (Magyarország vagy saját országa). Határozza meg: (a) a három legsürgősebb vízkihívást, (b) a szükséges hidroinformatikai képességeket, (c) az adatinfrastrukturális beruházásokat, (d) a humán kapacitásépítést (oktatás, képzés).

---

## Értékelési szempontok

A számítási feladatoknál a várt válaszok a szövegben szerepelnek. A nyílt végű és esszétípusú kérdéseknél az értékelés hangsúlyozza:

- Az adott fejezet fogalmainak helyes alkalmazását
- Logikus gondolkodást és világos kommunikációt
- A mértékegységek és értékes jegyek helyes használatát
- Gyakorlati GIS-készségek bemutatását, ahol alkalmazható
- Az amerikai példák nemzetközi összefüggésbe helyezésének képességét

GIS-szoftvert igénylő feladatoknál elfogadott platformok: ArcGIS Pro, QGIS, Google Earth Engine, vagy bármely platform, amely támogatja a szükséges térelemzési műveleteket.

---

## Gyakorlati GIS-feladatok (Maidment kurzusából adaptálva)

Az alábbi öt gyakorlat eredetileg David R. Maidment (University of Texas at Austin) és David G. Tarboton (Utah State University) GIS in Water Resources kurzusához (2018 ősz) készült. A feladatsor fokozatos: az alapvető GIS-készségektől a vízgyűjtő-lehatároláson át az árvízi elöntéselemzésig halad. Minden gyakorlathoz három változat tartozik:

- **Eredeti (USA)** -- Az eredeti amerikai adatbázisokkal és mintaterületekkel.
- **Nemzetközi** -- Ingyenes globális adatforrásokkal.
- **Magyar** -- Magyar adatokkal, vízgyűjtőkkel és koordináta-rendszerrel.

A hallgatók lehetőleg a lakóhelyükhöz legközelebbi változatot végezzék el, de próbálják ki az eredetit és a régió-specifikusat is, hogy lássák az adatinfrastruktúra különbségeit.

**Szoftverkövetelmények.** A gyakorlatok ArcGIS Pro 2.2+-ra készültek. Egyenértékű munkafolyamatok léteznek QGIS 3.x-ben (ingyenes, nyílt forráskódú). Ahol ArcGIS-specifikus eszközök szerepelnek, a QGIS-megfelelőt szögletes zárójelben adjuk meg. Python-alternatívák (WhiteboxTools, PyQGIS, arcpy) szintén elfogadhatók.

---

### 1. gyakorlat: Bevezetés a GIS-be vízgazdálkodási alkalmazásokkal

*Maidment és Tarboton 1. gyakorlata (2018) alapján. Becsült időszükséglet: 3--4 óra.*

**Tanulási célok.** (1) GIS-projekt létrehozása és adatszervezés geodatabase-ben. (2) Vektor- és raszterrétegek hozzáadása. (3) Jelkulcs módosítása, rétegek rendezése, attribútumtábla értelmezése. (4) Koordináta-rendszerek és vetületek vizsgálata. (5) Alapvető geoprocesszing: kiválasztás attribútum és hely alapján, vetítés, vágás, térbeli összekapcsolás.

#### A változat: Eredeti (USA -- Texas)

**Mintaterület.** Texas állam a párolgásmérő állomásokkal és megyehatárokkal.

**Adatok.** Három shapefile: `Texas.shp` (Texas körvonala), `Counties.shp` (254 texasi megye), `Evap.shp` (párolgásmérő állomások éves adatokkal). Letöltés: `http://hydrology.usu.edu/dtarb/giswr/2018/Ex1Data.zip`

**Eljárás.**

1. Hozzon létre új projektet `Ex1Project` névvel.
2. Adja hozzá mindhárom shapefile-t.
3. Rendezze a rajzolási sorrendet: Counties a Texas felett, Evap legfelül.
4. Módosítsa a jelkulcsot: Texas átlátszó kitöltés, zöld körvonal (2 pt); Counties világoszöld; Evap piros körök (6 pt).
5. Másolja az adatokat a projekt geodatabase-be (Copy Features).
6. Vizsgálja meg az Evap tulajdonságait: koordináta-rendszer, geometriatípus, elemszám.
7. Nyissa meg az attribútumtáblát; keresse meg a legmagasabb és legalacsonyabb párolgású állomást.
8. Válassza ki az éves párolgás > 70 hüvelyk állomásokat. Hány darab?
9. Válassza ki azokat a megyéket, amelyekben legalább egy állomás található. Hány megye érintett?
10. Feliratozza az állomásokat és a megyéket.
11. Készítsen térképelrendezést: cím, aránymérték, észak-jelző, jelmagyarázat. Exportálás PDF-be.

**Beadandók.** (a) PDF-térkép. (b) Válaszok: > 70 hüvelyk párolgású állomások száma; érintett megyék száma; legmagasabb/legalacsonyabb állomás neve.

#### B változat: Nemzetközi

**Mintaterület.** Bármely ismert ország vagy régió.

**Adatforrások (ingyenes).**

- Ország- és közigazgatási határok: Natural Earth (https://www.naturalearthdata.com/) 1:10m.
- Klimaállomások: GHCN-Daily NOAA-ból (https://www.ncei.noaa.gov/), CSV-ből XY-pontok.
- Alternatíva: ERA5-Land havi potenciális párolgás a Copernicus CDS-ből.

**Eljárás.** Kövesse az A változat lépéseit a saját országos adataival.

**Beadandók.** Ugyanaz mint A változat, kiegészítve az adatelérhetőség összehasonlításával.

#### C változat: Magyar

**Mintaterület.** Magyarország, meteorológiai állomásokkal és megyehatárokkal.

**Adatforrások.**

- Ország- és megyehatárok: KSH / data.gov.hu, vagy EuroGlobalMap. EOV (EPSG:23700) vagy WGS84.
- Meteorológiai állomások: OMSZ (https://www.met.hu/) állomáslista. Alternatíva: E-OBS gridded adatbázis.
- Párolgási adat: ha nem elérhető, használjon éves átlaghőmérsékletet vagy ERA5-Land potenciális párolgást.

**Eljárás.**

1. Hozzon létre projektet `Gy1Projekt` névvel.
2. Adja hozzá a Magyarország és megyehatár shapefile-okat. Ellenőrizze a koordináta-rendszert -- EOV esetén vizsgálja az értéktartományt (Northing: 0--400 000; Easting: 400 000--1 000 000).
3. Adja hozzá a meteorológiai állomásokat. WGS84 esetén vetítse EOV-ra.
4. Kövesse az A változat 3--11. lépését magyar adatokkal.
5. **Kiegészítő feladat.** Válassza ki a Borsod-Abaúj-Zemplén megyei állomásokat. Hány darab van? Mekkora az állomássűrűség (db/1000 km²)?

**Beadandók.** Ugyanaz mint A változat, valamint állomássűrűség-összehasonlítás Magyarország és Texas között.

---

### 2. gyakorlat: Vízgyűjtő-alaptérkép készítése

*Maidment és Tarboton 2. gyakorlata (2018) alapján. Becsült idő: 4--6 óra.*

**Tanulási célok.** (1) Hidrográfiai adatok letöltése. (2) Feature dataset létrehozása definiált koordináta-rendszerrel. (3) Attribútum szerinti kiválasztás és exportálás. (4) Poligonok feloldása (dissolve) vízgyűjtő-kontúr létrehozásához. (5) Pontok hozzáadása koordinátatáblázatból. (6) Előrejelzési adatok elérése.

#### A változat: Eredeti (USA -- San Marcos-medence, Texas)

**Mintaterület.** San Marcos folyó medencéje (HUC-8 = 12100203), USGS 12. vízgazdálkodási régió.

**Adatok.** NFIEGeo_12.gdb a HydroShare-ről. USGS vízmérce-koordináták a NWIS-ből.

**Eljárás.**

1. Töltse le az NFIEGeo_12.gdb-t. Hozzon létre `Exercise2` projektet.
2. Adja hozzá a Geographic feature datasetet: StreamGage, Flowline, Waterbody, Subwatershed, Catchment.
3. Jelenítse meg a Subwatershed réteget HUC_8 szerinti egyedi értékekkel.
4. Válassza ki: `HUC_8 = '12100203'` (32 HUC-12 al-vízgyűjtő).
5. Hozzon létre `SanMarcos` feature datasetet GCS_North_American_1983 koordináta-rendszerrel.
6. Exportálja a kiválasztott al-vízgyűjtőket.
7. Dissolve HUC_8 szerint -> `Basin` kontúr.
8. Szimbolizálja HUC_10 szerinti egyedi értékekkel (5 vízgyűjtő).
9. Töltse le az NLCD területhasználatot, vágja a medencére, számítsa ki az osztályszázalékokat.
10. Hozzon létre vízmérce-pontokat Excel-táblázatból (USGS 08170500 és 08171000 szelvények).
11. Készítsen térképelrendezést.

**Beadandók.** (a) Térkép. (b) Táblázat: HUC-12-ek száma, HUC-10-ek száma, területek, területhasználati százalékok. (c) Catalog-képernyőkép a feature datasettel.

#### B változat: Nemzetközi

**Mintaterület.** 500--5000 km²-es vízgyűjtő bármely országban.

**Adatforrások.**

- HydroBASINS 12. szint (https://www.hydrosheds.org/).
- HydroRIVERS (https://www.hydrosheds.org/products/hydrorivers).
- ESA WorldCover 10 m (https://esa-worldcover.org/) vagy Copernicus Global Land Cover.
- GRDC vízmérce-katalógus (https://www.bafg.de/GRDC/).

**Eljárás.** Kövesse az A változat logikáját a globális adatokkal. Hasonlítsa össze a HydroBASINS és az esetleges nemzeti vízgyűjtő-határ adatbázist.

#### C változat: Magyar

**Mintaterület.** Sajó vízgyűjtő (~12 700 km² összes, magyar rész ~6400 km²).

**Adatforrások.**

- Vízgyűjtő-határok: OVF részvízgyűjtő-határok (https://geoportal.vizugy.hu/) vagy HydroBASINS.
- Vízhálózat: EU-Hydro (https://land.copernicus.eu/imagery-in-situ/eu-hydro) vagy HydroRIVERS.
- Területhasználat: CORINE Land Cover 2018 (https://land.copernicus.eu/pan-european/corine-land-cover).
- Vízmércék: Sajó Felsőzsolcánál, Hernád Hidasnémetinél, Bódva Szendrőládnál.
- Koordináta-rendszer: EOV (EPSG:23700).

**Eljárás.**

1. `Gy2Sajo` projekt, EOV koordináta-rendszer.
2. Adja hozzá a részvízgyűjtő-határokat. HydroBASINS esetén vetítse EOV-ra.
3. Válassza ki a Sajó vízgyűjtőt alkotó al-vízgyűjtőket. Exportálás és dissolve -> medence-kontúr.
4. EU-Hydro/HydroRIVERS vágása a medencére.
5. CORINE 2018 vágása, osztálystatisztika: mezőgazdasági (2xx), erdő (3xx), beépített (1xx), víz (5xx).
6. Vízmérce-pontok létrehozása EOV-koordinátákkal. *Mindig az értéktartomány alapján azonosítsa az oszlopokat!*
7. Térképelrendezés.

**Kiegészítő feladatok.** Hasonlítsa össze a dissolve-területet az OVF hivatalos adatával. Azonosítsa a szlovákiai részvízgyűjtőket (a Sajó Szlovákiában Slaná néven ered). Tárgyalja a határon átnyúló adatkezelés kihívásait.

---

### 3. gyakorlat: Térelemzés -- Lejtés, kitettség és folyásirány

*Tarboton és Maidment 3. gyakorlata (2018) alapján. Becsült idő: 5--7 óra.*

**Tanulási célok.** (1) Lejtés, kitettség és folyásirány számítása különböző algoritmusokkal. (2) Kézi számítás és GIS-eredmény összehasonlítása. (3) ModelBuilder-munkafolyamat automatizálás. (4) Térbeli interpoláció és vízgyűjtő-átlagos csapadékszámítás. (5) Raszterkalkulátor használata hidrológiai vízmérleghez.

#### A változat: Eredeti (USA)

Két rész: (1) szintetikus DEM kézi számításokhoz; (2) San Marcos-medence interpolációhoz. Adatok: `http://hydrology.usu.edu/dtarb/giswr/2018/Ex3Data.zip`

**1. rész: Lejtésszámítás.** Használja a megadott 5×4-es rácsot (cellaméret 10 m). Számítsa ki a lejtést az A cellánál (26,4) három módszerrel: ESRI felületi lejtés, D8 és D-végtelen. Ellenőrizze GIS-ben.

**1.3. rész: ModelBuilder.** Építsen munkafolyamatot: ASCII to Raster > Flow Direction (D8) > Slope > Aspect > Flow Direction (DINF). Futtassa `demo.asc`-n.

**2. rész: Interpoláció és vízmérleg.** Számítson átlagos magasságot, interpoláljon csapadékot, számítson lefolyási hányadot.

#### B változat: Nemzetközi

Copernicus DEM GLO-30 vagy SRTM 30 m. ERA5-Land csapadék és PET. Az 1. rész (kézi számítás) helyfüggetlen. A 2. résznél használja az ERA5 gridded adatokat interpoláció helyett.

#### C változat: Magyar

DDM-5 vagy EU-DEM a Hernád-almedencéhez. CARPATCLIM csapadék és PET. Hasonlítsa össze a számított lefolyást a Hernád hidasnémeti vízmércéjén mért átlagos éves vízhozammal (~15--20 m³/s, ~5400 km² vízgyűjtő).

**Kiegészítő feladat.** A Hernád vízgyűjtő határon átnyúló (Hornad Szlovákiában). Tárgyalja, hogyan szerezné be és egyesítené a szlovák DEM- és klímaadatokat. Milyen koordináta-rendszeri kérdések merülnek fel az EOV és az S-JTSK (EPSG:5514) kombinálásánál?

---

### 4. gyakorlat: Vízgyűjtő- és vízhálózat-lehatárolás

*Tarboton és Maidment 4. gyakorlata (2018) alapján. Becsült idő: 6--8 óra.*

**Tanulási célok.** (1) Online és GIS-eszközök használata vízgyűjtő-lehatároláshoz. (2) DEM-csempék letöltése és egyesítése. (3) A teljes hidrológiai terepelemzési sorrend végrehajtása: kitöltés > folyásirány > akkumuláció > vízhálózat > szakaszkód > vízgyűjtő. (4) DEM-hálózat és hivatalos hidrográfia összehasonlítása. (5) Vízgyűjtőterület, vízhálózat-hossz és vízhálózati sűrűség számítása.

#### A változat: Eredeti (USA -- Logan-folyó medence, Utah)

**Mintaterület.** USGS 10109000, Logan River above State Dam. ~554 km², 41,7443° É, 111,7819° Ny.

Részletes eljárás: online vízgyűjtő-lehatárolás, DEM-csempék letöltése és egyesítése, puffer, kivágás, vetítés (UTM 12N, 10 m), Fill, Flow Direction, Flow Accumulation, Stream Link, Watershed, Stream to Feature, Raster to Polygon. NHDPlus összehasonlítás.

#### B változat: Nemzetközi

Copernicus DEM GLO-30, HydroRIVERS összehasonlításhoz. 200--1000 km² hegyi vízgyűjtő.

#### C változat: Magyar

**Mintaterület.** Bódva vízgyűjtő (~900 km²), az Aggteleki-karszt és a Cserehát területén. Vízmérce: Bódva Szendrőládnál.

**Adatforrások.** DDM-5 vagy EU-DEM, EU-Hydro vagy OVF hidrográfia. EOV (EPSG:23700).

**Eljárás.** DEM előkészítés, hidrológiai elemzés, vízhálózat-összehasonlítás az EU-Hydro vagy magyar adatbázissal.

**Karszt-szempont.** A Bódva-vízgyűjtő tartalmazza az Aggteleki-karsztot, ahol a felszíni és a felszín alatti vízlefolyás jelentősen eltér. Azonosítsa azokat a területeket, ahol a DEM-alapú hálózat nem tükrözi a valós vízlefolyási mintázatot. Tárgyalja, miért vannak alapvető korlátai a DEM-alapú terepelemzésnek karsztos régiókban.

---

### 5. gyakorlat: HAND és árvízi elöntéselemzés

*Tarboton 5. gyakorlata (2018) alapján. Becsült idő: 6--8 óra.*

**Tanulási célok.** (1) HAND-raszter számítása DEM-ből. (2) Folyószakasz hidraulikai tulajdonságainak meghatározása HAND-ból. (3) Manning-egyenlettel szintetikus vízhozamgörbe készítése. (4) Árvízi elöntési térkép készítése adott vízhozamra. (5) Árvízi hatásértékelés GIS-átfedés-elemzéssel.

#### A változat: Eredeti (USA -- Onion Creek, Texas)

**Mintaterület.** Onion Creek, a Colorado folyó mellékfolyója Austin közelében. Súlyos árvizek 2013 októberében és 2015 májusában.

**Adatok.** `http://www.caee.utexas.edu/prof/maidment/giswr2018/Ex5/Ex5Data.zip` -- OnionHand.gdb és Onion3.tif.

**Eljárás.**

**1. rész: HAND-számítás.** Folyóforráspont-azonosítás (dangling vertex), raszterizálás, Fill, D8 Flow Direction, Flow Accumulation (súlyozott), Con (folyóraszter), DINF Flow Direction, Flow Distance (függőleges = HAND). Vízhálózat-lehatárolás: Stream Link, Watershed, Stream to Feature, Raster to Polygon.

**2. rész: Hidraulikai tulajdonságok.** Egy vízgyűjtő-poligon kiválasztása (FeatureID = 5781733). HAND-kivágás, vízszintenként (h = 1--14 m) cellastatisztika számítása, Manning-egyenlet, vízhozamgörbe.

**3. rész: Elöntési térkép.** 2013-as árvízi vízhozamhoz (~2782 m³/s) vízszint meghatározása, elöntési mélységraszter, átfedés a címpontokkal.

**Beadandók.** (a) HAND-térkép. (b) Hidraulikai táblázat. (c) Vízhozamgörbe. (d) Elöntési térkép. (e) Érintett címek száma.

#### B változat: Nemzetközi

Copernicus DEM GLO-30 (vagy nemzeti LiDAR), HydroRIVERS, OpenStreetMap épületek, Copernicus EMS összehasonlításra.

#### C változat: Magyar

**Mintaterület.** Sajó Miskolc közelében, Felsőzsolca és a Tisza-torkolat közötti szakasz. Súlyos árvizek 2010 júniusában és 2013 májusában.

**Adatforrások.**

- DEM: DDM-5 (5 m, ideális) vagy Copernicus DEM GLO-30 / EU-DEM (25 m, tartalék).
- Vízhálózat: EU-Hydro vagy OVF.
- Épületek: OpenStreetMap Magyarország (Geofabrik: https://download.geofabrik.de/europe/hungary.html).
- Hivatalos árvízveszélyi térkép: OVF árvízi kockázati térkép az EU Árvíz Irányelv (2007/60/EK) alapján.
- Manning-n: magyar alföldi folyókra 0,03--0,05 (főmeder), 0,05--0,10 (ártér).

**Eljárás.**

1. DEM előkészítés: DDM-5 (EOV) vagy EU-DEM átvetítése EOV-ra, 10 m-re.
2. Folyóforráspont-raszter készítése EU-Hydro/OVF folyóvonalakból.
3. Fill > D8 > akkumuláció (súlyozott) > Con (folyóraszter) > DINF > Flow Distance (HAND).
4. HAND osztályozás: 0--2 m (rendkívül magas kockázat), 2--5 m (magas), 5--10 m (közepes), >10 m (alacsony).
5. Válasszon ki egy veszélyeztetett szakaszt (pl. Felsőzsolca környéke). HAND-kivágás, hidraulikai számítás, vízhozamgörbe (n = 0,04, mederesés a DEM-ből).
6. Mértékadó árvíz (2010-es Sajó-árvíz, ~1200 m³/s csúcsvízhozam Felsőzsolcánál): vízszint meghatározása, elöntési térkép.
7. Átfedés OpenStreetMap épületkontúrokkal. Érintett épületek száma.
8. Összehasonlítás az OVF hivatalos árvízveszélyes területi térképpel.

**Kiegészítő feladatok.**

- Határozza meg a HAND-értéket a Miskolci Víztisztító Telepnél (EOV ~Y = 310 000, X = 775 000). Mekkora vízszint szükséges ennek a kritikus infrastruktúrának az elöntéséhez?
- A 2010-es árvíz során Felsőzsolcánál szükséggátat kellett építeni. Azonosítsa a gátak helyét a DEM-en, és tárgyalja, hogyan befolyásolják a gátak a HAND-alapú árvíztérképezést.

**Beadandók.** (a) HAND-térkép osztályozott jelkulccsal. (b) Hidraulikai táblázat és vízhozamgörbe. (c) Elöntési térkép a 2010-es mértékadó árvízre. (d) Érintett épületek száma. (e) Összehasonlítás az OVF árvízveszélyi térképpel. (f) A HAND korlátai védművekkel ellátott ártéren.

---

### Adatforrás-összefoglaló változatonként

| Adattípus | USA (eredeti) | Nemzetközi | Magyar |
|-----------|---------------|------------|--------|
| Közigazgatási határok | US Census TIGER | Natural Earth | KSH / data.gov.hu |
| Vízgyűjtő-határok | NHDPlus WBD / HydroShare | HydroBASINS | OVF / HydroBASINS |
| Vízhálózat | NHDPlus flowline | HydroRIVERS | EU-Hydro / OVF |
| DEM | USGS 3DEP (1/3") | Copernicus GLO-30 / SRTM | DDM-5 / EU-DEM |
| Területhasználat | NLCD 30 m | ESA WorldCover 10 m | CORINE 100 m |
| Csapadék | NOAA GHCN / PRISM | ERA5-Land / CHIRPS | OMSZ / CARPATCLIM |
| Vízmércék | USGS NWIS | GRDC | OVF |
| Árvíz-előrejelzés | National Water Model | EFAS / GloFAS | EFAS / OVF |
| Épületek | Census címpontok | OpenStreetMap / MS Buildings | OpenStreetMap |
| Hivatalos árvíztérkép | FEMA | Nemzeti megfelelők | OVF árvízi kockázati térkép |
| Koordináta-rendszer | NAD83 / UTM | WGS84 / UTM | HD72/EOV (EPSG:23700) |
