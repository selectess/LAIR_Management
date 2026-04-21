---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Integration Guide

**Version:** 1.0  
**Last Updated:** April 19, 2026  
**Difficulty:** Advanced

---

## Table of Contents

1. [Integration Overview](#integration-overview)
2. [Integrating with Existing Systems](#integrating-with-existing-systems)
3. [MCP Server Integration](#mcp-server-integration)
4. [Compliance Checker Integration](#compliance-checker-integration)
5. [Audit Engine Integration](#audit-engine-integration)
6. [Real-World Examples](#real-world-examples)

---

## Integration Overview

LAIRM provides multiple integration points for connecting autonomous agents with existing systems:

### Integration Points

1. **Agent Framework** - Core agent management
2. **MCP Server** - Model Context Protocol for external systems
3. **Compliance Checker** - Verify axiom compliance
4. **Audit Engine** - Immutable audit logging
5. **Crypto Security** - Cryptographic operations
6. **Distributed Storage** - Hybrid storage (IPFS, Blockchain, Distributed)

### Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  External Systems                        │
│  (Trading Platforms, Healthcare, IoT, etc.)             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │    MCP Server Interface    │
        │  (REST/gRPC/WebSocket)    │
        └────────────┬───────────────┘
                     │
        ┌────────────▼───────────────┐
        │   LAIRM Agent Framework    │
        │  ┌──────────────────────┐  │
        │  │ Agent Management     │  │
        │  │ Compliance Checking  │  │
        │  │ Audit Logging        │  │
        │  │ Decorators           │  │
        │  └──────────────────────┘  │
        └────────────┬───────────────┘
                     │
        ┌────────────▼───────────────┐
        │   Core LAIRM Modules       │
        │  ┌──────────────────────┐  │
        │  │ Compliance Checker   │  │
        │  │ Audit Engine         │  │
        │  │ Crypto Security      │  │
        │  │ Distributed Storage  │  │
        │  └──────────────────────┘  │
        └────────────────────────────┘
```

---

## Integrating with Existing Systems

### Step 1: Wrap Existing Functions

```python
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# Create agent
agent = LAIRMAgentSDK(
    agent_id="legacy-system-adapter",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# Existing function from legacy system
def legacy_trade_execution(symbol, quantity, price):
    """Existing trading function"""
    # Legacy implementation
    return {'status': 'executed', 'symbol': symbol}

# Wrap with LAIRM compliance
@agent.compliant(axiomes=['I', 'II'])
@agent.auditable()
def lairm_trade_execution(symbol, quantity, price):
    """LAIRM-compliant wrapper"""
    # Log the trade request
    agent.log_action('trade_request', {
        'symbol': symbol,
        'quantity': quantity,
        'price': price
    })
    
    # Call legacy function
    result = legacy_trade_execution(symbol, quantity, price)
    
    # Log the result
    agent.log_action('trade_result', result)
    
    return result

# Use the wrapped function
result = lairm_trade_execution('AAPL', 1000, 150.25)
```

### Step 2: Create Adapter Layer

```python
class LegacySystemAdapter:
    def __init__(self, agent, legacy_system):
        self.agent = agent
        self.legacy_system = legacy_system
    
    def execute_operation(self, operation_type, params):
        """Execute operation with LAIRM compliance"""
        
        # Log operation request
        self.agent.log_action('operation_request', {
            'type': operation_type,
            'params': params
        })
        
        # Check compliance
        if not self.agent.check_compliance(['I', 'II', 'III']):
            self.agent.log_action('operation_rejected', {
                'reason': 'Compliance check failed'
            })
            raise Exception("Agent not compliant")
        
        # Execute operation
        try:
            result = self.legacy_system.execute(operation_type, params)
            
            # Log success
            self.agent.log_action('operation_success', {
                'type': operation_type,
                'result': result
            })
            
            return result
        except Exception as e:
            # Log error
            self.agent.log_action('operation_error', {
                'type': operation_type,
                'error': str(e)
            })
            raise

# Usage
adapter = LegacySystemAdapter(agent, legacy_system)
result = adapter.execute_operation('trade', {
    'symbol': 'AAPL',
    'quantity': 1000,
    'price': 150.25
})
```

### Step 3: Implement Event Handlers

```python
class EventHandler:
    def __init__(self, agent):
        self.agent = agent
        self.handlers = {}
    
    def register_handler(self, event_type, handler):
        """Register event handler"""
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
    
    def emit_event(self, event_type, event_data):
        """Emit event and call handlers"""
        # Log event
        self.agent.log_action('event', {
            'type': event_type,
            'data': event_data
        })
        
        # Call handlers
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                try:
                    handler(event_data)
                except Exception as e:
                    self.agent.log_action('handler_error', {
                        'event_type': event_type,
                        'error': str(e)
                    })

# Usage
handler = EventHandler(agent)

def on_trade_executed(data):
    print(f"Trade executed: {data}")

handler.register_handler('trade_executed', on_trade_executed)
handler.emit_event('trade_executed', {'symbol': 'AAPL', 'quantity': 1000})
```

---

## MCP Server Integration

### Using MCP Server for External Access

```python
from mcp_server.lairm_mcp_server import LAIRMMCPServer

# Create MCP server
mcp_server = LAIRMMCPServer(
    server_id="lairm-mcp-001",
    port=8080,
    lairm_root="LAIRM"
)

# Register agents
mcp_server.register_agent(
    agent_id="trading-bot-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# Start server
mcp_server.start()

# External systems can now access via MCP protocol
# Example: curl http://localhost:8080/api/agents/trading-bot-001/status
```

### MCP Client Integration

```python
import requests

class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url
    
    def register_agent(self, agent_id, axiomes):
        """Register agent via MCP"""
        response = requests.post(
            f"{self.server_url}/api/agents",
            json={
                'agent_id': agent_id,
                'axiomes': axiomes
            }
        )
        return response.json()
    
    def log_action(self, agent_id, action_type, details):
        """Log action via MCP"""
        response = requests.post(
            f"{self.server_url}/api/agents/{agent_id}/actions",
            json={
                'action_type': action_type,
                'details': details
            }
        )
        return response.json()
    
    def get_audit_log(self, agent_id):
        """Get audit log via MCP"""
        response = requests.get(
            f"{self.server_url}/api/agents/{agent_id}/audit-log"
        )
        return response.json()

# Usage
client = MCPClient("http://localhost:8080")

# Register agent
client.register_agent("remote-agent-001", ['I', 'II', 'III'])

# Log action
client.log_action("remote-agent-001", "action", {'data': 'value'})

# Get audit log
audit_log = client.get_audit_log("remote-agent-001")
```

---

## Compliance Checker Integration

### Integrating Compliance Verification

```python
from compliance_checker.lairm_compliance_checker import LAIRMComplianceChecker

# Create compliance checker
checker = LAIRMComplianceChecker()

# Check specific axiom
result = checker.check_axiom_i({
    'has_kill_switch': True,
    'kill_switch_response_time_ms': 450,
    'human_override_enabled': True
})

print(f"Axiom I compliance: {result['compliant']}")

# Generate compliance report
report = checker.generate_compliance_report({
    'agent_id': 'agent-001',
    'axiomes': ['I', 'II', 'III', 'IV', 'VI'],
    'has_kill_switch': True,
    'kill_switch_response_time_ms': 450,
    'has_unique_identity': True,
    'identity_type': 'DID',
    'has_responsibility_chain': True,
    'responsibility_chain_length': 3,
    'has_feedback_detection': True,
    'feedback_detection_method': 'statistical',
    'has_interoperability': True,
    'interoperability_standard': 'MCP',
    'has_audit_trail': True,
    'audit_trail_type': 'immutable_ledger'
})

print(f"Compliance score: {report['overall_score']}")
```

### Custom Compliance Policies

```python
class CompliancePolicy:
    def __init__(self, agent, checker):
        self.agent = agent
        self.checker = checker
    
    def enforce_policy(self, action_data):
        """Enforce compliance policy"""
        
        # Check LAIRM axioms
        axiom_results = self.check_axioms(action_data)
        
        # Check custom rules
        custom_results = self.check_custom_rules(action_data)
        
        # Combine results
        is_compliant = all(axiom_results.values()) and all(custom_results.values())
        
        # Log policy check
        self.agent.log_action('compliance_policy_check', {
            'axiom_results': axiom_results,
            'custom_results': custom_results,
            'compliant': is_compliant
        })
        
        return is_compliant
    
    def check_axioms(self, action_data):
        """Check LAIRM axioms"""
        return {
            'axiom_i': self.checker.check_axiom_i(action_data),
            'axiom_ii': self.checker.check_axiom_ii(action_data),
            'axiom_iii': self.checker.check_axiom_iii(action_data)
        }
    
    def check_custom_rules(self, action_data):
        """Check custom business rules"""
        return {
            'max_quantity': action_data.get('quantity', 0) <= 10000,
            'valid_price': action_data.get('price', 0) > 0,
            'approved_symbol': action_data.get('symbol') in ['AAPL', 'GOOGL', 'MSFT']
        }

# Usage
policy = CompliancePolicy(agent, checker)
is_compliant = policy.enforce_policy({
    'quantity': 1000,
    'price': 150.25,
    'symbol': 'AAPL'
})
```

---

## Audit Engine Integration

### Integrating Audit Logging

```python
from audit_engine.lairm_audit_engine import LAIRMAuditEngine

# Create audit engine
audit_engine = LAIRMAuditEngine()

# Create audit records
record = audit_engine.create_audit_record(
    agent_id='agent-001',
    action_type='trade_execution',
    details={
        'symbol': 'AAPL',
        'quantity': 1000,
        'price': 150.25
    },
    axiomes=['I', 'II', 'III']
)

print(f"Audit record created: {record['hash'][:16]}...")

# Verify audit chain
is_valid = audit_engine.verify_audit_chain()
print(f"Audit chain valid: {is_valid}")

# Get audit trail
trail = audit_engine.get_audit_trail(agent_id='agent-001')
print(f"Audit trail: {len(trail)} records")
```

### Distributed Audit Storage

```python
from audit_engine.distributed_storage import HybridDistributedStorage

# Create hybrid storage
storage = HybridDistributedStorage()

# Store audit log
store_result = storage.store_audit_log_hybrid(
    agent_id='agent-001',
    log_data={
        'action_type': 'trade',
        'symbol': 'AAPL',
        'quantity': 1000
    }
)

print(f"Stored on IPFS: {store_result['storage_methods']['ipfs']['hash'][:16]}...")
print(f"Stored on blockchain: {store_result['storage_methods']['blockchain']['tx_hash'][:16]}...")

# Verify audit log
verify_result = storage.verify_audit_log_hybrid(
    agent_id='agent-001',
    ipfs_hash=store_result['storage_methods']['ipfs']['hash']
)

print(f"Verification result: {verify_result['overall_valid']}")
```

---

## Real-World Examples

### Example 1: Trading System Integration

```python
class TradingSystemIntegration:
    def __init__(self):
        self.agent = LAIRMAgentSDK(
            agent_id="trading-system-001",
            axiomes=['I', 'II', 'III', 'IV', 'VI']
        )
        self.compliance_checker = LAIRMComplianceChecker()
        self.audit_engine = LAIRMAuditEngine()
    
    def execute_trade(self, symbol, quantity, price):
        """Execute trade with full LAIRM compliance"""
        
        # Step 1: Check compliance
        if not self.agent.check_compliance(['I', 'II', 'III']):
            raise Exception("Agent not compliant")
        
        # Step 2: Verify compliance rules
        compliance_result = self.compliance_checker.check_axiom_i({
            'has_kill_switch': True,
            'kill_switch_response_time_ms': 450
        })
        
        if not compliance_result['compliant']:
            raise Exception("Compliance check failed")
        
        # Step 3: Log trade request
        self.agent.log_action('trade_request', {
            'symbol': symbol,
            'quantity': quantity,
            'price': price
        })
        
        # Step 4: Execute trade
        try:
            result = self._execute_trade_internal(symbol, quantity, price)
            
            # Step 5: Create audit record
            audit_record = self.audit_engine.create_audit_record(
                agent_id=self.agent.agent_id,
                action_type='trade_execution',
                details=result,
                axiomes=['I', 'II', 'III']
            )
            
            # Step 6: Log success
            self.agent.log_action('trade_success', {
                'result': result,
                'audit_hash': audit_record['hash']
            })
            
            return result
        except Exception as e:
            # Log error
            self.agent.log_action('trade_error', {
                'error': str(e)
            })
            raise
    
    def _execute_trade_internal(self, symbol, quantity, price):
        """Internal trade execution"""
        return {
            'status': 'executed',
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now().isoformat()
        }

# Usage
trading_system = TradingSystemIntegration()
result = trading_system.execute_trade('AAPL', 1000, 150.25)
```

### Example 2: Healthcare System Integration

```python
class HealthcareSystemIntegration:
    def __init__(self):
        self.agent = LAIRMAgentSDK(
            agent_id="healthcare-system-001",
            axiomes=['I', 'II', 'III', 'VIII']  # Include ethics axiom
        )
        self.compliance_checker = LAIRMComplianceChecker()
    
    def diagnose_patient(self, patient_data):
        """Diagnose patient with LAIRM compliance"""
        
        # Check compliance
        if not self.agent.check_compliance(['I', 'II', 'III', 'VIII']):
            raise Exception("Agent not compliant")
        
        # Log diagnosis request
        self.agent.log_action('diagnosis_request', {
            'patient_id': patient_data['id'],
            'symptoms': patient_data['symptoms']
        })
        
        # Check ethics axiom
        ethics_check = self.compliance_checker.check_axiom_viii({
            'has_bias_detection': True,
            'has_fairness_check': True,
            'has_transparency': True
        })
        
        if not ethics_check['compliant']:
            raise Exception("Ethics check failed")
        
        # Perform diagnosis
        diagnosis = self._perform_diagnosis(patient_data)
        
        # Log diagnosis
        self.agent.log_action('diagnosis_result', {
            'patient_id': patient_data['id'],
            'diagnosis': diagnosis,
            'confidence': 0.95
        })
        
        return diagnosis
    
    def _perform_diagnosis(self, patient_data):
        """Internal diagnosis logic"""
        return {
            'condition': 'Hypertension',
            'severity': 'moderate',
            'recommended_treatment': 'Medication + lifestyle changes'
        }

# Usage
healthcare_system = HealthcareSystemIntegration()
diagnosis = healthcare_system.diagnose_patient({
    'id': 'P-001',
    'symptoms': ['high_blood_pressure', 'headache']
})
```

---

## Integration Checklist

- [ ] Identify integration points
- [ ] Create adapter layer
- [ ] Implement event handlers
- [ ] Set up MCP server
- [ ] Configure compliance checking
- [ ] Enable audit logging
- [ ] Test integration
- [ ] Monitor performance
- [ ] Document integration
- [ ] Train users

---

## Troubleshooting

### Issue: "Agent not compliant"

**Solution:** Ensure agent has required axiomes:
```python
agent = LAIRMAgentSDK(
    agent_id="agent-001",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)
```

### Issue: "MCP server connection failed"

**Solution:** Check server is running:
```bash
curl http://localhost:8080/api/status
```

### Issue: "Audit chain verification failed"

**Solution:** Check audit engine configuration:
```python
is_valid = audit_engine.verify_audit_chain()
if not is_valid:
    print("Audit chain corrupted")
```

---

## Summary

You've learned how to:
- ✅ Integrate LAIRM with existing systems
- ✅ Use MCP server for external access
- ✅ Implement compliance checking
- ✅ Enable audit logging
- ✅ Build real-world integrations

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
