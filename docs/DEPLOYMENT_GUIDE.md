---
title: "LAIRM Platform - Complete Deployment Guide"
date_creation: 2026-04-12
last_updated: 2026-04-12
version: "1.0.0"
---

# LAIRM Platform - Complete Deployment Guide

## Overview

This guide covers the complete deployment of the LAIRM platform across three components:
1. **GitHub Pages Teaser** (Static HTML/CSS/JS)
2. **Vercel Platform** (Next.js 14+)
3. **Supabase Backend** (PostgreSQL)

## Prerequisites

- GitHub account with repository access
- Vercel account (free tier available)
- Supabase account (free tier available)
- Node.js 18+ installed locally
- Git installed locally

## Phase 1: Supabase Backend Setup

### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Click "New Project"
3. Fill in project details:
   - **Name**: `lairm-platform`
   - **Database Password**: Generate strong password
   - **Region**: Choose closest to your users
4. Click "Create new project"
5. Wait for project initialization (5-10 minutes)

### Step 2: Create Database Tables

1. In Supabase dashboard, go to "SQL Editor"
2. Click "New Query"
3. Copy and paste content from `lairm-web/supabase/migrations/001_create_tables.sql`
4. Click "Run"
5. Verify all tables created successfully

### Step 3: Enable Row Level Security

1. In SQL Editor, click "New Query"
2. Copy and paste content from `lairm-web/supabase/migrations/002_create_rls_policies.sql`
3. Click "Run"
4. Verify all policies created

### Step 4: Get API Keys

1. Go to "Settings" → "API"
2. Copy these values:
   - **Project URL**: `NEXT_PUBLIC_SUPABASE_URL`
   - **Anon Key**: `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - **Service Role Key**: `SUPABASE_SERVICE_ROLE_KEY`
3. Save these securely (you'll need them for Vercel)

### Step 5: Create Storage Bucket (Optional)

1. Go to "Storage" → "New Bucket"
2. Name: `articles`
3. Make public: Yes
4. Click "Create bucket"

## Phase 2: Vercel Platform Deployment

### Step 1: Prepare Repository

```bash
# Navigate to project
cd lairm-web

# Create .env.local with your Supabase keys
cat > .env.local << EOF
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
ADMIN_API_KEY=your-secure-admin-key
NEXT_PUBLIC_APP_URL=https://your-domain.com
EOF

# Install dependencies
npm install

# Build locally to verify
npm run build

# Test locally
npm run dev
# Visit http://localhost:3000
```

### Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial LAIRM platform commit"

# Add remote
git remote add origin https://github.com/your-username/lairm-platform.git

# Push to main branch
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Select "Import Git Repository"
4. Search for your repository and click "Import"
5. Configure project:
   - **Framework Preset**: Next.js
   - **Root Directory**: `lairm-web`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

### Step 4: Add Environment Variables

In Vercel project settings, go to "Environment Variables" and add:

```
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
ADMIN_API_KEY=your-secure-admin-key
NEXT_PUBLIC_APP_URL=https://your-vercel-domain.vercel.app
```

### Step 5: Deploy

1. Click "Deploy"
2. Wait for build to complete (2-5 minutes)
3. Verify deployment at provided URL
4. Test all pages and API routes

### Step 6: Configure Custom Domain (Optional)

1. In Vercel project, go to "Settings" → "Domains"
2. Add your custom domain
3. Follow DNS configuration instructions
4. Wait for DNS propagation (up to 48 hours)

## Phase 3: GitHub Pages Teaser (Optional)

### Step 1: Create gh-pages Branch

```bash
# Create new branch
git checkout --orphan gh-pages

# Remove all files
git rm -rf .

# Create teaser files (see TEASER_IMPLEMENTATION.md)
# ... add index.html, css/, js/, assets/

# Commit
git add .
git commit -m "Initial GitHub Pages teaser"

# Push
git push -u origin gh-pages
```

### Step 2: Enable GitHub Pages

1. Go to GitHub repository settings
2. Scroll to "GitHub Pages"
3. Select "Deploy from a branch"
4. Select `gh-pages` branch
5. Click "Save"
6. Visit `https://your-username.github.io/lairm-platform/`

## Post-Deployment Verification

### Test Checklist

- [ ] Homepage loads correctly
- [ ] Navigation works on all pages
- [ ] Magazine page displays articles
- [ ] Votes page allows submissions
- [ ] Directory page shows entries
- [ ] Contributors page displays profiles
- [ ] Waitlist form submits successfully
- [ ] API routes respond correctly
- [ ] Database queries work
- [ ] Images load properly
- [ ] Mobile responsive design works
- [ ] Performance is acceptable

### API Testing

```bash
# Test articles endpoint
curl https://your-domain.com/api/articles

# Test votes endpoint
curl https://your-domain.com/api/votes

# Test waitlist submission
curl -X POST https://your-domain.com/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@example.com","type":"individual"}'
```

### Performance Testing

1. Use Vercel Analytics dashboard
2. Check Core Web Vitals
3. Monitor database query performance
4. Review error logs

## Monitoring & Maintenance

### Daily Tasks

- Check error logs in Vercel
- Monitor database performance in Supabase
- Review user submissions (votes, waitlist)

### Weekly Tasks

- Review analytics
- Check for security updates
- Backup database (Supabase handles this)
- Review API usage

### Monthly Tasks

- Update dependencies
- Review and optimize slow queries
- Analyze user feedback
- Plan feature improvements

## Troubleshooting

### Build Fails

```bash
# Clear cache and rebuild
vercel rebuild

# Check build logs in Vercel dashboard
# Look for missing environment variables
# Verify Node.js version compatibility
```

### Database Connection Issues

1. Verify Supabase URL and keys are correct
2. Check RLS policies aren't blocking queries
3. Verify network access in Supabase settings
4. Check database connection limits

### Performance Issues

1. Enable caching in Vercel
2. Optimize database queries
3. Use ISR (Incremental Static Regeneration)
4. Implement pagination for large datasets

### CORS Errors

1. Check Supabase CORS settings
2. Verify API routes are properly configured
3. Check browser console for specific errors

## Scaling Considerations

### When to Scale

- **Traffic**: > 1000 requests/day
- **Data**: > 100,000 records
- **Users**: > 10,000 active users

### Scaling Options

1. **Vercel Pro**: Increased build minutes, priority support
2. **Supabase Pro**: Increased database size, priority support
3. **CDN**: Add Cloudflare for edge caching
4. **Database**: Upgrade Supabase plan or migrate to managed PostgreSQL

## Security Checklist

- [ ] All environment variables are secure
- [ ] Admin API key is strong and rotated regularly
- [ ] HTTPS is enforced
- [ ] CORS is properly configured
- [ ] RLS policies are correctly implemented
- [ ] Input validation is in place
- [ ] Rate limiting is configured
- [ ] Error messages don't leak sensitive info
- [ ] Database backups are automated
- [ ] Access logs are monitored

## Rollback Procedure

If deployment has critical issues:

```bash
# Revert to previous commit
git revert HEAD

# Push to main
git push origin main

# Vercel will automatically redeploy
# Monitor deployment in Vercel dashboard
```

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **Supabase Docs**: https://supabase.com/docs
- **Next.js Docs**: https://nextjs.org/docs
- **GitHub Pages Docs**: https://pages.github.com

## Next Steps

1. Set up monitoring and alerting
2. Configure email notifications
3. Implement analytics
4. Plan content strategy
5. Prepare marketing launch

---

**Deployment Status**: Ready for Production  
**Last Updated**: 2026-04-12  
**Version**: 1.0.0
