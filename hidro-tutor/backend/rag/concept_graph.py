"""Topic dependency graph for the hidroinformatics book.

Maps concepts to chapters and defines prerequisite relationships
so the system can guide students through topics in order.
"""

from dataclasses import dataclass, field


@dataclass
class Concept:
    """A concept/topic in the book."""
    name: str
    chapter: int
    section: str = ""
    prerequisites: list[str] = field(default_factory=list)
    description: str = ""


# The concept graph — topics and their prerequisites
CONCEPT_GRAPH: dict[str, Concept] = {
    # Part I: Foundations
    "global_water_crisis": Concept(
        "Global Water Crisis", 1, "1.1",
        [], "Floods, droughts, water quality challenges worldwide"
    ),
    "what_is_hidroinformatics": Concept(
        "What is Hidroinformatics", 1, "1.2",
        ["global_water_crisis"], "The convergence of hydrology, GIS, computing, and AI"
    ),
    "coordinate_systems": Concept(
        "Coordinate Reference Systems", 2, "2.1",
        [], "Geodetic datums, projections, CRS"
    ),
    "map_projections": Concept(
        "Map Projections", 2, "2.2",
        ["coordinate_systems"], "UTM, geographic, Hungarian EOV"
    ),
    "data_sources": Concept(
        "Hydrological Data Sources", 3, "3.1",
        [], "Where to find elevation, precipitation, discharge data"
    ),
    "gis_fundamentals": Concept(
        "GIS Fundamentals", 4, "4.1",
        ["coordinate_systems"], "Raster vs vector, spatial operations"
    ),

    # Part II: Terrain Analysis
    "raster_grids": Concept(
        "Raster Grids and DEMs", 5, "5.1",
        ["gis_fundamentals"], "How computers represent terrain as grids"
    ),
    "dem_sources": Concept(
        "DEM Data Sources", 5, "5.3",
        ["raster_grids"], "SRTM, Copernicus, ALOS, NED"
    ),
    "map_algebra": Concept(
        "Map Algebra", 6, "6.1",
        ["raster_grids"], "Local, focal, zonal, global operations"
    ),
    "slope_aspect": Concept(
        "Slope and Aspect", 7, "7.1",
        ["raster_grids", "map_algebra"], "Terrain derivatives from DEMs"
    ),
    "curvature": Concept(
        "Curvature", 7, "7.3",
        ["slope_aspect"], "Profile and plan curvature"
    ),
    "precipitation_measurement": Concept(
        "Precipitation Measurement", 8, "8.1",
        ["data_sources"], "Rain gauges, radar, satellite rainfall"
    ),
    "spatial_interpolation": Concept(
        "Spatial Interpolation of Rainfall", 8, "8.2",
        ["precipitation_measurement", "gis_fundamentals"], "IDW, kriging, Thiessen polygons"
    ),

    # Part III: Watershed Delineation
    "pit_filling": Concept(
        "Pit Filling / DEM Conditioning", 9, "9.1",
        ["raster_grids"], "Removing spurious depressions from DEMs"
    ),
    "flow_direction": Concept(
        "Flow Direction (D8, D-inf)", 10, "10.1",
        ["pit_filling", "slope_aspect"], "D8 algorithm, D-infinity, flow encoding"
    ),
    "flow_accumulation": Concept(
        "Flow Accumulation", 10, "10.2",
        ["flow_direction"], "Contributing area, drainage area grids"
    ),
    "stream_network": Concept(
        "Stream Network Delineation", 11, "11.1",
        ["flow_accumulation"], "Threshold-based channel extraction"
    ),
    "watershed_delineation": Concept(
        "Watershed Delineation", 11, "11.2",
        ["stream_network", "flow_direction"], "Pour points, catchment boundaries"
    ),
    "python_automation": Concept(
        "Python Automation for GIS", 12, "12.1",
        ["watershed_delineation"], "Scripting GIS workflows with Python"
    ),

    # Part IV: Flood Hazard
    "lidar": Concept(
        "LiDAR Technology", 13, "13.1",
        ["raster_grids"], "Airborne laser scanning, point clouds, high-res DEMs"
    ),
    "hand": Concept(
        "HAND (Height Above Nearest Drainage)", 14, "14.1",
        ["flow_direction", "stream_network"], "Relative elevation for flood mapping"
    ),
    "flood_inundation_mapping": Concept(
        "Flood Inundation Mapping", 15, "15.1",
        ["hand", "lidar"], "GIS-based flood extent delineation"
    ),
    "flood_forecasting": Concept(
        "Real-Time Flood Forecasting", 16, "16.1",
        ["flood_inundation_mapping", "precipitation_measurement"],
        "Operational flood prediction systems"
    ),
    "flood_exposure": Concept(
        "Flood Exposure and Vulnerability", 17, "17.1",
        ["flood_inundation_mapping"], "Demographics, damage estimation"
    ),

    # Part V: Groundwater
    "subsurface_3d": Concept(
        "3D Subsurface GIS", 18, "18.1",
        ["gis_fundamentals"], "Representing geology in 3D"
    ),
    "wells_boreholes": Concept(
        "Wells and Borehole Data", 19, "19.1",
        ["subsurface_3d", "data_sources"], "Hydrogeological observations"
    ),
    "hydrogeologic_modeling": Concept(
        "Hydrogeologic Model Building", 20, "20.1",
        ["wells_boreholes", "spatial_interpolation"], "Layer assembly, property estimation"
    ),
    "groundwater_simulation": Concept(
        "Groundwater Flow Simulation", 21, "21.1",
        ["hydrogeologic_modeling"], "MODFLOW, finite difference, calibration"
    ),

    # Part VI: AI and the Future
    "model_calibration": Concept(
        "Model Calibration", 22, "22.1",
        ["groundwater_simulation", "watershed_delineation"],
        "Parameter estimation, objective functions, uncertainty"
    ),
    "ml_hydrology": Concept(
        "Machine Learning in Hydrology", 23, "23.1",
        ["model_calibration"], "LSTM, random forests, deep learning for water"
    ),
    "agentic_ai": Concept(
        "Agentic AI for Modeling", 24, "24.1",
        ["ml_hydrology", "python_automation"], "LLM agents that build and calibrate models"
    ),
    "digital_twins": Concept(
        "Digital Twins for Water Systems", 25, "25.1",
        ["flood_forecasting", "ml_hydrology"], "Real-time model-observation fusion"
    ),
    "water_intelligence": Concept(
        "Water Intelligence and the Future", 25, "25.4",
        ["digital_twins", "agentic_ai"], "Open science, equity, climate adaptation"
    ),
}


def get_prerequisites(concept_key: str) -> list[str]:
    """Get all prerequisite concepts (recursive) for a given concept."""
    visited = set()
    result = []

    def _walk(key: str):
        if key in visited or key not in CONCEPT_GRAPH:
            return
        visited.add(key)
        for prereq in CONCEPT_GRAPH[key].prerequisites:
            _walk(prereq)
            if prereq not in result:
                result.append(prereq)

    _walk(concept_key)
    return result


def get_concepts_for_chapter(chapter: int) -> list[str]:
    """Get all concept keys for a given chapter number."""
    return [k for k, v in CONCEPT_GRAPH.items() if v.chapter == chapter]


def get_concept_tree() -> dict:
    """Return the full concept graph as a serializable dict."""
    return {
        key: {
            "name": c.name,
            "chapter": c.chapter,
            "section": c.section,
            "prerequisites": c.prerequisites,
            "description": c.description,
        }
        for key, c in CONCEPT_GRAPH.items()
    }
