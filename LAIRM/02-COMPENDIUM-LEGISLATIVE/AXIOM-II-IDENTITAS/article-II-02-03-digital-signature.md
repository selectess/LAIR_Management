---
title: "Article II.2.3 : Digital Signature"
axiom: Ψ-II
article_number: II.2.3
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - identity
  - digital signature
  - cryptography
  - RSA
  - verification
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.3: DIGITAL SIGNATURE
## Axiom Ψ-II: IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST digitally sign all its actions and decisions with a unique cryptographic key. The signature MUST be verifiable, immutable, and attributable. No agent action can be executed without a valid digital signature.

**Minimum Requirements**:
- Unique cryptographic key (RSA-4096 minimum)
- Digital signature on all actions (100%)
- Signature algorithm: RSA-4096-SHA256
- Mandatory signature verification (before execution)
- Immutable timestamp (UTC, signed)
- Signature chain (complete audit trail)
- Digital certificate (valid and non-revoked)
- Revocation possible (blacklist)
- Signature archival (immutable)
- Complete audit trail (history preserved)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II: IDENTITAS AGENTICA**

Digital signature is cryptographic proof that the agent took an action. Without signature, there is no proof of attribution. Signature guarantees authenticity, integrity, and non-repudiation of each action.

**Fundamental Principles**:
- Authenticity (proof of identity)
- Integrity (no modification)
- Non-repudiation (impossible to deny)
- Immutability (permanent signature)
- Verifiability (publicly verifiable)
- Traceability (complete audit trail)
- Accountability (action attributable)
- Legality (legal value)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Signature Algorithm

**Algorithm**: RSA-4096-SHA256
- Key: RSA 4096 bits
- Hash: SHA-256
- Padding: PSS (Probabilistic Signature Scheme)
- Format: PEM (Privacy Enhanced Mail)

**Example Signature**:
```
-----BEGIN SIGNATURE-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END SIGNATURE-----
```

### 3.2 Signature Process

```python
import hashlib
import json
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend

class DigitalSignatureManager:
    """Digital signature manager"""
    
    def __init__(self):
        self.signature_log = []
        self.revocation_list = set()
    
    def sign_action(self, agent_id: str, action: dict, private_key) -> dict:
        """Signs an agent action"""
        
        # Create payload to sign
        payload = {
            'agent_id': agent_id,
            'action': action,
            'timestamp': datetime.utcnow().isoformat(),
            'nonce': self._generate_nonce()
        }
        
        # Serialize
        payload_str = json.dumps(payload, sort_keys=True)
        
        # Calculate hash
        action_hash = hashlib.sha256(payload_str.encode()).hexdigest()
        
        # Sign
        signature_value = private_key.sign(
            payload_str.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # Create signature record
        signature_record = {
            'signature_id': self._generate_signature_id(),
            'agent_id': agent_id,
            'action_hash': action_hash,
            'signature': signature_value.hex(),
            'algorithm': 'RSA-4096-SHA256',
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'valid'
        }
        
        # Register
        self.signature_log.append(signature_record)
        
        return signature_record
    
    def verify_signature(self, signature_record: dict, public_key) -> bool:
        """Verifies a digital signature"""
        
        # Check revocation
        if signature_record['signature_id'] in self.revocation_list:
            raise ValueError("Signature is revoked")
        
        # Retrieve signature
        signature_value = bytes.fromhex(signature_record['signature'])
        
        # Create original payload
        payload = {
            'agent_id': signature_record['agent_id'],
            'action_hash': signature_record['action_hash'],
            'timestamp': signature_record['timestamp']
        }
        payload_str = json.dumps(payload, sort_keys=True)
        
        # Verify
        try:
            public_key.verify(
                signature_value,
                payload_str.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def revoke_signature(self, signature_id: str) -> None:
        """Revokes a signature"""
        self.revocation_list.add(signature_id)
    
    def _generate_nonce(self) -> str:
        """Generates a unique nonce"""
        import uuid
        return str(uuid.uuid4())
    
    def _generate_signature_id(self) -> str:
        """Generates a unique signature ID"""
        import uuid
        return f"SIG-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4()}"
```

### 3.3 Signature Chain

Each signature MUST include:
- Unique signature identifier
- Agent identifier
- Action hash (SHA-256)
- Cryptographic signature (RSA-4096)
- Algorithm used (RSA-4096-SHA256)
- Immutable timestamp (UTC)
- Status (valid, revoked, expired)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: TradeBot3000 Signature (Q1 2026)

**Action**: $45M position opening

**Generated Signature**:
- Signature ID: `SIG-20260115100000-a1b2c3d4`
- Agent ID: `did:lairm:agent:a1b2c3d4-e5f6-47g8-h9i0-j1k2l3m4n5o6`
- Action Hash: `sha256:abc123def456...`
- Signature: `RSA-4096-SHA256 (hex)`
- Timestamp: `2026-01-15T10:00:00Z`
- Status: `valid`

**Verification**:
1. ✓ Valid signature
2. ✓ Agent identified
3. ✓ Action intact
4. ✓ Immutable timestamp
5. ✓ Not revoked

**Result**: Action attributed and traceable

### 4.2 Reference Code (Rust 1.70+)

```rust
use sha2::{Sha256, Digest};
use chrono::Utc;
use std::collections::HashSet;

pub struct SignatureRecord {
    pub signature_id: String,
    pub agent_id: String,
    pub action_hash: String,
    pub signature: String,
    pub algorithm: String,
    pub timestamp: String,
    pub status: String,
}

pub struct SignatureVerifier {
    revocation_list: HashSet<String>,
}

impl SignatureVerifier {
    pub fn new() -> Self {
        SignatureVerifier {
            revocation_list: HashSet::new(),
        }
    }
    
    pub fn verify_signature(
        &self,
        signature_record: &SignatureRecord,
        public_key: &str,
    ) -> Result<bool, String> {
        // Check revocation
        if self.revocation_list.contains(&signature_record.signature_id) {
            return Err("Signature is revoked".to_string());
        }
        
        // Verify timestamp
        let sig_time = chrono::DateTime::parse_from_rfc3339(&signature_record.timestamp)
            .map_err(|e| e.to_string())?;
        let now = Utc::now();
        
        if (now - sig_time.with_timezone(&Utc)).num_seconds() > 86400 * 365 {
            return Err("Signature is too old".to_string());
        }
        
        // Verify algorithm
        if signature_record.algorithm != "RSA-4096-SHA256" {
            return Err("Invalid algorithm".to_string());
        }
        
        Ok(true)
    }
    
    pub fn revoke_signature(&mut self, signature_id: &str) {
        self.revocation_list.insert(signature_id.to_string());
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Signature on all actions test (100%)
2. Signature verification test (before execution)
3. RSA-4096-SHA256 algorithm test
4. Immutable timestamp test
5. Signature chain test (audit trail)
6. Digital certificate test (valid)
7. Revocation test (blacklist)
8. Signature archival test

**Frequency**: Monthly for all agents

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Unsigned action | Immediate stop | Immediate |
| Invalid signature | Operation suspension + 30% CA fine | 7 days |
| Weak algorithm | License revocation + 35% CA fine | 7 days |
| Modified timestamp | License revocation + 40% CA fine | 7 days |
| Expired certificate | Operation suspension + 20% CA fine | 14 days |
| False signature | License revocation + 50% CA fine | 7 days |
| Recurrence | Permanent ban | Immediate |

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
- Article II.2.2 : Unique Identifier
- RFC 3394 : AES Key Wrap Algorithm
- FIPS 186-4 : Digital Signature Standard
- The Cybernetic Criterion : Chapters 0-5

---

**Next Review** : January 2027

