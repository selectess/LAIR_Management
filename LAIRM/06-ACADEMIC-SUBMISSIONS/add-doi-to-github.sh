#!/bin/bash

# ============================================================================
# Add DOI to GitHub README and Website
# Updates repository with Zenodo DOI badge and links
# ============================================================================

set -e

DOI_FILE="${1:-zenodo-doi.txt}"
REPO_ROOT="${2:-.}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}=== Adding DOI to GitHub ===${NC}"
echo ""

# Check if DOI file exists
if [ ! -f "$DOI_FILE" ]; then
    echo -e "${RED}❌ Error: DOI file not found: $DOI_FILE${NC}"
    exit 1
fi

DOI=$(cat "$DOI_FILE")
RECORD_ID=$(echo "$DOI" | sed 's/.*\.//')

echo -e "${GREEN}✅ DOI found: $DOI${NC}"
echo -e "${GREEN}✅ Record ID: $RECORD_ID${NC}"
echo ""

# Update README.md
README="$REPO_ROOT/README.md"
if [ -f "$README" ]; then
    echo -e "${YELLOW}Updating README.md...${NC}"
    
    # Add DOI badge at the top if not already present
    if ! grep -q "zenodo.org/badge" "$README"; then
        # Add badge after title
        sed -i '' "1s/^/[![DOI](https:\/\/zenodo.org\/badge\/DOI\/$DOI.svg)](https:\/\/doi.org\/$DOI)\n\n/" "$README"
        echo -e "${GREEN}✅ DOI badge added to README.md${NC}"
    else
        echo -e "${YELLOW}⚠️  DOI badge already in README.md${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  README.md not found${NC}"
fi

# Update manifesto.html
MANIFESTO="$REPO_ROOT/gh-pages/manifesto.html"
if [ -f "$MANIFESTO" ]; then
    echo -e "${YELLOW}Updating manifesto.html...${NC}"
    
    # Add DOI section if not already present
    if ! grep -q "zenodo" "$MANIFESTO"; then
        # Add DOI section before closing body tag
        DOI_SECTION="
    <!-- Zenodo Publication -->
    <section class=\"zenodo-publication\">
        <h2>Academic Publication</h2>
        <p>This document is published on Zenodo with a permanent DOI:</p>
        <p><a href=\"https://doi.org/$DOI\" target=\"_blank\" class=\"doi-link\">
            <strong>DOI: $DOI</strong>
        </a></p>
        <p><a href=\"https://zenodo.org/record/$RECORD_ID\" target=\"_blank\">
            View on Zenodo
        </a></p>
        <img src=\"https://zenodo.org/badge/DOI/$DOI.svg\" alt=\"DOI Badge\">
    </section>"
        
        sed -i '' "/<\/body>/i\\
$DOI_SECTION
" "$MANIFESTO"
        
        echo -e "${GREEN}✅ DOI section added to manifesto.html${NC}"
    else
        echo -e "${YELLOW}⚠️  Zenodo section already in manifesto.html${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  manifesto.html not found${NC}"
fi

# Create CITATION.cff file
CITATION_FILE="$REPO_ROOT/CITATION.cff"
cat > "$CITATION_FILE" << EOF
# LAIRM Citation File
cff-version: 1.2.0
title: "LAIRM: The Global Agentive Constitution"
message: "If you use this software, please cite it using these metadata."
type: software
authors:
  - name: "ORCID: 0009-0007-0110-9437"
    affiliation: "LAIRM International Framework"
identifiers:
  - type: doi
    value: "$DOI"
  - type: url
    value: "https://zenodo.org/record/$RECORD_ID"
repository-code: "https://github.com/selectess/LAIR_Management"
url: "https://selectess.github.io/LAIR_Management/"
abstract: "Comprehensive international legislative framework for autonomous agent governance. Includes 19 foundational axioms, 361 executable articles, and technical reference implementation (ARAM)."
keywords:
  - "autonomous agents"
  - "AI governance"
  - "cybernetic control"
  - "algorithmic accountability"
  - "constitutional framework"
license: "CC-BY-4.0"
version: "1.0"
date-released: 2026-04-22
EOF

echo -e "${GREEN}✅ CITATION.cff created${NC}"

echo ""
echo -e "${GREEN}=== Complete ===${NC}"
echo -e "DOI: ${YELLOW}$DOI${NC}"
echo -e "Zenodo URL: ${YELLOW}https://doi.org/$DOI${NC}"
echo -e "Record: ${YELLOW}https://zenodo.org/record/$RECORD_ID${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Review changes in README.md and manifesto.html"
echo "2. Commit: git add -A && git commit -m 'docs: Add Zenodo DOI reference'"
echo "3. Push: git push origin main"
