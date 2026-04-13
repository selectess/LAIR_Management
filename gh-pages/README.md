# LAIRM - GitHub Pages

Professional static website for LAIRM (Legislature for Autonomous Intelligent Resources Management).

## Overview

Minimalist, institutional website showcasing LAIR Management as a comprehensive framework for autonomous agent governance.

## Features

- ✅ Responsive design (mobile-first)
- ✅ Professional aesthetic (gold/blue on beige)
- ✅ Smooth scroll animations
- ✅ Fast performance (static HTML/CSS/JS)
- ✅ SEO optimized
- ✅ Accessible design

## Structure

```
gh-pages/
├── index.html          # Main page
├── css/
│   └── style.css       # Stylesheet
├── js/
│   └── main.js         # JavaScript
├── .nojekyll           # GitHub Pages config
└── README.md           # This file
```

## Sections

1. **Navigation** - Sticky header with logo and menu
2. **Hero** - Main title with CTA buttons
3. **Vision** - Problem statement with 3 cards
4. **Axioms** - 19 axioms in grid layout
5. **Framework** - 6 framework components
6. **Waitlist** - Email subscription form

## Design System

### Colors
- **Background**: #f5f0e8 (Beige), #ffffff (White)
- **Accent Gold**: #c9a962
- **Accent Blue**: #003366
- **Text**: #0a0a0f (Primary), #4a4a5a (Secondary)

### Typography
- **Display**: Playfair Display (serif)
- **Body**: Inter (sans-serif)

## Deployment

### GitHub Pages

1. Push to repository:
```bash
git add gh-pages/
git commit -m "Add: GitHub Pages website"
git push origin main
```

2. Enable GitHub Pages:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /gh-pages

3. Access at: `https://selectess.github.io/LAIR_Management/`

## Local Testing

```bash
cd gh-pages
python -m http.server 8000
# Visit http://localhost:8000
```

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: iOS Safari, Chrome Mobile

## License

CC-BY-SA-4.0

---

**LAIR Management - The Cybernetic Criterion**  
*Global Agentive Constitution 2026–2036*
