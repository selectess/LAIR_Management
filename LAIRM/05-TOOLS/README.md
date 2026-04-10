---
title: "LAIRM Tools - Complete Ecosystem"
type: Section
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# LAIRM TOOLS
## Complete Ecosystem for Autonomous Agents

### Description

This section contains the complete ecosystem for integrating and using the LAIRM framework:

- **MCP Server**: Standardized access to LAIRM articles
- **Agent Framework**: SDK for developing compliant agents
- **Developer Tools**: Tools for contributors and developers
- **Workflow Engine**: LAIRM workflow orchestration
- **Compliance Checker**: Automatic compliance verification
- **Audit Engine**: Immutable traceability and audit
- **Integrations**: Connectors (OpenClaw, ARAM, etc.)

### Structure

```
05-TOOLS/
├── mcp-server/
│   ├── lairm_mcp_server.py
│   ├── resources/
│   ├── tools/
│   └── config.yaml
├── agent-framework/
│   ├── lairm_agent_sdk.py
│   ├── decorators/
│   ├── validators/
│   └── models/
├── developer-tools/
│   ├── cli/
│   ├── generators/
│   ├── validators/
│   └── templates/
├── workflow-engine/
│   ├── lairm_workflow_engine.py
│   ├── workflows/
│   └── rules/
├── compliance-checker/
│   ├── lairm_compliance_checker.py
│   ├── checkers/
│   └── rules/
├── audit-engine/
│   ├── lairm_audit_engine.py
│   ├── auditors/
│   └── storage/
└── integrations/
    ├── openclaw/
    ├── aram/
    └── external/
```

### Components

#### 1. MCP Server
Standardized interface for accessing the LAIRM framework via MCP (Model Context Protocol).

**Available Tools**:
- `search_articles(query, axiom, status)` - Search articles
- `get_article(number)` - Retrieve article
- `get_axiom(number)` - Retrieve axiom
- `validate_compliance(agent_config)` - Validate compliance
- `audit_action(agent_id, action)` - Audit action

#### 2. Agent Framework
SDK for developing autonomous agents compliant with LAIRM.

**Decorators**:
- `@compliant(axioms=['I', 'II'])` - Verify compliance
- `@auditable` - Audit action
- `@responsible` - Trace responsibility
- `@supervised` - Human supervision

#### 3. Developer Tools
Tools for contributors and developers.

**CLI**:
- `lairm validate` - Validate structure
- `lairm search` - Search articles
- `lairm generate` - Generate reports
- `lairm audit` - Audit framework

#### 4. Workflow Engine
LAIRM workflow orchestration.

**Workflows**:
- Compliance workflow - Verify compliance
- Audit workflow - Audit actions
- Approval workflow - Human approval
- Escalation workflow - Escalation

#### 5. Compliance Checker
Automatic compliance verification.

**Verifications**:
- Axiom compliance - Axiom conformity
- Article compliance - Article conformity
- Agent compliance - Agent conformity
- Action compliance - Action conformity

#### 6. Audit Engine
Immutable traceability and audit.

**Audits**:
- Action audit - Audit actions
- Decision audit - Audit decisions
- Resource audit - Audit resources
- Compliance audit - Audit compliance

#### 7. Integrations
Connectors for external systems.

**Integrations**:
- OpenClaw plugin - Native OpenClaw plugin
- ARAM connector - ARAM connector
- External APIs - External APIs
- Monitoring - Prometheus, Grafana

### Usage

#### For Agents (OpenClaw, etc.)

```python
from lairm_agent_sdk import compliant, auditable

@compliant(axioms=['I', 'II', 'III'])
@auditable
def agent_action(params):
    # Action compliant with axioms I, II, III
    return result
```

#### For Developers

```bash
# Validate LAIRM structure
lairm validate

# Search articles
lairm search --axiom I --query "kill-switch"

# Generate report
lairm generate --type compliance

# Audit framework
lairm audit --all
```

#### For MCP Clients

```python
from lairm_mcp_server import LAIRMMCPServer

server = LAIRMMCPServer()
articles = server.search_articles("kill-switch", axiom="I")
compliance = server.validate_compliance(agent_config)
```

### Status

- **Section**: Final
- **MCP Server**: Implemented
- **Agent Framework**: Implemented
- **Developer Tools**: Implemented
- **Workflow Engine**: Implemented
- **Compliance Checker**: Implemented
- **Audit Engine**: Implemented
- **Integrations**: Implemented

### Contributors

- Mehdi Wahbi (Founder)

---

**Last Updated**: March 30, 2026
**Version**: 1.0.0-final
**Status**: Production-Ready

**Last Reviewed**: April 3, 2026
