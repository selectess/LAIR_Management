# LAIRM Platform - Detailed Flux Diagrams

## 1. TEASER FLUX (GitHub Pages)

### User Journey Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER VISITS TEASER                       │
│              (GitHub Pages Static Site)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              BROWSER LOADS HTML/CSS/JS                      │
│                                                             │
│  1. Fetch index.html                                        │
│  2. Parse CSS (design-system.css)                           │
│  3. Load JavaScript (main.js)                               │
│  4. Render hero section                                     │
│  5. Initialize scroll animations                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  HERO SECTION DISPLAYED                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Logo (centered, gold on dark)                      │   │
│  │  Title: "The Cybernetic Criterion"                  │   │
│  │  Subtitle: "Global Agentive Constitution 2026-36"   │   │
│  │  CTA Button: "Explore Platform"                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Animations:                                                │
│  - Logo fade-in (300ms)                                     │
│  - Title slide-up (500ms)                                   │
│  - Button glow effect (infinite)                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  User scrolls   │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
    ┌──────────────────────┐  ┌──────────────────────┐
    │  VISION SECTION      │  │  AXIOMS GRID         │
    │  (3 columns)         │  │  (3x3 grid)          │
    │                      │  │                      │
    │  - Principles        │  │  - Ψ-I SUPREMATIA    │
    │  - Axioms            │  │  - Ψ-II IDENTITAS    │
    │  - Impact            │  │  - Ψ-III RESPONSAB.  │
    │                      │  │  - ... (9 total)     │
    │  Animations:         │  │                      │
    │  - Fade-in on scroll │  │  Interactions:       │
    │  - Stagger cards     │  │  - Hover: gold border│
    │  - Gold accents      │  │  - Click: details    │
    └──────────────────────┘  └──────────────────────┘
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │  CASE STUDIES SECTION    │
                │                          │
                │  - Knight Capital        │
                │  - Flash Crash           │
                │  - Boeing 737 MAX        │
                │                          │
                │  Animations:             │
                │  - Slide-in from left    │
                │  - Hover: expand detail  │
                └──────────────────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │  FOOTER SECTION          │
                │                          │
                │  - Links                 │
                │  - Social media          │
                │  - Copyright             │
                └──────────────────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │  USER CLICKS CTA BUTTON  │
                │  "Explore Platform"      │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │  REDIRECT TO VERCEL      │
                │  https://platform...     │
                └──────────────────────────┘
```

### Teaser Component Hierarchy

```
index.html
├── Header
│   ├── Logo
│   └── Navigation (minimal)
├── Hero Section
│   ├── Logo (large)
│   ├── Title
│   ├── Subtitle
│   └── CTA Button
├── Vision Section
│   ├── Column 1: Principles
│   ├── Column 2: Axioms
│   └── Column 3: Impact
├── Axioms Grid
│   ├── Axiom Card 1 (Ψ-I)
│   ├── Axiom Card 2 (Ψ-II)
│   ├── ... (9 cards total)
│   └── Axiom Card 9 (Ψ-IX)
├── Case Studies Section
│   ├── Case Study 1 (Knight Capital)
│   ├── Case Study 2 (Flash Crash)
│   └── Case Study 3 (Boeing 737 MAX)
└── Footer
    ├── Links
    ├── Social Media
    └── Copyright
```

---

## 2. PLATFORM FLUX (Vercel)

### Complete User Flow

```
┌─────────────────────────────────────────────────────────────┐
│              USER VISITS PLATFORM                           │
│                (Vercel Next.js App)                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│         NEXT.JS LOADS APP ROUTER                            │
│                                                             │
│  1. Load layout.tsx (root layout)                           │
│  2. Load page.tsx (portal page)                             │
│  3. Initialize Supabase client                              │
│  4. Fetch initial data                                      │
│  5. Render portal page                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              PORTAL PAGE DISPLAYED (/)                      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Header                                             │   │
│  │  - Logo                                             │   │
│  │  - Navigation (Magazine, Votes, Directory, etc.)    │   │
│  │  - Admin login (if applicable)                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Hero Section                                       │   │
│  │  - Welcome message                                  │   │
│  │  - Quick stats                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Module Cards (5 columns)                           │   │
│  │  - Magazine                                         │   │
│  │  - Votes                                            │   │
│  │  - Directory                                        │   │
│  │  - Contributors                                     │   │
│  │  - Waitlist                                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Featured Content                                   │   │
│  │  - Latest articles (3)                              │   │
│  │  - Top votes (3)                                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Footer                                             │   │
│  │  - Links                                            │   │
│  │  - Social media                                     │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
    ┌──────────────────┐  ┌──────────────┐  ┌──────────────┐
    │ MAGAZINE MODULE  │  │ VOTES MODULE │  │ DIRECTORY    │
    │ (/magazine)      │  │ (/votes)     │  │ (/directory) │
    └────────┬─────────┘  └──────┬───────┘  └──────┬───────┘
             │                   │                 │
             ▼                   ▼                 ▼
    ┌──────────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Article List     │  │ Vote Form    │  │ Directory    │
    │ - Filters        │  │ - Username   │  │ List         │
    │ - Search         │  │ - Message    │  │ - Categories │
    │ - Sort           │  │ - Submit     │  │ - Search     │
    │ - Pagination     │  │              │  │ - Filter     │
    │                  │  │ Vote Feed    │  │              │
    │ Article Cards    │  │ - Top votes  │  │ Directory    │
    │ - Title          │  │ - Recent     │  │ Cards        │
    │ - Excerpt        │  │ - Voting     │  │ - Name       │
    │ - Topic          │  │ - Pagination │  │ - Description│
    │ - Date           │  │              │  │ - Link       │
    │ - Click → Detail │  │              │  │ - Category   │
    └────────┬─────────┘  └──────────────┘  └──────────────┘
             │
             ▼
    ┌──────────────────────────┐
    │ ARTICLE DETAIL PAGE      │
    │ (/magazine/[id])         │
    │                          │
    │ - Article header         │
    │ - Full content           │
    │ - Images                 │
    │ - Related articles       │
    │ - Comments (optional)    │
    └──────────────────────────┘
```

### Magazine Module Detailed Flow

```
User clicks "Magazine"
    ↓
Navigate to /magazine
    ↓
┌─────────────────────────────────────────┐
│  FETCH ARTICLES FROM SUPABASE           │
│                                         │
│  GET /api/articles                      │
│  ├─ Query: status = 'published'         │
│  ├─ Limit: 12 per page                  │
│  ├─ Sort: created_at DESC               │
│  └─ Include: topic, author              │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  RENDER ARTICLE LIST                    │
│                                         │
│  - Display filters (topics)             │
│  - Display search box                   │
│  - Display sort options                 │
│  - Display article cards (3 columns)    │
│  - Display pagination                   │
└─────────────────────────────────────────┘
    ↓
    ├─ User filters by topic
    │   ├─ Query: topic_id = X
    │   └─ Re-fetch articles
    │
    ├─ User searches
    │   ├─ Query: title ILIKE '%search%'
    │   └─ Re-fetch articles
    │
    └─ User clicks article
        ├─ Navigate to /magazine/[id]
        ├─ Fetch article details
        ├─ Fetch related articles
        └─ Render article detail page
```

### Votes Module Detailed Flow

```
User clicks "Votes"
    ↓
Navigate to /votes
    ↓
┌─────────────────────────────────────────┐
│  RENDER VOTE FORM                       │
│                                         │
│  - Username input                       │
│  - Message textarea (150 chars max)     │
│  - Submit button                        │
│  - Character counter                    │
└─────────────────────────────────────────┘
    ↓
    ├─ User enters username
    │   └─ Validate: not empty
    │
    ├─ User enters message
    │   ├─ Validate: max 150 chars
    │   └─ Update character counter
    │
    └─ User clicks submit
        ├─ Validate form
        ├─ POST /api/votes
        │   ├─ Body: { username, content }
        │   └─ Response: { id, score, created_at }
        ├─ Clear form
        ├─ Show success message
        └─ Refresh vote feed
            ├─ GET /api/votes
            ├─ Sort: top (score DESC)
            ├─ Render vote cards
            └─ Enable up/down voting
                ├─ Click up arrow
                │   └─ PUT /api/votes/[id] { score: +1 }
                └─ Click down arrow
                    └─ PUT /api/votes/[id] { score: -1 }
```

### Admin Dashboard Flow

```
Admin clicks "Admin" in header
    ↓
Navigate to /admin
    ↓
┌─────────────────────────────────────────┐
│  CHECK AUTHENTICATION                   │
│                                         │
│  - Verify admin API key                 │
│  - Check JWT token                      │
│  - Verify role = 'admin'                │
└─────────────────────────────────────────┘
    ↓
    ├─ If not authenticated
    │   └─ Redirect to login
    │
    └─ If authenticated
        ├─ Render admin dashboard
        │   ├─ Navigation sidebar
        │   │   ├─ Articles
        │   │   ├─ Votes
        │   │   ├─ Directory
        │   │   ├─ Contributors
        │   │   ├─ Waitlist
        │   │   └─ Settings
        │   │
        │   └─ Main content area
        │       ├─ Articles management
        │       │   ├─ List all articles
        │       │   ├─ Create new
        │       │   ├─ Edit existing
        │       │   ├─ Delete
        │       │   ├─ Change status (draft/published)
        │       │   └─ Upload images
        │       │
        │       ├─ Votes management
        │       │   ├─ View all votes
        │       │   ├─ Moderate (delete if needed)
        │       │   └─ View statistics
        │       │
        │       ├─ Directory management
        │       │   ├─ Add/edit/delete entries
        │       │   └─ Manage categories
        │       │
        │       ├─ Contributors management
        │       │   ├─ Add/edit/delete profiles
        │       │   └─ Manage types
        │       │
        │       ├─ Waitlist management
        │       │   ├─ View all signups
        │       │   ├─ Export to CSV
        │       │   └─ Send emails
        │       │
        │       └─ Settings
        │           ├─ Site configuration
        │           ├─ API keys
        │           └─ Backup/restore
```

---

## 3. BACKEND FLUX (Supabase)

### Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (Vercel)                        │
│                                                             │
│  React Component                                            │
│  └─ useEffect(() => fetchArticles())                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    API ROUTE (Next.js)                      │
│                                                             │
│  /api/articles/route.ts                                     │
│  ├─ GET: Fetch articles                                     │
│  │   ├─ Parse query params (page, limit, topic)            │
│  │   ├─ Validate inputs                                     │
│  │   ├─ Call Supabase client                                │
│  │   └─ Return JSON response                                │
│  │                                                          │
│  ├─ POST: Create article (admin only)                       │
│  │   ├─ Verify admin API key                                │
│  │   ├─ Validate request body                               │
│  │   ├─ Call Supabase client                                │
│  │   └─ Return created article                              │
│  │                                                          │
│  └─ Error handling                                          │
│      ├─ 400: Bad request                                    │
│      ├─ 401: Unauthorized                                   │
│      ├─ 500: Server error                                   │
│      └─ Log to console                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  SUPABASE CLIENT                            │
│                                                             │
│  supabase.ts                                                │
│  ├─ Initialize Supabase client                              │
│  ├─ Set API key                                             │
│  ├─ Set database URL                                        │
│  └─ Configure auth                                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  SUPABASE API                               │
│                                                             │
│  REST API Endpoint                                          │
│  ├─ https://[project].supabase.co/rest/v1/articles          │
│  ├─ Headers: Authorization, Content-Type                    │
│  ├─ Query params: select, where, order, limit               │
│  └─ HTTP methods: GET, POST, PUT, DELETE                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  RLS POLICIES                               │
│                                                             │
│  Row Level Security                                         │
│  ├─ Check: status = 'published' (public read)               │
│  ├─ Check: auth.jwt() ->> 'role' = 'admin' (admin write)    │
│  └─ Enforce: Only authorized rows returned                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  POSTGRESQL DATABASE                        │
│                                                             │
│  articles table                                             │
│  ├─ id (UUID)                                               │
│  ├─ title (TEXT)                                            │
│  ├─ content (TEXT)                                          │
│  ├─ topic_id (UUID FK)                                      │
│  ├─ status (TEXT)                                           │
│  ├─ created_at (TIMESTAMPTZ)                                │
│  ├─ updated_at (TIMESTAMPTZ)                                │
│  └─ created_by (UUID FK)                                    │
│                                                             │
│  Indexes:                                                   │
│  ├─ PRIMARY KEY (id)                                        │
│  ├─ INDEX (status, created_at)                              │
│  ├─ INDEX (topic_id)                                        │
│  └─ FOREIGN KEY (topic_id) → topics(id)                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  RESPONSE FLOW                              │
│                                                             │
│  PostgreSQL returns rows                                    │
│  ↓                                                          │
│  RLS policies filter rows                                   │
│  ↓                                                          │
│  Supabase API formats JSON                                  │
│  ↓                                                          │
│  API route receives response                                │
│  ↓                                                          │
│  Frontend receives JSON                                     │
│  ↓                                                          │
│  React component updates state                              │
│  ↓                                                          │
│  UI re-renders with new data                                │
└─────────────────────────────────────────────────────────────┘
```

### CRUD Operations Flow

```
CREATE (POST /api/articles)
    ↓
Admin submits form
    ├─ Validate: title, content, topic
    ├─ POST /api/articles
    │   ├─ Verify admin key
    │   ├─ INSERT INTO articles
    │   │   ├─ id: gen_random_uuid()
    │   │   ├─ title: from form
    │   │   ├─ content: from form
    │   │   ├─ topic_id: from form
    │   │   ├─ status: 'draft'
    │   │   ├─ created_at: NOW()
    │   │   └─ created_by: admin_id
    │   └─ Return: created article
    └─ Show success message

READ (GET /api/articles)
    ↓
Frontend requests articles
    ├─ GET /api/articles?page=1&limit=12
    │   ├─ SELECT * FROM articles
    │   ├─ WHERE status = 'published'
    │   ├─ ORDER BY created_at DESC
    │   ├─ LIMIT 12 OFFSET 0
    │   └─ Return: array of articles
    └─ Render article list

UPDATE (PUT /api/articles/[id])
    ↓
Admin edits article
    ├─ Validate: title, content, topic
    ├─ PUT /api/articles/[id]
    │   ├─ Verify admin key
    │   ├─ UPDATE articles
    │   │   ├─ SET title = new_title
    │   │   ├─ SET content = new_content
    │   │   ├─ SET topic_id = new_topic
    │   │   ├─ SET updated_at = NOW()
    │   │   └─ WHERE id = [id]
    │   └─ Return: updated article
    └─ Show success message

DELETE (DELETE /api/articles/[id])
    ↓
Admin deletes article
    ├─ Confirm deletion
    ├─ DELETE /api/articles/[id]
    │   ├─ Verify admin key
    │   ├─ DELETE FROM articles
    │   │   └─ WHERE id = [id]
    │   └─ Return: success
    └─ Remove from list
```

---

## 4. AUTHENTICATION FLOW

```
┌─────────────────────────────────────────────────────────────┐
│                    ADMIN LOGIN                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Admin enters credentials                                   │
│  - Email                                                    │
│  - Password                                                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  POST /api/auth/login                                       │
│  - Validate email format                                    │
│  - Validate password strength                               │
│  - Query admin user from database                           │
│  - Compare password hash                                    │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
        ┌──────────────────┐        ┌──────────────────┐
        │  Invalid         │        │  Valid           │
        │  credentials     │        │  credentials     │
        │                  │        │                  │
        │  Return 401      │        │  Generate JWT    │
        │  Unauthorized    │        │  token           │
        └──────────────────┘        │                  │
                                    │  Set secure      │
                                    │  cookie          │
                                    │                  │
                                    │  Return 200 OK   │
                                    └────────┬─────────┘
                                             │
                                             ▼
                                    ┌──────────────────┐
                                    │  Store JWT in    │
                                    │  secure cookie   │
                                    │                  │
                                    │  Redirect to     │
                                    │  /admin          │
                                    └────────┬─────────┘
                                             │
                                             ▼
                                    ┌──────────────────┐
                                    │  Admin dashboard │
                                    │  loaded          │
                                    │                  │
                                    │  JWT included    │
                                    │  in all requests │
                                    └──────────────────┘
```

---

## 5. IMAGE UPLOAD FLOW

```
Admin uploads image
    ↓
┌─────────────────────────────────────────┐
│  File input change event                │
│  - Get file from input                  │
│  - Validate: type, size                 │
│  - Show preview                         │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  POST /api/upload                       │
│  - FormData with file                   │
│  - Verify admin key                     │
│  - Validate file                        │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Supabase Storage                       │
│  - Upload to bucket: 'articles'         │
│  - Generate unique filename             │
│  - Return public URL                    │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Return URL to frontend                 │
│  - Insert into article content          │
│  - Show in preview                      │
└─────────────────────────────────────────┘
```

---

## 6. REAL-TIME UPDATES (Optional)

```
┌─────────────────────────────────────────┐
│  Supabase Realtime Subscription         │
│                                         │
│  supabase                               │
│    .channel('articles')                 │
│    .on('postgres_changes',              │
│      { event: '*', schema: 'public' },  │
│      (payload) => {                     │
│        // Update UI                     │
│      }                                  │
│    )                                    │
│    .subscribe()                         │
└─────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
    INSERT     UPDATE      DELETE
        │           │           │
        └───────────┼───────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │  Broadcast to all    │
        │  connected clients   │
        │                      │
        │  Update UI in        │
        │  real-time           │
        └──────────────────────┘
```

---

This comprehensive flux documentation provides:
- ✅ Complete user journey flows
- ✅ Component hierarchies
- ✅ Data flow architecture
- ✅ CRUD operation flows
- ✅ Authentication flows
- ✅ File upload flows
- ✅ Real-time update patterns