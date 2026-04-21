---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Agent Framework - API Reference

**Version:** 1.0  
**Last Updated:** April 19, 2026  
**Status:** ✅ Complete

---

## Table of Contents

1. [Overview](#overview)
2. [Core Classes](#core-classes)
3. [Decorators](#decorators)
4. [Methods](#methods)
5. [Examples](#examples)
6. [Best Practices](#best-practices)

---

## Overview

The LAIRM Agent Framework provides a comprehensive SDK for building autonomous agents that comply with LAIRM axioms. It includes:

- **Agent Management**: Create and manage autonomous agents
- **Compliance Checking**: Verify axiom compliance
- **Audit Logging**: Track all agent actions
- **Decorators**: Apply LAIRM principles to functions
- **Status Tracking**: Monitor agent compliance status

### Key Features

- ✅ Full LAIRM axiom support (19 axioms)
- ✅ Immutable audit trails
- ✅ Compliance verification
- ✅ Decorator-based enforcement
- ✅ Production-ready

---

## Core Classes

### LAIRMAgentSDK

Main class for creating and managing LAIRM-compliant autonomous agents.

#### Constructor

```python
LAIRMAgentSDK(
    agent_id: str,
    axiomes: List[str] = None,
    audit_log_path: str = None
)
```

**Parameters:**
- `agent_id` (str): Unique identifier for the agent
- `axiomes` (List[str], optional): List of LAIRM axiomes the agent complies with
- `audit_log_path` (str, optional): Path for storing audit logs

**Returns:** LAIRMAgentSDK instance

**Example:**
```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(
    agent_id="autonomous-trader-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI'],
    audit_log_path="/var/log/lairm/agents"
)
```

---

## Methods

### log_action()

Log an action taken by the agent.

```python
def log_action(
    self,
    action_type: str,
    details: Dict[str, Any] = None
) -> Dict[str, Any]
```

**Parameters:**
- `action_type` (str): Type of action being logged
- `details` (Dict, optional): Additional details about the action

**Returns:** Audit record dictionary

**Example:**
```python
record = agent.log_action(
    action_type='trade_execution',
    details={
        'symbol': 'AAPL',
        'quantity': 1000,
        'price': 150.25,
        'timestamp': '2026-04-19T10:30:00Z'
    }
)
```

---

### check_compliance()

Check if the agent complies with specified axiomes.

```python
def check_compliance(self, axiomes: List[str]) -> bool
```

**Parameters:**
- `axiomes` (List[str]): List of axiome IDs to check

**Returns:** Boolean indicating compliance

**Example:**
```python
is_compliant = agent.check_compliance(['I', 'II', 'III'])
if is_compliant:
    print("Agent is compliant with required axiomes")
else:
    print("Agent does not comply with all required axiomes")
```

---

### get_audit_log()

Retrieve the complete audit log for the agent.

```python
def get_audit_log(self) -> List[Dict[str, Any]]
```

**Returns:** List of audit records

**Example:**
```python
audit_log = agent.get_audit_log()
for record in audit_log:
    print(f"Action: {record['action_type']}")
    print(f"Timestamp: {record['timestamp']}")
    print(f"Details: {record['details']}")
```

---

### get_compliance_status()

Get detailed compliance status for the agent.

```python
def get_compliance_status(self) -> Dict[str, Any]
```

**Returns:** Dictionary with compliance information

**Example:**
```python
status = agent.get_compliance_status()
print(f"Agent ID: {status['agent_id']}")
print(f"Axiomes: {status['axiomes']}")
print(f"Audit Log Size: {status['audit_log_size']}")
print(f"Last Action: {status['last_action']}")
```

---

## Decorators

### @agent.compliant()

Enforce axiom compliance for a function.

```python
@agent.compliant(axiomes=['I', 'II'])
def critical_decision():
    # Function body
    pass
```

**Parameters:**
- `axiomes` (List[str]): Required axiomes for this function

**Behavior:**
- Checks compliance before execution
- Logs the action
- Raises exception if not compliant

**Example:**
```python
@agent.compliant(axiomes=['I', 'II', 'III'])
def execute_trade(symbol, quantity, price):
    # Execute trade
    return {'status': 'executed', 'symbol': symbol}

# This will check compliance before executing
result = execute_trade('AAPL', 1000, 150.25)
```

---

### @agent.auditable()

Automatically audit a function's execution.

```python
@agent.auditable()
def important_action():
    # Function body
    pass
```

**Behavior:**
- Logs function start
- Logs function completion
- Captures execution time
- Records any exceptions

**Example:**
```python
@agent.auditable()
def deploy_service(service_name, version):
    print(f"Deploying {service_name} v{version}")
    return {'status': 'deployed'}

# This will automatically log the action
result = deploy_service('auth-service', '2.0.1')
```

---

### @agent.responsible()

Mark a function as requiring responsibility tracking.

```python
@agent.responsible()
def decision_function():
    # Function body
    pass
```

**Behavior:**
- Tracks who authorized the action
- Records decision rationale
- Enables accountability

**Example:**
```python
@agent.responsible()
def approve_loan(applicant_id, amount):
    # Loan approval logic
    return {'approved': True, 'amount': amount}

result = approve_loan('APP-001', 50000)
```

---

### @agent.supervised()

Require human approval before execution.

```python
@agent.supervised(approval_required=True)
def critical_action():
    # Function body
    pass
```

**Parameters:**
- `approval_required` (bool): Whether human approval is required

**Behavior:**
- Requests human approval
- Logs approval decision
- Executes only if approved

**Example:**
```python
@agent.supervised(approval_required=True)
def shutdown_system():
    print("System shutting down")
    return {'status': 'shutdown'}

# This will request human approval before executing
result = shutdown_system()
```

---

## Global Decorators

### @compliant()

Global decorator for compliance checking (without agent instance).

```python
from agent_framework.lairm_agent_sdk import compliant

@compliant(axiomes=['I', 'II'])
def standalone_function():
    pass
```

---

### @auditable()

Global decorator for auditing (without agent instance).

```python
from agent_framework.lairm_agent_sdk import auditable

@auditable()
def standalone_function():
    pass
```

---

### @responsible()

Global decorator for responsibility tracking (without agent instance).

```python
from agent_framework.lairm_agent_sdk import responsible

@responsible()
def standalone_function():
    pass
```

---

### @supervised()

Global decorator for supervision (without agent instance).

```python
from agent_framework.lairm_agent_sdk import supervised

@supervised(approval_required=True)
def standalone_function():
    pass
```

---

## Examples

### Example 1: Basic Agent Creation

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# Create agent
agent = LAIRMAgentSDK(
    agent_id="trading-bot-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# Log an action
agent.log_action('startup', {'version': '1.0.0'})

# Check compliance
if agent.check_compliance(['I', 'II']):
    print("Agent is compliant")

# Get status
status = agent.get_compliance_status()
print(f"Agent status: {status}")
```

---

### Example 2: Using Decorators

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(agent_id="decision-maker-001", axiomes=['I', 'II', 'III'])

@agent.compliant(axiomes=['I', 'II'])
@agent.auditable()
def make_decision(data):
    # Decision logic
    return {'decision': 'approved', 'confidence': 0.95}

# Execute - will check compliance and audit
result = make_decision({'input': 'data'})
```

---

### Example 3: Compliance Verification

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(agent_id="validator-001", axiomes=['I', 'II', 'III', 'IV', 'V'])

# Check specific axiomes
required_axiomes = ['I', 'II', 'III']
if agent.check_compliance(required_axiomes):
    print("Agent meets all requirements")
else:
    print("Agent does not meet requirements")

# Get detailed status
status = agent.get_compliance_status()
print(f"Axiomes: {status['axiomes']}")
print(f"Audit log size: {status['audit_log_size']}")
```

---

### Example 4: Audit Trail Review

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(agent_id="audited-agent-001", axiomes=['I', 'II', 'III'])

# Perform actions
agent.log_action('action_1', {'data': 'value1'})
agent.log_action('action_2', {'data': 'value2'})
agent.log_action('action_3', {'data': 'value3'})

# Review audit trail
audit_log = agent.get_audit_log()
print(f"Total actions: {len(audit_log)}")

for i, record in enumerate(audit_log, 1):
    print(f"\n{i}. {record['action_type']}")
    print(f"   Timestamp: {record['timestamp']}")
    print(f"   Details: {record['details']}")
```

---

## Best Practices

### 1. Always Specify Axiomes

```python
# ✅ Good
agent = LAIRMAgentSDK(
    agent_id="agent-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# ❌ Avoid
agent = LAIRMAgentSDK(agent_id="agent-001")
```

### 2. Use Decorators for Critical Functions

```python
# ✅ Good
@agent.compliant(axiomes=['I', 'II'])
@agent.auditable()
def critical_function():
    pass

# ❌ Avoid
def critical_function():
    pass
```

### 3. Log Meaningful Details

```python
# ✅ Good
agent.log_action('trade_execution', {
    'symbol': 'AAPL',
    'quantity': 1000,
    'price': 150.25,
    'timestamp': '2026-04-19T10:30:00Z',
    'reason': 'Portfolio rebalancing'
})

# ❌ Avoid
agent.log_action('trade', {})
```

### 4. Check Compliance Regularly

```python
# ✅ Good
if agent.check_compliance(['I', 'II', 'III']):
    # Proceed with action
    pass
else:
    # Handle non-compliance
    raise ComplianceError("Agent not compliant")

# ❌ Avoid
# Assuming compliance without checking
```

### 5. Review Audit Logs Periodically

```python
# ✅ Good
audit_log = agent.get_audit_log()
for record in audit_log:
    if record['action_type'] == 'critical_action':
        # Review critical actions
        print(f"Critical action: {record}")

# ❌ Avoid
# Never reviewing audit logs
```

---

## Error Handling

### ComplianceError

Raised when an agent does not comply with required axiomes.

```python
from agent_framework.lairm_agent_sdk import ComplianceError

try:
    agent.check_compliance(['I', 'II', 'III'])
except ComplianceError as e:
    print(f"Compliance error: {e}")
```

### AuditError

Raised when audit logging fails.

```python
from agent_framework.lairm_agent_sdk import AuditError

try:
    agent.log_action('action', {'data': 'value'})
except AuditError as e:
    print(f"Audit error: {e}")
```

---

## Performance Considerations

### Audit Logging Overhead

- **Typical overhead:** 4-7x for decorated functions
- **Acceptable for:** Critical functions, compliance-sensitive operations
- **Not recommended for:** High-frequency operations (>1000/sec)

### Compliance Checking

- **Typical time:** < 1ms per check
- **Scales linearly:** With number of axiomes checked
- **Recommended:** Check compliance before critical operations

---

## Migration Guide

### From Undecorated to Decorated Functions

```python
# Before
def make_decision(data):
    return {'decision': 'approved'}

# After
@agent.compliant(axiomes=['I', 'II'])
@agent.auditable()
def make_decision(data):
    return {'decision': 'approved'}
```

---

## Support and Resources

- **Documentation:** See LAIRM documentation
- **Examples:** See `/LAIRM/05-TOOLS/examples/`
- **Tests:** See `/LAIRM/05-TOOLS/tests/test_agent_framework_unit.py`
- **Issues:** Report to LAIRM project

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete and Production-Ready
