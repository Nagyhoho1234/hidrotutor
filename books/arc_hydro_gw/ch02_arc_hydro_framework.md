# Chapter 2: Arc Hydro Framework

Groundwater strata 
Understanding groundwater systems requires 
being able to depict their horizontal extent and also 
their vertical structure, usually visualized as cross- 
sections cut through the various hydrogeologic 
strata (figure 1.7). 
In Arc Hydro Groundwater, tabular information 
from well logs about the “contact points” at which Groundwater strata 
the well driller encountered each new subsurface 
layer is translated within ArcGIS into a 3D vertical 
representation of the borehole. Cross-sections can 
be drawn by connecting a sequence of boreholes 
or by cutting directly through a “geovolume” rep- 
resentation of the 3D structure of these hydrogeo- 
logic units. A special extension of the Arc Hydro 
Groundwater tools called Subsurface Analyst can 
be used to perform these functions. 
Drainage Area 
Edwards Water 
Table Aquifer Water Table Spring ts 
\* AS 
iD 
[2] Land Surface 
Relatively Impermeable 
Younger Formations 
Edwards Limestones Typical Cross-Section of the Edwards Aquifer Region 
Recharge Zone 
ypseyy2q H6as5 Jo AsayinoD Artesian Zone 
Edwards 3 
Artesian Aquifer | 
MOEN Fault Zone es Relatively impermeable 
Older Formations 
L 
Figure 1.7 A typical cross section of the Edwards Aquifer describes strata, hydrogeologic units, and features such as faults 
and wells within the subsurface. 


CHAPTER 1: INTRODUCTION 
Groundwater modeling 
Because groundwater systems are largely hidden 
from sight, groundwater simulation models are 
used to infer the properties of groundwater sys- 
tems and to simulate the flow and storage of water 
within the subsurface under variable conditions, 
including natural conditions and human-made 
influences such as pumping. The most widely 
used groundwater simulation model is MOD- 
FLOW, produced by the USGS, which is as much 
of a standard in the groundwater field as ArcGIS 
is a standard for geographic information systems. 
oo ita Fi 
GILLESPIE BLANCO The various data arrays in a MODFLOW model 
are like the pages in a groundwater system book. 
As you view them one by one, you see the spatial 
extent and physical properties of the aquifer, such 
as its thickness, porosity, and hydraulic conduc- 
tivity (figure 1.8). You see the pumping stresses, 
flow patterns, and recharge and discharge vol- 
umes, and you see the piezometric head map that 
depicts the levels of water within the different 
layers of the groundwater system. 
The Arc Hydro Groundwater tools include a 
special extension called MODFLOW Analyst that 
enables MODFLOW descriptions of groundwater 
100" 
EXPLANATION | 
Ground-water-model area Hydraulic conductivity, in 
Inactive model area feet per day 
Active model area BBN Less than or equal to 20 
Hydraulic conductivity of PR 20t0 50 
conduits in feet per day (9 5010 100 
im 10 {100 to 200 
Em 3.000 ©) 200 to 400 t 
Hm 3.500 400 to 600 
— sii 600 to 800 © « aa 800 to 1,000 ai 
EE 10,000 HBB 1.000 to 2,000 ; 
HE 75,000 (2,000 to 7,247 BBE 100,000 
HB 300,000 ¢ Bs BANDERA { P 
EDWARDS ye REAL 
PF MAVERICK 
a 
\ FRIO |-“ZAVALA Sos | KERR 
: COS ~ 
Springs 
¥ CALDWELL A 
ASAIN jeD1H0|0a5 *S'N ‘vOOT ‘|e 39 UaLHpurq jo AsaqinoD 
GONZALES 
\ 
> Zi 
Ni Ze 
\ cal | \ WILSON ¥ 
e Yi 
ATASCOSA 
40 MILES 
Ul een ee NS, | —— 
Figure 1.8 Simulated distribution of horizontal hydraulic conductivity for a calibrated MODFLOW model of the southern 
part of the Edwards Aquifer. Warmer colors represent higher conductivity and faster movement of water within the aqui- 
fer. The linear features within the model represent conduits with very high conductivity. 
10 


systems to be viewed and mapped in ArcGIS, thus 
enabling a much larger audience to understand 
the behavior of groundwater systems simulated 
with MODFLOW (see chapter 8). 
Scope of the book 
The book is divided into nine chapters. The first 
three chapters introduce the subject, describe the 
core framework data model, and present an expo- 
sition of how to represent 3D objects in ArcGIS. 
The next three chapters present components of 
the groundwater data model for geological map- 
ping, wells and aquifers, and 3D hydrostratigra- 
phy. The final three chapters describe time series, 
groundwater modeling, and implementation of 
the groundwater data model in ArcGIS. 
It is important to understand some of the 
limitations of this book—we are describing an 
information model for groundwater data. This is 
not a book about groundwater simulation model- 
ing. Arc Hydro Groundwater can be used to help 
create groundwater simulation models and to 
store the results of groundwater simulations, but 
Arc Hydro Groundwater is not itself a ground- 
water simulation model. Likewise, although we 
devote considerable attention to hydrogeology, 
Arc Hydro Groundwater is not intended to capture 
all the detailed cartographic aspects of geologic 
and hydrogeologic mapping. Our focus is on the 
groundwater environment and on the properties 
of the water flowing through that environment. 
References 
Lindgren, R.J., A. R. Dutton, S. D. Hovorka, S. R. H. Worthing- 
ton, and P. Scott. 2004. Conceptualization and simulation of 
the Edwards aquifer, San Antonio region, Texas: U.S. Geolog- 
ical Survey Scientific Investigations Report 2004-5277, 143 p. 
Maidment, D. R., ed. 2002. Arc Hydro: GIS for Water Resources. 
Redlands, California: Esri Press. Scope of the book 
11 


_— 
ne : ; het : 7 
ne aa a Ve pu 
= we — 
‘ : : “3 a * ee: =o = oa ) = | a | nn 
a fen 2 
=e, ene a data cee = 7 3 . Phi oe a c tg : 
- 2 Bag 


chapter two 
NT AND GIL 
Thematic layers of the Arc Hydro framework 
Hydrography (WaterLine, Waterbody, and WaterPoint) 
The “blue lines” on maps representing rivers and streams, water bodies, and 
points of interest such as springs and diversions points. 
Representation: Points, Lines, and Polygon features 
- Watershed 
ae Drainage areas defining the extent of land from which water drains into a body 
“ of water. 
Representation: Polygon features 
” cag har Sipe ; a ee a ae ; fe aaa ; ae MonitoringPoint 
Locations where water is measured, such as stream and precipitation gages, and 
water quality monitoring stations. 
Representation: Point features 
Aquifer 
Geologic formations that yield significant quantities of water to springs and wells. 
Representation: Polygon features 
Well 
Man-made structure to withdraw or sample groundwater. 
Representation: Point features 
Time Series 
Temporal information describing water quantity and properties. 
Representation: Tabular data related to spatial features 
pieog juawdojaAag Jaze\\ Sexa) pue Addins je21Ho}0a5 *s'p Jo Asayinod eyeg 


CHAPTER 2: ARC HYDRO FRAMEWORK 
WHEN A STUDY IS UNDERTAKEN USING ARC 
Hydro Groundwater, the first step is to compile 
readily available data into a geodatabase so that 
they form a foundation upon which more detailed 
datasets and interpretations can later be built. The 
Arc Hydro Framework is formed of feature classes 
representing common surface and groundwater 
features, such as hydrography, watersheds, moni- 
toring points, aquifers, wells, and time series of 
water observations data. The same Arc Hydro 
Framework datasets are used for surface water 
studies implementing Arc Hydro as well, so that 
we can think of water as a single resource. In a par- 
ticular study, some feature classes or tables of the 
Arc Hydro Framework are not needed; those can 
be retained in the framework data structure but 
not filled with data. 
Once the Arc Hydro Framework is created, other 
data model components can be added, as shown in 
figure 2.1. In the case of groundwater, these include 
components for geological maps, 3D description 
of boreholes and hydrostratigraphy, and links to 
groundwater simulation models. In the case of 
surface water, the additional components include 
a GIS network representation of the stream system, 
Surface water components 
x se 
Arc Hydro 
Framework catchments, and watersheds that convey drainage 
to the stream network, description of hydrography, 
including rivers and water bodies (e.g., lakes, estu- 
aries, marshes and bays), and 3D representation of 
river channels. Both Arc Hydro surface water and 
groundwater share a common description of tem- 
poral data such as time series of water levels and 
water quality measured in wells. 
An important design consideration for the Arc 
Hydro data model is to have a parsimonious data 
model—namely to limit the number of required 
feature classes, tables, and attributes to the mini- 
mum needed to achieve a description of the basics 
of a groundwater system. Often, more information 
is required than this basic description provides. 
Indeed, the Arc Hydro Groundwater tools them- 
selves generate additional tables and attributes 
shown in this book. The data model presented 
here is intended to be a basis for further elabo- 
ration in your context rather than an exhaustive 
description of every possible variant for describing 
groundwater systems. 
We created the groundwater data model to 
focus on classes of information for which data 
are readily available in most applications and to 
Groundwater components 
Figure 2.1 Components of the Arc Hydro data model (including surface water and groundwater). 
14 


support implementation workflows that create 
useful information products. As such, each chap- 
ter that outlines a component of the groundwater 
data model concludes by describing the process of 
implementing that component in a useful way. 
The Arc Hydro Groundwater data model 
components are described further in chapters 4 
through 8 of this book: 
¢ Geology—Point, line, and area features from 
geologic maps; 
e Aquifer, well, and borehole data—2D 
representation of aquifers and wells, and the 
borehole component that represents 3D data 
along boreholes; 
Hydrostratigraphy—Representation of hydro- 
geologic units with 2D and 3D features (cross- 
sections and geovolumes) and surfaces; 
e Simulation—Groundwater simulation models 
represented as 2D and 3D features; 
¢ Temporal—Representation of spatial-temporal 
datasets. 
As noted in chapter 1, an update to Arc Hydro: GIS 
for Water Resources (Maidment 2002) is envisioned 
to better describe the components of a data model 
for surface water. 
Desktop, server, and online GIS 
When Arc Hydro: GIS for Water Resources was 
published in 2002, it was conceived as a data model 
to be used within ArcGIS Desktop to ingest and 
process information from various local sources. 
More than a hundred Arc Hydro tools have been 
built on this foundation in subsequent years, and 
the Arc Hydro toolset is now the most widely used 
means of performing tasks such as watershed and Desktop, server, and online GIS 
stream network delineation from digital elevation 
models (DEMs). Very often the input data for such 
a process are downloaded from the Internet, such 
as getting a DEM dataset for a study area from the 
USGS Seamless Server. 
In subsequent years, other patterns for using 
geospatial information have emerged, including 
ArcGIS Server and ArcGIS Online. ArcGIS Server 
is a mechanism for publishing information as geo- 
graphic data services and tiled image maps that 
can be rapidly ingested through the Web into 
ArcGIS Desktop or other applications such as 
mobile GIS, or Web interfaces for geospatial data 
query and analysis. 
ArcGIS Online is a central repository of 
information in “the cloud” that is directly acces- 
sible through Web connections to ArcGIS Desktop, 
and it supplies global coverage of high-quality 
basemaps for topography, roads, hydrography, 
geology, orthophotography, and other themes. 
These 2D basemaps are tiled for rapid display 
at any spatial scale, and they provide important 
context for the detailed feature representations 
created in Arc Hydro Groundwater. New informa- 
tion, such as a completed Arc Hydro Groundwater 
geodatabase, can be symbolized in an ArcMap dis- 
play, assembled into a “Layer Package,” and pub- 
lished in ArcGIS Online, either publicly or shared 
just within a group of other ArcGIS Online users. 
In this sense, ArcGIS Online is a Web-based social 
network for map and data sharing. 
The emergence of ArcGIS Server and ArcGIS 
Online as automated mechanisms for map and 
data sharing means that creating Arc Hydro geo- 
databases is a more valuable activity than was for- 
merly the case, because the constructed result can 
more readily be accessed and used by others. 
The importance of these developments in Web 
access to geospatial information should not be 
underestimated. The United States has a National 
Hydrography Dataset for surface water features 
but lacks a National Hydrogeologic Dataset for 
15 


CHAPTER 2: ARC HYDRO FRAMEWORK 
groundwater features. Thus, Web-based technol- 
ogy now exists to develop and publish regionally 
consistent hydrogeologic datasets even when no 
national system is available. 
Time series of water observations data such as 
streamflow and groundwater levels are now being 
published by the U.S. Geological Survey and other 
water agencies as Web services in the WaterML 
language. WaterML is an eXtended Markup Lan- 
guage (XML) specification that describes the site 
at which measurements are made, such as a well; 
the variables measured there; the time period of 
record and number of values of each variable 
available; and the time series of the measured 
values themselves. WaterML Web services can be 
used to directly ingest water observations data 
into the Arc Hydro temporal component, where 
Arc Hydro Groundwater tools can be used to 
create time varying maps of groundwater condi- 
tions such as piezometric head levels or concentra- 
tions of a chemical constituent. 
The simultaneous advent of Web services for 
water observations data such as groundwater 
levels and water quality means that the geographic 
data services just described can be augmented by 
water observations data services supplying cur- 
rent information about water conditions in aquifer 
systems. These GIS and water observation data 
services taken together constitute the basis for 
implementing a services-oriented architecture for 
groundwater information, a concept from com- 
puter science that promises to greatly facilitate the 
synthesis of otherwise fragmented groundwater 
information housed at water agencies in differ- 
ent geographic locations. The process for publish- 
ing and ingesting Arc Hydro Groundwater data 
services is explained in chapter 9. 
Building a geographic data model 
Building a geographic data model requires some 
general principles. In part, these are derived from 
16 the nature of ArcGIS itself, but in the larger sense, 
geographic data modeling is part of a wider disci- 
pline of representing the world by abstract models. 
Booch et al. (1999) define a model as a “simplifi- 
cation of reality” aimed to better understand the 
system we are studying. Data models help us 
describe complex systems using a structured set of 
data objects. A geographic data model is a repre- 
sentation of the real world expressed with spatial 
datasets within a GIS. 
Geographic data models are useful for two 
major reasons: 
1. They provide a template for modeling types of 
systems by defining a set of common spatial 
objects and the relationships between them. 
2.They define a common vocabulary to assist 
sharing of data, tools, and analyses within a 
discipline. 
Designing a geographic data model includes 
three phases: conceptual design, logical design, 
and physical design (Arctur and Zeiler 2004). 
The conceptual design includes the identifica- 
tion of information products created with GIS 
and defines the key thematic layers and how 
these can be grouped into datasets. The logi- 
cal design defines the structure and behavior of 
the datasets and results in a geodatabase pro- 
totype. The physical design includes the imple- 
mentation process where the prototype is tested 
through case studies and reviewed by users. This 
is an iterative process of refining the data model 
based on reviews and results from case studies. 
During the logical design we define a set of the- 
matic layers that describe objects in the modeled 
system. Thematic layers are defined by classi- 
fying and grouping objects with similar geom- 
etries, properties, and behavior. For example, in 
the groundwater data model, all wells (irriga- 
tion, domestic, industrial, etc.) are grouped into 


one thematic layer and are described as point 
features with similar attributes. 
The behavior of the system, or “how the system 
works,” is described by relationships between 
objects of the data model. Feature-to-feature 
relationships enable us to track the movement of 
water through the hydrologic system. Water can 
be traced from where it drops on the land surface 
to the outflow point of the watershed in which it 
fell and through the downstream water bodies 
and monitoring points on its way to the ocean 
(figure 2.2). In some cases water can be traced 
through the stream network and over an aqui- 
fer outcrop where water can enter the underling 
aquifer, ultimately flowing to a well within the 
aquifer or discharging at a spring. The ability to 
create relationships between spatial datasets is 
AaAins jed1Hojoay “sf ‘suenq “W UYOr JO AsayinoD Geodatabases 
an important capability provided as part of the 
geodatabase environment. 
Geodatabases 
A geodatabase is a repository of geographic 
information organized into geographic datasets. It 
provides a common data storage and management 
framework for storing all the types of datasets sup- 
ported in ArcGIS. There are three types of geoda- 
tabases: personal geodatabases, file geodatabases, 
and ArcSDE geodatabases. The personal and 
ArcSDE geodatabases are built on top of relational 
database management systems (RDBMS) such as 
Microsoft Access, Oracle, or Microsoft SOL server, 
which are customized for storing spatial data 
structures. The file geodatabase manages data in a 
Figure 2.2 Feature-to-feature relationships enable the description of how water flows through the hydrologic system. 
1\2/ 


G HAPTER 2: ARC HYDRO FRAMEWORK 
| § Geodatabase 
datasets supported in ArcGIS. 
L i | Feature dataset 
Container for a collection of spatially related feature 
classes together with relationship, topology, and 
network classes. The feature dataset is used for 
grouping feature classes either by spatial reference (all 
features classes in a feature dataset share the same 
spatial reference) or thematically. 
L/] [eZ] Feature class 
A collection of features with the same geometry 
type, attributes, and relationships. A feature class 
is a table in the geodatabase that contains a : 
custom field (Shape) for defining the geometry of 
features. 
User-defined Predefined fields 
« Features 
Subtype Default Domain Subtypes let you discriminate 
classes of features in a feature 
class to control fine-grained 
behavior through attribute, 
topology, network, and 
relationship rules. 
RX] Topology 
Integrity rules that define the behavior of 
geographically-integrated features. 
Feature class Rank Rules Predefined 
fields 
@)e) (=e) 8) Repository of geographic information organized into geographic datasets within a relational database 
system. It provides a common data storage and management framework for storing all the types of 
Ee] Table 
An object for storing data values as an array of 
rows and columns. 
User-defined 
fields 
Domain 
Defines a set or range of 
valid values for a field. 
LR 
<3 An association between classes based 
on common values in key fields. Relationship 
Primary key Foreign key 
Raster catalog 
Provides a container for storing, indexing, 
and attributing raster datasets. 
} Raster dataset 
Represents imaged, sampled, or interpolated 
data on a uniform rectangular grid. 
18 Figure 2.3 Geodatabase objects used in the groundwater data model. 


file system folder. For a more detailed description 
of the types of geodatabase and the differences 
between them see the ArcGIS desktop help system 
(http: //webhelp.esri.com). Storing data in a geo- 
database has a number of technical advantages. A 
geodatabase can store a variety of spatial and tab- 
ular datasets in one centralized location, support 
versioning and multiuser access to the data, and 
allow easy scaling of storage solutions. 
Data objects in the Arc Hydro Groundwater 
geodatabase include feature classes, feature datas- 
ets, raster datasets, raster catalogs, tables, and rela- 
tionships (figure 2.3). A more detailed description 
of geodatabase objects is provided by Zeiler (1999). 
Hydro features 
As part of the Arc Hydro design, generic feature 
classes are customized by adding HydroID and 
HydroCode attributes to them. We call these 
modified features hydro features. Generic geoda- 
tabase objects contain an ObjectID field, which is 
maintained by ArcGIS and guarantees a unique 
ID for each row in a table (also for features in a 
feature class and rasters in a raster catalog). The 
two custom attributes, HydroID and HydroCode, 
are added to spatial features in the Arc Hydro 
Hydro Features 
The HydrolD is an integer 
identifier for a feature 
used for internal management 
of information within 
base. ag an Arc Hydro geodatabase 
HydroCode is the permanent 
public identifier of a feature, 
a text attribute which links 
Arc Hydro to external sources 
of information about the feature 
stored in other information 
systems. 
In this way Arc Hydro can be 
linked with other information 
system to automatically acquire 
the data needed for hydrologic studies. Streamflow Hydro features 
geodatabase to provide a mechanism for uniquely 
identifying features across the geodatabase, estab- 
lishing relationships between classes, and tracing 
data back to its source in external information 
systems (figure 2.4). 
e HydroID is an integer attribute that uniquely 
identifies objects in an Arc Hydro geodatabase. 
The HydroID differs from the ObjectID, as it is 
unique across the geodatabase and not only 
within a certain class (table, feature class, raster 
catalog). 
¢ HydroCode is a text attribute that is a permanent 
public identifier of a feature. The HydroCode 
provides a linkage with external information 
systems. 
For example, in chapter 7 we describe how wells 
(described as point features) are related with 
water-level measurements stored on the USGS 
National Water Information System (NWIS). The 
HydroID of the well feature is unique within the 
geodatabase, but the USGS system also has its 
own unique identifier. In this case the well site 
number of 295443097554201 uniquely identifies 
this well from all other wells in the USGS system. 
Figure 2.4 Hydro — 
features are created by 
adding HydrolD and 
ydroCode attributes to - Water levels 
spatial features in an Arc 
ydro geodatabase. 
Water quality 
19 


CHAPTER 2: ARC HYDRO FRAMEWORK 
The well site number is stored in the HydroCode 
attribute of the well feature, which enables query- 
ing data (e.g., water levels, water quality) from the 
USGS external database. Tools developed on top 
of the Arc Hydro data model enable the retrieval 
of data from local tables or over the internet based 
on the HydroCode values. In this way Arc Hydro 
can be linked with external information systems 
to acquire data necessary for hydrologic analysis. 
HydroID is managed carefully because it is 
such an important attribute within Arc Hydro. 
HydrolDs are managed using a pair of tables, 
named APUNIQUEID and LAYERKEYTABLE, 
which are created automatically when you use the 
Arc Hydro tools (figure 2.5). HydroID values are 
tracked in the APUNIQUEID table. Each time a 
new ID is assigned to a feature in the geodatabase, 
a counter is updated so that the same HydroID 
is never assigned again within the given geoda- 
tabase. The APUNIQUEID table includes two 
fields: IDNAME is the name of the key field (e.g., 
HydroID), and LASTID stores the last ID used 
for that key field. The LASTID field is updated 
accordingly each time new IDs are assigned. An 
additional table) LAYERKEYTABLE, can be 
used to manage multiple identifiers, so that data 
Ae Ke) | 2) 
A unique numerical integer identifier for all features within 
one Arc Hydro geodatabase. 
wenwoieont | Hyacio | Keys} — 
The HydrolD for a new feature is dispensed from the 
APUNIQUEID table. A feature class points to its HydrolD 
dispenser in the APUNIQUEID table through the LAYERKEY 
defined in the LAYERKEY table. 
Several feature classes can point to the same HydrolD 
dispenser by using the same LAYERKEY. 
20 from different sources or for different projects or 
separate areas can be attributed with separate sets 
of unique identifiers. 
Hydro features in the geodatabase can be 
associated with other hydro features by storing 
their HydroID values as an attribute. By this pro- 
cess, river reaches can be associated with aquifers, 
which can be associated with wells, thus defining 
the movement of water between the stream and 
wells. Similarly, time-series data can be associ- 
ated with hydro features simply by storing the 
HydroID of a feature as an attribute of the time- 
series record. Uniquely labeling all hydro features 
in a geodatabase is a powerful concept for sup- 
porting behavioral modeling, because the geoda- 
tabase can be considered as an integrated whole 
rather than a set of separate data layers. 
In Arc Hydro, all fields used to support HydroID- 
based relationships are of type integer. Integers 
are easier to manage than text strings, and data- 
base queries operate more efficiently when inte- 
gers index data values. All Arc Hydro attributes 
ending in ID (e.g., HydroID, AquiferID, WellID, 
and FeatureID) indicate an integer identifier, 
and attributes ending in Code (e.g., HydroCode) 
indicate a text identifier. 
Figure 2.5 HydrolDs 
within an Arc Hydro geo- 
database are managed 
using the APUNIQUEID 
and LAYERKEY tables. 


Arc Hydro framework 
The Arc Hydro framework (figure 2.6) provides 
a simple data structure for storing the most basic 
geospatial datasets for describing hydrologic 
systems. This framework supports basic water 
resources analysis such as tracing water as it flows 
over the terrain in watersheds, streams, and water 
bodies; creating groundwater level and ground- 
water quality maps; and viewing time-series data 
related with monitoring stations and wells. The 
framework serves as a simple point of departure 
to which more detailed components can be added, 
as discussed in later chapters. 
The creation of an integrated geodatabase 
instead of a collection of data layers is a key accom- 
plishment of the Arc. Hydro design, providing 
) H WaterPoint i 
| HydrolD 
HydroCode 
| Name 
| JunctionID 
| FType 
WaterLine | 
HydrolD 
HydroCode 
Name 
FlowDir 
| NextDown!ID 
LengthKm 
FType 
= 
4 wl WaterBody 
= HydrolD 
HydroCode 
Name 
JunctionID 
NextDown|D 
| AreaSqkKm 
FType -| HydrolD 
| VarName 
~| VarDesc 
VarUnits TimeSeries | 
h 
| FeaturelD 2 
VarlD 
TsTime 
UTCOffset 
| TsValue wl Watershed | 
| HydrolD : 
| HydroCode 
| Name 
DrainID 
JunctionID 
NextDownID 
AreaSqkm 
FType pueog juawdojanag Jaze sexa} pue AdAsns [edIHoj}Oay *s‘fq Jo Asaqino>-eleg | BE SeriesCatalog | 
| FeaturelD 
FeatClass 
VarlD 
TsTable 
StartTime 
EndTime [ 
ValueCount h Arc Hydro framework 
a starting point for building stronger water 
resources applications in GIS. The green lines 
in figure 2.6 show the relationships between the 
features in the framework. Each relationship has 
a cardinality (represented by the numbers in the 
analysis diagram) that defines the number of fea- 
tures in each class that can be related. In the frame- 
work data model all relationships are one-to-many 
(1:M), meaning that a single feature in one class 
can be related to one or more features in the related 
class. For example one Aquifer feature can be asso- 
ciated with one or more Well features. The estab- 
lishment of relationships allows the association 
between features and objects in the data model 
so that Well features can be linked with Aquifer 
features. Although no explicit relationship is built, 
WaterLine, Waterbody, and WaterPoint features 
vl Aquifer 
| HydrolD 
| HydroCode 
Name 
| HGUID 
| FT 
HydroCode 
LandElev 
WellDepth 
| AquiferlD 
AqCode 
is 
fl MonitoringPoint : 
4) HydrolD 
HydroCode 
Name 
| JunctionID 
FType 
Figure 2.6 Analysis diagram describing the datasets of the Arc Hydro framework. 
21 


CHAPTER 2: ARC HYDRO FRAMEWORK 
can also be associated with Aquifer features. Since 
Aquifer features are related to Well features, one 
can trace the movement of water from where it 
falls on the land surface through the drainage and 
river network and into the subsurface. In addition, 
MonitoringPoints and Wells are related with time 
series data to enable storage and visualization of 
measurements recorded at monitoring stations 
and wells. 
Hydrography (the blue lines on a map) and 
drainage areas which contribute flow to the 
water system are represented by a set of feature 
classes describing river networks, water bodies, 
watersheds, and special points of interest in the 
hydrologic system. Feature classes describing 
hydrography include WaterLine, WaterBody and 
WaterPoint (figure 2.7). WaterLine is a line feature 
class for representing hydrographic “blue lines,” 
which represent mapped streams and water body 
center lines. The features are usually directional 
(digitized with the flow direction) and connected 
so that they can form a network. WaterBody is a 
polygon feature class for representing areal water 
features in the water system, such as lakes, ponds, 
swamps, and estuaries. WaterPoint is a point fea- 
ture class for representing hydrographic features 
such as springs, water withdrawal/discharge 
locations, and structures. 
22 fy WaterLine 
Line feature class for storing hydrographic “blue 
lines” representing mapped streams and water 
body center lines 
Fieldname Description Pais 
HydrolID Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating features 
with extemal information systems. 
Name Text attribute representing the name of the river or stream. 
FlowDir Direction of flow for the feature (e.g., with digitized, against 
(flow direction) digitized). 
NextDownID Relates a WaterLine feature to its downstream feature, thus 
creating river network connectivity. NextDownID is equal to the 
HydrolD of the next downstream feature. 
LengthKm Length of the WaterLine feature in km units. This attribute is 
(length in km) | commonly used for modeling purposes and analytic calculations. 
FType Distinguishes between types of WaterLine features. 
(feature type) 
1 Waterbody 
Polygon feature class for representing 
areal water features in the water system 
Field name Description Al £ 
HydroID Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
Name Text attribute representing the name of the water body. 
JunctionID Relates a Waterbody feature with a river network by 
associating a water body with a junction on the network. The 
Junction|D of a Waterbody feature is equal to the HydrolD of 
a related HydroJunction feature. 
NextDownID Relates a WaterBody feature to its downstream feature, thus 
creating feature to feature connectivity. NextDownlD of a 
WaterBody feature is equal to the HydrolD of the next 
downstream feature. 
AreaSqKm Area of the water body in square km units. This attribute is 
(area in square km) commonly used for modeling purposes and analytic 
calculations. 
FType Distinguish between types of water bodies (e.g., lake, pond, 
(feature type) and estuary). 
@A WaterPoint 
Point feature class for 
hydrographic features representing 
Fieldname Description 
HydroID Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
Name Text attribute representing the name of the water point. 
JunctionID Relates a HydroPoint feature with a river network by associating 
the point feature with a junction on the network. The JunctionID of 
a HydroPoint feature is equal to the HydrolD of a related 
HydroJunction feature. 
FType Distinguishes between types of HydroPoint features (e.g., spring, 
(feature type) diversion point, structure). 
Figure 2.7 WaterLine, Waterbody, and WaterPoint feature 
classes represent hydrography—the blue lines on a map. 


Watershed is a polygon feature class for 
representing drainage areas contributing flow 
from the land surface to the water system 
(figure 2.8). 
Time series are measured at different locations 
and represent different types of water properties 
and quantities. There are many types of monitor- 
ing points, such as stream gages where flow is 
measured, precipitation gages, and sampling loca- 
tions where water properties (e.g., temperature, 
pH, and water quality) are measured. Monitor- 
ingPoint is a point feature class for representing 
locations where water is measured (figure 2.9). 
A number of the framework feature classes 
include a JunctionID attribute that relates these 
features to a river network. The river network itself 
is included as a separate component, “Network,” 
which is based on a geometric network dataset. 
The most basic features commonly used to 
represent groundwater systems are aquifers and 
wells. Aquifers are commonly delineated in aqui- 
fer maps that describe the boundaries of aquifers 
=i Watershed —— é Behe = 
Polygon feature class for representing drainage A od 
areas contributing flow from the land surface to a 
the water system ye 
3 aT ie Field name Description a 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
Name Text attribute representing the name of the watershed. 
DrainID Index associating Watershed features with a_ specific 
drainage area. The DrainID of a Watershed feature is equal 
to the HydrolD of the reference drainage area feature. 
JunctionID Relates a Watershed feature with a river network by 
associating a watershed with a junction on the network. The 
JunctionID of a Watershed feature is equal to the HydrolD of 
a related HydroJunction feature. 
NextDownID Relates a Watershed feature to its downstream feature, thus 
creating feature to feature connectivity. NextDownlD is equal 
to the HydrolD of the next downstream feature. 
AreaSqkKm Area of the watershed in square km units. This attribute is 
(area in square km) commonly used for modeling purposes and analytic 
calculations. 
FType Distinguishes between types of Watershed features. 
(feature type) 
Figure 2.8 Watershed feature class for representing drainage 
areas. Arc Hydro framework 
and zones within the aquifers such as unconfined 
and confined sections. Aquifer is a polygon feature 
class, where each feature represents an aquifer or a 
part of an aquifer (figure 2.10). 
WW feYalicolalare|exeyfays 
Point feature class for representing 
locations where water is measured = 
Fieldname Description Ree URS 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
Name Text attribute representing the name of the monitoring point. 
JunctionID Relates a MonitoringPoint feature with a river network by 
associating the point feature with a junction on the network. The 
Junction!D of MonitoringPoint feature is equal to the HydrolD of a 
related HydroJunction feature. 
FType Distinguishes between types of monitoring points (e.g., stream 
(feature type) and precipitation gages, water quality monitoring sites). 
Figure 2.9 MonitoringPoint feature class for representing 
locations where water is measured. 
=i Aquifer 
Polygon feature class, where each feature 
represents an aquifer or a part of an aquifer 
Fieldname Description 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating features 
with external information systems. 
Name Text attribute representing the name of the aquifer. 
HGUID Relates aquifer polygons with more detailed descriptions of 
(hydrogeologic hydrogeologic units defined in the HydrogeologicUnit table. 
unit identifier) 
Distinguishes between types of aquifers or zones within an aquifer 
(e.g., unconfined and confined). FType 
(feature type) 
Figure 2.10 Aquifer feature class for representing aquifer 
boundaries. 
23 


CHAPTER 2: ARC HYDRO FRAMEWORK 
Wells are commonly described in groundwater 
databases, and most of the transient data col- 
lected for describing the variability in ground- 
water quantity and quality are collected at wells. 
Well is a point feature class for representing well 
locations and their attributes (figure 2.11). 
Transient data describing the variation in flow, 
water levels, precipitation, and water quality are 
commonly collected at monitoring points and at 
wells. The Arc Hydro framework includes a simple 
tabular structure to store such transient measure- 
ments, to index different types of time series, and 
to relate the time series with spatial features. The 
Arc Hydro framework uses relationships to associ- 
ate time series with monitoring points and wells. 
These relationships are a one-to-many type, thus 
a monitoring point or well feature can have many 
time series records (of different types). 
The temporal component of the framework 
includes three tables: TimeSeries, VariableDefini- 
tion, and SeriesCatalog (figure 2.12). TimeSeries 
is a tabular dataset for storing time series values 
indexed by location, time, and the type of the 
Point feature class for representing well 
locations and their attributes. 
Fieldname __ Description 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
LandElev The elevation of the land surface at the well location. Is 
(land elevation) commonly used to reference vertical information (measured as 
depth along the well). 
WellDepth The depth of the well. Together with the LandElev provides a 
(well depth) description of the well’s 3D geometry. 
AquiferlD Relates a Well feature with an Aquifer feature. The AquiferlD of a 
(aquifer Well feature is equal to the HydrolD of an Aquifer feature. 
identifier) 
AqCode Text describing the aquifer. Is used to symbolize wells based on 
(aquifer Code) _ the related aquifer. 
HGUID Relates the well to a hydrogeologic unit. 
(hydrogeologic 
unit identifier) 
FType Distinguishes between types of wells (e.g., domestic, water 
(feature type) supply, industrial). time-series data, VariableDefinition is a table 
with attributes to describe the nature of a variable 
represented in the TimeSeries table, and Series- 
Catalog is a table for indexing and summarizing 
time series stored in the TimeSeries table. A more 
ES TimeSeries 
Table storing single-variable 
time series 
Fieldname _ Description rgueasseae eee, 
FeaturelD Unique feature identifier. Is equal to the HydrolD of the feature 
associated with the time series value. 
VarlD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
TsTime Time stamp specifying the date and time associated with the time 
series value. 
UTCOffset Number of hours the time coordinate system used to define 
TsTime is displaced from Coordinated Universal Time. 
TsValue Numerical value of the variable at the given location and time. 
SSMAYElarle)(:)PL-yalalicel a 
Table for storing time series values 
Fieldname _ Description ie 
VarilD Unique numerical identifier for the variable within the 
geodatabase. 
VarName The name of the variable. 
VarDesc 
VarUnits The description of the variable. 
Units of measure for the variable. 
E SeriesCatalog 
Table for indexing and 2518 MocaonngP ont | a : ; 2817 MondodngPoin summarizing time series = 
stored in the TimeSeries 
table 
Fieldname _ Description 
FeaturelD Unique feature identifier. Is equal to the HydrolD of the feature 
associated with the time series summarized in the catalog. 
FeatClass Name of the feature class to which the related feature belongs. 
VariD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
TsTable Table containing the time series records. 
StartTime The start date/time value of the series. 
EndTime The end date/time value of the series. 
ValueCount Number of time-series values in the series. 
Figure 2.11 Well feature class for representing the location 
of wells and their basic attributes. 
24 Figure 2.12 TimeSeries,VariableDefinition, and SeriesCata- 
log tables for storing temporal data. 


‘complete description of these tables is presented 
in chapter 7. 
The Arc Hydro framework is simple and is 
easily created, yet it is powerful enough to support 
a range of applications. First, the relationships in 
the framework support a variety of querying and 
visualization capabilities. Some simple example 
queries are: “show me all the domestic wells in 
the Edwards Aquifer,” or “select all streams and 
water bodies within the Guadalupe River basin,” 
or “select all stream segments related with the 
Edwards Aquifer outcrop.” More sophisticated 
queries joining features and TimeSeries (e.g., 
using the Well-TimeSeries relationship) can be 
used to plot observations such as streamflow and 
groundwater levels over time, and we can design 
special SQL-based queries to generate maps of 
groundwater levels and groundwater quality for 
mapped aquifers (see chapter 7 for more details on 
creating spatial-temporal views of groundwater 
observations). Because the framework represents 
both surface water and groundwater features, we 
can visualize and analyze data for surface water 
and groundwater in conjunction. 
Implementation 
This section outlines the main steps involved in 
creating and populating the Arc Hydro frame- 
work. The first step is to create the geodatabase 
classes necessary for your project. You can use the 
XML schema as a template to create the frame- 
work classes, or you can create them with ArcCat- 
alog. After creating the classes, you set the spatial 
reference appropriate for your project, add project 
specific attributes, add relationships, create addi- 
tional tables and feature classes if necessary, and 
add coded value domains for selected attributes. 
The next step is to document your newly created 
data model. 
Once the data model is defined you can import 
data into your geodatabase. Next, HydroIDs are Implementation 
assigned to the features, and relationships are 
established. New features can be created and attri- 
butes calculated. Finally, you can use the results 
of this process to create products such as maps, 
scenes, and reports. The following checklist pro- 
vides a summary of the main steps for creating the 
Arc Hydro framework. 
Checklist 
. Create the classes of the Arc Hydro framework 
(manually using ArcCatalog or by importing from 
an XML schema) 
. Define the spatial reference, add project specific 
classes, attributes, relationships, and domains as 
necessary rn 
N 
Ww . Document the datasets and changes made to the 
data model 
4. Import data into the framework classes (e.g., 
streams, wells, aquifers, time series) 
nn . Assign key attributes to uniquely identify the 
features and establish relationships 
oO’ . Apply tools to create new features and calculate 
attributes 
N . Visualize data and create products (maps, scenes, 
reports) 
25 


CHAPTER 2: ARC HYDRO FRAMEWORK 
The following example of an Arc Hydro 
Framework representation of the Guadalupe Basin 
and the Edwards Aquifer in Texas illustrates the 
use of the framework to represent surface water 
and groundwater features. After creating the fea- 
ture classes of the framework, the first step is to 
import data into the framework geodatabase. In 
the following example we added streams, water 
bodies, and watersheds from the National Hydrog- 
raphy Dataset (NHD). HydroIDs were assigned to 
all features so they could be uniquely identified 
within the geodatabase. HydroCodes were estab- 
lished to maintain the original public identifier of 
the features. For example, river reaches from NHD 
were imported into the WaterLine feature class 
SMS EL ah a. 
pend oes : 
PRIS SI 
Zee, (figure 2.13). Each line was assigned a HydroID 
that became its unique identifier within the Arc 
Hydro geodatabase. In addition, the NHD reach 
codes were imported to the HydroCode attribute 
of the of the line features. For example, the river 
reach representing the Blanco River was indexed 
with a HydrolD of 8753, which became its unique 
identifier within the geodatabase. The NHD code 
for this reach is 12100203000078, thus the Hydro- 
Code given to this station is 12100203000078 to 
represent the original reach code. You can have 
multiple NHD river segments with the same reach 
identifier, thus you may have multiple WaterLine 
features each with a unique HydroID sharing the 
same HydroCode. 
rN 
ca 
KAAINS [221H0}0285 "Sy JO Asayinod ejeg 
~__ 8757 /12100202000324 [Fi 
Reco | «ff 0 >| 
Figure 2.13 WaterLine features created by importing river reaches from the NHD. The HydrolD (in this case 8753) is a 
unique feature identifier within the geodatabase, and HydroCode (12100203000078) is the public identifier that relates to 
external information systems, in this case NHD. 
26 
