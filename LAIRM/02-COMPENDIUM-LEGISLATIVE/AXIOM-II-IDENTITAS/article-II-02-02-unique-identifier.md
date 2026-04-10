---
title: "Article II.2.2 : Unique Identifier"
axiom: Ψ-II
article_number: II.2.2
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - identity
  - unique identifier
  - UUID
  - DID
  - immutability
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.2: UNIQUE IDENTIFIER
## Axiom Ψ-II: IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST possess a unique, immutable, and non-reusable identifier. The identifier MUST be generated with cryptographic security and MUST guarantee global uniqueness across all LAIRM systems. No two agents can ever share the same identifier.

**Minimum Requirements**:
- Globally unique identifier (absolute guarantee)
- Guaranteed immutability (no modification possible)
- Absolute non-reusability (never reassigned)
- Cryptographically secure generation (UUID v4 or DID)
- Standardized format (UUID v4 or LAIRM DID)
- Immutable creation record (blockchain)
- Collision impossibility (probability < 10^-15)
- Mandatory uniqueness verification (before deployment)
- Public registry (accessible to all)
- Complete audit trail (history preserved)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II: IDENTITAS AGENTICA**

The unique identifier is the foundation of agent identity. Without a unique identifier, traceability and accountability are impossible. Identifier immutability guarantees that each agent remains identifiable throughout its lifecycle, even after revocation or archival.

**Fundamental Principles**:
- Absolute and guaranteed uniqueness (no exceptions)
- Identifier immutability (never modified)
- Perpetual non-reusability (never reassigned)
- Complete traceability (all actions attributable)
- Attributable accountability (creator identified)
- Cryptographic verification (immutable signature)
- Public registry (complete transparency)
- Permanent audit (complete history)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Identifier Format

**UUID v4 Format**:
- Format: `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`
- Length: 36 characters
- Example: `550e8400-e29b-41d4-a716-446655440000`
- Generation: Cryptographically random (RFC 4122)
- Collision probability: < 10^-15

**DID Format (Decentralized Identifier)**:
- Format: `did:lairm:agent:{uuid}`
- Length: 50+ characters
- Example: `did:lairm:agent:550e8400-e29b-41d4-a716-446655440000`
- Resolution: Public LAIRM registry
- Immutability: Guaranteed by blockchain

### 3.2 Identifier Generation

```python
import uuid
import hashlib
from datetime import datetime
from typing import Dict, Set

class UniqueIdentifierGenerator:
    """Unique identifier generator compliant with Article II.2.2"""
    
    def __init__(self):
        self.registry: Set[str] = set()
        self.creation_log: list = []
        self.collision_attempts = 0
    
    def generate_uuid(self) -> str:
        """Generates a cryptographically secure UUID v4"""
        max_attempts = 1000
        attempts = 0
        
        while attempts < max_attempts:
            agent_uuid = str(uuid.uuid4())
            
            if agent_uuid not in self.registry:
                self.registry.add(agent_uuid)
                self.creation_log.append({
                    'timestamp': datetime.utcnow().isoformat(),
                    'identifier': agent_uuid,
                    'type': 'UUID',
                    'status': 'created',
                    'attempts': attempts
                })
                return agent_uuid
            
            attempts += 1
            self.collision_attempts += 1
        
        raise RuntimeError("Failed to generate unique UUID after 1000 attempts")
    
    def generate_did(self) -> str:
        """Generates a unique LAIRM DID"""
        agent_uuid = self.generate_uuid()
        did = f"did:lairm:agent:{agent_uuid}"
        
        self.creation_log[-1]['type'] = 'DID'
        self.creation_log[-1]['did'] = did
        
        return did
    
    def verify_uniqueness(self, identifier: str) -> bool:
        """Verifies identifier uniqueness"""
        if identifier in self.registry:
            raise ValueError(f"Identifier {identifier} already exists")
        return True
    
    def get_creation_info(self, identifier: str) -> Dict:
        """Retrieves identifier creation information"""
        for entry in self.creation_log:
            if entry['identifier'] == identifier or entry.get('did') == identifier:
                return entry
        raise ValueError(f"Identifier {identifier} not found")
    
    def get_statistics(self) -> Dict:
        """Returns generation statistics"""
        return {
            'total_generated': len(self.registry),
            'collision_attempts': self.collision_attempts,
            'collision_rate': self.collision_attempts / max(len(self.registry), 1),
            'registry_size': len(self.registry)
        }
```

### 3.3 Uniqueness Verification

```python
import re
from typing import Optional

class UniqueIdentifierVerifier:
    """Unique identifier verifier"""
    
    def __init__(self, registry: Set[str]):
        self.registry = registry
    
    def verify_uuid_format(self, uuid_str: str) -> bool:
        """Verifies UUID v4 format"""
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        if not re.match(uuid_pattern, uuid_str.lower()):
            raise ValueError(f"Invalid UUID format: {uuid_str}")
        return True
    
    def verify_did_format(self, did_str: str) -> bool:
        """Verifies LAIRM DID format"""
        did_pattern = r'^did:lairm:agent:[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        if not re.match(did_pattern, did_str.lower()):
            raise ValueError(f"Invalid DID format: {did_str}")
        return True
    
    def verify_uniqueness(self, identifier: str) -> bool:
        """Verifies identifier uniqueness"""
        if identifier in self.registry:
            raise ValueError(f"Identifier {identifier} already exists")
        return True
    
    def verify_immutability(self, identifier: str, creation_info: Dict) -> bool:
        """Verifies identifier immutability"""
        if creation_info['identifier'] != identifier:
            raise ValueError("Identifier has been modified")
        return True
    
    def verify_non_reusability(self, identifier: str) -> bool:
        """Verifies identifier non-reusability"""
        if identifier in self.registry:
            raise ValueError(f"Identifier {identifier} is already in use")
        return True
```

### 3.4 Identifier Registry

The identifier registry MUST be:
- Immutable (blockchain or equivalent)
- Distributed (replicated on minimum 3 nodes)
- Publicly accessible (REST API)
- Cryptographically verifiable (SHA-256 signature)
- Permanently auditable (complete history)
- Resilient (fault tolerant)
- Performant (< 100ms latency)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Registry Architecture

```
┌─────────────────────────────────────────────────┐
│   LAIRM Identifier Registry (Blockchain)        │
│   (Immutable, Distributed, Verifiable)          │
├─────────────────────────────────────────────────┤
│ • Immutable (SHA-256 hashing)                   │
│ • Distributed (3+ nodes)                        │
│ • Verifiable (RSA-4096 signature)               │
│ • Auditable (complete history)                  │
│ • Public (REST API)                             │
└────────────┬────────────────────────────────────┘
             │
    ┌────────┼────────┐
    │        │        │
    ▼        ▼        ▼
 [Node 1] [Node 2] [Node 3]
(Replica) (Replica) (Replica)
    │        │        │
    └────────┼────────┘
             │
             ▼
    ┌─────────────────────┐
    │  Autonomous Agent   │
    │  (Identifier)       │
    └─────────────────────┘
```

### 4.2 Reference Code (Rust 1.70+)

```rust
use std::collections::HashSet;
use std::sync::{Arc, Mutex};
use chrono::{DateTime, Utc};
use sha2::{Sha256, Digest};

pub struct IdentifierRegistry {
    identifiers: Arc<Mutex<HashSet<String>>>,
    creation_log: Arc<Mutex<Vec<IdentifierEntry>>>,
}

#[derive(Clone, Debug)]
pub struct IdentifierEntry {
    pub identifier: String,
    pub created_at: DateTime<Utc>,
    pub status: String,
    pub hash: String,
}

impl IdentifierRegistry {
    pub fn new() -> Self {
        IdentifierRegistry {
            identifiers: Arc::new(Mutex::new(HashSet::new())),
            creation_log: Arc::new(Mutex::new(Vec::new())),
        }
    }
    
    pub fn register_identifier(&self, identifier: &str) -> Result<(), String> {
        let mut ids = self.identifiers.lock().unwrap();
        
        if ids.contains(identifier) {
            return Err(format!("Identifier {} already registered", identifier));
        }
        
        ids.insert(identifier.to_string());
        
        let entry = IdentifierEntry {
            identifier: identifier.to_string(),
            created_at: Utc::now(),
            status: "active".to_string(),
            hash: Self::hash_identifier(identifier),
        };
        
        let mut log = self.creation_log.lock().unwrap();
        log.push(entry);
        
        Ok(())
    }
    
    pub fn verify_uniqueness(&self, identifier: &str) -> Result<(), String> {
        let ids = self.identifiers.lock().unwrap();
        if ids.contains(identifier) {
            return Err(format!("Identifier {} already exists", identifier));
        }
        Ok(())
    }
    
    fn hash_identifier(identifier: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(identifier.as_bytes());
        format!("{:x}", hasher.finalize())
    }
}
```

### 4.3 Use Case: TradeBot3000 Identifier (Q1 2026)

**Context**: TradeBot3000 took a $45M position without authorization. Its identifier must be unique and traceable.

**Generated Identifier**:
- UUID: `a1b2c3d4-e5f6-47g8-h9i0-j1k2l3m4n5o6`
- DID: `did:lairm:agent:a1b2c3d4-e5f6-47g8-h9i0-j1k2l3m4n5o6`
- Created: 2026-01-15T10:00:00Z
- Status: Active
- Hash: `sha256:abc123def456...`

**Verification**:
1. ✓ Valid UUID v4 format
2. ✓ Valid DID format
3. ✓ Uniqueness verified (no collision)
4. ✓ Immutability guaranteed
5. ✓ Public registry accessible

**Result**: Unique and traceable identifier established

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Unique identifier generation test (no collision)
2. Uniqueness verification test (registry)
3. UUID/DID format test (regex validation)
4. Identifier immutability test (no modification)
5. Identifier registry test (immutable, distributed)
6. Non-reusability test (never reassigned)
7. Creation logging test (blockchain)
8. Cryptographic verification test (SHA-256)

**Frequency**: Quarterly for all agents

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Non-unique identifier | License revocation + 40% CA fine | 7 days |
| Modified identifier | License revocation + 45% CA fine | 7 days |
| Identifier reuse | License revocation + 50% CA fine | 7 days |
| Invalid format | Operation suspension + 20% CA fine | 14 days |
| Non-immutable registry | Immediate stop + 60% CA fine | Immediate |
| Missing logging | 15% CA fine | 14 days |
| Collision detected | Immediate revocation | Immediate |
| Recurrence | Permanent ban | Immediate |

### 5.3 Verification Process

1. Internal audit (monthly)
2. External audit (quarterly)
3. Cryptographic audit (semi-annual)
4. Citizen audit on demand

---

## 6. EFFECTIVE DATE

**Framework Publication**: April 2026

**Implementation Status**: 
This framework is published as an open-source reference standard. The articles herein are immediately applicable for voluntary adoption by all stakeholders in the AI ecosystem, including:

- **Individual developers** (solo developers, researchers, hobbyists)
- **Organizations** (startups, enterprises, NGOs, academic institutions)
- **Infrastructure providers** (cloud platforms, API services, hosting providers)
- **End users** (individuals and organizations deploying or benefiting from AI agents)
- **Contributors** (open-source contributors, community members, standards bodies)

This framework applies to anyone who creates, deploys, uses, provides infrastructure for, or otherwise participates in the development and deployment of autonomous agents within the global digital, humanitarian, cultural, political, and economic ecosystem.

**Adoption Pathway**:
Actual enforcement and mandatory compliance depend on formal adoption by:
- National and supranational regulatory authorities
- Industry standards organizations (ISO, IEEE, W3C)
- Professional certification bodies
- Contractual and procurement requirements

**Note on Governance**:
LAIRM operates as a community-driven open-source project, accessible to all participants regardless of organizational affiliation or scale of operation. This framework provides technical specifications, legal principles, and implementation guidelines. The timeline and mechanisms for mandatory compliance will be determined by adopting jurisdictions and regulatory bodies.

For detailed discussion of decentralized governance models and international community coordination, see Chapter 18: Paradigm of Governance.

---

## REFERENCES

- Axiom Ψ-II : IDENTITAS AGENTICA
- Article II.2.1 : Agent Passport
- Article II.2.3 : Digital Signature
- RFC 4122 : UUID Standard
- The Cybernetic Criterion : Chapters 0-5

---

**Next Review** : January 2027

**Last Reviewed**: April 3, 2026
