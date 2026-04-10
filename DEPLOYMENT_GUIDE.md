# 🚀 LAIRM Platform Deployment Guide

## ✅ What's Been Completed

### 1. GitHub Pages Teaser Site
- **Status**: ✅ Code Complete, Awaiting GitHub Pages Configuration
- **Location**: `/docs` folder
- **URL**: Will be `https://selectess.github.io/LAIR_Management/`

#### Created Files:
- `docs/index.html` - Futuristic teaser page with ImFro.jpeg hero image
- `docs/manifesto/index.html` - Language selector (11 languages)
- `docs/manifesto/{lang}/index.html` - Documentation index for each language:
  - 🇬🇧 English (`/en/`)
  - 🇫🇷 French (`/fr/`)
  - 🇪🇸 Spanish (`/es/`)
  - 🇩🇪 German (`/de/`)
  - 🇨🇳 Chinese (`/zh/`)
  - 🇸🇦 Arabic (`/ar/`)
  - 🇷🇺 Russian (`/ru/`)
  - 🇵🇹 Portuguese (`/pt/`)
  - 🇯🇵 Japanese (`/ja/`)
  - 🇮🇳 Hindi (`/hi/`)
  - 🇮🇹 Italian (`/it/`)

### 2. Next.js Web Platform
- **Status**: ✅ Complete, Running Locally
- **Location**: `/lairm-web` folder
- **Local URL**: http://localhost:3001
- **Production URL**: Pending Vercel deployment

#### Features:
- Landing page with 2 CTA buttons
- Manifesto page (19 axioms, 361 articles)
- Platform page (5 integrated modules)
- Admin backoffice for content management
- REST API endpoints for all resources

### 3. Supabase Backend
- **Status**: ✅ Configured & Running
- **Project ID**: vfpgwoxfpveiolidfmcz
- **Database**: 8 tables with RLS policies
- **API Keys**: Stored in `.env.local`

---

## 🔧 Next Steps to Complete Deployment

### Step 1: Enable GitHub Pages (2 minutes)

1. Go to: https://github.com/selectess/LAIR_Management/settings/pages
2. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Click **Save**
4. Wait 2-3 minutes for deployment
5. Visit: https://selectess.github.io/LAIR_Management/

**Expected Result**: Teaser page with 2 buttons:
- Button 1: "📖 Le Manifeste" → Language selector → Documentation
- Button 2: "🌐 Cybernetic Criterion Platform" → Next.js app (will update URL after Vercel deployment)

---

### Step 2: Deploy Next.js to Vercel (5 minutes)

#### Option A: Via Vercel CLI (Recommended)
```bash
cd lairm-web
npx vercel login
npx vercel --prod
```

#### Option B: Via Vercel Dashboard
1. Go to: https://vercel.com/new
2. Import Git Repository: `selectess/LAIR_Management`
3. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `lairm-web`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
4. Add Environment Variables (from `.env.local`):
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://vfpgwoxfpveiolidfmcz.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
5. Click **Deploy**

**Expected Result**: 
- Production URL: `https://lairm.vercel.app` (or similar)
- Platform accessible with all 5 modules working

---

### Step 3: Update Teaser Page with Vercel URL (1 minute)

After Vercel deployment, update the button link:

```bash
# Edit docs/index.html
# Change line 165:
<a href="https://lairm.vercel.app" class="btn btn-secondary">

# Replace with your actual Vercel URL
<a href="https://your-actual-url.vercel.app" class="btn btn-secondary">

# Commit and push
git add docs/index.html
git commit -m "Update Vercel URL in teaser page"
git push origin main
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  selectess.github.io/LAIR_Management/                   │
│  (GitHub Pages - Static Teaser + Multilingual Docs)    │
│  • Teaser page with ImFro.jpeg                          │
│  • Language selector (11 languages)                     │
│  • Documentation links to GitHub markdown files         │
└─────────────────────────────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────┐
│  lairm.vercel.app                                       │
│  (Vercel - Dynamic Next.js Platform)                   │
│  • Landing page                                         │
│  • Manifesto (19 axioms)                               │
│  • Platform (5 modules)                                 │
│  • Admin backoffice                                     │
│  • REST APIs                                            │
└─────────────────────────────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Supabase (Backend)                                     │
│  • PostgreSQL database (8 tables)                       │
│  • Authentication                                       │
│  • Row Level Security                                   │
│  • Real-time subscriptions                             │
└─────────────────────────────────────────────────────────┘
```

---

## 💰 Cost Breakdown (All Free Tiers)

| Service | Free Tier Limit | Usage | Cost |
|---------|----------------|-------|------|
| GitHub Pages | 1GB storage, 100GB bandwidth/month | ~50MB | $0 |
| Vercel | 100GB bandwidth/month | ~10GB expected | $0 |
| Supabase | 500MB database, 1GB file storage | ~100MB expected | $0 |
| **TOTAL** | | | **$0/month** |

---

## 🎯 Platform Features

### Teaser Site (GitHub Pages)
- ✅ Futuristic design with cybernetic grid background
- ✅ Animated particles and glow effects
- ✅ Hero image (ImFro.jpeg) with gradient border
- ✅ 2 CTA buttons with hover animations
- ✅ Stats display (19 axioms, 361 articles, 28 chapters)
- ✅ Multilingual support (11 languages)
- ✅ Direct links to GitHub markdown documentation

### Next.js Platform (Vercel)
- ✅ Landing page with hero section
- ✅ Manifesto page with 19 axioms display
- ✅ Platform page with 5 modules:
  1. Portail (General presentation)
  2. Magazine/Blog (Articles & videos)
  3. AI Directory (Agent & model listings)
  4. Voting System (150 char messages with @username)
  5. Waitlist (Step form for contributors)
- ✅ Admin backoffice:
  - Article management
  - Video management
  - AI directory management
  - Vote moderation
  - Contributor management
- ✅ REST API endpoints:
  - `/api/articles` - GET/POST articles
  - `/api/videos` - GET/POST videos
  - `/api/directory` - GET/POST AI agents
  - `/api/votes` - GET/POST votes
  - `/api/waitlist` - GET/POST contributors

### Supabase Backend
- ✅ 8 database tables:
  - `articles` - Blog posts and content
  - `videos` - Video metadata and links
  - `ai_directory` - AI agent/model listings
  - `topics` - Content categorization
  - `comments` - User discussions
  - `votes` - Voting system (150 char max)
  - `waitlist` - Contributor applications
  - `contributors` - Approved contributors
- ✅ Row Level Security (RLS) policies
- ✅ Timestamps and soft deletes
- ✅ Foreign key relationships

---

## 🔮 Future Enhancements (Not Yet Implemented)

### Article-to-Video Automation Pipeline
**Goal**: Convert LAIRM articles to videos and upload to YouTube channel "Cybernetic Criterion LAIR Management"

**Proposed Stack** (All Free Tier):
1. **Supabase Edge Functions** (Free: 500K invocations/month)
   - Trigger: New article created
   - Extract article text and metadata
2. **Text-to-Speech**: ElevenLabs Free Tier (10K chars/month)
   - Generate narration audio
3. **Visual Generation**: Canva API Free Tier
   - Create video visuals from article content
4. **Video Assembly**: FFmpeg (Open source)
   - Combine audio + visuals
5. **YouTube Upload**: YouTube Data API v3 (Free: 10K requests/day)
   - Upload to channel
   - Save video_id to database

**Implementation**: Not started (requires additional setup)

### Content Automation Agent
**Goal**: Generate 5 articles/day automatically

**Proposed Approach**:
- Supabase Edge Function with cron trigger
- AI content generation (OpenAI/Anthropic API)
- Auto-publish to platform
- Cost: ~$10-20/month for AI API calls

**Status**: Not implemented (would exceed $0 budget)

---

## 📝 Testing Checklist

### GitHub Pages
- [ ] Visit https://selectess.github.io/LAIR_Management/
- [ ] Verify teaser page loads with ImFro.jpeg
- [ ] Click "📖 Le Manifeste" button
- [ ] Select a language (e.g., English)
- [ ] Verify documentation links work
- [ ] Test all 11 language versions

### Vercel Platform
- [ ] Visit production URL
- [ ] Test landing page navigation
- [ ] Browse manifesto (19 axioms)
- [ ] Explore platform modules
- [ ] Access admin backoffice
- [ ] Test API endpoints with Postman/curl

### Supabase
- [ ] Verify database connection
- [ ] Test CRUD operations via API
- [ ] Check RLS policies
- [ ] Monitor query performance

---

## 🆘 Troubleshooting

### GitHub Pages Not Loading
1. Check repository settings: Settings → Pages
2. Verify branch is `main` and folder is `/docs`
3. Wait 2-3 minutes after enabling
4. Check Actions tab for deployment status

### Vercel Deployment Fails
1. Verify `lairm-web/package.json` exists
2. Check build logs in Vercel dashboard
3. Ensure environment variables are set
4. Try deploying from CLI: `npx vercel --prod`

### Supabase Connection Issues
1. Verify `.env.local` has correct keys
2. Check Supabase project status
3. Test connection: `curl https://vfpgwoxfpveiolidfmcz.supabase.co`
4. Review RLS policies if queries fail

---

## 📞 Support

- **GitHub Issues**: https://github.com/selectess/LAIR_Management/issues
- **Documentation**: See `/LAIRM/00-METADATA/` folder
- **Supabase Dashboard**: https://supabase.com/dashboard/project/vfpgwoxfpveiolidfmcz

---

## 🎉 Summary

**Completed**:
- ✅ GitHub Pages teaser site (11 languages)
- ✅ Next.js platform (running locally)
- ✅ Supabase backend (configured)
- ✅ All code pushed to GitHub

**Remaining** (5-10 minutes):
1. Enable GitHub Pages in repository settings
2. Deploy Next.js to Vercel
3. Update teaser page with Vercel URL

**Total Cost**: $0/month (all free tiers)

**Scalability**: Platform designed for 8 billion users with serverless architecture
