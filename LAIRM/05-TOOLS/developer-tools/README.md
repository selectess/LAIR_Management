---
title: "Developer Tools LAIRM"
type: component
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# DEVELOPER TOOLS LAIRM
## Outils pour Contributeurs et Développeurs

### Description

Les Developer Tools fournissent une interface CLI et des utilitaires pour les contributeurs et développeurs travaillant avec le framework LAIRM.

### Fichiers

- `lairm_cli.py` - Interface CLI principale (250+ lignes)
- `README.md` - Cette documentation

### Fonctionnalités

#### Commandes CLI

1. **lairm validate**
   - Valider structure LAIRM
   - Vérifier tous les articles
   - Générer rapport de validation

2. **lairm search**
   - Chercher articles
   - Filtrer par Axiom, Status
   - Afficher résultats

3. **lairm get-Article**
   - Récupérer Article complet
   - Afficher métadonnées
   - Afficher contenu

4. **lairm compliance**
   - Vérifier conformité
   - Générer rapport
   - Afficher violations

5. **lairm audit**
   - Auditer framework
   - Vérifier intégrité
   - Générer rapport d'audit

6. **lairm generate**
   - Générer rapports
   - Générer documentation
   - Générer statistiques

### Utilisation

#### Validation

```bash
# Valider structure complète
lairm validate

# Valider Axiom spécifique
lairm validate --Axiom I

# Valider avec rapport détaillé
lairm validate --verbose

# Sauvegarder rapport
lairm validate --output validation_report.json
```

#### Recherche

```bash
# Chercher articles
lairm search "kill-switch"

# Chercher par Axiom
lairm search --Axiom I

# Chercher par Status
lairm search --Status Enrichi

# Chercher avec filtres multiples
lairm search "supervision" --Axiom II --Status Enrichi

# Limiter résultats
lairm search "agent" --limit 10
```

#### Récupérer Article

```bash
# Récupérer Article
lairm get-Article I-01-01

# Afficher avec métadonnées
lairm get-Article I-01-01 --metadata

# Afficher avec liens
lairm get-Article I-01-01 --links

# Exporter en Markdown
lairm get-Article I-01-01 --output Article.md
```

#### Vérifier Conformité

```bash
# Vérifier conformité globale
lairm compliance

# Vérifier agent spécifique
lairm compliance --agent agent-001

# Vérifier Axiom
lairm compliance --Axiom I

# Générer rapport détaillé
lairm compliance --verbose --output compliance_report.json
```

#### Auditer Framework

```bash
# Auditer framework complet
lairm audit

# Auditer agent spécifique
lairm audit --agent agent-001

# Vérifier intégrité
lairm audit --verify-chain

# Générer rapport d'audit
lairm audit --output audit_report.json
```

#### Générer Rapports

```bash
# Générer rapport de conformité
lairm generate --type compliance

# Générer rapport d'audit
lairm generate --type audit

# Générer documentation
lairm generate --type documentation

# Générer statistiques
lairm generate --type statistics

# Générer tous les rapports
lairm generate --all
```

### Exemples Complets

#### Workflow de Validation

```bash
# 1. Valider structure
lairm validate

# 2. Chercher articles spécifiques
lairm search "kill-switch" --Axiom I

# 3. Récupérer Article
lairm get-Article I-01-01

# 4. Vérifier conformité
lairm compliance --verbose

# 5. Auditer framework
lairm audit --verify-chain

# 6. Générer rapport complet
lairm generate --all --output reports/
```

#### Workflow de Développement

```bash
# 1. Chercher articles pertinents
lairm search "agent_supervision"

# 2. Récupérer articles
lairm get-Article II-02-05
lairm get-Article III-03-01

# 3. Vérifier conformité
lairm compliance --Axiom II --Axiom III

# 4. Générer documentation
lairm generate --type documentation --output docs/

# 5. Auditer changements
lairm audit --agent my-agent
```

### Configuration

Fichier `.lairm/config.yaml`:

```yaml
cli:
  verbose: false
  output_format: json
  
search:
  max_results: 100
  timeout: 30
  
validation:
  strict_mode: true
  check_links: true
  
audit:
  verify_chain: true
  generate_report: true
```

### Sortie

#### Format JSON
```json
{
  "Status": "success",
  "data": [...],
  "timestamp": "2026-03-30T10:30:00Z"
}
```

#### Format Texte
```
✓ Validation successful
  - Total articles: 399
  - Valid: 399
  - Invalid: 0
  - Score: 100/100
```

### Performance

- Validation: ~2s (399 articles)
- Recherche: ~100ms
- Récupération Article: ~10ms
- Conformité: ~500ms
- Audit: ~1s

### Status

- **Implémentation** : ✅ Complète
- **Tests** : ✅ Passés
- **Production** : ✅ Prêt

### Contributeurs

- Mehdi Wahbi (Founder)

---

**Last Updated** : 30 mars 2026
**Version** : 1.0.0-final

**Last Reviewed**: April 3, 2026
