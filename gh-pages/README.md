# LAIRM Teaser - GitHub Pages

Professional static teaser website for LAIRM (Legislature for Autonomous Intelligent Resources Management).

## Overview

This is a minimalist, institutional teaser website showcasing:
- Hero section with key statistics
- Vision statement
- 9 fundamental axioms (Ψ-I to Ψ-IX)
- Case studies demonstrating governance failures
- Call-to-action for platform and GitHub

## Features

- ✅ Responsive design (mobile-first)
- ✅ Professional aesthetic (gold/beige on dark)
- ✅ Smooth animations and transitions
- ✅ Fast performance (static HTML/CSS/JS)
- ✅ SEO optimized
- ✅ Accessible design

## File Structure

```
gh-pages/
├── index.html          # Main page
├── css/
│   ├── style.css       # Main stylesheet
│   └── animations.css  # Animation definitions
├── js/
│   └── main.js         # JavaScript functionality
└── README.md           # This file
```

## Design System

### Colors
- **Primary Background**: #0a0a0f (Deep Black)
- **Secondary Background**: #12121a (Dark Navy)
- **Accent Gold**: #c9a962 (Warm Gold)
- **Accent Beige**: #d4c4a8 (Soft Beige)
- **Text Primary**: #faf8f5 (Off-White)
- **Text Secondary**: #a8a5a0 (Light Gray)

### Typography
- **Display Font**: Playfair Display (Serif)
- **Body Font**: Inter (Sans-serif)

### Components
- Navigation bar (sticky)
- Hero section with stats
- Axiom cards (9 items)
- Case study cards (3 items)
- CTA buttons
- Footer with links

## Sections

### 1. Navigation
- Logo and tagline
- Navigation links (Axioms, Vision, Platform, GitHub)
- Sticky positioning with scroll effects

### 2. Hero Section
- Main title (LAIRM)
- Subtitle (The Cybernetic Criterion)
- Description
- Statistics grid (19 Axioms, 361 Articles, 28 Chapters, 127M+ Agents)
- CTA buttons (Manifesto, Platform)

### 3. Vision Section
- Explanation of LAIRM's purpose
- Context about autonomous agents
- Call to action

### 4. Axioms Section
- Grid of 9 fundamental axioms
- Each axiom card shows:
  - Axiom number (Ψ-I to Ψ-IX)
  - Latin name
  - Description
- Note about Volume II axioms

### 5. Case Studies Section
- 3 real-world incidents:
  - Knight Capital (2012)
  - Flash Crash (2010)
  - Boeing 737 MAX (2018-2019)
- Shows impact and governance gap

### 6. CTA Section
- Call to join waitlist
- Link to contribute on GitHub

### 7. Footer
- Brand information
- Resource links
- Legal information
- Copyright notice

## Animations

- **Fade-in**: Hero title
- **Slide-up**: Hero subtitle, description, stats, buttons
- **Scroll animations**: Axiom cards and case study cards
- **Hover effects**: Cards and buttons
- **Glow effects**: Gold accents

## Responsive Design

- Mobile-first approach
- Breakpoints:
  - Mobile: < 768px
  - Tablet: 768px - 1024px
  - Desktop: > 1024px

## Performance

- Static HTML/CSS/JS (no build required)
- Minimal dependencies (Google Fonts only)
- Fast load times
- Optimized for all devices

## Deployment

### GitHub Pages

1. Push to `gh-pages` branch:
```bash
git checkout gh-pages
git add .
git commit -m "Add LAIRM teaser"
git push origin gh-pages
```

2. Enable GitHub Pages in repository settings:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: gh-pages
   - Folder: / (root)

3. Access at: `https://your-username.github.io/LAIR_Management/`

### Local Testing

Simply open `index.html` in a browser:
```bash
open gh-pages/index.html
```

Or use a local server:
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

## Accessibility

- Semantic HTML
- WCAG AA compliant
- High contrast colors
- Keyboard navigation
- Screen reader friendly

## SEO

- Meta tags (title, description, keywords)
- Open Graph tags
- Semantic HTML structure
- Mobile-friendly design
- Fast load times

## Customization

### Colors
Edit CSS variables in `css/style.css`:
```css
:root {
  --accent-gold: #c9a962;
  --accent-beige: #d4c4a8;
  /* ... */
}
```

### Content
Edit text in `index.html`:
- Hero section
- Axiom descriptions
- Case study details
- Footer links

### Fonts
Change in `index.html` `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
```

## Performance Optimization

- Minify CSS/JS for production
- Optimize images (if added)
- Use CDN for fonts
- Enable gzip compression
- Cache static assets

## Future Enhancements

- [ ] Add axiom detail pages
- [ ] Add blog section
- [ ] Add newsletter signup
- [ ] Add language selector
- [ ] Add dark/light mode toggle
- [ ] Add search functionality
- [ ] Add analytics

## Support

- **GitHub**: https://github.com/selectess/LAIR_Management
- **Email**: selectess@gmail.com
- **Documentation**: https://selectess.github.io/lairm/

## License

CC-BY-SA-4.0

---

**LAIRM - The Cybernetic Criterion**  
*Global Agentive Constitution 2026–2036*
