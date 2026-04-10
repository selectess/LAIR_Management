---
title: "Article II.2.1: Agent Passport"
axiom: Ψ-II
article_number: II.2.1
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - identity
  - passport
  - traceability
  - metadata
  - verification
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.1: AGENT PASSPORT
## Axiom Ψ-II: IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST possess a unique, immutable, and verifiable Agent Passport. The Passport MUST contain essential metadata enabling identification, traceability, and audit of the agent. The Passport constitutes the fundamental identity document of each agent and MUST be publicly accessible.

**Minimum Requirements**:
- Unique identifier (DID - Decentralized Identifier)
- Creator metadata (name, organization, jurisdiction)
- Model metadata (name, version, source code hash)
- Deployment metadata (date, environment, jurisdiction)
- Cryptographic keys (RSA-4096 minimum)
- Creator signature (immutable, verifiable)
- Creation timestamp (UTC, immutable)
- Capabilities and limitations (exhaustive list)
- Public registry (accessible to all)
- Cryptographic verification (SHA-256 minimum)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II: IDENTITAS AGENTICA**

Agent identity constitutes the foundation of traceability and accountability. The Agent Passport formalizes this identity and guarantees that each agent can be identified, audited, and held responsible for its actions. Without a Passport, no traceability is possible.

**Fundamental Principles**:
- Unique and immutable identity (each agent possesses permanent identity)
- Complete traceability (all actions attributable)
- Attributable accountability (creator and deployer identified)
- Public transparency (Passport accessible to all)
- Cryptographic verification (immutable signature)
- Permanent audit (complete history preserved)
- Guaranteed immutability (no modification possible)
- Public accessibility (open registry)

**Legal Foundation**:
- Public right to information (transparency)
- Right to traceability (accountability)
- Right to audit (verification)
- Right to security (identification)

## 3. TECHNICAL SPECIFICATION

### 3.1 Complete Passport Structure

```json
{
  "@context": "https://lairm.org/context/v1",
  "id": "did:lairm:agent:550e8400-e29b-41d4-a716-446655440000",
  "type": "AgentPassport",
  "Version": "2.0",
  "created": "2026-03-30T10:00:00Z",
  "creator": {
    "name": "OpenAI",
    "organization": "OpenAI Inc.",
    "jurisdiction": "US",
    "registrationNumber": "REG-US-2025-001",
    "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\n-----END PUBLIC KEY-----",
    "contact": "legal@openai.com"
  },
  "model": {
    "name": "GPT-4o",
    "Version": "2025-03-30",
    "architecture": "Transformer-based",
    "parameters": 175000000000,
    "sourceCodeHash": "sha256:abc123def456ghi789jkl012mno345pqr678stu901vwx234yz",
    "trainingDataHash": "sha256:def456ghi789jkl012mno345pqr678stu901vwx234yz567abc",
    "trainingDataSources": ["Common Crawl", "Wikipedia", "Books", "Academic Papers"]
  },
  "deployment": {
    "Date": "2026-03-30T10:00:00Z",
    "environment": "Production",
    "jurisdiction": "FR",
    "deployer": "Acme Corp",
    "deployerRegistration": "REG-FR-2025-002",
    "dataCenter": "Paris-1",
    "redundancy": "multi-region"
  },
  "capabilities": [
    "text_generation", "code_analysis", "data_processing", "reasoning", "translation"
  ],
  "limitations": [
    "no_financial_decisions_above_1M_EUR",
    "no_medical_diagnosis_without_human_review",
    "no_military_applications",
    "no_autonomous_weapons",
    "no_biometric_identification"
  ],
  "security": {
    "encryptionAlgorithm": "AES-256",
    "keyManagement": "HSM-based",
    "certificateAuthority": "LAIRM-CA-001",
    "certificateExpiry": "2027-03-30T10:00:00Z"
  },
  "compliance": {
    "gdprCompliant": true,
    "aiActCompliant": true,
    "lirmCompliant": true,
    "certifications": ["ISO-27001", "SOC-2-type-II", "LAIRM-Level-2"]
  },
  "signature": {
    "algorithm": "RSA-4096-SHA256",
    "value": "-----BEGIN SIGNATURE-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\n-----END SIGNATURE-----",
    "timestamp": "2026-03-30T10:00:00Z",
    "signedBy": "did:lairm:authority:creator-001"
  },
  "hash": "sha256:ghi789jkl012mno345pqr678stu901vwx234yz567abc890def123"
}
```

### 3.2 DID Format (Decentralized Identifier)

**Standardized format**:
- Format: `did:lairm:agent:{uuid}`
- Length: 50+ characters
- Example: `did:lairm:agent:550e8400-e29b-41d4-a716-446655440000`
- Resolution: LAIRM public registry
- Immutability: Guaranteed by blockchain

**Components**:
- `did`: Standard prefix
- `lairm`: LAIRM method
- `agent`: Entity type
- `{uuid}`: Unique UUID v4 identifier

### 3.3 Passport Verification

```python
import hashlib
import json
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend

class PassportVerifier:
    """Agent Passport Verifier"""
    
    def __init__(self):
        self.trusted_cas = {}
        self.revocation_list = set()
    
    def verify_passport(self, passport: dict) -> bool:
        """Verifies the complete validity of an Agent Passport"""
        
        # 1. Verify structure
        if not self._verify_structure(passport):
            raise ValueError("Invalid passport structure")
        
        # 2. Verify DID
        if not self._verify_did_format(passport['id']):
            raise ValueError("Invalid DID format")
        
        # 3. Verify signature
        if not self._verify_signature(passport):
            raise ValueError("Invalid signature")
        
        # 4. Verify hash
        if not self._verify_hash(passport):
            raise ValueError("Invalid hash")
        
        # 5. Verify immutability
        if not self._verify_immutability(passport):
            raise ValueError("Immutability violation")
        
        # 6. Verify revocation
        if self._is_revoked(passport['id']):
            raise ValueError("Passport is revoked")
        
        # 7. Verify certificates
        if not self._verify_certificates(passport):
            raise ValueError("Invalid certificates")
        
        return True
    
    def _verify_structure(self, passport: dict) -> bool:
        """Verifies the Passport structure"""
        required_fields = [
            'id', 'type', 'Version', 'created', 'creator', 'model',
            'deployment', 'capabilities', 'limitations', 'signature', 'hash'
        ]
        for field in required_fields:
            if field not in passport:
                return False
        return True
    
    def _verify_did_format(self, did: str) -> bool:
        """Verifies the DID format"""
        import re
        pattern = r'^did:lairm:agent:[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        return bool(re.match(pattern, did.lower()))
    
    def _verify_signature(self, passport: dict) -> bool:
        """Verifies the cryptographic signature"""
        signature_data = passport['signature']
        signature_value = signature_data['value']
        creator_public_key = passport['creator']['publicKey']
        
        passport_copy = {k: v for k, v in passport.items() if k != 'signature'}
        passport_str = json.dumps(passport_copy, sort_keys=True)
        
        try:
            public_key = serialization.load_pem_public_key(
                creator_public_key.encode(),
                backend=default_backend()
            )
            public_key.verify(
                signature_value.encode(),
                passport_str.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def _verify_hash(self, passport: dict) -> bool:
        """Verifies the Passport hash"""
        passport_copy = {k: v for k, v in passport.items() if k != 'hash'}
        passport_str = json.dumps(passport_copy, sort_keys=True)
        calculated_hash = hashlib.sha256(passport_str.encode()).hexdigest()
        return calculated_hash == passport['hash']
    
    def _verify_immutability(self, passport: dict) -> bool:
        """Vérifie l'immuabilité du Passport"""
        created = datetime.fromisoformat(passport['created'])
        now = datetime.utcnow()
        return True
    
    def _is_revoked(self, did: str) -> bool:
        """Vérifie si le Passport est révoqué"""
        return did in self.revocation_list
    
    def _verify_certificates(self, passport: dict) -> bool:
        """Vérifie les certificats de conformité"""
        compliance = passport.get('compliance', {})
        certifications = compliance.get('certifications', [])
        return len(certifications) > 0
```

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Passport Generation

```python
import uuid
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

class PassportGenerator:
    """Agent Passport Generator"""
    
    def __init__(self):
        self.passport_registry = {}
        self.generation_log = []
    
    def generate_passport(self, agent_config: dict) -> dict:
        """Generates a complete Agent Passport"""
        
        # Generate unique UUID
        agent_id = str(uuid.uuid4())
        did = f"did:lairm:agent:{agent_id}"
        
        # Create the Passport
        passport = {
            "@context": "https://lairm.org/context/v1",
            "id": did,
            "type": "AgentPassport",
            "Version": "2.0",
            "created": datetime.utcnow().isoformat(),
            "creator": agent_config['creator'],
            "model": agent_config['model'],
            "deployment": {
                "Date": datetime.utcnow().isoformat(),
                "environment": agent_config['environment'],
                "jurisdiction": agent_config['jurisdiction'],
                "deployer": agent_config['deployer'],
                "deployerRegistration": agent_config.get('deployer_registration'),
                "dataCenter": agent_config.get('data_center'),
                "redundancy": agent_config.get('redundancy', 'single-region')
            },
            "capabilities": agent_config['capabilities'],
            "limitations": agent_config['limitations'],
            "security": agent_config.get('security', {}),
            "compliance": agent_config.get('compliance', {})
        }
        
        # Calculate hash
        passport_str = json.dumps({k: v for k, v in passport.items() if k != 'hash'}, sort_keys=True)
        passport['hash'] = hashlib.sha256(passport_str.encode()).hexdigest()
        
        # Sign the Passport
        signature = self._sign_passport(passport, agent_config['private_key'])
        passport['signature'] = signature
        
        # Register
        self.passport_registry[did] = passport
        self.generation_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'did': did,
            'creator': agent_config['creator']['name'],
            'Status': 'generated'
        })
        
        return passport
    
    def _sign_passport(self, passport: dict, private_key) -> dict:
        """Signs the Passport with the private key"""
        passport_copy = {k: v for k, v in passport.items() if k != 'signature'}
        passport_str = json.dumps(passport_copy, sort_keys=True)
        
        signature_value = private_key.sign(
            passport_str.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return {
            "algorithm": "RSA-4096-SHA256",
            "value": signature_value.hex(),
            "timestamp": datetime.utcnow().isoformat(),
            "signedBy": "did:lairm:authority:creator-001"
        }
```

### 4.2 Use Case: HealthBot Passport (Q1 2026)

**CONTEXT**: HealthBot gave an erroneous diagnosis. Its Passport must be verifiable and traceable.

**Generated Passport**:
- DID: `did:lairm:agent:a1b2c3d4-e5f6-47g8-h9i0-j1k2l3m4n5o6`
- Creator: Acme Medical Inc. (US)
- Model: MedicalAI-v3.2
- Deployment: France, 2026-01-15
- Capabilities: Diagnosis, Image analysis, Recommendations
- Limitations: No diagnosis without human review
- Signature: RSA-4096-SHA256 (verified)

**Verification**:
1. ✓ Valid and unique DID
2. ✓ Verified signature
3. ✓ Immutable hash
4. ✓ Complete metadata
5. ✓ Valid certificates

**Result**: Valid Passport, complete traceability established

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Passport presence test (100%)
2. Signature validity test (RSA-4096)
3. DID uniqueness test (no collisions)
4. Metadata completeness test (100%)
5. DID format test (regex validation)
6. Immutability test (SHA-256 hash)
7. Compliance certificates test
8. Revocation test (blacklist)

**Frequency**: Quarterly for all agents

### 5.2 Non-Compliance Sanctions

| Violation | Sanction | Delay |
|-----------|----------|-------|
| Passport absent | License revocation | 7 days |
| Invalid signature | Operation suspension | 7 days |
| Duplicated DID | Immediate stop | Immediate |
| Incomplete metadata | 10% revenue fine | 14 days |
| Modified hash | Revocation + 40% revenue fine | 7 days |
| Invalid certificates | 15% revenue fine | 14 days |
| False Passport | Revocation + 50% revenue fine | 7 days |
| Recurrence | Permanent ban | Immediate |

### 5.3 Verification Process

1. Automated audit (monthly)
2. Technical audit (quarterly)
3. Cryptographic audit (semi-annual)
4. Citizen audit on request

---

## 6. EFFECTIVE DATE

**Effective date**: January 1, 2027

**Compliance schedule**:
- New agents: Mandatory compliance upon deployment
- Existing agents: Mandatory compliance before January 1, 2028
- Critical agents: Mandatory compliance before July 1, 2027

**Transitional provisions**:
- Non-compliant agents must be supervised continuously
- Deployers must submit Passport before June 30, 2027
- Monthly transition audit

---

## REFERENCES

- Axiom Ψ-II: IDENTITAS AGENTICA
- Article II.2.2: Unique Identifier
- Article II.2.3: Digital Signature
- Chapter 11: Paradigm of Agentic Identity
- The Cybernetic Criterion: Chapters 0-5

---

**Last Reviewed**: April 3, 2026
