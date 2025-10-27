#!/usr/bin/env python3
"""
Export PostgreSQL Bible database to SQLite for Obsidian.

This creates a single SQLite file that Obsidian can query using the Dataview plugin.
Supports multiple Bible translations with unified verse IDs.
"""

import sqlite3
import psycopg2
from pathlib import Path
import json

def create_sqlite_schema(conn):
    """Create SQLite tables matching PostgreSQL structure"""
    cursor = conn.cursor()

    # Books table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        uid TEXT PRIMARY KEY,
        book_code TEXT UNIQUE NOT NULL,
        book_name TEXT NOT NULL,
        testament TEXT,
        book_order INTEGER
    )
    """)

    # Verses table (supports multiple translations)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS verses (
        uid TEXT NOT NULL,
        translation TEXT NOT NULL DEFAULT 'KJV',
        book_code TEXT NOT NULL,
        chapter_num INTEGER NOT NULL,
        verse_num INTEGER NOT NULL,
        text TEXT NOT NULL,
        PRIMARY KEY (uid, translation),
        FOREIGN KEY (book_code) REFERENCES books(book_code)
    )
    """)

    # Entities table (people, places)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entities (
        uid TEXT PRIMARY KEY,
        entity_name TEXT NOT NULL,
        entity_type TEXT,
        description TEXT,
        metadata TEXT
    )
    """)

    # Topics table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        uid TEXT PRIMARY KEY,
        topic_name TEXT NOT NULL,
        category TEXT,
        description TEXT
    )
    """)

    # Lexicon table (Strong's numbers)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lexicon (
        uid TEXT PRIMARY KEY,
        strongs_number TEXT,
        word TEXT,
        transliteration TEXT,
        pronunciation TEXT,
        definition TEXT,
        language TEXT
    )
    """)

    # Relationships table (verse -> entity/topic/lexicon)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relationships (
        verse_uid TEXT NOT NULL,
        target_uid TEXT NOT NULL,
        relationship_type TEXT NOT NULL,
        context TEXT,
        PRIMARY KEY (verse_uid, target_uid, relationship_type)
    )
    """)

    # Create indexes for performance
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_book ON verses(book_code)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_chapter ON verses(chapter_num)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_translation ON verses(translation)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_entities_type ON entities(entity_type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_relationships_verse ON relationships(verse_uid)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_relationships_target ON relationships(target_uid)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(relationship_type)")

    conn.commit()
    print("✓ SQLite schema created")

def copy_table_data(pg_cursor, sqlite_conn, table_name, columns):
    """Copy data from PostgreSQL to SQLite"""
    print(f"\n📋 Copying {table_name}...")

    # Fetch from PostgreSQL
    pg_cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name}")
    rows = pg_cursor.fetchall()

    if not rows:
        print(f"   ⚠️  No data in {table_name}")
        return

    # Insert into SQLite
    placeholders = ', '.join(['?' for _ in columns])
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.executemany(
        f"INSERT OR REPLACE INTO {table_name} VALUES ({placeholders})",
        rows
    )
    sqlite_conn.commit()

    print(f"   ✓ Copied {len(rows):,} rows")

def main():
    # Configuration
    pg_config = {
        'host': 'localhost',
        'database': 'bible_database',
        'user': 'postgres',
        'password': 'your_password'
    }

    output_file = Path("obsidian-bible.db")

    print("🔄 Exporting PostgreSQL Bible database to SQLite...")
    print("=" * 60)

    # Connect to PostgreSQL
    print("\n📡 Connecting to PostgreSQL...")
    try:
        pg_conn = psycopg2.connect(**pg_config)
        pg_cursor = pg_conn.cursor()
        print("   ✓ Connected")
    except Exception as e:
        print(f"   ❌ Failed to connect: {e}")
        print("\n💡 Update pg_config in this script with your database credentials")
        return

    # Create SQLite database
    print(f"\n📝 Creating SQLite database: {output_file}")
    sqlite_conn = sqlite3.connect(output_file)
    create_sqlite_schema(sqlite_conn)

    # Copy data
    tables = {
        'books': ['uid', 'book_code', 'book_name', 'testament', 'book_order'],
        'verses': ['uid', 'book_code', 'chapter_num', 'verse_num', 'text'],
        'entities': ['uid', 'entity_name', 'entity_type', 'description'],
        'topics': ['uid', 'topic_name', 'category', 'description'],
        'lexicon': ['uid', 'strongs_number', 'word', 'transliteration',
                   'pronunciation', 'definition', 'language'],
        'relationships': ['verse_uid', 'target_uid', 'relationship_type', 'context']
    }

    for table_name, columns in tables.items():
        try:
            copy_table_data(pg_cursor, sqlite_conn, table_name, columns)
        except Exception as e:
            print(f"   ❌ Error: {e}")

    # Add metadata table
    print("\n📊 Adding metadata...")
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute("""
    CREATE TABLE IF NOT EXISTS metadata (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # Get statistics
    stats = {}
    for table_name in tables.keys():
        sqlite_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        stats[table_name] = sqlite_cursor.fetchone()[0]

    # Store metadata
    import datetime
    metadata = {
        'export_date': datetime.datetime.now().isoformat(),
        'source': 'PostgreSQL Bible Database',
        'default_translation': 'KJV',
        'translations': json.dumps(['KJV']),  # Will expand for multiple translations
        'statistics': json.dumps(stats)
    }

    for key, value in metadata.items():
        sqlite_cursor.execute(
            "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
            (key, value)
        )

    sqlite_conn.commit()
    print("   ✓ Metadata added")

    # Summary
    print("\n" + "=" * 60)
    print("✅ Export Complete!")
    print(f"\n📄 Output: {output_file.absolute()}")
    print(f"📊 Statistics:")
    for table_name, count in stats.items():
        print(f"   {table_name:20s}: {count:,}")

    file_size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"\n💾 Database size: {file_size_mb:.2f} MB")

    # Close connections
    pg_cursor.close()
    pg_conn.close()
    sqlite_conn.close()

    print("\n✨ Next step: Run 2_generate_markdown_vault.py to create Obsidian vault")

if __name__ == "__main__":
    main()
