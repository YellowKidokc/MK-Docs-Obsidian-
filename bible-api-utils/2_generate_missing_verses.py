#!/usr/bin/env python3
"""
Generate missing_verses.sql containing only verses not yet loaded into D1.

This script:
1. Reads the master verses.sql file
2. Reads the list of loaded verse UIDs from D1
3. Generates a new SQL file with only missing verses
"""

from pathlib import Path
import re

def extract_uid_from_insert(line):
    """Extract UID from an INSERT statement"""
    # Match pattern: INSERT INTO verses VALUES ('UID', ...
    match = re.search(r"INSERT INTO verses VALUES \('([^']+)'", line)
    return match.group(1) if match else None

def main():
    # File paths
    master_sql = Path("data/verses.sql")
    loaded_uids_file = Path("loaded_verse_uids.txt")
    output_sql = Path("data/missing_verses.sql")

    print("📖 Reading master verses.sql file...")
    if not master_sql.exists():
        print(f"❌ Error: {master_sql} not found!")
        print("   Make sure you're running this from the Cloudflare_D1 directory")
        return

    with open(master_sql, 'r', encoding='utf-8') as f:
        master_lines = f.readlines()

    print(f"   Found {len(master_lines)} lines in master file")

    # Extract all verse INSERT statements with their UIDs
    master_verses = {}
    for line in master_lines:
        if line.strip().startswith("INSERT INTO verses VALUES"):
            uid = extract_uid_from_insert(line)
            if uid:
                master_verses[uid] = line

    print(f"   Parsed {len(master_verses)} verse INSERT statements")

    # Read loaded UIDs from D1
    print("\n📊 Reading loaded verse UIDs from D1 export...")
    if not loaded_uids_file.exists():
        print(f"❌ Error: {loaded_uids_file} not found!")
        print("   Run 1_export_loaded_verses.sh first")
        return

    with open(loaded_uids_file, 'r', encoding='utf-8') as f:
        loaded_content = f.read()

    # Parse UIDs from wrangler output (skip header rows)
    loaded_uids = set()
    for line in loaded_content.split('\n'):
        line = line.strip()
        # Skip empty lines, header lines, and separator lines
        if (line and
            not line.startswith('│') and
            not line.startswith('┌') and
            not line.startswith('├') and
            not line.startswith('└') and
            not line == 'uid' and
            not line.startswith('-')):
            # Clean the UID (remove table formatting)
            uid = line.replace('│', '').strip()
            if uid and len(uid) > 5:  # Basic validation
                loaded_uids.add(uid)

    print(f"   Found {len(loaded_uids)} verses already loaded in D1")

    # Find missing verses
    print("\n🔍 Identifying missing verses...")
    missing_uids = set(master_verses.keys()) - loaded_uids
    print(f"   Found {len(missing_uids)} missing verses")

    if not missing_uids:
        print("\n✅ All verses are already loaded! Nothing to do.")
        return

    # Generate missing_verses.sql
    print(f"\n📝 Generating {output_sql}...")
    missing_lines = [master_verses[uid] for uid in sorted(missing_uids)]

    with open(output_sql, 'w', encoding='utf-8') as f:
        f.write("-- Missing verses to be imported into D1\n")
        f.write(f"-- Generated from verses.sql\n")
        f.write(f"-- Contains {len(missing_uids)} verses\n\n")
        f.writelines(missing_lines)

    print(f"   ✓ Created {output_sql}")
    print(f"   ✓ Contains {len(missing_uids)} INSERT statements")

    # Calculate file size
    file_size_mb = output_sql.stat().st_size / (1024 * 1024)
    print(f"   ✓ File size: {file_size_mb:.2f} MB")

    # Check if we need to split the file
    if file_size_mb > 1.0:
        print(f"\n⚠️  File is {file_size_mb:.2f} MB - may need to split into chunks")
        print("   Run 3_split_missing_verses.py if import fails")
    else:
        print(f"\n✅ File is small enough ({file_size_mb:.2f} MB) - ready to import!")

    print("\n📊 Summary:")
    print(f"   Total verses in master: {len(master_verses)}")
    print(f"   Already loaded in D1:   {len(loaded_uids)}")
    print(f"   Missing verses:         {len(missing_uids)}")
    print(f"   Completion percentage:  {len(loaded_uids) / len(master_verses) * 100:.1f}%")

    print("\n✨ Next step: Run 4_import_missing_verses.sh to load the missing verses")

if __name__ == "__main__":
    main()
