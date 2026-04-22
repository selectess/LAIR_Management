#!/bin/bash

# ============================================================================
# Add DOI to PDF Metadata
# Updates the PDF with Zenodo DOI information
# ============================================================================

set -e

DOI_FILE="${1:-zenodo-doi.txt}"
PDF_FILE="${2:-lairm-executive-presentation/main-lairm.pdf}"
OUTPUT_PDF="${3:-lairm-executive-presentation/main-lairm-with-doi.pdf}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}=== Adding DOI to PDF ===${NC}"
echo ""

# Check if DOI file exists
if [ ! -f "$DOI_FILE" ]; then
    echo -e "${RED}❌ Error: DOI file not found: $DOI_FILE${NC}"
    echo "Run publish-to-zenodo.sh first"
    exit 1
fi

DOI=$(cat "$DOI_FILE")
echo -e "${GREEN}✅ DOI found: $DOI${NC}"

# Check if PDF exists
if [ ! -f "$PDF_FILE" ]; then
    echo -e "${RED}❌ Error: PDF file not found: $PDF_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✅ PDF found: $PDF_FILE${NC}"
echo ""

# Check if exiftool is available
if ! command -v exiftool &> /dev/null; then
    echo -e "${YELLOW}⚠️  exiftool not found. Installing...${NC}"
    if command -v brew &> /dev/null; then
        brew install exiftool
    else
        echo -e "${RED}❌ Please install exiftool: brew install exiftool${NC}"
        exit 1
    fi
fi

echo -e "${YELLOW}Adding DOI metadata to PDF...${NC}"

# Add DOI to PDF metadata using exiftool
exiftool -overwrite_original \
  -Subject="DOI: $DOI" \
  -Keywords="DOI: $DOI, LAIRM, Autonomous Agents, AI Governance" \
  -Creator="ORCID: 0009-0007-0110-9437" \
  -CreatorTool="LAIRM Publication Pipeline" \
  "$PDF_FILE"

echo -e "${GREEN}✅ DOI metadata added to PDF${NC}"
echo ""
echo -e "${GREEN}=== Complete ===${NC}"
echo -e "Original PDF: ${YELLOW}$PDF_FILE${NC}"
echo -e "DOI: ${YELLOW}$DOI${NC}"
echo -e "Zenodo URL: ${YELLOW}https://doi.org/$DOI${NC}"
