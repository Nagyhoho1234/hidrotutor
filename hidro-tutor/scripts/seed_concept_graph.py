#!/usr/bin/env python3
"""CLI script to display and verify the concept graph.

Usage:
    cd hidro-tutor
    python -m scripts.seed_concept_graph
"""

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from backend.rag.concept_graph import CONCEPT_GRAPH, get_prerequisites


def main():
    print("=" * 60)
    print("Hidro-Tutor Concept Graph")
    print(f"Total concepts: {len(CONCEPT_GRAPH)}")
    print("=" * 60)

    # Group by chapter
    by_chapter: dict[int, list] = {}
    for key, concept in CONCEPT_GRAPH.items():
        ch = concept.chapter
        if ch not in by_chapter:
            by_chapter[ch] = []
        by_chapter[ch].append((key, concept))

    for ch_num in sorted(by_chapter.keys()):
        items = by_chapter[ch_num]
        print(f"\nChapter {ch_num}:")
        for key, concept in items:
            prereqs = concept.prerequisites
            prereq_str = f" <- [{', '.join(prereqs)}]" if prereqs else ""
            print(f"  {concept.section:8s} {concept.name}{prereq_str}")

    # Show a full prerequisite chain example
    print("\n" + "=" * 60)
    print("Example: Full prerequisites for 'digital_twins':")
    chain = get_prerequisites("digital_twins")
    for i, c in enumerate(chain, 1):
        print(f"  {i}. {c} (Ch. {CONCEPT_GRAPH[c].chapter})")


if __name__ == "__main__":
    main()
