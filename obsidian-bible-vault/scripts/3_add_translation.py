#!/usr/bin/env python3
"""
Add a new Bible translation to the SQLite database.

This script allows you to import additional Bible translations while
maintaining unified verse IDs based on the KJV structure.

Usage:
    python 3_add_translation.py --translation ESV --file esv_verses.csv
"""

import sqlite3
import csv
import argparse
from pathlib import Path

def validate_verse_uid(uid: str) -> bool:
    """Validate verse UID format (e.g., GN-01-01-AA)"""
    parts = uid.split('-')
    return len(parts) == 4 and len(parts[0]) <= 3 and parts[1].isdigit() and parts[2].isdigit()

def add_translation(db_path: Path, translation_code: str, input_file: Path):
    """
    Add a new translation to the database.

    Expected CSV format:
    uid,text
    GN-01-01-AA,"In the beginning God created..."
    GN-01-02-AA,"And the earth was..."
    """
    print(f"📖 Adding {translation_code} translation to database...")
    print("=" * 60)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if translation already exists
    cursor.execute("""
        SELECT COUNT(*) FROM verses WHERE translation = ?
    """, (translation_code,))

    existing_count = cursor.fetchone()[0]
    if existing_count > 0:
        print(f"\n⚠️  Translation {translation_code} already exists with {existing_count} verses")
        response = input("Do you want to replace it? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            return

        # Delete existing translation
        cursor.execute("DELETE FROM verses WHERE translation = ?", (translation_code,))
        conn.commit()
        print(f"   Deleted {existing_count} existing verses")

    # Read CSV file
    print(f"\n📂 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        verses = list(reader)

    print(f"   Found {len(verses)} verses")

    # Validate UIDs
    print("\n🔍 Validating verse UIDs...")
    invalid_count = 0
    for verse in verses:
        if not validate_verse_uid(verse['uid']):
            print(f"   ⚠️  Invalid UID: {verse['uid']}")
            invalid_count += 1

    if invalid_count > 0:
        print(f"\n❌ Found {invalid_count} invalid UIDs. Please fix and try again.")
        return

    print("   ✓ All UIDs valid")

    # Insert verses
    print(f"\n💾 Inserting verses into database...")
    inserted = 0
    skipped = 0

    for verse in verses:
        uid = verse['uid']
        text = verse['text']

        # Get book/chapter/verse from existing KJV entry
        cursor.execute("""
            SELECT book_code, chapter_num, verse_num
            FROM verses
            WHERE uid = ? AND translation = 'KJV'
        """, (uid,))

        result = cursor.fetchone()
        if not result:
            print(f"   ⚠️  Skipping {uid} - not found in KJV (base translation)")
            skipped += 1
            continue

        book_code, chapter_num, verse_num = result

        # Insert new translation
        cursor.execute("""
            INSERT INTO verses (uid, translation, book_code, chapter_num, verse_num, text)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (uid, translation_code, book_code, chapter_num, verse_num, text))

        inserted += 1

        if inserted % 1000 == 0:
            print(f"   Inserted {inserted:,} verses...")

    conn.commit()

    # Update metadata
    cursor.execute("SELECT value FROM metadata WHERE key = 'translations'")
    result = cursor.fetchone()

    if result:
        import json
        translations = json.loads(result[0])
        if translation_code not in translations:
            translations.append(translation_code)
            cursor.execute("""
                UPDATE metadata SET value = ? WHERE key = 'translations'
            """, (json.dumps(translations),))
    else:
        import json
        cursor.execute("""
            INSERT INTO metadata (key, value) VALUES ('translations', ?)
        """, (json.dumps(['KJV', translation_code]),))

    conn.commit()
    conn.close()

    # Summary
    print("\n" + "=" * 60)
    print("✅ Translation added successfully!")
    print(f"\n📊 Statistics:")
    print(f"   Inserted: {inserted:,} verses")
    print(f"   Skipped:  {skipped:,} verses")
    print(f"\n💡 Translation code: {translation_code}")
    print(f"   Users can now select this translation in Obsidian")

def export_template(output_file: Path):
    """Export a CSV template for adding translations"""
    print(f"📄 Creating template file: {output_file}")

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['uid', 'text'])
        writer.writerow(['GN-01-01-AA', 'In the beginning God created the heaven and the earth.'])
        writer.writerow(['GN-01-02-AA', 'And the earth was without form, and void; and darkness was upon the face of the deep.'])

    print(f"   ✓ Template created")
    print("\n💡 Fill in this CSV with your translation verses")
    print("   UID must match KJV structure (book-chapter-verse-variant)")

def main():
    parser = argparse.ArgumentParser(description='Add Bible translation to SQLite database')
    parser.add_argument('--db', default='obsidian-bible.db', help='SQLite database file')
    parser.add_argument('--translation', help='Translation code (e.g., ESV, NIV, NASB)')
    parser.add_argument('--file', help='Input CSV file with verses')
    parser.add_argument('--template', action='store_true', help='Create a template CSV file')

    args = parser.parse_args()

    if args.template:
        export_template(Path('translation_template.csv'))
        return

    if not args.translation or not args.file:
        parser.print_help()
        print("\n💡 Examples:")
        print("   python 3_add_translation.py --translation ESV --file esv.csv")
        print("   python 3_add_translation.py --template")
        return

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        print("   Run 1_export_to_sqlite.py first")
        return

    input_file = Path(args.file)
    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        return

    add_translation(db_path, args.translation, input_file)

if __name__ == "__main__":
    main()
