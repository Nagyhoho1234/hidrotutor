"""Generate a single chapter using the chapter prompt template.
Self-contained — reads all paths relative to this script.

Usage:
  python generate_chapter.py 1    # Generate chapter 1
  python generate_chapter.py all  # Generate all chapters (sequentially)
  python generate_chapter.py 1-5  # Generate chapters 1 through 5

This script prints the full prompt to stdout. Pipe it to your AI tool of choice:
  python generate_chapter.py 1 > prompt_ch01.txt

Or use it as a template for batch processing with the Claude API / Codex.
"""
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CHAPTER_MAP = {
    1:  ("Why Hidroinformatics Matters", "ch01_introduction_to_gis.md", "Introduction to the field, water crises, the convergence of hydrology + GIS + AI"),
    2:  ("Mapping Water: From Paper to Pixels", "ch02_geodesy_projections_coordinates.md", "Coordinate systems, projections, datums — accessible treatment with US/EU/Hungarian examples"),
    3:  ("Where the Data Lives", "ch04_data_sources.md", "Global tour of water data sources: US, EU/Hungary, Asia/Africa"),
    4:  ("GIS as a Water Tool", "ch03_working_with_gis_software.md", "What GIS does for hydrology, from desktop to cloud"),
    5:  ("The Grid: How Computers See Terrain", "ch05_raster_data_fundamentals.md", "Raster fundamentals, DEMs, resolution trade-offs"),
    6:  ("Calculating with Maps", "ch06_map_algebra.md", "Map algebra, combining layers"),
    7:  ("Slope, Aspect, and the Shape of the Land", "ch07_slope_and_aspect.md", "D8, D-infinity, terrain derivatives"),
    8:  ("Measuring Rain Where It Falls", "ch08_spatial_interpolation.md", "Interpolation, rain gauges vs radar vs satellite"),
    9:  ("Preparing the Digital Landscape", "ch09_dem_hydrologic_conditioning.md", "DEM conditioning, pit filling, stream burning"),
    10: ("Which Way Does Water Flow?", "ch10_flow_direction_accumulation.md", "Flow direction, accumulation, digital river network"),
    11: ("Drawing Watersheds from Data", "ch11_stream_network_watershed_delineation.md", "Automated watershed delineation"),
    12: ("Automating the Workflow", "ch12_python_programming.md", "Python scripting for GIS automation"),
    13: ("Seeing the Ground in 3D: LiDAR", "ch13_lidar.md", "LiDAR technology and high-resolution terrain"),
    14: ("How High Above the River?", "ch14_hand.md", "The HAND concept for flood-prone terrain identification"),
    15: ("Mapping Where Floods Go", "ch15_flood_inundation_mapping.md", "Inundation mapping, rating curves, damage estimation"),
    16: ("Forecasting Floods in Real Time", "ch16_flood_response_nwm.md", "NWM, EFAS, GloFAS, Hungarian operational systems"),
    17: ("Who Lives in the Flood Zone?", "ch17_demography.md", "Population exposure, building databases, emergency response"),
    18: ("Seeing Underground: 3D Subsurface GIS", None, "3D GIS for subsurface — from Arc Hydro GW Ch 3"),
    19: ("Wells, Boreholes, and Aquifer Maps", None, "Groundwater data — from Arc Hydro GW Ch 4-5"),
    20: ("Building a Picture of the Underground", None, "Hydrogeologic framework — from Arc Hydro GW Ch 6"),
    21: ("Simulating Groundwater Flow", None, "MODFLOW and GIS — from Arc Hydro GW Ch 8"),
    22: ("When Models Meet Data", None, "The calibration problem, traditional optimization"),
    23: ("AI as a Hydrologist's Assistant", None, "Practical ML for water: LSTM, satellite ET, GW forecasting"),
    24: ("Agentic AI: The Autonomous Modeler", None, "AI agents for hydrological model parameterization"),
    25: ("The Future of Water Intelligence", None, "Digital twins, real-time assimilation, climate adaptation"),
}


def build_prompt(ch_num):
    """Build the full prompt for generating a chapter."""
    title, source_file, description = CHAPTER_MAP[ch_num]

    # Read the chapter prompt template
    prompt_path = os.path.join(SCRIPT_DIR, "chapter_prompt.md")
    with open(prompt_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Build source material references
    sources = []
    if source_file:
        sources.append(f"- Lecture notes (v1): C:/maidment_hidroGIS/lecture_notes/{source_file}")

    # Add Arc Hydro GW sources for Part V
    arc_hydro_map = {
        18: "ch03_3d_subsurface.md",
        19: "ch04_geologic_maps.md, ch05_aquifers_wells.md",
        20: "ch06_hydrostratigraphy.md",
        21: "ch08_gw_simulation.md",
    }
    if ch_num in arc_hydro_map:
        sources.append(f"- Arc Hydro GW: C:/maidment_hidroGIS/books/arc_hydro_gw/{arc_hydro_map[ch_num]}")

    # Add handbook references for Part VI
    handbook_map = {
        22: "vol3_part03 (HEC-HMS), vol3_part08 (data assimilation)",
        23: "vol2_part01-04 (ML methods), vol3_part11 (GIS flood mapping)",
        24: "New content — agentic AI for model parameterization",
        25: "Synthesis chapter",
    }
    if ch_num in handbook_map:
        sources.append(f"- Handbook reference: {handbook_map[ch_num]}")

    sources.append("- International data: C:/maidment_hidroGIS/Hungarian_EU_Data_Sources.md")
    sources.append("- Global data: C:/maidment_hidroGIS/international_data_sources.md")
    sources.append("- Internationalization guide: C:/maidment_hidroGIS/INTERNATIONALIZATION_PROMPT.md")

    source_text = "\n".join(sources)

    specific = f"""
CHAPTER-SPECIFIC INSTRUCTION:
- Chapter number and title: Chapter {ch_num}: {title}
- Source materials:
{source_text}
- Output file: C:/maidment_hidroGIS/chapters_v2/ch{ch_num:02d}.md
- Content description: {description}

TASK:
1. Read the source material as a starting point — don't copy, develop further into book-quality prose
2. Read the BOOK_CONCEPT_2026.md for the overall vision
3. Read the internationalization guide for this chapter's specific requirements
4. Write the chapter to chapters_v2/ch{ch_num:02d}.md
5. Check: any 5-line subsections? Unexpanded lists? Unnumbered tables? Figure placeholders? International content?
"""

    return template + "\n\n---\n\n" + specific


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_chapter.py <chapter_number|all|range>")
        print("  python generate_chapter.py 1")
        print("  python generate_chapter.py 1-5")
        print("  python generate_chapter.py all")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "all":
        chapters = list(range(1, 26))
    elif "-" in arg:
        start, end = arg.split("-")
        chapters = list(range(int(start), int(end) + 1))
    else:
        chapters = [int(arg)]

    for ch in chapters:
        if ch not in CHAPTER_MAP:
            print(f"ERROR: Chapter {ch} not in chapter map (valid: 1-25)", file=sys.stderr)
            continue

        prompt = build_prompt(ch)

        if len(chapters) == 1:
            # Single chapter — print to stdout
            print(prompt)
        else:
            # Multiple chapters — save to files
            out = os.path.join(SCRIPT_DIR, f"prompt_ch{ch:02d}.txt")
            with open(out, 'w', encoding='utf-8') as f:
                f.write(prompt)
            print(f"  Saved: {out}")


if __name__ == '__main__':
    main()
