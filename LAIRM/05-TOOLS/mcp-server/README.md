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
## Standardized Interface for LAIRM Framework

### Description

The MCP Server provides a standardized interface (Model Context Protocol) to access the LAIRM framework. It allows MCP clients to search, retrieve, and validate framework articles.

### Files

- `lairm_mcp_server.py` - Main MCP server (400+ lines)
- `config.yaml` - Server configuration
- `README.md` - This documentation

### Features

#### Available MCP Tools

1. **search_articles(query, axiom, status)**
   - Search articles by query, axiom, or status
   - Returns list of matching articles
   - Supports multi-criteria filtering

2. **get_article(number)**
   - Retrieve complete article by number
   - Returns content, metadata, validations
   - Includes links to related articles

3. **get_axiom(number)**
   - Retrieve complete axiom
   - Returns all articles of the axiom
   - Includes statistics and compliance

4. **validate_compliance(agent_config)**
   - Validate agent compliance
   - Verifies required axioms
   - Returns compliance score

5. **audit_action(agent_id, action)**
   - Audit agent action
   - Records in audit trail
   - Returns audit hash

### Usage

#### Start the Server

```bash
# Simple startup
python mcp-server/lairm_mcp_server.py

# With custom configuration
python mcp-server/lairm_mcp_server.py --config config.yaml

# With logging
LAIRM_LOG_LEVEL=DEBUG python mcp-server/lairm_mcp_server.py
```

#### Call Tools

```python
from lairm_mcp_server import LAIRMMCPServer

# Initialize server
server = LAIRMMCPServer()

# Search articles
articles = server.search_articles(
    query="kill-switch",
    axiom="I",
    status="Enriched"
)

# Retrieve article
article = server.get_article("I-01-01")

# Retrieve axiom
axiom = server.get_axiom("I")

# Validate compliance
compliance = server.validate_compliance({
    "agent_id": "agent-001",
    "axioms": ["I", "II", "III"]
})

# Audit action
audit = server.audit_action(
    agent_id="agent-001",
    action="allocate_resource"
)
```

### Configuration

The `config.yaml` file contains:

```yaml
server:
  host: localhost
  port: 8000
  debug: false

resources:
  articles_path: ../02-COMPENDIUM-LEGISLATIVE
  cache_enabled: true
  cache_ttl: 3600

tools:
  search_max_results: 100
  timeout: 30

security:
  require_auth: false
  allowed_axioms: [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX]
```

### Architecture

```
MCP Client
    ↓
LAIRMMCPServer
    ├── search_articles()
    ├── get_article()
    ├── get_axiom()
    ├── validate_compliance()
    └── audit_action()
    ↓
LAIRM Framework (399 Articles)
```

### Performance

- Initial load: ~500ms
- Search: ~50ms (with cache)
- Article retrieval: ~10ms
- Compliance validation: ~100ms

### Status

- **Implementation** : ✅ Complete
- **Tests** : ✅ Passed
- **Production** : ✅ Ready

### Contributors

- Mehdi Wahbi (Founder)

---

**Version** : 1.0.0-final

