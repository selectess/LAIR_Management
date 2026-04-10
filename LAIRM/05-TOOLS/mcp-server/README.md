---
title: "MCP Server LAIRM"
type: component
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# MCP SERVER LAIRM
## Interface Standardisée pour Framework LAIRM

### Description

Le MCP Server fournit une interface standardisée (Model Context Protocol) pour accéder au framework LAIRM. Il permet aux clients MCP de chercher, récupérer et valider les articles du framework.

### Fichiers

- `lairm_mcp_server.py` - Serveur MCP principal (400+ lignes)
- `config.yaml` - Configuration du serveur
- `README.md` - Cette documentation

### Fonctionnalités

#### Outils MCP Disponibles

1. **search_articles(query, Axiom, Status)**
   - Chercher articles par query, Axiom ou Status
   - Retourne liste d'articles correspondants
   - Supporte filtrage multi-critères

2. **get_article(numero)**
   - Récupérer Article complet par numéro
   - Retourne contenu, métadonnées, validations
   - Inclut liens vers articles connexes

3. **get_axiome(numero)**
   - Récupérer Axiom complet
   - Retourne tous les articles de l'Axiom
   - Inclut statistiques et conformité

4. **validate_compliance(agent_config)**
   - Valider conformité d'agent
   - Vérifie axiomes requis
   - Retourne score de conformité

5. **audit_action(agent_id, action)**
   - Auditer action d'agent
   - Enregistre dans audit trail
   - Retourne hash d'audit

### Utilisation

#### Démarrage du Serveur

```bash
# Démarrage simple
python mcp-server/lairm_mcp_server.py

# Avec configuration personnalisée
python mcp-server/lairm_mcp_server.py --config config.yaml

# Avec logging
LAIRM_LOG_LEVEL=DEBUG python mcp-server/lairm_mcp_server.py
```

#### Appel des Outils

```python
from lairm_mcp_server import LAIRMMCPServer

# Initialiser serveur
server = LAIRMMCPServer()

# Chercher articles
articles = server.search_articles(
    query="kill-switch",
    Axiom="I",
    Status="Enrichi"
)

# Récupérer Article
Article = server.get_article("I-01-01")

# Récupérer Axiom
Axiom = server.get_axiome("I")

# Valider conformité
compliance = server.validate_compliance({
    "agent_id": "agent-001",
    "axiomes": ["I", "II", "III"]
})

# Auditer action
audit = server.audit_action(
    agent_id="agent-001",
    action="allocate_resource"
)
```

### Configuration

Le fichier `config.yaml` contient:

```yaml
server:
  host: localhost
  port: 8000
  debug: false

resources:
  articles_path: ../02-COMPENDIUM-LEGISLATIF
  cache_enabled: true
  cache_ttl: 3600

tools:
  search_max_results: 100
  timeout: 30

security:
  require_auth: false
  allowed_axiomes: [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX]
```

### Architecture

```
Client MCP
    ↓
LAIRMMCPServer
    ├── search_articles()
    ├── get_article()
    ├── get_axiome()
    ├── validate_compliance()
    └── audit_action()
    ↓
Framework LAIRM (399 Articles)
```

### Performance

- Chargement initial: ~500ms
- Recherche: ~50ms (avec cache)
- Récupération Article: ~10ms
- Validation conformité: ~100ms

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
