#!/bin/bash

# 🔗 Update Teaser Page with Vercel URL
# Usage: ./update-teaser-url.sh https://your-actual-url.vercel.app

if [ -z "$1" ]; then
    echo "❌ Error: Please provide your Vercel URL"
    echo ""
    echo "Usage: ./update-teaser-url.sh https://your-url.vercel.app"
    echo ""
    exit 1
fi

VERCEL_URL=$1

echo "🔧 Updating teaser page with Vercel URL..."
echo "📝 New URL: $VERCEL_URL"
echo ""

# Update docs/index.html
sed -i '' "s|https://lairm.vercel.app|$VERCEL_URL|g" docs/index.html

echo "✅ Updated docs/index.html"
echo ""

# Show the change
echo "📋 Verifying change:"
grep -n "btn-secondary" docs/index.html | head -1
echo ""

# Commit and push
echo "💾 Committing changes..."
git add docs/index.html
git commit -m "Update Vercel production URL to $VERCEL_URL"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "🎉 Done! Your teaser page now links to: $VERCEL_URL"
echo ""
echo "📋 Next step: Enable GitHub Pages"
echo "   Go to: https://github.com/selectess/LAIR_Management/settings/pages"
echo "   Set: Branch 'main', Folder '/docs'"
