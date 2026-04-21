---
date_creation: 2024-03-18
last_updated: 2026-04-20
last_review: 2026-04-20
---

# LAIRM Troubleshooting Guide

**Version:** 1.0  
**Last Updated:** April 19, 2026

---

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Agent Creation Issues](#agent-creation-issues)
3. [Compliance Issues](#compliance-issues)
4. [Audit Logging Issues](#audit-logging-issues)
5. [Performance Issues](#performance-issues)
6. [Integration Issues](#integration-issues)
7. [FAQ](#faq)

---

## Installation Issues

### Issue: "ModuleNotFoundError: No module named 'agent_framework'"

**Symptoms:**
```
ModuleNotFoundError: No module named 'agent_framework'
```

**Causes:**
- LAIRM not installed
- Wrong Python path
- Virtual environment not activated

**Solutions:**

1. **Install LAIRM:**
```bash
cd LAIRM/05-TOOLS
pip install -r requirements.txt
```

2. **Verify installation:**
```bash
python -c "from agent_framework.lairm_agent_sdk import LAIRMAgentSDK; print('✅ OK')"
```

3. **Check Python path:**
```bash
python -c "import sys; print(sys.path)"
```

4. **Activate virtual environment:**
```bash
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

---

### Issue: "ImportError: cannot import name 'LAIRMAgentSDK'"

**Symptoms:**
```
ImportError: cannot import name 'LAIRMAgentSDK' from 'agent_framework'
```

**Causes:**
- Incomplete installation
- Corrupted package
- Wrong import path

**Solutions:**

1. **Reinstall LAIRM:**
```bash
pip uninstall lairm-framework
pip install -r requirements.txt
```

2. **Check import path:**
```python
# ✅ Correct
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK

# ❌ Wrong
from lairm_agent_sdk import LAIRMAgentSDK
from agent_framework import LAIRMAgentSDK
```

3. **Verify package structure:**
```bash
ls -la LAIRM/05-TOOLS/agent_framework/
```

---

## Agent Creation Issues

### Issue: "TypeError: __init__() missing required positional argument 'agent_id'"

**Symptoms:**
```
TypeError: __init__() missing required positional argument 'agent_id'
```

**Causes:**
- Missing agent_id parameter
- Wrong parameter order

**Solutions:**

1. **Provide agent_id:**
```python
# ✅ Correct
agent = LAIRMAgentSDK(agent_id="my-agent")

# ❌ Wrong
agent = LAIRMAgentSDK()
```

2. **Use keyword arguments:**
```python
# ✅ Recommended
agent = LAIRMAgentSDK(
    agent_id="my-agent",
    axiomes=['I', 'II', 'III']
)

# ⚠️ Works but less clear
agent = LAIRMAgentSDK("my-agent", ['I', 'II', 'III'])
```

---

### Issue: "ValueError: axiomes must be a list"

**Symptoms:**
```
ValueError: axiomes must be a list
```

**Causes:**
- Axiomes not provided as list
- Wrong data type

**Solutions:**

1. **Use list for axiomes:**
```python
# ✅ Correct
agent = LAIRMAgentSDK(
    agent_id="my-agent",
    axiomes=['I', 'II', 'III']
)

# ❌ Wrong
agent = LAIRMAgentSDK(
    agent_id="my-agent",
    axiomes='I,II,III'
)

agent = LAIRMAgentSDK(
    agent_id="my-agent",
    axiomes=('I', 'II', 'III')
)
```

---

## Compliance Issues

### Issue: "Agent not compliant with required axiomes"

**Symptoms:**
```
ComplianceError: Agent not compliant with required axiomes
```

**Causes:**
- Agent doesn't have required axiomes
- Compliance check failed

**Solutions:**

1. **Check agent axiomes:**
```python
status = agent.get_compliance_status()
print(f"Agent axiomes: {status['axiomes']}")
```

2. **Add required axiomes:**
```python
# Create agent with required axiomes
agent = LAIRMAgentSDK(
    agent_id="compliant-agent",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)

# Verify compliance
if agent.check_compliance(['I', 'II', 'III']):
    print("✅ Agent is compliant")
```

3. **Debug compliance check:**
```python
required = ['I', 'II', 'III']
agent_axiomes = agent.get_compliance_status()['axiomes']

missing = set(required) - set(agent_axiomes)
if missing:
    print(f"Missing axiomes: {missing}")
```

---

### Issue: "Compliance check returns False unexpectedly"

**Symptoms:**
```python
agent.check_compliance(['I', 'II']) # Returns False
```

**Causes:**
- Agent axiomes don't match
- Compliance checker has issues
- Axiome format mismatch

**Solutions:**

1. **Verify axiome format:**
```python
# ✅ Correct format
axiomes = ['I', 'II', 'III']

# ❌ Wrong format
axiomes = ['Axiom I', 'Axiom II']
axiomes = ['1', '2', '3']
```

2. **Check agent axiomes:**
```python
status = agent.get_compliance_status()
print(f"Agent axiomes: {status['axiomes']}")
print(f"Checking: {['I', 'II']}")

# Verify each axiome
for axiome in ['I', 'II']:
    if axiome in status['axiomes']:
        print(f"✅ {axiome} present")
    else:
        print(f"❌ {axiome} missing")
```

---

## Audit Logging Issues

### Issue: "Audit log is empty"

**Symptoms:**
```python
audit_log = agent.get_audit_log()
print(len(audit_log))  # 0
```

**Causes:**
- No actions logged
- Audit logging disabled
- Wrong agent instance

**Solutions:**

1. **Log an action:**
```python
agent.log_action('test_action', {'data': 'value'})

# Now check
audit_log = agent.get_audit_log()
print(f"Audit log size: {len(audit_log)}")
```

2. **Verify agent instance:**
```python
# ✅ Correct - same instance
agent = LAIRMAgentSDK(agent_id="my-agent", axiomes=['I', 'II'])
agent.log_action('action', {'data': 'value'})
audit_log = agent.get_audit_log()

# ❌ Wrong - different instances
agent1 = LAIRMAgentSDK(agent_id="my-agent", axiomes=['I', 'II'])
agent1.log_action('action', {'data': 'value'})

agent2 = LAIRMAgentSDK(agent_id="my-agent", axiomes=['I', 'II'])
audit_log = agent2.get_audit_log()  # Empty!
```

---

### Issue: "Error logging action: details must be a dict"

**Symptoms:**
```
Error logging action: details must be a dict
```

**Causes:**
- Details not provided as dictionary
- Wrong data type

**Solutions:**

1. **Use dict for details:**
```python
# ✅ Correct
agent.log_action('action', {'key': 'value'})

# ❌ Wrong
agent.log_action('action', 'string')
agent.log_action('action', ['list'])
agent.log_action('action', 123)
```

2. **Handle None details:**
```python
# ✅ Correct
agent.log_action('action')  # Details defaults to {}
agent.log_action('action', {})  # Explicit empty dict

# ❌ Wrong
agent.log_action('action', None)
```

---

## Performance Issues

### Issue: "Decorator overhead is too high"

**Symptoms:**
```
Decorator overhead ratio: 7.5x
```

**Causes:**
- Too many decorators
- Compliance checking on every call
- Audit logging overhead

**Solutions:**

1. **Use batch logging:**
```python
class BatchLogger:
    def __init__(self, agent, batch_size=100):
        self.agent = agent
        self.batch = []
        self.batch_size = batch_size
    
    def log(self, action_type, details):
        self.batch.append({'action_type': action_type, 'details': details})
        if len(self.batch) >= self.batch_size:
            self.flush()
    
    def flush(self):
        for item in self.batch:
            self.agent.log_action(item['action_type'], item['details'])
        self.batch = []

# Usage
logger = BatchLogger(agent)
for i in range(10000):
    logger.log('action', {'index': i})
logger.flush()
```

2. **Cache compliance checks:**
```python
from functools import lru_cache

class CachedChecker:
    def __init__(self, agent):
        self.agent = agent
    
    @lru_cache(maxsize=1000)
    def check_compliance_cached(self, axiomes_tuple):
        return self.agent.check_compliance(list(axiomes_tuple))

checker = CachedChecker(agent)
for i in range(1000):
    checker.check_compliance_cached(('I', 'II', 'III'))
```

3. **Reduce decorator stack:**
```python
# ✅ Minimal decorators
@agent.auditable()
def function():
    pass

# ❌ Too many decorators
@agent.supervised()
@agent.responsible()
@agent.auditable()
@agent.compliant()
def function():
    pass
```

---

### Issue: "Memory usage is too high"

**Symptoms:**
```
MemoryError: Unable to allocate memory
```

**Causes:**
- Large audit logs
- Memory leaks
- Unbounded data structures

**Solutions:**

1. **Limit audit log size:**
```python
class LimitedAuditLog:
    def __init__(self, agent, max_size=10000):
        self.agent = agent
        self.max_size = max_size
    
    def get_audit_log(self):
        audit_log = self.agent.get_audit_log()
        if len(audit_log) > self.max_size:
            return audit_log[-self.max_size:]
        return audit_log

limited_log = LimitedAuditLog(agent, max_size=10000)
```

2. **Archive old logs:**
```python
import json
from datetime import datetime, timedelta

def archive_old_logs(agent, days=30):
    audit_log = agent.get_audit_log()
    cutoff = datetime.now() - timedelta(days=days)
    
    old_logs = []
    new_logs = []
    
    for record in audit_log:
        record_time = datetime.fromisoformat(record['timestamp'])
        if record_time < cutoff:
            old_logs.append(record)
        else:
            new_logs.append(record)
    
    # Archive old logs
    if old_logs:
        with open(f'archive-{datetime.now().isoformat()}.json', 'w') as f:
            json.dump(old_logs, f)
    
    return new_logs
```

---

## Integration Issues

### Issue: "MCP server connection failed"

**Symptoms:**
```
ConnectionError: Failed to connect to MCP server
```

**Causes:**
- Server not running
- Wrong URL
- Network issues

**Solutions:**

1. **Check server status:**
```bash
curl http://localhost:8080/api/status
```

2. **Start MCP server:**
```python
from mcp_server.lairm_mcp_server import LAIRMMCPServer

server = LAIRMMCPServer(port=8080)
server.start()
```

3. **Verify connection:**
```python
import requests

try:
    response = requests.get('http://localhost:8080/api/status')
    print(f"✅ Server is running: {response.json()}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

---

### Issue: "Agent not found on MCP server"

**Symptoms:**
```
Error: Agent not found
```

**Causes:**
- Agent not registered
- Wrong agent ID
- Server restart

**Solutions:**

1. **Register agent:**
```python
mcp_server.register_agent(
    agent_id="my-agent",
    axiomes=['I', 'II', 'III']
)
```

2. **Verify registration:**
```python
agents = mcp_server.list_agents()
print(f"Registered agents: {agents}")
```

---

## FAQ

### Q: How do I reset an agent's audit log?

**A:** Create a new agent instance:
```python
# Old agent with history
agent1 = LAIRMAgentSDK(agent_id="agent-001", axiomes=['I', 'II'])
agent1.log_action('action', {'data': 'value'})

# New agent with clean log
agent2 = LAIRMAgentSDK(agent_id="agent-002", axiomes=['I', 'II'])
```

---

### Q: Can I change an agent's axiomes after creation?

**A:** No, axiomes are set at creation time. Create a new agent if needed:
```python
# Create new agent with different axiomes
agent = LAIRMAgentSDK(
    agent_id="agent-with-new-axiomes",
    axiomes=['I', 'II', 'III', 'IV', 'VI']
)
```

---

### Q: How do I export audit logs?

**A:** Use the audit log retrieval:
```python
import json

audit_log = agent.get_audit_log()

# Export to JSON
with open('audit-log.json', 'w') as f:
    json.dump(audit_log, f, indent=2)

# Export to CSV
import csv

with open('audit-log.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['timestamp', 'action_type', 'details'])
    writer.writeheader()
    for record in audit_log:
        writer.writerow({
            'timestamp': record['timestamp'],
            'action_type': record['action_type'],
            'details': json.dumps(record['details'])
        })
```

---

### Q: How do I verify audit trail integrity?

**A:** Use the audit engine:
```python
from audit_engine.lairm_audit_engine import LAIRMAuditEngine

audit_engine = LAIRMAuditEngine()
is_valid = audit_engine.verify_audit_chain()
print(f"Audit chain valid: {is_valid}")
```

---

### Q: Can I use LAIRM with async code?

**A:** Yes, but be careful with audit logging:
```python
import asyncio

async def async_function():
    # Log before async operation
    agent.log_action('async_start', {})
    
    # Async operation
    await asyncio.sleep(1)
    
    # Log after async operation
    agent.log_action('async_end', {})

asyncio.run(async_function())
```

---

## Getting Help

If you can't find a solution:

1. **Check the documentation:**
   - API Reference: `docs/API-REFERENCE-*.md`
   - Tutorials: `docs/TUTORIAL-*.md`
   - Best Practices: `docs/BEST-PRACTICES.md`

2. **Review test cases:**
   - `tests/test_agent_framework_unit.py`
   - `tests/test_compliance_checker_complete.py`
   - `tests/test_integration_complete.py`

3. **Check examples:**
   - `examples/` directory

4. **Report issues:**
   - Create an issue on GitHub
   - Include error message and minimal reproduction

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
