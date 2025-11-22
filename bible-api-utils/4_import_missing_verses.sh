#!/bin/bash
# Import missing_verses.sql to D1
# Use this if the file is small (<1 MB)
# Otherwise, run 3_split_missing_verses.py and then 5_import_missing_chunks.sh

cd "/c/Postgres/Bible_Database/Exports/Cloudflare_D1" || exit 1

echo "📤 Importing missing verses to Cloudflare D1..."
echo ""

if [ ! -f "data/missing_verses.sql" ]; then
    echo "❌ Error: data/missing_verses.sql not found!"
    echo "   Run 2_generate_missing_verses.py first"
    exit 1
fi

# Check file size
file_size=$(stat -f%z "data/missing_verses.sql" 2>/dev/null || stat -c%s "data/missing_verses.sql" 2>/dev/null)
file_size_mb=$(echo "scale=2; $file_size / 1048576" | bc)

echo "File size: ${file_size_mb} MB"

if (( $(echo "$file_size_mb > 1.0" | bc -l) )); then
    echo "⚠️  File is too large (${file_size_mb} MB)"
    echo "   Run 3_split_missing_verses.py to split into chunks"
    echo "   Then run 5_import_missing_chunks.sh to import"
    exit 1
fi

echo "Importing missing_verses.sql..."
wrangler d1 execute bible_data --remote --file=data/missing_verses.sql

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Import successful!"
    echo ""
    echo "Verifying verse count..."
    wrangler d1 execute bible_data --remote \
        --command="SELECT COUNT(*) as verse_count FROM verses;"
    echo ""
    echo "✨ All missing verses imported! Run 6_verify_deployment.sh to verify."
else
    echo ""
    echo "❌ Import failed!"
    echo "   Try running 3_split_missing_verses.py to split into smaller chunks"
fi
