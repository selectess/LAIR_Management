---
title: "DID Specification for Autonomous Agents"
type: specification
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
Axiom: II
license: CC-BY-SA-4.0
---

# DID SPECIFICATION FOR AUTONOMOUS AGENTS
## Decentralized Identifiers for LAIRM Agent Identity

---

## 📋 Overview

The DID (Decentralized Identifiers) specification for autonomous agents implements **Axiom II (Identitas)** by providing a decentralized, verifiable, and immutable identification system for each agent.

### Objectives
- ✅ Unique and verifiable identity
- ✅ Decentralization (no single point of failure)
- ✅ Immutability of identifiers
- ✅ Interoperability with W3C standards

---

## 🔑 DID Format

### Syntax

```
did:lairm:agent:<method>:<identifier>

Example:
did:lairm:agent:ethereum:0x1234567890abcdef
did:lairm:agent:solana:9B5X3...
did:lairm:agent:ipfs:QmXxxx...
```

### Components

- **Scheme**: `did` (W3C standard)
- **Method**: `lairm` (LAIRM method)
- **Type**: `agent` (entity type)
- **Blockchain**: `ethereum|solana|ipfs|...`
- **Identifier**: Unique identifier on the blockchain

---

## 📄 DID Document

### Structure

```json
{
  "@context": "https://w3id.org/did/v1",
  "id": "did:lairm:agent:ethereum:0x1234567890abcdef",
  "publicKey": [
    {
      "id": "did:lairm:agent:ethereum:0x1234567890abcdef#key-1",
      "type": "EcdsaSecp256k1VerificationKey2019",
      "controller": "did:lairm:agent:ethereum:0x1234567890abcdef",
      "publicKeyHex": "0x..."
    }
  ],
  "authentication": [
    "did:lairm:agent:ethereum:0x1234567890abcdef#key-1"
  ],
  "service": [
    {
      "id": "did:lairm:agent:ethereum:0x1234567890abcdef#endpoint",
      "type": "LAIRMAgentEndpoint",
      "serviceEndpoint": "https://agent.example.com"
    }
  ],
  "axioms": {
    "accepted": ["I", "II", "III", "V", "VI"],
    "compliance": {
      "score": 98,
      "last_verification": "2026-03-30T10:00:00Z"
    }
  },
  "created": "2026-03-30T10:00:00Z",
  "updated": "2026-03-30T10:00:00Z",
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2026-03-30T10:00:00Z",
    "verificationMethod": "did:lairm:agent:ethereum:0x1234567890abcdef#key-1",
    "signatureValue": "0x..."
  }
}
```

---

## 🔐 DID Resolution

### Resolution Process

1. **Parse** the DID
2. **Identify** the blockchain
3. **Retrieve** the DID Document
4. **Validate** the signature
5. **Return** the document

### Example

```python
from lairm_did import DIDResolver

resolver = DIDResolver()

# Resolve a DID
did = "did:lairm:agent:ethereum:0x1234567890abcdef"
doc = resolver.resolve(did)

# Verify the signature
if resolver.verify(doc):
    print("DID valid and verifiable")
else:
    print("DID invalid")
```

---

## 🔗 Blockchain Registration

### Ethereum

```solidity
contract LAIRMAgentRegistry {
    mapping(bytes32 => bytes) public didDocuments;
    
    function registerAgent(
        bytes32 agentId,
        bytes memory didDocument
    ) public {
        require(msg.sender == agentOwner[agentId]);
        didDocuments[agentId] = didDocument;
    }
    
    function getAgent(bytes32 agentId) 
        public view returns (bytes memory) 
    {
        return didDocuments[agentId];
    }
}
```

### Solana

```rust
use anchor_lang::prelude::*;

#[program]
pub mod lairm_agent_registry {
    use super::*;
    
    pub fn register_agent(
        ctx: Context<RegisterAgent>,
        agent_id: [u8; 32],
        did_document: Vec<u8>,
    ) -> Result<()> {
        let agent = &mut ctx.accounts.agent;
        agent.agent_id = agent_id;
        agent.did_document = did_document;
        Ok(())
    }
}
```

---

## 📊 LAIRM Compliance

### Axiom II (Identitas)
- ✅ Immutable unique identifier
- ✅ Mandatory digital signature
- ✅ Complete traceability
- ✅ Decentralized audit trail

### Axiom V (Interoperability)
- ✅ W3C DID standard
- ✅ Multi-blockchain interoperability
- ✅ Standardized resolution

### Axiom VI (Auditum)
- ✅ Immutable history on blockchain
- ✅ Cryptographic verification
- ✅ Decentralized audit trail

---

## 🚀 Implementation

### Create a DID

```python
from lairm_did import DIDFactory

factory = DIDFactory()

# Create a DID for an agent
did = factory.create_agent_did(
    agent_id="agent-001",
    blockchain="ethereum",
    public_key="0x...",
    axioms=["I", "II", "III", "V", "VI"]
)

print(f"DID created: {did}")
# Output: did:lairm:agent:ethereum:0x1234567890abcdef
```

### Verify a DID

```python
from lairm_did import DIDVerifier

verifier = DIDVerifier()

# Verify a DID
is_valid = verifier.verify(
    did="did:lairm:agent:ethereum:0x1234567890abcdef",
    signature="0x..."
)

if is_valid:
    print("DID valid")
else:
    print("DID invalid")
```

---

## 📈 Scalability

### Performance
- Resolution: < 100ms
- Verification: < 50ms
- Registration: < 2s (block time)

### Capacity
- Supported agents: Unlimited
- Transactions per second: 1000+
- Cost per registration: < $1

---

## 🔄 Versioning

### Version 1.0.0 (Current)
- ✅ Basic DID format
- ✅ Ethereum/Solana support
- ✅ Standardized resolution
- ✅ LAIRM compliance

### Version 1.1.0 (Planned)
- ⏳ Multi-blockchain support
- ⏳ Distributed resolution
- ⏳ Decentralized caching

---

## 📚 References

- [W3C DID Specification](https://www.w3.org/TR/did-core/)
- [Axiom II - Identitas](../../02-COMPENDIUM-LEGISLATIVE/Axiom-II-IDENTITAS/)
- [Agent Passport Schema](../schemas/agent-passport-schema.json)
- [MCP Protocol Specification](./mcp-protocol-spec.md)

---

**Date of Creation**: 2024-03-18  
**Founder**: Mehdi Wahbi

