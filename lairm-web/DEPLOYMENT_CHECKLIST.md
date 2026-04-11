# ✅ Vercel Deployment Checklist

## Step 1: Answer Vercel CLI Prompts (IN YOUR TERMINAL NOW)

In your terminal, answer these prompts:

- [ ] **Which scope?** → Select your username
- [ ] **Link to existing project?** → Type `N` and press Enter
- [ ] **Project name?** → Type `lairm` and press Enter  
- [ ] **Directory?** → Press Enter (use default `./`)
- [ ] **Override settings?** → Type `N` and press Enter

⏳ **Wait 2-3 minutes for build to complete...**

---

## Step 2: Copy Your Production URL

When you see:
```
✅ Production: https://lairm-xxxxx.vercel.app
```

- [ ] **Copy this URL** (it's automatically copied to clipboard)
- [ ] **Save it somewhere** - you'll need it later

---

## Step 3: Add Environment Variables (AUTOMATED)

After the first deployment completes, run this script:

```bash
./setup-vercel-env.sh
```

This will:
1. Add `NEXT_PUBLIC_SUPABASE_URL`
2. Add `NEXT_PUBLIC_SUPABASE_ANON_KEY`
3. Automatically redeploy with the variables

⏳ **Wait 2-3 minutes for rebuild...**

---

## Step 4: Test Your Deployment

- [ ] Visit your production URL in browser
- [ ] Check landing page loads
- [ ] Navigate to `/manifesto`
- [ ] Navigate to `/platform`
- [ ] Navigate to `/admin`
- [ ] Test API: `curl https://your-url.vercel.app/api/articles`

---

## Step 5: Update GitHub Pages Teaser

```bash
# Go back to project root
cd ..

# Edit docs/index.html
# Find line 165 and replace with your actual Vercel URL
nano docs/index.html

# Or use this command (replace YOUR_URL):
sed -i '' 's|https://lairm.vercel.app|https://YOUR_ACTUAL_URL.vercel.app|g' docs/index.html

# Commit and push
git add docs/index.html
git commit -m "Update Vercel production URL in teaser page"
git push origin main
```

---

## Step 6: Enable GitHub Pages

- [ ] Go to: https://github.com/selectess/LAIR_Management/settings/pages
- [ ] Set Source: **Deploy from a branch**
- [ ] Set Branch: **main**
- [ ] Set Folder: **/docs**
- [ ] Click **Save**
- [ ] Wait 2-3 minutes

---

## 🎉 Final Result

After completing all steps:

✅ **GitHub Pages**: https://selectess.github.io/LAIR_Management/
✅ **Vercel Platform**: https://your-url.vercel.app
✅ **Supabase Backend**: Connected and working
✅ **Total Cost**: $0/month

---

## 🆘 If Something Goes Wrong

### Deployment fails?
```bash
# Check logs
vercel logs

# Try local build first
npm run build
```

### Environment variables not working?
```bash
# List current env vars
vercel env ls

# Remove and re-add
vercel env rm NEXT_PUBLIC_SUPABASE_URL production
./setup-vercel-env.sh
```

### Need to redeploy?
```bash
vercel --prod
```

---

## 📞 Quick Commands

```bash
# View deployment logs
vercel logs

# List all deployments
vercel ls

# Open project in browser
vercel open

# View environment variables
vercel env ls

# Redeploy
vercel --prod
```

---

## Current Status

- [x] Code complete
- [x] Supabase configured
- [ ] **→ YOU ARE HERE: Answering Vercel prompts**
- [ ] Add environment variables
- [ ] Update teaser page
- [ ] Enable GitHub Pages
