#!/bin/bash
# Verify complete Bible API deployment

API_URL="https://bible-api.davidokc28.workers.dev"

echo "🔍 Verifying Bible API Deployment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check D1 database statistics
echo "📊 Database Statistics:"
echo "━━━━━━━━━━━━━━━━━━━━━━"

wrangler d1 execute bible_data --remote \
    --command="SELECT
        (SELECT COUNT(*) FROM verses) as verses,
        (SELECT COUNT(*) FROM entities) as entities,
        (SELECT COUNT(*) FROM topics) as topics,
        (SELECT COUNT(*) FROM lexicon) as lexicon,
        (SELECT COUNT(*) FROM relationships) as relationships;"

echo ""

# Expected totals
EXPECTED_VERSES=31102
EXPECTED_ENTITIES=3000
EXPECTED_TOPICS=5319

echo "📋 Expected vs Actual:"
echo "━━━━━━━━━━━━━━━━━━━━━━"

# Get actual verse count
actual_verses=$(wrangler d1 execute bible_data --remote \
    --command="SELECT COUNT(*) as count FROM verses;" 2>/dev/null | \
    grep -A1 "count" | tail -1 | tr -d ' │')

echo "Verses: $actual_verses / $EXPECTED_VERSES"

if [ "$actual_verses" = "$EXPECTED_VERSES" ]; then
    echo "✅ All verses loaded!"
else
    missing=$((EXPECTED_VERSES - actual_verses))
    percent=$((actual_verses * 100 / EXPECTED_VERSES))
    echo "⚠️  Missing $missing verses ($percent% complete)"
fi

echo ""
echo "🌐 Testing API Endpoints:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━"

# Test root endpoint
echo -n "GET / ... "
if curl -s -f "$API_URL/" > /dev/null 2>&1; then
    echo "✓"
else
    echo "✗"
fi

# Test stats endpoint
echo -n "GET /api/stats ... "
if curl -s -f "$API_URL/api/stats" > /dev/null 2>&1; then
    echo "✓"
else
    echo "✗"
fi

# Test verse endpoint
echo -n "GET /api/verse/GN-01-01-AA ... "
result=$(curl -s "$API_URL/api/verse/GN-01-01-AA")
if echo "$result" | grep -q '"uid":"GN-01-01-AA"'; then
    echo "✓"
else
    echo "✗"
fi

# Test search endpoint
echo -n "GET /api/search?q=love ... "
result=$(curl -s "$API_URL/api/search?q=love")
if echo "$result" | grep -q '"uid"'; then
    count=$(echo "$result" | grep -o '"uid"' | wc -l)
    echo "✓ ($count results)"
else
    echo "✗"
fi

# Test topics endpoint
echo -n "GET /api/topics ... "
if curl -s -f "$API_URL/api/topics" > /dev/null 2>&1; then
    echo "✓"
else
    echo "✗"
fi

# Test book endpoint
echo -n "GET /api/book/GN ... "
result=$(curl -s "$API_URL/api/book/GN")
if echo "$result" | grep -q '"book_code":"GN"'; then
    count=$(echo "$result" | grep -o '"uid"' | wc -l)
    echo "✓ ($count verses)"
else
    echo "✗"
fi

echo ""
echo "📈 Performance Check:"
echo "━━━━━━━━━━━━━━━━━━━━━━"

# Test response time for search
start=$(date +%s%N)
curl -s "$API_URL/api/search?q=faith" > /dev/null
end=$(date +%s%N)
duration=$(( (end - start) / 1000000 ))
echo "Search query response time: ${duration}ms"

# Test response time for verse lookup
start=$(date +%s%N)
curl -s "$API_URL/api/verse/JN-03-16-AA" > /dev/null
end=$(date +%s%N)
duration=$(( (end - start) / 1000000 ))
echo "Verse lookup response time: ${duration}ms"

echo ""
echo "🔗 API Documentation:"
echo "━━━━━━━━━━━━━━━━━━━━━━"
curl -s "$API_URL/" | grep -A 100 "endpoints"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Verification Complete!"
echo ""
echo "🌐 Live API: $API_URL"
echo "📊 API Stats: $API_URL/api/stats"
echo "🔍 Search: $API_URL/api/search?q=your+query"
echo "📖 Verse: $API_URL/api/verse/GN-01-01-AA"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
