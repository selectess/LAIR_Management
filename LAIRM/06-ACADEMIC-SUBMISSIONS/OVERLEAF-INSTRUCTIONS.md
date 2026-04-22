# 📄 Instructions pour Compiler le PDF avec Overleaf

## ✅ Fichier Prêt

Le fichier `lairm-executive-presentation-overleaf.zip` (313 KB) est prêt pour Overleaf.

## 🚀 Étapes de Compilation

### 1. Aller sur Overleaf
Ouvrir: https://www.overleaf.com

### 2. Créer un Compte (si nécessaire)
- Gratuit pour documents publics
- Ou se connecter avec Google/GitHub

### 3. Uploader le Projet
1. Cliquer sur **"New Project"**
2. Sélectionner **"Upload Project"**
3. Choisir le fichier: `lairm-executive-presentation-overleaf.zip`
4. Attendre l'upload (quelques secondes)

### 4. Configurer le Compilateur
1. Cliquer sur l'icône **Menu** (☰) en haut à gauche
2. Dans **"Settings"**:
   - **Compiler**: Sélectionner `pdfLaTeX`
   - **Main document**: Vérifier que c'est `main-lairm.tex`
3. Fermer le menu

### 5. Compiler
1. Cliquer sur **"Recompile"** (bouton vert)
2. Attendre 30-60 secondes (première compilation)
3. Le PDF apparaîtra à droite avec le logo sur la première page!

### 6. Télécharger le PDF
1. Cliquer sur l'icône **Download PDF** (↓) au-dessus du PDF
2. Le fichier sera téléchargé: `main-lairm.pdf`

## 🎨 Résultat Attendu

Le PDF contiendra:
- ✅ **Logo LAIRM** en grand format sur la première page (40% de largeur)
- ✅ **Couleurs correctes**: Bleu législatif (#003366) et Or (#B8860B)
- ✅ **Page de titre professionnelle** avec toutes les métadonnées
- ✅ **Table des matières** complète
- ✅ **Environ 70-100 pages** (selon le contenu des placeholders)

## 🔧 Si Erreurs de Compilation

### Erreur: "File not found"
- Vérifier que tous les fichiers sont bien uploadés
- Regarder dans le dossier `figures/` si `logo-lairm.png` existe

### Erreur: "Undefined control sequence"
- Vérifier que `config/commands.tex` est bien présent
- Recompiler une 2ème fois (certaines références nécessitent 2 passes)

### Erreur: "Missing bibliography"
- Normal pour la première compilation
- Cliquer sur **"Recompile"** une 2ème fois

## 📊 Contenu du PDF

### Pages Principales:
1. **Page de titre** avec logo (page 1)
2. **Informations du document** (page 2)
3. **The Crisis is Now** - Narrative d'ouverture
4. **Why You Should Care** - Pour chaque audience
5. **The Vision** - Futur avec LAIRM
6. **Acknowledgments**
7. **Document Metadata**
8. **Preamble** - Cadre législatif
9. **Abstract** - Résumé exécutif
10. **Executive Summary**
11. **Table of Contents**
12. **Parts 0-5** - Contenu principal (avec placeholders)
13. **Appendices**
14. **Glossary & Index**
15. **Bibliography**

## 🎯 Prochaines Étapes

Après avoir le PDF compilé:

1. **Vérifier le logo** - Taille et position OK?
2. **Vérifier les couleurs** - Bleu et or corrects?
3. **Remplacer les placeholders** - Ajouter le contenu réel dans les parties manquantes
4. **Publier sur Zenodo** - Utiliser l'API Zenodo configurée

## 📝 Notes

- Le fichier zip contient **tous les fichiers nécessaires**
- Les **placeholders** sont des chapitres minimaux pour permettre la compilation
- Le **contenu réel** des axiomes XII-XIX est déjà présent
- Les **autres sections** peuvent être développées progressivement

## 🆘 Support

Si problèmes:
1. Vérifier les logs de compilation dans Overleaf (bouton "Logs and output files")
2. Chercher les erreurs en rouge
3. Les warnings en jaune sont généralement OK

---

**Temps estimé**: 5 minutes pour upload + compilation + téléchargement

**Fichier à utiliser**: `lairm-executive-presentation-overleaf.zip` (313 KB)

**Localisation**: `LAIRM/06-ACADEMIC-SUBMISSIONS/lairm-executive-presentation-overleaf.zip`
