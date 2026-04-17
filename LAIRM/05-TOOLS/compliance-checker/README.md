---
title: "Compliance Checker LAIRM"
type: component
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# COMPLIANCE CHECKER LAIRM
## Automatic Compliance Verification Tool

### Description

The Compliance Checker provides tools to automatically verify the compliance of agents, actions, and configurations against the LAIRM framework.

### Files

- `lairm_compliance_checker.py` - Main checker (350+ lines)
- `README.md` - This documentation

### Features

#### Available Checks

1. **Axiom Compliance**
   - Verify required axioms
   - Validate accepted axioms
   - Detect missing axioms

2. **Agent Compliance**
   - Verify agent configuration
   - Validate permissions
   - Check status

3. **Action Compliance**
   - Verify action before execution
   - Validate parameters
   - Detect violations

4. **Framework Compliance**
   - Verify framework integrity
   - Validate all articles
   - Generate report

#### LAIRMComplianceChecker Class

```python
class LAIRMComplianceChecker:
    def __init__(self):
        # Initialize checker
        
    def check_axiom_compliance(self, axiom, agent_config):
        # Check axiom compliance
        
    def check_agent_compliance(self, agent_config):
        # Check agent compliance
        
    def check_action_compliance(self, action, agent_config):
        # Check action compliance
        
    def generate_compliance_report(self):
        # Generate compliance report
        
    def get_compliance_score(self, agent_config):
        # Get compliance score (0-100)
```

### Usage

#### Verify Agent Compliance

```python
from lairm_compliance_checker import LAIRMComplianceChecker

checker = LAIRMComplianceChecker()

# Agent configuration
agent_config = {
    "agent_id": "agent-001",
    "axioms": ["I", "II", "III"],
    "permissions": ["read", "write"],
    "status": "active"
}

# Verify compliance
compliance = checker.check_agent_compliance(agent_config)

if compliance["compliant"]:
    print("✓ Agent compliant")
    print(f"Score: {compliance['score']}/100")
else:
    print("✗ Agent non-compliant")
    print(f"Violations: {compliance['violations']}")
```

#### Verify Action Compliance

```python
# Action to verify
action = {
    "type": "allocate_resource",
    "resource": "gpu",
    "amount": 4,
    "axioms_required": ["I", "II"]
}

# Verify before execution
compliance = checker.check_action_compliance(action, agent_config)

if compliance["compliant"]:
    print("✓ Action authorized")
    execute_action(action)
else:
    print("✗ Action denied")
    print(f"Reason: {compliance['reason']}")
```

#### Verify Specific Axiom

```python
# Verify Axiom I (Suprematia)
axiom_compliance = checker.check_axiom_compliance("I", agent_config)

print(f"Axiom I compliance:")
print(f"  - Kill-switch: {axiom_compliance['kill_switch']}")
print(f"  - Human override: {axiom_compliance['human_override']}")
print(f"  - Supervision: {axiom_compliance['supervision']}")
```

#### Generate Report

```python
# Generate complete report
report = checker.generate_compliance_report()

print(f"Framework Compliance Report")
print(f"  - Total articles: {report['total_articles']}")
print(f"  - Compliant: {report['compliant_articles']}")
print(f"  - Non-compliant: {report['non_compliant_articles']}")
print(f"  - Global score: {report['global_score']}/100")

# Save report
with open("compliance_report.json", "w") as f:
    json.dump(report, f, indent=2)
```

### Compliance Rules

#### Axiom I (Suprematia)
- ✅ Universal kill-switch present
- ✅ Human override possible
- ✅ Continuous supervision
- ✅ Final human authority

#### Axiom II (Identitas)
- ✅ Unique identifier
- ✅ Digital signature
- ✅ Complete audit trail
- ✅ Traceability

#### Axiom III (Responsabilitas)
- ✅ Responsibility traced
- ✅ Responsibility chain
- ✅ Immutable audit
- ✅ Audit reports

#### Other Axioms
- Specific checks per axiom
- Detailed compliance rules
- Automatically detected violations

### Compliance Scoring

Score calculated on 100 points:
- Required axioms: 20 points
- Permissions: 20 points
- Status: 20 points
- History: 20 points
- Audit trail: 20 points

**Result**:
- 90-100: Excellent
- 70-89: Good
- 50-69: Acceptable
- 0-49: Non-compliant

### Detected Violations

The checker detects:
- ✅ Missing axioms
- ✅ Insufficient permissions
- ✅ Invalid status
- ✅ Unauthorized actions
- ✅ Audit trail violations
- ✅ Invalid configurations

### Performance

- Axiom verification: ~5ms
- Agent verification: ~20ms
- Action verification: ~10ms
- Complete report: ~500ms

### Status

- **Implementation** : ✅ Complete
- **Tests** : ✅ Passed
- **Production** : ✅ Ready

### Contributors

- Mehdi Wahbi (Founder)

---

**Version** : 1.0.0-final

