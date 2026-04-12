# LAIRM Platform - Implementation Guide

## Quick Start

### 1. Teaser (GitHub Pages)

**Location**: `gh-pages/` branch

**Files to create**:
```
gh-pages/
├── index.html
├── css/
│   ├── style.css
│   ├── design-system.css
│   └── animations.css
├── js/
│   ├── main.js
│   ├── axioms.js
│   └── scroll.js
└── assets/
    ├── logo.png
    └── axioms/
```

**Key sections**:
- Hero (Logo + Title + CTA)
- Vision (3 columns)
- Axioms Grid (3x3)
- Case Studies (3 cards)
- Footer

**Deployment**:
```bash
git checkout -b gh-pages
# Add files
git add .
git commit -m "Add teaser"
git push origin gh-pages
```

---

### 2. Platform (Vercel)

**Location**: `platform/` directory

**Tech Stack**:
- Next.js 14+ (App Router)
- React 18+
- TypeScript
- Tailwind CSS
- Supabase Client

**Key pages**:
- `/` - Portal
- `/magazine` - Articles
- `/votes` - Voting
- `/directory` - AI Directory
- `/contributors` - Profiles
- `/waitlist` - Onboarding
- `/admin` - Backoffice

**Deployment**:
```bash
# Connect to Vercel
vercel link

# Deploy
vercel deploy --prod
```

---

### 3. Backend (Supabase)

**Setup**:
1. Create Supabase project
2. Run migrations
3. Configure RLS policies
4. Set up storage buckets

**Database tables**:
- articles
- videos
- votes
- ai_directory
- contributors
- waitlist
- topics
- comments

**Environment variables**:
```
NEXT_PUBLIC_SUPABASE_URL=https://[project].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=[key]
SUPABASE_SERVICE_ROLE_KEY=[key]
ADMIN_API_KEY=[your-secret-key]
```

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB PAGES (Teaser)                    │
│              Static HTML/CSS/JS - Minimalist                │
│                   Hosted on gh-pages branch                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    VERCEL (Platform)                        │
│              Next.js 14+ App Router                         │
│              React + TypeScript + Tailwind                  │
│                   Hosted on Vercel                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SUPABASE (Backend)                       │
│              PostgreSQL + Auth + Storage                    │
│                   Hosted on Supabase                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Design System

### Colors
- **Primary BG**: #0a0a0f
- **Secondary BG**: #0f0f1a
- **Accent Gold**: #c9a962
- **Accent Beige**: #d4c4a8
- **Text Primary**: #ffffff

### Typography
- **Display**: Playfair Display (serif)
- **Body**: Inter (sans-serif)

### Components
- Buttons (Primary, Secondary)
- Cards
- Inputs
- Badges
- Modals

---

## API Routes

```
GET    /api/articles              → List articles
POST   /api/articles              → Create article (admin)
GET    /api/articles/[id]         → Get article
PUT    /api/articles/[id]         → Update article (admin)
DELETE /api/articles/[id]         → Delete article (admin)

GET    /api/votes                 → List votes
POST   /api/votes                 → Create vote
PUT    /api/votes/[id]            → Update vote score

GET    /api/directory             → List directory
POST   /api/directory             → Create entry (admin)

GET    /api/contributors          → List contributors
POST   /api/contributors          → Create contributor (admin)

POST   /api/waitlist              → Join waitlist
GET    /api/waitlist              → List waitlist (admin)

POST   /api/auth/login            → Admin login
POST   /api/auth/logout           → Admin logout
```

---

## Database Schema

```sql
-- Articles
CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    content TEXT,
    topic_id UUID REFERENCES topics(id),
    status TEXT DEFAULT 'draft',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Votes
CREATE TABLE votes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL,
    content TEXT CHECK (char_length(content) <= 150),
    score INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- AI Directory
CREATE TABLE ai_directory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    description TEXT,
    link TEXT,
    category TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Contributors
CREATE TABLE contributors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    type TEXT CHECK (type IN ('thinker', 'developer', 'researcher', 'investor')),
    bio TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Waitlist
CREATE TABLE waitlist (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    type TEXT,
    message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Topics
CREATE TABLE topics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE
);
```

---

## Security

### Authentication
- Admin API key for write operations
- JWT tokens for session management
- Secure cookies for token storage

### Data Protection
- HTTPS only
- CORS configured
- Rate limiting
- Input validation
- SQL injection prevention (Supabase)
- XSS protection

### Row Level Security (RLS)
```sql
-- Public read published articles
CREATE POLICY "Public read" ON articles
    FOR SELECT USING (status = 'published');

-- Admin write access
CREATE POLICY "Admin write" ON articles
    FOR ALL USING (auth.jwt() ->> 'role' = 'admin');
```

---

## Performance

### Frontend Optimization
- Static generation (SSG)
- Image optimization
- Code splitting
- Lazy loading
- Edge caching

### Backend Optimization
- Database indexing
- Query optimization
- Connection pooling
- Caching layer
- CDN for static assets

---

## Deployment Checklist

### Teaser (GitHub Pages)
- [ ] Create gh-pages branch
- [ ] Add HTML/CSS/JS files
- [ ] Add logo and assets
- [ ] Test locally
- [ ] Push to gh-pages
- [ ] Verify GitHub Pages deployment

### Platform (Vercel)
- [ ] Create Next.js project
- [ ] Configure environment variables
- [ ] Connect GitHub repository
- [ ] Deploy to Vercel
- [ ] Configure custom domain
- [ ] Set up preview deployments

### Backend (Supabase)
- [ ] Create Supabase project
- [ ] Create database tables
- [ ] Configure RLS policies
- [ ] Set up storage buckets
- [ ] Configure authentication
- [ ] Test API endpoints

---

## Testing

### Frontend Testing
```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Build test
npm run build
```

### API Testing
```bash
# Test articles endpoint
curl https://platform.lairm.org/api/articles

# Test with admin key
curl -H "Authorization: Bearer YOUR_API_KEY" \
  -X POST https://platform.lairm.org/api/articles \
  -d '{"title":"Test","content":"..."}'
```

---

## Monitoring

### Frontend
- Vercel Analytics
- Error tracking (Sentry)
- Performance monitoring

### Backend
- Supabase Dashboard
- Database monitoring
- API logs

---

## Maintenance

### Regular Tasks
- Monitor error logs
- Review performance metrics
- Update dependencies
- Backup database
- Review security logs

### Content Management
- Publish new articles
- Moderate votes
- Update directory
- Manage contributors
- Process waitlist

---

## Support

### Documentation
- See `ARCHITECTURE.md` for detailed architecture
- See `FLUX_DIAGRAMS.md` for user flows
- See `DESIGN_SYSTEM.md` for design reference

### Resources
- LAIRM Creator Power: `powers/lairm-creator/`
- GitHub Repository: `https://github.com/selectess/LAIRM`
- Supabase Docs: `https://supabase.com/docs`
- Next.js Docs: `https://nextjs.org/docs`

---

## Next Steps

1. **Create Teaser** (GitHub Pages)
   - Build static HTML/CSS/JS
   - Deploy to gh-pages branch
   - Verify deployment

2. **Create Platform** (Vercel)
   - Set up Next.js project
   - Create pages and components
   - Configure API routes
   - Deploy to Vercel

3. **Set up Backend** (Supabase)
   - Create database tables
   - Configure RLS policies
   - Set up storage
   - Test API endpoints

4. **Connect Everything**
   - Configure environment variables
   - Test end-to-end flows
   - Monitor performance
   - Launch publicly

---

**Status**: Ready for implementation  
**Last Updated**: 2026-04-11  
**Version**: 1.0.0