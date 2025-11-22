

# Obsidian Bible Vault System

**Create a rich, interactive Bible study experience in Obsidian with progressive disclosure, customizable sidebars, and SQLite-powered queries.**

---

## 🎯 Overview

This system transforms your PostgreSQL Bible database into an interactive Obsidian vault with:

### **Three Progressive Layers**

1. **Layer 1 (Reading)**: Clean, distraction-free Bible reading
2. **Layer 2 (Exploring)**: Highlight entities, topics, and events on hover
3. **Layer 3 (Deep Dive)**: Click to reveal detailed lexicon, cross-references, and relationships

### **Dual Sidebar System**

- **Left Sidebar**: Structured data (People, Places, Timeline, Events)
- **Right Sidebar**: Custom content (Personal notes, AI insights, Future: community discussions)

### **Multiple Translations**

- Support for 5-6 Bible versions
- Unified verse IDs across translations
- Switch between versions instantly

---

## 📦 What's Included

```
obsidian-bible-vault/
├── scripts/
│   ├── 1_export_to_sqlite.py          # PostgreSQL → SQLite
│   ├── 2_generate_markdown_vault.py   # Create Obsidian vault
│   └── 3_add_translation.py           # Add Bible translations
├── templates/
│   ├── Chapter-Template.md            # Chapter layout
│   └── Settings.md                    # User preferences
├── css/
│   └── bible-layers.css               # Progressive disclosure UI
└── documentation/
    └── [guides and examples]
```

---

## 🚀 Quick Start

### Step 1: Export PostgreSQL to SQLite

```bash
cd obsidian-bible-vault/scripts

# Edit database credentials in the script
nano 1_export_to_sqlite.py

# Run export
python 1_export_to_sqlite.py
```

**Output**: `obsidian-bible.db` (SQLite database file)

### Step 2: Generate Obsidian Vault

```bash
python 2_generate_markdown_vault.py
```

**Output**: `ObsidianBibleVault/` folder with complete Bible structure

### Step 3: Open in Obsidian

1. Open Obsidian
2. **Open folder as vault** → Select `ObsidianBibleVault`
3. Install required plugins:
   - **Dataview** (essential)
   - **Templater** (optional)
   - **Buttons** (optional)

### Step 4: Enable CSS

1. In Obsidian: **Settings** → **Appearance** → **CSS snippets**
2. Copy `css/bible-layers.css` to `.obsidian/snippets/`
3. Enable "bible-layers" snippet

### Step 5: Configure Settings

1. Open `Settings.md` in your vault
2. Customize sidebars, layers, and preferences
3. Click **Save Settings**

---

## 📚 Vault Structure

```
ObsidianBibleVault/
├── Home.md                          # Main index
├── Settings.md                      # User preferences
├── Bible/
│   ├── Genesis/
│   │   ├── Chapter 1.md
│   │   ├── Chapter 2.md
│   │   └── ...
│   ├── Exodus/
│   └── ... (66 books)
├── Entities/
│   ├── People/
│   │   ├── Abraham.md
│   │   ├── Moses.md
│   │   └── ...
│   └── Places/
│       ├── Jerusalem.md
│       └── ...
├── Topics/
│   ├── Love.md
│   ├── Faith.md
│   └── ...
├── Lexicon/
│   └── [Strong's entries]
├── Notes/
│   └── [Your personal notes]
└── .obsidian/
    ├── snippets/
    │   └── bible-layers.css
    └── ...
```

---

## 🎨 Features

### Progressive Disclosure UI

**Layer 1: Reading**
- Clean text, minimal UI
- Just verse numbers and text
- Perfect for reading straight through

**Layer 2: Highlighting**
- Entities underlined in color:
  - 🔵 Blue = People
  - 🟢 Green = Places
  - 🟡 Yellow = Topics
- Hover to preview information
- Click verse number to expand

**Layer 3: Deep Dive**
- All relationships visible
- Lexicon entries expanded
- Cross-references shown
- Parallel translations (if available)

### Customizable Sidebars

**Left Sidebar (Structured Data)**:
```dataview
- People in this chapter
- Places mentioned
- Timeline events
- Cross references
```

**Right Sidebar (Custom Content)**:
- Personal notes
- AI insights (future)
- Community discussions (future)
- Study questions

### Multi-Translation Support

Add translations using:

```bash
python 3_add_translation.py --translation ESV --file esv_verses.csv
```

**Supported formats**:
- CSV: `uid,text`
- JSON: `[{uid: "", text: ""}]`

**Unified IDs**: All translations use KJV verse structure

---

## 🔧 Configuration

### Settings.md

Customize your experience:

#### Display
- Toggle layers (Reading/Exploring/Deep Dive)
- Select default translation
- Set font size and line spacing

#### Sidebars
- Choose which sections appear
- Reorder sections by priority
- Set sidebar width

#### Entity Highlighting
- Enable/disable by type
- Customize colors
- Set hover behavior

#### Performance
- Lazy load verse details
- Cache queries
- Preload chapters

---

## 📖 Usage Examples

### Basic Reading

1. Open any chapter: `Bible/Genesis/Chapter 1.md`
2. Read in Layer 1 (default)
3. Click **Explore** to enable highlights

### Studying a Verse

1. Click verse number to expand details
2. View people, places, topics
3. Click links to explore relationships

### Searching

Use Dataview queries:

```dataview
LIST
FROM "Bible"
WHERE contains(file.content, "love")
```

### Cross-Referencing

```dataview
TABLE file.link AS "Verse"
FROM "Bible"
WHERE contains(cross_references, "GN-01-01-AA")
```

---

## 🔌 Required Obsidian Plugins

### Essential

- **Dataview**: Powers all queries and dynamic content
  - Install: Community Plugins → Search "Dataview"
  - Enable JavaScript queries

### Recommended

- **Templater**: Enhanced templating
- **Buttons**: Interactive UI elements
- **Admonitions**: Callout boxes for notes
- **Hover Editor**: Preview links on hover

---

## 🗄️ Database Schema

The SQLite database contains:

```sql
books           -- 66 books of the Bible
verses          -- ~31,000 verses (multiple translations)
entities        -- ~3,000 people and places
topics          -- ~5,000 topics
lexicon         -- ~8,000 Strong's entries
relationships   -- ~14,000 verse-to-entity links
metadata        -- System configuration
```

### Query Examples

**Get all verses in a chapter**:
```sql
SELECT * FROM verses
WHERE book_code = 'GN' AND chapter_num = 1
ORDER BY verse_num;
```

**Find verses mentioning "Abraham"**:
```sql
SELECT v.* FROM verses v
JOIN relationships r ON v.uid = r.verse_uid
JOIN entities e ON r.target_uid = e.uid
WHERE e.entity_name = 'Abraham';
```

---

## 🌐 Future Features

### Community Integration (Planned)

- **Forum Discussions**: Community commentary per verse
- **Ranked Insights**: Upvote/downvote system
- **Shared Study Notes**: Collaborate with friends
- **Reputation System**: Trust high-quality contributors

### Advanced Features (Planned)

- **Audio Narration**: Listen to chapters
- **Reading Plans**: Guided study schedules
- **Custom Collections**: Organize favorite verses
- **Advanced Search**: Semantic/AI-powered search
- **Export Options**: PDF, Word, Markdown

---

## 📊 Adding Your Own Data

### Add a Bible Translation

```bash
# Create CSV with format: uid,text
python 3_add_translation.py --translation NIV --file niv.csv
```

### Add Custom Entities

Edit `obsidian-bible.db` directly:

```sql
INSERT INTO entities (uid, entity_name, entity_type, description)
VALUES ('PER-CUSTOM-001', 'John the Baptist', 'Person', 'Prophet...');
```

### Add Custom Topics

```sql
INSERT INTO topics (uid, topic_name, category, description)
VALUES ('TOP-CUSTOM-001', 'Baptism', 'Theological', 'Description...');
```

### Link Entities to Verses

```sql
INSERT INTO relationships (verse_uid, target_uid, relationship_type)
VALUES ('MT-03-01-AA', 'PER-CUSTOM-001', 'ENTITY');
```

---

## 🎯 Use Cases

### Personal Study

- Read through the Bible with layered insights
- Take personal notes in right sidebar
- Track reading progress

### Group Study

- Share vault with study group
- Collaborative note-taking
- Discussion threads (future)

### Teaching/Preaching

- Prepare sermons with integrated research
- Access lexicon and cross-references instantly
- Export notes for presentations

### Research

- Query relationships across the Bible
- Track themes and topics
- Lexical analysis with Strong's numbers

---

## 🛠️ Troubleshooting

### "Dataview plugin not found"

- Install Dataview from Community Plugins
- Enable in Settings → Community Plugins

### "CSS not applied"

- Copy `bible-layers.css` to `.obsidian/snippets/`
- Enable in Settings → Appearance → CSS snippets

### "Database queries slow"

- Enable "Cache queries" in Settings
- Reduce sidebar section count
- Use smaller verse ranges

### "Entities not highlighting"

- Enable Layer 2 in layer controls
- Check CSS snippet is active
- Verify entity data exists in database

---

## 📁 File Locations

- **SQLite Database**: `obsidian-bible.db` (root folder)
- **CSS Snippets**: `.obsidian/snippets/bible-layers.css`
- **Settings**: `Settings.md`
- **Templates**: `Templates/` folder

---

## 🤝 Contributing

Want to improve the system?

1. Add more Bible translations
2. Create custom entity types
3. Design new sidebar layouts
4. Build community features
5. Share CSS themes

---

## 📄 License

Use freely for personal and church/ministry use. Share with friends!

---

## 🔗 Related Projects

- **Cloudflare Bible API**: Public REST API (already deployed)
- **PostgreSQL Bible Database**: Source data (your database)
- **Obsidian**: Knowledge management app (obsidian.md)

---

## 💡 Tips & Tricks

### Keyboard Shortcuts

- `Cmd/Ctrl + E`: Edit mode ↔ Reading mode
- `Cmd/Ctrl + P`: Quick switcher
- `Cmd/Ctrl + O`: Open file

### Custom Queries

Create your own Dataview queries:

```dataview
TABLE
  verse_count as "Verses",
  length(entities) as "People"
FROM "Bible"
WHERE book = "Genesis"
```

### Mobile Support

- Sync vault to phone (Obsidian Sync or iCloud/Dropbox)
- Mobile-optimized CSS (included)
- Touch-friendly controls

---

## 📞 Support

- Issues? Check the troubleshooting section
- Questions? Open an issue on GitHub
- Feature requests? Let me know!

---

**Ready to start?** Run `python 1_export_to_sqlite.py` to begin! 🚀
