# Bible API Deployment Utilities

Complete toolkit for finishing the Cloudflare D1 Bible API deployment.

## Current Status

✅ **API Deployed**: https://bible-api.davidokc28.workers.dev
📊 **Verses Loaded**: 21,102 / 31,102 (68%)
⏳ **Missing Verses**: ~10,000

## Quick Start Guide

Follow these steps to complete the deployment:

### Step 1: Export Loaded Verses

Export the list of verse UIDs currently in D1:

```bash
cd C:\Postgres\Bible_Database\Exports\Cloudflare_D1
bash bible-api-utils/1_export_loaded_verses.sh
```

**Output**: `loaded_verse_uids.txt`

### Step 2: Generate Missing Verses SQL

Identify and extract missing verses from the master file:

```bash
python bible-api-utils/2_generate_missing_verses.py
```

**Output**: `data/missing_verses.sql`

This script compares the master `verses.sql` with loaded UIDs and generates a SQL file containing only the missing verses.

### Step 3A: Import Missing Verses (Small File)

If `missing_verses.sql` is < 1 MB, import directly:

```bash
bash bible-api-utils/4_import_missing_verses.sh
```

### Step 3B: Split & Import (Large File)

If the file is > 1 MB, split into chunks:

```bash
python bible-api-utils/3_split_missing_verses.py
bash bible-api-utils/5_import_missing_chunks.sh
```

This splits the file into 500-verse chunks and imports them sequentially.

### Step 4: Add Performance Indexes

Optimize database queries by adding indexes:

```bash
bash bible-api-utils/8_add_indexes.sh
```

**Indexes added**:
- Verse lookups (uid, book_code, chapter, verse)
- Full-text search optimization
- Entity and topic lookups
- Relationship queries
- Composite indexes for common query patterns

### Step 5: Verify Deployment

Run complete verification:

```bash
bash bible-api-utils/6_verify_deployment.sh
```

This tests:
- Database statistics
- All API endpoints
- Response times
- Data completeness

## Scripts Overview

| Script | Purpose | Output |
|--------|---------|--------|
| `1_export_loaded_verses.sh` | Export UIDs from D1 | `loaded_verse_uids.txt` |
| `2_generate_missing_verses.py` | Find missing verses | `data/missing_verses.sql` |
| `3_split_missing_verses.py` | Split large SQL files | `data/missing_verses_chunks/` |
| `4_import_missing_verses.sh` | Import small SQL file | Updates D1 |
| `5_import_missing_chunks.sh` | Import chunks | Updates D1 |
| `6_verify_deployment.sh` | Test everything | Console output |
| `7_add_indexes.sql` | Index definitions | SQL commands |
| `8_add_indexes.sh` | Apply indexes | Updates D1 |

## API Endpoints

Once complete, these endpoints will be available:

```bash
# Root - API documentation
curl https://bible-api.davidokc28.workers.dev/

# Statistics
curl https://bible-api.davidokc28.workers.dev/api/stats

# Get specific verse
curl https://bible-api.davidokc28.workers.dev/api/verse/GN-01-01-AA

# Search verses
curl "https://bible-api.davidokc28.workers.dev/api/search?q=love"

# List topics
curl https://bible-api.davidokc28.workers.dev/api/topics

# Get verses by topic
curl https://bible-api.davidokc28.workers.dev/api/topic/TOP-000001

# Get all verses in a book
curl https://bible-api.davidokc28.workers.dev/api/book/GN

# Get verses mentioning a person
curl https://bible-api.davidokc28.workers.dev/api/person/PER-000001
```

## Troubleshooting

### "statement too long: SQLITE_TOOBIG"

**Solution**: The SQL file is too large. Run step 3B to split into chunks.

```bash
python bible-api-utils/3_split_missing_verses.py
bash bible-api-utils/5_import_missing_chunks.sh
```

### "UNIQUE constraint failed"

**Solution**: These verses are already loaded (duplicates). This is normal - the script will continue with remaining verses.

### Import Stalls or Times Out

**Solution**:
1. Check your internet connection
2. Try reducing chunk size in `3_split_missing_verses.py` (change `chunk_size = 500` to `250`)
3. Add longer delays between imports in `5_import_missing_chunks.sh` (change `sleep 1` to `sleep 3`)

### Can't Find wrangler Command

**Solution**: Install or update Cloudflare Wrangler:

```bash
npm install -g wrangler
wrangler --version
```

## Expected Timeline

- Step 1 (Export): ~30 seconds
- Step 2 (Generate): ~5 seconds
- Step 3 (Import): ~10-15 minutes for ~10,000 verses
- Step 4 (Indexes): ~30 seconds
- Step 5 (Verify): ~30 seconds

**Total**: ~15-20 minutes

## Success Criteria

After completing all steps, you should have:

✅ **31,102 verses** loaded (100%)
✅ **All API endpoints** responding
✅ **Search queries** returning results in < 200ms
✅ **Database indexes** optimizing performance
✅ **No error responses** from any endpoint

## Next Steps After Completion

1. **Build Frontend**: Create a web app consuming the API
2. **Add Caching**: Implement Cloudflare cache headers for faster responses
3. **Add Authentication**: Protect endpoints if needed with Cloudflare Access
4. **Monitor Usage**: Set up Cloudflare Analytics to track API usage
5. **Backup Database**: Regular exports with `wrangler d1 export`

## Files Location

All scripts should be copied to:

```
C:\Postgres\Bible_Database\Exports\Cloudflare_D1\bible-api-utils\
```

Make sure this directory is in your `Cloudflare_D1` project folder where `wrangler.toml` is located.

## Support

If you encounter issues:

1. Check script output messages carefully - they contain helpful hints
2. Verify you're in the correct directory (`Cloudflare_D1`)
3. Ensure `wrangler` is authenticated: `wrangler whoami`
4. Check Cloudflare dashboard for D1 database status
5. Review Wrangler logs in `%APPDATA%\.wrangler\logs\`

---

**Generated for**: Bible API v1.0
**Database**: Cloudflare D1 (bible_data)
**API URL**: https://bible-api.davidokc28.workers.dev
**Last Updated**: 2025-10-27
