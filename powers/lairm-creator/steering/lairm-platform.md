# LAIRM Platform Development Guidelines

## Platform Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB PAGES (Teaser)                    │
│         Static HTML/CSS/JS - Minimalist & Institutional     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    VERCEL (Platform)                        │
│              Next.js 14+ App Router                         │
│              Tailwind CSS + Design System                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SUPABASE (Backend)                       │
│     PostgreSQL + Auth + Storage + RLS + Realtime           │
└─────────────────────────────────────────────────────────────┘
```

## Pages Structure

### / (Portal)
- Hero section (coherent with teaser)
- Vision LAIRM
- Access modules: Magazine, Votes, Directory, Contributors, Waitlist

### /magazine
- Article list with filtering
- Dynamic article pages
- Topic-based navigation
- SEO optimized

### /votes
- Simple principle voting system
- Username + message (150 chars max)
- Up/down voting
- Sort by top/recent

### /directory
- AI Directory listing
- Categories: Tools, Frameworks, Models, Services
- External links
- Search and filter

### /contributors
- Contributor profiles
- Types: Thinker, Developer, Researcher, Investor
- Bio cards
- Contribution history

### /waitlist
- Multi-step form
- Name, Email, Type, Message
- Qualitative onboarding

### /manifesto
- Redirect to GitHub Pages

### /admin
- Backoffice central
- CRUD for all entities
- Publication/Draft status
- Image upload
- Moderation tools

## Database Schema

```sql
-- Articles
CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    content TEXT,
    topic_id UUID REFERENCES topics(id),
    status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Videos
CREATE TABLE videos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    youtube_url TEXT,
    related_article_id UUID REFERENCES articles(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
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

-- Comments
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    related_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## API Routes

### /api/articles
- GET: List articles
- POST: Create article (admin)
- PUT: Update article (admin)
- DELETE: Delete article (admin)

### /api/votes
- GET: List votes
- POST: Create vote
- PUT: Update vote score

### /api/directory
- GET: List directory entries
- POST: Create entry (admin)
- PUT: Update entry (admin)
- DELETE: Delete entry (admin)

### /api/waitlist
- GET: List waitlist (admin)
- POST: Join waitlist

### /api/contributors
- GET: List contributors
- POST: Create contributor (admin)
- PUT: Update contributor (admin)

## Design System Implementation

### Tailwind Config
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        background: {
          primary: '#0a0a0f',
          secondary: '#0f0f1a',
          tertiary: '#1a1a2e',
        },
        accent: {
          gold: '#c9a962',
          beige: '#d4c4a8',
          cream: '#f5f0e8',
        },
        text: {
          primary: '#ffffff',
          secondary: '#a0a0b0',
          muted: '#6b6b7b',
        },
        border: {
          DEFAULT: 'rgba(201, 169, 98, 0.2)',
          hover: 'rgba(201, 169, 98, 0.4)',
        },
      },
      fontFamily: {
        display: ['Playfair Display', 'Georgia', 'serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
}
```

### Component Examples

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

#### Input
```tsx
<input
  type="text"
  className="w-full px-4 py-3 bg-background-secondary border border-border-default focus:border-accent-gold text-text-primary outline-none transition-colors"
  placeholder="Placeholder"
/>
```

## Security

### Row Level Security (RLS)
```sql
-- Public read access
CREATE POLICY "Public read" ON articles FOR SELECT USING (status = 'published');

-- Admin write access
CREATE POLICY "Admin write" ON articles FOR ALL USING (auth.jwt() ->> 'role' = 'admin');
```

### API Security
- Admin API key for write operations
- Rate limiting
- Input validation
- CORS configuration

## Deployment

### GitHub Pages (Teaser)
1. Build static HTML
2. Deploy to gh-pages branch
3. Configure custom domain (optional)

### Vercel (Platform)
1. Connect GitHub repository
2. Configure environment variables
3. Set up preview deployments
4. Configure production domain

### Supabase (Backend)
1. Create project
2. Run migrations
3. Configure RLS policies
4. Set up storage buckets
5. Configure authentication

## Performance

### Optimization
- Static generation where possible
- Image optimization (Next.js Image)
- Code splitting
- Lazy loading
- Edge caching

### Monitoring
- Vercel Analytics
- Supabase Dashboard
- Error tracking (Sentry)