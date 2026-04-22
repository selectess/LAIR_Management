# 🚀 Zenodo Publication Workflow

## Overview

Complete automated pipeline to publish LAIRM PDF on Zenodo and update GitHub with DOI references.

```
PDF (Overleaf) → Zenodo → DOI → PDF Metadata → GitHub
```

## Prerequisites

✅ **Already Configured:**
- Zenodo API Key: `hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E`
- Metadata template ready
- Publication scripts prepared

⚠️ **You Need:**
- Compiled PDF: `main-lairm.pdf` (from Overleaf)
- `curl` command (usually pre-installed on macOS)
- `exiftool` (optional, for PDF metadata): `brew install exiftool`

## Quick Start (3 Steps)

### Step 1: Compile PDF on Overleaf
1. Go to https://www.overleaf.com
2. Upload `lairm-executive-presentation-overleaf.zip`
3. Click "Recompile"
4. Download `main-lairm.pdf`
5. Place it in: `LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation/main-lairm.pdf`

### Step 2: Run Publication Pipeline
```bash
cd LAIRM/06-ACADEMIC-SUBMISSIONS
chmod +x publish-complete.sh
./publish-complete.sh
```

### Step 3: Commit and Push
```bash
git add -A
git commit -m "docs: Add Zenodo DOI reference"
git push origin main
```

**Total time: ~5 minutes**

## Detailed Workflow

### Option A: Automated (Recommended)

**One command does everything:**
```bash
./publish-complete.sh lairm-executive-presentation/main-lairm.pdf
```

**What it does:**
1. ✅ Verifies PDF exists
2. ✅ Publishes to Zenodo (creates deposition, uploads file, publishes)
3. ✅ Extracts DOI from Zenodo response
4. ✅ Adds DOI to PDF metadata
5. ✅ Updates README.md with DOI badge
6. ✅ Updates manifesto.html with Zenodo section
7. ✅ Creates CITATION.cff file
8. ✅ Saves DOI to `zenodo-doi.txt`

**Output:**
```
DOI: 10.5281/zenodo.123456
Zenodo URL: https://doi.org/10.5281/zenodo.123456
```

### Option B: Step-by-Step

If you want to run each step separately:

#### Step 1: Publish to Zenodo
```bash
./publish-to-zenodo.sh lairm-executive-presentation/main-lairm.pdf
```

**Output:**
- Creates `zenodo-metadata.json`
- Creates `zenodo-doi.txt` with the DOI
- Prints Zenodo URL

#### Step 2: Add DOI to PDF
```bash
./add-doi-to-pdf.sh zenodo-doi.txt lairm-executive-presentation/main-lairm.pdf
```

**Output:**
- Updates PDF metadata with DOI
- Adds keywords and creator info

#### Step 3: Update GitHub
```bash
./add-doi-to-github.sh zenodo-doi.txt .
```

**Output:**
- Updates `README.md` with DOI badge
- Updates `gh-pages/manifesto.html` with Zenodo section
- Creates `CITATION.cff` file

## What Gets Updated

### 1. README.md
Adds DOI badge at the top:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.123456.svg)](https://doi.org/10.5281/zenodo.123456)
```

### 2. gh-pages/manifesto.html
Adds Zenodo publication section:
```html
<section class="zenodo-publication">
    <h2>Academic Publication</h2>
    <p>This document is published on Zenodo with a permanent DOI:</p>
    <p><a href="https://doi.org/10.5281/zenodo.123456">
        <strong>DOI: 10.5281/zenodo.123456</strong>
    </a></p>
</section>
```

### 3. CITATION.cff
Creates citation file for GitHub:
```yaml
cff-version: 1.2.0
title: "LAIRM: The Global Agentive Constitution"
doi: "10.5281/zenodo.123456"
license: "CC-BY-4.0"
```

### 4. PDF Metadata
Adds to PDF:
- Subject: DOI reference
- Keywords: DOI, LAIRM, Autonomous Agents, etc.
- Creator: ORCID: 0009-0007-0110-9437

## Zenodo Metadata Included

The publication includes:
- **Title**: LAIRM: The Global Agentive Constitution
- **Type**: Technical Documentation
- **License**: CC-BY-4.0 (Open Access)
- **Keywords**: 12 relevant keywords
- **Description**: Full abstract
- **Subjects**: AI, Computer Science, International Law
- **Related Identifiers**: Links to GitHub and website
- **Version**: 1.0
- **Language**: English
- **Date**: 2026-04-22

## Troubleshooting

### Error: "PDF file not found"
```bash
# Make sure PDF is in the right location:
ls -la lairm-executive-presentation/main-lairm.pdf
```

### Error: "Failed to create deposition"
- Check API key is correct
- Verify internet connection
- Check Zenodo status: https://zenodo.org/status

### Error: "exiftool not found"
```bash
# Install exiftool (optional, for PDF metadata):
brew install exiftool
```

### Error: "curl: command not found"
- macOS should have curl pre-installed
- If not: `brew install curl`

## Verification

After publication, verify everything:

```bash
# Check DOI was saved
cat zenodo-doi.txt

# Check README was updated
grep "zenodo.org/badge" README.md

# Check manifesto was updated
grep "zenodo" gh-pages/manifesto.html

# Check CITATION.cff was created
cat CITATION.cff

# Check PDF metadata (if exiftool installed)
exiftool lairm-executive-presentation/main-lairm.pdf | grep -i doi
```

## Citation Examples

### BibTeX
```bibtex
@software{lairm2026,
  title={LAIRM: The Global Agentive Constitution},
  author={ORCID: 0009-0007-0110-9437},
  year={2026},
  doi={10.5281/zenodo.123456},
  url={https://doi.org/10.5281/zenodo.123456}
}
```

### APA
```
ORCID: 0009-0007-0110-9437. (2026). LAIRM: The Global Agentive Constitution. 
Zenodo. https://doi.org/10.5281/zenodo.123456
```

### Chicago
```
ORCID: 0009-0007-0110-9437. "LAIRM: The Global Agentive Constitution." 
Zenodo, 2026. https://doi.org/10.5281/zenodo.123456.
```

## Files in This Workflow

| File | Purpose |
|------|---------|
| `publish-complete.sh` | Master orchestration script (run this!) |
| `publish-to-zenodo.sh` | Publishes PDF to Zenodo, extracts DOI |
| `add-doi-to-pdf.sh` | Adds DOI to PDF metadata |
| `add-doi-to-github.sh` | Updates GitHub files with DOI |
| `zenodo-metadata.json` | Metadata template (auto-generated) |
| `zenodo-doi.txt` | Saved DOI (auto-generated) |
| `CITATION.cff` | Citation file (auto-generated) |

## API Details

**Zenodo API Endpoint**: `https://zenodo.org/api/deposit/depositions`

**Authentication**: Bearer token (API key)

**Operations**:
1. `POST /depositions` - Create new deposition
2. `POST /depositions/{id}/files` - Upload file
3. `POST /depositions/{id}/actions/publish` - Publish

**Response**: JSON with DOI and record ID

## Security Notes

⚠️ **API Key Protection**:
- The API key is stored in `.kiro/settings/mcp.json`
- Never commit API keys to public repositories
- The key is already configured and ready to use
- Scripts use the key from the configuration

## Next Steps After Publication

1. ✅ PDF published on Zenodo with DOI
2. ✅ GitHub updated with DOI badge
3. ✅ Website updated with Zenodo link
4. ✅ Citation file created

**Then:**
- Share the DOI: `https://doi.org/10.5281/zenodo.123456`
- Add to academic profiles (ORCID, ResearchGate, etc.)
- Announce on social media
- Update institutional repositories

## Support

For issues:
- Zenodo API docs: https://developers.zenodo.org/
- Zenodo status: https://zenodo.org/status
- GitHub issues: https://github.com/selectess/LAIR_Management/issues

---

**Ready to publish?** Run: `./publish-complete.sh`
