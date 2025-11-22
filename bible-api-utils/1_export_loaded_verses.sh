#!/bin/bash
# Export list of verse UIDs currently loaded in D1
# Run this from: C:\Postgres\Bible_Database\Exports\Cloudflare_D1

echo "Exporting verse UIDs from Cloudflare D1..."

wrangler d1 execute bible_data --remote \
  --command="SELECT uid FROM verses ORDER BY uid;" \
  > loaded_verse_uids.txt

# Count how many verses are loaded
verse_count=$(wrangler d1 execute bible_data --remote \
  --command="SELECT COUNT(*) as count FROM verses;" | grep -A1 "count" | tail -1 | tr -d ' ')

echo "✓ Exported $verse_count verse UIDs to loaded_verse_uids.txt"
echo ""
echo "Next step: Run 2_generate_missing_verses.py to identify missing verses"
