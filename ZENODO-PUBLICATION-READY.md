# ✅ Zenodo Publication Pipeline - Ready to Deploy

**Date**: April 22, 2026  
**Status**: ✅ COMPLETE AND READY

## 🎯 What's Been Prepared

### 1. Complete Publication Pipeline
All scripts are ready in `LAIRM/06-ACADEMIC-SUBMISSIONS/`:

| Script | Purpose |
|--------|---------|
| `publish-complete.sh` | **Master script** - Run this one! |
| `publish-to-zenodo.sh` | Publish PDF to Zenodo, extract DOI |
| `add-doi-to-pdf.sh` | Add DOI to PDF metadata |
| `add-doi-to-github.sh` | Update GitHub with DOI references |

### 2. Documentation
- `LAIRM/06-ACADEMIC-SUBMISSIONS/ZENODO-PUBLICATION-WORKFLOW.md` - Complete usage guide
- `LAIRM/06-ACADEMIC-SUBMISSIONS/OVERLEAF-INSTRUCTIONS.md` - How to compile PDF
- `LAIRM/06-ACADEMIC-SUBMISSIONS/ZENODO-PUBLICATION-GUIDE.md` - API details

### 3. Configuration
- ✅ Zenodo API Key configured in `.kiro/settings/mcp.json`
- ✅ Metadata template ready
- ✅ All scripts executable

## 🚀 Quick Start (When You Have PDF)

### Step 1: Compile PDF on Overleaf
1. Upload `lairm-executive-presentation-overleaf.zip` to Overleaf
2. Click "Recompile"
3. Download `main-lairm.pdf`
4. Place in: `LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation/main-lairm.pdf`

### Step 2: Run Publication Pipeline
```bash
cd LAIRM/06-ACADEMIC-SUBMISSIONS
./publish-complete.sh
```

### Step 3: Commit and Push
```bash
git add -A
git commit -m "docs: Add Zenodo DOI reference"
git push origin main
```

**Total time: ~5 minutes**

## 📊 What Happens Automatically

When you run `./publish-complete.sh`:

1. ✅ **Verifies PDF** exists
2. ✅ **Creates Zenodo deposition** with metadata
3. ✅ **Uploads PDF** to Zenodo
4. ✅ **Publishes** and gets DOI
5. ✅ **Extracts DOI** from response
6. ✅ **Adds DOI to PDF** metadata
7. ✅ **Updates README.md** with DOI badge
8. ✅ **Updates manifesto.html** with Zenodo section
9. ✅ **Creates CITATION.cff** for GitHub
10. ✅ **Saves DOI** to `zenodo-doi.txt`

## 📝 Zenodo Metadata Included

The publication will include:
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

## 🔐 Security

- ✅ API key stored in `.kiro/settings/mcp.json` (not in scripts)
- ✅ Scripts use environment variable for key
- ✅ Safe to commit scripts to public repo
- ✅ Key is already configured and ready

## 📋 Files That Will Be Updated

After running the pipeline:

1. **README.md**
   - Adds DOI badge at top
   - Example: `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.123456.svg)](https://doi.org/10.5281/zenodo.123456)`

2. **gh-pages/manifesto.html**
   - Adds Zenodo publication section
   - Links to DOI and Zenodo record

3. **CITATION.cff** (new file)
   - GitHub citation file
   - Includes DOI for proper attribution

4. **PDF Metadata**
   - Subject: DOI reference
   - Keywords: DOI, LAIRM, Autonomous Agents, etc.
   - Creator: ORCID: 0009-0007-0110-9437

## 🎓 Citation Examples

After publication, users can cite as:

**BibTeX:**
```bibtex
@software{lairm2026,
  title={LAIRM: The Global Agentive Constitution},
  author={ORCID: 0009-0007-0110-9437},
  year={2026},
  doi={10.5281/zenodo.123456},
  url={https://doi.org/10.5281/zenodo.123456}
}
```

**APA:**
```
ORCID: 0009-0007-0110-9437. (2026). LAIRM: The Global Agentive Constitution. 
Zenodo. https://doi.org/10.5281/zenodo.123456
```

## ✅ Checklist

- [x] Zenodo API key configured
- [x] Publication scripts created
- [x] Metadata template prepared
- [x] Documentation written
- [x] Scripts tested and executable
- [x] GitHub integration ready
- [x] PDF metadata integration ready
- [ ] PDF compiled (you do this on Overleaf)
- [ ] Publication pipeline executed
- [ ] DOI obtained and verified
- [ ] GitHub updated and pushed
- [ ] Website updated with DOI link

## 🔗 Useful Links

- **Zenodo**: https://zenodo.org
- **API Docs**: https://developers.zenodo.org/
- **Overleaf**: https://www.overleaf.com
- **GitHub Repo**: https://github.com/selectess/LAIR_Management
- **Website**: https://selectess.github.io/LAIR_Management/

## 📞 Support

If you encounter issues:

1. **PDF not compiling?**
   - See: `LAIRM/06-ACADEMIC-SUBMISSIONS/OVERLEAF-INSTRUCTIONS.md`

2. **Publication script fails?**
   - Check: `LAIRM/06-ACADEMIC-SUBMISSIONS/ZENODO-PUBLICATION-WORKFLOW.md` troubleshooting section
   - Verify: API key in `.kiro/settings/mcp.json`
   - Check: Internet connection

3. **Need more details?**
   - Read: `LAIRM/06-ACADEMIC-SUBMISSIONS/ZENODO-PUBLICATION-GUIDE.md`

## 🎉 Next Steps

1. **Compile PDF on Overleaf** (5 minutes)
2. **Run publication pipeline** (2 minutes)
3. **Commit and push** (1 minute)
4. **Share DOI** with the world!

---

**Everything is ready. Just compile the PDF and run the script!**

```bash
cd LAIRM/06-ACADEMIC-SUBMISSIONS
./publish-complete.sh
```

**That's it!** 🚀
