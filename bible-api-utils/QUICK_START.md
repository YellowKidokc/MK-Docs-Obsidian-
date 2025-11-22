# Quick Start: Complete Bible API Deployment

## TL;DR - Run These 5 Commands

```bash
# Navigate to your Cloudflare D1 project
cd C:\Postgres\Bible_Database\Exports\Cloudflare_D1

# Copy bible-api-utils folder here (from the MK-Docs-Obsidian repo)

# 1. Export what's currently loaded
bash bible-api-utils/1_export_loaded_verses.sh

# 2. Find what's missing
python bible-api-utils/2_generate_missing_verses.py

# 3. Import missing verses (choose one):
# Option A - if missing_verses.sql is small:
bash bible-api-utils/4_import_missing_verses.sh

# Option B - if file is large:
python bible-api-utils/3_split_missing_verses.py
bash bible-api-utils/5_import_missing_chunks.sh

# 4. Add performance indexes
bash bible-api-utils/8_add_indexes.sh

# 5. Verify everything works
bash bible-api-utils/6_verify_deployment.sh
```

## What This Does

1. **Exports**: Gets list of 21,102 verses already in D1
2. **Compares**: Finds ~10,000 missing verses from master file
3. **Imports**: Loads all missing verses to D1 (gets you to 31,102 total)
4. **Optimizes**: Adds indexes for faster queries
5. **Verifies**: Tests all endpoints and confirms 100% completion

## Expected Results

**Before**:
```
Verses: 21,102 / 31,102 (68%)
Missing: ~10,000 verses
```

**After**:
```
Verses: 31,102 / 31,102 (100%) ✅
Complete: Full Bible API ready!
```

## Time Required

- Total: ~15-20 minutes
- Most time spent: Importing verse chunks (10-15 mins)
- Everything else: < 5 minutes

## Test Your API

```bash
# Get stats
curl https://bible-api.davidokc28.workers.dev/api/stats

# Search for "faith"
curl "https://bible-api.davidokc28.workers.dev/api/search?q=faith"

# Get John 3:16
curl https://bible-api.davidokc28.workers.dev/api/verse/JN-03-16-AA

# List topics
curl https://bible-api.davidokc28.workers.dev/api/topics
```

## If Something Goes Wrong

**"statement too long"**:
→ Use Option B (split into chunks)

**"UNIQUE constraint failed"**:
→ Normal! Those verses are already loaded

**"wrangler not found"**:
→ Run: `npm install -g wrangler`

**"File not found"**:
→ Make sure you're in the `Cloudflare_D1` directory

## Files You'll Get

```
bible-api-utils/
├── 1_export_loaded_verses.sh      # Export UIDs from D1
├── 2_generate_missing_verses.py   # Find missing verses
├── 3_split_missing_verses.py      # Split large files
├── 4_import_missing_verses.sh     # Import small file
├── 5_import_missing_chunks.sh     # Import chunks
├── 6_verify_deployment.sh         # Test everything
├── 7_add_indexes.sql              # Index definitions
├── 8_add_indexes.sh               # Apply indexes
├── README.md                      # Full documentation
├── DEPLOYMENT_CHECKLIST.md        # Step-by-step guide
└── QUICK_START.md                 # This file
```

## Success Criteria

✅ `wrangler d1 execute bible_data --remote --command="SELECT COUNT(*) FROM verses;"`
→ Should show: **31,102**

✅ `curl https://bible-api.davidokc28.workers.dev/api/stats`
→ Should show: **"verses": 31102**

✅ All API endpoints return data (no errors)

## What Happens During Import

```
[1/63] Importing verses_part_001.sql... ✓
[2/63] Importing verses_part_002.sql... ✓
[3/63] Importing verses_part_003.sql... ✓
...
[63/63] Importing verses_part_063.sql... ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Import Complete!
  Successful: 63
  Failed: 0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Ready?

Run the first command and follow the on-screen instructions:

```bash
cd C:\Postgres\Bible_Database\Exports\Cloudflare_D1
bash bible-api-utils/1_export_loaded_verses.sh
```

The script will tell you what to do next! 🚀

---

**Need help?** Check `README.md` for detailed documentation.
