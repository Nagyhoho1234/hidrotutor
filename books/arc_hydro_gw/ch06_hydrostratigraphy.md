# Chapter 6: Hydrostratigraphy

pieog juatudojanag salem sexe jo Asaqino> e1eG Steps for creating 3D borehole data 
a Attributes of Well 
Figure 5.18 Example of well-construction data stored in the BoreholeLog table. The relationship between well-comple- 
tion data and Well features is established by populating the WelllD attribute in the BoreholeLog table. 
63 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
The following example demonstrates the use 
of the BoreholeLog table to store hydrostrati- 
graphic data. The USGS has developed a 3D 
geologic framework of the Edwards Aquifer in 
Bexar County (Pantea and Cole 2004). The frame- 
work includes stratigraphic data from about 450 
wells, representing ten stratigraphic units and 
three hydrogeologic units (see a more detailed 
discussion on representation of 3D stratigraphy 
and hydrogeologic units in chapter 6). The strati- 
graphic data are given as a set of elevations, where 
each elevation represents a stratigraphic pick (the 
3D location where the well penetrates a strati- 
graphic unit). The horizontal location is defined 
by x and y coordinates followed by a set of ver- 
tical (z) coordinates defining tops of formations 
(figure 5.19). Not all formations are represented 
in all wells, and the number of stratigraphic picks 
can range from one to the number of stratigraphic 
units (10 in this case). Well features were created from the x,y 
coordinates, and HydroIDs were assigned to 
the Well features. The vertical information was 
imported into the BoreholeLog table, such that 
each row in the BoreholeLog table stores a strati- 
graphic pick related to a Well feature through the 
WellID attribute. Figure 5.20 shows an example of 
stratigraphy for Well 3266 (well code Ay-68-30-807). 
750 
Upper confining unit Well feature 
(HydrolD = 3266) @ 
Land elevation = 750 ft 
(above mean sea level) as 
146 
Georgetown Fm. (GTWN) 
128 
Cyclic + Marine member (CYMRN) 
Leached + collapsed member (LCCLP) 41 
Regional dense member (RGDNS) -60 
"| 81 
| Grainstone member (GRNSTN) 
Kirschberg evaporite member (KSCH) 
-217 
Dolomitic member (DOLO) 
-372 
Lower confining unit, upper Glen Rose (UGLRS) 
433 
Figure 5.20 Conceptual view of 3D stratigraphic data 
along a borehole. 
Type: scattered data # 
# Version: 
# Description: updated well and surface picks from USGS office San Antonio, Texas, 2/3/04 
# Format: free 
# Field: 1 wellid non-numeric 
# Field: 2 x 
# Field: J y 
# Field: 4 LSD feet 
# Field: 5 GTOWN feet 
# Field: 6 CYMRN feet 
# Field: 7 LCCLP feet 
# Field: 8 RGDNS feet 
# Field: 9 GRNSTN feet 
# Field: 10 KSCH feet 
# Field: 11 DOLO feet 
# Field: 12 BSNOD feet 
# Field: 13 UGLRS feet 
# Field: 14 LGLRS feet 
# Field: 15 BOTTOM feet 
# Field: 16 wT feet 
# Field: 17 SYMBOL integer 
# Projection: Universal Transverse Mercator 
# Zone: 14 
# Units: meters 
# Ellipsoid: Clarke 1866/NAD27 
# End: 
mO1 562588.2127 3278912.228 elas: eed 
m02 562664. 3297 3278860.636 ae hu 
m03 561211. 3176 3280911.12 Bae ae 
m04 561246.599 3280998.11 Uae ue 
m05 561409. 8196 3281286.481 see ed 
m06 555831.7998 3274689.727 ee 890 
m07 556358. 8088 3276018. 304 es Lae 
m08 556394.5713 3276020.023 the bt 
m09 550489. 534 3276215 .977 ie 985 
m10 552633.0826 3275756.452 ares sige 
mil 552657. 3674 3275797.193 me ee 
m12 546867.4363 3273027.965 at 875 
m13 546014. 3822 3273350. 38 955 ee 
m4 541898. 3365 3270921.297 985 eM 
m15 543105.0051 3271446.003 eA 905 
m16 541060.6341 3275433.315 nee ae 
m7 540937.9673 3275143.555 oe 
m8 537630.5677 3275342.196 
m19 537905 .4843 3275332.349 ABAAng je21Ho0j0ayd “SQ 4o Asayinod ejeq 
950 to ay if ans - 1 990 ee pnt alt 
mee 970 he Hae is 
sess) 910 ee 1 
yet 890 on eae us 
910 ee 1s ae ab 
ee 900 Aad nA 1 
920 vi cae za! af 
Hee SLE Lew 1 
1 
1150 es al! 
nh 1095 1 
sh 1255 ach at 
ey 1125 a 
64 Figure 5.19 Three-dimensional stratigraphic data developed as part of a 3D geologic framework of the Edwards Aquifer 
in Bexar County (Pantea and Cole 2004). The first column is a well identifier, followed by x and y coordinates. The next 
columns (4 to 16) contain a series of elevations representing Stratigraphic picks (tops of stratigraphic units). 


A conceptual view of this data starts from the 
land surface at an elevation of 750 feet above mean 
sea level (as recorded in the LandElev attribute of 
the Well feature), and a set of stratigraphic units 
are defined in sequence representing the strati- 
graphic layers down to a depth of 433 feet below 
mean sea level. 
— Attributes of Boreholel og 
feet above MSL CYMRM Steps for creating 3D borehole data 
Figure 5.21 shows the same stratigraphic data 
shown in figure 5.20 stored within the BoreholeLog 
table. In this example, data are already given in 
absolute units of feet above mean sea level, thus 
the RefElev, FromDepth, and ToDepth attributes 
are not populated. The Material attribute shows 
the stratigraphic units, and the HGUID and 
1) ‘Georgetown Fim ; | |Hydrostratigraphy 
2 Person Fm LHydrostratigraphy feet above MSL /LCCLP 
feet above MSL | RGDNS ~2 [Person Fm |Hydrostratigraphy 7 
| _ 2 Person Fm |Hydrostratigraphy | 
__feet above MSL_|GRNSTN 
[feet above MSL_|KSCH ie 3 Kainer Fm ___Hydrostratigraphy 
_ feetabove MSL [DOLO | ==T 3 \KainerFm ————_Hydrostratigraphy | 
3 |Kainer Fm ~ |Hydrostratigraphy 
‘feet above MSL_|BSNOD — 3 |Kainer Fm |Hydrostratigraphy 
|feet above MSL_|UGLRS 4 (Glen Rose Limestone Hydrostratigraphy | 
pieog juaudojanag Jajep sexa) pue Aaains |ed1H0j0a5 *S"/q Jo Asayinod ejeq 4 (Test hole | 
ai ‘Test hole | al es 47 Test hole | | 
Figure 5.21 Stratigraphic picks stored in the BoreholeLog table. Borehole data are related to Well features with the 
HydrolD-WelllD relationship. 
65 


CHAPTER 5: AQUIFERS, WELLS, AND BOREHOLES 
HGUCode show a classification of the data into 
hydrogeologic units. 
After importing the stratigraphic data into the 
BoreholeLog table, custom tools can be applied 
to create 3D BorePoint and BoreLine features that 
can be visualized in ArcScene. In the following 
example (figure 5.22), BorePoint features were cre- 
ated from all the stratigraphic picks available in 
the dataset. The BoreLine features were created 
for a smaller set of wells where interval data were 
available (where a number of picks are available 
for the same well). 
Vertical information recorded along boreholes 
is the basis for creating 3D subsurface represen- 
tations. It is common to start by interpolating 
hydrostratigraphic data to generate views of the 
subsurface, such as cross sections, surfaces, and 
volumes. The process of creating 3D subsur- 
face representations of hydrostratigraphy and 
@ Upper confining unit 
@ GTOWN 
@ CYMRN 
@ LCCLP 
@ RGDNS 
@ GRNSTN A2aing |221b0|0ad *s‘p Jo Asajino> ejeg hydrogeologic units and showing how these can 
be stored within the geodatabase is presented in 
the next chapter. 
References 
ASTM. 2004. D5254-92 (2004) Standard practice for minimum 
set of data elements to identify a groundwater site. 
ANG Committee 1999. The Australian National Groundwater 
Data Transfer Standard Release 1.0, Australian National 
Groundwater Committee, Working Group on National 
Groundwater Data Standards. 
Pantea, Michael P., and James C. Cole. 2004. Three-Dimen- 
sional Geologic Framework Modeling of Faulted Hydro- 
stratigraphic Units within the Edwards Aquifer, Northern 
Bexar County, Texas. USGS Scientific Investigations Report 
2004-5226. 
@@m Upper confining unit 
qm GTOWN 
=m CYMRN 
qm LCCLP 
@— RGDNS 
qm GRNSTN 
4 KSCH 
@ DOLO 
@m BSNOD 
qm UGLRS 
Figure 5.22 Three-dimensional view of stratigraphy displayed in ArcScene showing 3D features created from the Bore- 
holeLog table: a) BorePoint features represent stratigraphic pi 
stratigraphy as intervals. 
66 cks (top of formation), and b) BoreLine features represent 


HydrogeologicUnit 
Tabular representation of hydrogeologic units. 
Representation: Table. 
GeoArea 
2D extent of hydrogeologic units. 
Representation: Polygon features. 
GeoSection and SectionLine 
Representation of cross sections as 2D lines in plan view and as 3D features. 
Representation: Polyline and Multipatch. 
GeoRasters 
Collection of rasters describing properties of hydrogeologic units. 
Representation: Raster catalog. 
GeoVolume 
3D volumes representing hydrogeologic units. 
Representation: Multipatch. 
XS2D 
2D cross section view of 3D information along a SectionLine. 
Representation: Point, polyline, and polygon features displayed in a separate 
data frame with a unique coordinate system along a SectionLine feature 
DESCRIBING THE SUBSURFACE IS A KEY PART OF MANY GROUNDWATER-RELATED 
projects. Because we cannot directly view and sample subsurface strata continuously, we 
develop conceptual models that reflect our best understanding of the arrangement and 


CHAPTER 6: HYDROSTRATIGRAPHY 
properties of subsurface strata. These conceptual 
models are based on observations from outcrops, 
boreholes, and geophysical surveys, but much of 
the data are inferred through interpolation and 
interpretation. For groundwater purposes, we 
develop a hydrogeologic framework, a geologic 
framework that defines a distinct hydrologic 
system. In a hydrogeologic framework, subsur- 
face materials are classified not only by the rock 
properties but also by the hydraulic properties 
that effect water storage and flow. The creation of a 
hydrogeologic framework commonly involves the 
creation of 3D objects such as cross-sections, sur- 
faces, and volume elements. This chapter describes 
the process of creating a hydrogeologic framework 
and how related datasets are represented in an Arc 
Hydro Groundwater geodatabase. 
A hydrogeologic unit is any soil or rock unit or 
zone which by virtue of its hydraulic properties has 
a distinct influence on the storage or movement of 
groundwater (USGS glossary of hydrologic terms: 
http://or.water.usgs.gov/projs_dir/willgw/ 
Gd GeoVolume | 
HydrolD 
_ | HydroCode $i GeoArea ues 
| HydrolD 
| HydroCode m == HydrogeologicUnit F 
| HydrolD 
HGUCode | 
HGUName | HGUID _ | HGUID fara 
AquiferlD | HGUCode HGUCode eae 
AqCode | Horizon!D | Horizon!D red 
| Description 
HorizonID FType =] coy 
| | | 
| aa 
= Sd GeoSection 
HydrolD 
| HydroCode 
_ | SectionID 
| SName 
| HGUID HydroCode glossary.html). Establishing a hydrogeologic 
model that describes the spatial extent and prop- 
erties of hydrogeologic units is the starting point 
for many groundwater projects. The terms aqui- 
fer and hydrogeologic unit are commonly used to 
abstract the subsurface into conceptual elements 
related to groundwater storage and flow. An aqui- 
fer describes a water-bearing body of subsurface 
strata, which in many cases is subdivided and 
classified for management and regulatory pur- 
poses. An aquifer or aquifer system can include a 
number of hydrogeologic units, which may consist 
of several permeable units separated by less per- 
meable confining units. In many cases aquifers and 
hydrogeologic units are mapped as 2D polygons, 
and these mapped features are used for water- 
resource planning, management, and regulation. 
Hydrogeologic units can also be described as 3D 
features and visualized through a combination of 
mapped units, cross-sections, surfaces, and vol- 
umes. For example the Edwards Aquifer described 
in previous chapters was mapped as a set of 
Kecococee | 
Raster Figure 6.1 Analysis diagram showing 
Name 
Description the data elements in the hydrostratig- 
Units HGUID raphy component of the groundwa- 
HGUCode Horizon ter data model (see figure 6.15 for 
AquiferlD il Fer KaGode a detailed description of the XS2D 
component representing 2D cross 
sections). 
| HGUCode 
‘| HorizonID 
FType _ | SName 
| VertExag2D 
>> | FType '| SectionLine feature 
ten00 XS2D component: displayed in a separate 
| | data frame with unique coordinates along a 
68 


2D polygons defining the extent of the aquifer 
outcrop and confined zones. In chapter 5, a more 
detailed 3D dataset describes stratigraphic units 
of the Edwards Aquifer as 3D points and lines 
derived from borehole logs. The stratigraphic units 
described in chapter 5 can be categorized into 
more general hydrogeologic units used to describe 
groundwater flow and storage. 
Geodatabase representation of 
hydrogeologic units 
Chapter 3 described the process for creating a 3D 
description of hydrogeologic units. This process 
starts with point and interval data and continues 
through the creation of cross-sections and fence 
diagrams, the interpolation of surfaces for repre- 
senting the top and bottom of hydrogeologic units, 
and the construction of volume objects. To sup- 
port different spatial representations, the hydro- 
stratigraphy component includes the GeoArea, 
GeoSection, and GeoVolume feature classes and 
the GeoRasters raster catalog. Each of the spa- 
tial datasets is related to a conceptual (tabular) 
description of hydrogeologic units stored in the 
HydrogeologicUnit table. An additional compo- 
nent for dealing with 2D cross-sections (XS2D) 
includes a set of feature classes representing 3D 
data projected on a 2D cross-section plane along a 
section line of interest (figure 6.1). Geodatabase representation of hydrogeologic units 
One of the first steps in developing a hydrogeo- 
logic model is to establish a set of conceptual units. 
The conceptual model may vary for different cases, 
depending on the scale and requirements of the 
project. HydrogeologicUnit is a tabular represen- 
tation of hydrogeologic units. Attributes associ- 
ated with the hydrogeologic units are defined in 
the table, and spatial features created to describe 
the spatial location and extent of the units are 
related back to the conceptual definition in the 
table. Attributes of the HydrogeologicUnit table 
are shown in figure 6.2. 
Ea. HydrogeologicUnit 
Table for representing hydrogeologic units 
Fieldname — Description 
HydrolD Unique identifier in the geodatabase used for creating 
relationships between classes of the data model. Used to relate 
between hydrogeologic units defined in the table and spatial 
features within the hydrostratigraphy component. 
HGUCode Hydrogeologic unit code. The permanent identification code of 
hydrogeologic units, used to establish a linkage with external 
information systems. 
HGUName Text descriptor of hydrogeologic units used for labeling and 
symbolization. 
AquiferlD Aquifer identifier for grouping hydrogeologic units. Aquifer|D is 
also used to relate hydrogeologic units in the table with Aquifer 
features. 
AqCode Aquifer code, Text descriptor of the aquifer used for labeling, 
symbolization, and querying. 
Description Text for storing detailed descriptions of hydrogeologic units. 
HorizonID Index for describing the depositional sequence of hydrogeologic 
units. 
Figure 6.2 HydrogeologicUnit table for representing con- 
ceptual hydrogeologic units. 
69 


CHAPTER 6: HYDROSTRATIGRAPHY 
The following example shows how conceptual 
hydrogeologic units are grouped to define more 
general aquifers and confining units. For exam- 
ple, Aquifer A is a theoretical aquifer composed of 
three hydrogeologic units: a confining layer and 
two permeable formations (top and bottom units). 
The units are represented by three items (rows) in 
the HydrogeologicUnit table (figure 6.3). Each of 
the units is indexed with a HydroID, which will 
be its unique identifier within the geodatabase. 
The units are also indexed with the same aquifer 
identifier (AquiferID) and code (AqCode). In this 
example, the hydrogeologic units are indexed with 
AquiferID = 1001, which is the HydroID of an Aqui- 
fer feature that represents the boundary of Aquifer 
A. Thus, in this case three hydrogeologic units are 
grouped together to represent Aquifer A and are 
related to the same polygon feature representing 
the aquifer boundary. 
Units also are indexed with a HorizonID, an 
index defining the vertical arrangement of 
hydrogeologic units in a depositional sequence. 
HorizonID values are assigned from bottom to 
top such that the smallest HorizonID is given 
to the base unit (the first layer in a deposition 
sequence), and the largest is given to the top unit. 
We use the HorizonID attribute to build cross- 
sections and volumes by filling between hori- 
zons from bottom to top (following the method 
by Lemon and Jones, 2003). Figure 6.4 illustrates 
the concept of horizons and how they relate with 
hydrogeologic units. 
a Attributes of Ly dropeplogicl nt 
101 |HGU1 ‘(Confining | 
102 |HGU 2 Top Unit 
— 103/HGU3 | 
104) IHGU4 _ |Base ~eNull> 
coef > ol _{sMull> Toe Wiech 
__lmpermeable layer 1001 | Aquifer A (Formation consisting ¢ of limestone and dolomitic limestone == 
Show: ar Selected Conceptual units defined in the hydrogeologic 
unit table can be described by different 2D and 3D 
spatial datasets. The units can be represented as 
2D polygon features, where each polygon defines 
a boundary of a unit or part of it; as 3D panels that 
represent cross-sections along a section line; as 
surfaces that define the top and bottom boundar- 
ies of units; and as volume objects that represent 
the 3D geometry of units. The spatial datasets all 
represent the same conceptual units defined in the 
HydrogeologicUnit table, thus each of the spatial 
classes is indexed also by a hydrogeologic identifier 
(HGUID) that relates to the conceptual description 
of the unit in the HydrogeologicUnit table. 
GeoArea is a polygon feature class representing 
the 2D extent of hydrogeologic units. It is impor- 
tant to make a distinction between the concept of 
GeologyArea (presented in chapter 4) and Geo- 
Area. GeologyArea features represent outcrops 
HorizonID=4 
HorizonID=3 
HorizonID=2 
Horizon|ID=1 
HorizonID=0 
Figure 6.4 HorizoniDs define the vertical arrangement of 
hydrogeologic units from bottom to top. 
1001) Aquifer A |Top confining layer consists of clay and sand 
4001 Aquifer A |Formation 1 consisting of permeable limestone 
a 
Re oe Se a A tS A 
Records (0 out of 4 Selected) 
Figure 6.3 Example of hydrogeologic units defined in the HydrogeologicUnit table. 
70 


of geologic units from surficial geologic maps, 
while GeoArea is more conceptual and _ repre- 
sents boundaries of hydrogeologic units that can 
exist on the surface and in the subsurface. The 
extent of GeoArea features can be inferred and are 
= GeoArea 
Polygon features representing the 
2D extent of hydrogeologic units 
Fieldname Description — 
HydrolID Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating features 
with external information systems. 
HGUID Hydrogeologic unit identifier. Relates GeoArea polygons with more 
detailed descriptions of hydrogeologic units defined in the 
HydrogeologicUnit table. 
HGUCode Text descriptor of hydrogeologic units used for labeling, 
symbolization, and queries. 
Horizon!D . Index for describing the depositional sequence of hydrogeologic 
units. 
FType Distinguishes between types of GeoArea features. 
Figure 6.5 GeoArea features represent the 2D extent of 
hydrogeologic units. 
Figure 6.6 An example of GeoArea 
features representing boundaries of 
hydrogeologic units. The top hydrogeologic unit 
(HGU 1) is represented by multiple GeoArea features, 
indexed with the same HGUID. Geodatabase representation of hydrogeologic units 
not restricted to surficial outcrops. Attributes of 
GeoArea features are shown in figure 6.5. 
One hydrogeologic unit in the HydrogeologicUnit 
table can be associated with multiple GeoArea fea- 
tures. This allows mapping of discontinuous hydro- 
geologic units as multiple polygon features related 
to the same conceptual description in the Hydro- 
geologicUnit table. Figure 6.6 shows an example of 
a hydrogeologic unit defined by three separate Geo- 
Area features. In the example HGU 1 is defined by a 
number of separate features, and each feature con- 
tains a unique HydrolD. The features have the same 
HGUID and HGUCode relating to the definition of 
the unit in the HydrogeologicUnit table. 
de] HGUID_| g HGUCode_ 
71 


CHAPTER 6: HYDROSTRATIGRAPHY 
Cross-sections are commonly used to illustrate 
the vertical dimension of hydrogeologic units 
along a defined section line. The first step in creat- 
ing a cross-section is to define a 2D section line in 
plan view. Then a cross-section is created to pro- 
vide a 3D view of hydrogeologic units along the 
section line. It is common to add additional infor- 
mation on the cross-section such as stratigraphy or 
geophysical logs recorded at boreholes along the 
cross-section, or water-related properties such as 
water levels and water quality. Figure 6.7 shows an 
example of a cross-section showing hydrogeologic 
units of the Edwards Aquifer. 
We use two feature classes to represent cross- 
sections in the hydrostratigraphy component: Sec- 
tionLine is a polyline feature class for representing 
2D cross-section lines on a map, and GeoSection is 
a multipatch feature class representing 3D panels 
for constructing vertical cross-sections. Each fea- 
ture in the GeoSection feature class represents a 
slice of a hydrogeologic unit, and a set of GeoSec- 
tion features represent a complete cross-section 
} NGVD29 
“100 across multiple units. Attributes of SectionLine 
and GeoSection features are shown in figure 6.8 
and figure 6.9, respectively. 
Each GeoSection feature is a panel within a 3D 
cross-section that represents a single hydrogeologic 
unit along the section line (figure 6.10). Thus one 
can display or query data for specific hydrogeologic 
units based on the HGUID and HGUCode fields. The 
SY-Yeu toy a) Mil aT=) 
2D polyline features defining 
cross sections on a map 
Fieldname Description _ ae ee 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
SName Section name. Text descriptor of the section line for labeling, 
symbolization, and queries (e.g., A-A’). 
VertExag2D Vertical exaggeration that will be applied when creating XS2D 
features (see section on representing vertical cross sections in 
2D). 
|FType Distinguishes between types of SectionLine features. 
Figure 6.8 SectionLine features represent cross-section 
lines in plan view, 
K 104932802? 
B-8'Cross Section 
AAAANS |RD1H0|OaH “Sf ‘900Z "|e 32 YARID Jo Asayinoy 
2 4 Miles 
a hn VERTICAL EXAGERATION 25x 
Figure 6.7 Example of a cross-section showing the hydrogeologic formations of the Edwards Aquifer in Northefn Medina 
and Northeastern Uvalde counties, south-central Texas (figure modified from Clark et al. 2006). The left figure shows cross- 
section lines drawn in plan view, and the right figure shows the hydrogeologic units along section line A-A’. 
72 


relationship between SectionLine and GeoSection 
features is a one-to-many (1:M) relationship, where 
GeoSection 
3D panels for constructing 
vertical cross sections 
Fieldname _ Description 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
SectionID Equal to the HydrolD of a SectionLine feature. Relates 
GeoSection features with SectionLine features. 
SName Section name. Text descriptor of the section line for labeling, 
symbolization, and queries (e.g., A-A’). 
HGUID Hydrogeologic unit identifier. Relates GeoSection features with 
more detailed descriptions of hydrogeologic units defined in the 
HydrogeologicUnit table. 
HGUCode Text descriptor of the hydrogeologic unit used for labeling, 
symbolization, and queries. 
HorizonID Index for describing the depositional sequence of hydrogeologic 
units. 
FType Distinguishes between types of GeoSection features. 
Figure 6.9 GeoSection features represent 3D panels of a 
cross-section. Geodatabase representation of hydrogeologic units 
one or more GeoSection features are related with 
a SectionLine feature. The relationship is based on 
the HydroID and SectionID key fields, such that the 
SectionID attribute of GeoSection features is equal to 
the HydroID of a SectionLine feature. This enables 
querying a set of GeoSections along a selected 
section line of interest. 
Surfaces are commonly used for representing 
boundaries (top and bottom) of hydrogeologic 
units and for describing spatially varying hydrau- 
lic properties (e.g., hydraulic conductivity, trans- 
missivity, and porosity) of hydrogeologic units. In 
ArcGIS, surfaces can be created as raster or as tri- 
angular irregular networks (TIN) datasets. Raster 
datasets represent imaged, sampled, or interpo- 
lated data on a uniform rectangular grid. Each cell 
in the raster holds a value that represents a prop- 
erty of the surface, such as average elevation, over 
the cell’s area. TIN datasets represent surfaces 
as a triangulated network with nodes containing 
pie 
HF Attributes of SectionLi ne 
ag Ed of GeoSection 
Fiscord: 1 < oar T >| nies Show: a Selected i poss 5 (1 out of 23 Selected) 7 =a B Bina) EERE Section | 1 a re ee Te) 
1 >| Ca} Show: [all Selected | Records (lout w 
Figure 6.10 Example of SectionLine and GeoSection features representing cross-sections. GeoSection features are 
indexed with a Section|D that is equal to the HydrolD of a SectionLine feature. 
73 


CHAPTER 6: HYDROSTRATIGRAPHY 
surface values (e.g., elevation) and triangle edges 
connecting the nodes (for more information on 
rasters and TINs, see Zeiler 1999). 
GeoRasters is a raster catalog for storing raster 
datasets that describe properties of hydrogeologic 
units. The catalog enables storing and attributing 
rasters within the geodatabase. For example, a set 
of rasters can be created for representing the top 
fs GeoRasters 
Raster surfaces describing 
properties of hydrogeologic units. 
Fieldname Description 
Name Generic raster catalog attribute (created automatically when you 
create a raster catalog) used to store the name of a raster 
dataset. 
Description Text descriptor of the raster (e.g., formation top, formation 
bottom). 
RasUnits The raster units (e.g., feet above mean sea level). 
HGUID Hydrogeologic unit identifier. Relates rasters in the catalog with 
more detailed descriptions of hydrogeologic units defined in the 
HydrogeologicUnit table. 
HGUCode Text descriptor of the hydrogeologic unit used for labeling, 
symbolization, and queries. 
HorizonID Index for describing the depositional sequence of hydrogeologic 
units. 
AquiferlD Relates rasters with Aquifer features. The AquiferlD attribute of a 
GeoRaster relates to the HydrolD of an Aquifer feature. 
AqCode Aquifer code. Text descriptor of aquifers used for labeling, 
symbolization, and querying. 
Figure 6.11 GeoRasters raster catalog for storing and 
indexing raster datasets describing properties of hydro- 
geologic units. 
at Attributes of GeoRasters 
_jtop of formation of hydrogeologic units within a 3D hydrogeologic 
model. Each raster dataset represents the top of 
a formation, and in sequence the raster surfaces 
define a set of 3D units, where each unit is defined 
by a top and bottom surface (the bottom surface is 
the top of the unit below). An advantage of stor- 
ing raster datasets within the raster catalog is the 
ability to attribute the rasters. Attributes of rasters 
in the raster catalog can be edited within ArcMap 
like any other dataset. Figure 6.11 shows the 
attributes of the GeoRasters raster catalog. 
The example shown in figure 6.12 shows a set of 
raster surfaces stored in the GeoRasters raster cata- 
log. Each raster in the catalog represents the top of 
a hydrogeologic unit in feet above mean sea level. 
The units represented by the rasters are indexed 
with different HGUID values (101, 102, and 103). 
Three of the four rasters in the catalog are part of 
Aquifer A, thus they are indexed (in the AquiferID 
attribute) with the HydroID of the Aquifer feature 
representing Aquifer A, which is 1001. The rasters 
are also indexed with HorizonIDs to indicate the 
sequence of the units within the hydrogeologic 
framework. 
GeoRasters can also represent continuous 
properties of aquifers or hydrogeologic units, such 
as conductivity, transmissivity, and specific yield 
al 'top of formatior 
Show: = sila 
HGU3 
HGU1 
74 [al Selected aif Options . | 
Figure 6.12 Example of rasters stored in the Geo- Records (0 out of 4 Selected) 
Raster raster catalog. Each raster defines the top 
surface of a hydrogeologic unit. 


that are commonly interpolated from point data. 
The point data can be stored as attributes of Well 
features, and the interpolated results can be stored 
as raster datasets in the GeoRasters raster catalog. 
| GeoVolume 
3D volume objects representing 
hydrogeologic units 
Field name Description 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
HGUID Hydrogeologic unit identifier. Relates GeoVolume features with 
more detailed descriptions of hydrogeologic units defined in the 
HydrogeologicUnit table. 
HGUCode Text descriptor of the hydrogeologic unit used for labeling, 
symbolization, and queries. 
HorizonID Index for describing the depositional sequence of hydrogeologic 
units. 
FType Distinguishes between types of GeoVolume features. 
Figure 6.13 Attributes of GeoVolume features, which rep- 
resent hydrogeologic units as 3D volumes. 
Figure 6.14 Example of GeoVolume fea- 
tures representing hydrogeologic units Geodatabase representation of hydrogeologic units 
Although they can be represented using 
different types of features (cross-sections, 3D points 
and lines, surfaces, etc.), hydrogeologic units are 
fundamentally 3D objects. When developing a 3D 
hydrogeologic model, it is common to develop a 
set of 3D volumes representing the hydrogeologic 
units within the model. GeoVolume is a multipatch 
feature class for representing hydrogeologic units 
as 3D volume objects (figure 6.13). 
Each GeoVolume feature represents a hydro- 
geologic unit or a portion thereof, thus they are 
indexed with HGUID and HGUCode values that 
relate them with hydrogeologic units defined in 
the HydrogeologicUnit table. GeoVolume fea- 
tures can be displayed in ArcScene for visualizing 
3D hydrogeologic models. Figure 6.14 shows an 
example of GeoVolume features, where each fea- 
ture defines a closed volume of space representing 
a specific hydrogeologic unit. 
UID | HGUCode| 
as closed 3D volume objects. 
|__1|Interpolated |) j >| 
2 
Micu1 
Bircu2 
Bicus 
75 


CHAPTER 6: HYDROSTRATIGRAPHY 
Representing vertical cross-sections 
in 2D 
The feature classes of the hydrostratigraphy 
component described thus far can be visualized 
both in plan and 3D view. However, when it comes 
to displaying vertical cross-sections taken along a 
section line, sometimes a special 2D view is desired. 
In this view the cross-section is flattened out so 
that on a plot of the cross-section, the horizontal 
axis represents the distance along the section line 
(which may or may not be a straight line), and the 
vertical axis represents depth. In other words, this 
2D view translates real world (x, y, and z) coordi- 
nates into (s, z) coordinates, where s is the length 
along the section line and z is elevation. In addition, 
cross-section features are often scaled (exaggerated) 
in the vertical direction for better visualization. 
In the groundwater data model, the 2D 
representation of cross-sections is implemented with 
XS2D 
Catalog 
ae 
Minor Grid 
76 multiple feature classes, and these are given the 
“XS2D” prefix (e.g., XS2D_Boreline and XS2D_Panel). 
Each XS2D feature class is associated with a single 
SectionLine feature, which is indexed by a HydroID. 
For example, if you have three section lines defined 
in the SectionLine feature class with HydroIDs of 1, 
2, and 3, then you could have three sets of XS2D fea- 
ture classes in your geodatabase, following a certain 
naming convention such as XS2D_Panel_1, XS2D_ 
Panel_2, and XS2D_Panel_3. Since a single section- 
line feature could be associated with hundreds or 
even thousands of XS2D features, storing features 
associated with different section lines in separate 
XS2D feature classes helps to keep data organized. A 
value representing the vertical exaggeration is stored 
on the SectionLine features (in an attribute named 
VertExag2D), as it is assumed that all XS2D fea- 
tures associated with a given section line share the 
same vertical exaggeration. Figure 6.15 shows the 
geodatabase representation of the XS2D component. 
HydrolD 
HydroCode 
WelllD 
TopElev 
BottomElev 
Material 
HGUID 
HGUCode 
Offset 
Measure 
IsLeft 
FType 
=i XS2D 
MajorGrid | PS) 
Panel 
|| HydrolD 
HydroCode 
|| HGUID 
HGUCode 
FType 
mi XS2D 
PanelDivider 
| | HydrolD 
| | HydroCode 
_ | Measure 
fi XS2D 
MinorGrid 
» | HydrolD 
| | HydroCode 
| | GridValue 
| | IsVertical Figure 6.15 Analysis 
diagram showing the 
XS2D feature classes 
in the hydrostratig- 
raphy component 
of the groundwater 
data model. The 
upper left figure 
shows SectionLine 
features defining the 
section line in plan 
view, and the lower 
figure shows a typi- 
cal 2D cross-section. 


XS2D_Catalog is a table for managing XS2D 
feature classes and their association with Section- 
Line features. Each row in this table provides the 
name and role of a XS2D feature class and infor- 
mation about its associated SectionLine feature 
(figure 6.16). 
The structure of the XS2D_Catalog table allows 
limitless types of feature classes to be associated 
with a given cross-section. Common XS2D feature 
classes are described below, and additional feature 
classes can be added to represent items such as land 
surface elevation, water table, faults, and more. 
XS2D_Panel is a polygon feature class for rep- 
resenting hydrogeologic units as 2D cross-section 
“panels.” Usually a cross-section will be formed by 
EB XS2D_ Catalog 
Table for managing XS2D feature classes and 
their association with SectionLine features 
XS2D 1 
Fieldname Description xS2D 2 
SectLineFC Name of the SectionLine feature class containing the referenced 
SectionLine feature. 
SectionID HydrolD of the associated SectionLine feature. 
SName Name of the associated SectionLine feature. 
XS2D_FC Name of the XS2D feature class. 
XS2DType Role that the XS2D feature class plays in the cross section (e.g., 
Boreline, Panel, Grid, etc.). 
Figure 6.16 XS2D_Catalog table for managing XS2D 
features. 
=i XS2D_Panel 
Polygon features representing 
hydrogeologic units as 2D cross 
section “panels” 
Field name 
HydrolD Description O 
Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating features 
with external information systems. 
HGUID Hydrogeologic unit identifier. Is equal to the HydrolD of a 
hydrogeologic unit defined in the HydrogeologicUnit table. 
HGUCode Text descriptor of the hydrogeologic unit used for labeling, 
symbolization, and queries. 
FType Distinguishes between types of XS2D_Panel features. 
Figure 6.17 XS2D_Panel features represent hydrogeologic 
units along a section line as 2D panels. Representing vertical cross-sections in 2D 
a set of XS2D_Panel features, each representing a 
hydrogeologic unit along a section line. Figure 6.17 
shows the attributes of the XS2D_Panel feature class. 
XS2D_BoreLine is a polyline feature class for 
representing vertical borehole data projected 
on a vertical plane along a section line. Usually, 
when creating a new cross-section, a set of wells 
is selected near the line defining the cross-section, 
and hydrostratigraphic data along the boreholes is 
projected on the cross-section plane. XS2D_Bore- 
Line features can be created from data stored in 
the BoreholeLog table and serve as guides for 
digitizing XS2D_Panel features. Figure 6.18 shows 
attributes of the XS2D_BoreLine feature class. 
XS2D_BoreLine 
Polyline features representing 
borehole data projected on a 
vertical plane along a section line 
Fieldname _ Description [ ima | 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
WelllD HydrolD of the associated Well feature. 
TopElev Top elevation of the XS2D_BoreLine feature. 
BottomElev Bottom elevation of the XS2D_BoreLine feature. 
Material Description of strata observed along a borehole. Usually 
documented in drilling logs and later classified into 
geologic/hydrogeologic units. 
HGUID Hydrogeologic unit identifier. Is equal to the HydrolD of a 
hydrogeologic unit defined in the HydrogeologicUnit table. 
HGUCode Text descriptor of the hydrogeologic unit used for labeling, 
symbolization, and queries. 
Offset Distance from the well related to the XS2D_BoreLine feature to 
the nearest point on the section line (distance units aré the same 
as the units of the SectionLine feature class). 
Measure Distance along the section line to the Well feature associated 
with the XS2D_BoreLine feature. The distance is measured from 
the starting point of the section line to the point on the section 
line closest to the Well feature. 
IsLeft TRUE if the Well feature associated with the XS2D_BoreLine is 
on the left side of a section line in the direction of digitization. 
FALSE if it is on the right side 
FType Distinguishes between types of XS2D_BoreLine features. 
Figure 6.18 XS2D_BoreLine features represent borehole 
data projected on a vertical plane along a section line. 
77 


CHAPTER 6: HYDROSTRATIGRAPHY 
XS2D_PanelDivider is a polyline feature class 
representing vertical lines on a cross-section plane, 
showing the location where a section line changes 
direction (i.e., the location of vertices of the sec- 
tion line). Panel dividers are used as guides for 
orientation when viewing the 2D cross-section. 
Figure 6.19 shows the attributes of the XS2D_Pan- 
elDivider feature class. 
XS2D_MajorGrid and XS2D_MinorGrid are 
polyline feature classes representing grid lines 
showing the vertical and horizontal dimensions 
in a 2D cross-section. Major grid lines are typically 
drawn as vertical and horizontal lines across the 
cross-section, while minor grid lines are indicated 
by tick marks along the border of the cross-section. 
Grid lines serve as alternative coordinate indicators 
in the vertical axes, because a vertical exaggeration 
often is applied to vertical data, and the regular 
ArcMap coordinate indicators do not capture the 
“real” coordinates of the data. Attributes of the grid 
line feature classes are shown in figure 6.20. 
fj! XS2D_ PanelDivider 
Polyline features showing the 
location where a_ section line 
changes direction (i.e., the location 
of vertices of the section line) 
Fieldname Description ip ee essen 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model, 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
Measure Distance along the section line to the vertex of the line where the 
direction changes. The distance is measured from the starting 
point of the section line to the point of direction change. 
Figure 6.19 XS2D_PanelDivider features represent points 
where a section line changes in direction. 
78 Steps for populating the 
hydrostratigraphy component 
The first steps for implementing this component 
are to refine the geodatabase design to meet your 
specific project needs (see chapters 2 and 9 for a 
detailed description). For example, you may want to 
add descriptive attributes to the HydrogeologicUnit 
table that provide more detailed information on 
units in your study. Once you have built your geo- 
database, you will define hydrogeologic units in 
the HydrogeologicUnit table. You can then import 
or apply tools to create new features and assign 
HydrolDs to the features to create a unique identifier 
that will be the basis for queries and relationships 
within the geodatabase. Also, attribute the features 
with the appropriate HGUID to associate them with 
a hydrogeologic unit defined in the Hydrogeologi- 
cUnit table. You can apply tools to create 2D cross- 
section views of the data using the XS2D component 
feature classes. Finally, you can use the results of 
this process to create products such as maps, scenes, 
and reports. The following checklist provides a 
summary of the main steps for creating the classes 
in the hydrostratigraphy component. 
fs XS2D_MajorGrid 
XS2D_MinorGrid 
Polyline features representing 
grid lines showing the vertical 
and horizontal location in a 2D 
cross section 
Fieldname _ Description 
HydrolD Unique feature identifier in the geodatabase used for creating 
relationships between classes of the data model. 
HydroCode Permanent public identifier of the feature used for relating 
features with external information systems. 
GridValue Elevation or measure (distance along section line) value used for 
labeling grid lines, using the same distance units as the 
coordinate system of the SectionLine feature associated with the 
cross section, 
|!sVertical TRUE if the grid line is vertical; FALSE if it is horizontal. 
Figure 6.20 XS2D_MajorGrid and XS2D_MinorGrid features 
represent grid lines showing the vertical and horizontal 
dimensions in a 2D cross-section. 


Checklist 
1. Create the classes of the hydrostratigraphy compo- 
nent (manually using ArcCatalog or by importing 
from an XML schema) 
2. Add project specific classes, attributes, relation- 
ships, and domains as necessary 
3. Document datasets and changes made to the data 
model 
4. Define conceptual hydrogeologic units for your 
project in the HydrogeologicUnit table 
5. Import data and apply tools to create 2D and 3D 
features and raster surfaces 
6. Assign unique HydrolDs to features and assign 
HGUIDs to link them to hydrogeologic units 
7. Apply tools to create 2D and 3D views of the 
hydrogeologic units 
8. Create products (maps, scenes, reports) 
Stratigraphic units Hydrogeologic units 
Upper confining unit 
Georgetown Fm. (GTOWN) J Georgetown 
Cyclic + Marine member (CYMRN) 
Leached + collapsed member (LCCLP) Bereou 
Regional dense member (RGDNS) 
hte SE 
Grainstone member (GRNSTN) | — < 
Edwards Aquifer Kirschberg evaporite member (KSCH) 
Kainer 
Dolomitic member (DOLO) 
Basal Nodular member (BSNOD) 
Lower confining unit, upper Glen Rose (UGLRS) | i ) Upper Glen Rose 
é i 
Figure 6.21 Ten stratigraphic units were classified into four 
hydrogeologic units. Three of the hydrogeologic units are 
grouped to form a more general unit, the Edwards Aquifer. 
fi Attributes of HydrogeologicUnit 
I [ossectwo | ttyarow [HGucode|  HGUHtame | 
‘4761 [Edward 
4764 jEciw' 
| Steps for populating the hydrostratigraphy component 
The following examples illustrate the creation of 
2D and 3D features for representing the hydro- 
geology of the Edwards Aquifer. The first step 
is to define a set of hydrogeologic units for your 
project. Figure 6.21 shows how the ten hydro- 
stratigraphic units described in chapter 5 were 
classified into four hydrogeologic units, from 
bottom to top: Upper Glen Rose, Kainer, Person, 
and Georgetown. The latter three can be grouped 
to form a more general hydrogeologic unit, the 
Edwards Aquifer. 
For this example, five units were defined in the 
HydrogeologicUnit table (figure 6.22). Three units 
define the Kainer, Person, and Georgetown for- 
mations, which are part of the Edwards Aquifer, 
thus they are indexed with the same AquiferID 
(AquiferID = 4761), which references a polygon 
feature in the Aquifer feature class defining the 
general boundary of the Edwards Aquifer. The 
fourth hydrogeologic unit represents the Glen 
Rose limestone beneath the Edwards Aquifer, 
and the fifth hydrogeologic unit represents the 
Edwards Aquifer as a single hydrogeologic unit. 
The hydrogeologic units (except for the last one) 
are indexed with a HorizonID that defines the 
depositional sequence of the units from bottom 
to top. This is an important attribute for creating 
3D features and keeping track of the correct 3D 
layering of the units. 
f= EK) 
4761 Edwards (Georgetwow 
___ 4764 Edwards \Edwards 
Selected | Records (0 out of 5 Selected) 
Figure 6.22 Example of hydrogeologic units in the HydrogeologicUnit table. The Georgetown, Person, and Kainer units 
form the Edwards Aquifer, thus they are associated with an Aquifer feature through the Aquifer|D attribute. 
79 


CHAPTER 6: HYDROSTRATIGRAPHY 
GeologyArea features 
-GeologyArea representing geologic 
[__] Kainer mapdata =a 
es Person 
es Upper Glen Rose 
ae Upper confining units 
Adains jer1H0}0a5 *S"p Jo Asayinod eeq GeoArea feature representing 
the boundary of the Kainer 
hydrogeologic unit 
After defining conceptual units for our project, 
we can start populating the feature classes of the 
hydrostratigraphy component. Figure 6.23 shows 
GeoArea features representing the extent of the 
Kainer hydrogeologic unit that were delineated 
using data in the GeologyArea feature class (that 
define the outcrops of the hydrogeologic units), 
and points representing borehole hydrostratigra- 
phy. Similarly, boundaries of other units can be 
delineated, and these boundaries can later serve 
as the basis for spatial analysis such as interpolat- 
ing elevations or hydraulic properties within the 
defined hydrogeologic units. 
80 Data points representing 
top elevations of the 
Kainer hydrogeologic unit Figure 6.23 
GeoArea features 
representing the 
extent of the Kainer 
hydrogeologic unit. 


Steps for populating the hydrostratigraphy component 
£2 Attributes of SectionLine ( felt) Se : _ — ————]| Figure 6.24 Section lines defined by connecting a 
sequence of Well features. 
Section A-A’ 
(HydrolD 4666) 
The next step in the process is to create cross- Once a SectionLine is defined, a 3D cross- 
sections. The simplest approach for creating cross-section is created by connecting intervals of 
sections is to delineate a section line connecting a__ hydrogeologic units observed along the bore- 
sequence of wells with related 3D hydrogeologic _ holes. In the example shown in figure 6.25, Bore- 
information. As shown in figure 6.24, two section Line features were connected to form a set of 3D 
lines (A-A’ and B-B’) were drawn connecting Well GeoSection features. Each GeoSection in the cross- 
features, and each of the section lines was then — section is an individual multipatch feature that 
given a HydrolID. represents a single hydrogeologic unit. GeoSection 
Well 3613 Well 3610 
B Attributes of GeoSection 
7 _3| [Borehole | Sections i [| areoforown | fee) 
2 Teale = Bal SS eae = Records (1 out of 31 Selected) Options _-| 
Figure 6.25 Three-dimensional GeoSection features form a fence diagram. The GeoSections were created by connecting 
BoreLine features forming 3D panels representing hydrogeologic units along section lines. 
81 


CHAPTER 6: HYDROSTRATIGRAPHY 
features are related to a SectionLine feature via the 
SectionID attribute, such that we can query, display, 
and symbolize specific cross-sections. Two custom 
attributes (FromWell and ToWell) were added to 
store the well identifiers between which the Geo- 
Section features were constructed. Similarly, you 
can extend the data model to include attributes 
that are useful for your specific project. 
Another common approach for creating cross- 
sections is to develop a set of surfaces representing 
the top of each formation. We can then use custom 
tools that sample the rasters at specified intervals 
along the section line and construct 3D cross- 
Figure 6.26 shows rasters represent- 
ing the top of hydrogeologic units, created from 
hydrogeologic picks stored in the BoreholeLog 
table. The rasters were loaded into the GeoRasters 
raster catalog and indexed with a HGUID to relate sections. 
Ge] Attributes of GeoRasters them with hydrogeologic units defined in the 
HydrogeologicUnit table. Each of the rasters was 
also indexed with a HorizonID that defines the 
depositional sequence of the units from bottom 
to top. The HorizonID is used to process the ras- 
ters indexed in the GeoRasters raster catalog and 
derive 3D GeoSection and GeoVolume features. 
In addition to representing the boundaries (top 
and bottom) of hydrogeologic units and aqui- 
fers, rasters can also represent physical proper- 
ties of hydrogeologic units. For example, it is 
common to interpolate point data to create sur- 
faces representing hydraulic properties of aqui- 
fers such as conductivity, transmissivity, and 
specific yield. The surfaces can then be stored and 
indexed within the GeoRasters catalog. This data 
is commonly used for groundwater calculations 
and analysis or fed as inputs into groundwater 
|_| Polygon SCR 
i | Polygon _|sh Raste Jugirs_ surface _|top of formation 
a iner_surface jtop of formation Pe above mean sea level | 
feet a above mean sea level | | __4772|GLEN ROSE |<Null> 
[4771 | KAINER <Null> l<Null> i<Null> 
ik 
B Polygon _ \< TEs surface |top of formation feet above mean sea level | 4770 PERSON _| <Null> —_|<Null> 
_|sRaste | gtown_surface ‘top of formation 
Record: eas Show: oy Selected | 
Hs ctown 
HE Person 
Be sikainer 
HR” GLEN ROSE SOUZA) 
‘feet above mean sea level | 
Records (0 out of 4 Selected) | 4769|GTOWN [<Null> | <Null> 
Options + | 
Figure 6.26 Rasters representing the top of hydrogeologic units stored in a GeoRasters raster catalog. The rasters are 
indexed with a HGUID that relates them to definitions of hydrogeologic units in the HydrogeologicUnit table and are also 
indexed with a Horizon|D to define the sequence of deposition from bottom to top. 
82 
