# Chapter 5: Aquifers, Wells, and Boreholes

GeologyPoints represent point features such 
as springs, caves, sinks, and observation points. 
GeologyLines describe line features such as faults 
contacts, and dikes. GeologyAreas describe areal 
features such as rock units and alteration zones. J 
iw) . . 
SI © (Yo) Foleo WY axe) [a) mm C1-Lo) (oleh Mil al-Mar- Tale | be} 
8 Le T=To] (ole Nar] 
pa 4 5 de @ |Point, line, and polygon Pa 
= features from geologicmaps » ¢ ° 
= 2S Z 
w |Fieldname Description Giz 
a HydrolD Unique feature identifier in the geodatabase used for creating 
S telatiqgnships between classes of the data model. 
‘2. HydroCode Permanent public identifier of the feature used for relating 
= features with external information systems. 
wn 
£& |GeoAbbrev Abbreviation of the geologic feature. Used in map legends and 
B labeling. | 
Description A text description of the feature. 
HGUID Hydrogeologic unit identifier. Relates the feature with a 
hydrogeologic unit. 
HGUCode Text code for storing the permanent identification code of 
hydrogeologic units. 
FType Distinguishes between types of geologic features. 
Figure 4.5 GeologyPoint, GeologyLine, and GeologyArea 
feature classes represent data from geologic maps. Geology component 
The attributes of the feature classes are described 
in figure 4.5. The features have HydroID and 
HydroCode attributes for internal and external 
identification. GeoAbbrev contains the abbrevia- 
tion of the unit in the map and map legend, and 
Description provides a more detailed text descrip- 
tion of the unit. HGUID and HGUCode classify 
the units into hydrogeologic units (see chapter 6 
for a more detailed description of the HGUID and 
HGUCode attributes). FType classifies geologic 
features by their type (e.g., spring, contact, fault, 
dike, rock, and alteration). 
Geologic maps define the spatial extent, 
location, and topology of stratigraphic units, 
which are rocks or bodies of strata recognized as a 
unit for description, mapping, or correlation pur- 
poses. For example, a geologic map of the Edwards 
Aquifer recharge zone defines fifteen stratigraphic 
units (figure 4.6). These units can be grouped into 
more general units (e.g., Kainer Formation and 
Person Formation), and can also be grouped into 
aquifers and confining units. 
Figure 4.6 Correlation chart showing 
stratigraphic units, formations, and 
hydrogeologic units in the Edwards 
Aquifer recharge zone. ee 
e 2) Upper confining units, undivided 
A E OD =| 
< es Navarro and Taylor Groups, undivided ° c be — 
ey & Austin Group 
S %S 
; S Eagle Ford Group 
a 5 = 5 Buda Limestone 
=) 5 : 
a Del Rio Clay 
c . 
wn Georgetown Formation 
Q 
8 5 Cyclic and marine member roe =| + foe 3 
S & 2 Ss Leached and collapsed member 
a i) YF 
2 2 ae iS Regional dense member 
s 3 & a Grainstone member 3 < 
is 5 2 Kirschberg evaporite member 
Ny E Dolomitic member ) i Basal nodular member 
en een eee , 
5S ese Upper member of the Glen Rose Limestone 
222| 22 aS a Sel Sg 
1S) 
43 


CHAPTER 4: GEOLOGIC MAPS 
The datasets composing the recharge zone 
map include polygons describing the extent of 
geologic members, line features describing faults 
and contacts, and point features showing the loca- 
tion of caves/sinks and springs (figure 4.7). These 
features can be used in groundwater projects 
to help define the extent of hydrogeologic units 
and provide information on sources (caves/sinks 
that recharge the aquifer) and discharge features 
(springs) and flow conduits /barriers (faults). Implementation 
This section outlines the main steps involved in 
implementing the geology component of the data 
model. The first steps are to refine the geodatabase 
design to meet your specific project needs (see 
chapters 2 and 9 for a detailed description of these 
steps). Once the geodatabase is built, you can load 
data into the geology feature classes. Then you 
can assign HydroIDs to the imported features to 
US 29 zi Upper confining units, undivided 
Knit Navarro and Taylor Groups, undivided 
[Ka] Austin Group Mag 
[Ker] Eagle Ford Group 
[EKGS) Buda Limestone 
(ERA) (Del Rio Clay 
(xed Georgetown Formation 
[ Kpem | Cyclic and marine member 
{Kple | Leached and collapsed member 
[Kor] Regional dense member 
BS Grainstone member 
Kirschberg evaporite member 
Dolomitic member 
[EG] Basal nodular member 
[ [are | Upper member of the Glen Rose Limestone 
Kaains jer1bojoad °S'f ’SQ0z "|e 18 BWO}g jo AsaqinoD 
Contact 
Shy) 235 Fault—Dashed where inferred. U, upthrown side; D, downthrown side. 
Displacement amount in feet 
Geographic Information System polygon extent of county maps 
° Cave or sink 0) 4 
5 e Spring 
44 Figure 4.7 Geologic map of the Edwards Aquifer recharge zone. The different colored polygons represent different 
stratigraphic units, and the points and lines represent faults, springs, and caves or sinks. 


create a unique identifier that can be the basis for 
queries and relationships within the geodatabase. 
You can then apply tools to the imported data to 
calculate new attributes and create new features. 
Finally, you can use the results of this process to 
create products such as maps, scenes, and reports. 
The following checklist provides a summary of 
the main steps in implementing this component. 
Checklist 
1) Create the classes of the geology component 
(manually using ArcCatalog or by importing from 
an XML schema) 
2) Define the spatial reference, and add project spe- 
cific classes, attributes, relationships, and domains 
as necessary 
3) Document datasets and changes made to the data 
model 
4) Import data into the geology classes 
5) Assign key attributes to uniquely identify the 
features and establish relationships 
6) Apply tools to create new features and calculate 
attributes 
7) Visualize data and create products (maps, scenes, 
reports) Implementation 
The following example demonstrates how 
data from a USGS geologic map of the Edwards 
Aquifer recharge zone were incorporated into the 
geology component of the data model. The Geol- 
ogyArea feature class was populated with map 
units from a geologic map database (figure 4.8). 
After importing the features, each feature was 
given a HydrolID to uniquely identify it within 
the geodatabase. GeoAbbrev contains the abbre- 
viation of the unit in the map, and Description 
provides a more detailed text description of the 
unit. HGUID and HGUCode values were given 
to the features to classify the members into 
more general hydrogeologic units. As shown in 
the map legend in figure 4.9, a number of map 
members (with different abbreviations) were 
grouped and classified as more general units (e.g., 
Person, Kainer, etc.). The FIype attribute classi- 
fies geologic features by their type. In this case all 
the units were given a “Map unit” feature type. 
Where appropriate, FType values can be defined 
as coded value domains. 
__|Map Unit 
Figure 4.8 Each row in the GeologyArea feature class represents a map unit. 
45 


CHAPTER 4: GEOLOGIC MAPS 
Similarly, point and line features from the 
geologic map were imported and attributed in the 
GeologyPoint and GeologyLine feature classes. In 
this case, GeologyLine features represent mapped 
faults, and GeologyPoints represent caves/sinks 
and springs. As needed, more specific attributes 
can be added to the feature classes to represent 
features of interest in more detail. For example, 
in the map shown in figure 4.9, a FaultType field 
was added to the GeologyLine features to classify 
different types of faults (certain or inferred). 
References 
Geologic Data subcommittee, Federal Geographic Data 
Committee, FGDC Digital Cartographic Standard for Geo- 
logic Map Symbolization. 2006. FGDC Document Number 
FGDC-STD-013-2006. Raines, Gary L., Jordan T. Hastings, and Lorre A. Moyer. 
2007. Proposed ArcGeology Version 1, A Geodatabase 
Design for Digital Geologic Maps using ArcGIS. U.S. Geo- 
logical Survey, Reno, Nevada. 
Blome, Charles D., Jason R. Faith, Diana E. Pedraza, George 
B. Ozuna, James C. Cole, Allan K. Clark, Ted A. Small, 
and Robert R. Morris. 2005. Geologic map of the Edwards 
Aquifer recharge zone, south-central Texas. U.S. Geological 
Survey Special Investigations Map 2873. 
GeologyPoint GeologyLine 
FType FaultType 
@ Cave 
@ Spring GeologyArea 
HGUCode 
fault-certain Frag] Kainer 
en fault-inferred fees | Person 
es Upper Glen Rose 
ae Upper confining units 
A&AANs |22160|0a5 sq jo Asayinod ejeq 
Figure 4.9 GeologyPoint, GeologyLine, and GeologyArea representing features from a geologic map. 
46 


pieog juawdojanaq 
4a1eM Sexe} ay} pue Aaains jed1H0}0ay *s‘q Jo Asaqinod ejeq x Aquifer 
>» Aquifer boundaries and zones within them such as outcrops and confined zones. 
i Representation: Polygon features. 
Well 
Representation of well locations and attributes. 
Representation: Point features. 
BorePoint and BoreLine 
Spatial representation of 3D data along a borehole such as hydrostratigraphy 
and well construction. F 
Representation: PointZ and PolylineZ features. 
BoreholeLog 
Tabular representation of 3D data along a borehole such as hydrostratigraphy 
and well construction. 
Representation: Table. 
AQUIFER MAPS AND WELL DATABASES ARE PROBABLY THE MOST COMMON 
groundwater data products developed on national, state, and local scales, and both 
serve as important resources for groundwater projects. This chapter shows how 
the Arc Hydro Groundwater data model represents aquifer and well features and 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
MM) Pecos Valley 
Hl Seymour 
©) Gulf Coast 
WE Carrizo - Wilcox (outcrop) 
Carrizo - Wilcox (subcrop) 
MM Hueco - Mesilla Bolson 
I) Ogaliala 
Edwards - Trinity Plateau (outcrop) 
(> Edwards - Trinity Plateau (subcrop) 
WM Edwards BFZ (outcrop) 
VZA Edwards BFZ (subcrop) 
BE Trinity (outcrop) 
SSN Trinity (subcrop) 
NOTE: Chronology by Geologic age 
QUTCROP (portion of 2 watertesrng rock unt exposed & he land surface) 
SUBCROP (porton of a waterdeanng rock Unit existing below other rock unas} 
oT 
Figure 5.1 The major aquifers of Texas. 
48 S 
Map upcates Qecember 2006 dy Mark Hayes GSP pieog juawudojanag Jalen sexal jo Asayino> 


how the linkage between the two is established, 
in addition, the chapter discusses how 3D infor 
mation recorded along boreholes 
Visualized, 1 stored and 
Aquifer maps and aquifer features 
An aquifer is a group of formations, a single 
geologic formation, or part of a formation that 
contains sufficient saturated permeable material 
to yield 
springs and wells significant quantities of water to 
(http: //pubs.usgs.gov/gip/ 
gu/glossary.htm1). Aquifer maps are common 
data products developed on national, state, and 
local Jevels (figure 5.1). 
boundary of aquifers over a given region and can The maps “ebb the 
aiso distinguish between zones within an aquifer. 
Well databases and well features 
A water well is a human-made excavation or 
structure created in the ground to access ground- 
~©> 
~> QA 
AW JO AS 
Ag Ot n 3 
WRAY Aguiler maps and aquifer features 
6ALA ee ; iA a4 ¢ water Wells are among the oldest and most > 
important structures made by humans. Wells ) 
= have pla yes a crucia) role in the development o 
Svilizations since ancient MES, AS thes y pu wide PY Pp 
JO000K -¢ ~ ae 
PPO? is communitic 4 4 * 7 @ 
acces to groundwater that ¢ 
¢ lve : a ae ‘< even during dry periods when surface water is not 
Bayh zlel é or oe Se ; 144 4 : 
available. The importance of wells is documented j 
in numerous Siterary references, and archeo- 
logical findings show that wells have supported 
V228K4 Leena AOE fa é communities for thousands of Wells rem y 
OUVEMBY importar ib COBY, | With at Jeast 1.5 billion 
people WOW ide re ying On Zeon iniG IwWiater aS Hier 9 7) 
only ROUICeL drinking Water (http: //waon.usaid. 
gov/our_work/environgent/water/groundwater 
- 2 y A +4 
mgmt tml). Figure le shows € BAD) ics OF WEUS 
me : “g 
drilled within the Edwards Aquifer pipiae 
Wells are designed for many reasons: to ) 
prod uce water from aquifers, to monitor water 
levels and quality, and to inject (disch aah onu- 
tions into the subsurface 3 IONS INTO Te SUDSUSTAce. 
community, the terms well and borehole are com- 
; calcar ; ie Jat - «sa cot 
monly used interck lange bls y. in this book, we refex 
stor tO ace arc Z as 3 =< = 
commdered the larccest ator a ne wid 
49 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
to a borehole as a hole drilled into the subsurface, 
and we refer to a well as a borehole that is related 
to water extraction, injection, or monitoring. 
Cities, counties, and states document and issue 
permits for well construction. Many of these 
agencies have established well databases con- 
taining information on well locations and well 
properties describing the construction and usage 
of wells. These databases provide important 
information for the development of groundwater- 
management plans, groundwater simulation 
models, and research studies dealing with ground- 
water availability and water quality. Some data- 
bases provide detailed information on the well 
construction, water usage, and hydrostratigraphy, 
while others contain only basic information such 
as the owner and location of the wells. Various 
standards and guidelines have been established 
for data describing groundwater wells. One is the 
standard developed by the American Society for 
Testing and Materials (ASTM), which describes 
welldata 
* waterlevel 
state_well_number 
county_code 
basin state_well_number 
pn_well_visit_mark 
depth_from_lsd 
mm_date zone 
dd_date region_number 
yy_date previous_well_nu 
measurement_numbe latitude 
measuring _agenc lat_dec 
method_of_meas longitude 
remark long_dec 
are owner_1 
r owner_2 
waterquality driller 
s driller_2 
state_well_number source_of_coords 
pieog Juatudojanag Jayep Sexal Jo Asayinod ejeq mm_date aquifer_code 
dd_date aquifer_idl 
yydate aquifer_id2 
sample_number aquifer_id3 
sample_time elev_of_Isd 
temp_centigrade meth_of_meas_elev 
top_s_interval user_code_econ 
bottom_s_interval date_drilled 
samp_int_aqcode well_type 
collection_remarks well_depth 
reliability_rem source_of_depth 
collecting agency type_of_lift 
lab_code 
50 type_of_power the minimum set of data elements to identify a 
groundwater site (ASTM 2004). Another is the 
Australian National Groundwater Data Trans- 
fer Standard (Australian National Groundwater 
Committee 1999), which defines a set of data struc- 
tures and standards for core groundwater data 
used in Australia. Commercial software applica- 
tions (e.g., SiteFX, HydroGeo Analyst, and EQulIS) 
provide relational database designs to store 
well-related information and tools to view and 
analyze the data. The Arc Hydro Groundwater data 
model is not intended to replace these standards 
and applications but to provide geospatial classes 
for storing, viewing, and analyzing these data 
within ArcGIS. Rather than trying to be all inclu- 
sive and develop a new comprehensive standard, 
we asked ourselves, what are the common attri- 
butes in these well databases, and how can we best 
store, view, and analyze them within a GIS? This 
approach provides a simple template that users can 
customize as needed for their particular project. 
casing 
* 
state_well_number | 
group_number 
c_s_0_indicator 
diameter_csg_scn 
top_depth 
bottom_depth 
Figure 5.3 Example of a central well table in the Texas 
Water Development Board groundwater database. 
The “welldata” table in the center contains properties 
of wells defining their location, ownership, depth, etc. 
This central table is related through a well identifier 
(the state well number) to other tables containing 
information on well construction and monitoring 
data such as water levels and water quality, 


It is common for groundwater databases to 
have a central table that describes the location 
of wells and their properties (e.g., depth, water 
use, and owner). The central table is usually 
linked with additional tables describing infor- 
mation on the well construction, measurements 
of water levels and water quality taken at the 
well, and descriptions of the formation mate- 
rial observed along boreholes. For example, the 
groundwater database maintained by the Texas 
Water Development Board (TWDB) is available 
for public use and downloadable as a Microsoft 
Access database from the TWDB Web site. The 
main table in the database is the “welldata” table 
(figure 5.3). Each row in the table represents a 
single well, and fields in the table describe the 
well’s properties, including its geographic coor- 
dinates, land surface elevation, depth, owner, 
driller, and related aquifers. Each well in the 
TWDB groundwater database is assigned a “state 
well number” that identifies the well within the Well databases and well features 
database. Based on this number, associations are 
created to relate wells in the welldata table with 
data in other tables containing information on the 
casing intervals along the well, and on the water 
quality and water level sample data. 
Data from the well database can be visualized 
in a map environment by representing wells as 
point features, and the points can be the basis 
for querying and displaying well-related data. A 
good example of such a system is the Texas Water 
Information Integration & Dissemination (WIID) 
system. The WIID system provides a Web-based 
mapping interface for retrieving well data from 
drilling reports and groundwater monitoring data. 
When selecting a well in the map, basic informa- 
tion on the well is provided. This includes the 
well’s owner, water use, location, elevation, depth, 
and associated aquifer (figure 5.4). Upon request, 
users can retrieve data on water quality, water 
levels, well casing, and the driller report for the 
well. Similar systems have been developed for 
oaseon 
gsss0e3 
pieog juawidojanag Jaye sexe Jo Asaqyinod eyeq 
oe ae 
Mbccona (84.11) | Pree) 
Owner 
San Antonio Water Sys. S$ 7a7 931 TWDB Ground Datab Result ~ ae See hice’ roundwater Database Query OSU eapesstai — Geist 
aay, cae Sas See eee — goyeane | es36so4 
REPORTED WATER WELL DATA ON STATE WELL NUMBER = 6835905 | #esesor o-64 | CEIGS 
| gastana | gaaosoa 
Query for another State Well Number: | gensfor senen ea | 
| Pesseos : 64: Puree pina \ Se 364 
ee ee aera gigi ee Nee 
15946 \ na HOO ISON | 
\ gsseror 
TWDB GROUNDWATER DATA (Explanation) 
Water Use Elevation Well Depth Water Level Water Quality Aquifer Code Latitude Longitude COUNTY_CODE WELL_TYPE ares | FIstrEry 
geste snes 
pexores 
\ Lon 
ral e208 aed Ero 
nen pnd 
o81eaes 
A 2 sam goer? 
bers pnvors6 egress) 
= sree 
me 
a ‘2 
N Yi 21ZEBFZA 292414 963833 23 w 0.68 
Figure 5.4. The Texas Water Information Integration & Dissemination system (http://wiid.twdb.state.tx.us) is an example of 
a Web-based mapping interface for retrieving well data from a groundwater database. 
51 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
many U.S. states (e.g., Michigan, Washington, 
Illinois) and on the national level (e.g., the USGS 
National Water Information System). 
A theme that emerges from these information 
systems is the development of a 2D spatial 
representation of wells (points on a map) to which 
other data are related. Thus, the first step in spa- 
tially enabling well databases is to create a spatial 
representation of well features. In the groundwater 
data model, wells are represented as 2D points 
with attributes describing the properties of the well. 
Related data, such as well construction, hydro- 
stratigraphy, and monitoring information, are asso- 
ciated with well features. The data model provides 
a basic set of well attributes for identification, 3D 
representation, and linkages to aquifer and hydro- 
geologic units. While many groundwater databases 
contain large sets of fields describing wells, the 
groundwater data model focuses on providing a 
(Garam a 
) = Aquifer 
pieog JuaWUdojanag Ja}e/ Sexa| pue Aadins je21H0j0a5 ‘s'fq Jo Asaqinod ejeq HydrolD 
HydroCode 
WelllD 
| Material 
HGUID 
HGUCode 
PointElev minimum set of attributes that help integrate the 
well data with GIS. This set of attributes can be 
expanded for each project as needed. 
Geodatabase representation of 
aquifers and wells 
The Aquifer feature class is a polygon feature class 
for representing data from aquifer maps. Each 
Aquifer feature in the feature class represents 
an aquifer boundary or part of an aquifer (see 
figure 2.10 for a detailed description of the attri- 
butes of the Aquifer feature class). The HydroID 
and HydroCode attributes provide the means for 
internal and external identification (figure 5.5). For 
example, the major aquifers of Texas have a unique 
identifier used by Texas state agencies. The aqui- 
fer identifier of the Edwards Aquifer is 11, thus 
when creating aquifer features, the HydroCode of 
Figure 5.5. Analysis diagram describing 
the datasets for representing aquifers, 
wells, and boreholes. 
| BottomElev 
| FType 
os RefElev 
FromDepth 
ElevUnits 
; Material os *, 
| HGUID E 
_ | HGUCode 
LogType 
52 


features representing the Edwards Aquifer is set 
to 11. This lets users link Aquifer features in an 
Arc Hydro geodatabase with data from external 
information systems. The Name attribute is used 
to symbolize and label features, and the HGUID 
(hydrogeologic unit ID) relates aquifer features 
with more detailed descriptions of hydrogeologic 
units defined in the HydrogeologicUnit table 
(see chapter 6 for a more detailed description of 
hydrogeologic units). HGUID is also used to 
group aquifer features. For example, figure 5.6 
shows a dataset describing the Edwards Aquifer 
that is composed of a number of polygon features 
(each with a unique HydroID). The features in 
the example are indexed by HGUID = 4 (which 
is defined in the HydrogeologicUnit table as the 
[Poly 
4 eee tt 9} bh 
5 |Polygon | 123/11 
Record: Af [ >| | 
pieog Juatuudojanag Jae sexe] Jo Asayinod ejeq Geodatabase representation of aquifers and wells 
boundary of the Edwards Aquifer). Thus, the 
HGUID can be used to group, display, or query the 
features representing the Edwards Aquifer. In the 
following example features are also symbolized 
by the FType to differentiate between outcrop and 
confined zones. 
The Well feature class is a point feature class 
for representing well locations and basic well 
attributes for identification, 3D representation, 
and linkages to aquifer and hydrogeologic units 
(see figure 2.11 for a detailed description of the 
attributes of the Well feature class). HydroID and 
HydroCode are used for internal and external 
identification of the features. Each Well feature is 
assigned a HydroID that becomes its unique iden- 
tifier within the geodatabase. The HydrolD is the 
Figure 5.6. Polygon features representing the Edwards Aquifer are indexed by HGUID so that a group of features repre- 
sents a single aquifer. 
53 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
basis for relating data in other feature classes and 
tables to Well features. The HydroCode is the per- 
manent public identifier that helps maintain the 
original identification code of the well. For exam- 
ple, HydroCode can contain the state well number 
from a state groundwater database. The LandE- 
lev (land elevation) and WellDepth (well depth) 
attributes describe the 3D geometry of the well, 
and AquiferID (Aquifer identifier) and AqCode 
(Aquifer Code) associate wells with aquifers. 
HGUID relates the well to hydrogeologic units 
defined in the HydrogeologicUnit table. Figure 5.7 
shows an example of Well features in the Edwards 
Aquifer created by importing data from the TWDB 
groundwater database. 
ee Attributes of Well _ 
1 <n = ——+t —— 
% 2| / 6830201 aera = | 
[143 /218EDRDA | Relationships between Aquifer and 
Well features 
In the groundwater data model, Well and Aquifer 
features are related to provide the capabilities to 
query and display information regarding specific 
aquifers. The association between Aquifer and Well 
features is a one-to-many (1:M) relationship, thus 
an Aquifer feature can be associated with one or 
more Well features. The relationship is based on key 
fields in the Aquifer and Well feature classes, such 
that the AquiferID of Well features is set equal to 
the HydroID of an Aquifer feature. In the follow- 
ing example (figure 5.8), a Well feature represent- 
ing a public water supply well is attributed with an 
113 |218EDROA | 
pieog juawdojaaeq ADJEM\ SEXB] JO Asayinoo ejyeg 
Figure 5.7 Well features representing well locations and attributes of wells in the Edwards Aquifer. 
54 


AquiferID of 114. This relates the well to an Aquifer 
feature with HydroID 114, which is one of the fea- 
tures representing the Edwards Aquifer outcrop. 
The association between Aquifer and Well features 
enables querying well-related data for specific 
aquifers. Well features also can be labeled and sym- 
bolized by their related aquifer using the aquifer 
identifier (AquiferID) and code (AqCode) attributes. 
In some cases wells are associated with more 
than one aquifer. The assignment of multiple 
aquifers can result from a well being screened across 
multiple aquifer units or from the assignment of 
aquifers mapped at different scales. For example, 
wells stored in the USGS National Water Informa- 
tion System (NWIS) are indexed with a national 
aquifer and a local aquifer. To support the associa- 
utes of Well 
[OSIECTIO [shape | Hydro] 
58 | 5857305 
Record: a Cy >| | 
pieog juauidojanag sa}e\ Sexe} Jo Asaqinod ejeq Relationships between Aquifer and Well features 
tion with both, we can simply add another aquifer 
identifier attribute to the Well feature class (egy 
AquiferID2) and add another relationship that asso- 
ciates the new aquifer identifier with the HydroID 
of Aquifer features. This pattern can be repeated 
to create as many aquifer-well relationships as 
needed in your project. You can also create a many- 
to-many (M:N) association between the Aquifer 
and Well feature classes (our experience shows that 
managing an M:N relationship is more challenging 
from a user perspective). If your datasets include 
a many-to-many relationship between aquifer and 
wells and it is important for your project to support 
this relationship, you should consider using one of 
the approaches described above to represent such 
an association (see also chapter 9). 
Records (1 out of 3613 Selected) 
Well HydrolD = 53]. 
Figure 5.8. Relationship between Aquifer and Well features. The AquiferlD of a Well feature is equal to the HydrolD of the 
related Aquifer feature. 
55 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
Steps for creating Aquifer and Well 
features 
The first steps for implementing this component 
are to refine the geodatabase design to meet your 
specific project needs (see chapters 2 and 9 for a 
detailed description of these steps). For exam- 
ple, you may want to create a list of coded value 
domains for the FType attribute to constrain well 
types entered to the feature class or modify the 
relationship between Aquifer and Well features to 
fit your project datasets. After building the geoda- 
tabase, you can load data into the feature classes, 
and then assign HydrolDs to the imported features 
to create a unique identifier that will be the basis 
for queries and relationships within the geodata- 
base. You can then populate the key fields in the 
feature classes (e.g., AquiferID) to establish rela- 
tionships and apply tools to the imported data to 
calculate new attributes and create new features. 
Finally, you can use the results of this process to 
create products such as maps, scenes, and reports. 
The following checklist provides a summary of the 
main steps for creating Aquifer and Well features. 
Checklist 
1. Create the Aquifer and Well feature classes (manually 
or by importing from an XML schema) 
2. Add project specific attributes and domains as neces- 
sary (e.g., aquifer type, well type) 
Ww . Document datasets and changes made to the data 
model 
4. Define the data to be imported (all data or data for 
specific aquifers, counties, etc.) 
.ea) . Load data into the feature classes (if wells are defined 
in tabular format you first need to create point fea- 
tures from x,y coordinates) 
en Assign unique identifiers to features 
7. Populate the relationship between Aquifer and Well 
features 
8. Apply tools (e.g., calculate additional attributes, digi- 
tize new features) 
9. Create products (maps, scenes, reports) 
56 The following example illustrates the process 
of creating Aquifer and Well features. Aquifer 
features were imported into the Arc Hydro 
Groundwater geodatabase from a dataset created 
by the TWDB describing all the major aquifers in 
Texas. Because we are primarily interested in the 
Edwards Aquifer, only features with an Aquifer ID 
= 11 (the aquifer identifier in the TWDB database 
representing the Edwards Aquifer) were imported 
into the geodatabase. HydrolDs were assigned to 
the features to uniquely identify them within the 
geodatabase, and HydroCode was set to 11 to store 
the original aquifer identifier. Aquifer features 
were also given an FType to distinguish between 
confined and outcrop zones (see figure 5.6). 
Well features were created by importing 
information from the “welldata” table of the 
TWDB groundwater database. The table contains 
a description of about 130,000 wells in Texas, and 
each well is described by a set of about 50 attri- 
butes. The first step was to define a set of attributes 
of interest that will be valuable for the project. One 
could just import all 50 attributes from the TWDB 
table, but many of these may not be populated or 
necessary. As described above, the groundwater 
data model provides a minimum set of attributes, 
and users must decide what additional informa- 
tion is useful for their project and add these fields 
to the Well feature class. In the example shown 
in figure 5.9, fields describing the owner and 
the water use were added. Later, a set of coded 
value domains are defined for the water use field 
representing types of wells within the project. 
Once the feature classes are designed, we can 
load data into them, but first we need to decide 
on the data to be imported. Will we import data 
for all the wells in Texas, or are we interested only 
in the data for a particular county, groundwater 
management district, or aquifer? In this example, 
we use only wells in the Edwards Aquifer. In order 
to import features into the Well feature class, we 
first create a spatial representation of the wells 


defined by the coordinates in the well table (this 
can be done in ArcGIS with the Make XY Event 
Layer geoprocessing tool). Then the features are 
loaded into the Well feature class. When loading 
the data, we only import attributes of interest 
and only import wells in our area of interest, the 
Edwards Aquifer (AquiferID = 11). 
pieog 
juawdojanag sajej sexay Jo Asaqinod ejeq Feature Class Properties 
XY Coordinate System | Tolerance | Resolution | Domain | 
| Indexes | Subtypes | Relationships Representations 
i aoe nas: 
[ Field Properties 
To add a new field, ype the ante ko ani sipky row iilthe Pleid Name colar, click in 
the Data Type column to choose the data type, then edit the Field Properties, 
Figure 5.9. An ArcCatalog view showing the fields of the 
Well feature class. The highlighted fields are not part of the 
core data model and are added as needed. 
22] | Attributes of Well 
360 
375) x: 00 zt 
312] 
z 265 | 
380 [ 
415 | 
Show: a Selected | 245; 1 
400; 11 
ae eA a 14 Steps for creating Aquifer and Well features 
After importing the well data and creating Well 
features, we assign HydroIDs (using the Assign 
HydroID tool in the Arc Hydro tools). During this 
import process, the state well number is imported 
into the HydroCode attribute to establish a 
connection with the original database from which 
the data were created. Also, the HGUID is popu- 
lated to index Well features with a specific hydro- 
geologic unit, and the aquifer-well relationship 
is established by indexing Well features with the 
HydroID of an Aquifer feature. 
The next step is to define types of wells 
represented in the geodatabase. FType can be 
defined using a coded value domain. For example 
a WellFType coded value domain is created to 
define a set of unique values that can be entered 
in the FType field. The coded value domains can 
be edited, deleted, and extended to fit your project 
requirements (See chapter 9 for more information 
on creating coded value domains). After assigning 
the coded value domain, when editing the FType 
field in ArcMap, values will be restricted to the set 
of coded values defined in the Well FIype domain. 
In an edit session, a drop-down menu appears 
when you try to edit the FIype values, and you 
must select one of the predefined coded values 
(figure 5.10). 
Figure 5.10. When 
editing an attribute with 
a coded value domain 
the values entered 
are restricted to a pre- 
defined list. 
57 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
Field Calculator 
Fields: 
ad OBJECTID Number ea TYEE PTE TSM 
413 218EDRDA 
1 3 oteED 8EDRDA : Se bedi 
__ 113 |218EDRDA 
113 |218EDRDA Shape 
HydroID © String 
HydroCode 
LandElev © Date 
WellDepth 
AquiferID 
AqCode 
HGUID 
FType 
Pre-Logic VBA Script Code |W ‘Advanced 
Dim s as sting 
If [WaterUse] = “I" then 
s = "Irrigation" 
elself [WaterUse] = "H" then =e 
s ="Domestic” S} 
Endif save... | 
5 Help |. , 
= OK 
J Calculate selected 't records ons ' 
Data loaded. Cance' 3, 113 |218EDRDA | 
113 |216EDRDA 
5 | 113/21 18EDRDA | 
255] 113 |218EDRDA 
265 | | 113) j2t BEDRDA 
480 | == ~ 113 |218EDRDA 
pieog Juawidojanag Jajem sexal jo Asaqinod ejeq 
Figure 5.11. Example of a script in the Field Calculator for assigning FType values. 
In the Texas groundwater database, water use 
was defined using single letters. For example, 
“Water Use = I” stands for irrigation, and “Water 
Use = H” stands for domestic. Figure 5.11 shows 
a simple script written in the Field Calculator 
that is useful for automating the assignment of 
FType values. 
58 


At the end of this process, tabular data from the 
TWDB groundwater database were converted to 
spatial features representing wells in the Edwards 
Aquifer, and these were imported into the Well 
feature class. The features are attributed such that 
they can be linked with related Aquifer features, 
and are also classified by the Well FType coded 
value domain. The following map (figure 5.12) 
shows Well features in the Edwards Aquifer 
classified by the FType. 
3D borehole data 
Although wells in the data model are represented 
as 2D point features, in reality the geometry of a 
well is 3D as it extends into the subsurface. The 
3D geometry of a Well feature is defined by the x 
and y coordinates of the point feature and in the 
vertical (z) dimension by the LandElev and Well- 
Depth attributes. The 3D geometry of wells can be 
viewed in ArcScene by extruding the Well point 
from the land surface downward (figure 5.13). 
Many groundwater and well databases include 
tables for describing 3D construction elements 3D borehole data 
(e.g., screens, casing, and samplers) and tables for 
describing strata along boreholes. These types of 
data are commonly documented in construction 
and drilling logs and are later stored as tabular 
information in groundwater and well databases. 
In many cases these datasets follow a common 
data structure, where each record corresponds 
to a set of elevations representing vertical seg- 
ments along the borehole. The following section 
describes how such data are represented within 
the groundwater data model. Throughout this sec- 
tion we use the term borehole for describing the 
vertical dimension of a well. 
Land surface 
ety 
Extruded well features 
Figure 5.13. Example of Well features extruded from the 
land surface to the well depth. 
pieog JUaWIdojanaq Jaye sexa| Jo Asaj4nod jeg Figure 5.12. Well features rep- 
resenting wells in the Edwards 
Aquifer. The features are clas- 
sified by FType to distinguish 
among domestic, irrigation, and 
public supply wells. 
Domestic 
e Irrigation 
¢ Public supply 
59 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
BoreholeLog table 
BoreholeLog is a table for representing vertical 
data along boreholes and is the basis for creating 
3D features to represent vertical data as 3D geome- 
tries. Data in the BoreholeLog table do not contain 
x and y coordinates; rather a Well feature is refer- 
enced by indexing data in the table with a WellID 
attribute that is equal to the HydroID of a Well 
feature. This structure implies that the borehole 
BEM ={0) 9-1 ato) (-) mole] 
Table for representing vertical data 
along boreholes 
Fieldname Description 
WeilllD References the HydrolD of a Well feature. 
RefElev A reference elevation (e.g., land elevation, top of casing) giving 
the starting elevations for data measured as depth along the 
borehole, 
FromDepth The top elevation of an interval measured as depth along the 
borehole. 
ToDepth The bottom elevation of an interval measured as depth along the 
borehole, 
TopElev Top elevation of an interval represented in absolute elevation 
units (e.g., feet above mean sea level). 
BottomElev Bottom elevation of an interval represented in absolute elevation 
units (e.9., feet above mean sea level). 
ElevUnits Units of elevations stored in the TopElev and BottomElev 
attributes. 
Material Description of strata observed along a borehole. Usually 
documented in drilling logs and later classified into 
geologic/hydrogeologic units. 
HGUID Hydrogeologic unit identifier. Classifies borehole data into 
hydrogeologic units defined in the HydrogeologicUnit table. 
HGUCode Hydrogeologic unit code. Text for classifying, symbolizing, and 
labeling hydrogeologic units. 
LogType Distinguishes between types of borehole logs (e.g., well 
completion, hydrostratigraphy). 
Figure 5.14. The BoreholeLog table represents vertical 
information recorded along boreholes. 
Absolute elevations 
(above mean sea level) Elevations expressed as 
depth along the borehole represented is vertical and that all objects along the 
borehole have the same x and y coordinates as the 
referenced Well feature. The association between 
Well features and BoreholeLog objects is a one-to- 
many (1:M) relationship, where a Well feature can 
be associated with one or more vertical data ele- 
ments in the BoreholeLog table. Figure 5.14 shows 
the structure of the BoreholeLog table. 
Features along the borehole can be described 
as points defined by a single elevation or as inter- 
vals defined by two elevations, one for the top 
and one for the bottom of the interval. Top and 
bottom elevations can be defined with two types 
of referencing systems: depth along the borehole 
(relative elevations) or absolute elevations. Rela- 
tive elevations are measured from a reference 
elevation, which is usually the land surface at 
the well location (figure 5.15). This is a common 
method for storing information from borehole 
logs. Usually, data are recorded during the drill- 
ing and construction process and are defined as 
“depth below the land surface.” Thus, the vertical 
coordinate increases in the downward direction. 
The depth values are stored in the FromDepth and 
ToDepth attributes. When using such a referencing 
system, vertical data from different wells cannot 
be directly compared because the elevation of the 
land surface is not the same at each well location. 
To integrate data across a number of wells (e.g., 
interpolate rasters, create cross sections) absolute 
elevations must be used. Absolute elevations are 
referenced to a common datum, such as mean sea 
Figure 5.15 Vertical data along bore- 
Ss a8 5 holes are represented using absolute 
20 10 | 20 0 elevations (in green) and as depth along 
Wy 20 10 10 | Material | Hydrogeologic unit 4 - the borehole (in blue). Data are also clas- 0 29 Material2 | Confining layer ; 
Well 1 sified by material, and materials can be 
Well 2 grouped into hydrogeologic units. 
Material 3 Hydrogeologic unit 2 - 
Aquifer 
-70 100 
-80 100 
60 


level, and can be directly compared. Usually, raw 
data are given as depth along the borehole, and 
these are translated to absolute elevations. The 
absolute values are stored in the TopElev and 
BottomElev attributes. 
Figure 5.16 shows a populated BoreholeLog 
table for the boreholes described in figure 5.15. 
The FromDepth and ToDepth values for both 
wells are the same, but because the reference 
elevation (RefElev) is different, the absolute eleva- 
tions (stored as feet above mean sea level) repre- 
sented in the TopElev and BotmElev attributes 
vary accordingly. 
BorePoint and BoreLine features 
Data stored in the BoreholeLog table are the basis 
for creating 3D features that represent vertical 
data along boreholes. BorePoint and BoreLine are 
3D (z-enabled) point and line feature classes that 
represent point and interval data along boreholes, 
respectively. Similar to the relationship between 
BoreholeLog objects and Well features, BorePoint 
and BoreLine features are related to a Well feature 
by associating the WellID attribute of the 3D fea- 
tures to the HydroID of a Well feature. TopElev, Bot- 
tomElev, and PointElev are attributes for storing the 
elevations of the features. While the elevations are 
already stored internally in the geometry of the fea- 
tures, storing them as attributes enables easy display 
of elevations and can support elevation-based que- 
ries. For example, we could query for all BorePoints 
with an elevation between 500 and 800 feet above 
FF] Attributes, of Boreholel.0e 
: oak [al Selected | ea i | Records (0 out of 6 Selected) BorePoint and BoreLine features 
mean sea level. Figure 5.17 shows the structure 
of the BorePoint and BoreLine feature classes. 
ZA BorePoint 
Point Z feature class for representing 
point data along boreholes 
Fieldname _ Description i 
HydroID Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
WelllD References the HydrolD of a Well feature. 
Material Description of strata observed along a borehole. Usually 
documented in drilling logs and later classified into 
geologic/hydrogeologic units. 
HGUID Hydrogeologic unit identifier. Classifies borehole data into 
hydrogeologic units defined in the HydrogeologicUnit table. 
HGUCode Hydrogeclogic unit code. Text for classifying, symbolizing, and 
labeling hydrogeologic units. 
PointElev Elevation of the BorePoint feature. 
FType Distinguishes between types of BorePoint features (e.g., 
= stratigraphic picks, sampling ports). 
Polyline Z feature class for representing 
interval data along boreholes ! ( a |[Fieldname Description 
HydrolD Unique feature identifier in the ae used for ceeinan 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
WelllD References the HydrolD of a Well feature. 
Material Description of strata observed along a borehole. Usually 
documented in drilling logs and later classified into 
geologic/hydrogeologic units. 
HGUID Hydrogeologic unit identifier. Classifies borehole data into 
hydrogeologic units defined in the HydrogeologicUnit table. 
HGUCode Hydrogeologic unit code. Text for classifying, symbolizing, and 
labeling hydrogeologic units. 
TopElev Top elevation of the BoreLine feature. 
BottomEley Bottom elevation of the BoreLine feature. 
FType Distinguishes between types of BoreLine features (e.g., well 
completion, hydrostratigraphy). 
Figure 5.17 BorePoint and BoreLine feature classes repre- 
sent vertical data along boreholes as 3D features. 
Options & 
Figure 5.16. BoreholeLog table representing vertical information along two boreholes, as shown in figure 5.15. 
61 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
Steps for creating 3D borehole data 
This section outlines the steps involved in popu- 
lating the BoreholeLog table and creating 3D 
BorePoint and BoreLine features. The first steps 
for implementing this component are to refine 
the geodatabase design to meet your specific 
project needs (see chapters 2 and 9 for a detailed 
description of these steps). Once the geodatabase 
is created, you can load vertical data into the Bore- 
holeLog table. You can then assign WellID values 
to the data to associate the vertical data with 
Well features and translate referenced elevations 
(FromDepth and ToDepth) to absolute elevations 
(stored in the TopElev and BottomElev attributes). 
You can then apply tools to build 3D BorePoint 
and BoreLine features. Finally, you can use the 
results of this process to create products such as 
maps, scenes, and reports. The following checklist 
provides a summary of the main steps in creating 
3D borehole data. 
Checklist 
. Create the BoreholeLog table and BorePoint and 
BoreLine feature classes (manually or by importing 
from an XML schema) = 
N . Add project specific attributes and domains as 
necessary 
Ww . Document datasets and changes made to the data 
model 
a . Load vertical information into the BoreholeLog table 
iva . Assign WelllD values to the vertical information, and 
calculate top and bottom elevations (if necessary) 
6. 
7. Create products (maps, scenes, reports) Apply tools to create 3D features 
The following examples illustrate the process of 
creating 3D borehole data, including representa- 
tion of completion intervals and hydrostratig- 
raphy along boreholes. The first step is to create 
the BoreholeLog table and to import the vertical 
information into the table. Figure 5.18 shows well- 
completion data from the TWDB groundwater 
62 database. A selected Well feature (HydroID = 53) 
has seven completion intervals documented in the 
database. The LogType is defined as “well comple- 
tion” intervals, and the elevation values represent 
a series of elements recorded from the land surface 
downward. A custom attribute, CompletionType, 
was added to the BoreholeLog table to distinguish 
between different completion types (e.g., screen, 
porous concrete). Similarly, appropriate attributes 
can be added to extend the BoreholeLog table as 
necessary to better represent specific datasets in 
your projects. 
A conceptual 3D view of these data starts from 
the land surface and includes the completion 
intervals along the well. Interval depths start from 
0 at the land surface and extend to 300 feet below 
land surface. The elevations stored in the TWDB 
groundwater database represent depth along 
the borehole measured from the land surface, in 
this example at 800 feet above mean sea level, as 
shown in the RefElev attribute. Absolute eleva- 
tions are calculated by deducting the depth from 
the elevation of the land surface. 
Another common type of vertical data is 
information describing subsurface strata, which is 
observed and classified when the well is drilled. 
Material HGUID, and HGUCode attributes 
in the BoreholeLog table store information on 
subsurface formations related with intervals of 
the well. Material is a text attribute for storing 
descriptions of earth material along the borehole, 
and HGUID and HGUCode store hydrogeologic 
unit identifiers and codes to relate borehole data 
with defined hydrogeologic units. There is a dis- 
tinction between descriptions of material, color, 
and texture provided in well logs and classified 
stratigraphy or hydrostratigraphy. Description 
of strata observed along the borehole is usually 
raw information recorded in the field that is later 
stored in groundwater databases. For hydrogeo- 
logical analysis, the raw data are classified into 
conceptual stratigraphic or hydrogeologic units. 
