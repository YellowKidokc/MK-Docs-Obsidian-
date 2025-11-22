#!/bin/bash
# Add performance indexes to Bible API database

cd "/c/Postgres/Bible_Database/Exports/Cloudflare_D1" || exit 1

echo "📈 Adding performance indexes to Cloudflare D1 database..."
echo ""

# Check if we're in the right directory
if [ ! -f "wrangler.toml" ]; then
    echo "❌ Error: wrangler.toml not found!"
    echo "   Make sure you're in the Cloudflare_D1 directory"
    exit 1
fi

# Add indexes from SQL file
echo "Creating indexes..."
wrangler d1 execute bible_data --remote --file=bible-api-utils/7_add_indexes.sql

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Indexes created successfully!"
    echo ""
    echo "📊 Checking index status..."
    wrangler d1 execute bible_data --remote \
        --command="SELECT name, tbl_name FROM sqlite_master WHERE type='index' ORDER BY tbl_name, name;"

    echo ""
    echo "✨ Database optimization complete!"
    echo "   Your API queries should now be faster."
else
    echo ""
    echo "❌ Failed to create indexes"
    echo "   Some indexes may already exist (this is OK)"
fi

echo ""
echo "💡 Tip: Run 6_verify_deployment.sh to test API performance"
