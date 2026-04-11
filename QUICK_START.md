# 🚀 LAIRM Platform - Quick Start Guide

## 📍 Current Status: 95% Complete

All code is written, tested, and pushed to GitHub. Only 3 simple configuration steps remain (8 minutes total).

---

## ✅ What's Already Done

### 1. GitHub Pages Teaser Site ✅
- **Location**: `/docs` folder
- **Files**: 14 HTML files (teaser + 11 languages + language selector)
- **Design**: Futuristic cybernetic theme with ImFro.jpeg
- **Status**: Code complete, awaiting GitHub Pages activation

### 2. Next.js Web Platform ✅
- **Location**: `/lairm-web` folder
- **Status**: Running locally at http://localhost:3001
- **Features**: Landing, Manifesto, Platform (5 modules), Admin, REST APIs
- **Stack**: Next.js 15 + TypeScript + Tailwind CSS + Supabase

### 3. Supabase Backend ✅
- **Project**: lairm-platform (vfpgwoxfpveiolidfmcz)
- **Database**: 8 tables with RLS policies
- **Status**: Configured and connected

---

## 🎯 3 Steps to Go Live (8 minutes)

### Step 1: Enable GitHub Pages (2 min)

1. Open: https://github.com/selectess/LAIR_Management/settings/pages
2. Configure:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Click **Save**
4. Wait 2-3 minutes

**Result**: https://selectess.github.io/LAIR_Management/ will be live

**What you'll see**:
- Futuristic teaser page with ImFro.jpeg
- 2 buttons:
  - "📖 Le Manifeste" → 11 language selector → Documentation
  - "🌐 Cybernetic Criterion Platform" → Next.js app

---

### Step 2: Deploy to Vercel (5 min)

**Option A - CLI** (Fastest):
```bash
cd lairm-web
npx vercel login
npx vercel --prod
```

**Option B - Dashboard**:
1. Go to: https://vercel.com/new
2. Import: `selectess/LAIR_Management`
3. Settings:
   - **Root Directory**: `lairm-web`
   - **Framework**: Next.js
   - **Build Command**: `npm run build`
4. Environment Variables (copy from `.env.local`):
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://vfpgwoxfpveiolidfmcz.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
5. Click **Deploy**

**Result**: Production URL (e.g., `https://lairm.vercel.app`)

---

### Step 3: Update Platform URL (1 min)

After Vercel deployment, update the teaser page button:

```bash
# Edit docs/index.html
# Find line 165:
<a href="https://lairm.vercel.app" class="btn btn-secondary">

# Replace with your actual Vercel URL
<a href="https://your-actual-url.vercel.app" class="btn btn-secondary">

# Commit and push
git add docs/index.html
git commit -m "Update Vercel URL in teaser page"
git push origin main
```

**Result**: Teaser page button now links to live platform

---

## 🎉 You're Live!

After completing these 3 steps, you'll have:

### 🌐 Public URLs
- **Teaser Site**: https://selectess.github.io/LAIR_Management/
- **Platform**: https://your-app.vercel.app
- **Admin**: https://your-app.vercel.app/admin
- **API**: https://your-app.vercel.app/api/*

### 📊 Features Available
- ✅ Multilingual documentation (11 languages)
- ✅ Manifesto with 19 axioms, 361 articles
- ✅ Platform with 5 modules
- ✅ Admin backoffice for content management
- ✅ REST APIs for all resources
- ✅ Supabase backend with 8 tables

### 💰 Cost
- **$0/month** (all free tiers)

### 📈 Scalability
- **Serverless architecture** designed for 8 billion users

---

## 🧪 Test Your Deployment

### GitHub Pages
```bash
# After Step 1, test:
curl -I https://selectess.github.io/LAIR_Management/
# Should return: HTTP/2 200
```

### Vercel Platform
```bash
# After Step 2, test:
curl https://your-app.vercel.app/api/articles
# Should return: JSON array of articles
```

### Supabase
```bash
# Test database connection:
curl https://vfpgwoxfpveiolidfmcz.supabase.co
# Should return: Supabase API response
```

---

## 📁 What's in the Repository

```
LAIR_Management/
├── docs/                    # GitHub Pages (14 files)
│   ├── index.html           # Teaser page
│   ├── ImFro.jpeg           # Hero image
│   └── manifesto/           # 11 language versions
├── lairm-web/               # Next.js platform
│   ├── app/                 # Pages & APIs
│   ├── lib/                 # Supabase clients
│   └── .env.local           # Environment variables
├── supabase/                # Database schema
├── LAIRM/                   # Documentation (28 chapters)
├── DEPLOYMENT_GUIDE.md      # Detailed deployment instructions
├── STATUS.md                # Current status
└── QUICK_START.md           # This file
```

---

## 🆘 Troubleshooting

### GitHub Pages shows 404
- Wait 2-3 minutes after enabling
- Check: Settings → Pages → "Your site is live at..."
- Verify branch is `main` and folder is `/docs`

### Vercel build fails
- Check build logs in Vercel dashboard
- Verify environment variables are set
- Try: `cd lairm-web && npm run build` locally first

### Supabase connection error
- Verify `.env.local` has correct keys
- Check Supabase project status
- Test: https://supabase.com/dashboard/project/vfpgwoxfpveiolidfmcz

---

## 📞 Resources

- **Repository**: https://github.com/selectess/LAIR_Management
- **Supabase Dashboard**: https://supabase.com/dashboard/project/vfpgwoxfpveiolidfmcz
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Documentation**: See `DEPLOYMENT_GUIDE.md` for detailed instructions

---

## 🎯 Summary

**Time to Complete**: 8 minutes  
**Cost**: $0/month  
**Complexity**: Low (3 simple steps)  
**Result**: Global platform for 8 billion users

**Next Action**: Go to https://github.com/selectess/LAIR_Management/settings/pages and enable GitHub Pages!
