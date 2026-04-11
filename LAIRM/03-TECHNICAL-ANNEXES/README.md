---
title: "LAIRM Technical Annexes"
type: Section
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# LAIRM Technical Annexes
## Specifications, Implementations and Schemas

### Description

This section contains technical specifications, reference implementations, and data schemas for the LAIRM framework. It provides the technical foundations for integrating the LAIRM framework into autonomous agent systems.

### Structure

```
03-TECHNICAL-ANNEXES/
├── specifications/
│   ├── kill-switch-spec.md
│   ├── did-agent-spec.md
│   ├── mcp-protocol-spec.md
│   ├── a2a-protocol-spec.md
│   └── audit-log-spec.md
├── implementations/
│   ├── python/
│   │   ├── lairm_core.py
│   │   ├── compliance_engine.py
│   │   └── audit_engine.py
│   ├── rust/
│   │   ├── lairm_core.rs
│   │   └── compliance_engine.rs
│   ├── go/
│   │   └── lairm_core.go
│   ├── solidity/
│   │   └── LAIRMCore.sol
│   └── reference/
│       ├── agent_example.py
│       └── workflow_example.py
└── schemas/
    ├── agent-passport-schema.json
    ├── audit-log-schema.json
    ├── kill-signal-schema.json
    ├── compliance-report-schema.json
    └── action-record-schema.json
```

### Content

#### Technical Specifications

- **kill-switch-spec.md**: Universal kill-switch specification (Axiom I)
- **did-agent-spec.md**: DID specification for agents (Axiom II)
- **mcp-protocol-spec.md**: MCP protocol specification (Axiom V)
- **a2a-protocol-spec.md**: A2A protocol specification (Axiom V)
- **audit-log-spec.md**: Audit log specification (Axiom VI)

#### Implementations

**Python** (Production-ready):
- `lairm_core.py`: LAIRM core framework in Python
- `compliance_engine.py`: Compliance engine
- `audit_engine.py`: Audit engine

**Rust** (High-performance):
- `lairm_core.rs`: LAIRM core framework in Rust
- `compliance_engine.rs`: High-performance compliance engine

**Go** (Concurrent):
- `lairm_core.go`: LAIRM core framework in Go

**Solidity** (Blockchain):
- `LAIRMCore.sol`: LAIRM core framework for Ethereum/EVM chains

**Examples**:
- `agent_example.py`: Compliant agent example
- `workflow_example.py`: LAIRM workflow example

#### Schemas

- **agent-passport-schema.json**: Unique agent identity
- **audit-log-schema.json**: Immutable audit log format
- **kill-signal-schema.json**: Emergency stop signal
- **compliance-report-schema.json**: Compliance report
- **action-record-schema.json**: Agent action record

### Usage

#### For Developers

```bash
# Import LAIRM core
from lairm_core import LAIRMFramework

# Create instance
lairm = LAIRMFramework()

# Check compliance
compliance = lairm.check_compliance(agent_config)

# Audit action
audit_record = lairm.audit_action(agent_id, action)
```

#### For Agents

```python
from lairm_agent_sdk import compliant, auditable

@compliant(axiomes=['I', 'II', 'III'])
@auditable
def agent_action(params):
    # Action compliant with axioms I, II, III
    return result
```

### Status

- **Section**: Final
- **Specifications**: Complete
- **Implementations**: Python, Rust, Go, Solidity
- **Schemas**: Defined and validated

### Contributors

- Mehdi Wahbi (Founder)

---

**Version**: 1.0.0-final

