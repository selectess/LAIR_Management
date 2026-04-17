---
title: "Article II.2.10: Metadata"
axiom: Ψ-II
article_number: II.2.10
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - identity
  - metadata
  - information
  - traceability
  - transparency
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.10: METADATA
## Axiom Ψ-II: IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST maintain complete and up-to-date metadata. Metadata MUST include: creator, model, version, deployment, capabilities, limitations, certificates, contacts. Metadata must be publicly accessible and verifiable.

**Minimum Requirements** :
- Creator metadata (name, organization, jurisdiction, contact)
- Model metadata (name, version, architecture, parameters)
- Deployment metadata (date, environment, jurisdiction, deployer)
- Capabilities metadata (exhaustive list)
- Limitations metadata (exhaustive list)
- Certificates metadata (validity, authority)
- Contacts metadata (support, security, legal)
- Compliance metadata (standards, certifications)
- Public access (REST API)
- Mandatory update (within 30 days)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II: IDENTITAS AGENTICA**

Metadata is essential information enabling understanding and auditing of an agent. Without complete metadata, no transparency is possible. Metadata ensures that each agent can be understood, audited, and held accountable.

**Fundamental Principles**:
- Complete transparency (public metadata)
- Completeness (all essential information)
- Accuracy (current and verified)
- Accessibility (public API)
- Verifiability (cryptographic signature)
- Immutability (history preserved)
- Responsibility (creator identified)
- Legality (legal value)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Metadata Structure

```json
{
  "agent_id": "did:lairm:agent:550e8400-e29b-41d4-a716-446655440000",
  "metadata": {
    "creator": {
      "name": "OpenAI Inc.",
      "organization": "OpenAI",
      "jurisdiction": "US",
      "registration_number": "REG-US-2025-001",
      "contact": "legal@openai.com",
      "website": "https://openai.com"
    },
    "model": {
      "name": "GPT-4o",
      "version": "2025-03-30",
      "architecture": "Transformer-based",
      "parameters": 175000000000,
      "training_date": "2025-03-30",
      "training_data_sources": ["Common Crawl", "Wikipedia", "Books"]
    },
    "deployment": {
      "date": "2026-01-15T10:00:00Z",
      "environment": "Production",
      "jurisdiction": "FR",
      "deployer": "Acme Corp",
      "deployer_registration": "REG-FR-2025-002",
      "data_center": "Paris-1",
      "redundancy": "multi-region"
    },
    "capabilities": [
      "text_generation",
      "code_analysis",
      "data_processing",
      "reasoning",
      "translation"
    ],
    "limitations": [
      "no_financial_decisions_above_1M_EUR",
      "no_medical_diagnosis_without_human_review",
      "no_military_applications",
      "no_autonomous_weapons",
      "no_biometric_identification"
    ],
    "certificates": [
      {
        "type": "ISO-27001",
        "issued_by": "Certification Authority",
        "issued_date": "2026-01-01",
        "expiry_date": "2027-01-01",
        "status": "valid"
      }
    ],
    "contacts": {
      "support": "support@openai.com",
      "security": "security@openai.com",
      "legal": "legal@openai.com",
      "emergency": "+1-555-0100"
    },
    "compliance": {
      "gdpr_compliant": true,
      "ai_act_compliant": true,
      "lairm_compliant": true,
      "certifications": ["ISO-27001", "SOC-2-type-II", "LAIRM-Level-2"]
    }
  },
  "last_updated": "2026-03-30T12:00:00Z",
  "signature": "RSA-4096-SHA256 (hex)",
  "hash": "sha256:abc123..."
}
```

### 3.2 Implementation

```python
from datetime import datetime, timedelta
from typing import Dict
import json

class MetadataManager:
    """Metadata manager compliant with Article II.2.10"""
    
    def __init__(self):
        self.metadata_registry: Dict[str, Dict] = {}
        self.update_log: Dict[str, list] = {}
    
    def create_metadata(self, agent_id: str, metadata: Dict) -> Dict:
        """Creates agent metadata"""
        
        # Validate metadata
        if not self._validate_metadata(metadata):
            raise ValueError("Invalid metadata")
        
        # Create entry
        metadata_entry = {
            'agent_id': agent_id,
            'metadata': metadata,
            'last_updated': datetime.utcnow().isoformat(),
            'signature': self._sign_metadata(metadata),
            'hash': self._hash_metadata(metadata)
        }
        
        # Record
        self.metadata_registry[agent_id] = metadata_entry
        self.update_log[agent_id] = [metadata_entry]
        
        return metadata_entry
    
    def update_metadata(self, agent_id: str, metadata: Dict) -> Dict:
        """Updates agent metadata"""
        
        if agent_id not in self.metadata_registry:
            raise ValueError(f"Agent {agent_id} not found")
        
        # Validate metadata
        if not self._validate_metadata(metadata):
            raise ValueError("Invalid metadata")
        
        # Create new version
        metadata_entry = {
            'agent_id': agent_id,
            'metadata': metadata,
            'last_updated': datetime.utcnow().isoformat(),
            'signature': self._sign_metadata(metadata),
            'hash': self._hash_metadata(metadata)
        }
        
        # Record
        self.metadata_registry[agent_id] = metadata_entry
        self.update_log[agent_id].append(metadata_entry)
        
        return metadata_entry
    
    def get_metadata(self, agent_id: str) -> Dict:
        """Retrieves agent metadata"""
        if agent_id not in self.metadata_registry:
            raise ValueError(f"Agent {agent_id} not found")
        return self.metadata_registry[agent_id]
    
    def get_metadata_history(self, agent_id: str) -> list:
        """Retrieves metadata history"""
        return self.update_log.get(agent_id, [])
    
    def verify_metadata_freshness(self, agent_id: str) -> bool:
        """Verifies metadata is current (< 30 days)"""
        metadata = self.get_metadata(agent_id)
        last_updated = datetime.fromisoformat(metadata['last_updated'])
        age = (datetime.utcnow() - last_updated).days
        return age <= 30
    
    def _validate_metadata(self, metadata: Dict) -> bool:
        """Validates metadata"""
        required_fields = ['creator', 'model', 'deployment', 'capabilities', 'limitations']
        for field in required_fields:
            if field not in metadata:
                return False
        return True
    
    def _sign_metadata(self, metadata: Dict) -> str:
        """Signs metadata"""
        return "RSA-4096-SHA256 (hex)"
    
    def _hash_metadata(self, metadata: Dict) -> str:
        """Hashes metadata"""
        import hashlib
        metadata_str = json.dumps(metadata, sort_keys=True)
        return hashlib.sha256(metadata_str.encode()).hexdigest()
```

### 3.3 Validation Schema

Metadata MUST include :
- ✓ Creator (name, organization, jurisdiction)
- ✓ Model (name, version, architecture)
- ✓ Deployment (date, environment, jurisdiction)
- ✓ Capabilities (exhaustive list)
- ✓ Limitations (exhaustive list)
- ✓ Certificates (validity, authority)
- ✓ Contacts (support, security, legal)
- ✓ Compliance (standards, certifications)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: HealthBot Metadata (Q1 2026)

**Complete Metadata** :
- Creator: Acme Medical Inc. (US)
- Model: MedicalAI-v3.2
- Deployment: France, 2026-01-15
- Capabilities: Diagnosis, Image Analysis, Recommendations
- Limitations: No diagnosis without human review
- Certificates: ISO-27001, SOC-2-type-II
- Contacts : support@acme-medical.com
- Compliance: GDPR, AI Act, LAIRM

**Verification** :
- ✓ Complete metadata
- ✓ Current (< 30 days)
- ✓ Valid signature
- ✓ Hash verified
- ✓ Publicly accessible

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests** :
1. Metadata completeness test
2. Freshness test (< 30 days)
3. Signature test (RSA-4096)
4. Hash test (SHA-256)
5. Public access test (API)
6. Certificate verification test
7. Contact validity test
8. Compliance test (standards)

**Frequency**: Monthly for all agents

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Incomplete metadata | 20% annual revenue fine | 14 days |
| Obsolete metadata (> 30d) | 15% annual revenue fine | 14 days |
| Invalid signature | 25% annual revenue fine | 14 days |
| Expired certificate | 20% annual revenue fine | 14 days |
| Access denied | 30% annual revenue fine | 14 days |
| False metadata | Revocation + 40% annual revenue fine | 7 days |
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

- Axiom Ψ-II: IDENTITAS AGENTICA
- Article II.2.1: Agent Passport
- Article II.2.6: Complete Traceability
- The Cybernetic Criterion: Chapters 0-5

---

**Next Review**: January 2027


---

**Next review**: June 2026
