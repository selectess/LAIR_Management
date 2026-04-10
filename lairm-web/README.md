# LAIRM Web Platform

The official web platform for the Legislature for Autonomous Intelligent Resources Management (LAIRM).

## 🚀 Features

- **Landing Page**: Futuristic hero with ImFro.jpeg image
- **Manifesto**: 19 Axioms, 361 Articles, 28 Chapters with video integration
- **Platform**: 5 integrated modules
  - Presentation
  - Magazine/Blog (5 articles/day)
  - Community Forum (Reddit-like voting)
  - AI Directory (127M+ agents catalog)
  - Contribution Hub
- **Admin Backoffice**: Full CRUD management
- **REST API**: Secure endpoints for remote management

## 🛠️ Tech Stack

- **Frontend**: Next.js 15 + React + TypeScript + Tailwind CSS
- **Backend**: Supabase (PostgreSQL + Auth + Storage + API)
- **Hosting**: Vercel (Free tier)
- **Cost**: $0/month (Free tier limits)

## 📦 Installation

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.local.example .env.local

# Edit .env.local with your Supabase credentials

# Run development server
npm run dev
```

## 🌐 Environment Variables

```env
NEXT_PUBLIC_SUPABASE_URL=your-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

## 📡 API Endpoints

### Articles
- `GET /api/articles` - List articles
- `POST /api/articles` - Create article
- `GET /api/articles/:id` - Get article
- `PUT /api/articles/:id` - Update article
- `DELETE /api/articles/:id` - Delete article

### AI Directory
- `GET /api/directory?type=agent` - List AI agents/models
- `POST /api/directory` - Add to directory

### Votes
- `GET /api/votes?axiom_id=PSI-I` - Get votes
- `POST /api/votes` - Submit vote (max 150 chars)

### Waitlist
- `GET /api/waitlist` - List waitlist
- `POST /api/waitlist` - Join waitlist

### Videos
- `GET /api/videos` - List videos
- `POST /api/videos` - Add video

## 🔐 Authentication

Currently using Supabase RLS policies:
- Public: Read access to published content
- Authenticated: Write access to all resources

## 📊 Database Schema

8 tables:
- `articles` - Blog/Magazine content
- `videos` - YouTube videos
- `ai_directory` - AI agents/models catalog
- `topics` - Forum discussions
- `comments` - Topic comments
- `votes` - Principle votes
- `waitlist` - Contributor waitlist
- `contributors` - Active contributors

## 🚢 Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables in Vercel dashboard
```

### Manual

```bash
# Build
npm run build

# Start
npm start
```

## 📝 Content Management

### Via Admin UI
Navigate to `/admin` for full backoffice interface

### Via API
```bash
# Create article
curl -X POST https://your-domain.com/api/articles \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Article Title",
    "content": "Article content...",
    "status": "published",
    "category": "legislation"
  }'
```

## 🎥 Video Integration

Add YouTube videos linked to axioms/articles:

```bash
curl -X POST https://your-domain.com/api/videos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Axiom I Explanation",
    "youtube_id": "dQw4w9WgXcQ",
    "axiom_id": "PSI-I",
    "description": "Detailed explanation..."
  }'
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📄 License

CC-BY-SA-4.0

## 📧 Contact

- **Email**: selectess@gmail.com
- **GitHub**: https://github.com/selectess/LAIR_Management
- **ORCID**: 0009-0007-0110-9437

---

**LAIRM - The Cybernetic Criterion**  
*Global Agentive Constitution 2026–2036*