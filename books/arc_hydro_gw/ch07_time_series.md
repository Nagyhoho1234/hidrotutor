# Chapter 7: Time Series for Hydrologic Systems

*By Timothy L. Whiteaker, David R. Maidment, and Gil Strassberg*

TimeSeries 
Tabular description of single-variable time series, such as stream discharge and groundwater levels, where each value is recorded at a certain location in space at a given time. 
Representation: Tabular date related with spatial features. 
AttributeSeries 
Tabular description of multi-variable time series, such as chemical concentrations in a water sample, where multiple variables are recorded at the same location and time. 
Representation: Tabular date related with spatial features. 
RasterSeries 
Catalog for storing collection of raster datasets indexed by time. 
Representation: Raster catalog. 
Feature series 
Collection of features indexed by time that represent a time-varying geometry 
(e.g. particle track, inundation polygon) varying in shape and location. 
Representation: Point, line, polygon, and multipatch features indexed by time. 
MUCH OF OUR UNDERSTANDING OF HYDROLOGIC SYSTEMS AND HOW WATER moves and changes in composition while it travels through them is based on mea- surements of water quantities and properties (e.g., flow, pressure, temperature, and concentrations) determined by measurements taken at monitoring points such as wells, gages, and sampling points along rivers. Some of the data, such as daily precipita- tion, daily discharge, and water levels, are collected continuously through time at fixed locations, and measurements are taken at regular intervals (e.g., every minute, hour, 

or day). Other data, such as water quality, are measured irregularly in time and space and might be sampled several times a year or once every couple of years. Atmospheric processes such as precipita- tion and evaporation play roles in the distribution of water, and these processes are often described by temporal values defined over a spatial grid. 
This chapter provides a new design for dealing with temporal data within the Arc Hydro data model. The design provides better support for using multiple representations of time-series data and an improved schema for describing time-series vari- ables. The chapter includes examples showing how to integrate temporal groundwater information within ArcGIS and also provides a more general description of implementation strategies that are useful for supporting datasets where time, location, and a set of variables are involved. 
Suppose we have a geographic region, S, in which we wish to define information over a time horizon, T, for a variable, V. For groundwater, we can use the piezometric head as a simple example, measuring the water levels in an aquifer at wells and then interpolating them to form a grid or contour map representing the piezometric head in the aquifer. Because water levels do not gener- ally vary rapidly through time, it is common when constructing piezometric head maps to choose a period of months or years, average the water levels in each well over that period, and then construct the piezometric head map by interpolating the time-averaged values. If this process is repeated for several time periods, subtracting earlier piezo- metric head maps from the later ones gives a mea- sure of the change in groundwater levels within the aquifer over time. 
In the example just described it is implicit that there are two types of temporal informa- tion involved: time series of water-level observa- tions in wells and space-time datasets formed by interpreting those observations in space and time. 
These two concepts (time series and space-time 
88 datasets) are the cornerstones of the temporal data model presented in this chapter. 
Time series 
A time series is a sequence {v, t} that describes the values, v, of a variable indexed against time, t. The value of t is called the time stamp, which records an instant of time used to reference the value, v. 
For measuring a water level, the time stamp is the point in time at which the measurement is made. 
A series may be regular, that is, the time stamps 
(t,t, t, =. €) tor successive values in the series are separated by a fixed time interval; or the series may be irregular, in which case there is no fixed time interval between successive values. Regular series may be produced from irregular ones—sup- pose the water levels measured at a well are averaged through the year for each year, y, of mea- surements. Then the sequence of averaged water levels indexed against the years (y,, Y» Vy ---Y,) 
is a regular time series whose values are assumed to apply over the whole of the interval they rep- resent. In a relational database, such as the ones used by ArcGIS, it is assumed that the time stamp for a regular time series occurs at the beginning of the time interval; for an annual time series that is midnight on the first day of the first month of each year in the series. A similar assumption is made for data averaged over any other time interval, such as daily or monthly data. A time series can thus be classified as an instantaneous series if the values in the series apply only at their time stamps or as an interval series if the values apply over the interval between one time stamp and the next. 

Time-series data sources 
Fortunately, many time-series datasets are now available online. Local, state, and federal agency 
Web sites are often a good place to look for timeseries data, while universities and research labs provide alternative places for more project-specific datasets. These datasets were traditionally accessed by navigating Web pages, but more and more insti- tutions are turning to Web services as a means of automating and standardizing data access. 
Archives of groundwater data such as the U.S. 
Geological Survey (USGS) National Water Information System (NWIS) or the Texas Water Development Board Groundwater Database include 
Kanins jer1Hojoay ‘sn 4o AsayinoD 
-e AG ca Ca hes Ss awe Explanation - Percentile classes (symbol color bs i ae Est Set Gr? as SS ar T 
4 Bh a Be ee 1 Low ee Below) Below |  tonmal lormal — Normal Friday. November 20, 2009 
| 76-90 | 
| Above | Much Above| High 
|__Normal i = Time-series data sources time series that describe changes in groundwater properties over time. The most common datasets are measurements of water levels and water quality taken at wells. These data can be measured continu- ously at fixed locations with measurements taken at regular intervals or measured irregularly in space and time. For example, figure 7.1 shows a map of the USGS Climate Response Network, which is a national network of about 140 wells used to moni- tor the effects of droughts and climate variability on groundwater levels (http: //groundwaterwatch. 
usgs.gov). The regularly measured water levels are summarized into statistics such as mean daily, monthly, or annual water levels, and these can be downloaded for selected wells. 
[Figure 7.1] The USGS 
Climate Response Network provides summary statistics of water levels showing water levels across the United States. 
Data are symbolized by their percentile classes so that the warmer colors indicate water levels below normal, and the cooler colors indicate water levels above normal. 
| Normal 
[Figure 7.2] shows an example of a file of daily water levels downloaded from the USGS archive. 
The data appear as a set of columns identifying the agency providing the data (typically “USGS”), the unique USGS site number (e.g., “295443097554201” for a well in Texas), the date and time (date/time), variable values, and data qualifiers. The type of data that a variable represents is described by a code (e.g., 01_72019_00003 = Mean depth to water level, feet below land surface), which is used as the column heading for the values. Data qualifiers provide record-level metadata that indicate, for example, if a data value has been approved for publication (qualifier code = “A”). 
The [time, value] pair is unique for each record, and a collection of [time, value] pairs of the same type at the same location form a time series, which can be visualized or used in hydrologic analysis and modeling. The most basic operation with time series is to visualize it in a graph that describes how a certain variable changes over time at a spe- cific location or zone. To understand where these changes are occurring in space, we need to associ- ate the time series with a spatial feature. For exam- 
© NWIS_WL_data.txt - Notepad 
File Edit Format View Help 
# Data provided for site 295443097554201 # DD parameter statistic Description 
01 72019 00003 Depth to water level, 
Data-value qualification codes included in this output: 
e Value has been estimated. 
01_72019_00003 
Ae datetime 
14s 14s 
2000-02-01 
2000-02-02 
2000-02-03 
2000-02-04 
2000-02-05 
2000-02-06 
2000-02-07 
2000-02-08 
2000-02-09 
2000-02-10 
2000-02-11 
2000-02-12 
2000-02-13 
2000-02-14 
2000-02-15 
2000-02-16 
2000-02-17 
2000-02-18 
2000-02-19 
2000-02-20 
2000-02-21 site_no agency_cd 
5s 15s 16s 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 
295443097554201 Aaning je21boj0ay *s"p Jo Asayinod eyeg bP 
PRP PPPPPP PPP PP rPyYPyP 
A Approved for publication -- Processing and review completed. 
01_72019_00003_cd ple, if we take the time series of water levels just described, we can plot the change in water level over time, and we know where these water-level changes are occurring by mapping the location of the well at which the measurements are taken. In this example, we can get the latitude and longitude coordinates for well number 295443097554201 and create a map showing the well location and the associated water-level measurements (figure 7.3). 
In addition to Web pages, time-series data can also be published via Web services. A Web service is an Internet-based program built to provide a particular set of functionality or services. Whereas 
Web pages are accessed with Web browsers and meant to be viewed with human eyes, Web ser- vices are accessed using programming code, whose end result typically is not displayed as a 
Web page. A very simple example of a Web service is a function that gives you the latest quote for a stock when you provide its ticker symbol. An example of a standardized Web service for time- series data is WaterOneFlow, which was devel- oped by the CUAHSI Hydrologic Information 
System (HIS) project (http://his.cuahsi.org). 
[Figure 7.2] Example of a file containing feet below land surface (Mean) 
mean daily water levels downloaded from the 
USGS National Water 
Information System. 
Data values are indexed by site, date/time, and a code defining the vari- able measured. 

WaterOneFlow uses a simple interface to ask for data: basically, you make one of the four following requests to retrieve data from WaterOneFlow: 
° GetSites—Returns a list of observation sites (e.g., wells, stream gages) available in the Web service. 
¢ GetSiteInfo—Returns detailed information about a particular site, such as a list of all time-series variables measured at the site and the period of record of data. 
¢ GetVariableInfo—Returns information about a time-series variable, such as its units of measure. 
~ 
AdAANG |Pd160j0aH *s'- Jo Asayinod eieq Time-series data sources 
¢ GetValues— Returns a time series of values for a given site, variable, and date range. 
No matter whether the data source is the EPA, 
USGS, or a university, the same four basic Web service requests are made to access data, making it intuitive for a user to access data from sev- eral different sources (a list of publicly avail- able WaterOneFlow Web services can be found at http://hiscentral.cuahsi.org). Additionally, 
WaterOneFlow Web services always return data in a standardized format called WaterML. The strict rules about naming conventions and data orga- nization in WaterML make it easy for a data user to interpret what is returned in a given WaterML 
[Figure 7.3] Water levels recorded at a monitoring well located north of San Marcos Springs in Texas. The x axis of the plot represents the time domain and the y axis shows the water level values. The well is part of the USGS NWIS real-time monitoring network. 
file. Tools designed to consume the WaterML formatted Web services, such as the CUAHSI HIS 
HydroGET tool (http: //his.cuahsi.org/hydroget 
. html) make it easy to retrieve time-series data from 
WaterOneFlow Web services and store the results in an Arc Hydro geodatabase. In addition, custom applications can be developed to consume Web services. An example of such an application is the 
NWIS Time Series Analyst developed at Utah State 
University. This Web-based application provides users with plotting and export functionality for data at any USGS monitoring station in the United 
States. Such applications, built upon Web services streamline data gathering and exploration, as they enable you to use online services instead of having to download data and use local applications for data formatting and analysis. With the adoption of Web services by more organizations, Web-based applications will be able to stream up-to-date datasets from multiple organizations through a single interface. [Figure 7.4] shows an example of a plot created with NWIS Time Series Analyst. To create the plot you do not need to download data from the NWIS Web site. Instead, you simply spec- ify the type of data you want to plot and the station number. The Time Series Analyst retrieves the data from the NWIS Web services and displays the plot and related statistics. 
Another standard for data publication is Web 
Feature Service, or WES. WFS is a standard way of serving vector data, defined by the Open Geo- spatial Consortium (http://www. opengeospatial 
.org/standards/wfs). ArcGIS Server has the capability to publish geodatabase feature classes and tables as WFS. Therefore, data providers using 
Arc Hydro to store time-series data can publish the temporal component online as WFS. A data user can then use ArcMap to access the tables and 
Fille Graph Data Help 
Time Series | Probability | Histogram | Box Vhisker | 
LR-67-01-809 (Tipps) 
Depth to wetter level, feet below land surface 
1990 1995 2000 
Date Summary | Plat Options | aes eeee [Figure 7.4] A plot of water 
Statistics ci levels created using the [24.44] 
2424) 
_28.97| 
14.57 ot 
2.937 Geometric Mean NWIS Time Series Analyst, a 
Maximum 
Web-services based applica- Minimum 
Standard Deviation tion. The x axis shows the 
Coefficient of Variation time dimension and the y axis eee ent) 
10% shows water level values. 
25% 
Median, 50% | 
75% 
90% | 
# of Observations 
# Censored | 
— Enter Data Selection Parameters = aoa = : fr one FS Se Comat | 
NWIS Database: | Ground Water Level Data ¥| | | | 
Station: LR-67-01 -809 (Tipps) ae | | Start ete SS —— 1) lowow \ Plot Graph | Search |[295443097564201 | || geo _| | | See 5 | End Date: 
| Variable: Depth to water level, feet below land surface || lo2z12010 | | Clear Graph } | 
| (Search }|72019 | i aoe | | oie Sot a ae eres Iie as ee =| 
UtahState weary @USG | Created by: UNIVERSITY Dae Peres By: aU. Ss i This is a PROVISIONAL application that is under development. Please send any questions or comments to Jeff Horsburgh. 
| This application uses web services developed by the CUAHSI Hydrologic Information System Project. For more details, see http: /wwvw.cuahsi.org. science for a changing work! 
AUSIOAIUA 2323S YeIP) Ie A1oyeOGe7 Yoivasay J9xe/\\ YeIN ay) Je payeald sem yshjPuy Salas SWI] SIMN SUL 
0 N 

feature classes from the WFS so that the data appear as if they were stored in a local geodata- base on the user’s computer. 
By incorporating time-series data into an Arc 
Hydro geodatabase, we are creating a spatial-temporal information system that represents spatial features such as wells, streams, monitoring stations, and springs, and also stores time-varying infor- mation recorded at these locations. Archiving one time series of [time, value] pairs may only require a simple data structure, but in reality we might be dealing with many sets of time series, some of which can be recorded simultaneously at the same location. Moreover, for any hydrologic analysis, we will probably need to create different space- time datasets to represent the spatial and temporal distribution of hydrologic variables over time. 
Space-time datasets 
Time-varying data can be archived and visualized with various data structures depending on the type of data collected and the information contained in the data. Arc Hydro includes four types of space- time datasets designed to support archiving and visualizing hydrologic time series within ArcGIS: 
e Time series—A single variable recorded at a location, such as stream discharge or groundwater levels. 
e Attribute series—Multiple variables recorded simultaneously at the same location, such as chemical analysis of a water sample. 
e Raster series—Raster datasets of a spatially continuous phenomenon indexed by time. The rasters describe how variables change spatially and temporally, such as the change in water levels in an aquifer, or the variation of precipitation measured by NEXRAD. Space-time datasets e Feature series—-A collection of features indexed by time. Each feature in a feature series class represents a variable at a given location and time period, e.g., point features representing the movement of particles through the subsurface or polygons representing the change in inundated areas over time. 
[Figure 7.5] shows an analysis diagram describing the datasets included in the temporal component of Arc Hydro. The component includes the four types of space-time datasets, with additional tables for defining variables and creating summaries of time-series data. 
Time-series variables 
A key concept in the design of the temporal component of Arc Hydro is the definition of vari- ables in a central table, to which different space- time datasets can be related. VariableDefinition is a table for defining temporal variables. Each variable defined in the VariableDefinition table is uniquely indexed with a HydroID, and space-time datasets are related to the variable definition by referencing the HydroID of the variable defined in the table (figure 7.6). 
AMEREEP Ry 8 
| HydrolD |_| Feature!D 
_ VarKey aie / VarlD 
' | VarName | TsTime 
| | VarDesc __ UTCOffset 
"| VarUnits _TsValue 
| Medium 
| DataType 
| IsRegular 
_ | TimeStep 
| TimeUnits 
| NoDataVal 
__ Vocabulary 
_ | VarCode 
] RasterSeries ) = AttributeSeries | ; | FeaturelD 
| TsTime 
' | UTCOffset 
| Varkey 1 
‘ | VarKey 2 
The following example (figure 7.7) shows a populated VariableDefinition table. Each variable in the table is indexed with a unique HydrolID. 
The VarName, VarDesc, and VarUnits attributes describe the properties of the variable (for simplic- ity, not all attributes of the VariableDefinition are shown). Notice that the water-quality variables 
(silica, calctum, magnesium, etc.) are indexed with a VarKey. This allows us to represent these vari- ables as attribute series, where fields in the Attri- buteSeries table are named based on the VarKey values in the VariableDefiniton table (see the section below on attribute series). 
Single-variable time series 
In a single-variable time series each value describes one variable recorded at a certain loca- tion in space at a given time. This type of data can 
== SeriesCatalog — 
TTS [Figure 7.5] Analysis diagram 
FeatClass 
VariD 
TsTable showing the datasets in the temporal component of Arc Hydro. 
/ StartTime 
EndTime 
ValueCount 
DatasetCatalog 
VarlID 
DsType 
DsSource 
TsTable 
StartTime 
EndTime 
UTCOffset 
Group!ID 

be depicted as a 3D space-time data cube, where the three coordinates are space, indexed by loca- tion L; time indexed by T; and the variable being measured indexed by V. The data value, D, can be written as D(L,T,V) to symbolize its dependence on these coordinate axes (figure 7.8). 
= VariableDefinition 
Table for defining temporal variables 
‘Fieldname _ Description 
HydrolD Unique numerical identifier for the row within the gecdseare: 
Matches VarlD in related tables. 
VarKey Unique text ID for a variable, used when a variable is indexed in an attribute series table via field names. 
VarName The name of the variable. 
VarDesc The description of the variable. 
Vocabulary Name of the list of variables in which a particular VarCode is defined (e.g., USGS NWIS). 
VarCode Public identifier for a variable (e.g., "00060" for discharge in 
USGS NWIS). 
Medium Medium in which the variable is observed or occurs (e.g., 
"Groundwater"). 
VarUnits Units of measure for the variable. 
DataType Describes whether the time series contains instantaneous measurements, cumulative values, etc. 
IsRegular Integer field that stores 1 (TRUE) if the time series values are regularly spaced in time, or 0 (FALSE) if the time series is irregular. 
TimeStep For regular time series, the number of TimeUnits between each occurrence of a time series value. 
TimeUnits For regular time series, the time unit used to describe the length of time between occurrences of a time series value. 
NoDataVal Numerical value used to indicate a "No Data Value" (e.g., a missing value) in the time series table. 
[Figure 7.6] VariableDefinition table for defining temporal variables. 
[Figure 7.7] An example of a VariableDefinition table defining a set of time-series variables. Single-variable time series 
To describe time-series data values in a tabular structure, Arc Hydro defines the attributes index- ing the time series. FeatureID represents the spatial feature or location (L), TsTime represents the time 
(T), and VarID represents the variable measured 
(V). Thus, any time-series value, TsValue, can be represented by a point in 3D space with its corre- sponding FeatureID, TsTime, and VarID (figure 7.9). 
Time 
[Figure 7.8] 
A time-series value represented in a data cube. The value (D) is indexed by location 
(L), Time (T), and the variable (V). 
FeaturelD arlD 
[Figure 7.9] The Arc Hydro structure for describing timeseries data values (TsValue). The data are indexed by the location (FeaturelD), the time (TsTime), and the variable 
(VarlD). 
| Attributes of VariableDefinition — 
Silica concentration as SiO2 a oe Records (0 out of 10 Selected} Bag os = —_ | 
For data originating from different timecoordinate systems (e.g., different time zones), the UTCOffset field is attached to the TsTime field to provide an unambiguous representation of the date/time. UTCOffset is the number of hours that the TsTime is offset from Coordinated 
Universal Time (which is equivalent to Greenwich Mean Time). For example, in the wintertime, the Central Time Zone in the United States is six hours behind Greenwich Mean Time. So for a groundwater level value measured in Austin, 
Texas, at 1 p.m. local time on January 23, 2007, the 
TsTime is “1/23/07 1:00 PM,” and the UTCOffset is “-6.0.” From the viewpoint of local hydrology alone this concern with local time versus univer- sal time may seem irrelevant because most local 
EE TimeSeries 
Table for storing singlevariable time series 
Description sn ge ae fa Field name 
Unique feature identifier. Is equal to the HydrolD of the feature associated with the time series value. FeaturelD 
VariD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
TsTime Time stamp specifying the date and time associated with the time series value. 
UTCOffset Number of hours the time coordinate system used to define 
TsTime is displaced from Coordinated Universal Time. 
TsValue Numerical value of the variable at the given location and time. 
[Figure 7.10] TimeSeries table for representing single-variable time series. 
#3 Selected Attributes of VariableDefinition 7 Ee) [ [| Hyaroio | varkey [ vartiame | Varbesc | 
< < ae) > 
Record: 1 «| 1 >|] Show: All felectec | 
[Figure 7.11] Example of time series stored in the TimeSeries table. Time-series records are indexed with a VarlD that points to the HydrolD of a variable defined in the Vari- ableDefinition table. 
96 hydrology studies operate using the local timecoordinate system, whatever that may be, including the switch between standard time and daylight saving time. However, the treatment of universal time is relevant, even for local hydrology studies when hydrologists employ weather data such as 
NEXRAD radar rainfall or outputs from weather and climate models. The weather data and fore- casting systems are global in extent. To avoid confusion among countries, many weather data products are presented in universal time coor- dinates. In order to use these data products and correctly synchronize them with local hydrologic data, the offset between local and universal time has to be understood and factored into the time- series database development. 
TimeSeries is a table for storing single-variable, time-series data. The table implements the 3D structure for storing time-series values indexed by location, time, and variable. This structure is simple, yet general enough for archiving a wide array of time series. Multiple sets of time series can easily be stored using this data structure, and queries can be made on the data to extract cer- tain variables at specific locations over a defined time interval. Each row in the TimeSeries table represents a value of a particular variable at a par- ticular time associated with a particular feature 
(figure 7.10). 
The TimeSeries table data structure supports the storage of many single-variable time series in 
£3 Selected Attributes of TimeSeries (= \fel(x) 
[| Featurew | vario [ Tstime | uTCoffset| TsValue| « 
~ 

Single-variable time series the same table, indexed by VarID. Each row ina “[FeatureID] = 2791.” The view created by such a 
TimeSeries table has a VarID, which matches the 
HydroID of a row in the VariableDefinition table that describes the time-series variable. In the fol- lowing example, shown in figure 7.11, measure- ments of daily stream flow downloaded from the USGS NWIS Web site for gages in the Gua- dalupe River basin (VarID = 6874), and ground- water level measurements from the Texas Water 
Development Board (VarID = 6875) are stored together in one TimeSeries table. The TimeSeries records are attributed with a VarID that associ- ates the records with a variable defined in the 
VariableDefinition table. 
Suppose we want to select ali the time-series data measured at state well 6823302 (the same well shown in chapter 2) near Comal Springs, 
Texas. The HydroID of this well is 2791, thus any time-series data related to this well will be indexed with the HydroID of the Well feature. To extract time-series data related to this well, we perform a query on the TimeSeries table stating query contains all the time-series data recorded at this well. This data view is represented as a vertical plane in the 3D time-series cube, perpen- dicular to the FeatureID axis, and can include multiple variables (e.g., water levels, water qual- ity) measured at many TsTimes. A different query can be applied to extract all data values of a spe- cific variable; for example, water levels. Suppose the HydroID for the water-level variable in our geodatabase is 6875. To execute our query we create a query stating “[VarID] = 6875” in the 
TimeSeries table. This view represents a vertical plane perpendicular to the VarID axis. Combining these two queries together, “[FeatureID] 
= 2791 AND [VarID] = 6875,” creates a view of time series for a single variable at a single fea- ture, represented by the vertical line in the time- series cube formed by the intersection of the two vertical planes described above. [Figure 7.12] shows the different views created by querying the TimeSeries table. 
FeaturelD 
[Figure 7.12] Time-series views created by queries on the TimeSeries table: (a) view of time series for a given feature 
(indexed by the same FeaturelD), (b) view of time series of a certain variable (VarlD), and (c) view of time series at a certain location and a given variable. 
The dataset created from such a query has fixed 
FeatureID and VarID attributes and can have multiple TsTime values. The result is a single-variable time series that represents the change in water levels (VarID 6875) at the specified well (FeatureID 
2791), as shown in figure 7.13. 
By performing this kind of query, you can discover the various time series you have in your 
TimeSeries table. However, often it is useful to see a list of all available time series at a glance. For this purpose, the temporal component includes the SeriesCatalog table. SeriesCatalog is a table for indexing and summarizing time series stored in the TimeSeries table. By creating the SeriesCata- log, you can quickly identify time series of interest and then perform a query on the TimeSeries table to select the time-series values for analysis. This becomes especially useful with datasets contain- ing a large number of time-series records because the time for processing queries may be significant. 
Having the summary SeriesCatalog prepopulated 
Select by Attributes 
Enter a WHERE clause to select records in the table window. 
Method : [Create anew selection a iy | 
[FeaturelD] 
[ValD] 
[TsTime] 
(UTCOffset] eee! 
Get Unique Values | Go To: | + 
SELECT “FROM TimeSeries WHERE: 
[FeaturelD] = 2791 AND [VarlD] = 6875 
| Clear | Verify Help Load... Y Se coe 
98 ( )() £8 Selected Attributes of TimeSeries _ inne eo a helps to quickly identify and extract datasets of interest (for specific variables, time periods, and features). [Figure 7.14] shows the attributes of the 
SeriesCatalog table. 
EB SeriesCatalog = (onnees ananoeg 1826 
Table for indexing and eee summarizing time series stored in the TimeSeries table 
Fieldname Description 
FeaturelD Unique feature identifier. ls equal to the HydrolD of the feature associated with the time series summarized in the catalog. 
FeatClass Name of the feature class to which the related feature belongs. 
VarlD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
TsTable Table containing the time series records. 
StartTime The start date/time value of the series. 
EndTime The end date/time value of the series. 
ValueCount Number of time-series values in the series. 
[Figure 7.14] SeriesCatalog table for summarizing singlevariable time series stored in the TimeSeries table. 
TTC a cae 
: Nir “i a an ie £5.¢ A 
Show: All | Selected Records w 
[Figure 7.13] An example query on the TimeSeries table that necro 7 of creates a view of a single-variable time series at a specific feature. 

The following example (figure 7.15) shows a populated SeriesCatalog table. The highlighted series in the catalog is indexed with a FeatureID of 2791 and a FeatClass value of “Well,” meaning that the values recorded in this series are related to a Well feature with HydroID = 2791. The VarID value of 6875 relates to the water-level vari- able defined in the VariableDefinition table. The 
ValueCount attribute indicates that 1167 water level values were recorded at this well, between 
November 15, 1948, and August 27, 2003. 
Customizations can be made to the SeriesCatalog table if desired. For example, a GroupName attribute could be added as a means of grouping individual time series into categories such as “groundwater” or “surface water.” Sometimes, a given time series applies to more than one geospatial feature. For example, data measured at a rainfall gage could be applied to a watershed and also a county. In this case, a HydrolID field is added to the SeriesCatalog to uniquely identify each series. The HydrolD of the series can be used in a separate table that pairs Serie- sIDs and FeatureIDs. This table essentially creates a a 
2798\well =—Sséd|=«éB7 dd Ee ee cee Es 
2799 | Well aa 
~ 2800 Well eSeries 51211 HD hr a ~~ 0 ee = Single-variable time series many-to-many association between time series and features, such that a series can be associated with multiple features, and a feature can be associated with multiple series. Within the SeriesCatalog table, the FeatureID is still used, storing the HydrolD of the feature where the time series was actually measured, e.g., the rainfall gage. 
Until this point we have demonstrated the management of single-variable time series and the ability to query a certain variable at a given loca- tion over a specified time. Other common tasks performed with GIS are mapping time series for a given time across multiple features and the anima- tion of variables over space and time. In the space- time cube, the combination of a horizontal slice for a particular TsTime and a particular VarID results in a view containing all data of a certain type (e.g., groundwater levels) recorded at the specified time. 
This data includes measurements at multiple features. It is common to create maps represent- ing the spatial distribution of the variable at the specified time. Examples are the creation of maps that show the spatial distribution of groundwater 
[Figure 7.15] An example of a populated SeriesCatalog table showing summaries of time series. 
1936 (421961 is 
37996 | 
Records (1 out of 2040 levels and water quality within an aquifer. The following query (figure 7.16) on the time- series table retrieves all the groundwater levels measured in January 1991. 
The result is a view of measurements taken at wells within the Edwards Aquifer for the time period specified. By joining the queried time series with Well features, we can create a map of water levels within the aquifer for the selected date. Using the animation tools built within 
ArcGIS, we can animate a set of maps showing the spatial-temporal variations in water levels within the Edwards Aquifer. The water-level maps in figure 7.17 were created by querying the Time- 
Series table for a specific variable and date, and the results were joined with the Well feature class. 
The examples above demonstrate a conceptual process by which time-series data are visualized. 
Time series are related to features that locate them in space, and by using the relationship between features and time series, we can plot time series for particular features or create maps showing 
Select by Attributes 
Enter a WHERE clause to select records in the table window’. 
Method : [Create anew selection x] 
{OBJECTID] : 
{Feature!D] 
[VarlD] 
[Ts Time] 
{UTCOffset] 
[Ts Value] 
[Vari] = 6875 AND Yeari[TsTime}) = 1999 AND Monthi[TsTime]) = 1 load. Save... | 
100 the spatial distribution of a variable at a given time. The TimeSeries table allows easy storage of time-series data within a simple table structure. 
Because the TimeSeries table has only one value attribute (TsValue), it is most useful for storing single-variable time series where one variable is recorded for any location at a specific time. Some datasets are not suitable for such a table because they actually contain multiple variables for a spe- cific location recorded at the same time. Common examples are datasets describing chemical analy- ses where multiple variables are analyzed from a single water sample taken at the same location and time. Another example is the inputs and out- puts of simulation models, where it is common to have multiple variables (e.g., pressure, velocity, storage) calculated for every model time step. 
Attribute series 
AttributeSeries is a table for archiving time-series data where multiple variables are indexed with 
Ts Time 
FeaturelD arlD 
[Figure 7.16] Example query for extracting a specific variable (in this case groundwater levels, VarlID=6875) for a specified time 
(in this case, January 1991). 

the same feature and time. The term attribute series was coined by combining the ideas that features have attributes (the attribute values that describe them in a Feature Attribute Table), and 
“time has series (the values that are indexed against each point in time in a series). Hence, if we think of feature attributes that no longer have fixed values but instead are expressed as time series, we create attribute series rather than simply attri- butes for each feature in a feature class. Each row in an attribute series table is indexed by a particu- lar FeatureID and a particular TsTime. Because a single row in this table can store values for several different time-series variables, this type of table may also be known as a multivariable time-series 
Feet above mean sea level 
< 600 
600 - 700 
700 - 800 
800 - 900 
900 - 1000 
> 1000 Attribute series table. For example, the Texas Water Development 
Board groundwater database stores results of water-quality analyses sampled at wells across 
Texas. For each sample analyzed, a set of about twenty water-quality parameters is recorded (e.g., 
TDS, pH, sulfate, calcium). All these parameters are related to the same sample, so they all can be indexed by the same feature and time. Thus, to store these data for a single feature and date/ time within the single-variable TimeSeries table, we would have to populate twenty rows, one for each variable measured. A more efficient way to archive these data is to add attributes for storing multiple values for each row in the table. The result is a table structure similar to the TimeSeries 
January 1991 
[Figure 7.17] A set of animated maps showing water levels in the Edwards Aquifer for the month of January in 1991, 1992, and 1993. 
table: data are indexed by space (FeatureID) and by time (TsTime), but instead of one variable, we store multiple variables. The resulting table 
(figure 7.18) is an attribute-series table (in this case the table is named WaterQuality to reflect that the series represent water-quality data). For a given value field, the field name indicates the variable whose TsValues are stored in that field. We call this field name the variable key (VarKey). Each of these variables is described in the VariableDefi- nition table as before, with the linkage between 
VariableDefinition and the attribute series established via the VarKey. Thus, the VarKey serves the same role as the VarID from the single-attribute a Attributes of WaterQuality,, 
Seat T7006 iy “1566 |7/7/2005 
+3155 eee 
Slit ae 
- “72.9 oe a5 [al Selected “1808 6/16/2005 EE a 
61 |615/2005 | 
Record: 14] «ff 1 >|] 7] ae __ 118 
Records (0 out aie +2000 Selected) time-series table, except that VarKey is better suited to be used as a field name as required by the attribute-series table. 
We analyze attribute series the same way we analyze single-variable time series. First we query for data related with a feature of interest over a specified time frame, then we can select one or more of the variables stored in the attribute-series table for inclusion in the time-series plot. For example, figure 7.19 shows a plot of water-quality parameters related with well 2833 located near 
Comal Springs in New Braunfels, Texas. The plot was created by querying an attribute-series table of water quality for FeatureID = 2833. 
[Figure 7.18] Example of an attribute-series table storing water-quality data. 
Graph of WaterQuality 
@ Calcium 
Well HydrolD = 2833 ®@ Magnesium [Figure 7.19] Plot of water quality at a well near Comal Springs in 
New Braunfels, Texas. 
The plot was created by querying an attri- bute-series table con- taining water-quality measurements. By querying for a specific 
[FeatuelD] = 2833 
SELECT * FROM WaterOualty WHERE: 
Clear | Verity Help | Load... Saye.., 
[fey] cose _| ae or are . - os feature one can plot sates See rs + — multiple water- i 1993 1997 1999 2001 ie EN Ga — 
1995 
— time series. 

Raster series 
The above examples have demonstrated how time-series datasets are stored within the Arc 
Hydro geodatabase. The task of mapping and animating time-series data stored in single- and multi-variable time-series tables is common to many groundwater studies. For analysis purposes it is also common to create continuous datasets describing the spatial distribution of a variable at a given time. These datasets are usually repre- sented as surfaces interpolated from monitoring data and stored as raster datasets. 
RasterSeries is a raster catalog for storing collections of raster datasets indexed by time 
(3) RasterSeries 
Raster catalog for storing collections of raster datasets indexed by time Time 1 
Fieldname __ Description 
Generic attribute (created automatically when you create a raster catalog) used to store the name of a raster dataset. Name 
VarilD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
TsTime Time stamp specifying the date and time associated with the raster. 
UTCOffset Number of hours the time coordinate system used to define 
TsTime is displaced from Coordinated Universal Time. 
[Figure 7.20] RasterSeries raster catalog for storing collections of time-indexed rasters. 
January 1991 
1992 |1/31/1992. 
iii ea UE ATAt cl 
_Selected | Records (0 ha] por) Show: rar Raster series 
(figure 7.20). Each raster is a snapshot of the environment at some instant in time, and grouping a series of rasters describes how the environment changes over time. Raster series are useful for describing the dynamics of spatially continuous phenomena, like the variations in groundwater levels or the distribution of rainfall over time. 
Rasters in the RasterSeries catalog are indexed by time (TsTime and UTCOffset) and by the time- series variable (VarID). Thus, each record in the 
RasterSeries catalog describes the continuous distribution of a single variable at a given time. 
For example, the water-level data shown for the month of January in 1991, 1992, and 1993 can be interpolated into three water-level surfaces repre- sented as raster datasets (figure 7.21). Similar to the water-level point features, rasters in the RasterSer- ies catalog can be animated over time to show the spatial-temporal change of a certain variable. 
Feature series 
The previous examples have described data structures where time-varying data is related with stationary features (e.g., wells and gages). 
Time-series data can also describe dynamic 
January 1992 
January 1993 
[Figure 7.21] Rasters representing water-level surfaces within the Edwards Aquifer stored in a RasterSeries raster catalog. 
features where the feature itself is moving over time or changing its geometry. A common exam- ple is the use of time-varying features to create particle tracks that describe the movement of 
Sei] FeatureSeries 
\Collections of features indexed by time 
|representing a series of geometries 
|varying in location or shape j 
| 
| 
Fieldname Description | 
| HydrolD Unique feature identifier in the geodatabase used for creating relationships between classes of the data model. 
VariD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the | 
VanableDefinition table. | 
| 
TsTime Time stamp specifying the date and time associated with the | feature. 
| UTCOffset Number of hours the time coordinate system used to define | 
| TsTime is displaced from Coordinated Universal Time. | 
| GroupID Index for grouping a set of features into a “track” showing the change of a feature’s shape, location, or both. 
c oes of features tnat [Figure 7.22] Feature series are collection vA) 
represent the change of a feature’s shape, location, or both. 
104 6882 2/21/2005, 1) «138.404 
66996882 81320051 138.577) 
| 6697) 88827872005 | «138536 
6696-6882 .6/14/2008 1) 138.517 
6882 5/27/2005 ; water and the time of travel of constituents within an aquifer. To describe such data, Arc Hydro introduces the concept of feature series. 
FeatureSeries are collections of features indexed by time representing a series of geometries vary- ing in location or shape. Each feature in a feature series exists for only a period of time. Features in a feature series can be grouped to form a “track” representing the change (in geometry, location, or both) of a particular feature over time. [Figure 7.22] shows the attributes of a feature-series dataset. 
Take for example the particle tracks shown in figure 7.23. Each feature in the dataset is indexed by VarID and TsTime, and in addition to these standard indexes the particles are also given a 
GroupID that creates a “particle track” from a set of standalone particles (in this example, four 
Animation Manaper 
Keyframes | Tracks Tine Yew | 
Tene Scale: = 1.00 + 
Aanins 22160085 *s'fp Jo Aseyinod ejeg 

tracks are indexed from 0 to 3). In addition to these indices, features in a feature series can be attributed with time-varying parameters. In this case, particles are attributed with the depth at which they are observed below the ground surface 
(Z_value). The combination of the Shape, TsTime, and GroupID supports tracking the movement of the time-varying particle features through space and time. We can create views of the feature series at different times or simply animate the track. 
Dataset catalog 
Recall that the SeriesCatalog table indexes individual time series in the TimeSeries table. Simi- larly, the DatasetCatalog table indexes time-series 
EB DatasetCatalog Dataset 4 
Table for indexing time-series datasets Dataset 2 Dataset 3 
| Dataset y 
Fieldname __ Description Se en 
VarlD Numerical identifier for the variable within the geodatabase. 
Matches the HydrolD of the associated record in the 
VariableDefinition table. 
DsType Type of time-series dataset described, e.g., RasterSeries, 
FeatureSeries, Feature Layer. 
DsSource Name of the time-series dataset described. 
TsTable Name of the time-series table that contains time-series values, used in cases where features are associated with a time series of values stored in a separate table (e.g., wells related with water levels, or polygons related with precipitation) 
StartTime Start date/time of the series. 
EndTime End date/time of the series. 
StepCount Number of unique time steps in the time-series dataset. 
[Figure 7.24] DatasetCatalog table for indexing time-series datasets (e.g., FeatureSeries and RasterSeries). 
= Attributes of aaa sacace dca 
Show: a Selected nf 688 a aa Dataset catalog datasets within a geodatabase, except that entries in the DatasetCatalog relate to time-series datasets as a whole rather than an individual feature. Whereas the SeriesCatalog applies to the TimeSeries table, the DatasetCatalog is typically associated with Ras- terSeries or FeatureSeries in the geodatabase. For example, one entry in the DatasetCatalog might indicate that groundwater levels are represented in the geodatabase as a raster series with X number of time steps. [Figure 7.24] shows the structure of the 
DatasetCatalog table. 
[Figure 7.25] shows an example of a DatasetCatalog table summarizing two time-series datasets. The selected row in the table shows a time series of 
VarID 6882, which in the VariableDefinition table is defined as subsurface particle tracks. DsType indi- cates that this is a feature series type dataset, and the source of the data is the Particles feature class. 
The start and end dates show the time range of the dataset, and the StepCount shows the number of date/time stamps (unique TsTime values) in the dataset. The DatasetCatalog and SeriesCatalog provide summary tables that enable us to quickly understand what types of time series are available within the geodatabase, the time period they cover, and in what type of datasets they are represented. 
Time enablement of ArcGIS layers 
Beginning with ArcGIS version 10, feature classes and tables can be “time-enabled” by specifying the field in the attribute table athat contains the time stamp and specifying some properties of this time 
[Figure 7.25] DatasetCatalog table summarizing time-series datasets. 
Records (1 out of 2 Selected) y| index, for example, its time zone and time interval. 
Functions are provided in ArcToolbox to convert data from one time zone to another. Graphing data indexed against different time zones is automati- cally handled in ArcGIS so that the information is viewed ina single-time context. This is particularly important when merging temporal information from weather and climate data sources with infor- mation from regular water data sources. Weather and climate data are typically indexed using the 
Universal Time Coordinate system, applicable at Greenwich, England, for data from anywhere on earth. This is done so that worldwide weather maps can be drawn for a unique point in time. 
Because groundwater and water resources data in general are usually viewed locally rather than globally, local time coordinates are typically used to record the time of measurement. 
Time-enablement of ArcGIS layers means that a record in a feature attribute table can have a time stamp associated with it, and if other records in this table describe the same feature at different times, or other features at the same time, then the begin- nings of a space-time analysis system exists. Time- enablement of ArcGIS data structures enhances and strengthens the temporal component of Arc Hydro. 
Framework and extended temporal components 
When integrating time-series data with a GIS, a common approach is to first collect single-variable time series of interest, and then use GIS tools to derive interpreted products such as raster series or feature series. Therefore, the Arc Hydro temporal component is available in two levels: framework and extended. The framework version includes the Time- 
Series, VariableDefinition, and SeriesCatalog table. 
These tables store, describe, and index single-variable time series, respectively. The extended version includes all the tables from the framework version, plus RasterSeries, FeatureSeries, AttributeSeries, and 
DatasetCatalog. If you do not need these additional datasets, then the framework version provides a lightweight geodatabase design for your work. 
Otherwise, the extended version gives you the full capabilities of the Arc Hydro temporal component. 
Steps for implementing the temporal component 
This section outlines the main steps involved in archiving and analyzing time-series data using the temporal component datasets. The first steps involved in implementing this component are to refine the geodatabase design to meet your specific project needs (see chapters 1 and 9 for a detailed description of these steps). Then you can import data into the time-series component tables and start creating different space-time datasets. In the follow- ing example we use a common workflow, creating water-level maps from water-level measurements taken at wells, for demonstrating the process of working with time-series data. The first step is to import time-series data into the tabular structures and then assign key attributes to relate time-series records with spatial features. You can then apply tools to create new space-time datasets such as maps of time series averaged over specific time periods and raster datasets created by interpolating time series measured at point locations. Finally, you can use the results of this process to create products such as maps, scenes, graphs, and animations. The following checklist provides a summary of the main steps for implementing the temporal component. 

Checklist 
1. Create the classes of the temporal component 
(manually using ArcCatalog or by importing from an XML schema) 
2. Add project specific classes, attributes, relationships, and domains as necessary 
3. Document datasets and changes made to the data model 
4. Import time-series data into the appropriate tables 
(TimeSeries, AttributeSeries) 
5. Establish relationships between time series and spatial features by populating key attributes 
6. Apply tools to create new time-series datasets 
(e.g., average values over a specified time period, interpolate raster datasets) 
7. Populate the summary catalog tables (SeriesCatalog, DatasetCatalog) 
8. Visualize time-series data and create products 
(maps, scenes, plots, animations) 
6875 | 9/8/1881 
6875 (7/7/1882 
: “6875 9/20/1929 oe ee saul all ” Selected cords 
[Figure 7.26] Example of water-level time series imported into the TimeSeries table. Steps for implementing the temporal component 
We start with importing our time-series data from its original form (text files, spreadsheets, database tables) into the table structures of the temporal component. In the following example 
(figure 7.26), water-level data from the Texas 
Water Development Board’s groundwater database were imported into the TimeSeries table. Key attributes were assigned after importing the data into the table. For example, water-level records were attributed with FeatureID values to associate the records with Well features. The original table in the groundwater database indexes wells by a “state well ID” (in the Arc Hydro geodatabase, this is stored in the HydroCode attribute). While this index is valid, the HydroID is used in the Arc 
Hydro geodatabase to assure that each feature is uniquely identified within the geodatabase. Thus, each of the water-level records was assigned a Fea- tureID corresponding to the well where the water levels were recorded. Also, each of the water-level records was attributed with a VarID (in this case 
VarID = 6875 for water levels), and UTCOffset of 
-6 to represent the local time zone in Central Texas. 
The water-level records and the time values were imported into the TsTime and TsValue fields. 
The next step is to apply tools to create new temporal datasets from the original time series. 
It is common to calculate summary statistics of a time-varying variable to represent the variable over a given time period. For example, we might want to create a water-level map for the winter of 
2001, such that each well will have a single value representing the winter period (January through 
March). There could be multiple measurements taken at a well during this period, thus we need to calculate a summary statistic that represents the water level at a well for the required time period. For example, we can select the repre- sentative value as the average of all water levels measured between January 1 and March 31, 2001 
(the Arc Hydro Groundwater tools include a geoprocessing tool, Make Time Series Statistics, to support this task). [Figure 7.27] shows the result of the averaging process, a new feature class where each feature includes an attribute giving pieog juawidojanag JajeM sexa| Jo Asayinod ejeq 
108 the summary statistic calculated from the timeseries records. 
The point features with the calculated statistics can be the basis for interpolating water-level rasters. For example, attribute values of the point features shown in figure 7.27 were used as inputs to the IDW interpolation tool (available with the Spa- tial Analyst extension). The result is a raster dataset representing the mean water level within the aqui- fer during the winter of 2001. The raster dataset can then be loaded into the RasterSeries raster catalog and indexed with a VarID and time stamped with a TsTime (figure 7.28). The Arc Hydro Groundwa- ter tools also include a tool, Add to Raster Series, to support automatic loading and attribution of rasters into the RasterSeries raster catalog. 
This workflow of going from water-level measurements in the time-series table to creating raster datasets stored and attributed in the Ras- terSeries raster catalog can be automated with a 
[Figure 7.27] Averaged water levels for wells in the Edwards Aqui- fer between January 
1 and March 31, 
2001. The Make Time 
Series Statistics tool was used to create the new feature class representing the sum- 
Feet above mary statistics over mean sea level the selected time 
@ <600 : 
@ 601-700 peved 
@ 701-800 
@ 201-900 
@ 901 - 100 

S Attributes of RasterSeries 
~ peeree winter 2001/6881 /1/1/2001 (1/1/2001 [373172001 | 
Record: 4] «ff 1} ma] Show: | All Selected | Records (0 x single model as shown in figure 7.29. The model starts with the Make Time Series Statistics tool that takes time series stored in the TimeSeries table and creates a new set of point features with summary statistics values for a defined time period. The 
*° Model 
Model Edit View Window Help 
Bl SS (ele) +) rslealselzz/ Qe ele) >) Steps for implementing the temporal component 
[Figure 7.28] |nterpolated raster dataset representing average water levels in the 
Edwards Aquifer during the winter of 
2001. The raster is stored and attributed » in the RasterSeries raster catalog. 
Feet above mean sea level 
< 600 
601 ~ 700 () 
@ 
@ 701-800 | to) 
@ 801 - 900 
‘901 - 1000, time-series statistics values are then interpolated to create a raster representing the water level as a continuous surface, and the raster is indexed and stored in the RasterSeries raster catalog using the 
Add to Raster Series tool. 
[Figure 7.29] Workflow of mapping time-series data related with Well features. The model includes creating time-series statistics, interpolating the calculated values to a raster, and storing and attributing the raster in the RasterSeries raster catalog.
