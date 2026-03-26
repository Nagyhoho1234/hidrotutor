"""
Copy matched PPT images to the book images directory with proper naming.

Only copies HIGH-confidence matches where a single primary image is identified.
For composite figures (requiring multiple source images), prints a note instead.

Usage:
    python copy_matched_images.py
"""

import shutil
from pathlib import Path

# Base paths
PPT_BASE = Path(r"C:\maidment_hidroGIS\images\ppt")
BOOK_DIR = Path(r"C:\maidment_hidroGIS\images\book")

# Create output directory
BOOK_DIR.mkdir(parents=True, exist_ok=True)

# Mapping: (figure_id, chapter, figure_num) -> list of (ppt_folder, filename, confidence, notes)
# Each entry is the best single representative image for that figure.
MATCHES = {
    # Chapter 2
    "fig_02_01": {
        "sources": [("MapProj", "slide28_img034.png")],
        "confidence": "high",
        "notes": "Geoid, ellipsoid, and Earth surface diagram",
    },
    "fig_02_04": {
        "sources": [("MapProj", "slide49_img060.png")],
        "confidence": "high",
        "notes": "Map projection families (Earth to Globe to Map)",
    },
    "fig_02_06": {
        "sources": [("MapProj", "slide41_img048.png")],
        "confidence": "high",
        "notes": "GRACE satellite mission concept",
    },
    # Chapter 4
    "fig_04_03": {
        "sources": [("Lecture22018", "slide28_img046.png")],
        "confidence": "high",
        "notes": "Geodatabase structure diagram",
    },
    "fig_04_04": {
        "sources": [
            ("Lecture22018", "slide10_img013.gif"),
            ("Lecture22018", "slide10_img014.gif"),
        ],
        "confidence": "high",
        "notes": "Vector vs raster comparison (two images to composite)",
    },
    # Chapter 7
    "fig_07_04": {
        "sources": [
            ("ExtendedTerrainAnalysis", "slide51_img071.png"),
            ("ExtendedTerrainAnalysis", "slide51_img072.png"),
        ],
        "confidence": "high",
        "notes": "D8 vs D-infinity flow direction",
    },
    # Chapter 8
    "fig_08_01": {
        "sources": [("Ex3Overview", "slide11_img003.png")],
        "confidence": "high",
        "notes": "Thiessen polygons with watershed intersection",
    },
    # Chapter 9
    "fig_09_01": {
        "sources": [("ExtendedTerrainAnalysis", "slide02_img002.png")],
        "confidence": "high",
        "notes": "Terrain flow analysis framework overview",
    },
    "fig_09_03": {
        "sources": [("DemWatershedDelineation", "slide08_img012.png")],
        "confidence": "high",
        "notes": "Pit filling cross-section",
    },
    "fig_09_04": {
        "sources": [("DemWatershedDelineation", "slide29_img026.wmf")],
        "confidence": "high",
        "notes": "AGREE method cross-section (WMF format - may need conversion)",
    },
    # Chapter 10
    "fig_10_01": {
        "sources": [("DemWatershedDelineation", "slide13_img014.png")],
        "confidence": "high",
        "notes": "Flow direction grid",
    },
    "fig_10_02": {
        "sources": [("Ex3Explanations", "slide06_img009.png")],
        "confidence": "high",
        "notes": "Flow direction encoding from ArcGIS help",
    },
    "fig_10_03": {
        "sources": [
            ("ExtendedTerrainAnalysis", "slide52_img073.png"),
            ("ExtendedTerrainAnalysis", "slide52_img074.png"),
        ],
        "confidence": "high",
        "notes": "D8 vs D-infinity contributing area comparison",
    },
    "fig_10_04": {
        "sources": [
            ("ExtendedTerrainAnalysis", "slide36_img061.png"),
            ("ExtendedTerrainAnalysis", "slide36_img062.png"),
            ("ExtendedTerrainAnalysis", "slide36_img063.png"),
        ],
        "confidence": "high",
        "notes": "Stream networks at three thresholds",
    },
    "fig_10_05": {
        "sources": [("ExtendedTerrainAnalysis", "slide60_img085.png")],
        "confidence": "high",
        "notes": "Dependence function grid",
    },
    "fig_10_07": {
        "sources": [("HAND", "slide12_img019.png")],
        "confidence": "high",
        "notes": "HAND concept from TauDEM D-infinity",
    },
    # Chapter 11
    "fig_11_01": {
        "sources": [
            ("ExtendedTerrainAnalysis", "slide16_img027.png"),
            ("ExtendedTerrainAnalysis", "slide16_img028.png"),
            ("ExtendedTerrainAnalysis", "slide16_img029.png"),
        ],
        "confidence": "high",
        "notes": "Stream definition at different thresholds",
    },
    "fig_11_04": {
        "sources": [("ExtendedTerrainAnalysis", "slide47_img068.png")],
        "confidence": "high",
        "notes": "Peuker-Douglas curvature computation",
    },
    "fig_11_05": {
        "sources": [("ExtendedTerrainAnalysis", "slide38_img064.png")],
        "confidence": "high",
        "notes": "Strahler stream ordering",
    },
    # Chapter 12
    "fig_12_01": {
        "sources": [
            ("Programming", "slide02_img001.png"),
            ("Programming", "slide02_img002.png"),
        ],
        "confidence": "high",
        "notes": "Manual vs scripted workflow advantage",
    },
    # Chapter 13
    "fig_13_02": {
        "sources": [
            ("LIDAR", "slide09_img009.png"),
            ("LIDAR", "slide10_img010.png"),
        ],
        "confidence": "high",
        "notes": "Linear mode vs Geiger mode LiDAR",
    },
    "fig_13_06": {
        "sources": [("LIDAR", "slide56_img098.tiff")],
        "confidence": "high",
        "notes": "National HAND map for CONUS",
    },
    # Chapter 14
    "fig_14_01": {
        "sources": [("NWMFlood", "slide34_img086.png")],
        "confidence": "high",
        "notes": "HAND concept cross-section with flood level",
    },
    "fig_14_02": {
        "sources": [
            ("HAND", "slide14_img021.png"),
            ("HAND", "slide14_img022.png"),
        ],
        "confidence": "high",
        "notes": "HAND algorithm step-by-step on grid",
    },
    "fig_14_03": {
        "sources": [("HAND", "slide17_img026.png")],
        "confidence": "high",
        "notes": "HAND raster for Onion Creek, Austin TX",
    },
    "fig_14_04": {
        "sources": [("HAND", "slide49_img080.tiff")],
        "confidence": "high",
        "notes": "Continental US HAND map at 10m resolution",
    },
    # Chapter 15
    "fig_15_01": {
        "sources": [
            ("HAND", "slide05_img001.png"),
            ("HAND", "slide05_img002.png"),
            ("HAND", "slide05_img003.png"),
            ("HAND", "slide05_img004.png"),
        ],
        "confidence": "high",
        "notes": "Four-step flood inundation mapping pipeline",
    },
    # Chapter 16
    "fig_16_02": {
        "sources": [
            ("NWMFlood", "slide24_img055.png"),
            ("NWMFlood", "slide24_img058.png"),
        ],
        "confidence": "high",
        "notes": "National Water Model / WRF-Hydro architecture",
    },
    "fig_16_03": {
        "sources": [
            ("NWMFlood", "slide38_img097.png"),
            ("NWMFlood", "slide38_img098.png"),
        ],
        "confidence": "high",
        "notes": "Harvey forecast vs actual damage comparison",
    },
    "fig_16_06": {
        "sources": [
            ("NWMFlood", "slide48_img128.png"),
            ("NWMFlood", "slide48_img129.png"),
            ("NWMFlood", "slide48_img130.png"),
        ],
        "confidence": "high",
        "notes": "Three-tier flood observation architecture",
    },
    # Chapter 17
    "fig_17_05": {
        "sources": [
            ("Demography2018", "slide22_img034.png"),
            ("Demography2018", "slide24_img036.png"),
            ("Demography2018", "slide27_img039.png"),
            ("Demography2018", "slide29_img041.png"),
        ],
        "confidence": "high",
        "notes": "Travis County demographic maps (income, age, growth, income)",
    },
}

# Medium confidence matches (copy but flag for review)
MEDIUM_MATCHES = {
    "fig_01_03": {
        "sources": [
            ("Lecture12018", "slide32_img045.png"),
            ("Lecture12018", "slide32_img046.png"),
            ("Lecture12018", "slide32_img047.png"),
        ],
        "confidence": "medium",
        "notes": "Three GIS views icons; needs compositing",
    },
    "fig_01_04": {
        "sources": [
            ("Lecture12018", "slide18_img022.jpg"),
            ("Lecture12018", "slide18_img023.jpg"),
            ("Lecture12018", "slide18_img024.jpg"),
            ("Lecture12018", "slide18_img025.png"),
        ],
        "confidence": "medium",
        "notes": "Four water problems photos; needs compositing",
    },
    "fig_02_03": {
        "sources": [("MapProj", "slide47_img059.png")],
        "confidence": "medium",
        "notes": "Vertical datum differences (US, not Europe)",
    },
    "fig_03_02": {
        "sources": [("DataSources2018", "slide08_img007.png")],
        "confidence": "medium",
        "notes": "NHDPlus river networks (US only)",
    },
    "fig_04_01": {
        "sources": [
            ("Lecture12018", "slide34_img053.png"),
            ("Lecture12018", "slide35_img056.png"),
            ("Lecture12018", "slide36_img059.png"),
        ],
        "confidence": "medium",
        "notes": "Three views of GIS; data, vector, raster slides",
    },
    "fig_05_01": {
        "sources": [("DataSources2018", "slide17_img025.png")],
        "confidence": "medium",
        "notes": "DEM from contours; shows grid concept only",
    },
    "fig_07_01": {
        "sources": [("Ex3Overview", "slide02_img001.png")],
        "confidence": "medium",
        "notes": "Slope and aspect concept (partial)",
    },
    "fig_08_04": {
        "sources": [
            ("Ex3Overview", "slide11_img003.png"),
            ("Ex3Overview", "slide12_img004.png"),
            ("Ex3Overview", "slide12_img005.png"),
            ("Ex3Overview", "slide12_img006.png"),
            ("Ex3Overview", "slide12_img007.png"),
        ],
        "confidence": "medium",
        "notes": "Thiessen polygon workflow steps",
    },
    "fig_10_06": {
        "sources": [("LIDAR", "slide53_img091.png")],
        "confidence": "medium",
        "notes": "TWI map (Eel River, not book's target area)",
    },
    "fig_12_02": {
        "sources": [("Programming", "slide04_img004.png")],
        "confidence": "medium",
        "notes": "ArcGIS Pro geoprocessing help page",
    },
    "fig_12_04": {
        "sources": [
            ("DemWatershedDelineation", "slide39_img039.png"),
            ("DemWatershedDelineation", "slide39_img040.png"),
        ],
        "confidence": "medium",
        "notes": "TauDEM architecture (partial)",
    },
    "fig_13_04": {
        "sources": [
            ("LIDAR", "slide32_img041.tiff"),
            ("LIDAR", "slide33_img042.tiff"),
        ],
        "confidence": "medium",
        "notes": "DSM and DEM from LiDAR (West Maui, different location)",
    },
    "fig_13_05": {
        "sources": [("LIDAR", "slide21_img017.jpg")],
        "confidence": "medium",
        "notes": "Bathymetric LiDAR Snell's Law diagram",
    },
    "fig_15_03": {
        "sources": [("HAND", "slide31_img045.png")],
        "confidence": "medium",
        "notes": "Reach-averaged hydraulic properties",
    },
    "fig_15_04": {
        "sources": [("HAND", "slide35_img054.png")],
        "confidence": "medium",
        "notes": "Onion Creek reach catchment example",
    },
    "fig_17_02": {
        "sources": [("Demography2018", "slide04_img001.png")],
        "confidence": "medium",
        "notes": "Census geographic hierarchy (US only)",
    },
    "fig_17_04": {
        "sources": [
            ("Demography2018", "slide43_img061.png"),
            ("Demography2018", "slide43_img062.png"),
            ("Demography2018", "slide43_img063.png"),
        ],
        "confidence": "medium",
        "notes": "Clip function for population (partial match)",
    },
    "fig_01_05": {
        "sources": [("Maidment", "slide08_img008.png")],
        "confidence": "medium",
        "notes": "NDVI Texas drought; single image, not side-by-side comparison",
    },
}


def copy_images():
    """Copy matched images to book directory."""
    copied = 0
    skipped = 0
    errors = 0

    all_matches = {}
    all_matches.update(MATCHES)
    all_matches.update(MEDIUM_MATCHES)

    for fig_id, info in sorted(all_matches.items()):
        sources = info["sources"]
        confidence = info["confidence"]
        notes = info["notes"]

        if len(sources) == 1:
            # Single source image - copy directly
            ppt_folder, filename = sources[0]
            src = PPT_BASE / ppt_folder / filename
            # Determine output extension
            ext = Path(filename).suffix
            dst = BOOK_DIR / f"{fig_id}{ext}"

            if src.exists():
                shutil.copy2(src, dst)
                print(f"  COPIED [{confidence}] {fig_id}{ext} <- {ppt_folder}/{filename}")
                copied += 1
            else:
                print(f"  ERROR  {fig_id} - Source not found: {src}")
                errors += 1
        else:
            # Multiple source images - copy all with suffixes
            for i, (ppt_folder, filename) in enumerate(sources):
                src = PPT_BASE / ppt_folder / filename
                ext = Path(filename).suffix
                suffix = chr(ord('a') + i)  # a, b, c, ...
                dst = BOOK_DIR / f"{fig_id}_{suffix}{ext}"

                if src.exists():
                    shutil.copy2(src, dst)
                    print(f"  COPIED [{confidence}] {fig_id}_{suffix}{ext} <- {ppt_folder}/{filename}")
                    copied += 1
                else:
                    print(f"  ERROR  {fig_id}_{suffix} - Source not found: {src}")
                    errors += 1
            print(f"  NOTE:  {fig_id} needs compositing: {notes}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Copied:  {copied} files")
    print(f"  Errors:  {errors} files")
    print(f"  Output:  {BOOK_DIR}")
    print(f"\nFigures NOT copied (need AI generation): 107 figures")
    print(f"Figures NOT copied (need book PDF extraction): 4 figures")
    print(f"  - Fig 13.3: Drone LiDAR vs SfM")
    print(f"  - Fig 23.5: U-Net architecture")
    print(f"  - Fig 23.8: GEE + Python ML integration")
    print(f"  - Fig 25.5: Foundation model workflow")


if __name__ == "__main__":
    print(f"Copying matched PPT images to {BOOK_DIR}\n")
    copy_images()
