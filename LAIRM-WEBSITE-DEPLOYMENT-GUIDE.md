---
title: "LAIRM Website v2 - Deployment Guide"
type: guide
Status: Final
Version: 1.0
date_creation: 2024-03-18
last_updated: 2026-04-09
last_review: 2026-04-09
license: CC-BY-SA-4.0
---

# LAIRM WEBSITE v2 — DEPLOYMENT GUIDE

## QUICK START

### Option 1: Replace v1 with v2 (Recommended)

```bash
# 1. Navigate to website directory
cd LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-website/

# 2. Backup v1 files (optional)
mkdir backup-v1
cp index.html style.css main.js voting.js backup-v1/

# 3. Replace with v2
mv index-v2.html index.html
mv style-v2.css style.css
mv main-v2.js main.js
mv voting-v2.js voting.js

# 4. Verify files
ls -la *.html *.css *.js

# 5. Deploy to GitHub Pages
git add .
git commit -m "Deploy LAIRM Website v2 - Futuristic Legislative Interface"
git push origin main
```

### Option 2: Keep Both Versions

```bash
# Keep v1 as backup, deploy v2 as main
# No changes needed - just deploy v2 files alongside v1

# Deploy to GitHub Pages
git add index-v2.html style-v2.css main-v2.js voting-v2.js
git commit -m "Add LAIRM Website v2 - Futuristic Legislative Interface"
git push origin main
```

---

## DETAILED DEPLOYMENT STEPS

### Step 1: Prepare Files

**Files to Deploy**:
- `index-v2.html` (or `index.html` if replacing)
- `style-v2.css` (or `style.css` if replacing)
- `main-v2.js` (or `main.js` if replacing)
- `voting-v2.js` (or `voting.js` if replacing)
- `logo.svg` (existing, no changes)

### Step 2: Test Locally

```bash
# Option A: Using Python
python -m http.server 8000

# Option B: Using Node.js
npx http-server

# Option C: Using VS Code Live Server
# Right-click index.html → Open with Live Server

# Visit: http://localhost:8000
```

**Test Checklist**:
- [ ] Hero section loads with animations
- [ ] Counters animate from 0 to final values
- [ ] Axiom cards render correctly
- [ ] Search and filters work
- [ ] Axiom modal opens on click
- [ ] Voting proposals display
- [ ] Voting modal opens on click
- [ ] Vote buttons work
- [ ] Timeline displays correctly
- [ ] Navigation links scroll smoothly
- [ ] Mobile responsive (test at 768px, 480px)
- [ ] Console API works (`LAIRM.inspect()`)

### Step 3: Deploy to GitHub Pages

**Prerequisites**:
- GitHub account
- Git installed
- Repository: `selectess/lairm` or `selectess/lairm-website`

**Deployment Steps**:

```bash
# 1. Navigate to repository
cd /path/to/lairm-website

# 2. Add files
git add index-v2.html style-v2.css main-v2.js voting-v2.js

# 3. Commit changes
git commit -m "Deploy LAIRM Website v2 - Futuristic Legislative Interface

- Clear, minimal design
- Extensive animations
- Futuristic aesthetic
- Legislative theme
- Responsive mobile design
- Console API for developers"

# 4. Push to GitHub
git push origin main

# 5. Enable GitHub Pages (if not already enabled)
# Go to: https://github.com/selectess/lairm/settings/pages
# Select: main branch as source
# Save

# 6. Wait for deployment (usually < 1 minute)
# Site available at: https://selectess.github.io/lairm/
```

### Step 4: Verify Deployment

```bash
# Check deployment status
# Visit: https://github.com/selectess/lairm/deployments

# Test live site
# Visit: https://selectess.github.io/lairm/

# Test on mobile
# Use browser DevTools (F12) → Toggle device toolbar
# Test at: 768px (tablet), 480px (mobile)
```

---

## CUSTOM DOMAIN (Optional)

### Setup Custom Domain

```bash
# 1. Create CNAME file
echo "lairm.global" > CNAME

# 2. Add to git
git add CNAME
git commit -m "Add custom domain: lairm.global"
git push origin main

# 3. Update DNS records
# Go to your domain registrar
# Add CNAME record:
#   Name: @
#   Value: selectess.github.io
# Or:
#   Name: lairm
#   Value: selectess.github.io

# 4. Wait for DNS propagation (up to 24 hours)

# 5. Verify
# Visit: https://lairm.global
```

---

## TROUBLESHOOTING

### Issue: Site not loading

**Solution**:
1. Check GitHub Pages settings
2. Verify branch is set to `main`
3. Check file names (case-sensitive)
4. Clear browser cache (Ctrl+Shift+Delete)

### Issue: Styles not loading

**Solution**:
1. Check CSS file name matches HTML link
2. Verify file is in same directory
3. Check browser console for 404 errors
4. Clear browser cache

### Issue: JavaScript not working

**Solution**:
1. Check JS file names match HTML script tags
2. Verify files are in same directory
3. Check browser console for errors
4. Verify no syntax errors in JS files

### Issue: Animations not smooth

**Solution**:
1. Check browser supports CSS animations
2. Disable browser extensions
3. Check GPU acceleration is enabled
4. Test on different browser

### Issue: Mobile layout broken

**Solution**:
1. Check viewport meta tag in HTML
2. Verify CSS media queries
3. Test at exact breakpoints (768px, 480px)
4. Check touch target sizes (48px minimum)

---

## PERFORMANCE OPTIMIZATION

### Measure Performance

```bash
# Using Lighthouse (Chrome DevTools)
# 1. Open DevTools (F12)
# 2. Go to Lighthouse tab
# 3. Click "Analyze page load"
# 4. Review report

# Target scores:
# - Performance: 95+
# - Accessibility: 95+
# - Best Practices: 95+
# - SEO: 95+
```

### Optimize if Needed

```css
/* Reduce animation complexity */
/* Use will-change sparingly */
/* Optimize images */
/* Minify CSS and JS */
```

---

## MONITORING

### Setup Analytics

```html
<!-- Add to index.html before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Track Key Metrics

- Page views
- Unique visitors
- Bounce rate
- Time on page
- Click-through rate (CTR)
- Axiom searches
- Voting participation
- GitHub link clicks

---

## MAINTENANCE

### Regular Updates

```bash
# Check for updates monthly
git status

# Pull latest changes
git pull origin main

# Deploy updates
git add .
git commit -m "Update LAIRM Website"
git push origin main
```

### Backup Strategy

```bash
# Create backup before major changes
git tag -a v2.0 -m "LAIRM Website v2.0 - Futuristic Legislative Interface"
git push origin v2.0

# Restore from backup if needed
git checkout v2.0
```

---

## ROLLBACK PROCEDURE

### If v2 has issues

```bash
# Option 1: Restore v1 from backup
cp backup-v1/index.html .
cp backup-v1/style.css .
cp backup-v1/main.js .
cp backup-v1/voting.js .

git add .
git commit -m "Rollback to v1"
git push origin main

# Option 2: Revert to previous commit
git revert HEAD
git push origin main

# Option 3: Reset to specific tag
git checkout v1.0
git push origin main --force
```

---

## COMMUNICATION

### Announce Deployment

```markdown
# LAIRM Website v2 — Now Live! 🚀

We've completely redesigned the LAIRM website with a focus on:

✅ **Clear, minimal design** — Only essential information
✅ **Sophisticated animations** — Every element tells a story
✅ **Futuristic aesthetic** — Legislative interface from 2050
✅ **Legislative theme** — Governance flows, not marketing
✅ **Mobile responsive** — Perfect on all devices

## What's New

- Animated hero section with live counters
- Interactive axiom explorer with search/filters
- Real-time voting system with 3 active proposals
- Deployment timeline (2026-2030)
- Smooth scroll animations
- Console API for developers

## Try It Out

Visit: https://selectess.github.io/lairm/

Or explore in console:
```javascript
LAIRM.inspect()
LAIRM.printAxioms()
LAIRM.voting.getProposals()
```

## Feedback

We'd love to hear your thoughts! Open an issue on GitHub:
https://github.com/selectess/lairm/issues
```

---

## CHECKLIST

### Pre-Deployment
- [ ] All files created and tested
- [ ] Local testing completed
- [ ] Mobile responsive verified
- [ ] Console API working
- [ ] No console errors
- [ ] Performance acceptable
- [ ] Accessibility checked

### Deployment
- [ ] Files committed to git
- [ ] Commit message clear
- [ ] Pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Deployment completed

### Post-Deployment
- [ ] Live site verified
- [ ] All sections working
- [ ] Mobile layout correct
- [ ] Analytics tracking
- [ ] Announcement posted
- [ ] Feedback collected

---

## SUPPORT

### Need Help?

1. **Check Documentation**
   - LAIRM-WEBSITE-V2-SUMMARY.md
   - LAIRM-WEBSITE-REDESIGN-VISION.md

2. **Review Code**
   - index-v2.html (HTML structure)
   - style-v2.css (CSS styling)
   - main-v2.js (JavaScript logic)
   - voting-v2.js (Voting system)

3. **Test Locally**
   - Use local server
   - Check browser console
   - Test on multiple devices

4. **Contact**
   - Email: selectess@gmail.com
   - GitHub: https://github.com/selectess
   - Issues: https://github.com/selectess/lairm/issues

---

## CONCLUSION

LAIRM Website v2 is ready for deployment. Follow this guide to deploy successfully and monitor performance.

**Status**: ✅ **READY FOR DEPLOYMENT**

---

**Guide Created**: April 9, 2026  
**Version**: 1.0  
**Status**: Complete

