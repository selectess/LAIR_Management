#!/bin/bash

# ============================================================================
# LAIRM Zenodo Publication Script
# Publishes the LAIRM PDF to Zenodo with complete metadata
# ============================================================================

set -e

# Configuration
ZENODO_API="https://zenodo.org/api/deposit/depositions"
API_KEY="hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E"
PDF_FILE="${1:-lairm-executive-presentation/main-lairm.pdf}"
METADATA_FILE="zenodo-metadata.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== LAIRM Zenodo Publication ===${NC}"
echo ""

# Check if PDF exists
if [ ! -f "$PDF_FILE" ]; then
    echo -e "${RED}❌ Error: PDF file not found: $PDF_FILE${NC}"
    echo "Please compile the PDF first using Overleaf or LaTeX"
    exit 1
fi

echo -e "${GREEN}✅ PDF found: $PDF_FILE${NC}"
echo "File size: $(du -h "$PDF_FILE" | cut -f1)"
echo ""

# Create metadata JSON
echo -e "${YELLOW}Creating metadata...${NC}"
cat > "$METADATA_FILE" << 'EOF'
{
  "metadata": {
    "title": "LAIRM: The Global Agentive Constitution - Legislature for Autonomous Intelligent Resources Management",
    "upload_type": "publication",
    "publication_type": "technicaldocumentation",
    "description": "Comprehensive international legislative framework for autonomous agent governance. Includes 19 foundational axioms, 361 executable articles, and technical reference implementation (ARAM). Addresses human supremacy, perpetual accountability, and operational transparency for autonomous intelligent systems.",
    "creators": [
      {
        "name": "ORCID: 0009-0007-0110-9437",
        "affiliation": "LAIRM International Framework"
      }
    ],
    "keywords": [
      "autonomous agents",
      "AI governance",
      "cybernetic control",
      "algorithmic accountability",
      "human oversight",
      "constitutional framework",
      "agent regulation",
      "ARAM architecture",
      "kill-switch mechanisms",
      "audit trails",
      "international law",
      "UN framework"
    ],
    "access_right": "open",
    "license": "cc-by-4.0",
    "version": "1.0",
    "language": "eng",
    "publication_date": "2026-04-22",
    "communities": [
      {"identifier": "zenodo"}
    ],
    "subjects": [
      {"term": "Artificial Intelligence", "identifier": "http://id.loc.gov/authorities/subjects/sh2018002413"},
      {"term": "Computer Science", "identifier": "http://id.loc.gov/authorities/subjects/sh89003285"},
      {"term": "International Law", "identifier": "http://id.loc.gov/authorities/subjects/sh85067435"}
    ],
    "notes": "This document presents LAIRM (Legislature for Autonomous Intelligent Resources Management), a comprehensive constitutional framework for governing autonomous intelligent systems. Version 1.0 - Legislative Release. Document Number: LAIRM-2026-001.",
    "related_identifiers": [
      {
        "identifier": "https://selectess.github.io/LAIR_Management/",
        "relation": "isDocumentedBy",
        "resource_type": "other"
      },
      {
        "identifier": "https://github.com/selectess/LAIR_Management",
        "relation": "isSupplementTo",
        "resource_type": "software"
      }
    ]
  }
}
EOF

echo -e "${GREEN}✅ Metadata created${NC}"
echo ""

# Step 1: Create new deposition
echo -e "${YELLOW}Step 1: Creating new deposition on Zenodo...${NC}"
RESPONSE=$(curl -s -X POST "$ZENODO_API" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$METADATA_FILE")

DEPOSIT_ID=$(echo "$RESPONSE" | grep -o '"id":[0-9]*' | head -1 | grep -o '[0-9]*')

if [ -z "$DEPOSIT_ID" ]; then
    echo -e "${RED}❌ Failed to create deposition${NC}"
    echo "Response: $RESPONSE"
    exit 1
fi

echo -e "${GREEN}✅ Deposition created with ID: $DEPOSIT_ID${NC}"
echo ""

# Step 2: Upload PDF
echo -e "${YELLOW}Step 2: Uploading PDF to Zenodo...${NC}"
UPLOAD_RESPONSE=$(curl -s -X POST "$ZENODO_API/$DEPOSIT_ID/files" \
  -H "Authorization: Bearer $API_KEY" \
  -F "file=@$PDF_FILE")

echo -e "${GREEN}✅ PDF uploaded${NC}"
echo ""

# Step 3: Publish
echo -e "${YELLOW}Step 3: Publishing on Zenodo...${NC}"
PUBLISH_RESPONSE=$(curl -s -X POST "$ZENODO_API/$DEPOSIT_ID/actions/publish" \
  -H "Authorization: Bearer $API_KEY")

# Extract DOI from response
DOI=$(echo "$PUBLISH_RESPONSE" | grep -o '"doi":"[^"]*' | head -1 | sed 's/"doi":"//')

if [ -z "$DOI" ]; then
    echo -e "${RED}❌ Failed to publish${NC}"
    echo "Response: $PUBLISH_RESPONSE"
    exit 1
fi

echo -e "${GREEN}✅ Published successfully!${NC}"
echo ""
echo -e "${GREEN}=== Publication Complete ===${NC}"
echo -e "DOI: ${YELLOW}$DOI${NC}"
echo -e "URL: ${YELLOW}https://doi.org/$DOI${NC}"
echo -e "Zenodo: ${YELLOW}https://zenodo.org/record/$DEPOSIT_ID${NC}"
echo ""

# Save DOI to file
echo "$DOI" > zenodo-doi.txt
echo -e "${GREEN}✅ DOI saved to zenodo-doi.txt${NC}"

# Output for use in other scripts
echo "ZENODO_DOI=$DOI"
echo "ZENODO_RECORD_ID=$DEPOSIT_ID"
