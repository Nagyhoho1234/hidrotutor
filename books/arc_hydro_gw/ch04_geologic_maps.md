# Chapter 4: Geologic Maps

features. For example, a z-enabled polygon 
feature does not automatically calculate its 3D 
area, and a z-enabled line feature does not show 
its true 3D length. Rather, the features show the 
2D projected area and length as they are viewed 
in ArcMap. Also, operations such as intersection 
or buffering which are commonly applied on 2D 
features cannot be applied in 3D. Thus, z-enabled 
objects are somewhat limited but still provide a 
data structure to store and display 3D geometries 
within the ArcGIS environment. 
Creating volume (multipatch) objects 
A multipatch geometry is composed of 3D rings 
and triangles and represents objects that occupy a 
3D area or volume. These can be geometric objects 
such as a cube or a sphere, or represent real-world 
objects such as buildings or trees (http: //support. 
esri.com). In the groundwater data model, multi- 
patches represent volume objects usually defined 
as a set of triangular elements defining the surface 
boundary of the volume feature. The interior of 
the volume is not discretized, and the attributes 
of the feature apply to the volume defined by the 
multipatch (similar to the area of a polygon in 2D 
space). Several methods are available for creating 
multipatch geometries. The simplest method is to 
create a 3D multipatch by extruding a 2D polygon 
Base geometry 
Figure 3.6. Multipatch features created by extruding a 
z-enabled base geometry (shown in blue): at left, the base 
geometry is extruded between two constant heights; in 
the middle, the base geometry is extruded upward by 
adding a constant height to its base heights; at right, the 
base geometry is extruded downward. Creating volume (multipatch) objects 
vertically (either up or down). The extrusion 
process takes the area defined by the polygon 
feature and creates a 3D multipatch feature that 
represents a 3D volume (figure 3.6). The extrusion 
process starts with a base geometry that itself can 
be z-enabled and can have a different z value at 
each vertex. The base geometry is then extruded 
either by adding a constant height to the base 
geometry or by extruding the base geometry to a 
defined height. 
Another option for creating multipatch 
features is to extrude a base geometry between 
two surfaces. This method allows us to represent 
a volume of space between two surfaces over a 
given area. For example, we can take two surfaces 
defining the top and bottom of a hydrogeologic 
unit and apply the “Extrude Between” geopro- 
cessing tool (part of the 3D Analyst extension) to 
create a complex multipatch feature representing 
the volume between the two surfaces (figure 3.7). 
By repeating this process over a set of “stacked” 
surfaces representing a sequence of hydrogeo- 
logic units, a set of volumes can be defined, form- 
ing a 3D representation of a hydrogeologic model. 
This method is implemented in the Arc Hydro 
Groundwater tools to create a set of GeoVolumes 
from raster surfaces indexed in a raster catalog 
(see chapter 6 for a more detailed description of 
this process). 
Top TIN 
Extruded 
multipatch 
feature 
Bottom TIN 
Figure 3.7 A volume object (multipatch) created by 
extruding a polygon between two TIN surfaces using the 
Extrude Between geoprocessing tool. 
35 


CHAPTER 3: THREE-DIMENSIONAL ARCGIS FOR SUBSURFACE REPRESENTATION 
More complex 3D volumes can be created 
by developing a surface representation of the 
volume, also known as a polyhedron. A poly- 
hedron is a region of space whose boundary is 
composed of a finite number of flat polygonal 
faces (O’Rourke 1998). Polyhedron surfaces are 
commonly expressed as surface triangulations to 
simplify the data structure and construction of 
the geometry, and many software applications 
use triangulated surfaces to represent 3D volume 
objects. While ArcGIS currently does not include 
algorithms and editing tools to construct complex 
volumes, these objects can still be stored as mul- 
tipatch features and viewed within ArcScene. In 
this manner, volume objects created in specialized 
software applications can be imported into the 
geodatabase and viewed in context with other GIS 
datasets (one of the Arc Hydro Groundwater tools 
can import volumes from XML documents into a 
multipatch feature class). For example, figure 3.8 
shows a text file describing a set of volume objects. 
Each object is described by a set of attributes such 
as its identifier, name, and the number of verti- 
ces and triangles from which it is composed. The 
geometry of the object is constructed as a collection 
of triangles defined by a set of 3D vertices. 
36 Attributes of volume feature 1: 
ID, name, number of vertices, number of triangles 
1, Unit 1, 98, 192 
Vertices: 
xX, y, Z 
846373, 337437, -72 
894815, 324602, -199 
853724, 290001, -98 
846373, 337437, 31 
853724, 290001, 7 
894815, 324602,10 
908756, 280252, -300 | 
continued.. Vertices defined by x, y, 
and z coordinates 
Triangles: 
vertex 1, vertex 2, vertex 3 
Triangles as 
groups of vertices 
continued... 
Attributes of the next volume feature: 
2, Unit 2, 36, 54 
continued... 
J 
Figure 3.8 Text file describing a set of 3D volume objects. 
Each volume contains a set of attributes (e.g., ID and 
Name), and the 3D geometry of the volume is defined by a 
set of triangles composed of 3D vertices. 


Creating volume (multipatch) objects 
ete eS ae RR See —— —_——— — 
This volume object is stored in the geodatabase 
as a multipatch feature constructed by reading 
(programmatically) the text file and building the 
3D geometry. Properties of the volume (ID, Name) 
are stored as attributes of the feature and can be 
accessed through the feature class’s attribute table 
(figure 3.9). 
References 
Apel, M. 2006. From 3D geomodelling systems towards 3D 
geosciences information systems: Data model, query func- 
tionality, and data management. Computers & Geosciences 32: 
PSD Paids), 
£3 Attributes of GeoVolume 
== =i 7 iy 
7 |MultiPatch Fisher, T. R. 1993. Use of 3D Geographic Information Sys- 
tems in Hazardous Waste Site Investigations. Pages xxiii, 
488, [488] of col. plates in Environmental modeling with GIS, 
ed. M. F. Goodchild, B. O. Parks, and L. T. Steyaert, Oxford 
University Press, New York. 
O'Rourke, J. 1998. Computational geometry in C, 2nd edi- 
tion. Cambridge University Press, Cambridge, UK, ; New 
York, New York. 
Turner, A. K. 2000. Geoscientific Modeling: Past, Present, 
and Future in Geographic information systems in petroleum 
exploration and development: AAPG computer applications in 
geology no. 4, ed. T. C. Coburn and J. M. Yarus, American 
Association of Petroleum Geologists, Tulsa, Oklahoma. 
Sent cn ; lmuor 
imported volumes 
Show: [all Selected | Imported volumes 
Options + | Records (1 out of 3 Selected) 
Figure 3.9 A volume object stored in a geodatabase as a multipatch feature. The volume is constructed from a set of 
triangular elements. 
37 


a am 7 me = 5 ' ~ 
7 - } 
a er a a i ke ye 4\ yd eee 
i 
a ‘a a © a — 
~ ; eat i 
- = 
tg ar ae 5 bt Yee ot hey ‘ ay a > 
jj a 
& : ’ 


GeologyPoint 
Point features from geologic maps such as springs, 
caves, sinks, and observation points. 
Representation: Point features. 
GeologyLine 
Line features from geologic maps such as faults, 
contacts, and dikes. 
Representation: Polyline features. 
GeologyArea 
Areal features from geologic maps such as rock units 
and alteration zones. 
Representation: Polygon features. 
TO DEVELOP A HY DROGEOLOGIC MODEL ONE MUST FIRST UNDERSTANDTHE GEOLOGY 
in the area of interest. Geologic maps are the most common data products used to 
describe the geology of a region. Geologic maps are developed on a wide range of 
scales, from continental maps to site scale maps. For groundwater purposes, geologic 
maps provide important information about the geologic formations in the area and the 
locations of geologic features that may serve as water conduits or barriers. Geologic 
maps are complex because they describe the 3D distribution of material within the 
subsurface. For the Arc Hydro Groundwater data model, a simplified set of features is 
used to represent data from geologic maps. These features provide a basic placeholder 
to include spatial data from geologic maps in groundwater projects. 


CHAPTER 4: GEOLOGIC MAPS 
Geologic maps and geologic map 
databases 
Geologic maps are cartographic products 
containing information about the kinds of earth 
materials in a specific geographic area, the 
boundaries that separate them, and the geologic 
structures that have deformed them (Geologic 
Data Subcommittee, Federal Geographic Data 
Committee 2006). These maps represent 3D geo- 
logic features in a 2D mapping environment. To 
do this, the maps usually contain special graphi- 
cal elements such as cross-sections, graphic leg- 
ends, and text blocks explaining the geology of 
the region portrayed. In many cases, geologic 
maps are the basis for mapping groundwater 
features such as aquifer units. In turn, aquifer 
boundaries described in aquifer maps are closely 
related to geologic formations defined in geo- 
logic maps. For example, figure 4.1 shows a gen- 
eralized geologic map and a map of the major 
aquifers of the United States. The maps dem- 
onstrate the close spatial relationships between 
geologic formations and aquifers. 
Standards to support the creation of geologic 
maps have been established for many years by 
different agencies. Guides for creating geologic Scie —— ee ere 
maps were developed soon after the USGS was 
established in 1879 (Geologic Data Subcommit- 
tee, Federal Geographic Data Committee 2006). In 
recent years, the adoption of GIS to collect geologic 
data in the field, archive the data, and produce 
maps has led to the design of standards for rep- 
resenting digital geologic maps. These standards 
define a geologic map database, which is a digi- 
tally compiled collection of spatial (geographically 
referenced) and descriptive geologic information 
about a specific geographic area (Geologic Data 
Subcommittee, Federal Geographic Data Com- 
mittee 2006). One example is the North American 
Geologic Map Data Model (NADM) that aims to 
develop standardized methodologies for the stor- 
age, manipulation, analysis, management, and 
distribution of digital geologic-map information 
(http: //www.nadm-geo.org). Another example is 
the National Geologic Map Database (NGMDB), 
a collaborative effort to create a single national 
standard for the digital cartographic representa- 
tion of geologic map features, primarily involving 
the USGS and the Association of American State 
Geologists (http: //ngmdb.usgs.gov). 
Geologic map databases contain information 
on the geographic location, geometry, and attri- 
butes of geologic features. The fundamental data 
AdAing jed1H0j0ay “sn Jo AsaqinoD 
Figure 4.1 a) Generalized geologic map of the United States, and b) Principal aquifers of the United States. Map units are 
colored to represent different geologic units and aquifers. 
40 


elements of a geologic map database are lines (e.g., 
contacts and faults), points (e.g., bedding attitudes 
and sample locations), and polygons (e.g., map- 
unit areas and zones of alteration). Geologic maps 
are generated based on the objects in the geologic 
map database by symbolizing features and label- 
ing the features with the appropriate attributes 
stored in the database. An example of a generic 
geologic map database implemented within 
KaAains jed16oj0oay °s'f ‘2007 ‘Je 38 Sauley Jo AseyNOD 
0 150 300 Geologic maps and geologic map databases 
ArcGIS is the Arc Geology geodatabase design 
(Raines et al. 2007). This design takes a simplistic 
approach for representing geologic features, cross- 
sections, and legend graphics, using sets of point, 
line, and polygon feature classes with a set of 
common feature attributes. Arc Geology enables 
the production of geologic maps from features 
stored within the geodatabase by simple built-in 
ArcGIS tools (figure 4.2). 
Tertiary Basalt 
Dakota Sandstone 
Benton Shale 
Morrison Formation 
Triassic Hill 
Permian Majuba 
Water 
—— Contact - Certain 
Dike - Certain 
Fault - Certain 
Fault - Approximately located 
Fault - Approximately located, queried 
600 900 Feet 
Thrust fault - Certain 
Monocline - Approximately located 
Line of cross section 
Boundary 
@ Cinder cone 
t Inclined bedding 
| Photo-interpreted bedding 
Figure 4.2 A simple geologic map created with Arc Geology. 
41 


CHAPTER 4: GEOLOGIC MAPS 
State agencies have developed project-specific 
geologic databases to support the production of 
digital geologic maps and convert existing paper 
maps into digital format. For example, the USGS- 
Texas Water Science Center (USGS-TWSC) and 
Texas Water Development Board have digitized 
the Geologic Atlas of Texas (GAT), which was 
developed by the Bureau of Economic Geology at 
the University of Texas at Austin. The atlas was 
= San_Antonio. mdb 
4} Geology250k 
Fault 
€] MemberLine 
MemberPoly 
&3 rel_lut_member_memberline 
@ rel_lut_member_memberpoly 
@ rel_lut_rockunit_rockunit 
8 rel_rockunit_memberline 
&3 rel_rockunit_memberpoly 
RackUnit 
#4 BEG_SanAntonio 
) lut_Member 
(2) lut_RockUnit 
& rel_lutrockunit_lutmember Figure 4.3 Geoda- 
tabase design from 
the Geologic Atlas 
of Texas for storing 
geologic map data. 
A8AINS |eI1HOjOaH “Sf Jo Asayino> eieq 
aia ay Seog ps 7 a cae 
GeologyArea ER GeologyPoint | 
| HydrolD 
HydroCode 
| GeoAbbrev 
| Description 
| HGUID 
4 HGUCode 
| | FType 
GeologyLine 
| HydrolD 
HydroCode 
GeoAbbrev 
| Description 
§) HGUID 
HGUCode 
AaAins |e2160j0a9 ‘sf ‘Z00Z ‘|e 38 SauleYy Jo Asayino> 
HydrolD 
)| HydroCode 
4 GeoAbbrev 
| HGUID 
| HGUCode 
FType f 
42 composed of 38 (1:250,000) hardcopy map sheets, 
which were scanned and digitized to produce a 
digital geologic map of Texas (http://www.tnris. 
state.tx.us). To archive the digital maps in a 
standard form, a GAT geodatabase data model 
was designed (figure 4.3). Other state geologic 
surveys have undertaken similar efforts. 
Geology component 
While it is important to recognize the importance 
of geologic features for groundwater analysis, we 
did not attempt to create a comprehensive geo- 
logic map database in the groundwater data model 
design. Instead, we provided a simple place- 
holder for spatial features that may be included 
in a groundwater project. The geology component 
of the data model includes three feature classes: 
GeologyPoint, GeologyLine, and GeologyArea 
(figure 4.4). These general classes can be linked to 
data from more extensive geologic map databases. 
Figure 4.4 Analysis diagram 
describing the feature classes 
of the geology component. 
The background map from 
(Blome et al. 2005) shows 
point, line, and polygon fea- 
tures within a geologic map. 
