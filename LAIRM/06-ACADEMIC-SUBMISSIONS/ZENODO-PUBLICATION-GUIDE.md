# 📚 Guide de Publication sur Zenodo

## ✅ Configuration MCP Zenodo

La clé API Zenodo est déjà configurée dans `.kiro/settings/mcp.json`:
- **API Key**: `hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E`
- **Scopes**: deposit:actions, deposit:write, user:email
- **Actions auto-approuvées**: deposit_create, deposit_upload, deposit_publish

## ⚠️ Installation Requise

Le serveur MCP Zenodo n'est pas encore installé. Deux options:

### Option 1: Installation via uvx (Recommandé)
```bash
# Installer uv (gestionnaire de packages Python)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Le serveur MCP sera automatiquement téléchargé au premier usage
# Pas besoin d'installation manuelle avec uvx
```

### Option 2: Installation manuelle
```bash
pip install zenodo-mcp-server
```

## 📤 Publication du PDF sur Zenodo

### Étape 1: Préparer les Métadonnées

Créer un fichier `zenodo-metadata.json`:

```json
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
```

### Étape 2: Utiliser l'API Zenodo

#### Via MCP (si installé):
```bash
# Créer un nouveau dépôt
kiro mcp zenodo deposit_create --metadata zenodo-metadata.json

# Uploader le PDF
kiro mcp zenodo deposit_upload --deposit-id <ID> --file main-lairm.pdf

# Publier
kiro mcp zenodo deposit_publish --deposit-id <ID>
```

#### Via cURL (Alternative):
```bash
# 1. Créer un nouveau dépôt
curl -X POST https://zenodo.org/api/deposit/depositions \
  -H "Authorization: Bearer hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E" \
  -H "Content-Type: application/json" \
  -d @zenodo-metadata.json

# Récupérer l'ID du dépôt de la réponse (ex: 123456)

# 2. Uploader le PDF
curl -X POST https://zenodo.org/api/deposit/depositions/123456/files \
  -H "Authorization: Bearer hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E" \
  -F "file=@main-lairm.pdf"

# 3. Publier
curl -X POST https://zenodo.org/api/deposit/depositions/123456/actions/publish \
  -H "Authorization: Bearer hsp05RMI2FiHzwvIyYms2uYBaZpq7jydhYPnSb9L3ZYnQ5zVRXet9DiBun1E"
```

#### Via Interface Web (Plus Simple):
1. Aller sur https://zenodo.org
2. Se connecter avec le compte associé à la clé API
3. Cliquer sur **"Upload"** → **"New upload"**
4. Remplir les métadonnées:
   - **Title**: LAIRM: The Global Agentive Constitution
   - **Upload type**: Publication → Technical documentation
   - **Authors**: ORCID: 0009-0007-0110-9437
   - **Description**: (copier de zenodo-metadata.json)
   - **Keywords**: (copier de zenodo-metadata.json)
   - **License**: Creative Commons Attribution 4.0 International
   - **Version**: 1.0
5. Uploader `main-lairm.pdf`
6. Cliquer sur **"Publish"**

### Étape 3: Obtenir le DOI

Après publication, Zenodo génère automatiquement:
- **DOI**: ex: `10.5281/zenodo.123456`
- **URL permanente**: ex: `https://doi.org/10.5281/zenodo.123456`
- **Badge**: Pour afficher sur GitHub

### Étape 4: Ajouter le DOI au Document

Mettre à jour `config/metadata.tex`:
```latex
\hypersetup{
    ...
    pdfsubject={International Legislative Framework for Autonomous Agents},
    pdfkeywords={DOI: 10.5281/zenodo.123456}
}
```

### Étape 5: Ajouter le Badge au README

Dans `README.md`:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.123456.svg)](https://doi.org/10.5281/zenodo.123456)
```

## 📊 Avantages de Zenodo

✅ **DOI permanent** - Citation académique
✅ **Archivage long terme** - CERN infrastructure
✅ **Versioning** - Nouvelles versions avec DOI liés
✅ **Découvrabilité** - Indexé dans Google Scholar, OpenAIRE
✅ **Gratuit** - Jusqu'à 50 GB par dépôt
✅ **Open Access** - Conforme aux exigences de publication ouverte

## 🔗 Liens Utiles

- **API Documentation**: https://developers.zenodo.org/#rest-api
- **Zenodo Homepage**: https://zenodo.org
- **Votre clé API**: Configurée dans `.kiro/settings/mcp.json`
- **GitHub Integration**: https://zenodo.org/account/settings/github/

## 📝 Checklist de Publication

- [ ] PDF compilé avec succès (via Overleaf)
- [ ] Logo visible sur la première page
- [ ] Métadonnées préparées (zenodo-metadata.json)
- [ ] Compte Zenodo créé/connecté
- [ ] PDF uploadé sur Zenodo
- [ ] Métadonnées remplies
- [ ] Publication effectuée
- [ ] DOI obtenu
- [ ] DOI ajouté au document
- [ ] Badge ajouté au README
- [ ] Lien partagé sur le site web (manifesto.html)

## 🎯 Prochaines Étapes

1. **Compiler le PDF** (voir OVERLEAF-INSTRUCTIONS.md)
2. **Publier sur Zenodo** (suivre ce guide)
3. **Mettre à jour le site web** avec le lien DOI
4. **Annoncer la publication** sur les réseaux académiques

---

**Note**: La clé API est déjà configurée et prête à l'emploi!
