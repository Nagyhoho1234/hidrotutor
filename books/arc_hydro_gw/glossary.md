# Afterword

IN THIS BOOK WE PROVIDED A DESCRIPTION OF THE ARC HYDRO GROUNDWATER data model, including the design concepts, data structures, and the common uses one may find for the data model. The chapters of the book describe the different components of the data model and include an implementation section in each chapter to help you get started with applying the data model to your own projects. We hope that the book serves as a starting point for getting acquainted with the data model so that you can leverage the presented knowledge in your own projects. 
Remember that the Arc Hydro data model, introduced in 2002 with the publication of Arc Hydro: GIS for Water Resources, is not a fixed design. Like water, the data model is continuously adapting to a fast-changing technological environment. The Arc Hydro 
Groundwater data model is a natural outgrowth of that earlier work. By the time you read this book, the evolving field of GIS will have introduced new technologies, providing new opportunities for us to improve the way we integrate GIS and water resources. Emerging fields of GIS will greatly affect the way we use the technology for hydrologic analysis. 
These include: 1) the development of time-aware spatial datasets, 2) the improvement of 3D datasets and tools, 3) the emergence of ArcGIS Online and the adoption of Web services by many agencies to serve spatial and temporal data over the Web, and 4) the evolution of GeoDesign to enable wider communities to quickly visualize and test their designs within a geographic context. These new technologies, and others we cannot fore- see, will greatly impact the Arc Hydro data model and its tools and how they are used in your projects. 

This book does not stand on its own; it is part of a wider set of resources that include papers, pre- sentations, case studies, tools, and Web sites with updated designs. We encourage you to visit these 
Web sites and even provide your own content: 
¢ A community-based Wiki where you can add your own content about the groundwater data model: www. archydrogw.com. 
¢ The Arc Hydro Resource Center Web pages: 
http://resources.arcgis.com/archydro 
Equally important to the geodatabase design presented in this book are tools that support the implementation of the data model. As mentioned in the book, Esri and Aquaveo have developed a set of tools named Arc Hydro Groundwater Tools to support the implementation of the groundwater data model: http://www. aquaveo.com/archydro. 
From its initial conceptualization, Arc Hydro has tried to serve as a bridge between two the first dealing with water resources and hydrology and the second deal- ing with GIS. We hope water resource engineers, hydrologists; hydrogeologists, geographers, and 
GIS specialists will all find this book a valuable addition to their respective fields. We believe edu- cators will also find Arc Hydro Groundwater: GIS for 
Hydrogeology a valuable academic resource. Since its publication, Arc Hydro: GIS for Water Resources has been used as a textbook, not only for teaching 
GIS concepts but scientific concepts as well. The ability to show hydrologic concepts within a map is a strong learning method, as students can visu- alize hydrologic theory at a real location and time and with a true geographic context. We anticipate that educators will adopt Arc Hydro Groundwater as a textbook for college and postgraduate classes dealing with GIS and hydrogeology. communities: 
As you find new ways to apply the groundwater data model and the concepts contained in this book, we invite you to share your insights with other community members to help advance the use of GIS within the field of water resources and hydrogeology.

---

# Glossary

**APUNIQUEID** Table for tracking HydroID values. Each time a new HydrolID is assigned to a feature in the geodatabase, a counter is updated so that the same HydroID is never assigned again within the given geodatabase. 
aquifer Group of formations, a single geologic formation, or part of a formation that contains sufficient saturated permeable material to yield significant quantities of water to springs and wells. 
Aquifer (feature class) Polygon feature class for representing data from aquifer maps. 
Each Aquifer feature in the feature class represents the areal extent of an aquifer or a region within an aquifer. 
aquifer map Common data product that portrays the boundary of aquifers over a given region and can also distinguish between zones within an aquifer. 
Arc Hydro The overall data model for representing hydrology, including surface water and groundwater. Within this book we refer to this general model as the Arc Hydro data model, or simply as Arc Hydro. 
Arc Hydro Framework Data model for representing the basic surface water and groundwater features. Within this book we refer to the framework data model as the Arc 
Hydro Framework, or simply as the framework. 

Arc Hydro Groundwater The groundwater components of the Arc Hydro data model, which is the focus of Arc Hydro Groundwater: GIS for 
Hydrogeology. The book often refers to this data model simply as the groundwater data model. 
Arc Hydro Groundwater Tools ArcGIS tools, for groundwater analysis, designed on top of the 
Arc Hydro Groundwater data model. The tools are developed collaboratively by Aquaveo and 
Esri and are available on the Aquaveo Web site 
(www. aquaveo.com/archydro). 
Arc Hydro Tools ArcGIS tools, for surface water analysis, designed on top of the Arc Hydro data model. The tools are developed by Esri and available on the Arc Hydro Resource Center (www. 
arcgis.com/archydro). 
AttributeSeries Table for archiving time-series data where multiple variables are indexed with the same feature and time. 
borehole A hole drilled into the subsurface. 
BoreholeLog Table for representing vertical data along boreholes. The table is the basis for creating 3D features to represent vertical borehole data as 3D geometries. 
BorePoint and BoreLine 3D (z-enabled) point and line feature classes that represent point and interval data along boreholes. 
Boundary (feature class) Polygon feature class that represents the 2D extent and orientation of a simulation model. 
Cell2D Polygon feature class that represents cells or elements associated with a 2D simulation model or a single layer of a 3D model. 
Cell3D Multipatch feature class that represents 
3D cells and elements of a simulation model. 
Celllndex Table containing indexes of MOD- 
FLOW ceils and nodes used for joining tables and features in the MODFLOW data model. 
data model Framework for describing a subject and storing data about it. Data models help us describe systems using structured sets of data objects. 
DatasetCatalog Table for indexing time-series datasets within a geodatabase. DatasetCatalog is typically associated with RasterSeries or Feature- 
Series in the geodatabase. 
feature A row ina feature class representing a spatial object, including its geometry and attri- butes. 
feature class A collection of features with the same geometry type, attributes, and relationships. 
A feature class is a table in the geodatabase that contains a custom field (Shape) for defining the geometry of features (point, line, polygon, mullti- point, and multipatch). 
feature dataset Container for a collection of spatially related feature classes together with relationship, topology, and network classes. The feature dataset is used for grouping feature classes either by spatial reference (all features classes in a feature dataset share the same spatial reference) or thematically. 

FeatureSeries Collections of features indexed by time representing a series of geometries vary- ing in location or shape. Each feature in a feature series exists for only a period of time. Features in a feature series can be grouped to form a “track” representing the change (in geometry, location, or both) of a particular feature over time. 
GeoArea Polygon feature class representing the 
2D extent of hydrogeologic units. 
geodatabase Repository of geographic information organized into geographic datasets within a relational database system. It provides a common data storage and management frame- work for storing datasets supported in ArcGIS. 
geographic data model Data model for representing the real world (or part of it) expressed with spatial datasets within a GIS. 
geologic map Cartographic product containing information about the kinds of earth materials in a specific geographic area, the boundaries that separate them, and the geologic structures that have deformed them. 
geologic map database Digitally compiled collection of spatial (geographically referenced) and descriptive geologic information about a specific geographic area. 
GeologyPoint, GeologyLine, and 
GeologyArea Feature classes for representing data from geologic maps. 
geomodel A combination of geo-objects that provides an abstract digital representation of a part of the earth’s subsurface. 
geo-object Distinctive subsurface features with measurable spatial boundaries in 3D. Geo-objects describe discrete entities such as a rock layer, fault, or a volume element. 
GeoRasters Raster catalog for storing and indexing raster datasets that describe properties of hydrogeologic units. 
GeoSection Multipatch feature class representing 3D panels for constructing vertical cross sections. Each feature in the GeoSection feature class represents a slice of a hydrogeologic unit, and a set of GeoSection features represent a complete cross section across multiple units. 
GeoVolume Multipatch feature class for representing hydrogeologic units as 3D volume objects. 
groundwater simulation model Simplified mathematical representations of aquifer systems used to interpret the flow of water and transport of contaminants within an aquifer and to predict how these will change under future stresses. 
GSIS Geoscientific Information Systems, also known as geomodeling systems. These informa- tion systems differ from traditional GIS in their capabilities to represent complex 3D objects using either surface representations or volume objects. 
HGUID Hydrogeologic unit identifier. Index used to associate features with descriptions of hydrogeologic units defined in the Hydrogeologi- cUnit table. 
HorizonID Index defining the vertical arrangement of hydrogeologic units in a depositional sequence. HorizonID values are assigned from bottom to top such that the smallest HorizonID is given to the base unit (the first layer in a depo- sition sequence), and the largest is given to the top unit. 
hydro feature Feature classes customized as part of the Arc Hydro data model by adding 
HydroID and HydroCode attributes to them. 
HydroCode Text attribute that is a permanent public identifier of a feature. The HydroCode provides a linkage with external information systems. 
hydrogeologic framework A geologic framework that defines a distinct hydrologic system. In a hydrogeologic framework, subsurface materials are classified not only by the rock properties but also by the hydraulic properties that effect water storage and flow. 
hydrogeologic unit Any soil or rock unit or zone which by virtue of its hydraulic properties has a distinct influence on the storage or move- ment of groundwater. 
HydrogeologicUnit Tabular representation of hydrogeologic units. Attributes associated with hydrogeologic units are defined in the table, and spatial features created to describe the spatial location and extent of the units are related back to the conceptual definition in the table. 
HydrolID An integer attribute that uniquely identifies objects in an Arc Hydro geodatabase. 
The HydroID differs from the ObjectID, as it is unique across the geodatabase and not only within a certain class (table, feature class, raster catalog). 
146 interface data model A geodatabase design for storing the entire contents of a given simulation model. 
LAYERKEYTABLE Table used to manage multiple identifiers, so that data from different sources or for different projects or separate areas can be attributed with separate sets of unique identifiers. 
MODFLOW Modular finite-difference flow model developed by the USGS. The most widely used groundwater simulation model. 
MODFLOW Analyst A suite of ArcGIS tools developed as part of the Arc Hydro Groundwater tools. MODFLOW Analyst is used for build- ing and managing MODFLOW models via the 
Arc Hydro Groundwater and MODFLOW data models. 
MODFLOW data model (MDM) An interface data model developed as an extension to the 
Arc Hydro Groundwater data model. The MDM contains a series of tables and relationships and supports the storage of an entire MODFLOW simulation within a geodatabase. 
MonitoringPoint Point feature class for representing locations where water is measured. 
multipatch Geometry composed of 3D rings and triangles that represents objects that occupy a 3D area or volume. These can be geometric objects such as a cube or a sphere, or represent real-world objects such as buildings or trees. In the groundwater data model, multipatches repre- sent 3D features such as GeoVolume, GeoSection, and Cell3D features. 
Node2D Point feature class that represents the computational nodes in a 2D simulation model or a single layer of a 3D model. 

Node3D Z-enabled point feature class for representing the computational nodes of a 3D simulation model grid. 
piezometric head map Map describing the spatial patterns of groundwater levels (or pressure) 
in aquifers. 
raster catalog Container for storing, indexing, and attributing raster datasets. 
raster dataset. Represents imaged, sampled, or interpolated data on a uniform rectangular grid. 
RasterSeries Raster catalog for storing collections of raster datasets indexed by time. Raster series are useful for describing the dynamics of spatially continuous phenomena, like the varia- tions in groundwater levels or the distribution of rainfall over time. 
relationship Data structure that defines the association between objects in two classes using common attribute values in key fields. 
SectionLine Polyline feature class for representing 2D cross-section lines on a map. 
SeriesCatalog Table for indexing and summarizing time series stored in the TimeSeries table. 
stratigraphic units Rocks or bodies of strata recognized as a unit for description, mapping, or correlation purposes. 
Subsurface Analyst A suite of ArcGIS tools developed as part of the Arc Hydro Groundwa- ter tools. Subsurface Analyst is used for creating, editing, and managing 2D and 3D hydrogeologic data within ArcGIS. 
table A dataset for storing data values as an array of rows and columns. 
time series A sequence {v, t} that describes the values, v, of a variable indexed against time, t. The value of t is called the time stamp, which records an instant of time used to reference the value, v. 
TimeSeries Table for storing single-variable time-series data. The table implements a 3D structure for storing time-series values indexed by location, time, and variable. Each row in the 
TimeSeries table represents a value of a particular variable at a particular time associated-with a particular feature. 
TsTime Attribute representing the time stamp specifying the date and time associated with a time-series value. 
TsValue Attribute containing a numerical value of a variable at a given location and time. 
UTCOffset Attribute representing the number of hours the time coordinate system used to define 
TsTime is displaced from Coordinated Universal 
Time. 
VariableDefinition Table for defining temporal variables. Each variable defined in the Vari- ableDefinition table is uniquely indexed with a 
HydrolID, and space-time datasets are related to the variable definition by referencing the 
HydrolD of the variable defined in the table. 
VarID Attribute containing a numerical identifier of a variable. Matches to the HydroID of a vari- able defined in the VariableDefinition table. 
VarKey Unique text identifier for a variable, used when a variable is indexed in an attribute series table via field names. 
Waterbody (feature class) Polygon feature class for representing areal water features in the water system, such as lakes, ponds, swamps, and estuaries. 
WaterLine Line feature class for representing hydrographic “blue lines,” which represent mapped streams and water body center lines. 
WaterPoint Point feature class for representing hydrographic features such as springs, water withdrawal/discharge locations, and structures. 
Watershed (feature class) Polygon feature class for representing drainage areas contributing flow from the land surface to the water system. 
Web service Internet-based program built to provide a particular set of functionality or services. 
well Human-made excavation or structure created in the ground to access groundwater for water extraction, injection, or monitoring. 
Well (feature class) Point feature class for representing well locations and basic well attributes for identification, 3D representation, and linkages to aquifer and hydrogeologic units. 
XS2D Prefix of feature classes and tables in the groundwater data model used for representing 
2D cross sections. 
XS2D_BoreLine Polyline feature class for representing vertical borehole data projected on a vertical plane along a section line. 
XS2D_Catalog Table for managing XS2D feature classes and their association with Section- 
Line features. Each row in this table provides the name and role of a XS2D feature class and infor- mation about its associated SectionLine feature. 
X$2D_MajorGrid and XS2D_MinorGrid 
Polyline feature classes representing grid lines showing the vertical and horizontal dimensions in a 2D cross section. 
XS2D_Panel Polygon feature class for representing hydrogeologic units as 2D cross- section “panels.” Usually a cross section will be formed by a set of XS2D_Panel features, each representing a hydrogeologic unit along a section line. 
XS2D_PanelDivider Polyline feature class representing vertical lines on a cross-section plane showing the location where a section line changes direction (i.e., the location of vertices of the section line). Panel dividers are used as guides for orientation when viewing the 2D cross section.
