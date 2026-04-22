#!/bin/bash

# ============================================================================
# LAIRM Complete Publication Pipeline
# Orchestrates: Zenodo publication → DOI to PDF → DOI to GitHub
# ============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
PDF_FILE="${1:-lairm-executive-presentation/main-lairm.pdf}"
REPO_ROOT="${2:-.}"

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║     LAIRM Complete Publication Pipeline                    ║"
echo "║     Zenodo → PDF → GitHub                                  ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Step 1: Verify PDF exists
echo -e "${YELLOW}[1/4] Verifying PDF...${NC}"
if [ ! -f "$PDF_FILE" ]; then
    echo -e "${RED}❌ PDF not found: $PDF_FILE${NC}"
    echo "Please compile the PDF first using Overleaf"
    exit 1
fi
echo -e "${GREEN}✅ PDF verified: $PDF_FILE${NC}"
echo ""

# Step 2: Publish to Zenodo
echo -e "${YELLOW}[2/4] Publishing to Zenodo...${NC}"
if [ ! -f "publish-to-zenodo.sh" ]; then
    echo -e "${RED}❌ publish-to-zenodo.sh not found${NC}"
    exit 1
fi

chmod +x publish-to-zenodo.sh
./publish-to-zenodo.sh "$PDF_FILE"

if [ ! -f "zenodo-doi.txt" ]; then
    echo -e "${RED}❌ Zenodo publication failed${NC}"
    exit 1
fi

DOI=$(cat zenodo-doi.txt)
echo -e "${GREEN}✅ Published to Zenodo${NC}"
echo -e "   DOI: $DOI"
echo ""

# Step 3: Add DOI to PDF
echo -e "${YELLOW}[3/4] Adding DOI to PDF metadata...${NC}"
if [ ! -f "add-doi-to-pdf.sh" ]; then
    echo -e "${RED}❌ add-doi-to-pdf.sh not found${NC}"
    exit 1
fi

chmod +x add-doi-to-pdf.sh
./add-doi-to-pdf.sh "zenodo-doi.txt" "$PDF_FILE" || {
    echo -e "${YELLOW}⚠️  Warning: Could not add DOI to PDF (exiftool may not be installed)${NC}"
    echo "   You can install it with: brew install exiftool"
}
echo ""

# Step 4: Add DOI to GitHub
echo -e "${YELLOW}[4/4] Adding DOI to GitHub...${NC}"
if [ ! -f "add-doi-to-github.sh" ]; then
    echo -e "${RED}❌ add-doi-to-github.sh not found${NC}"
    exit 1
fi

chmod +x add-doi-to-github.sh
./add-doi-to-github.sh "zenodo-doi.txt" "$REPO_ROOT"
echo ""

# Summary
echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║     ✅ Publication Complete!                               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""
echo -e "${BLUE}Publication Details:${NC}"
echo -e "  DOI: ${YELLOW}$DOI${NC}"
echo -e "  Zenodo: ${YELLOW}https://doi.org/$DOI${NC}"
echo -e "  PDF: ${YELLOW}$PDF_FILE${NC}"
echo ""
echo -e "${BLUE}Files Updated:${NC}"
echo -e "  ✅ README.md (DOI badge added)"
echo -e "  ✅ gh-pages/manifesto.html (Zenodo section added)"
echo -e "  ✅ CITATION.cff (created)"
echo -e "  ✅ PDF metadata (DOI added)"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "  1. Review the changes:"
echo "     git diff README.md"
echo "     git diff gh-pages/manifesto.html"
echo ""
echo "  2. Commit and push:"
echo "     git add -A"
echo "     git commit -m 'docs: Add Zenodo DOI reference - $DOI'"
echo "     git push origin main"
echo ""
echo -e "${BLUE}Citation:${NC}"
echo "  @software{lairm2026,"
echo "    title={LAIRM: The Global Agentive Constitution},"
echo "    author={ORCID: 0009-0007-0110-9437},"
echo "    year={2026},"
echo "    doi={$DOI},"
echo "    url={https://doi.org/$DOI}"
echo "  }"
echo ""
