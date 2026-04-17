---
title: "Agent Framework LAIRM"
type: component
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# AGENT FRAMEWORK LAIRM
## SDK for Developing Compliant Autonomous Agents

### Description

The Agent Framework provides a complete SDK for developing autonomous agents compliant with the LAIRM framework. It includes decorators to automate compliance verification, audit, and supervision.

### Files

- `lairm_agent_sdk.py` - Main SDK (300+ lines)
- `README.md` - This documentation

### Features

#### Decorators

1. **@compliant(axioms=['I', 'II'])**
   - Verify compliance before execution
   - Validate required axioms
   - Raise exception if non-compliant

2. **@auditable**
   - Record action in audit trail
   - Compute audit hash
   - Trace responsibility

3. **@responsible**
   - Trace action responsibility
   - Record agent_id and timestamp
   - Link to audit trail

4. **@supervised**
   - Request human supervision
   - Wait for approval before execution
   - Record decision

#### LAIRMAgentSDK Class

```python
class LAIRMAgentSDK:
    def __init__(self, agent_id, axioms):
        # Initialize SDK
        
    def check_compliance(self, axioms):
        # Verify compliance
        
    def log_action(self, action, details):
        # Record action
        
    def get_audit_log(self):
        # Retrieve audit trail
        
    def get_compliance_status(self):
        # Get compliance status
```

### Usage

#### Develop Compliant Agent

```python
from lairm_agent_sdk import LAIRMAgentSDK, compliant, auditable, responsible

# Initialize SDK
sdk = LAIRMAgentSDK(
    agent_id="agent-001",
    axioms=["I", "II", "III"]
)

# Define compliant action
@compliant(axioms=["I", "II"])
@auditable
@responsible
def allocate_resource(resource_type, amount):
    """Allocate resource in a compliant manner"""
    # Automatic compliance verification
    # Automatic audit
    # Responsibility traced
    return {"status": "allocated", "amount": amount}

# Execute action
result = allocate_resource("gpu", 4)

# Get audit trail
audit = sdk.get_audit_log()
print(f"Audit entries: {len(audit)}")

# Get compliance status
status = sdk.get_compliance_status()
print(f"Compliance score: {status['score']}/100")
```

#### With Human Supervision

```python
from lairm_agent_sdk import supervised

@compliant(axioms=["I", "II", "III"])
@supervised  # Request human approval
@auditable
def critical_action(params):
    """Critical action requiring supervision"""
    # Wait for human approval
    # Record decision
    # Execute if approved
    return {"status": "executed"}

# Execute action
result = critical_action({"param": "value"})
```

#### Manual Verification

```python
# Verify compliance before action
if sdk.check_compliance(["I", "II"]):
    result = execute_action()
else:
    print("Action non-compliant")

# Record action manually
sdk.log_action(
    action="custom_action",
    details={"param": "value"}
)
```

### Architecture

```
Autonomous Agent
    ↓
LAIRMAgentSDK
    ├── @compliant
    ├── @auditable
    ├── @responsible
    └── @supervised
    ↓
Compliance Checker
Audit Engine
Agent Framework
    ↓
LAIRM Framework
```

### Audit Trail

Each action records:
- `agent_id` - Agent identifier
- `action` - Action type
- `timestamp` - When
- `axioms` - Verified axioms
- `status` - Result
- `hash` - Integrity hash

### Compliance

Automatic checks:
- ✅ Required axioms present
- ✅ Agent permissions
- ✅ Agent status
- ✅ Resource limits
- ✅ Action history

### Performance

- Initialization: ~50ms
- Compliance verification: ~10ms
- Audit recording: ~5ms
- Audit retrieval: ~20ms

### Status

- **Implementation** : ✅ Complete
- **Tests** : ✅ Passed
- **Production** : ✅ Ready

### Contributors

- Mehdi Wahbi (Founder)

---

**Version** : 1.0.0-final

