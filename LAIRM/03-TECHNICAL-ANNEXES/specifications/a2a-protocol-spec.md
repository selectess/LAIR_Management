---
title: "A2A Protocol Specification (Agent-to-Agent)"
type: specification
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
Axiom: V
license: CC-BY-SA-4.0
---

# A2A PROTOCOL SPECIFICATION
## Agent-to-Agent Communication Protocol for LAIRM

---

## 📋 Overview

The A2A (Agent-to-Agent) protocol is the direct communication protocol between autonomous agents in the LAIRM ecosystem. It implements **Axiom V (Interoperability)** by providing a secure, decentralized, and auditable peer-to-peer communication mechanism.

### Objectives
- ✅ Direct agent-to-agent communication
- ✅ Decentralization (no central server)
- ✅ End-to-end security
- ✅ LAIRM axiom compliance

---

## 🏗️ Architecture

### Peer-to-Peer Model

```
Agent A                          Agent B
   │                                │
   ├─ Discovery (DHT)              │
   ├─ Connection establishment     │
   ├─ Key exchange (ECDH)          │
   ├─ Compliance verification      │
   └─ Secure communication ───────→│
                                    │
                    ←─ Response ────┤
```

### Components

1. **Discovery Service** - Agent discovery
2. **Connection Manager** - Connection management
3. **Encryption Engine** - End-to-end encryption
4. **Compliance Checker** - Compliance verification
5. **Audit Logger** - Communication logging

---

## 🔍 Agent Discovery

### DHT (Distributed Hash Table)

```python
from lairm_a2a import DHT

dht = DHT()

# Register an agent
dht.register(
    agent_id="agent-001",
    endpoint="https://agent-001.example.com",
    public_key="0x...",
    axioms=["I", "II", "III", "V", "VI"]
)

# Discover an agent
agent_info = dht.lookup("agent-002")
print(f"Endpoint: {agent_info.endpoint}")
print(f"Public Key: {agent_info.public_key}")
```

### Decentralized Directory

- Based on IPFS/DHT
- Distributed replication
- No single point of failure
- Resolution in < 100ms

---

## 🔐 Connection Establishment

### A2A Handshake

```
Agent A                          Agent B
   │                                │
   ├─ HELLO (agent_id, nonce)      │
   │─────────────────────────────→ │
   │                                │
   │ ← HELLO_ACK (agent_id, nonce) │
   │                                │
   ├─ KEY_EXCHANGE (public_key)    │
   │─────────────────────────────→ │
   │                                │
   │ ← KEY_EXCHANGE_ACK (public_key)
   │                                │
   ├─ VERIFY_COMPLIANCE (axioms)   │
   │─────────────────────────────→ │
   │                                │
   │ ← VERIFY_COMPLIANCE_ACK (ok)  │
   │                                │
   └─ Connection established ──────→
```

### Implementation

```python
from lairm_a2a import A2AClient

client = A2AClient(
    agent_id="agent-001",
    private_key="0x..."
)

# Establish a connection
connection = client.connect(
    remote_agent_id="agent-002",
    axioms=["I", "II", "III", "V", "VI"]
)

if connection.is_compliant:
    print("Connection established and compliant")
else:
    print("Connection non-compliant")
```

---

## 📨 A2A Message Format

### Structure

```json
{
  "version": "1.0.0",
  "message_id": "uuid",
  "timestamp": "2026-03-30T10:00:00Z",
  "sender": {
    "agent_id": "uuid",
    "did": "did:lairm:agent:ethereum:0x..."
  },
  "receiver": {
    "agent_id": "uuid",
    "did": "did:lairm:agent:ethereum:0x..."
  },
  "type": "request|response|notification",
  "payload": {
    "action": "string",
    "params": {}
  },
  "encryption": {
    "algorithm": "AES-256-GCM",
    "iv": "hex",
    "tag": "hex"
  },
  "signature": {
    "algorithm": "ECDSA-SHA256",
    "value": "hex"
  }
}
```

---

## 🔄 Communication Patterns

### Request-Response

```python
# Agent A sends a request
response = client.request(
    remote_agent_id="agent-002",
    action="process_data",
    params={"data": "..."},
    timeout=5000
)

if response.status == "success":
    print(f"Result: {response.data}")
```

### Pub-Sub

```python
# Agent A publishes an event
client.publish(
    topic="data_updated",
    data={"timestamp": "...", "value": "..."}
)

# Agent B subscribes
@client.on_message("data_updated")
def handle_data_update(message):
    print(f"Data updated: {message.data}")
```

### Streaming

```python
# Agent A sends a stream
stream = client.stream(
    remote_agent_id="agent-002",
    action="stream_data"
)

# Agent B receives the stream
@stream.on_data
def handle_stream_data(chunk):
    print(f"Chunk received: {chunk}")
```

---

## 📊 LAIRM Compliance

### Axiom I (Suprematia)
- ✅ Human control over communications
- ✅ Integrated kill-switch
- ✅ Supervision enabled

### Axiom II (Identitas)
- ✅ Unique identification (DID)
- ✅ Mandatory digital signature
- ✅ Complete traceability

### Axiom V (INTEROPERABILITAS)
- ✅ Standardized protocol
- ✅ Guaranteed interoperability
- ✅ Decentralization

### Axiom VI (Auditum)
- ✅ Complete audit trail
- ✅ Log immutability
- ✅ Integrity verification

---

## 🚀 Implementation

### A2A Server

```python
from lairm_a2a import A2AServer

server = A2AServer(
    agent_id="agent-001",
    port=9000,
    axioms=["I", "II", "III", "V", "VI"]
)

@server.on_request("process_data")
def handle_process_data(message):
    # Verify compliance
    if not server.verify_compliance(message):
        return {"error": "Non-compliant"}
    
    # Process data
    result = process_data(message.params)
    
    return {"status": "success", "data": result}

server.start()
```

### A2A Client

```python
from lairm_a2a import A2AClient

client = A2AClient(
    agent_id="agent-002",
    axioms=["I", "II", "III", "V", "VI"]
)

# Send a request
response = client.request(
    remote_agent_id="agent-001",
    action="process_data",
    params={"data": "..."}
)

print(f"Response: {response}")
```

---

## 📈 Performance

### Latency
- Discovery: < 100ms
- Handshake: < 200ms
- Message: < 50ms
- Response: < 100ms

### Throughput
- Messages per second: 10000+
- Concurrent connections: 100000+
- Bandwidth: 1Gbps+

---

## 🔄 Versioning

### Version 1.0.0 (Current)
- ✅ Basic communication
- ✅ End-to-end encryption
- ✅ DHT discovery
- ✅ LAIRM compliance

### Version 1.1.0 (Planned)
- ⏳ Message compression
- ⏳ Multiplexing
- ⏳ Advanced streaming

---

## 📚 References

- [Axiom V - Interoperability](../../02-COMPENDIUM-LEGISLATIVE/AXIOM-V-INTEROPERABILITAS/)
- [MCP Protocol Specification](./mcp-protocol-spec.md)
- [DID Agent Specification](./did-agent-spec.md)
- [Agent Passport Schema](../schemas/agent-passport-schema.md)

**Last Reviewed**: April 3, 2026
