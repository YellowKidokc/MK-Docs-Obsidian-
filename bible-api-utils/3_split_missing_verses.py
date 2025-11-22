#!/usr/bin/env python3
"""
Split missing_verses.sql into smaller chunks if needed for D1 import.
Only run this if missing_verses.sql is too large (>1 MB).
"""

from pathlib import Path

def main():
    input_file = Path("data/missing_verses.sql")
    chunks_dir = Path("data/missing_verses_chunks")

    if not input_file.exists():
        print("❌ Error: data/missing_verses.sql not found!")
        print("   Run 2_generate_missing_verses.py first")
        return

    # Read the file
    print(f"📖 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Filter out comment lines
    insert_lines = [line for line in lines if line.strip().startswith("INSERT INTO verses")]

    file_size_mb = input_file.stat().st_size / (1024 * 1024)
    print(f"   File size: {file_size_mb:.2f} MB")
    print(f"   Insert statements: {len(insert_lines)}")

    # Create chunks directory
    chunks_dir.mkdir(exist_ok=True)

    # Split into chunks of 500 verses each (safe for D1)
    chunk_size = 500
    num_chunks = (len(insert_lines) + chunk_size - 1) // chunk_size

    print(f"\n✂️  Splitting into {num_chunks} chunks of ~{chunk_size} verses each...")

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(insert_lines))
        chunk_lines = insert_lines[start_idx:end_idx]

        chunk_file = chunks_dir / f"missing_verses_part_{i+1:03d}.sql"
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.write(f"-- Missing verses chunk {i+1} of {num_chunks}\n")
            f.write(f"-- Verses {start_idx + 1} to {end_idx}\n\n")
            f.writelines(chunk_lines)

        print(f"   Created {chunk_file.name} ({len(chunk_lines)} verses)")

    print(f"\n✅ Split complete! Created {num_chunks} chunk files")
    print(f"   Location: {chunks_dir}/")
    print("\n✨ Next step: Run 5_import_missing_chunks.sh to load all chunks")

if __name__ == "__main__":
    main()
