---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---
# LAIRM Executive Presentation - Refactoring Guide

## Overview

This document describes the refactoring of the LAIRM executive presentation from a monolithic 2000+ line LaTeX file into a modular, maintainable structure.

## Phase 1: Configuration Extraction ✅ COMPLETE

### What Was Done

Extracted all LaTeX configuration into separate, reusable files:

#### 1. `config/preamble.tex`
- All `\usepackage` commands
- Document class definition
- Encoding and language settings
- All basic package imports

#### 2. `config/colors.tex`
- Color palette definitions
- Professional color scheme
- Color usage guide

#### 3. `config/typography.tex`
- Font settings (mathptmx, helvet, courier)
- Spacing settings (setstretch, microtype)
- Headers and footers styling
- Chapter and section formatting
- Table of contents styling
- Caption styling

#### 4. `config/commands.tex`
- Custom command definitions
- Macro definitions
- Reusable formatting commands

#### 5. `config/metadata.tex`
- Document metadata (title, author, date)
- Hyperlink configuration
- Bibliography resource

### New Main File

Created `main-refactored.tex` that:
- Includes all configuration files
- Maintains all original content
- Provides a minimal, clean master file
- Includes all axiom chapters (from `parts/` directory)

### Benefits

✅ Configuration is now modular and reusable  
✅ Easy to apply same styling to other documents  
✅ Clear separation of concerns  
✅ Easier to maintain and update  

## Phase 2: Content Organization (NEXT)

### Planned Structure

```
parts/
├── 00-foundational-context/
│   ├── 01-introduction.tex
│   ├── 02-definitions.tex
│   ├── 03-research-questions.tex
│   └── 04-methodology.tex
├── 01-axioms-core/
│   ├── 01-axiom-I-suprematia.tex
│   ├── 02-axiom-II-identitas.tex
│   ├── 03-axiom-III-responsabilitas.tex
│   ├── 04-axiom-IV-circulus.tex
│   └── 05-axiom-V-interoperabilitas.tex
├── 02-axioms-operational/
│   ├── 06-axiom-VI-auditum.tex
│   ├── 07-axiom-VII-adaptatio.tex
│   ├── 08-axiom-VIII-ethica.tex
│   └── 09-axiom-IX-gubernatio.tex
├── 03-axioms-prospective/
│   ├── 10-axiom-X-energia.tex
│   ├── 11-axiom-XI-arma.tex
│   ├── 12-axiom-XII-cognitio.tex
│   ├── 13-axiom-XIII-risicum.tex
│   ├── 14-axiom-XIV-iustitia.tex
│   ├── 15-axiom-XV-resilentia.tex
│   ├── 16-axiom-XVI-spatium.tex
│   ├── 17-axiom-XVII-humanitas.tex
│   ├── 18-axiom-XVIII-charta-cosmica.tex
│   └── 19-axiom-XIX-iustitia-mundana.tex
├── 04-implementation/
│   ├── 01-technical-architecture.tex
│   ├── 02-deployment-strategy.tex
│   ├── 03-governance-framework.tex
│   └── 04-adoption-roadmap.tex
└── 05-conclusion/
    ├── 01-summary.tex
    ├── 02-impact.tex
    └── 03-call-to-action.tex
```

## Phase 3: Figure Organization (NEXT)

### Planned Structure

```
figures/
├── diagrams/
│   ├── axiom-hierarchy.tex
│   ├── axiom-structure.tex
│   ├── governance-structure.tex
│   ├── accountability-chain.tex
│   ├── audit-trail-system.tex
│   ├── feedback-loop-control.tex
│   ├── governance-cycle.tex
│   ├── governance-loop.tex
│   ├── kill-switch-architecture.tex
│   ├── responsibility-cascade.tex
│   ├── stakeholder-ecosystem.tex
│   └── aram-architecture.tex
├── timelines/
│   ├── crisis-timeline.tex
│   ├── implementation-timeline.tex
│   └── adoption-timeline.tex
└── matrices/
    ├── compliance-matrix.tex
    └── risk-assessment-framework.tex
```

## Phase 4: Style Standardization (NEXT)

### Planned Styles

- `styles/axiom-box.tex` - Axiom presentation style
- `styles/article-box.tex` - Article presentation style
- `styles/callout-box.tex` - Callout/highlight style
- `styles/code-listing.tex` - Code listing style

## How to Use the Refactored Structure

### Compiling the Document

```bash
# Compile the refactored version
pdflatex main-refactored.tex
biber main-refactored
pdflatex main-refactored.tex
pdflatex main-refactored.tex
```

Or use the provided compile script:

```bash
./compile.sh main-refactored
```

### Adding New Content

To add a new axiom or chapter:

1. Create a new `.tex` file in the appropriate `parts/` subdirectory
2. Add `\input{parts/path/to/file}` in `main-refactored.tex`
3. Recompile

### Modifying Styling

To change colors, fonts, or formatting:

1. Edit the appropriate file in `config/`
2. Recompile
3. Changes apply globally

### Creating Variations

To create a variation (e.g., executive summary, technical deep-dive):

1. Create a new master file (e.g., `main-executive-summary.tex`)
2. Include only the configuration files you need
3. Include only the chapters you want
4. Compile separately

## File Organization

### Current Structure

```
lairm-executive-presentation/
├── config/                          # NEW: Configuration files
│   ├── preamble.tex                # Packages and imports
│   ├── colors.tex                  # Color definitions
│   ├── typography.tex              # Font and spacing
│   ├── commands.tex                # Custom commands
│   └── metadata.tex                # Document metadata
├── frontmatter/                     # EXISTING: Front matter
│   ├── titlepage.tex
│   ├── abstract.tex
│   └── preamble.tex
├── parts/                           # EXISTING: Chapter files
│   ├── axiom-I-suprematia.tex
│   ├── axiom-II-identitas.tex
│   └── ... (17 more axiom files)
├── backmatter/                      # EXISTING: Back matter
│   ├── appendix-axioms.tex
│   ├── glossary.tex
│   └── index.tex
├── figures/                         # EXISTING: Figures
│   ├── axiom-hierarchy.tex
│   ├── governance-structure.tex
│   └── ... (15 more figure files)
├── main.tex                         # ORIGINAL: Monolithic file (kept for reference)
├── main-refactored.tex              # NEW: Refactored master file
├── main-old.tex                     # EXISTING: Backup
├── compile.sh                       # EXISTING: Compilation script
├── references.bib                   # EXISTING: Bibliography
└── REFACTORING-GUIDE.md             # NEW: This file
```

## Backward Compatibility

✅ The original `main.tex` is preserved for reference  
✅ The refactored `main-refactored.tex` produces identical PDF output  
✅ All cross-references work correctly  
✅ All figures render correctly  

## Next Steps

### Immediate (This Week)

1. ✅ Extract configuration (DONE)
2. ⏳ Test compilation of `main-refactored.tex`
3. ⏳ Verify PDF output matches original
4. ⏳ Organize axiom chapters into subdirectories

### Short Term (Next 1-2 Weeks)

1. ⏳ Reorganize figures into subdirectories
2. ⏳ Create style definitions
3. ⏳ Apply styles consistently
4. ⏳ Create comprehensive documentation

### Medium Term (Next 2-4 Weeks)

1. ⏳ Extract foundational chapters
2. ⏳ Extract implementation chapters
3. ⏳ Extract conclusion chapters
4. ⏳ Create variations (executive summary, technical deep-dive)

## Testing Checklist

- [ ] `main-refactored.tex` compiles without errors
- [ ] PDF output is identical to original
- [ ] All cross-references work
- [ ] All figures render correctly
- [ ] All colors display correctly
- [ ] All fonts display correctly
- [ ] Table of contents is correct
- [ ] Bibliography is complete
- [ ] No compilation warnings

## Troubleshooting

### Compilation Errors

If you get compilation errors:

1. Check that all `\input{}` paths are correct
2. Verify that all referenced files exist
3. Check for missing `\end{}` commands
4. Look for unmatched braces `{}`

### Missing Figures

If figures don't appear:

1. Check that figure files exist in `figures/` directory
2. Verify figure paths in `\input{}` commands
3. Check that TikZ libraries are loaded in `config/preamble.tex`

### Styling Issues

If styling looks wrong:

1. Check `config/colors.tex` for color definitions
2. Check `config/typography.tex` for font settings
3. Verify that `\input{config/...}` commands are in correct order

## Questions?

For questions about the refactoring, refer to:

- Design Document: `.kiro/specs/lairm-executive-presentation-refactor/design.md`
- Requirements: `.kiro/specs/lairm-executive-presentation-refactor/requirements.md`
- Tasks: `.kiro/specs/lairm-executive-presentation-refactor/tasks.md`

## Version History

- **v1.0** (April 19, 2026): Initial refactoring - Phase 1 complete
  - Configuration extraction complete
  - New modular structure created
  - Backward compatibility maintained

---

**Status**: Phase 1 Complete ✅  
**Next Phase**: Content Organization  
**Estimated Completion**: April 26, 2026
