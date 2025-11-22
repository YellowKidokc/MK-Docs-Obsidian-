#!/bin/bash
# Import missing verse chunks to D1
# Use this if you've split missing_verses.sql into chunks

cd "/c/Postgres/Bible_Database/Exports/Cloudflare_D1" || exit 1

chunks_dir="data/missing_verses_chunks"

if [ ! -d "$chunks_dir" ]; then
    echo "❌ Error: $chunks_dir not found!"
    echo "   Run 3_split_missing_verses.py first"
    exit 1
fi

# Count chunk files
chunk_count=$(ls -1 "$chunks_dir"/missing_verses_part_*.sql 2>/dev/null | wc -l)

if [ $chunk_count -eq 0 ]; then
    echo "❌ Error: No chunk files found in $chunks_dir"
    exit 1
fi

echo "📤 Importing $chunk_count missing verse chunks to Cloudflare D1..."
echo "⏱️  This will take a few minutes..."
echo ""

success=0
failed=0

for chunk_file in "$chunks_dir"/missing_verses_part_*.sql; do
    chunk_name=$(basename "$chunk_file")
    chunk_num=$(echo "$chunk_name" | grep -oP 'part_\K\d+')

    echo -n "[${chunk_num}/${chunk_count}] Importing $chunk_name... "

    if wrangler d1 execute bible_data --remote --file="$chunk_file" >/dev/null 2>&1; then
        echo "✓"
        ((success++))
    else
        echo "✗ FAILED"
        ((failed++))
    fi

    # Small delay to avoid rate limiting
    sleep 1
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Import Complete!"
echo "   Successful: $success"
echo "   Failed: $failed"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $failed -gt 0 ]; then
    echo "⚠️  Some chunks failed - likely due to duplicate UIDs (already imported)"
    echo "   This is normal if you're re-running the import"
fi

echo ""
echo "Verifying total verse count..."
wrangler d1 execute bible_data --remote \
    --command="SELECT COUNT(*) as verse_count FROM verses;"

echo ""
echo "✨ Done! Run 6_verify_deployment.sh to verify the complete deployment."
