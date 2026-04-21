---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Advanced Usage Guide

**Version:** 1.0  
**Last Updated:** April 19, 2026  
**Difficulty:** Advanced

---

## Table of Contents

1. [Advanced Decorators](#advanced-decorators)
2. [Custom Compliance Rules](#custom-compliance-rules)
3. [Multi-Agent Systems](#multi-agent-systems)
4. [Performance Optimization](#performance-optimization)
5. [Security Considerations](#security-considerations)
6. [Advanced Patterns](#advanced-patterns)

---

## Advanced Decorators

### Stacking Decorators

Combine multiple decorators for comprehensive control:

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

agent = LAIRMAgentSDK(agent_id="advanced-agent", axiomes=['I', 'II', 'III', 'IV', 'VI'])

@agent.supervised(approval_required=True)
@agent.responsible()
@agent.auditable()
@agent.compliant(axiomes=['I', 'II', 'III'])
def critical_decision(data):
    """
    This function:
    1. Requires human approval (supervised)
    2. Tracks responsibility (responsible)
    3. Logs execution (auditable)
    4. Verifies compliance (compliant)
    """
    return {'decision': 'approved', 'confidence': 0.95}

# Execute - will go through all decorator checks
result = critical_decision({'input': 'data'})
```

### Conditional Decorators

Apply decorators conditionally:

```python
def apply_decorators(func, require_approval=False):
    if require_approval:
        func = agent.supervised(approval_required=True)(func)
    func = agent.auditable()(func)
    func = agent.compliant(axiomes=['I', 'II'])(func)
    return func

@apply_decorators
def standard_function():
    return "result"

@apply_decorators(require_approval=True)
def critical_function():
    return "result"
```

### Custom Decorator Chains

Create reusable decorator chains:

```python
def critical_operation(func):
    """Decorator chain for critical operations"""
    @agent.supervised(approval_required=True)
    @agent.responsible()
    @agent.auditable()
    @agent.compliant(axiomes=['I', 'II', 'III'])
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@critical_operation
def execute_trade(symbol, quantity, price):
    return {'status': 'executed', 'symbol': symbol}
```

---

## Custom Compliance Rules

### Implementing Custom Compliance Checks

```python
class CustomComplianceChecker:
    def __init__(self, agent):
        self.agent = agent
    
    def check_business_rules(self, action_data):
        """Check custom business rules"""
        # Example: Ensure trade quantity is within limits
        if action_data.get('quantity', 0) > 10000:
            return False, "Quantity exceeds maximum"
        
        # Example: Ensure price is reasonable
        if action_data.get('price', 0) <= 0:
            return False, "Price must be positive"
        
        return True, "All business rules satisfied"
    
    def check_risk_limits(self, action_data):
        """Check risk management rules"""
        # Example: Check portfolio exposure
        total_exposure = self.calculate_exposure(action_data)
        if total_exposure > 1000000:
            return False, "Exposure exceeds limit"
        
        return True, "Risk limits satisfied"
    
    def calculate_exposure(self, action_data):
        """Calculate portfolio exposure"""
        quantity = action_data.get('quantity', 0)
        price = action_data.get('price', 0)
        return quantity * price

# Usage
checker = CustomComplianceChecker(agent)

action_data = {'quantity': 100, 'price': 150.25}
is_valid, message = checker.check_business_rules(action_data)
print(f"Business rules: {message}")

is_valid, message = checker.check_risk_limits(action_data)
print(f"Risk limits: {message}")
```

### Extending Compliance Verification

```python
def verify_comprehensive_compliance(agent, action_data, custom_checker):
    """Verify both LAIRM and custom compliance"""
    
    # Check LAIRM axiom compliance
    if not agent.check_compliance(['I', 'II', 'III']):
        return False, "LAIRM axiom compliance failed"
    
    # Check business rules
    is_valid, message = custom_checker.check_business_rules(action_data)
    if not is_valid:
        return False, f"Business rule violation: {message}"
    
    # Check risk limits
    is_valid, message = custom_checker.check_risk_limits(action_data)
    if not is_valid:
        return False, f"Risk limit violation: {message}"
    
    return True, "All compliance checks passed"

# Usage
is_compliant, message = verify_comprehensive_compliance(
    agent, 
    action_data, 
    checker
)
print(f"Compliance: {message}")
```

---

## Multi-Agent Systems

### Creating Multiple Agents

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# Create multiple agents with different roles
agents = {
    'trader': LAIRMAgentSDK(
        agent_id="trader-001",
        axiomes=['I', 'II', 'III', 'IV', 'VI']
    ),
    'risk_manager': LAIRMAgentSDK(
        agent_id="risk-manager-001",
        axiomes=['I', 'II', 'III', 'IV', 'VI']
    ),
    'compliance_officer': LAIRMAgentSDK(
        agent_id="compliance-001",
        axiomes=['I', 'II', 'III', 'IV', 'VI']
    )
}

print(f"Created {len(agents)} agents")
```

### Agent Communication

```python
class AgentCommunicationBus:
    def __init__(self):
        self.messages = []
    
    def send_message(self, from_agent, to_agent, message_type, data):
        """Send message between agents"""
        message = {
            'from': from_agent.agent_id,
            'to': to_agent.agent_id,
            'type': message_type,
            'data': data,
            'timestamp': datetime.now().isoformat()
        }
        self.messages.append(message)
        
        # Log in both agents
        from_agent.log_action('message_sent', {
            'to': to_agent.agent_id,
            'type': message_type
        })
        to_agent.log_action('message_received', {
            'from': from_agent.agent_id,
            'type': message_type
        })
        
        return message
    
    def get_messages(self, agent_id):
        """Get messages for an agent"""
        return [m for m in self.messages if m['to'] == agent_id]

# Usage
bus = AgentCommunicationBus()

message = bus.send_message(
    agents['trader'],
    agents['risk_manager'],
    'trade_request',
    {'symbol': 'AAPL', 'quantity': 1000, 'price': 150.25}
)

print(f"Message sent: {message}")
```

### Coordinated Decision Making

```python
class CoordinatedDecisionMaker:
    def __init__(self, agents, bus):
        self.agents = agents
        self.bus = bus
    
    def make_coordinated_decision(self, decision_data):
        """Make decision with multiple agents"""
        
        # Step 1: Trader proposes action
        trader = self.agents['trader']
        trader.log_action('proposal', decision_data)
        
        # Step 2: Risk manager evaluates
        risk_manager = self.agents['risk_manager']
        risk_assessment = self.evaluate_risk(decision_data)
        risk_manager.log_action('risk_assessment', risk_assessment)
        
        # Step 3: Compliance officer verifies
        compliance_officer = self.agents['compliance_officer']
        compliance_check = self.verify_compliance(decision_data)
        compliance_officer.log_action('compliance_check', compliance_check)
        
        # Step 4: Make final decision
        if risk_assessment['approved'] and compliance_check['approved']:
            return {'decision': 'approved', 'reason': 'All checks passed'}
        else:
            return {'decision': 'rejected', 'reason': 'Failed compliance or risk check'}
    
    def evaluate_risk(self, data):
        """Evaluate risk"""
        return {'approved': True, 'risk_score': 0.3}
    
    def verify_compliance(self, data):
        """Verify compliance"""
        return {'approved': True, 'compliance_score': 0.95}

# Usage
coordinator = CoordinatedDecisionMaker(agents, bus)
decision = coordinator.make_coordinated_decision({
    'symbol': 'AAPL',
    'quantity': 1000,
    'price': 150.25
})
print(f"Decision: {decision}")
```

---

## Performance Optimization

### Batch Logging

```python
class BatchLogger:
    def __init__(self, agent, batch_size=100):
        self.agent = agent
        self.batch_size = batch_size
        self.batch = []
    
    def log_action_batch(self, action_type, details):
        """Log action to batch"""
        self.batch.append({
            'action_type': action_type,
            'details': details
        })
        
        if len(self.batch) >= self.batch_size:
            self.flush()
    
    def flush(self):
        """Flush batch to agent"""
        for item in self.batch:
            self.agent.log_action(item['action_type'], item['details'])
        self.batch = []

# Usage
batch_logger = BatchLogger(agent, batch_size=100)

for i in range(1000):
    batch_logger.log_action_batch('action', {'index': i})

batch_logger.flush()  # Flush remaining
```

### Caching Compliance Checks

```python
from functools import lru_cache

class CachedComplianceChecker:
    def __init__(self, agent):
        self.agent = agent
    
    @lru_cache(maxsize=1000)
    def check_compliance_cached(self, axiomes_tuple):
        """Check compliance with caching"""
        axiomes = list(axiomes_tuple)
        return self.agent.check_compliance(axiomes)
    
    def check_compliance(self, axiomes):
        """Check compliance (cached)"""
        return self.check_compliance_cached(tuple(axiomes))

# Usage
checker = CachedComplianceChecker(agent)

# First call - computed
result1 = checker.check_compliance(['I', 'II', 'III'])

# Second call - cached
result2 = checker.check_compliance(['I', 'II', 'III'])

print(f"Cache info: {checker.check_compliance_cached.cache_info()}")
```

### Async Logging

```python
import asyncio

class AsyncLogger:
    def __init__(self, agent):
        self.agent = agent
        self.queue = asyncio.Queue()
    
    async def log_action_async(self, action_type, details):
        """Log action asynchronously"""
        await self.queue.put({
            'action_type': action_type,
            'details': details
        })
    
    async def process_queue(self):
        """Process logging queue"""
        while True:
            item = await self.queue.get()
            self.agent.log_action(item['action_type'], item['details'])
            self.queue.task_done()

# Usage
async def main():
    logger = AsyncLogger(agent)
    
    # Start queue processor
    processor = asyncio.create_task(logger.process_queue())
    
    # Log actions asynchronously
    for i in range(100):
        await logger.log_action_async('action', {'index': i})
    
    await logger.queue.join()
    processor.cancel()

# asyncio.run(main())
```

---

## Security Considerations

### Secure Audit Trail Storage

```python
import hashlib
import json

class SecureAuditTrail:
    def __init__(self, agent):
        self.agent = agent
        self.chain = []
    
    def add_record(self, record):
        """Add record with cryptographic chain"""
        # Calculate hash of previous record
        if self.chain:
            previous_hash = self.chain[-1]['hash']
        else:
            previous_hash = '0' * 64
        
        # Create record with chain reference
        record['previous_hash'] = previous_hash
        record_json = json.dumps(record, sort_keys=True)
        record['hash'] = hashlib.sha256(record_json.encode()).hexdigest()
        
        self.chain.append(record)
    
    def verify_chain(self):
        """Verify chain integrity"""
        for i, record in enumerate(self.chain):
            if i > 0:
                if record['previous_hash'] != self.chain[i-1]['hash']:
                    return False
            
            # Verify record hash
            record_copy = record.copy()
            record_hash = record_copy.pop('hash')
            record_json = json.dumps(record_copy, sort_keys=True)
            calculated_hash = hashlib.sha256(record_json.encode()).hexdigest()
            
            if record_hash != calculated_hash:
                return False
        
        return True

# Usage
secure_trail = SecureAuditTrail(agent)

# Add records
for i in range(10):
    secure_trail.add_record({
        'action_type': 'action',
        'index': i,
        'timestamp': datetime.now().isoformat()
    })

# Verify integrity
is_valid = secure_trail.verify_chain()
print(f"Chain integrity: {'✅ Valid' if is_valid else '❌ Invalid'}")
```

### Access Control

```python
class AccessControlledAgent:
    def __init__(self, agent, authorized_users):
        self.agent = agent
        self.authorized_users = authorized_users
    
    def log_action_secure(self, user_id, action_type, details):
        """Log action with access control"""
        if user_id not in self.authorized_users:
            raise PermissionError(f"User {user_id} not authorized")
        
        # Log with user information
        self.agent.log_action(action_type, {
            'user_id': user_id,
            'details': details
        })
    
    def get_audit_log_secure(self, user_id):
        """Get audit log with access control"""
        if user_id not in self.authorized_users:
            raise PermissionError(f"User {user_id} not authorized")
        
        return self.agent.get_audit_log()

# Usage
secure_agent = AccessControlledAgent(
    agent,
    authorized_users=['admin', 'operator']
)

secure_agent.log_action_secure('admin', 'action', {'data': 'value'})
```

---

## Advanced Patterns

### Pattern 1: Circuit Breaker

```python
class CircuitBreaker:
    def __init__(self, agent, failure_threshold=5):
        self.agent = agent
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.is_open = False
    
    def execute(self, func, *args, **kwargs):
        """Execute function with circuit breaker"""
        if self.is_open:
            raise Exception("Circuit breaker is open")
        
        try:
            result = func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.agent.log_action('circuit_breaker_failure', {
                'failure_count': self.failure_count,
                'error': str(e)
            })
            
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
                self.agent.log_action('circuit_breaker_open', {
                    'reason': 'Failure threshold exceeded'
                })
            
            raise

# Usage
breaker = CircuitBreaker(agent, failure_threshold=3)

for i in range(5):
    try:
        breaker.execute(risky_function)
    except Exception as e:
        print(f"Error: {e}")
```

### Pattern 2: Retry with Exponential Backoff

```python
import time

class RetryWithBackoff:
    def __init__(self, agent, max_retries=3, base_delay=1):
        self.agent = agent
        self.max_retries = max_retries
        self.base_delay = base_delay
    
    def execute(self, func, *args, **kwargs):
        """Execute function with retry"""
        for attempt in range(self.max_retries):
            try:
                result = func(*args, **kwargs)
                if attempt > 0:
                    self.agent.log_action('retry_success', {
                        'attempt': attempt + 1
                    })
                return result
            except Exception as e:
                if attempt == self.max_retries - 1:
                    self.agent.log_action('retry_failed', {
                        'attempts': self.max_retries,
                        'error': str(e)
                    })
                    raise
                
                delay = self.base_delay * (2 ** attempt)
                self.agent.log_action('retry_attempt', {
                    'attempt': attempt + 1,
                    'delay': delay
                })
                time.sleep(delay)

# Usage
retry = RetryWithBackoff(agent, max_retries=3)
result = retry.execute(unreliable_function)
```

### Pattern 3: Audit Trail Analysis

```python
class AuditAnalyzer:
    def __init__(self, agent):
        self.agent = agent
    
    def get_action_statistics(self):
        """Get statistics about actions"""
        audit_log = self.agent.get_audit_log()
        
        stats = {}
        for record in audit_log:
            action_type = record['action_type']
            stats[action_type] = stats.get(action_type, 0) + 1
        
        return stats
    
    def get_timeline(self):
        """Get timeline of actions"""
        audit_log = self.agent.get_audit_log()
        
        timeline = []
        for record in audit_log:
            timeline.append({
                'timestamp': record['timestamp'],
                'action': record['action_type']
            })
        
        return timeline
    
    def find_anomalies(self):
        """Find anomalous actions"""
        audit_log = self.agent.get_audit_log()
        
        anomalies = []
        for record in audit_log:
            # Example: Flag actions with high-value trades
            if record['action_type'] == 'trade':
                if record['details'].get('quantity', 0) > 10000:
                    anomalies.append(record)
        
        return anomalies

# Usage
analyzer = AuditAnalyzer(agent)

stats = analyzer.get_action_statistics()
print(f"Action statistics: {stats}")

timeline = analyzer.get_timeline()
print(f"Timeline: {timeline}")

anomalies = analyzer.find_anomalies()
print(f"Anomalies: {anomalies}")
```

---

## Summary

You've learned advanced techniques for:
- ✅ Stacking and chaining decorators
- ✅ Implementing custom compliance rules
- ✅ Building multi-agent systems
- ✅ Optimizing performance
- ✅ Securing audit trails
- ✅ Implementing advanced patterns

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
