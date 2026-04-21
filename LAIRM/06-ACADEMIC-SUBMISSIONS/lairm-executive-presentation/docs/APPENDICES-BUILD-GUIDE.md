---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---
# LAIRM Technical Appendices - Build Guide

## Overview

This guide explains how to compile the LAIRM document with the new technical appendices into a PDF.

---

## Prerequisites

### Required Software

1. **LaTeX Distribution**
   - **macOS**: MacTeX (https://tug.org/mactex/)
   - **Linux**: TeX Live (https://www.tug.org/texlive/)
   - **Windows**: MiKTeX (https://miktex.org/)

2. **Required LaTeX Packages**
   ```
   - book (document class)
   - geometry (page layout)
   - fancyhdr (headers/footers)
   - tikz (diagrams)
   - listings (code highlighting)
   - algorithm (pseudocode)
   - amsmath (mathematics)
   - amssymb (mathematical symbols)
   - xcolor (colors)
   - hyperref (hyperlinks)
   - biblatex (bibliography)
   - tabularx (tables)
   - graphicx (graphics)
   ```

3. **Optional Tools**
   - Biber (for bibliography processing)
   - Ghostscript (for PDF optimization)

---

## Installation

### macOS (using MacTeX)

```bash
# Install MacTeX (one-time)
brew install --cask mactex

# Verify installation
pdflatex --version
```

### Linux (using TeX Live)

```bash
# Install TeX Live
sudo apt-get install texlive-full

# Verify installation
pdflatex --version
```

### Windows (using MiKTeX)

1. Download MiKTeX from https://miktex.org/
2. Run the installer
3. During installation, select "Install missing packages on-the-fly"

---

## Compilation

### Method 1: Direct pdflatex (Recommended)

```bash
cd LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation

# Single pass (fast, for quick preview)
pdflatex main-refactored.tex

# Multiple passes (recommended for final version)
pdflatex main-refactored.tex
pdflatex main-refactored.tex
pdflatex main-refactored.tex
```

### Method 2: Using latexmk (Automatic)

```bash
cd LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation

# Automatic compilation with all necessary passes
latexmk -pdf main-refactored.tex

# Clean up auxiliary files
latexmk -c main-refactored.tex
```

### Method 3: Using Makefile

Create a `Makefile` in the presentation directory:

```makefile
.PHONY: build clean view

build:
	pdflatex -interaction=nonstopmode main-refactored.tex
	pdflatex -interaction=nonstopmode main-refactored.tex
	pdflatex -interaction=nonstopmode main-refactored.tex

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg

view: build
	open main-refactored.pdf  # macOS
	# xdg-open main-refactored.pdf  # Linux
	# start main-refactored.pdf  # Windows

all: clean build view
```

Then run:

```bash
make all
```

---

## Troubleshooting

### Common Issues

#### 1. Missing Packages

**Error**: `! LaTeX Error: File 'tikz.sty' not found.`

**Solution**:
```bash
# macOS
sudo tlmgr install tikz

# Linux
sudo apt-get install texlive-pictures

# Windows
MiKTeX will prompt to install missing packages automatically
```

#### 2. Bibliography Issues

**Error**: `! Undefined control sequence \printbibliography`

**Solution**:
```bash
# Install biblatex
sudo tlmgr install biblatex

# Recompile with biber
pdflatex main-refactored.tex
biber main-refactored
pdflatex main-refactored.tex
pdflatex main-refactored.tex
```

#### 3. File Not Found

**Error**: `! I can't find file 'parts/06-appendices/A-formal-proofs.tex'`

**Solution**:
- Verify all appendix files exist in `parts/06-appendices/`
- Check file names match exactly (case-sensitive on Linux/macOS)
- Ensure directory structure is correct

#### 4. Memory Issues

**Error**: `TeX capacity exceeded`

**Solution**:
```bash
# Increase TeX memory
pdflatex -interaction=nonstopmode -max-print-line=1000 main-refactored.tex
```

---

## File Structure

```
LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation/
├── main-refactored.tex                    # Main document
├── config/
│   ├── preamble.tex
│   ├── colors.tex
│   ├── typography.tex
│   ├── commands.tex
│   └── metadata.tex
├── styles/
│   ├── axiom-box.tex
│   ├── article-box.tex
│   ├── callout-box.tex
│   └── code-listing.tex
├── frontmatter/
│   ├── titlepage.tex
│   ├── preamble.tex
│   └── abstract.tex
├── parts/
│   ├── 00-foundational-context/
│   ├── 01-axioms-core/
│   ├── 02-axioms-operational/
│   ├── 03-axioms-prospective/
│   ├── 04-implementation/
│   ├── 05-conclusion/
│   └── 06-appendices/              # NEW
│       ├── A-formal-proofs.tex
│       ├── B-implementation-specs.tex
│       ├── C-code-examples.tex
│       └── D-technical-architecture.tex
├── backmatter/
│   ├── glossary.tex
│   └── index.tex
├── figures/
│   ├── diagrams/
│   ├── timelines/
│   └── matrices/
├── README.md
├── AXIOM-EXPANSION-SUMMARY.md
├── APPENDICES-COMPLETION-SUMMARY.md
└── APPENDICES-BUILD-GUIDE.md
```

---

## Output

### Generated Files

After successful compilation:

```
main-refactored.pdf          # Final PDF document (400-500+ pages)
main-refactored.aux          # Auxiliary file (can be deleted)
main-refactored.log          # Compilation log
main-refactored.out          # Outline file (can be deleted)
main-refactored.toc          # Table of contents
main-refactored.lof          # List of figures
main-refactored.lot          # List of tables
```

### PDF Properties

- **Format**: PDF 1.5
- **Pages**: 400-500+
- **Size**: ~50-100 MB (depending on figures)
- **Compression**: Enabled
- **Bookmarks**: Enabled (clickable TOC)
- **Hyperlinks**: Enabled

---

## Optimization

### Reduce PDF Size

```bash
# Using Ghostscript
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
   -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=main-refactored-optimized.pdf \
   main-refactored.pdf
```

### Extract Specific Pages

```bash
# Extract pages 1-50 (front matter)
pdftk main-refactored.pdf cat 1-50 output front-matter.pdf

# Extract pages 400-500 (appendices)
pdftk main-refactored.pdf cat 400-500 output appendices.pdf
```

---

## Validation

### Check PDF Integrity

```bash
# Verify PDF structure
pdfinfo main-refactored.pdf

# Check for errors
pdftotext main-refactored.pdf - | head -20
```

### Verify Compilation

```bash
# Check for warnings
grep -i "warning" main-refactored.log

# Check for errors
grep -i "error" main-refactored.log

# Count pages
pdfinfo main-refactored.pdf | grep Pages
```

---

## Advanced Options

### Custom Compilation Script

Create `compile.sh`:

```bash
#!/bin/bash

set -e

echo "Compiling LAIRM document..."

# Clean previous build
rm -f *.aux *.log *.out *.toc *.lof *.lot

# First pass
echo "Pass 1..."
pdflatex -interaction=nonstopmode main-refactored.tex > /dev/null

# Second pass
echo "Pass 2..."
pdflatex -interaction=nonstopmode main-refactored.tex > /dev/null

# Third pass (for TOC/LOF/LOT)
echo "Pass 3..."
pdflatex -interaction=nonstopmode main-refactored.tex > /dev/null

# Check for errors
if grep -q "Error" main-refactored.log; then
    echo "Compilation errors detected!"
    grep "Error" main-refactored.log
    exit 1
fi

echo "Compilation successful!"
echo "Output: main-refactored.pdf"

# Optional: Open PDF
# open main-refactored.pdf
```

Run with:
```bash
chmod +x compile.sh
./compile.sh
```

---

## Continuous Integration

### GitHub Actions Example

Create `.github/workflows/build-pdf.yml`:

```yaml
name: Build LAIRM PDF

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Install LaTeX
        run: sudo apt-get install -y texlive-full
      
      - name: Compile PDF
        run: |
          cd LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation
          pdflatex -interaction=nonstopmode main-refactored.tex
          pdflatex -interaction=nonstopmode main-refactored.tex
          pdflatex -interaction=nonstopmode main-refactored.tex
      
      - name: Upload PDF
        uses: actions/upload-artifact@v2
        with:
          name: LAIRM-Document
          path: LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation/main-refactored.pdf
```

---

## Performance Tips

1. **Use SSD**: Compilation is I/O intensive
2. **Increase RAM**: Allocate more memory to TeX
3. **Disable Graphics**: Temporarily remove figures for faster compilation
4. **Use latexmk**: Automatically determines necessary passes

---

## Support

### Resources

- **LaTeX Documentation**: https://www.latex-project.org/
- **TikZ Manual**: https://pgf-tikz.github.io/pgf/pgfmanual.pdf
- **Overleaf Guides**: https://www.overleaf.com/learn

### Troubleshooting

1. Check the `.log` file for detailed error messages
2. Search error messages on TeX Stack Exchange
3. Verify all input files exist and are readable
4. Try compiling a minimal example first

---

## Next Steps

After successful compilation:

1. **Review PDF**: Check formatting, page breaks, figures
2. **Verify Content**: Ensure all appendices are included
3. **Check References**: Verify cross-references and citations
4. **Optimize**: Reduce file size if needed
5. **Distribute**: Share PDF with stakeholders

---

## Conclusion

The LAIRM document with technical appendices can be compiled into a professional PDF suitable for academic publication and technical distribution.

For questions or issues, refer to the LaTeX documentation or contact the LAIRM development team.

---

**Last Updated**: April 2026  
**Document Version**: 1.0  
**Status**: Production Ready
