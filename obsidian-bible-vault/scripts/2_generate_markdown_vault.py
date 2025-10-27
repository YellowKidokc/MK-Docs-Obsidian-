#!/usr/bin/env python3
"""
Generate Obsidian Markdown vault from SQLite Bible database.

Creates a hierarchical vault structure:
- Bible/
  - Genesis/
    - Chapter 1.md
    - Chapter 2.md
  - Exodus/
    ...
- Entities/
  - People/
  - Places/
- Topics/
- Lexicon/

Each verse has embedded metadata for Dataview queries.
"""

import sqlite3
from pathlib import Path
import json
from typing import Dict, List, Any

class ObsidianBibleVaultGenerator:
    def __init__(self, db_path: Path, output_dir: Path):
        self.db_path = db_path
        self.output_dir = output_dir
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def generate_vault(self):
        """Generate complete Obsidian vault"""
        print("📖 Generating Obsidian Bible Vault...")
        print("=" * 60)

        # Create directory structure
        self.create_directories()

        # Generate Bible chapters
        self.generate_bible_chapters()

        # Generate entity pages
        self.generate_entity_pages()

        # Generate topic pages
        self.generate_topic_pages()

        # Generate lexicon pages
        self.generate_lexicon_pages()

        # Generate index pages
        self.generate_index_pages()

        # Copy CSS and templates
        self.copy_assets()

        print("\n" + "=" * 60)
        print("✅ Vault generation complete!")
        print(f"\n📁 Location: {self.output_dir.absolute()}")
        print("\n✨ Open this folder in Obsidian to start using your Bible vault!")

    def create_directories(self):
        """Create vault directory structure"""
        print("\n📁 Creating directory structure...")

        dirs = [
            "Bible",
            "Entities/People",
            "Entities/Places",
            "Topics",
            "Lexicon",
            "Notes",
            ".obsidian/snippets",
            "Templates"
        ]

        for dir_path in dirs:
            (self.output_dir / dir_path).mkdir(parents=True, exist_ok=True)

        print("   ✓ Directories created")

    def generate_bible_chapters(self):
        """Generate Markdown files for each Bible chapter"""
        print("\n📖 Generating Bible chapters...")

        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT DISTINCT book_code, book_name
            FROM books
            ORDER BY book_order
        """)
        books = cursor.fetchall()

        total_chapters = 0
        for book in books:
            book_code = book['book_code']
            book_name = book['book_name']

            # Create book directory
            book_dir = self.output_dir / "Bible" / book_name
            book_dir.mkdir(exist_ok=True)

            # Get chapters for this book
            cursor.execute("""
                SELECT DISTINCT chapter_num
                FROM verses
                WHERE book_code = ?
                ORDER BY chapter_num
            """, (book_code,))
            chapters = cursor.fetchall()

            for chapter in chapters:
                chapter_num = chapter['chapter_num']
                self.generate_chapter_file(book_code, book_name, chapter_num)
                total_chapters += 1

        print(f"   ✓ Generated {total_chapters} chapter files across {len(books)} books")

    def generate_chapter_file(self, book_code: str, book_name: str, chapter_num: int):
        """Generate a single chapter Markdown file with layered information"""
        cursor = self.conn.cursor()

        # Get verses for this chapter
        cursor.execute("""
            SELECT * FROM verses
            WHERE book_code = ? AND chapter_num = ?
            ORDER BY verse_num
        """, (book_code, chapter_num))
        verses = cursor.fetchall()

        if not verses:
            return

        # Create chapter file
        file_path = self.output_dir / "Bible" / book_name / f"Chapter {chapter_num}.md"

        with open(file_path, 'w', encoding='utf-8') as f:
            # Frontmatter
            f.write("---\n")
            f.write(f"book: {book_name}\n")
            f.write(f"book_code: {book_code}\n")
            f.write(f"chapter: {chapter_num}\n")
            f.write(f"type: bible-chapter\n")
            f.write(f"verse_count: {len(verses)}\n")
            f.write("---\n\n")

            # Title
            f.write(f"# {book_name} {chapter_num}\n\n")

            # Reading view (Layer 1 - clean text)
            f.write('<div class="bible-reading-view">\n\n')

            for verse in verses:
                verse_uid = verse['uid']
                verse_num = verse['verse_num']
                text = verse['text']

                # Get entities/topics for this verse
                entities = self.get_verse_relationships(verse_uid, 'ENTITY')
                topics = self.get_verse_relationships(verse_uid, 'TOPIC')
                lexicon = self.get_verse_relationships(verse_uid, 'LEXICON')

                # Layer 1: Clean reading
                f.write(f'<span class="verse-number">{verse_num}</span> ')

                # Layer 2: Text with entity markers
                # We'll use CSS classes to highlight entities on hover
                f.write(f'<span class="verse-text" data-uid="{verse_uid}" ')

                # Add data attributes for Dataview queries
                if entities:
                    f.write(f'data-entities="{",".join([e["target_uid"] for e in entities])}" ')
                if topics:
                    f.write(f'data-topics="{",".join([t["target_uid"] for t in topics])}" ')
                if lexicon:
                    f.write(f'data-lexicon="{",".join([l["target_uid"] for l in lexicon])}" ')

                f.write(f'>{text}</span> ')

                # Layer 3: Expandable details (hidden by default)
                if entities or topics or lexicon:
                    f.write(f'\n\n<div class="verse-details" id="details-{verse_uid}" style="display:none">\n\n')

                    if entities:
                        f.write("**People/Places:**\n")
                        for entity in entities:
                            entity_info = self.get_entity(entity['target_uid'])
                            if entity_info:
                                f.write(f"- [[Entities/{entity_info['entity_type']}/{entity_info['entity_name']}]]\n")

                    if topics:
                        f.write("\n**Topics:**\n")
                        for topic in topics:
                            topic_info = self.get_topic(topic['target_uid'])
                            if topic_info:
                                f.write(f"- [[Topics/{topic_info['topic_name']}]]\n")

                    if lexicon:
                        f.write("\n**Word Study:**\n")
                        for lex in lexicon[:3]:  # Limit to top 3
                            lex_info = self.get_lexicon(lex['target_uid'])
                            if lex_info:
                                f.write(f"- {lex_info['word']} ({lex_info['strongs_number']}): {lex_info['definition'][:100]}...\n")

                    f.write("\n</div>\n\n")

            f.write("\n</div>\n\n")

            # Sidebar queries (will be rendered by Dataview)
            f.write("---\n\n")
            f.write("## Chapter Information\n\n")
            f.write("```dataview\n")
            f.write("TABLE WITHOUT ID\n")
            f.write(f"  file.link as \"Chapter\",\n")
            f.write(f"  verse_count as \"Verses\"\n")
            f.write(f"WHERE file = this.file\n")
            f.write("```\n\n")

    def get_verse_relationships(self, verse_uid: str, rel_type: str) -> List[Dict]:
        """Get all relationships of a specific type for a verse"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM relationships
            WHERE verse_uid = ? AND relationship_type = ?
        """, (verse_uid, rel_type))
        return [dict(row) for row in cursor.fetchall()]

    def get_entity(self, entity_uid: str) -> Dict:
        """Get entity information"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entities WHERE uid = ?", (entity_uid,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_topic(self, topic_uid: str) -> Dict:
        """Get topic information"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM topics WHERE uid = ?", (topic_uid,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_lexicon(self, lexicon_uid: str) -> Dict:
        """Get lexicon entry"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM lexicon WHERE uid = ?", (lexicon_uid,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def generate_entity_pages(self):
        """Generate pages for people and places"""
        print("\n👥 Generating entity pages...")

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entities ORDER BY entity_name")
        entities = cursor.fetchall()

        for entity in entities:
            entity_type = entity['entity_type'] or 'Other'
            entity_dir = self.output_dir / "Entities" / entity_type
            entity_dir.mkdir(parents=True, exist_ok=True)

            file_path = entity_dir / f"{entity['entity_name']}.md"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(f"entity_uid: {entity['uid']}\n")
                f.write(f"entity_name: {entity['entity_name']}\n")
                f.write(f"entity_type: {entity_type}\n")
                f.write(f"type: entity\n")
                f.write("---\n\n")

                f.write(f"# {entity['entity_name']}\n\n")

                if entity['description']:
                    f.write(f"{entity['description']}\n\n")

                f.write("## Verses Mentioning This Entity\n\n")
                f.write("```dataview\n")
                f.write("LIST\n")
                f.write(f"FROM \"Bible\"\n")
                f.write(f"WHERE contains(string(file), \"{entity['entity_name']}\")\n")
                f.write("```\n\n")

        print(f"   ✓ Generated {len(entities)} entity pages")

    def generate_topic_pages(self):
        """Generate pages for topics"""
        print("\n🏷️  Generating topic pages...")

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM topics ORDER BY topic_name")
        topics = cursor.fetchall()

        topic_dir = self.output_dir / "Topics"

        for topic in topics:
            file_path = topic_dir / f"{topic['topic_name']}.md"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(f"topic_uid: {topic['uid']}\n")
                f.write(f"topic_name: {topic['topic_name']}\n")
                f.write(f"type: topic\n")
                f.write("---\n\n")

                f.write(f"# {topic['topic_name']}\n\n")

                if topic['description']:
                    f.write(f"{topic['description']}\n\n")

                f.write("## Related Verses\n\n")
                f.write("```dataview\n")
                f.write("TABLE file.link as Verse\n")
                f.write("FROM \"Bible\"\n")
                f.write(f"WHERE contains(data-topics, \"{topic['uid']}\")\n")
                f.write("```\n\n")

        print(f"   ✓ Generated {len(topics)} topic pages")

    def generate_lexicon_pages(self):
        """Generate lexicon (Strong's) pages"""
        print("\n📚 Generating lexicon pages...")

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM lexicon")
        count = cursor.fetchone()[0]

        print(f"   ℹ️  Skipping {count} lexicon entries (create on-demand)")
        print("   💡 Use Dataview queries to access lexicon data dynamically")

    def generate_index_pages(self):
        """Generate main index pages"""
        print("\n📑 Generating index pages...")

        # Main index
        with open(self.output_dir / "Home.md", 'w', encoding='utf-8') as f:
            f.write("# Bible Study Vault\n\n")
            f.write("Welcome to your interactive Bible study vault!\n\n")
            f.write("## Quick Start\n\n")
            f.write("- [[Bible Index]] - Browse all books and chapters\n")
            f.write("- [[Entities/Index]] - People and places\n")
            f.write("- [[Topics/Index]] - Topical index\n")
            f.write("- [[Settings]] - Customize your experience\n\n")
            f.write("## How to Use\n\n")
            f.write("1. **Layer 1 (Read)**: Clean reading experience\n")
            f.write("2. **Layer 2 (Explore)**: Hover over text to see highlights\n")
            f.write("3. **Layer 3 (Deep Dive)**: Click footnotes for detailed info\n\n")

        print("   ✓ Index pages created")

    def copy_assets(self):
        """Copy CSS snippets and templates"""
        print("\n🎨 Creating assets...")
        print("   ℹ️  CSS and templates will be created separately")

    def close(self):
        """Close database connection"""
        self.conn.close()

def main():
    db_path = Path("obsidian-bible.db")
    output_dir = Path("ObsidianBibleVault")

    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        print("   Run 1_export_to_sqlite.py first")
        return

    generator = ObsidianBibleVaultGenerator(db_path, output_dir)
    generator.generate_vault()
    generator.close()

if __name__ == "__main__":
    main()
