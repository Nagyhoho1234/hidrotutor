# Chapter 9: Implementation

*By Steven Grise and Gil Strassberg*

PREVIOUS CHAPTERS DISCUSSED THE CONTENTS OF THE ARC HYDRO GROUNDWATER data model and provided a number of examples. This chapter is designed to help you implement your own groundwater project and efficiently tailor the data model to fit your specific needs. Remember that the data model and associated materials are a starting point for your project rather than a final solution. Online resources for further information include http://support.esri.com/ and http://webhelp.esri.com. The first step in this process is to download a design template, available at the Esri Web site 
(http: //resources.arcgis.com/ArcHydro) and at the Arc Hydro Groundwater Web site (www. archydrogw.com). 
Implementation process ti 
Getting started on your groundwater project is straightforward. At a basic level, the process involves creating and refining a geodatabase and then documenting and deploying the design. For most projects, this simple approach is adequate. Toward the end of the chapter we also introduce some additional patterns and methods that should help you deal with more complex project requirements. You can use the following checklist as a guide for outlining tasks to be completed for your project. 

Checklist 
Status 
1. Create an Arc Hydro Groundwater geodatabase 
2. Refine data model content 
3. Set spatial reference 
4. Load data 
5. Index features and build relationships, networks, and topologies 
6. Set up tools and applications 
7. Document 
8. Deploy 
Creating an Arc Hydro Groundwater geodatabase from a template 
To create an Arc Hydro Groundwater geodatabase, you can use a template stored as an XML work- space document that contains the model. The XML document contains a complete description of a geodatabase (in this case an Arc Hydro Groundwa- ter geodatabase) that can be imported to an exist- ing geodatabase. This process will add the feature classes, tables, relationships, and domains defined in the XML document (figure 9.1). A detailed description on creating a new Arc Hydro Ground- water geodatabase is available on the Arc Hydro 
Groundwater Web site (www. archydrogw. com). 
Catalog Tree tS} re | MyProject, mdb 
+ SQ) Borehole 
&® ©} Framework 
+ GY Geology 
GB GeoRasters 
© ©) Hydrostratigraphy 
@Y RasterSeries [Figure 9.1] Example of an Arc Hydro Ground- water geodatabase created by import- + GP Simulation i) SS} Temporal ing the data model 
+ QP xs20 
 AttributeSeries 
@) BoreholeLog 
@ DatasetCatalog 
D HydrogeolagicUnit 
@ SeriesCatalog 
) TimeSeries 
HD VariableDefinition 
@ xXs20_catalog datasets from an XML document. 
Customizing the data model 
Your starting point for design is to review the template data model. Refining it for your own project involves adding (or removing) feature data- sets, feature classes, fields, coded values, topolo- gies, and any other necessary modifications. Most people spend time reviewing existing datasets in the original data model and making improvements so the new model better supports their specific data needs. Understanding what you need for a particu- lar project typically involves reviewing existing datasets and talking with subject-matter experts and end users. You can use the conceptual ground- water data model for discussion purposes, and it’s a good practice to make notes on a paper or digi- tal copy of the model as you talk with your project team and users. Eventually, one person typically uses ArcGIS to make the model changes, and the number of changes is typically quite small (at least compared to the length of the discussions about changes!). It’s relatively easy to get carried away in a complex series of meetings, and sometimes there is a tendency to overanalyze the design challenges. 
Thus, you can consider a few simple guidelines: 
1. You, as the person leading this part of the project, need to own the design process and the design of the system. With that focus, you will likely learn a lot more by working with the data, maps, and tools required for your project than by talking to people. 
2. Typically, the biggest gaps are in understanding how technology can be applied to solve long- standing problems. Take the opportunity to innovate during the design phase, because it gets harder to make changes once a new system is built. Prototype your ideas and refine the design based on practical problems that need to be solved. The ArcGIS Desktop Help system has a series of steps outlined in a section called 

“Designing a geodatabase” that should help you in the process (http: //webhelp.esri.com). 
3. You should leverage the experience in your 
4. organization; somebody has probably thought about this problem a lot more than you have. 
You shouldn’t pretend to be that person if you aren't, and you need to work closely with people who have the domain experience and expertise. 
People will always tell you about the need for more data—information they don’t have today that they believe is necessary for the organi- zation. Be cautious about these requests. If it is really important to your business, the data already should be available. Otherwise, addi- tional data acquisition and maintenance costs might be involved. 
Catalog Tree 
= & myProject.mdb 
+ GP Borehole 
2 QP Simulation 
# GQ} Temporal we GP xS20 
@) xs20_Catalog © G) Framework : — General | XY Coordinate System | Tolerance | Resolution i Domain a orHawe Fields | Indexes | Subtypes | Relationships | Representations 
~ ceased Click any field to see its properties. 
UD OatasetCataog | [eS i i | Alias scription ogeologicUnit SS se ee | a Allow NULL values |YeS: =e ee | | wo Estas! [p[Defeut Value | | ‘Domain 
(@) VariableDefinition | [Length ae 50 
To odd anew field type the name into an empty row in the Field Name column, click in the Data Type column to choose the data type, then edit the Field Properties. Implementation process 
5.It’s relatively easy to build a data model that your organization has no hope of managing on a day-to-day basis. Try to start with a simple implementable design with additional wish- list items that can be added after the initial implementation. 
Using ArcCatalog to refine geodatabase contents 
Like most Windows applications, you can use the “Properties...” context menu in ArcCatalog to modify the groundwater data model for your proj- ect. In the following example (figure 9.2), the proper- ties of the Aquifer feature class are being inspected. 
In the Fields tab, a new text field called “Description” is added to the Aquifer feature class. This will allow users to add a detailed text description of the aquifer. 
Figure 9.2. You can use ArcCatalog to customize the groundwater data model. 
You can also customize the data model by adding lists of coded values specific for your  []GERRaMGyais project/organization. In the first Arc Hydro data General Domains model, FIype fields were defined with coded Pl etoeetan le a ee value domains. These were intended for mapping / - “rear ena aa classification of different kinds of water features, so that we could distinguish between rivers and | Tonatge oases veucooremse i F : | |\DataType domain for MENS SUI table | canals for mapping and analytic purposes. His- e class torically, this was rooted in USGS hydrographic \Indicates what type of time-enabled dataset is refer | 
Domain Properties: 
mapping. Many other organizations around the Field Type —— ie Se 
1 7 Mf i of Ud 7 a DomainType (Coded Values world involved in “blue-line mapping” had simi eae eee lar practices. In the first Arc Hydro data model we Merge potoy | [Defaut Value didn’t provide any examples, but the USGS and other organizations developed fairly sophisticated implementations that in our experience were eos beyond what most project teams required. In the ]Monitoring Monitoring 
Arc Hydro Groundwater data model we included some sample domains for FType, and we kept the ee pattern quite simple. When you create the data model from the template XML document, a few of the feature classes (e.g., Well, Aquifer) willhave [Figure 9.3] ArcCatalog interface for editing, adding, or coded values associated with the FType fields. deleting coded value domains. The upper section shows 
These examples should form a good starting point — the domains available in the geodatabase, and the lower for you to manage the types of features in your section shows the coded values defined for the selected project, but it is likely you will need to edit the — domain. 
list or even add multiple attributes to achieve the results you are looking for. 
Coded value domains are defined on the geodatabase level, which means that the same list of codes can be applied to multiple attributes in different feature classes and tables. You can modify coded value domains with Arc Catalog. 
When you select a domain name, the codes of the domain are shown in the bottom part of the inter- face. You can then modify, delete, or add values to the list. The following example (figure 9.3) shows a WellFType coded value domain created to define a set of unique values that can be entered in the 
FType field of the Well feature class. 
After creating the coded value domain, we associate the FType field in the Well feature class with the WellFType Domain (figure 9.4). You can create as many domains as necessary for your proj- ect and assign those to fields within the geodatabase. 
When a coded value domain is related to an attribute, the values in that attribute are limited to the coded values defined in the domain. For exam- ple, when you edit the FType field in ArcMap, values will be restricted to the set of coded values 
Feature Class Properties 
Tolerance | Resolution | Domain | 
Representations Relsionsos | 
Fie) FE Se i ee lick in the Data Type column to choose the data type, then edit the Field Properties. 
[Figure 9.4] Coded value domain is assigned to the FType field in the Well feature class. 
2 Attributes of Well 
49 /Poirt 49 | 5857204 — 245 | pm eg ae wr a aw ; case ff So —— rc Implementation process defined in the WellFType domain. In an edit session, a drop-down menu appears when you try to edit the FType values, and you must select one of the predefined coded values (figure 9.5). 
You can also consider using design tools available on the ArcGIS resources center (http: // resources.arcgis.com), suchas GDB XRay (search for “GDB XRay”), ArcGIS Diagrammer (search for 
“Diagrammer”), and CASE tools based on Unified 
Modeling Language (search for “Building geodatabases with CASE tools”). These tools can help to automate some of your design tasks, but for most projects it’s easier to get started using ArcCatalog. 
Set a spatial reference for datasets 
An important part of the design process is the definition of spatial references that will be used in your project. The definition can be based on exist- ing data available in your organization or based on planned datasets for which you will need to determine the appropriate spatial reference. It is important to get the spatial reference assigned cor- rectly before loading data. While it is sometimes possible to change the spatial reference after load- ing the data, you should avoid this because it can cause errors while attempting to load data and result in shifts in geometry that may introduce inaccuracies in your data. 
The spatial reference should be set at the feature dataset level when feature classes are con- tained within a feature dataset. This will set the 
[Figure 9.5] A list of 
4 Stock coded values appears when editing an attri- bute with a coded value domain. 
Records (1 out of 3613 SelectelUnused we properties for all feature classes in the feature dataset. If feature classes are outside a feature ® Batch Aid| s8 Seer Denon ee eee Saii= EN) 
dataset, then you will need to specify each dataset ff} input Feature Class or Dataset separately. You can select a predefined spatial ref- | | ce erence, modify it, or specify a new one. If you have C;\MyProject.mdb\Borehole existing data, you can choose to import the spatial | C:\MyProject.mdb\Framework we , C:\MyProject.mdb\Geology reference from the existing data. [Figure 9.6] shows } =| C:\MyProject.mdb\Hydrostratigraphy 
; F } C:\MyProject.mdb\ Simulation an example of selecting the State Plane spatial ff | c:\myproject.mdb\Temporal reference from a list of spatial references that are Ce\MyProject mab\xS2D supplied with ArcGIS. 
In addition, for feature datasets containing 3D le eres features (e.g., Borehole, Hydrostratigraphy, and | C:\MyProject.mdb | 
Output Coordinate System (optional) 
Simulation), it is important to define the z coor- }}__[1ab_1983_Texas_Centric_Mapping_System_ Albers [es] dinate system as well as the x and y coordinate ff _ Template dataset (optional) - us| | system. Additional information on managing spa- ‘ : Transformation (optional : ae ‘ tial references can be found in the ArcGIS Desktop | help system (http://webhelp.esri.com). Youcan ff i) 
also use the Batch Project geoprocessing tool to Ok | Cancel | Environments. | Show Help >> | batch project multiple datasets (figure 9.7). 
The contents of the template data model are [Figure 9.7] The Batch Project geoprocessing tool can be organized into different feature datasets in the used to project the feature datasets of the groundwater geodatabase. Each component, such as framework — data model to a selected coordinate system. 
Browse for Coordinate System 
)NAD 1983 StatePlane Pennsylvania South FIPS 3 
{E)NAD 1983 StatePlane Puerto Rico Virgin Islands 
(@)NaD 1983 StatePlane Rhode Island FIPS 3800.p 
{GSNAD 1983 StatePlane South Carolina FIPS 3900, 
‘NAD 1983 StatePlane South Dakota North FIPS 4 [Figure 9.6] ArcGIS provides 
General XY Coordinate System | Z Coordinate System | Tolerance | Resolution | Domain | 
Name: | NAD_1983_StatePlane_Texas_Central_FIPS_4203 a list of spatial references to select from, and these can be customized as necessary. 
KesNAD 1993 StatePlane Texas Central FIPS 4203,p 
(®@)NAD 1983 StatePlane Texas North Central FIPS is 
NAD 1983 StatePlane Texas Central FIPS 42 
Geographic Coordinate System: GCS_North_American_1983 
Angular Unit; Degree (0.017453292519943299) = 
Prime Meridian: Greenwich (0,000000000000000000) 
Datum: D_North_American_1983 
Spheroid: GRS_1980 v Show of type: [Coordinate Systems 
Select a predefined coordinate system, 
Import a coordinate system and Xj, Z and M domains from an existing geodataset (e.g., feature dataset, feature class, raster), 
Create a new coordinate system, 
Edit the properties of the currently selected coordinate system, YT Set the coordinate system to Unknown, 
Save the coordinate system to a file. 
or hydrostratigraphy, has its own feature dataset. 
This logical grouping easily can be changed if necessary, but you should be aware that all feature classes in a feature dataset must have the same spatial refer- ence. Also, Esri recommends that all feature classes in the same feature dataset have the same permis- sions for editing and data management/access. If you have one workgroup editing the framework data and another workgroup managing the simula- tion datasets, you should plan the organization of the data according to editing privileges. 
Loading data 
This step involves using ArcCatalog data loading tools and possibly the ArcGIS Data Interoperability extension for more sophisticated data-loading tasks. 
Again, the ArcGIS Desktop Help system includes significant content to support data-loading tasks. 
Catalog Tree 
25, aan area & QR simula natch Biddresses. i ioodtn ute Dasma Hil 
Figure 9.8. Loading data using ArcCatalog. Implementation process 
The simplest way to load data is to use the basic tools in ArcCatalog (figure 9.8). 
There are also a number of geoprocessing and model-builder options for automating the data- loading process. You can use the Append geopro- cessing tool to copy features and append them to your target feature classes (figure 9.9). The tool also allows you to match fields from your source datasets and the target feature classes. 
The ArcGIS Data Interoperability extension is another useful toolset for loading data into the geodatabase. It provides a visual user interface for mapping source and target datasets. It also pro- vides sophisticated extract, transform, and load 
(ETL) tools for data loading. The extension enables 
: C:\arcHydroGroundwater|major _aquifers_dd.shp 
Target Dataset 
| C:\arcHydroGroundwater\Project1 .gdb\Framework\Aquifer oe i 
Schema T: ‘optional : £ Z 
Do a eS ~ Field Map (optional) 
HydrolID (Long) 
HydroCode (Text) 
f=]: Name (Text) 
C:\arcHydroGroundwater\majar_aquifers_dd.shp.AQ_NAME (Text) 
HGUID (Long) 
FType (Text) 
SHAPE_Length (Double) 
SHAPE _Area (Double) 
Description (Text) 
[Figure 9.9] The Append geoprocessing tool can be used to load data from your source datasets to the target feature classes. 
you to build loading workflows to automate repetitive loading tasks. [Figure 9.10] shows an example of an ETL tool for loading well data from a text file. The tool automates the process of creat- ing new Well features from the x and y coordinates and matching the fields in the source data with the fields in the target Well feature class. Again, the 
ArcGIS Desktop Help system provides documentation and examples that can help you efficiently load data into your data model. 
Add geodatabase datasets such as networks and topologies 
The groundwater data model does not require specific topologies, networks, annotation, or other datasets. You may choose, however, to add addi- tional datasets to your project data model. For example, surface water networks can be created from the WaterLine and WaterBody feature classes. 
Another option is to add spatial topologies to define how spatial features interact. For example, you can define a topology rule that forces Well fea- 
I fe lubbock_well_ data [CSV] 
(4-5) Groundwater [GEODATABASE_FILE] ie Source CSV File(s}: D:\SG\Projects\Groundwater be | ie Destination Geodatabase; D:\SG\Projects\Groundu. 
“Du ‘QIeEMIOS ayes Jo AsayinoD tures to be inside an Aquifer feature (figure 9.11). 
Thus, this rule will be enforced when adding wells to your Well feature class. 
New Topology 
[Figure 9.11] 
Example of a topology rule between 
Aquifer and 
Well feature classes. 
[Figure 9.10] Example of using ETL tools in the Data Interoperability Extension. The process shown from left to right: 
importing a text file, filtering by the aquifer code to get data for a specific aquifer, creating 2D points based on the x and y coordinates, and loading the points into the Well feature class. 
Set up tools and applications 
Install any tools and applications you plan to use and test with your data model. This will typically include basic editing and productivity tools and can also include more sophisticated modeling and simulation tools (e.g., the Arc 
Hydro Groundwater tools). It is also important at this stage to create some of the output prod- ucts required for your project. If you’ve done a thorough job, you won’t have any surprises here, but data models always require minor changes when you try to produce outputs for the first time. Make sure you do this before documenting and deploying the system. 
porteridbee 
Ce a o w 
AaAins je2160j0e5 °s*Q pue ‘pieog uatudojanag Ja1eM Sexo) 
"Duy ‘EUaWY YUON sey ajay Jo Asaqinoa /eyeg uoNebIAeN eAowony GNY © elep dew Eagle Pass 
\gidson Road | Crystal 
Lity eee ee | 
Carrizo 
Springs al cio Mae \ Uppera 5 
Cove Killeen  Belton,— Temple sas Hae - 
S ce y, Implementation process 
Configure maps and services 
While setting up your application environment, you can access Web services. Developing a plan for these services should be part of your implementa- tion project, whether you need to access observa- tions and measurements from partner systems or whether you simply need a base map in your Web- mapping applications. A simple example of using base-map services with your groundwater data is posted on the Arc Hydro Resource Center at http://resources.arcgis.com/ArcHydro. Exam- ples on that site will guide you through setting up a dynamic map service and consuming online map services (figure 9.12). 
Rye aya) 
. Gameron e 
Huntsville ye ‘ne gh q| oF ee } 
3 4 
< a s f 7 Giddings Le Brenkam- 4 hs oy 
Henipistead : 
ree ¥ A eo { MIDDLE GUADALUPE} \yookum Wharton “io 
Ei Campo = 
7 6. Swen 3 
_ Cahunrbia 
Beeville 
[Figure 9.12] Example of a dynamic map service displaying wells, aquifers, streams, and monitoring points stored in an 
Arc Hydro Groundwater geodatabase on top of a topographic base map published as a Web service by Esri. 
You also have the ability to publish your own map and data services for other users to consume 
(figure 9.13). The example above demonstrates publishing ArcGIS Server map services, but other 
Publish to ArcGIS Server ; 
Choose the capabilities you would like to enable: [Figure 9.13] You 
| 2] Mapping (always enabled) can provide different capabilities for 
| LC) mobile Data Access aie 
Cceodata Access applications/users consuming your 
Web services. 
Catalog Tree 
=) (@ Database Connections 
+} @§) Database Servers 
+) Ga} GIS Servers 
=) 488 Interoperability Connections 
4 Add Interoperability Connection 
#44 Connection (1) - WES. fdl i) 2H Connection (2) - WES. fdl fa Scalar References 
#4 Search Results 
(8% Toolboxes 
[Figure 9.14] In ArcCatalog you can create interoperability connections to many types of services and consume them in ArcGlS Desktop. 
E; Editing ‘Well’ 
Identificaton Data Quality 
Detailed Descrintion | Overview Descrintion| 
Entity Type Attribute | 
General | Dates | Attribute Domain Values | 
Type: a 
Width: 
136 options to publish KML, Web Feature Services 
(WES), and Geodata services from ArcGIS Server are also available. 
You have different options to consume Web services, including ArcGIS applications and sev- eral Web mapping APIs. One example of using 
Web services is the consumption of Web Feature 
Service, which involves creating a data interoperability connection using ArcGIS Desktop 
(figure 9.14). Once a connection has been created, you can access the Web services using ArcMap like you would use other local datasets. While the performance of these services is not as fast as cached and dynamic map services, the one advan- tage of WFS in ArcMap is that you can work with these map layers as vector datasets and perform a number of operations like select, copy, paste, export, and other more advanced tasks. 
Document the data model 
You can document your data model several ways. 
The most basic way is to populate the metadata for each of the datasets in your geodatabase. You can use ArcCatalog to create standard metadata, which includes a description of the datasets, the fields in each dataset, and information on the spatial ref- erence and extent of the data (figure 9.15). Some 
[Figure 9.15] You can use ArcCatalog to create metadata describing the datas- ets within your geodatabase. 

of the information is automatically populated for you, but you must add additional information to complete the documentation. 
To document a more general view of your data model, you can use the version of the conceptual data model you developed with your project team. 
This approach works well for making a poster and documenting your design in a simple graphical 
~ Untitled* = ArcGIS Diagrammer Implementation process way. You can find several tools to generate documentation at http://resources.arcgis.com. 
ArcGIS Diagrammer is a popular application for managing the design of your geodatabase using an XML Workspace document like ArcHydro- 
Groundwater.xml. The application also allows you to create visual diagrams that are good for documenting and sharing your design (figure 9.16). 
j=l Fields % OBJECTID 
@ SHAPE 
% HydroD 
% LandElev 
®@ AquiferID 
@ AqCode 
% HGUID ® RydroCode | 
@ WellDepth |- 
Untitled tinal) Borehole 
§- (Framework 
-{&) Geology 
© Hycrostratigraphy 
{@ Simulation 
&#1{ Temporal t- xS2D 
AttributeSeries uses 
[Figure 9.16] ArcGIS Diagrammer provides a graphical interface for editing and documenting your data model. In this example the properties of the Well feature class are inspected. 
GDB XRay is another application that provides the ability to generate simple vector graphics 
(SVG) and data dictionary reports (figure 9.17). 
Many of the diagrams in this book were created with GDB XRay then further refined using 
Microsoft Visio. 
Deploy to users 
The best way to deploy the system to your users depends on the size of your user base. In many smaller projects, you are deploying to yourself and a few colleagues, so the challenges of testing, train- ing, and deployment are minor. Larger workgroups and enterprise implementations require careful planning and testing to ensure that the system works correctly in a production environment. You 
Unique feature identifier in the Geodatabase 
Permanent public identifier of the feature 
Land surface elevation or reference elevation 
Depth of feature 
HydrolD of related Aquifer 
Tet description for the aquifer related to the well 
Identifier of the hydrogeologic unit 
Well - FeatureClass A point that represents the location of a well and associated attributes 
Classification of the F eature Type for mapping and analytic purposes can deploy these types of systems using many different organizational and IT practices. Most project teams vary in the way they test and deploy solutions to end users. In general, you should use functional and performance testing as necessary to prove that the system will work before deployment. 
As the number of users and applications increase, you will need to do more testing and validation of your solution. You should also develop training and technical support plans that suit the scale of your deployment. A suitable change management plan for the system should also be in place prior to going live with the system. 
Design patterns and tradeoffs 
In previous chapters you have seen solutions to anumber of design challenges. 
Each of these solutions took some time to develop, and there are always tradeoffs in any solution. The next section describes some of the key design patterns in more detail to help you understand some of the thinking that went into the data model. 
Name Well 
ShapeType Point 
FeatureType Simple 
AliasName Wels 
HasM false [Figure 9.17] Examples of graphics and data 
HasZ false dictionary reports created usi Description A point that represents the location of a well and associated attributes oe oereat gees ee SNE 
DataTheme ArcHydroFramework 
Field DataType Length AliasName Description Domain DefaultValue IsNullable 
HydroID Unique feature true identifier in the 
Geodatabase 
HydroCode Permanent public true identifier of the feature 
LandElev Land surface elevation true or reference elevation 
WellDepth Depth of feature [true 
AquiferID HydrolD of related true 
Aquifer 
AqCode Text description for “rue the aquifer related to the well 
HGUID Identifier of the true hydrogeologic unit i 
FType Classification of the | WellFType true 
Feature Type for mapping and analytic purposes 

Representing wells and boreholes 
We took a simple approach in representing wells and boreholes in the data model. Wells are point fea- tures, and they can be associated with BoreholeLog data from which 3D spatial features (BoreLines and 
BorePoints) can be created. It is also possible to consider wells as 3D line features and to set them up to have measures and z-values in their geometry. This would permit changing the BoreLine and BorePoint classes to tables and using ArcGIS Linear Referenc- ing to display the borehole data along the path of the well. This alternate approach appears to be more suited for petroleum and other drilling activi- ties (where most of the wells are not vertical) than for groundwater data, but you can consider this alternative, especially-if your data are focused on displaying 3D information along nonvertical wells. 
One-to-many versus many-to-many associations 
The template data model includes a number of one-to-many (1:M) associations, such as the rela- tionship between Aquifer and Well features and the relationship between Cell2D and Node2D features. With different implementation strategies 
Well features class 
Co | wt [rn [rn 3 [oP Screen table and Well features. Design patterns and tradeoffs these relationships can be substituted with many- to-many (M:N) relationships. For example, a well can be screened across multiple aquifers or can be associated with different aquifers depend- ing on the scale of the project. To support such associations one can develop an M:N relation- ship between wells and aquifers. The following example (figure 9.18) shows a conceptual M:N relationship between Well and Aquifer features. 
An intermediate table (named Screen) is created to support the M:N association. In this example, two wells are highlighted: Well 1 and Well 2. Each of the wells has a HydroID and is related with two Aquifer features. For each well, two instances are created in the intermediate table, the WellID attribute in the intermediate table references the 
HydroID of the Well feature and the AquiferID references the HydroID of an Aquifer feature. 
Through the intermediate table we associate Well 1 with Aquifer 1 and Aquifer 2, and Well 2 is related with Aquifer 2 and Aquifer 3. One can also query in the opposite direction. For example, if we start from Aquifer 2 and query the intermediate table, we will see that we have two wells (Well 1 and 
Well 2) related to this aquifer. Thus, a many-tomany relationship is established because a well 
[Figure 9.18] Example of a many-to-many (M:N) relationship between Aquifer 
Aquifer feature class 
HydrolD | HydroCode FType 
“Aquifer? Unconfined | 
‘Aquifer3- - Unconti ined can be related to multiple aquifers, and an aquifer can be related to multiple wells. 
While it is possible to implement M:N associations, experience shows that managing data in M:N associations is more difficult from a user perspective. For this reason, we implemented a 1:M association in the template model. You should consider implementing a M:N relationship if necessary in your project. Another approach is to create additional relationships between Well and Aquifer features (see chapter 5 for a more detailed description of this approach). 
Beyond the template— additional design methods 
The template data model is not always well suited for your needs. For example, you might need addi- tional content that does not exist in the Arc Hydro 
Groundwater template data model, or your data needs may be quite different from what the model provides. In general, the approach to tackling these types of challenges is similar to the process we went through while developing the ground- water data model. For a more complex project you can use some of the same techniques to add con- tent for your needs. This involves a combination of database and GIS design methods: 
° Start with the template conceptual data model. 
¢ Work with subject-matter experts and your project team to identify data needs and refine the conceptual model. 
¢ Look at your information products: maps, tools, 
Web services, and other requirements to determine the information needs of your users. 
Refine the conceptual data model to support the creation of maps, layers, Web services, and other content. 
140 e Test and refine with real data. Get feedback early—people may not be able to provide much help on design details, but they will provide feed- back when you show them data, maps, and tools. 
¢ Build logical and physical models to support the design. Work as a single team with people who are building the applications and infrastructure for the project. 
¢ Document and deploy.
