#!/bin/bash

# 🚀 Vercel Environment Variables Setup Script
# Run this AFTER your first deployment completes

echo "🔧 Setting up Vercel environment variables..."
echo ""

# Add Supabase URL
echo "📝 Adding NEXT_PUBLIC_SUPABASE_URL..."
echo "https://vfpgwoxfpveiolidfmcz.supabase.co" | vercel env add NEXT_PUBLIC_SUPABASE_URL production

echo ""

# Add Supabase Anon Key
echo "📝 Adding NEXT_PUBLIC_SUPABASE_ANON_KEY..."
echo "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZmcGd3b3hmcHZlaW9saWRmbWN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4NDM4NDEsImV4cCI6MjA5MTQxOTg0MX0.ZLGWFN1PFimIcQp_3gLkCCLVW3Sg3QGWs_CELNBFXwM" | vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production

echo ""
echo "✅ Environment variables added!"
echo ""
echo "🔄 Redeploying with environment variables..."
vercel --prod

echo ""
echo "🎉 Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "1. Copy your production URL from above"
echo "2. Test your site in the browser"
echo "3. Update docs/index.html with the production URL"
