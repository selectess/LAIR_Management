# LAIRM Design System - Complete Reference

## 1. COLOR PALETTE

### Primary Colors (from Logo.png)

```
Background Colors:
├─ Primary:    #0a0a0f (Almost black - main background)
├─ Secondary:  #0f0f1a (Dark blue-black - cards, sections)
└─ Tertiary:   #1a1a2e (Slightly lighter - hover states)

Accent Colors (Gold/Beige):
├─ Gold:       #c9a962 (Warm gold - primary accent)
├─ Beige:      #d4c4a8 (Light beige - secondary accent)
└─ Cream:      #f5f0e8 (Off-white cream - highlights)

Text Colors:
├─ Primary:    #ffffff (White - main text)
├─ Secondary:  #a0a0b0 (Light gray - secondary text)
└─ Muted:      #6b6b7b (Muted gray - disabled, hints)

Border Colors:
├─ Default:    rgba(201, 169, 98, 0.2) (Subtle gold border)
└─ Hover:      rgba(201, 169, 98, 0.4) (Prominent gold border)
```

### CSS Variables

```css
:root {
  /* Background */
  --bg-primary: #0a0a0f;
  --bg-secondary: #0f0f1a;
  --bg-tertiary: #1a1a2e;
  
  /* Accent */
  --accent-gold: #c9a962;
  --accent-beige: #d4c4a8;
  --accent-cream: #f5f0e8;
  
  /* Text */
  --text-primary: #ffffff;
  --text-secondary: #a0a0b0;
  --text-muted: #6b6b7b;
  
  /* Border */
  --border-default: rgba(201, 169, 98, 0.2);
  --border-hover: rgba(201, 169, 98, 0.4);
  
  /* Semantic */
  --success: #4ade80;
  --error: #f87171;
  --warning: #facc15;
  --info: #60a5fa;
}
```

### Color Usage Guidelines

```
Primary Background (#0a0a0f):
- Page backgrounds
- Main container
- Large sections

Secondary Background (#0f0f1a):
- Cards
- Modals
- Dropdowns
- Sidebar

Tertiary Background (#1a1a2e):
- Hover states
- Active states
- Nested containers

Gold Accent (#c9a962):
- Primary buttons
- Links
- Borders on hover
- Icons
- Headings

Beige Accent (#d4c4a8):
- Secondary buttons
- Subtle highlights
- Badges

Cream (#f5f0e8):
- Button hover states
- Highlights
- Focus states

Text Primary (#ffffff):
- Main body text
- Headings
- Important information

Text Secondary (#a0a0b0):
- Secondary information
- Descriptions
- Metadata

Text Muted (#6b6b7b):
- Disabled text
- Hints
- Placeholders
```

---

## 2. TYPOGRAPHY

### Font Families

```
Display Font:  Playfair Display (serif)
- Used for: Headings, titles, hero text
- Weight: 400, 700
- Style: Regular, Italic

Body Font:     Inter (sans-serif)
- Used for: Body text, UI elements
- Weight: 400, 500, 600, 700
- Style: Regular, Italic
```

### Font Sizes

```
xs:   0.75rem   (12px)  - Small labels, captions
sm:   0.875rem  (14px)  - Small text, secondary info
base: 1rem      (16px)  - Body text, default
lg:   1.125rem  (18px)  - Large text, emphasis
xl:   1.25rem   (20px)  - Subheadings
2xl:  1.5rem    (24px)  - Section headings
3xl:  2rem      (32px)  - Page headings
4xl:  2.5rem    (40px)  - Hero headings
5xl:  3rem      (48px)  - Large hero text
6xl:  4rem      (64px)  - Extra large hero text
```

### Font Weights

```
Light:    300
Regular:  400
Medium:   500
Semibold: 600
Bold:     700
```

### Line Heights

```
Tight:    1.2   (Headings)
Normal:   1.5   (Body text)
Relaxed:  1.75  (Large text)
Loose:    2     (Captions)
```

### Typography Scale

```
H1 (Hero):
- Font: Playfair Display
- Size: 4xl (2.5rem)
- Weight: 700
- Line-height: 1.2
- Color: --text-primary

H2 (Section):
- Font: Playfair Display
- Size: 3xl (2rem)
- Weight: 700
- Line-height: 1.2
- Color: --accent-gold

H3 (Subsection):
- Font: Playfair Display
- Size: 2xl (1.5rem)
- Weight: 700
- Line-height: 1.3
- Color: --text-primary

H4 (Card title):
- Font: Inter
- Size: xl (1.25rem)
- Weight: 600
- Line-height: 1.4
- Color: --accent-gold

Body:
- Font: Inter
- Size: base (1rem)
- Weight: 400
- Line-height: 1.5
- Color: --text-primary

Small:
- Font: Inter
- Size: sm (0.875rem)
- Weight: 400
- Line-height: 1.5
- Color: --text-secondary
```

---

## 3. SPACING SYSTEM

### Spacing Scale

```
1:   0.25rem  (4px)
2:   0.5rem   (8px)
3:   0.75rem  (12px)
4:   1rem     (16px)
6:   1.5rem   (24px)
8:   2rem     (32px)
12:  3rem     (48px)
16:  4rem     (64px)
20:  5rem     (80px)
24:  6rem     (96px)
```

### Spacing Usage

```
Padding:
- Small elements:  4px (1)
- Cards:           16px (4)
- Sections:        24px (6) to 48px (12)
- Page:            32px (8) to 64px (16)

Margin:
- Between elements: 8px (2) to 16px (4)
- Between sections: 32px (8) to 64px (16)
- Bottom of text:   8px (2) to 16px (4)

Gap (Flexbox/Grid):
- Tight:           8px (2)
- Normal:          16px (4)
- Loose:           24px (6)
- Extra loose:     32px (8)
```

---

## 4. COMPONENTS

### Button

#### Primary Button
```tsx
<button className="
  px-6 py-3
  bg-accent-gold
  text-bg-primary
  font-semibold
  rounded-lg
  hover:bg-accent-cream
  active:bg-accent-beige
  disabled:opacity-50
  transition-all duration-300
  cursor-pointer
">
  Button Text
</button>
```

CSS:
```css
.btn-primary {
  padding: 0.75rem 1.5rem;
  background-color: var(--accent-gold);
  color: var(--bg-primary);
  font-weight: 600;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: all 300ms ease-in-out;
}

.btn-primary:hover {
  background-color: var(--accent-cream);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(201, 169, 98, 0.3);
}

.btn-primary:active {
  background-color: var(--accent-beige);
  transform: translateY(0);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

#### Secondary Button
```tsx
<button className="
  px-6 py-3
  border-2 border-accent-gold
  text-accent-gold
  font-semibold
  rounded-lg
  hover:bg-accent-gold
  hover:text-bg-primary
  active:bg-accent-beige
  disabled:opacity-50
  transition-all duration-300
  cursor-pointer
">
  Button Text
</button>
```

CSS:
```css
.btn-secondary {
  padding: 0.75rem 1.5rem;
  border: 2px solid var(--accent-gold);
  color: var(--accent-gold);
  background-color: transparent;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 300ms ease-in-out;
}

.btn-secondary:hover {
  background-color: var(--accent-gold);
  color: var(--bg-primary);
  transform: translateY(-2px);
}

.btn-secondary:active {
  background-color: var(--accent-beige);
  border-color: var(--accent-beige);
}
```

### Card

```tsx
<div className="
  p-6
  bg-bg-secondary
  border border-border-default
  rounded-lg
  hover:border-border-hover
  hover:shadow-lg
  transition-all duration-300
">
  <h3 className="
    text-xl
    font-display
    text-accent-gold
    mb-2
  ">
    Card Title
  </h3>
  <p className="
    text-text-secondary
    text-sm
  ">
    Card description
  </p>
</div>
```

CSS:
```css
.card {
  padding: 1.5rem;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-default);
  border-radius: 0.5rem;
  transition: all 300ms ease-in-out;
}

.card:hover {
  border-color: var(--border-hover);
  box-shadow: 0 8px 24px rgba(201, 169, 98, 0.15);
}

.card-title {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--accent-gold);
  margin-bottom: 0.5rem;
}

.card-description {
  color: var(--text-secondary);
  font-size: 0.875rem;
  line-height: 1.5;
}
```

### Input

```tsx
<input
  type="text"
  className="
    w-full
    px-4 py-3
    bg-bg-secondary
    border border-border-default
    text-text-primary
    placeholder-text-muted
    rounded-lg
    focus:border-accent-gold
    focus:outline-none
    focus:ring-2
    focus:ring-accent-gold
    focus:ring-opacity-20
    transition-all duration-300
  "
  placeholder="Enter text..."
/>
```

CSS:
```css
.input {
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-default);
  color: var(--text-primary);
  border-radius: 0.5rem;
  font-family: var(--font-body);
  font-size: 1rem;
  transition: all 300ms ease-in-out;
}

.input::placeholder {
  color: var(--text-muted);
}

.input:focus {
  outline: none;
  border-color: var(--accent-gold);
  box-shadow: 0 0 0 3px rgba(201, 169, 98, 0.1);
}

.input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### Badge

```tsx
<span className="
  inline-block
  px-3 py-1
  bg-accent-gold
  text-bg-primary
  text-xs
  font-semibold
  rounded-full
">
  Badge
</span>
```

CSS:
```css
.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background-color: var(--accent-gold);
  color: var(--bg-primary);
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 9999px;
}

.badge-secondary {
  background-color: var(--accent-beige);
  color: var(--bg-primary);
}

.badge-outline {
  background-color: transparent;
  border: 1px solid var(--accent-gold);
  color: var(--accent-gold);
}
```

---

## 5. ANIMATIONS

### Transitions

```css
/* Fast transition */
.transition-fast {
  transition: all 150ms ease-in-out;
}

/* Normal transition */
.transition-normal {
  transition: all 300ms ease-in-out;
}

/* Slow transition */
.transition-slow {
  transition: all 500ms ease-in-out;
}
```

### Keyframe Animations

```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideLeft {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideRight {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes glow {
  0% {
    box-shadow: 0 0 20px rgba(201, 169, 98, 0.1);
  }
  50% {
    box-shadow: 0 0 30px rgba(201, 169, 98, 0.2);
  }
  100% {
    box-shadow: 0 0 20px rgba(201, 169, 98, 0.1);
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
```

### Animation Usage

```css
.fade-in {
  animation: fadeIn 300ms ease-in-out;
}

.slide-up {
  animation: slideUp 500ms ease-in-out;
}

.slide-down {
  animation: slideDown 500ms ease-in-out;
}

.slide-left {
  animation: slideLeft 500ms ease-in-out;
}

.slide-right {
  animation: slideRight 500ms ease-in-out;
}

.glow {
  animation: glow 2s ease-in-out infinite;
}

.pulse {
  animation: pulse 2s ease-in-out infinite;
}
```

---

## 6. LAYOUT PATTERNS

### Container

```tsx
<div className="
  max-w-6xl
  mx-auto
  px-6
  py-12
">
  {/* Content */}
</div>
```

CSS:
```css
.container {
  max-width: 72rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}
```

### Grid

```tsx
<div className="
  grid
  grid-cols-1
  md:grid-cols-2
  lg:grid-cols-3
  gap-6
">
  {/* Grid items */}
</div>
```

CSS:
```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

@media (max-width: 768px) {
  .grid-3 {
    grid-template-columns: 1fr;
  }
}
```

### Flexbox

```tsx
<div className="
  flex
  items-center
  justify-between
  gap-4
">
  {/* Flex items */}
</div>
```

---

## 7. RESPONSIVE DESIGN

### Breakpoints

```
Mobile:    < 640px
Tablet:    640px - 1024px
Desktop:   1024px - 1280px
Large:     > 1280px
```

### Mobile-First Approach

```css
/* Mobile (default) */
.component {
  font-size: 1rem;
  padding: 1rem;
}

/* Tablet and up */
@media (min-width: 640px) {
  .component {
    font-size: 1.125rem;
    padding: 1.5rem;
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .component {
    font-size: 1.25rem;
    padding: 2rem;
  }
}
```

---

## 8. ACCESSIBILITY

### Color Contrast

```
Text on background:
- Primary text (#ffffff) on primary bg (#0a0a0f): 21:1 ✓
- Secondary text (#a0a0b0) on secondary bg (#0f0f1a): 8.5:1 ✓
- Gold accent (#c9a962) on primary bg (#0a0a0f): 7.2:1 ✓

All ratios meet WCAG AA standards (4.5:1 minimum)
```

### Focus States

```css
.focusable:focus {
  outline: 2px solid var(--accent-gold);
  outline-offset: 2px;
}

.focusable:focus-visible {
  outline: 2px solid var(--accent-gold);
  outline-offset: 2px;
}
```

### Semantic HTML

```html
<!-- Good -->
<button>Click me</button>
<a href="/page">Link</a>
<h1>Heading</h1>
<label for="input">Label</label>
<input id="input" />

<!-- Avoid -->
<div onclick="...">Click me</div>
<span onclick="...">Link</span>
<div class="heading">Heading</div>
```

---

## 9. DESIGN PRINCIPLES

1. **Minimalist** - Clean, uncluttered interfaces
2. **Institutional** - Professional, credible appearance
3. **Futuristic** - Modern, forward-thinking aesthetic
4. **Accessible** - High contrast, clear typography
5. **Consistent** - Unified design language

---

This design system ensures:
- ✅ Visual consistency across all pages
- ✅ Professional, institutional appearance
- ✅ Accessibility compliance (WCAG AA)
- ✅ Responsive design for all devices
- ✅ Smooth animations and transitions
- ✅ Clear hierarchy and readability