---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Best Practices Guide

**Version:** 1.0  
**Last Updated:** April 19, 2026

---

## Table of Contents

1. [Agent Design](#agent-design)
2. [Compliance Management](#compliance-management)
3. [Audit Logging](#audit-logging)
4. [Performance Optimization](#performance-optimization)
5. [Security](#security)
6. [Testing](#testing)
7. [Deployment](#deployment)

---

## Agent Design

### 1. Always Specify Axiomes

**✅ Good:**
```python
agent = LAIRMAgentSDK(
    agent_id="trading-bot-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)
```

**❌ Bad:**
```python
agent = LAIRMAgentSDK(agent_id="trading-bot-001")
```

**Why:** Specifying axiomes ensures the agent is designed for compliance from the start.

---

### 2. Use Meaningful Agent IDs

**✅ Good:**
```python
agent = LAIRMAgentSDK(
    agent_id="trading-bot-equity-001",
    axiomes=['I', 'II', 'III']
)
```

**❌ Bad:**
```python
agent = LAIRMAgentSDK(
    agent_id="bot1",
    axiomes=['I', 'II', 'III']
)
```

**Why:** Meaningful IDs make audit trails easier to understand and trace.

---

### 3. Design for Compliance from the Start

**✅ Good:**
```python
class ComplianceFirstAgent:
    def __init__(self):
        self.agent = LAIRMAgentSDK(
            agent_id="compliant-agent",
            axiomes=['I', 'II', 'III', 'IV', 'VI']
        )
    
    @property
    def required_axiomes(self):
        return ['I', 'II', 'III']
    
    def execute_action(self, action_data):
        # Check compliance first
        if not self.agent.check_compliance(self.required_axiomes):
            raise ComplianceError("Agent not compliant")
        
        # Then execute
        return self._execute(action_data)
```

**❌ Bad:**
```python
class NonCompliantAgent:
    def __init__(self):
        self.agent = LAIRMAgentSDK(agent_id="agent")
    
    def execute_action(self, action_data):
        # Execute first, check compliance later
        result = self._execute(action_data)
        self.agent.check_compliance(['I', 'II'])
        return result
```

**Why:** Compliance-first design prevents violations before they happen.

---

## Compliance Management

### 1. Regular Compliance Verification

**✅ Good:**
```python
class ComplianceMonitor:
    def __init__(self, agent):
        self.agent = agent
        self.check_interval = 60  # seconds
    
    def monitor(self):
        while True:
            if not self.agent.check_compliance(['I', 'II', 'III']):
                self.alert_compliance_violation()
            time.sleep(self.check_interval)
    
    def alert_compliance_violation(self):
        self.agent.log_action('compliance_violation', {
            'severity': 'high',
            'timestamp': datetime.now().isoformat()
        })
```

**❌ Bad:**
```python
# Never checking compliance
agent.execute_action(data)
agent.execute_action(data)
agent.execute_action(data)
```

**Why:** Regular monitoring catches compliance issues early.

---

### 2. Document Compliance Requirements

**✅ Good:**
```python
class DocumentedAgent:
    """
    Trading Agent with LAIRM Compliance
    
    Required Axiomes:
    - Axiom I (SUPREMATIA): Human supremacy with kill-switch
    - Axiom II (IDENTITAS): Unique agent identity
    - Axiom III (RESPONSABILITAS): Clear accountability
    - Axiom IV (CIRCULUS): Feedback loop detection
    - Axiom VI (AUDITUM): Immutable audit trails
    
    Compliance Checks:
    - Kill-switch response time: < 500ms
    - Audit trail: Immutable ledger
    - Identity: DID-based
    """
    
    REQUIRED_AXIOMES = ['I', 'II', 'III', 'IV', 'VI']
    
    def __init__(self):
        self.agent = LAIRMAgentSDK(
            agent_id="documented-agent",
            axiomes=self.REQUIRED_AXIOMES
        )
```

**❌ Bad:**
```python
# No documentation
agent = LAIRMAgentSDK(agent_id="agent", axiomes=['I', 'II'])
```

**Why:** Documentation ensures compliance requirements are clear and maintainable.

---

## Audit Logging

### 1. Log Meaningful Details

**✅ Good:**
```python
agent.log_action('trade_execution', {
    'symbol': 'AAPL',
    'quantity': 1000,
    'price': 150.25,
    'order_type': 'market',
    'execution_time_ms': 45,
    'slippage_bps': 2.5,
    'reason': 'Portfolio rebalancing',
    'trader_id': 'trader-001',
    'approval_id': 'approval-12345'
})
```

**❌ Bad:**
```python
agent.log_action('trade', {})
agent.log_action('trade', {'data': 'executed'})
```

**Why:** Detailed logs enable proper auditing and investigation.

---

### 2. Log Both Success and Failure

**✅ Good:**
```python
try:
    result = execute_trade(symbol, quantity, price)
    agent.log_action('trade_success', {
        'symbol': symbol,
        'result': result
    })
except Exception as e:
    agent.log_action('trade_failure', {
        'symbol': symbol,
        'error': str(e),
        'error_type': type(e).__name__
    })
    raise
```

**❌ Bad:**
```python
# Only logging success
result = execute_trade(symbol, quantity, price)
agent.log_action('trade', {'result': result})
```

**Why:** Logging failures is critical for debugging and compliance.

---

### 3. Include Timestamps and Context

**✅ Good:**
```python
agent.log_action('decision', {
    'timestamp': datetime.now().isoformat(),
    'decision_id': str(uuid.uuid4()),
    'context': {
        'market_conditions': 'volatile',
        'portfolio_exposure': 0.85,
        'risk_level': 'high'
    },
    'decision': 'hold',
    'confidence': 0.92
})
```

**❌ Bad:**
```python
agent.log_action('decision', {'decision': 'hold'})
```

**Why:** Context helps understand why decisions were made.

---

## Performance Optimization

### 1. Batch Logging for High-Frequency Operations

**✅ Good:**
```python
class BatchLogger:
    def __init__(self, agent, batch_size=100):
        self.agent = agent
        self.batch_size = batch_size
        self.batch = []
    
    def log(self, action_type, details):
        self.batch.append({'action_type': action_type, 'details': details})
        if len(self.batch) >= self.batch_size:
            self.flush()
    
    def flush(self):
        for item in self.batch:
            self.agent.log_action(item['action_type'], item['details'])
        self.batch = []

# Usage
logger = BatchLogger(agent, batch_size=100)
for i in range(10000):
    logger.log('tick', {'price': 150.25 + i * 0.01})
logger.flush()
```

**❌ Bad:**
```python
# Logging every tick individually
for i in range(10000):
    agent.log_action('tick', {'price': 150.25 + i * 0.01})
```

**Why:** Batching reduces overhead for high-frequency operations.

---

### 2. Cache Compliance Checks

**✅ Good:**
```python
from functools import lru_cache

class CachedComplianceChecker:
    def __init__(self, agent):
        self.agent = agent
    
    @lru_cache(maxsize=1000)
    def check_compliance_cached(self, axiomes_tuple):
        return self.agent.check_compliance(list(axiomes_tuple))
    
    def check_compliance(self, axiomes):
        return self.check_compliance_cached(tuple(axiomes))

# Usage
checker = CachedComplianceChecker(agent)
for i in range(1000):
    checker.check_compliance(['I', 'II', 'III'])  # Cached after first call
```

**❌ Bad:**
```python
# Checking compliance every time
for i in range(1000):
    agent.check_compliance(['I', 'II', 'III'])
```

**Why:** Caching reduces redundant compliance checks.

---

## Security

### 1. Validate All Inputs

**✅ Good:**
```python
def execute_trade(agent, symbol, quantity, price):
    # Validate inputs
    if not isinstance(symbol, str) or len(symbol) == 0:
        raise ValueError("Invalid symbol")
    
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Invalid quantity")
    
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Invalid price")
    
    # Log and execute
    agent.log_action('trade', {
        'symbol': symbol,
        'quantity': quantity,
        'price': price
    })
    
    return _execute_trade(symbol, quantity, price)
```

**❌ Bad:**
```python
# No validation
def execute_trade(agent, symbol, quantity, price):
    agent.log_action('trade', {
        'symbol': symbol,
        'quantity': quantity,
        'price': price
    })
    return _execute_trade(symbol, quantity, price)
```

**Why:** Input validation prevents injection attacks and data corruption.

---

### 2. Protect Audit Trails

**✅ Good:**
```python
class SecureAuditTrail:
    def __init__(self, agent):
        self.agent = agent
        self.chain = []
    
    def add_record(self, record):
        # Add cryptographic chain
        if self.chain:
            record['previous_hash'] = self.chain[-1]['hash']
        else:
            record['previous_hash'] = '0' * 64
        
        record_json = json.dumps(record, sort_keys=True)
        record['hash'] = hashlib.sha256(record_json.encode()).hexdigest()
        
        self.chain.append(record)
    
    def verify_integrity(self):
        for i, record in enumerate(self.chain):
            if i > 0:
                if record['previous_hash'] != self.chain[i-1]['hash']:
                    return False
        return True
```

**❌ Bad:**
```python
# Unprotected audit trail
audit_log = []
audit_log.append(record)  # Can be modified
```

**Why:** Cryptographic protection ensures audit trail integrity.

---

### 3. Implement Access Control

**✅ Good:**
```python
class AccessControlledAgent:
    def __init__(self, agent, authorized_users):
        self.agent = agent
        self.authorized_users = authorized_users
    
    def log_action_secure(self, user_id, action_type, details):
        if user_id not in self.authorized_users:
            raise PermissionError(f"User {user_id} not authorized")
        
        self.agent.log_action(action_type, {
            'user_id': user_id,
            'details': details
        })
```

**❌ Bad:**
```python
# No access control
def log_action(action_type, details):
    agent.log_action(action_type, details)
```

**Why:** Access control prevents unauthorized operations.

---

## Testing

### 1. Test Compliance

**✅ Good:**
```python
def test_agent_compliance():
    agent = LAIRMAgentSDK(
        agent_id="test-agent",
        axiomes=['I', 'II', 'III']
    )
    
    # Test compliance
    assert agent.check_compliance(['I', 'II', 'III'])
    assert not agent.check_compliance(['I', 'II', 'III', 'IV'])
    
    # Test status
    status = agent.get_compliance_status()
    assert status['axiomes'] == ['I', 'II', 'III']
```

**❌ Bad:**
```python
# No compliance testing
agent = LAIRMAgentSDK(agent_id="test-agent", axiomes=['I', 'II', 'III'])
# No assertions
```

**Why:** Testing ensures compliance is maintained.

---

### 2. Test Audit Logging

**✅ Good:**
```python
def test_audit_logging():
    agent = LAIRMAgentSDK(agent_id="test-agent", axiomes=['I', 'II'])
    
    # Log actions
    agent.log_action('action_1', {'data': 'value1'})
    agent.log_action('action_2', {'data': 'value2'})
    
    # Verify audit log
    audit_log = agent.get_audit_log()
    assert len(audit_log) == 2
    assert audit_log[0]['action_type'] == 'action_1'
    assert audit_log[1]['action_type'] == 'action_2'
```

**❌ Bad:**
```python
# No audit logging tests
agent.log_action('action', {'data': 'value'})
# No verification
```

**Why:** Testing ensures audit trails are complete and accurate.

---

## Deployment

### 1. Use Configuration Management

**✅ Good:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

class AgentConfig:
    AGENT_ID = os.getenv('AGENT_ID', 'default-agent')
    AXIOMES = os.getenv('AXIOMES', 'I,II,III').split(',')
    AUDIT_LOG_PATH = os.getenv('AUDIT_LOG_PATH', '/var/log/lairm')
    MCP_SERVER_URL = os.getenv('MCP_SERVER_URL', 'http://localhost:8080')

# Usage
agent = LAIRMAgentSDK(
    agent_id=AgentConfig.AGENT_ID,
    axiomes=AgentConfig.AXIOMES,
    audit_log_path=AgentConfig.AUDIT_LOG_PATH
)
```

**❌ Bad:**
```python
# Hardcoded configuration
agent = LAIRMAgentSDK(
    agent_id="trading-bot-001",
    axiomes=['I', 'II', 'III'],
    audit_log_path="/var/log/lairm"
)
```

**Why:** Configuration management enables easy deployment across environments.

---

### 2. Monitor Agent Health

**✅ Good:**
```python
class AgentHealthMonitor:
    def __init__(self, agent):
        self.agent = agent
    
    def check_health(self):
        health = {
            'agent_id': self.agent.agent_id,
            'compliant': self.agent.check_compliance(self.agent.axiomes),
            'audit_log_size': len(self.agent.get_audit_log()),
            'status': self.agent.get_compliance_status()
        }
        
        if not health['compliant']:
            self.alert_compliance_issue()
        
        return health
    
    def alert_compliance_issue(self):
        # Send alert
        print("⚠️ Agent compliance issue detected")

# Usage
monitor = AgentHealthMonitor(agent)
health = monitor.check_health()
```

**❌ Bad:**
```python
# No monitoring
agent = LAIRMAgentSDK(agent_id="agent", axiomes=['I', 'II'])
# No health checks
```

**Why:** Monitoring ensures agents remain compliant in production.

---

### 3. Implement Graceful Shutdown

**✅ Good:**
```python
import signal

class GracefulAgent:
    def __init__(self, agent):
        self.agent = agent
        self.running = True
        signal.signal(signal.SIGTERM, self.shutdown)
    
    def shutdown(self, signum, frame):
        self.agent.log_action('shutdown', {
            'reason': 'SIGTERM received',
            'timestamp': datetime.now().isoformat()
        })
        self.running = False
    
    def run(self):
        while self.running:
            # Agent logic
            pass

# Usage
graceful_agent = GracefulAgent(agent)
graceful_agent.run()
```

**❌ Bad:**
```python
# No graceful shutdown
while True:
    agent.execute_action(data)
```

**Why:** Graceful shutdown ensures audit trails are complete.

---

## Summary

Key best practices:
- ✅ Always specify axiomes
- ✅ Use meaningful IDs
- ✅ Design for compliance
- ✅ Log meaningful details
- ✅ Validate inputs
- ✅ Protect audit trails
- ✅ Test thoroughly
- ✅ Monitor health
- ✅ Implement graceful shutdown

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
