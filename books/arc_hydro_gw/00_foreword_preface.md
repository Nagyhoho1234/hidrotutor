# Foreword and Preface

Foreword 
FEW GIS COMMUNITIES HAVE BEEN BRAVE AND WISE ENOUGH TO DEVELOP A SET 
of common procedures and approaches that can be widely shared and adopted. The 
hydrology community has been one of the most successful at accomplishing this. This 
is significant because the adoption of common approaches will become increasingly 
important as GIS moves onto the Web. 
The work contributed by the hydrology community—closely tied to the science of 
water and water-resource management—is groundbreaking and revolutionary because it 
has led to a series of consistent, science-based methodologies for applying GIS to hydro- 
logic applications anywhere. 
Early on, leaders in hydrology realized that this work was essential for cataloging 
and understanding the quality and availability of freshwater that we use as humans and 
upon which all life on our planet relies. They began to think about developing a standard 
approach that could be used across a broad range of water-resource issues and geogra- 
phies. They realized that to understand these precious resources, they needed to build 
rich content that was simple to use, standardized, and well-defined. It had to be informa- 
tion that was trusted and collected consistently across many organizations and jurisdic- 
tions—a continuous, harmonized GIS of the world’s water resources. 
Initially, their work and progress focused on surface water. A key breakthrough a decade 
ago was the development and release of Arc Hydro—a set of information models and 
tools for applying GIS to hydrology. These efforts, led by David Maidment, provided intel- 
lectual breakthroughs on how to apply GIS to water-resource problems. This led to the 
adoption and application of GIS by a large and growing scientific community. The results 
of their work have been applied across thousands of water organizations worldwide. 
The Arc Hydro Groundwater data model presented in this book represents another 
major breakthrough in hydrology applications using GIS. 


FOREWORD 
As the original Arc Hydro data model was 
being deployed, many members of the hydrology 
community knew that they wanted to integrate 
aspects of groundwater with their surface water 
modeling tools and solutions. Gil Strassberg, men- 
tored by Maidment at the University of Texas, and 
Norm Jones and his team at Brigham Young Uni- 
versity and Aquaveo, have made major advance- 
ments in their GIS database designs and methods 
for groundwater. 
They initially focused on creating groundwater 
models and tools, but these were designed to work 
independently of surface water models and solu- 
tions. In their second stage, the authors began to 
articulate a vision in which these two worlds of 
hydrology (surface water and groundwater) could 
be integrated and combined into a unified view for 
water-resource management. After all, wasn’t the 
ability to integrate a key GIS premise? 
This book presents their results. It is the culmi- 
nation of many years of hard work, and the result 
is fantastic. Their contributions include: the use 
of 3D information and visualization; time-series 
recording and modeling of observations; a design 
for operational information for groundwater man- 
agement; the ability to integrate widely adopted, 
scientific groundwater models into GIS; and the 
use of GIS to support groundwater modeling 
applications. 
Their designs are also elegantly simple and 
clearly articulated. Any hydrologist can under- 
stand and apply these models. 
Meanwhile, this team continues to make 
progress in advancing GIS-based hydrology. And 
this dynamic and ever-changing process comes 
at a very exciting time. GIS is advancing into the 
new Web 2.0 world with all of its social networking 
implications. Three-dimensional GIS and dynamic, 
time-aware GIS are starting to be used in many 
fields. GIS and sensor information are being inte- 
grated into these environments as Web services that 
can be aggregated and combined using GIS. 
Viii This work continues to provide leadership on 
how to move forward on rich information models, 
analytical tools and results, interactive maps, 
3D visualization, and working with time-based 
observations. 
The hydrology community has assumed a 
leadership role for many exciting advancements 
in the application and use of GIS. Strassberg and 
his collaborators have captured these designs and 
methods. This book provides a foundation and a 
point of departure for future work and progress 
in this field. 
I can’t wait to see the progress they will make in 
the coming years. 
Clint Brown 
Esri 
Redlands, California 
October 2010 


Preface 
GEOGRAPHIC DATA MODELS ARE IMPORTANT BECAUSE THEY ESTABLISH A COMMON 
language enabling us to describe aspects of our environment systematically and con- 
sistently over large areas. Instead of having finite projects that end with specific outputs, 
the data model process for groundwater continues through time and across people and 
institutions to produce a comprehensive system that increases as we add information 
and detail. Water is ubiquitous in our environment and is vital to every human and life 
form on our planet. So many different factors bear on the management and science of 
water that the contributions of many disciplines are needed to describe and understand 
it. Hydrologic and hydrogeologic information systems built using standardized data 
models capture some of this variety of knowledge and information for everyone to share 
and build upon. 
Arc Hydro: GIS for Water Resources, published by Esri Press in 2002, defined a geographic 
data model for surface water resources implemented in ArcGIS called Arc Hydro. In the 
years following, the Arc Hydro toolset has expanded to include more than 100 tools, 
becoming the most widely used geospatial toolkit for application in water resources. A 
question frequently asked during this period was, “What about groundwater?” This book 
responds to that question by describing a new and evolving geographic data model for 
groundwater named Arc Hydro Groundwater. As we presented the draft design for this 
data model to potential users, their feedback asked us to “connect surface and ground- 
water—they are really one resource.” We have done this by creating a common frame- 
work data representation of surface and groundwater features, associated with a set of 
more specialized data model components that can be individually selected for particular 
aspects of groundwater resources. We hope that this process will inspire others to develop 
additional data model components to cover subjects not dealt with in our work. 


PREFACE 
The main goals of Arc Hydro Groundwater are: 
¢ To provide a standard way to apply GIS to 
groundwater systems using readily available 
data such as geological and aquifer maps, loca- 
tions of wells and associated tables of subsurface 
borehole information, and water observations 
data such as piezometric head levels and water 
quality measurements; 
To build a 3D representation of the subsurface 
hydrogeologic environment, including the verti- 
cal structure of boreholes, “geovolumes” repre- 
senting the spatial extent of hydrogeologic units, 
and cross-sections drawn between boreholes or 
cut through the subsurface hydrostratigraphy; 
¢ To take sparse groundwater observations in 
space and time and enable time-averaging and 
spatial interpolation of these measurements to 
create time-sequenced maps; 
¢ To provide a link between ArcGIS and ground- 
water modeling, in particular to the MODFLOW 
(modular finite-difference flow model) ground- 
water simulation model that is a standard in the 
groundwater field. 
It can thus be seen that Arc Hydro Groundwater over- 
comes two challenges normally limiting the appli- 
cation of GIS to groundwater systems—describing 
a 3D system in a 2D mapping environment and 
describing the time-varying properties of the 
groundwater system. Arc Hydro Groundwater 
resolves these issues by extending the 2D static 
GIS approach to a 3D description of subsurface 
hydrogeology and by providing space-time data- 
sets for describing the time-varying properties of 
groundwater systems. 
Arc Hydro Groundwater can be used to publish 
digital descriptions of groundwater systems using 
ArcGIS Server and to assemble the description of 
x such systems using ArcGIS Desktop. As geospatial 
data becomes increasingly available for Web ser- 
vices, Arc Hydro Groundwater offers an ideal way 
for federal, state, and regional groundwater agen- 
cies to publish descriptions of their groundwater 
resources using a common structure. 
We hope that this book, Arc Hydro Groundwater: 
GIS for Hydrogeology, will be valuable to readers 
from a variety of disciplines, including water- 
resource engineers, hydrologists, hydrogeologists, 
geographers, and GIS specialists. We believe edu- 
cators will also find this book a valuable academic 
resource at the college and postgraduate levels. 
This book uses groundwater datasets from vari- 
ous locations in Texas to illustrate the application 
of Arc Hydro Groundwater to real situations. These 
datasets are available for download from the 
Arc Hydro Resource Center: http://resources. 
arcgis.com/archydro. Also accessible at this loca- 
tion are the graphics used in each chapter set up 
as PowerPoint presentations so that instructors 
using Arc Hydro Groundwater in their courses can 
readily incorporate visual material from the book 
into their lectures. A freely available toolset for 
getting started with Arc Hydro Groundwater is also 
available from the Arc Hydro Resource Center. 
The major credit for designing and developing 
the groundwater data model goes to Gil Strassberg, 
who accomplished this as part of his doctoral stud- 
ies at the Center for Research in Water Resources of 
the University of Texas at Austin under the super- 
vision of coauthor David Maidment. Strassberg 
experimented with 3D data structures, examined 
what others had done in related fields, designed 
the data model components, built a prototype 
toolset to implement the data model, developed 
working examples of applications in various 
areas, and wrote his dissertation to describe all 
this research. Strassberg carried the major load as 
lead author in writing this book. The groundwater 
data model received Esri’s Prize for Best Data 
Model at the 2006 Esri User Conference. 
