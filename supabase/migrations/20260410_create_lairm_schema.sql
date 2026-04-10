-- LAIRM Platform Database Schema
-- Created: 2026-04-10

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Articles table (blog/magazine)
CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL,
    excerpt TEXT,
    author_id UUID REFERENCES auth.users(id),
    status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
    category TEXT,
    tags TEXT[],
    featured_image TEXT,
    video_url TEXT,
    view_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    published_at TIMESTAMPTZ
);

-- AI Directory table
CREATE TABLE ai_directory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('agent', 'model', 'framework', 'tool')),
    description TEXT,
    website TEXT,
    documentation_url TEXT,
    github_url TEXT,
    logo_url TEXT,
    category TEXT,
    tags TEXT[],
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'deprecated', 'beta')),
    rating DECIMAL(3,2),
    usage_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Votes table (principle agreements)
CREATE TABLE votes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_identifier TEXT NOT NULL, -- @username from social
    message TEXT NOT NULL CHECK (LENGTH(message) <= 150),
    axiom_id TEXT, -- e.g., "PSI-I", "PSI-II"
    article_id TEXT, -- e.g., "I-01-01"
    vote_type TEXT NOT NULL CHECK (vote_type IN ('agree', 'disagree', 'abstain')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_identifier, axiom_id, article_id)
);

-- Waitlist table
CREATE TABLE waitlist (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    role TEXT, -- contributor type
    expertise TEXT[],
    message TEXT,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Contributors table
CREATE TABLE contributors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id),
    name TEXT NOT NULL,
    bio TEXT,
    avatar_url TEXT,
    expertise TEXT[],
    role TEXT, -- legal, technical, ethical, etc.
    github_url TEXT,
    linkedin_url TEXT,
    website TEXT,
    contribution_count INTEGER DEFAULT 0,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Topics/Discussions table
CREATE TABLE topics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author_id UUID REFERENCES auth.users(id),
    category TEXT,
    tags TEXT[],
    upvotes INTEGER DEFAULT 0,
    downvotes INTEGER DEFAULT 0,
    comment_count INTEGER DEFAULT 0,
    status TEXT DEFAULT 'open' CHECK (status IN ('open', 'closed', 'archived')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Comments table
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    topic_id UUID REFERENCES topics(id) ON DELETE CASCADE,
    parent_id UUID REFERENCES comments(id) ON DELETE CASCADE,
    author_id UUID REFERENCES auth.users(id),
    content TEXT NOT NULL,
    upvotes INTEGER DEFAULT 0,
    downvotes INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Videos table
CREATE TABLE videos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    youtube_id TEXT UNIQUE NOT NULL,
    description TEXT,
    axiom_id TEXT,
    article_id TEXT,
    thumbnail_url TEXT,
    duration INTEGER, -- in seconds
    view_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes for performance
CREATE INDEX idx_articles_status ON articles(status);
CREATE INDEX idx_articles_published_at ON articles(published_at DESC);
CREATE INDEX idx_articles_slug ON articles(slug);
CREATE INDEX idx_ai_directory_type ON ai_directory(type);
CREATE INDEX idx_ai_directory_category ON ai_directory(category);
CREATE INDEX idx_votes_axiom ON votes(axiom_id);
CREATE INDEX idx_votes_article ON votes(article_id);
CREATE INDEX idx_topics_category ON topics(category);
CREATE INDEX idx_topics_created_at ON topics(created_at DESC);
CREATE INDEX idx_comments_topic ON comments(topic_id);
CREATE INDEX idx_videos_axiom ON videos(axiom_id);

-- Enable Row Level Security
ALTER TABLE articles ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_directory ENABLE ROW LEVEL SECURITY;
ALTER TABLE votes ENABLE ROW LEVEL SECURITY;
ALTER TABLE waitlist ENABLE ROW LEVEL SECURITY;
ALTER TABLE contributors ENABLE ROW LEVEL SECURITY;
ALTER TABLE topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE comments ENABLE ROW LEVEL SECURITY;
ALTER TABLE videos ENABLE ROW LEVEL SECURITY;

-- RLS Policies (public read, authenticated write)
CREATE POLICY "Articles are viewable by everyone" ON articles FOR SELECT USING (status = 'published');
CREATE POLICY "Articles are editable by authenticated users" ON articles FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "AI Directory is viewable by everyone" ON ai_directory FOR SELECT USING (true);
CREATE POLICY "AI Directory is editable by authenticated users" ON ai_directory FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Votes are viewable by everyone" ON votes FOR SELECT USING (true);
CREATE POLICY "Anyone can vote" ON votes FOR INSERT WITH CHECK (true);

CREATE POLICY "Waitlist is insertable by anyone" ON waitlist FOR INSERT WITH CHECK (true);
CREATE POLICY "Waitlist is viewable by authenticated users" ON waitlist FOR SELECT USING (auth.role() = 'authenticated');

CREATE POLICY "Contributors are viewable by everyone" ON contributors FOR SELECT USING (status = 'active');
CREATE POLICY "Contributors are editable by authenticated users" ON contributors FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Topics are viewable by everyone" ON topics FOR SELECT USING (true);
CREATE POLICY "Topics are creatable by authenticated users" ON topics FOR INSERT WITH CHECK (auth.role() = 'authenticated');

CREATE POLICY "Comments are viewable by everyone" ON comments FOR SELECT USING (true);
CREATE POLICY "Comments are creatable by authenticated users" ON comments FOR INSERT WITH CHECK (auth.role() = 'authenticated');

CREATE POLICY "Videos are viewable by everyone" ON videos FOR SELECT USING (true);
CREATE POLICY "Videos are editable by authenticated users" ON videos FOR ALL USING (auth.role() = 'authenticated');