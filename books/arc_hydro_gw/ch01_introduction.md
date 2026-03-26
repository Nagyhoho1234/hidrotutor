# Chapter 1: Introduction

As work on the data model progressed, it 
became apparent that we needed to deal with two 
distinct bodies of knowledge—hydrogeology 
and groundwater modeling. Hydrogeology is a 
branch of geology dealing with water-bearing 
rock units near the earth’s surface. Groundwa- 
ter modeling is a branch of civil engineering that 
deals with management of groundwater resources 
and is concerned with issues of water supply and 
groundwater contamination. These are two very 
different perspectives, and we were fortunate in 
having advisers to guide us along the path—for 
hydrogeology, Randy Keller of the University of 
Oklahoma, and for groundwater modeling, coau- 
thor Norman Jones of Brigham Young University. 
Jones, in particular, has been closely involved in 
the groundwater data model design and is a coau- 
thor of this book. He has more than twenty years 
of experience in the groundwater field and is the 
principal developer of the widely used system 
that provides pre- and postprocessors for many 
groundwater models. 
The design of the data model is important, but 
realizing all of its benefits requires an associated 
set of tools. Accordingly, Esri has partnered with 
Aquaveo LLC of Provo, Utah, to develop the Arc 
Hydro Groundwater tools under Jones’ direction. 
The groundwater toolsets include a rich suite of 
tools for managing and analyzing groundwater 
data, including tools for querying, plotting, and 
mapping time series; editing 3D hydrogeologic 
models from borehole data, cross-sections, sur- 
faces, and volumes; and for editing and visual- 
izing MODFLOW simulation models. As a set of 
geoprocessing tools, the toolkit ensures that users 
will be able to build custom solutions and work- 
flows. Portions of the toolkit are freely distributed, 
and portions are fee-based. These fees support 
ongoing tool development and management of 
the data model. 
We thank Timothy Whiteaker and Steve Grisé, 
who participated in designing the groundwater PREFACE 
data model and wrote and edited substantial 
parts of this book. We are grateful to reviewers 
Todd Jarvis, associate director, Institute for Water 
and Watersheds, Oregon State University; Eileen 
Poeter, director, International Ground-Water Mod- 
eling Center, Emeritus Professor of Geological 
Engineering, Colorado School of Mines; and Wei 
Li, research fellow, Center for Applied GeoSci- 
ence, Hydrogeology, Eberhard Karls Universitat 
Tubingen, Germany, for their valuable feedback on 
the manuscript. As always, we have been guided 
by our colleagues at Esri, and in particular we 
would like to acknowledge the contributions of 
Steve Kopp, Lori Armstrong, Michael Zeiler, Dean 
Djokic, Nawajish Noman, Zichuan Ye, Scott More- 
house, Clint Brown, and Jack Dangermond, who 
in various ways have supported and guided our 
work. Joe Breman, formerly of Esri, also was a 
valuable resource. And, to our friends at Esri Press, 
we acknowledge another debt of gratitude—Esri 
Press books are not just books, they are works of 
art in their own right. Thanks to Mark Henry, who 
edited the text, and to Peter Adams, Judy Hawkins, 
David Boyles, Monica McGregor, Brian Harris, and 
their colleagues for all their contributions to our 
manuscript and its finished product, this book. 
Gil Strassberg 
Norman L. Jones 
David R. Maidment 
xi 


Arc Hydro Groundwater Data Model 
Framework — oe 
oe aS - — SF! Aquifer 
WaterLine i) Watershed F Waterbody WaterLine | 
sil WaterPoint 
fe 
a MonitoringPoint _ 
Polateg 
Water raced 
D 
Cubic 
feetper | S€Cong f Steamfoy, 
Calcium, 
Sonce, aq “tration Mg) 
CO3 
- 
a aay Cie MgiL 
xii 


== &@ GeoSection 
XS2D_ Panel 
X$2D_MajorGrid | 
xili 


Why Arc Hydro for groundwater? 
FRESHWATER IS ONE OF THE EARTH’S MOST PRECIOUS RESOURCES, VITAL TO 
human life and to plant and animal life. The volume of groundwater is much larger 
than the volume of water in rivers and lakes, but it lies hidden beneath the land surface 
in aquifers. About 90 percent of the earth’s readily available freshwater is stored as 
groundwater, slowly percolating through the pore spaces and fractures of rocks near 
the earth’s’surface. Large regions of the world depend on groundwater for their water 
supply, particularly in rural areas, because aquifers are spatially extensive. 
Groundwater has not been a traditional area of application of geographic information 
systems (GIS) to water resources, in part because groundwater resources are less visible 
and readily mapped compared to streams, rivers, lakes, and watersheds. Also, ground- 
water is inherently a 3D phenomenon because the depth at which water is found in a well 
is a critical measure of its accessibility. As a well is drilled, its borehole passes through 
many subsurface strata laid down in layers over geologic time. The spatial extent of these 
layers is much larger than is their vertical thickness, much like sheets of paper, so 2D 
GIS mapping of well locations and aquifer boundaries is the normal point of departure 
for groundwater projects. The core framework of the Arc Hydro data model supports 
2D mapping of groundwater resources, and the extensions of this model support 3D 
representations of boreholes and hydrogeologic strata. 


CHAPTER 1: INTRODUCTION 
We use a number of terms to define different 
aspects of Arc Hydro. The name Arc Hydro refers to 
the overall data model for representing hydrology, 
including surface water and groundwater. Within 
this book we refer to this general model as the Arc 
Hydro data model, or simply as Arc Hydro. The 
first version of Arc Hydro mainly described sur- 
face water systems including drainage, river net- 
works, and time series. This work was published 
in a book titled Arc Hydro: GIS for Water Resources 
(Maidment 2002). The original Arc Hydro has been 
redesigned to include a simplified framework for 
representing the basic surface water and ground- 
water features. Within this book we refer to the 
framework data model as the Arc Hydro Frame- 
work, or simply as the framework. You can add 
surface water and groundwater components to the 
Arc Hydro Framework to describe different aspects of hydrologic systems (the framework data model 
and the components are described in chapter 2). 
We refer to the groundwater components of the 
data model as Arc Hydro Groundwater, or simply 
as the groundwater data model, which is the focus 
of Arc Hydro Groundwater: GIS for Hydrogeology. 
Arc Hydro is not just a set of data models. Rich 
sets of tools have been developed to help ArcGIS 
users implement the data model, organize their 
data, and create GIS products. These tools make 
use of the standard data structures and the rela- 
tionships between features within the data model 
to enhance the capabilities of ArcGIS for the man- 
agement and analysis of water resources. For 
surface water analysis, a set of tools named Arc 
Hydro Tools has been developed by Esri. These 
tools are available on the Esri Web site (www.esri. 
com/archydro). For groundwater analysis a set of 
» Precipitation 
on land 
Infiltration Moisture over land 
Evaporation from land <—— 
Precipitation 
on ocean 
Evaporation and 
Evapotranspiration 
Evaporation from ocean 
Surface outflow ( ‘ 
Groundwater ou 
Figure 1.1 The hydrologic cycle depicts the circulation of the waters of the earth. 


tools named Arc Hydro Groundwater Tools has 
been developed by collaboration between Aqua- 
veo, a water resources engineering consulting firm 
in Provo, Utah, and Esri, and are available on the 
Aquaveo Web site (www. aquaveo.com/archydro). 
What makes water different when it 
comes to GIS? 
GIS is applied to many fields of endeavor, indeed to 
any field in which data can be depicted geospatially. 
So, what makes water different? Why do we need 
special geographic data models for water? First of 
all, water is a subtle substance. It flows from one 
place to another on the land surface and through 
the subsurface; water evaporates and travels great 
distances rapidly in the atmosphere and then 
returns to the earth again as precipitation. It flows 
in streams and rivers and accumulates in lakes, 
bays, and estuaries to form the blue features on 
topographic maps. Water movement through the 
hydrologic cycle (figure 1.1) is extremely complex 
and is still not completely understood. 
Using GIS to describe natural water systems 
requires a means to describe the connectivity of 
water flow through the landscape. It is not enough 
to know that there are geographic data layers of 
water features like streams, aquifers, and wells. It 
also matters which streams contribute water to 
a particular aquifer and which wells are drilled 
into that aquifer to supply water for domestic 
consumption or irrigation. Only in this way can 
we understand the inflow and outflow of water, 
in particular groundwater systems, and thus 
manage these systems wisely. This book, Arc Hydro 
Groundwater: GIS for Hydrogeology, describes a geo- 
graphic data model for hydrogeology, using the 
Edwards Aquifer in Texas as a vehicle for devel- 
oping and explaining concepts. The surface water 
components are described in the book Arc Hydro: 
GIS for Water Resources (Maidment 2002), which 
is planned to be updated to reflect the new Arc What makes water different when it comes to GIS? 
Hydro design. These books describe something 
more than geographic data models for surface 
and groundwater—they describe a geographic 
data framework for water, with particular com- 
ponents to depict different aspects of surface and 
groundwater systems. 


CHAPTER 1: INTRODUCTION 
city in the United States whose water supply 
comes principally from groundwater, distributed 
Aquifer systems are vital to the regions that overlie throughout the city after being pumped from hun- 
them. The Edwards Aquifer (figure 1.2) underlies dreds of wells drilled into the Edwards Aquifer. 
the cities of San Antonio, San Marcos, and Austin Water from these wells supports a population of 
in south-central Texas. San Antonio is the largest more than 2 million people. Edwards Aquifer 
The HEE contributing Zone 
Edwa rds Aq u ifer "Recharge Zone 
Re gi on Transition / Artesian Zone 
Artesian Zone Travis 
ypueyx29 BHa15 Jo AsayinoD 
d Brackettville . in 
a airs Uvalde = Medina 
Figure 1.2 Map of the Edwards Aquifer region showing the zones within the aquifer and the recharge zone contributing 
surface water to the aquifer. 


In San Marcos and Austin, beautiful springs 
discharge water from the Edwards Aquifer. 
Figure 1.3 shows the pool overlying San Marcos 
Springs. The deep water is perfectly clear—you 
can even see sand grains jumping on the bed 
rock as the groundwater discharges over them. 
This peaceful haven in San Marcos has sustained 
people for thousands of years and is considered 
to be one of the oldest continuously inhabited 
places in North America. 
The Edwards Aquifer is not just an environment 
of water and rocks. It is home to creatures such 
as the blind salamander, an almost transparent 
amphibian perfectly adapted to its life in the 
perpetual darkness of the aquifer’s underground What makes water different when it comes to GIS? 
cavities. Indeed, it is the necessity to sustain 
the spring flow and support the populations of 
endangered species such as the blind salamander 
that triggers restrictions on water pumping from 
the aquifer when water levels are low. The pres- 
sure of population growth bears down upon the 
Edwards Aquifer. New housing developments, 
shops, offices, and roads are spreading where 
once there was a quiet forest. Bacteria and chemi- 
cals washed down with runoff waters are invad- 
ing the pristine aquifer environment. Careful 
management of both water quantity and quality 
in the aquifer are needed to preserve this pre- 
cious asset to sustain future generations as it has 
sustained those of the past. 
ypseyy29 66159 jo Asayino> 
Figure 1.3 Tourists get a picturesque view of the abundant plant and fish life in the San Marcos Springs through a glass- 
bottom boat. 


CHAPTER 1: INTRODUCTION 
Surface water and groundwater 
Groundwater is strongly related with surface 
water in the Edwards Aquifer. Water seeping 
through the limestone rock of the aquifer has cre- 
ated a karst landscape with many caves, fractures, 
and sinkholes that allow fast movement of water 
from the surface into the aquifer formation and 
within the subsurface (figure 1.4). 
The groundwater discharge from the San 
Marcos Springs forms the flow of the San Marcos 
River. As this river meanders downstream, it is 
joined by the Blanco River, whose flow is derived 
mostly from surface runoff, and these in turn are 
tributaries of the Guadalupe River, which carries 
their waters to the Gulf of Mexico. Normally a 
quiet, slow-moving river, the Guadalupe can turn 
into a raging torrent during severe storms and 
devastate the surrounding countryside. 
To accurately describe the water resources of 
the region, we must map both groundwater and 
surface water features together (figure 1.5) and 
define the relationships between them. This is part 
of the new design of Arc Hydro, which includes 
a framework data model with basic surface water 
and groundwater features and additional compo- 
nents describing unique aspects of surface water 
and groundwater. 
Groundwater datasets 
In the United States, data depicted on blue lines, 
the color of surface water features on topographic 
maps, have been compiled by the Unites States 
Geological Survey (USGS) into seamless national 
hydrography datasets at scales of 1:100,000 and 
1:24,000, but no equivalent national hydrogeol- 
ogy dataset exists. Subsurface hydrogeologic data 
are measured and archived by many federal, state, 
and local groundwater agencies in a fragmented 
way without a common means of data access and Aouiny sayinby spuempy au} jo Asayinop 
Figure 1.4 On top is a limestone bedrock with dissolution 
features. Over time, water slowly dissolves the rock and 
creates fractures and recharge features. The bottom figure 
shows a 70-foot-deep vertical shaft recharging water into 
the aquifer. 
synthesis. The lack of a systematic organization of 
hydrogeologic and groundwater data means that 
their formats vary from state to state, from loca- 
tion to location, and from project to project. A new 
groundwater investigation can be like an Easter 
egg hunt, where you search around for the basic 
data needed to support the investigation, coping 
with many disparate data types and formats from 
different data sources. 
We envisage that the adoption of the Arc Hydro 
Groundwater data model will lead to better orga- 
nization of groundwater data so that standard- 
ized groundwater and hydrogeologic datasets 


can be systematically compiled and maintained. 
Since hydrogeology is a subfield of geology, it 
is appropriate that Arc Hydro Groundwater has 
a geology component to allow for incorporating 
existing geologic maps and data into Arc Hydro 
_ Groundwater datasets. 
The ArcGIS Desktop software system is the key 
means by which groundwater information is com- 
piled and synthesized in Arc Hydro Groundwater. 
@ = Springs 
g Rivers 
Aquifer 
i ae) Confined 
Outcrop Groundwater datasets 
However, this is now being supplemented by 
ArcGIS Server and ArcGIS Online, by which com- 
piled Arc Hydro datasets can be published on the 
Internet as maps and data services. This emerg- 
ing “services-oriented architecture” for geospa- 
tial information is an important way for separate 
organizations to publish geographically distributed 
groundwater datasets in a manner that facilitates 
their assembly and integration over a region. 
Kanins |e21bojoey ‘s'n pue ‘pieog Juatudojanag sare/y SEXA] ‘ADIAJAS Hed [PUOIIEN *S'1) 
"Su ‘eOUaWy UNON sepy ajay Jo Asazino> ‘eyeq UONeBiAeN aAHOWOINY GNY © Bep dey) 
Figure 1.5 The Edwards Aquifer (in brown) and the Guadalupe River Basin (with the watershed in green and rivers in blue) 
are located in Central Texas. A strong connectivity exists between surface water recharging the aquifer through streams 
flowing over the outcrop of the aquifer and groundwater discharging through springs. 


CHAPTER 1: INTRODUCTION 
Groundwater wells 
Wells provide the most abundant source of 
groundwater information. Many large tabular 
databases describing wells exist, both as “well 
logs” that describe the details of well construction 
and the subsurface materials encountered while 
drilling, and as “observations” that describe the 
water level and sometimes the chemical proper- 
ties of the well water indexed by time. This infor- 
mation is sparse both in space and in time: sparse 
in space because each well is an individual entity, 
and they are drilled relatively far apart from one 
another; sparse in time because groundwater con- 
ditions change slowly, and most wells are manu- 
ally sampled infrequently over periods of months 
or years. Figure 1.6 shows an artesian groundwa- 
ter well, with water flowing freely from the sub- 
surface. This is common to the artesian zones of 
the Edwards Aquifer. 
This sparse information must be interpreted and 
interpolated to generate spatial maps of ground- 
water properties, in particular to produce piezo- 
metric head maps that describe the spatial patterns 
of groundwater levels (or pressures) in aquifers. If 
piezometric head maps are constructed for succes- 
sive periods of time and subtracted one from the 
next, a picture of the rise and fall of groundwater 
conditions through time can be obtained. The Arc 
Hydro Groundwater tools include geoprocessing 
tools and models for accomplishing this task (see 
chapter 7). Figure 1.6 Groundwater under pressure flows freely from a 
confined aquifer to the surface of this flowing artesian well. Aywouny sayinby spsempy au} jo fsayino> 
