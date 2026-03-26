# Chapter 3: Three-dimensional ArcGIS for Subsurface Representation

Aquifer boundaries and well features from the 
Texas Water Development Board database were 
imported into the Aquifer and Well feature classes. 
Similarly to the NHD features, aquifers and wells 
were also assigned HydroID and HydroCode 
values to uniquely identify them within the geo- 
database and to maintain a connection to the orig- 
inal information systems. Additional attributes 
such as FType were also assigned to distinguish 
butes of Aquif 
1D ~ | HydroCode | fe 
pieog juatudojanag Jaye sexe pue Aanins jer16ojoay *s'f Jo Asaqinod eieq 
wan 
Figure 2.14 Example of Aquifer and Well features. tert] 3 9|n| aoa sn Implementation 
between types of wells and zones within the 
aquifer. For example, figure 2.14 shows aquifer 
features symbolized by the FType attribute to dis- 
tinguish between outcrop and confined zones of 
the aquifer. The selected feature in the following 
map (HydroID = 114) shows an unconfined area 
of the Edwards Aquifer. 
Streams that flow across the unconfined zones 
of the Edwards Aquifer are possible recharge 
_11/Outcrop Polygon 
27 


CHAPTER 2: ARC HYDRO FRAMEWORK 
features to the aquifer. Thus, an association can 
be established between river reaches flowing 
over the unconfined zones and the aquifer below. 
This is done by adding an AquiferID attribute to 
the WaterLine feature class and setting it equal 
to the HydroID of the Aquifer feature to which 
WaterLine features are related. In this case, the 
river reaches that intersect the Edwards Aqui- 
fer outcrop are assigned with an AquiferID of 
114, which is equal to the HydroID of the feature 
, Aquifer eA 
[] Confined | ~ 
~ Outcrop 
| WaterLine 
ae os 
CT] eee0 1210020200196 Helifax Creek 
|_| 644 1210020300016 =e A 
Record: 14| cor ee show: All [Selected representing the outcrop zone of the Edwards 
Aquifer (figure 2.15). 
Monitoring stations representing stream gages 
along the river network from the USGS National 
Water Information System (NWIS) were imported 
into the MonitoringPoint feature class. HydroID 
and HydroCode attributes were assigned to the 
stations. For example, a USGS monitoring station 
at New Braunfels, Texas, records the streamflow 
coming out of Comal Springs. The HydroID given 
Polygon 
RRR oN L.A gaeee Pepe | 
pueog Juawuidojanag 103M sexa] pue Aaving je21Bojoay “s'9 Jo Asayinod eleq 
Recorde (67 out of *2000 Selected) _o 
Figure 2.15 WaterLine features can be associated with Aquifer features. An AquiferlD attribute is added to the WaterLine 
feature class and is set equal to the HydrolD of an Aquifer feature. 
28 


to this feature is 2894, and the USGS code for this 
station is 08168710, thus the HydroCode for the sta- 
tion was set as “08168710” to represent the original 
station number. 
In addition to spatial features, time series of 
streamflow and water levels from the NWIS and 
the TWDB groundwater database, respectively, 
were imported into the TimeSeries table. Each Implementation 
time-series record was indexed with the HydroID 
of the feature to which it relates. Thus, each time- 
series record in the table can be located in space 
through the association with its related feature. 
For example, streamflow records recorded at the 
streamflow gage at Comal Springs (figure 2.16) 
were indexed with the HydroID of the Montor- 
ingPoint feature (2894). Similarly, time series 
- Point _ No oO oO w oO co i= a) oO n oO oO 
___ 2898 /08173500 
peqn>-! pue ‘ahj0ay ‘ypseyyd9 HHas5 Jo AsaqinoD Pier ite pecece| anced] aes (ie zy 
create E an Marcos ‘River At feng Tx a = 
Figure 2.16 MonitoringPoint features representing stream gages from the USGS National Water Information System. 
29 


CHAPTER 2: ARC HYDRO FRAMEWORK 
representing water levels were imported and 
indexed so they relate to Well features. The exam- 
ple below (figure 2.17) shows two time-series 
plots: the red plot represents groundwater levels 
(feet below land surface) at a well in the Edwards 
Aquifer adjacent to Comal Springs in New Braun- 
fels Texas, and the blue plot shows streamflow at 
a gaging station downstream from the springs. 
The plots demonstrate the strong connectivity 
between streamflow and groundwater levels in 
the Edwards Aquifer. During the 1950s drought 
groundwater levels dropped sharply, resulting in 
Comal Springs going dry for a few months. 
Graph of water levels and streamflow References 
Arctur, David, and Michael Zeiler. 2004. Designing Geodata- 
bases: Case Studies in GIS Data Modeling. Redlands, Califor- 
nia: Esri Press. 
Booch, Grady, James Rumbaugh, and Ivar Jacobson. 1999. 
The unified modeling language user guide. Addison-Wesley 
Professional. 
Zeiler, Michael. 1999. Modeling Our World: The Esri Guide to 
Geodatabase Design. Redlands, California: Esri Press. 
paqn>-! pue 
| |) Streamflow 
3 
cos 
8 2 2 
= 3 = E © © 
7) 3 
1950 1951 1952 1953 1954 1955 
Time 1956 1957 1958 1959 @ Groundwater level 
8 
=] (e2es1ns pues mojaq yy) (eA9| 4ayempunosg g G o 
R 
‘akq0ay ‘pieog Juawidojanag sae sexa ‘A2AANS [2D1H0jOayD *S'fQ 4O Asayinod ejeg 
Figure 2.17 The time series of water level and streamflow demonstrate the strong connectivity of surface water and 
groundwater in the Edwards Aquifer. Groundwater levels shown in the plot are from the Texas Water Development Board 
groundwater database, and streamflow are from the USGS NWIS system. 
30 


THE ABILITY TO STORE, VISUALIZE, QUERY, AND ANALYZE 3D PHENOMENA IS A 
well-established field in computer science. In the past decade, much advancement has 
been made in the field of computer-aided visualization as software, hardware, and 
viewing devices have been improved to support better design, science, and entertain- 
ment. This evolution has not bypassed the field of geographic information, and GIS 
now Offers tools for visualizing multidimensional phenomena, including animation of 
3D and time-varying datasets. Three-dimensional GIS is relevant to many industries 
and disciplines. GIS users in fields ranging from petroleum and groundwater to atmo- 
spheric science and oceanography are finding similarities in the way they view and 
store 3D datasets. This chapter starts with a review of 3D GIS for subsurface character- 
ization followed by a description of 3D geodatabase datasets and how these are used 
for subsurface representation. 
3D GIS for subsurface characterization 
Groundwater movement within the subsurface is truly a 3D phenomenon. Water can 
enter the subsurface as diffuse recharge over an outcrop area or as focused recharge 


CHAPTER 3: THREE-DIMENSIONAL ARCGIS FOR SUBSURFACE REPRESENTATION 
from streams and water bodies, then travel 
horizontally within an aquifer unit down to 
an underlying aquifer, or down and then up 
to discharge at a spring or into the ocean. The 
description of groundwater movement within 
the subsurface also requires representations of 
hydrogeologic formations, flow barriers and 
conduits, and the heterogeneity of strata. For 
the geology, mining, and petroleum industries, 
specialized software packages have been devel- 
oped to create sophisticated 3D models of the 
subsurface. This branch of GIS is also known as 
geoscientific information systems (GSIS) or geo- 
modeling systems. These differ from traditional 
GIS in their capabilities to represent complex 3D 
objects using either surface representations or 
volume objects, mainly voxels, which are equiva- 
lent to a 3D raster (Turner 2000). GSIS also has 
the capabilities to rapidly display, edit, and inter- 
polate 3D objects to support subsurface concep- 
tualization. GSIS is based on “geo-objects” which 
are distinctive subsurface features with measur- 
able spatial boundaries in 3D (Fisher 1993). Geo- 
objects describe discrete entities such as a rock 
layer, fault, or a volume element. A combination 
of geo-objects forms a geomodel (figure 3.1) that 
provides an abstract digital representation of a 
part of the earth’s subsurface (Apel 2006). 
Figure 3.1 A geo-model is an 
abstract representation of a part of 
the Earth's subsurface. Geomodels 12 
Geo-object are composed of one or more 
geo-objects that are distinctive 
subsurface features. 
Geomodels defining hydrogeologic units are 
created to understand the movement of groundwa- 
ter within the subsurface. Groundwater software 
applications use geologic maps, borehole stratig- 
raphy, cross-sections, and terrain data to construct 
3D models of the subsurface, and these form the 
32 base for developing numerical flow and transport 
simulation models. An example of such an appli- 
cation is the groundwater modeling system (GMS) 
used to create 3D hydrogeologic models and 
develop groundwater simulation models. Design- 
ing a groundwater data model requires us to 
answer two important questions: How well can 
we represent geo-objects within the geodatabase? 
How can we best use current ArcGIS datasets and 
tools to create, edit, and display 3D geo-objects? To 
answer these questions, we must first understand 
the workflow by which geo-objects are defined; 
how data is collected, stored, and analyzed; and 
what data structures are necessary for creating a 
geomodel representing a groundwater system. 
When conceptualizing a 3D groundwater system 
we usually start by abstracting the subsurface into 
hydrogeologic units. A hydrogeologic unit is a rock 
unit or zone that because of its hydraulic properties 
has a distinct influence on groundwater flow and 
storage. Hydrogeologic units include both aquifer 
units and confining units (also known as aqui- 
tards). These units have horizontal and vertical 
extents and are considered 3D. 
One of the major constraints for establishing an 
accurate representation of the subsurface is the 
lack of field data. While remotely sensed datasets 
are advancing our understanding and ability to 
model the movement of water on the earth’s sur- 
face and in the atmosphere, datasets describing 
the subsurface are relatively scarce. Classification 
of earth strata is based on samples extracted from 
boreholes (such as cores and cuttings), or inferred 
from geophysical logs. The borehole data are 
usually stored as a set of hydrogeologic contacts, 
with each contact representing the top of a hydro- 
geologic unit. The high cost of drilling prohibits 
collection of dense datasets. Thus, estimating the 
extent of hydrogeologic units is usually based 
on upscaling point borehole data to a larger area 
through interpolation procedures. The borehole 
point observations and the interpolated results 


are managed and visualized with a number of 
common data structures including 3D points and 
lines representing borehole contacts and intervals, 
cross-sections and fence diagrams, surfaces, and 
volumes (figure 3.2). 
Hydrostratigraphy along a borehole can be 
described as a set of 3D points that represent 
hydrogeologic contacts or as 3D lines represent- 
ing the hydrogeologic units as intervals along the 
borehole. Cross-sections connecting the borehole 
data are created for display purposes by interpo- 
lating between known data points projected on 
a vertical plane. The cross-section itself can be 
viewed in 2D. By editing the cross-section we can 
add imaginary data points between observations 
along the cross-section’s plane. Fence diagrams are 
collections of cross-sections viewed in 3D. Bore- 
hole data and added points from cross-sections 
(together with terrain data and geologic maps) are 
the basis for creating surfaces representing the top 
and bottom boundaries of hydrogeologic units. 
Borehole stratigraphy 
Sketch and edit 
cross sections 
nina eeeiee ae te od 
jt 
Define hydrogeologic 
units along boreholes Create surfaces from 
borehole data and 
cross sections 
Build volumes 
between ke 
2S. Volume objects representing 
hydrogeologic units “Cut” cross sections 
from the solid model 3D GIS for subsurface characterization 
Using borehole points we can interpolate surfaces 
representing the top and bottom boundaries of 
hydrogeologic units. By repeating this process 
we generate a set of “stacked” surfaces defining 
the vertical extent of hydrogeologic units over a 
defined area. We then use the surfaces to generate 
volume objects that represent the hydrogeologic 
units as individual entities. Volume objects cap- 
ture the “true” (in this sense we regard our con- 
ceptualization of the system as the truth) geometry 
of hydrogeologic units because they describe the 
horizontal and vertical extent of the unit. Addi- 
tional cross-sections can be created by “slicing” 
through volume objects to view the interior of the 
solids along planes of interest. 
The above process highlights the major 
geo-objects necessary for describing a geomodel. 
These include 3D objects for representing points 
and lines along boreholes, cross-sections, surfaces, 
and volumes. The following sections illustrate how 
geodatabase datasets represent such objects. 
Cross sections/fence diagrams 
Figure 3.2 Process of 
creating a 3D description of 
hydrogeologic units. Blue 
text represents the pro- 
cesses and black text shows 
the derived data products. 
Surfaces defining the extent 
of hydrogeologic units 
Create cross sections 
Sar) on the surfaces 
se Cross sections derived from 
the volumes/surfaces 
33 


CHAPTER 3: THREE-DIMENSIONAL ARCGIS FOR SUBSURFACE REPRESENTATION 
Z-enabled features in the 
geodatabase 
Feature classes within the geodatabase can store 
2D and 3D geometries. When creating a new 
feature class, the default is a 2D representation 
of features with longitude (x) and latitude (y) 
coordinates, but we can enable features to store 
coordinates in the vertical (z) dimension and any 
z-enabled feature class can hold 3D geometries 
(figure 3.3). 
Once a feature class is defined as z-enabled, we 
store 3D features in it by assigning vertical coor- 
dinates to the vertices of the geometry. In the geo- 
database, z-enabled features are distinguished by 
adding a “Z” to the geometry name (figure 3.4). 
For example, a Point feature becomes PointZ, a 
Line feature LineZ, and a Polygon feature becomes 
PolygonZ. The multipatch is a unique geometry 
type as it is always z-enabled. 
To create a 3D feature we need to edit the z 
coordinate of each of the feature’s vertices. This 
can be done in a regular edit session within 
New Feature Class 
Type of features stored in this feature class: 
[Pomonfestees 
Lee 
Raa ia ca 
: | [” Coordinates include M values. Lised to stare route data. 
| ¥ Doondinates include Z values. Used to store 30 data! 
Figure 3.3 Z-enabling a feature class enables the storage of 
3D geometries (points, lines, polygons, and multipatches) 
within the geodatabase. When creating a new feature class in 
ArcCatalog, we can select to include Z values, thus enabling 
the storage of vertical coordinates in the geometry. 
34 ArcMap or programmatically using custom tools. 
Take for example the polygon shown in figure 3.5; 
because it is z-enabled, each vertex is defined by 
coordinates in x, y, and z which can be viewed 
and modified in an edit session. This allows us to 
construct a 3D polygon representing an area in 3D 
space. If we view the polygon feature in Arc Map, 
we see it as 2D, but when we load it into ArcScene, 
the feature displays in 3D. A similar approach 
can be used to create 3D points and lines. Keep 
in mind that these 3D features are not truly 3D 
objects, and that 3D operations and calculations 
cannot be performed directly with the z-enabled 
Two-dimensional features 
Point Polyline 
1 oe Location defined by  Vertices (x. y coordinates) Closed line that 
xX y Coordinates connected to forma line defines and area 
Vertices (x, y, and z) Closed line that Location defined 
by x,y. and z form a 3D line defines a 3D area 
coordinates 
Figure 3.4 Features that are z-enabled support the defini- 
tion of a vertical coordinate and enable the representation 
of 3D geometries. 
vertical coordinates 
Edit Sketch Properties 
499177673 2 
499399.924 
4 499332.190  -92,07 498095.640 468989,290 
Figure 3.5 Three-dimensional coordinates of a z-enabled 
polygon feature. Each vertex in the geometry is assigned a 
Z coordinate, and the feature displays in 3D context when 
viewed in ArcScene. 
