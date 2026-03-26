#!/usr/bin/env python3
"""CLI script to ingest book chapters into ChromaDB.

Usage:
    cd hidro-tutor
    python -m scripts.ingest_book
    python -m scripts.ingest_book --chapters-dir ../chapters_v2
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from backend.rag.ingest import ingest_chapters, ingest_hungarian
from backend.config import settings


def main():
    parser = argparse.ArgumentParser(description="Ingest book chapters into vector store")
    parser.add_argument(
        "--chapters-dir",
        type=str,
        default=None,
        help=f"Path to chapters directory (default: {settings.chapters_path})",
    )
    parser.add_argument(
        "--chroma-dir",
        type=str,
        default=None,
        help=f"Path to ChromaDB storage (default: {settings.chroma_db_path})",
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        choices=["en", "hu"],
        help="Language to ingest: 'en' (default) or 'hu' (Hungarian)",
    )
    args = parser.parse_args()

    chapters_dir = Path(args.chapters_dir) if args.chapters_dir else None
    chroma_dir = Path(args.chroma_dir) if args.chroma_dir else None

    if args.lang == "hu":
        stats = ingest_hungarian(chapters_dir=chapters_dir, chroma_dir=chroma_dir)
    else:
        stats = ingest_chapters(chapters_dir=chapters_dir, chroma_dir=chroma_dir)

    print("\n--- Ingestion Summary ---")
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
