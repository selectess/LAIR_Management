# LAIRM Platform Architecture & Flux

## 1. TEASER - GitHub Pages (Static)

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB PAGES TEASER                      │
│                   (Static HTML/CSS/JS)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              HERO SECTION                            │  │
│  │  - Logo (centered, gold on dark)                     │  │
│  │  - Title: "The Cybernetic Criterion"                 │  │
│  │  - Subtitle: "Global Agentive Constitution 2026-36"  │  │
│  │  - CTA: "Explore Platform" → Vercel                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           VISION SECTION                             │  │
│  │  - 3 columns: Principles, Axioms, Impact             │  │
│  │  - Minimalist cards with gold accents                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        19 AXIOMS SHOWCASE                            │  │
│  │  - Grid: 3x3 axiom cards                             │  │
│  │  - Hover: Gold border, description                   │  │
│  │  - Click: Link to platform /axioms/:id               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        CASE STUDIES                                  │  │
│  │  - Knight Capital ($440M loss)                       │  │
│  │  - Flash Crash (2010)                                │  │
│  │  - Boeing 737 MAX (346 fatalities)                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        FOOTER                                        │  │
│  │  - Links: GitHub, Platform, Docs                     │  │
│  │  - Social: Twitter, LinkedIn                         │  │
│  │  - Copyright: CC-BY-SA-4.0                           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### File Structure

```
gh-pages/
├── index.html              # Main teaser page
├── css/
│   ├── style.css          # Main styles
│   ├── design-system.css  # Design tokens
│   └── animations.css     # Micro-animations
├── js/
│   ├── main.js            # Navigation & interactions
│   ├── axioms.js          # Axiom grid logic
│   └── scroll.js          # Scroll animations
├── assets/
│   ├── logo.png           # Logo (from root)
│   ├── axioms/            # Axiom icons (9 SVGs)
│   └── case-studies/      # Case study images
└── README.md              # GitHub Pages config
```

### Design System (CSS Variables)

```css
:root {
  /* Colors */
  --bg-primary: #0a0a0f;
  --bg-secondary: #0f0f1a;
  --bg-tertiary: #1a1a2e;
  
  --accent-gold: #c9a962;
  --accent-beige: #d4c4a8;
  --accent-cream: #f5f0e8;
  
  --text-primary: #ffffff;
  --text-secondary: #a0a0b0;
  --text-muted: #6b6b7b;
  
  --border-default: rgba(201, 169, 98, 0.2);
  --border-hover: rgba(201, 169, 98, 0.4);
  
  /* Typography */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', system-ui, sans-serif;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  
  /* Transitions */
  --transition-fast: 150ms ease-in-out;
  --transition-normal: 300ms ease-in-out;
}
```

### Key Pages

#### Hero Section
```html
<section class="hero">
  <div class="hero-content">
    <img src="assets/logo.png" alt="LAIRM" class="logo">
    <h1>The Cybernetic Criterion</h1>
    <p>Global Agentive Constitution 2026-2036</p>
    <a href="https://platform.lairm.org" class="btn-primary">
      Explore Platform
    </a>
  </div>
</section>
```

#### Axioms Grid
```html
<section class="axioms-grid">
  <div class="axiom-card" data-axiom="I">
    <h3>Ψ-I SUPREMATIA</h3>
    <p>Human Supremacy</p>
  </div>
  <!-- 8 more axiom cards -->
</section>
```

### Flux: User Journey

```
User visits GitHub Pages
    ↓
Loads teaser (static HTML)
    ↓
Reads hero section
    ↓
Explores axioms grid
    ↓
Reads case studies
    ↓
Clicks "Explore Platform"
    ↓
Redirects to Vercel platform
```

---

## 2. PLATFORM - Vercel (Dynamic)

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    VERCEL PLATFORM                          │
│                  (Next.js 14+ App Router)                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         FRONTEND LAYER (React + Tailwind)            │  │
│  │                                                      │  │
│  │  Pages:                                              │  │
│  │  - / (Portal)                                        │  │
│  │  - /magazine (Articles)                              │  │
│  │  - /votes (Voting system)                            │  │
│  │  - /directory (AI Directory)                         │  │
│  │  - /contributors (Profiles)                          │  │
│  │  - /waitlist (Onboarding)                            │  │
│  │  - /admin (Backoffice)                               │  │
│  │                                                      │  │
│  │  Components:                                         │  │
│  │  - Header (Navigation)                               │  │
│  │  - Footer (Links)                                    │  │
│  │  - Cards (Reusable)                                  │  │
│  │  - Forms (Input, Validation)                         │  │
│  │  - Modals (Dialogs)                                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         API LAYER (Next.js Routes)                   │  │
│  │                                                      │  │
│  │  /api/articles      (CRUD)                           │  │
│  │  /api/votes         (CRUD)                           │  │
│  │  /api/directory     (CRUD)                           │  │
│  │  /api/contributors  (CRUD)                           │  │
│  │  /api/waitlist      (POST)                           │  │
│  │  /api/auth          (Admin)                          │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         MIDDLEWARE LAYER                             │  │
│  │                                                      │  │
│  │  - Authentication (Admin API key)                    │  │
│  │  - Rate limiting                                     │  │
│  │  - CORS                                              │  │
│  │  - Error handling                                    │  │
│  │  - Logging                                           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SUPABASE BACKEND                         │
│                  (PostgreSQL + Auth + Storage)              │
└─────────────────────────────────────────────────────────────┘
```

### File Structure

```
platform/
├── app/
│   ├── layout.tsx              # Root layout
│   ├── page.tsx                # Portal (/)
│   ├── magazine/
│   │   ├── page.tsx            # Magazine list
│   │   └── [id]/
│   │       └── page.tsx        # Article detail
│   ├── votes/
│   │   └── page.tsx            # Voting system
│   ├── directory/
│   │   └── page.tsx            # AI Directory
│   ├── contributors/
│   │   └── page.tsx            # Contributors
│   ├── waitlist/
│   │   └── page.tsx            # Waitlist form
│   ├── admin/
│   │   ├── page.tsx            # Admin dashboard
│   │   ├── articles/
│   │   ├── votes/
│   │   └── settings/
│   └── api/
│       ├── articles/
│       │   ├── route.ts        # GET, POST
│       │   └── [id]/
│       │       └── route.ts    # GET, PUT, DELETE
│       ├── votes/
│       ├── directory/
│       ├── contributors/
│       ├── waitlist/
│       └── auth/
│           └── route.ts        # Admin auth
├── components/
│   ├── Header.tsx
│   ├── Footer.tsx
│   ├── ArticleCard.tsx
│   ├── VoteCard.tsx
│   ├── DirectoryCard.tsx
│   ├── ContributorCard.tsx
│   └── Forms/
│       ├── ArticleForm.tsx
│       ├── WaitlistForm.tsx
│       └── VoteForm.tsx
├── lib/
│   ├── supabase.ts             # Supabase client
│   ├── api.ts                  # API helpers
│   ├── auth.ts                 # Auth logic
│   └── validators.ts           # Input validation
├── styles/
│   ├── globals.css             # Global styles
│   ├── design-system.css       # Design tokens
│   └── components.css          # Component styles
├── types/
│   ├── index.ts                # TypeScript types
│   └── database.ts             # Database types
├── public/
│   ├── logo.png
│   └── assets/
├── .env.local                  # Environment variables
├── tailwind.config.ts          # Tailwind config
├── tsconfig.json               # TypeScript config
└── package.json                # Dependencies
```

### Page Flows

#### Portal (/)
```
┌─────────────────────────────────────────┐
│         PORTAL PAGE (/)                 │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Hero Section                   │   │
│  │  - Logo + Title                 │   │
│  │  - Vision statement             │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Module Cards (4 columns)       │   │
│  │  - Magazine                     │   │
│  │  - Votes                        │   │
│  │  - Directory                    │   │
│  │  - Contributors                 │   │
│  │  - Waitlist                     │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Featured Content               │   │
│  │  - Latest articles              │   │
│  │  - Top votes                    │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

#### Magazine (/magazine)
```
┌─────────────────────────────────────────┐
│      MAGAZINE PAGE (/magazine)          │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Filters & Search               │   │
│  │  - Topic filter                 │   │
│  │  - Search box                   │   │
│  │  - Sort (newest/popular)        │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Article List                   │   │
│  │  - Article cards (3 columns)    │   │
│  │  - Pagination                   │   │
│  │  - Load more                    │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
        │
        │ Click article
        ▼
┌─────────────────────────────────────────┐
│   ARTICLE DETAIL (/magazine/[id])       │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Article Header                 │   │
│  │  - Title                        │   │
│  │  - Author, Date                 │   │
│  │  - Topic badge                  │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Article Content                │   │
│  │  - Rich text                    │   │
│  │  - Images                       │   │
│  │  - Code blocks                  │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Related Articles               │   │
│  │  - 3 related articles           │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

#### Votes (/votes)
```
┌─────────────────────────────────────────┐
│        VOTES PAGE (/votes)              │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Vote Form                      │   │
│  │  - Username input               │   │
│  │  - Message (150 chars max)      │   │
│  │  - Submit button                │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Votes Feed                     │   │
│  │  - Sort: Top / Recent           │   │
│  │  - Vote cards                   │   │
│  │  - Up/Down voting               │   │
│  │  - Pagination                   │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

#### Admin (/admin)
```
┌─────────────────────────────────────────┐
│      ADMIN DASHBOARD (/admin)           │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Admin Navigation               │   │
│  │  - Articles                     │   │
│  │  - Votes                        │   │
│  │  - Directory                    │   │
│  │  - Contributors                 │   │
│  │  - Waitlist                     │   │
│  │  - Settings                     │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Content Management             │   │
│  │  - Create/Edit/Delete           │   │
│  │  - Publish/Draft status         │   │
│  │  - Image upload                 │   │
│  │  - Bulk actions                 │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

### API Routes

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
PUT    /api/directory/[id]        → Update entry (admin)
DELETE /api/directory/[id]        → Delete entry (admin)

GET    /api/contributors          → List contributors
POST   /api/contributors          → Create contributor (admin)
PUT    /api/contributors/[id]     → Update contributor (admin)

POST   /api/waitlist              → Join waitlist
GET    /api/waitlist              → List waitlist (admin)

POST   /api/auth/login            → Admin login
POST   /api/auth/logout           → Admin logout
```

### Flux: User Interactions

```
User visits platform
    ↓
Loads portal page
    ↓
Chooses module (Magazine, Votes, Directory, etc.)
    ↓
Interacts with content
    ├─ Magazine: Read articles
    ├─ Votes: Submit vote
    ├─ Directory: Browse AI tools
    ├─ Contributors: View profiles
    └─ Waitlist: Join waitlist
    ↓
Data saved to Supabase
    ↓
Page updates with new data
```

---

## 3. BACKEND - Supabase (PostgreSQL)

### Database Schema

```sql
-- Articles table
CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    content TEXT,
    topic_id UUID REFERENCES topics(id),
    status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID REFERENCES auth.users(id)
);

-- Videos table
CREATE TABLE videos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    youtube_url TEXT,
    related_article_id UUID REFERENCES articles(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Votes table
CREATE TABLE votes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL,
    content TEXT CHECK (char_length(content) <= 150),
    score INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- AI Directory table
CREATE TABLE ai_directory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    description TEXT,
    link TEXT,
    category TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Contributors table
CREATE TABLE contributors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    type TEXT CHECK (type IN ('thinker', 'developer', 'researcher', 'investor')),
    bio TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Waitlist table
CREATE TABLE waitlist (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    type TEXT,
    message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Topics table
CREATE TABLE topics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE
);

-- Comments table
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    related_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Row Level Security (RLS)

```sql
-- Public read access for published articles
CREATE POLICY "Public read articles" ON articles
    FOR SELECT USING (status = 'published');

-- Admin write access
CREATE POLICY "Admin write articles" ON articles
    FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Public read votes
CREATE POLICY "Public read votes" ON votes
    FOR SELECT USING (true);

-- Public create votes
CREATE POLICY "Public create votes" ON votes
    FOR INSERT WITH CHECK (true);
```

### Flux: Data Flow

```
Frontend (Vercel)
    ↓
API Route (/api/articles)
    ↓
Supabase Client
    ↓
PostgreSQL Query
    ↓
RLS Policy Check
    ↓
Return Data
    ↓
Frontend Updates UI
```

---

## 4. DESIGN SYSTEM

### Color Palette (from Logo.png)

```
Primary Background:  #0a0a0f (Almost black)
Secondary BG:        #0f0f1a (Dark blue-black)
Tertiary BG:         #1a1a2e (Slightly lighter)

Accent Gold:         #c9a962 (Warm gold)
Accent Beige:        #d4c4a8 (Light beige)
Accent Cream:        #f5f0e8 (Off-white cream)

Text Primary:        #ffffff (White)
Text Secondary:      #a0a0b0 (Light gray)
Text Muted:          #6b6b7b (Muted gray)

Border Default:      rgba(201, 169, 98, 0.2)
Border Hover:        rgba(201, 169, 98, 0.4)
```

### Typography

```
Display Font:  Playfair Display (serif)
Body Font:     Inter (sans-serif)

Sizes:
- xs:  0.75rem   (12px)
- sm:  0.875rem  (14px)
- base: 1rem     (16px)
- lg:  1.125rem  (18px)
- xl:  1.25rem   (20px)
- 2xl: 1.5rem    (24px)
- 3xl: 2rem      (32px)
- 4xl: 2.5rem    (40px)
```

### Components

#### Button
```tsx
// Primary
<button className="px-6 py-3 bg-accent-gold text-background-primary hover:bg-accent-cream transition-all">
  Button Text
</button>

// Secondary
<button className="px-6 py-3 border border-accent-gold text-accent-gold hover:bg-accent-gold hover:text-background-primary transition-all">
  Button Text
</button>
```

#### Card
```tsx
<div className="p-6 bg-background-secondary border border-border-default hover:border-accent-gold transition-all">
  <h3 className="text-xl font-display text-accent-gold mb-2">Title</h3>
  <p className="text-text-secondary">Description</p>
</div>
```

---

## 5. DEPLOYMENT FLOW

### GitHub Pages (Teaser)

```
1. Create gh-pages branch
2. Build static HTML/CSS/JS
3. Push to gh-pages
4. GitHub Pages auto-deploys
5. Available at: username.github.io/LAIRM
```

### Vercel (Platform)

```
1. Connect GitHub repository
2. Configure environment variables
3. Deploy on push to main
4. Auto-preview deployments
5. Available at: platform.lairm.org
```

### Supabase (Backend)

```
1. Create Supabase project
2. Run migrations
3. Configure RLS policies
4. Set up storage buckets
5. Configure authentication
```

---

## 6. SECURITY ARCHITECTURE

### Authentication

```
Admin Login
    ↓
Verify API Key
    ↓
Generate JWT Token
    ↓
Store in secure cookie
    ↓
Include in API requests
    ↓
Verify on backend
```

### Data Protection

```
- HTTPS only
- CORS configured
- Rate limiting
- Input validation
- SQL injection prevention (Supabase)
- XSS protection
```

---

## 7. PERFORMANCE OPTIMIZATION

### Frontend

```
- Static generation (SSG)
- Image optimization
- Code splitting
- Lazy loading
- Edge caching
```

### Backend

```
- Database indexing
- Query optimization
- Connection pooling
- Caching layer
- CDN for static assets
```

---

This comprehensive architecture provides:
- ✅ Professional teaser on GitHub Pages
- ✅ Dynamic platform on Vercel
- ✅ Scalable backend on Supabase
- ✅ Consistent design system
- ✅ Secure authentication
- ✅ Optimized performance