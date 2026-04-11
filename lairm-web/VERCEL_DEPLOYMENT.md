# 🚀 Vercel Deployment Guide

## Current Status: Deploying...

You're running: `npx vercel --prod` in `/lairm-web`

---

## 📋 Answer These Prompts

### 1. Which scope do you want to deploy to?
**Answer**: Select your personal account (your username)
- Use arrow keys to select
- Press Enter

### 2. Link to existing project?
**Answer**: `N` (No)
- This is a new project

### 3. What's your project's name?
**Suggested**: `lairm` or `lairm-platform`
- Type the name and press Enter
- This will be part of your URL: `https://lairm.vercel.app`

### 4. In which directory is your code located?
**Answer**: `./` (just press Enter)
- You're already in the correct directory

### 5. Want to override the settings?
**Answer**: `N` (No)
- Vercel will auto-detect Next.js configuration

---

## ⏳ Deployment Process

After answering prompts, Vercel will:
1. ✅ Upload your code
2. ✅ Install dependencies (`npm install`)
3. ✅ Build your app (`npm run build`)
4. ✅ Deploy to production

**Expected time**: 2-3 minutes

---

## 🎉 After Deployment Completes

You'll see output like:
```
✅ Production: https://lairm-xxxxx.vercel.app [copied to clipboard]
```

**Copy this URL!** You'll need it for Step 3.

---

## ⚠️ CRITICAL: Add Environment Variables

Your app won't work without Supabase credentials!

### Option A: Via CLI (Recommended)
```bash
# Add Supabase URL
vercel env add NEXT_PUBLIC_SUPABASE_URL
# When prompted, paste: https://vfpgwoxfpveiolidfmcz.supabase.co
# Select: Production

# Add Supabase Key
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY
# When prompted, paste the key from .env.local
# Select: Production

# Redeploy with environment variables
vercel --prod
```

### Option B: Via Dashboard
1. Go to: https://vercel.com/dashboard
2. Click your project (`lairm`)
3. Go to: Settings → Environment Variables
4. Add these variables for **Production**:
   - `NEXT_PUBLIC_SUPABASE_URL` = `https://vfpgwoxfpveiolidfmcz.supabase.co`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY` = (copy from `.env.local`)
5. Go to Deployments → Click "..." → Redeploy

---

## 🔍 Get Your Supabase Key

If you need to copy the Supabase key:

```bash
cat .env.local
```

Look for the line starting with `NEXT_PUBLIC_SUPABASE_ANON_KEY=`

---

## ✅ Verify Deployment

After adding environment variables and redeploying:

### Test Homepage
```bash
curl https://your-url.vercel.app
# Should return HTML
```

### Test API
```bash
curl https://your-url.vercel.app/api/articles
# Should return JSON array
```

### Test in Browser
1. Visit: `https://your-url.vercel.app`
2. Check: Landing page loads
3. Navigate: Manifesto, Platform, Admin pages
4. Test: API endpoints work

---

## 🔄 Next Step: Update Teaser Page

Once you have your Vercel URL, update the GitHub Pages teaser:

```bash
# Go back to project root
cd ..

# Edit docs/index.html
# Find line 165:
# <a href="https://lairm.vercel.app" class="btn btn-secondary">
# Replace with your actual URL

# Commit and push
git add docs/index.html
git commit -m "Update Vercel production URL"
git push origin main
```

---

## 🆘 Troubleshooting

### Build Fails
- Check build logs in terminal
- Verify `package.json` is correct
- Try local build: `npm run build`

### 404 Errors
- Environment variables not set
- Add them via CLI or dashboard
- Redeploy after adding

### Supabase Connection Error
- Verify environment variables are correct
- Check Supabase project is active
- Test: `curl https://vfpgwoxfpveiolidfmcz.supabase.co`

---

## 📞 Resources

- **Vercel Dashboard**: https://vercel.com/dashboard
- **Vercel Docs**: https://vercel.com/docs
- **Your Supabase**: https://supabase.com/dashboard/project/vfpgwoxfpveiolidfmcz
- **GitHub Repo**: https://github.com/selectess/LAIR_Management

---

## 🎯 Summary

**Current Step**: Answering Vercel CLI prompts
**Next Step**: Add environment variables
**Final Step**: Update teaser page with production URL

**Total Time**: ~5 minutes
**Result**: Live platform at `https://your-app.vercel.app`
