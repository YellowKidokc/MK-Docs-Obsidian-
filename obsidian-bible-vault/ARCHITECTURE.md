

# Obsidian Bible Vault - Architecture

Technical overview of how the interactive Bible vault system works.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ PostgreSQL Database                                          │
│ (Your existing Bible database)                              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ 1_export_to_sqlite.py
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ SQLite Database (obsidian-bible.db)                         │
│ ┌──────────┬──────────┬───────────┬─────────┬────────────┐ │
│ │ books    │ verses   │ entities  │ topics  │ lexicon    │ │
│ └──────────┴──────────┴───────────┴─────────┴────────────┘ │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ 2_generate_markdown_vault.py
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ Obsidian Vault (Markdown Files)                             │
│ ┌──────────────────────────────────────────────────────────┐│
│ │ Bible/Genesis/Chapter 1.md                               ││
│ │ - Frontmatter (metadata)                                 ││
│ │ - HTML/Markdown content                                  ││
│ │ - Dataview queries (live)                                ││
│ │ - JavaScript (interactions)                              ││
│ └──────────────────────────────────────────────────────────┘│
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ Obsidian App
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ User Interface                                               │
│ ┌──────────┬─────────────────────────┬──────────────────┐  │
│ │ Left     │ Main Content            │ Right Sidebar    │  │
│ │ Sidebar  │ (Bible Text)            │ (Custom Notes)   │  │
│ │          │                         │                  │  │
│ │ People   │ Layer 1: Read           │ Personal Notes   │  │
│ │ Places   │ Layer 2: Explore        │ AI Insights      │  │
│ │ Timeline │ Layer 3: Deep Dive      │ Community        │  │
│ └──────────┴─────────────────────────┴──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### 1. Export Phase

```
PostgreSQL → Python Script → SQLite

Process:
1. Connect to PostgreSQL
2. Read tables: books, verses, entities, topics, lexicon, relationships
3. Create SQLite schema
4. Copy data with transformations
5. Add indexes for performance
6. Store metadata (translations, statistics)
```

**Key files**:
- `scripts/1_export_to_sqlite.py`

**Output**:
- `obsidian-bible.db` (~50-100 MB)

---

### 2. Generation Phase

```
SQLite → Python Script → Markdown Files

Process:
1. Read SQLite database
2. For each book:
   - For each chapter:
     - Create Markdown file
     - Add frontmatter (metadata)
     - Write verse text with HTML markup
     - Embed entity relationships
     - Add Dataview queries
     - Include JavaScript for interactivity
3. Generate entity/topic pages
4. Create index pages
5. Copy CSS and templates
```

**Key files**:
- `scripts/2_generate_markdown_vault.py`

**Output**:
- `ObsidianBibleVault/` folder
- ~10,000+ Markdown files
- Total size: ~200-300 MB

---

### 3. Runtime Phase

```
Markdown Files → Obsidian → Rendered UI

Process:
1. Obsidian loads Markdown files
2. Dataview plugin executes queries
3. JavaScript adds interactivity
4. CSS applies styling
5. User interacts (clicks, hovers)
6. Dataview re-queries database
7. UI updates dynamically
```

---

## Component Breakdown

### SQLite Database

**Schema**:

```sql
books (
    uid TEXT PRIMARY KEY,
    book_code TEXT,
    book_name TEXT,
    testament TEXT,
    book_order INTEGER
)

verses (
    uid TEXT,
    translation TEXT,  -- KJV, ESV, NIV, etc.
    book_code TEXT,
    chapter_num INTEGER,
    verse_num INTEGER,
    text TEXT,
    PRIMARY KEY (uid, translation)
)

entities (
    uid TEXT PRIMARY KEY,
    entity_name TEXT,
    entity_type TEXT,  -- Person, Place, Event
    description TEXT,
    metadata TEXT
)

topics (
    uid TEXT PRIMARY KEY,
    topic_name TEXT,
    category TEXT,
    description TEXT
)

lexicon (
    uid TEXT PRIMARY KEY,
    strongs_number TEXT,
    word TEXT,
    transliteration TEXT,
    pronunciation TEXT,
    definition TEXT,
    language TEXT  -- Hebrew, Greek
)

relationships (
    verse_uid TEXT,
    target_uid TEXT,
    relationship_type TEXT,  -- ENTITY, TOPIC, LEXICON
    context TEXT,
    PRIMARY KEY (verse_uid, target_uid, relationship_type)
)

metadata (
    key TEXT PRIMARY KEY,
    value TEXT
)
```

**Indexes** (for performance):
- `idx_verses_book` on `verses(book_code)`
- `idx_verses_chapter` on `verses(chapter_num)`
- `idx_verses_translation` on `verses(translation)`
- `idx_entities_type` on `entities(entity_type)`
- `idx_relationships_verse` on `relationships(verse_uid)`
- `idx_relationships_target` on `relationships(target_uid)`

---

### Markdown File Structure

**Example**: `Bible/Genesis/Chapter 1.md`

```markdown
---
book: Genesis
book_code: GN
chapter: 1
type: bible-chapter
translation: KJV
verse_count: 31
---

# Genesis 1

<div class="bible-chapter-layout">

<!-- LEFT SIDEBAR -->
<div class="sidebar-left">
### People in This Chapter
\```dataview
TABLE entity_name, entity_type
FROM "Entities/People"
WHERE contains(this.file.content, entity_name)
\```
</div>

<!-- MAIN CONTENT -->
<div class="main-content">
<div class="bible-reading-view">

<span class="verse-number">1</span>
<span class="verse-text"
      data-uid="GN-01-01-AA"
      data-entities="GOD-001"
      data-topics="TOP-CREATION">
  In the beginning God created...
</span>

<div class="verse-details" id="details-GN-01-01-AA">
  **People**: [[Entities/People/God]]
  **Topics**: [[Topics/Creation]]
</div>

</div>
</div>

<!-- RIGHT SIDEBAR -->
<div class="sidebar-right">
### Personal Notes
*Add your notes here*
</div>

</div>
```

---

### CSS Layer System

**Progressive disclosure** via CSS classes:

```css
/* Layer 1: Default (clean reading) */
.bible-reading-view {
    font-size: 1.1em;
    line-height: 1.8;
}

/* Layer 2: Enable entity highlights */
body.layer-2-enabled .verse-text[data-entities]::after {
    content: '';
    border-bottom: 1px dotted blue;
}

/* Layer 3: Auto-expand all details */
body.zoom-mode .verse-details {
    display: block !important;
}
```

**Controlled by**:
- JavaScript button clicks
- CSS class toggles on `<body>`
- Settings preferences

---

### Dataview Queries

**Purpose**: Dynamic content without rebuilding vault

**Example queries**:

**List people in chapter**:
```dataview
TABLE entity_name, entity_type
FROM "Entities/People"
WHERE contains(this.file.content, entity_name)
```

**Find cross-references**:
```dataview
LIST
FROM "Bible"
WHERE contains(cross_references, this.uid)
```

**Count verses by book**:
```dataview
TABLE
  length(file.lists) as "Verses"
FROM "Bible"
GROUP BY book
```

---

### JavaScript Interactivity

**Embedded in Markdown files**:

```javascript
// Toggle verse details
function toggleVerseDetails(uid) {
    const details = document.getElementById('details-' + uid);
    details.style.display =
        details.style.display === 'none' ? 'block' : 'none';
}

// Layer controls
document.querySelectorAll('.layer-toggle-btn')
    .forEach(btn => {
        btn.addEventListener('click', function() {
            const layer = this.dataset.layer;
            document.body.className = '';

            if (layer === '2') {
                document.body.classList.add('layer-2-enabled');
            } else if (layer === '3') {
                document.body.classList.add('zoom-mode');
            }
        });
    });
```

---

## Performance Optimizations

### 1. Database Indexes

All frequently queried columns have indexes:
- Verse lookups: `uid`, `book_code`, `chapter_num`
- Entity searches: `entity_name`, `entity_type`
- Relationship queries: `verse_uid`, `target_uid`

### 2. Lazy Loading

Verse details hidden by default:
```html
<div class="verse-details" style="display:none">
```

Only loaded when clicked.

### 3. Dataview Caching

Dataview caches query results automatically.

Enable in Obsidian settings:
```
Settings → Dataview → Enable query result caching
```

### 4. Chunked Generation

Vault generation processes files in batches:
- 1 book at a time
- Commits to disk periodically
- Progress updates every 100 files

### 5. Minimal Markdown

Only essential HTML in Markdown files.
Heavy lifting done by:
- CSS (styling)
- JavaScript (interactivity)
- Dataview (queries)

---

## Extension Points

### Adding New Entity Types

1. **Add to database**:
```sql
INSERT INTO entities (uid, entity_name, entity_type, description)
VALUES ('EVT-001', 'The Exodus', 'Event', 'Description...');
```

2. **Link to verses**:
```sql
INSERT INTO relationships (verse_uid, target_uid, relationship_type)
VALUES ('EX-12-01-AA', 'EVT-001', 'ENTITY');
```

3. **Regenerate vault** or manually update Markdown

### Adding Translations

Use `3_add_translation.py`:

```bash
python 3_add_translation.py \
    --translation ESV \
    --file esv_verses.csv
```

Database supports multiple translations per verse:
```sql
SELECT text FROM verses
WHERE uid = 'GN-01-01-AA'
  AND translation IN ('KJV', 'ESV', 'NIV');
```

### Custom Sidebars

Edit `templates/Chapter-Template.md`:

```markdown
<div class="sidebar-left">

### My Custom Section
\```dataview
-- Your query here
\```

</div>
```

### New Query Types

Add Dataview queries anywhere in Markdown:

```dataview
TABLE
  custom_field as "My Field"
FROM "Bible"
WHERE custom_condition
```

---

## Security & Privacy

### Local-Only Data

- SQLite database stays on your machine
- No cloud sync (unless you enable it)
- No tracking or analytics

### Obsidian Sync (Optional)

- End-to-end encrypted
- Your data, your control
- Works across devices

### Community Features (Future)

When enabled:
- Opt-in sharing of notes/insights
- Pseudonymous (no personal info required)
- Encrypted communication

---

## Scalability

### Current Limits

- **Verses**: 31,102 (full Bible)
- **Entities**: ~3,000
- **Topics**: ~5,000
- **Vault size**: ~300 MB
- **Files**: ~10,000

### Performance

- **Vault generation**: ~5 minutes
- **Obsidian load time**: ~10 seconds
- **Dataview queries**: <100ms
- **Search**: <500ms

### Multi-Translation

Each translation adds:
- +31,102 verse records
- +0 files (same Markdown, different data)
- +5-10 MB database size

**Supports**: 5-10 translations easily

---

## Future Architecture

### Planned Enhancements

1. **Real-time Collaboration**
   - WebSocket sync
   - Shared study sessions
   - Live cursor positions

2. **AI Integration**
   - Local LLM for insights
   - Semantic search
   - Automatic cross-referencing

3. **Mobile-First**
   - Progressive Web App
   - Offline-first architecture
   - Touch-optimized UI

4. **Community Platform**
   - Discussion threads
   - Upvote/downvote
   - Reputation system

---

## Technology Stack

- **Backend**: Python 3.7+
- **Database**: SQLite 3
- **Frontend**: Obsidian (Electron app)
- **Styling**: CSS3 (custom snippets)
- **Queries**: Dataview plugin (JavaScript)
- **Interactivity**: Vanilla JavaScript
- **Markdown**: CommonMark + extensions

---

## Development Workflow

### Adding Features

1. **Update Python scripts**
   - Modify generation logic
   - Add new queries

2. **Update templates**
   - Edit Markdown structure
   - Add new sections

3. **Update CSS**
   - Style new components
   - Adjust responsive breakpoints

4. **Regenerate vault**
   ```bash
   python 2_generate_markdown_vault.py
   ```

5. **Test in Obsidian**
   - Verify queries work
   - Check responsiveness
   - Test interactions

### Debugging

**Database issues**:
```bash
sqlite3 obsidian-bible.db
.tables
.schema verses
SELECT COUNT(*) FROM verses;
```

**Dataview issues**:
- Check syntax in Markdown
- Enable Dataview debug mode
- View console in Obsidian (Ctrl+Shift+I)

**CSS issues**:
- Inspect element (F12)
- Check snippet is enabled
- Verify CSS file location

---

This architecture provides a solid foundation for an extensible, performant Bible study system in Obsidian! 🚀
