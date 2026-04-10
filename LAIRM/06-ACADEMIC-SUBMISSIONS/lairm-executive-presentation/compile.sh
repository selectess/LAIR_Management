#!/bin/bash
# LAIRM Executive Presentation - Compilation Script
# Compiles the LaTeX document with bibliography

echo "=========================================="
echo "LAIRM Executive Presentation"
echo "Compilation Script"
echo "=========================================="
echo ""

# Use full path to MacTeX binaries
PDFLATEX="/usr/local/texlive/2026/bin/universal-darwin/pdflatex"
BIBER="/usr/local/texlive/2026/bin/universal-darwin/biber"

if [ ! -f "$PDFLATEX" ]; then
    echo "ERROR: pdflatex not found at $PDFLATEX"
    exit 1
fi

echo "Step 1/4: First LaTeX pass..."
$PDFLATEX -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "Step 2/4: Generating bibliography..."
$BIBER main > /dev/null 2>&1

echo "Step 3/4: Second LaTeX pass..."
$PDFLATEX -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "Step 4/4: Final LaTeX pass..."
$PDFLATEX -interaction=nonstopmode main.tex

echo ""
echo "=========================================="
echo "Compilation complete!"
echo "=========================================="

if [ -f main.pdf ]; then
    SIZE=$(du -h main.pdf | cut -f1)
    PAGES=$(grep -o "Output written on main.pdf (\([0-9]*\) page" main.log 2>/dev/null | grep -o "[0-9]*" || echo "?")
    echo "Output: main.pdf"
    echo "Pages: $PAGES"
    echo "Size: $SIZE"
fi

echo "=========================================="
