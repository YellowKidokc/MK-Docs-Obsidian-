# Quick Start: Obsidian Bible Vault

Get your interactive Bible vault running in **15 minutes**!

---

## Prerequisites

- Python 3.7+
- PostgreSQL Bible database (already have)
- Obsidian app ([download here](https://obsidian.md))

---

## 3-Step Setup

### Step 1: Export Database (2 mins)

```bash
cd obsidian-bible-vault/scripts

# Edit database credentials
nano 1_export_to_sqlite.py
# Update: host, database, user, password

# Run export
python 1_export_to_sqlite.py
```

✅ **Output**: `obsidian-bible.db` (SQLite file)

---

### Step 2: Generate Vault (3 mins)

```bash
python 2_generate_markdown_vault.py
```

✅ **Output**: `ObsidianBibleVault/` folder

**Progress**:
```
📖 Generating Bible chapters... ✓ (2000+ files)
👥 Generating entity pages... ✓ (3000 files)
🏷️ Generating topic pages... ✓ (5000 files)
```

---

### Step 3: Open in Obsidian (5 mins)

1. **Launch Obsidian**

2. **Open folder as vault**
   - Click "Open folder as vault"
   - Select `ObsidianBibleVault/`

3. **Install Dataview plugin**
   - Settings → Community plugins
   - Browse → Search "Dataview"
   - Install + Enable

4. **Enable CSS**
   - Settings → Appearance → CSS snippets
   - Enable "bible-layers"

5. **Open Home.md**
   - Start reading!

---

## First Use

### Read a Chapter

1. Navigate: `Bible/Genesis/Chapter 1.md`
2. Click **Read** button (Layer 1)
3. Scroll and read normally

### Explore Entities

1. Click **Explore** button (Layer 2)
2. See highlighted people/places
3. Hover to preview information

### Deep Dive

1. Click a verse number
2. View detailed information
3. Click links to explore

---

## Quick Tips

✅ **Switch layers** using buttons at top-right
✅ **Customize** via `Settings.md`
✅ **Search** with `Cmd/Ctrl + O`
✅ **Link notes** using `[[double brackets]]`

---

## Common Issues

### "Dataview plugin not working"

→ Settings → Community plugins → Enable "Dataview"

### "CSS not applied"

→ Copy `css/bible-layers.css` to vault's `.obsidian/snippets/`

### "Database empty"

→ Check PostgreSQL credentials in Step 1

---

## What You Get

✅ **31,102 verses** in Markdown
✅ **3,000 entities** (people/places)
✅ **5,319 topics**
✅ **8,677 lexicon entries** (Strong's)
✅ **Interactive layers** (Read/Explore/Deep Dive)
✅ **Customizable sidebars**
✅ **SQLite queries** via Dataview

---

## Next Steps

1. **Customize settings**: Edit `Settings.md`
2. **Add translations**: Run `3_add_translation.py`
3. **Take notes**: Use right sidebar
4. **Explore relationships**: Click entity links

---

**Ready?** Start with Step 1! 🚀

**Questions?** See `README.md` for full documentation.
