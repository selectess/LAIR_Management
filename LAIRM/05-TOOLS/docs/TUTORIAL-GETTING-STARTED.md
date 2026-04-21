---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Getting Started Guide

**Version:** 1.0  
**Last Updated:** April 19, 2026  
**Difficulty:** Beginner

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Your First Agent](#your-first-agent)
4. [Understanding Axiomes](#understanding-axiomes)
5. [Logging Actions](#logging-actions)
6. [Checking Compliance](#checking-compliance)
7. [Next Steps](#next-steps)

---

## Introduction

Welcome to LAIRM! This guide will help you create your first LAIRM-compliant autonomous agent in 10 minutes.

### What You'll Learn

- ✅ How to install LAIRM
- ✅ How to create an autonomous agent
- ✅ How to log actions
- ✅ How to verify compliance
- ✅ How to review audit trails

### Prerequisites

- Python 3.8+
- Basic Python knowledge
- 10 minutes of your time

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/lairm/lairm-framework.git
cd lairm-framework/LAIRM/05-TOOLS
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
python -c "from agent_framework.lairm_agent_sdk import LAIRMAgentSDK; print('✅ LAIRM installed successfully')"
```

---

## Your First Agent

### Step 1: Create a Python File

Create a file called `my_first_agent.py`:

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# Create an agent
agent = LAIRMAgentSDK(
    agent_id="my-first-agent",
    axiomes=['I', 'II', 'III']
)

print(f"✅ Agent created: {agent.agent_id}")
```

### Step 2: Run Your Agent

```bash
python my_first_agent.py
```

**Output:**
```
✅ Agent created: my-first-agent
```

Congratulations! You've created your first LAIRM agent! 🎉

---

## Understanding Axiomes

LAIRM defines 19 axiomes that govern autonomous agents. Let's start with the core three:

### Axiom I: SUPREMATIA (Human Supremacy)

Humans remain in ultimate control. Agents must have kill-switches.

```python
# Axiom I ensures humans can stop the agent
agent = LAIRMAgentSDK(
    agent_id="controlled-agent",
    axiomes=['I']  # Requires human supremacy
)
```

### Axiom II: IDENTITAS (Agent Identity)

Every agent has a unique, verifiable identity.

```python
# Axiom II ensures the agent has a unique identity
agent = LAIRMAgentSDK(
    agent_id="identified-agent",
    axiomes=['II']  # Requires unique identity
)

print(f"Agent ID: {agent.agent_id}")
```

### Axiom III: RESPONSABILITAS (Accountability)

Clear responsibility chains for agent actions.

```python
# Axiom III ensures accountability
agent = LAIRMAgentSDK(
    agent_id="accountable-agent",
    axiomes=['III']  # Requires accountability
)
```

---

## Logging Actions

### Basic Action Logging

Log what your agent does:

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(
    agent_id="logging-agent",
    axiomes=['I', 'II', 'III']
)

# Log an action
record = agent.log_action(
    action_type='startup',
    details={'version': '1.0.0', 'status': 'ready'}
)

print(f"✅ Action logged: {record['action_type']}")
```

### Logging with Details

Include meaningful details:

```python
# Log a decision
agent.log_action(
    action_type='decision',
    details={
        'decision_type': 'trade_execution',
        'symbol': 'AAPL',
        'quantity': 100,
        'price': 150.25,
        'reason': 'Portfolio rebalancing',
        'confidence': 0.95
    }
)

print("✅ Decision logged with details")
```

### Logging Errors

Log when things go wrong:

```python
try:
    # Some operation
    result = 1 / 0
except Exception as e:
    agent.log_action(
        action_type='error',
        details={
            'error_type': type(e).__name__,
            'error_message': str(e),
            'severity': 'high'
        }
    )
    print("✅ Error logged")
```

---

## Checking Compliance

### Verify Axiom Compliance

Check if your agent complies with required axiomes:

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(
    agent_id="compliant-agent",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# Check compliance
required_axiomes = ['I', 'II', 'III']
is_compliant = agent.check_compliance(required_axiomes)

if is_compliant:
    print("✅ Agent is compliant with all required axiomes")
else:
    print("❌ Agent does not comply with all required axiomes")
```

### Get Compliance Status

Get detailed compliance information:

```python
status = agent.get_compliance_status()

print(f"Agent ID: {status['agent_id']}")
print(f"Axiomes: {status['axiomes']}")
print(f"Audit Log Size: {status['audit_log_size']}")
print(f"Last Action: {status['last_action']}")
```

---

## Reviewing Audit Trails

### View All Actions

See everything your agent has done:

```python
# Get the audit log
audit_log = agent.get_audit_log()

print(f"Total actions: {len(audit_log)}\n")

for i, record in enumerate(audit_log, 1):
    print(f"{i}. {record['action_type']}")
    print(f"   Timestamp: {record['timestamp']}")
    print(f"   Details: {record['details']}\n")
```

### Filter Actions

Find specific actions:

```python
audit_log = agent.get_audit_log()

# Find all decisions
decisions = [r for r in audit_log if r['action_type'] == 'decision']
print(f"Total decisions: {len(decisions)}")

# Find all errors
errors = [r for r in audit_log if r['action_type'] == 'error']
print(f"Total errors: {len(errors)}")
```

---

## Complete Example

Here's a complete example putting it all together:

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# Create agent
agent = LAIRMAgentSDK(
    agent_id="trading-bot-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

print("=== LAIRM Agent Demo ===\n")

# Log startup
agent.log_action('startup', {
    'version': '1.0.0',
    'status': 'ready',
    'timestamp': '2026-04-19T10:00:00Z'
})

# Check compliance
if agent.check_compliance(['I', 'II', 'III']):
    print("✅ Agent is compliant\n")

# Log some decisions
for i in range(3):
    agent.log_action('decision', {
        'decision_id': f'D-{i+1}',
        'type': 'trade',
        'symbol': 'AAPL',
        'quantity': 100 * (i + 1),
        'confidence': 0.90 + (i * 0.03)
    })

# Get status
status = agent.get_compliance_status()
print(f"Agent Status:")
print(f"  ID: {status['agent_id']}")
print(f"  Axiomes: {status['axiomes']}")
print(f"  Actions: {status['audit_log_size']}\n")

# Review audit trail
audit_log = agent.get_audit_log()
print(f"Audit Trail ({len(audit_log)} actions):")
for record in audit_log:
    print(f"  - {record['action_type']} at {record['timestamp']}")

print("\n✅ Demo complete!")
```

**Output:**
```
=== LAIRM Agent Demo ===

✅ Agent is compliant

Agent Status:
  ID: trading-bot-001
  Axiomes: ['I', 'II', 'III', 'IV', 'VI']
  Actions: 4

Audit Trail (4 actions):
  - startup at 2026-04-19T10:00:00.000000Z
  - decision at 2026-04-19T10:00:00.001234Z
  - decision at 2026-04-19T10:00:00.002456Z
  - decision at 2026-04-19T10:00:00.003678Z

✅ Demo complete!
```

---

## Common Patterns

### Pattern 1: Decision Making

```python
@agent.compliant(axiomes=['I', 'II'])
@agent.auditable()
def make_decision(data):
    # Your decision logic
    decision = analyze_data(data)
    return decision

result = make_decision({'input': 'data'})
```

### Pattern 2: Error Handling

```python
try:
    result = risky_operation()
except Exception as e:
    agent.log_action('error', {
        'operation': 'risky_operation',
        'error': str(e),
        'severity': 'high'
    })
```

### Pattern 3: Compliance Verification

```python
required_axiomes = ['I', 'II', 'III']
if agent.check_compliance(required_axiomes):
    # Proceed with operation
    execute_operation()
else:
    # Handle non-compliance
    raise ComplianceError("Agent not compliant")
```

---

## Troubleshooting

### Issue: "Agent not compliant"

**Solution:** Check that the agent has the required axiomes:

```python
# Check what axiomes the agent has
status = agent.get_compliance_status()
print(f"Agent axiomes: {status['axiomes']}")

# Create agent with required axiomes
agent = LAIRMAgentSDK(
    agent_id="agent-001",
    axiomes=['I', 'II', 'III']  # Add required axiomes
)
```

### Issue: "Audit log is empty"

**Solution:** Make sure you're logging actions:

```python
# Log an action
agent.log_action('test_action', {'data': 'value'})

# Now check the audit log
audit_log = agent.get_audit_log()
print(f"Audit log size: {len(audit_log)}")
```

### Issue: "Import error"

**Solution:** Make sure LAIRM is installed:

```bash
pip install -r requirements.txt
python -c "from agent_framework.lairm_agent_sdk import LAIRMAgentSDK; print('✅ OK')"
```

---

## Next Steps

### Learn More

1. **Advanced Usage**: See [TUTORIAL-ADVANCED-USAGE.md](TUTORIAL-ADVANCED-USAGE.md)
2. **Integration Guide**: See [TUTORIAL-INTEGRATION.md](TUTORIAL-INTEGRATION.md)
3. **API Reference**: See [API-REFERENCE-AGENT-FRAMEWORK.md](API-REFERENCE-AGENT-FRAMEWORK.md)

### Try These Exercises

1. **Exercise 1**: Create an agent with all 19 axiomes
2. **Exercise 2**: Log 10 different types of actions
3. **Exercise 3**: Implement a decision-making function with decorators
4. **Exercise 4**: Review and analyze an audit trail

### Get Help

- **Documentation**: See `/LAIRM/05-TOOLS/docs/`
- **Examples**: See `/LAIRM/05-TOOLS/examples/`
- **Tests**: See `/LAIRM/05-TOOLS/tests/`

---

## Summary

You've learned:
- ✅ How to install LAIRM
- ✅ How to create an autonomous agent
- ✅ How to understand axiomes
- ✅ How to log actions
- ✅ How to verify compliance
- ✅ How to review audit trails

**Congratulations! You're ready to build LAIRM-compliant agents!** 🚀

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
