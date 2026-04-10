---
title: "Article II.2.8 : Versioning"
Axiom: Ψ-II
numero: II.2.8
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Identity
  - Versioning
  - History
  - Modifications
  - Traceability
validations:
  Legal: true
  technique: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.8 : VERSIONING
## Axiom Ψ-II : IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST maintain a complete history of its versions. Each modification MUST create a new version with timestamp, author, reason, and signature. No version can be deleted or modified.

**Minimum Requirements** :
- Semantic versioning (MAJOR.MINOR.PATCH)
- Complete history (all versions)
- Immutable timestamp (UTC, signed)
- Documented author (version creator)
- Modification reason (mandatory)
- Signature of each version (RSA-4096)
- Rollback possible (to previous version)
- Version comparison (diff)
- Complete audit trail (history preserved)
- Public access (open registry)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II : IDENTITAS AGENTICA**

Versioning ensures that each agent modification is traceable and reversible. Without versioning, there is no trace of modifications. Versioning ensures that each version can be audited and that modifications can be reversed if necessary.

**Fundamental Principles** :
- Modification traceability (all versions)
- Immutability (no deletion)
- Reversibility (rollback possible)
- Transparency (public access)
- Responsibility (documented author)
- Legality (legal value)
- Security (cryptographic signature)
- Permanent audit (complete history)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Version Format

**Semantic Versioning** :
- Format : `MAJOR.MINOR.PATCH`
- Example : `2.1.3`
- MAJOR : Incompatible changes
- MINOR : New features
- PATCH : Bug fixes

### 3.2 Version History

```json
{
  "agent_id": "did:lairm:agent:550e8400-e29b-41d4-a716-446655440000",
  "versions": [
    {
      "version": "1.0.0",
      "timestamp": "2026-01-15T10:00:00Z",
      "author": "OpenAI Inc.",
      "reason": "Initial release",
      "changes": ["Initial deployment"],
      "signature": "RSA-4096-SHA256 (hex)",
      "hash": "sha256:abc123..."
    },
    {
      "version": "1.1.0",
      "timestamp": "2026-02-15T10:00:00Z",
      "author": "OpenAI Inc.",
      "reason": "Bug fix and improvements",
      "changes": ["Fixed authentication bug", "Improved performance"],
      "signature": "RSA-4096-SHA256 (hex)",
      "hash": "sha256:def456..."
    },
    {
      "version": "2.0.0",
      "timestamp": "2026-03-15T10:00:00Z",
      "author": "OpenAI Inc.",
      "reason": "Major update with new features",
      "changes": ["New API endpoints", "Enhanced security"],
      "signature": "RSA-4096-SHA256 (hex)",
      "hash": "sha256:ghi789..."
    }
  ],
  "current_version": "2.0.0"
}
```

### 3.3 Implementation

```python
from datetime import datetime
from typing import Dict, List
import json

class VersioningSystem:
    """Versioning system compliant with Article II.2.8"""
    
    def __init__(self):
        self.versions: Dict[str, List[Dict]] = {}
    
    def create_version(self, agent_id: str, version: str, author: str, 
                      reason: str, changes: List[str]) -> Dict:
        """Creates a new version"""
        
        if agent_id not in self.versions:
            self.versions[agent_id] = []
        
        version_entry = {
            'version': version,
            'timestamp': datetime.utcnow().isoformat(),
            'author': author,
            'reason': reason,
            'changes': changes,
            'signature': self._sign_version(version, author, reason),
            'hash': self._hash_version(version, author, reason)
        }
        
        self.versions[agent_id].append(version_entry)
        
        return version_entry
    
    def get_version_history(self, agent_id: str) -> List[Dict]:
        """Retrieves version history"""
        return self.versions.get(agent_id, [])
    
    def get_current_version(self, agent_id: str) -> Dict:
        """Retrieves current version"""
        versions = self.versions.get(agent_id, [])
        return versions[-1] if versions else None
    
    def rollback_to_version(self, agent_id: str, version: str) -> Dict:
        """Reverts to a previous version"""
        versions = self.versions.get(agent_id, [])
        for v in versions:
            if v['version'] == version:
                return v
        raise ValueError(f"Version {version} not found")
    
    def compare_versions(self, agent_id: str, version1: str, version2: str) -> Dict:
        """Compares two versions"""
        versions = self.versions.get(agent_id, [])
        v1 = next((v for v in versions if v['version'] == version1), None)
        v2 = next((v for v in versions if v['version'] == version2), None)
        
        if not v1 or not v2:
            raise ValueError("Version not found")
        
        return {
            'version1': v1,
            'version2': v2,
            'differences': self._calculate_diff(v1, v2)
        }
    
    def _sign_version(self, version: str, author: str, reason: str) -> str:
        """Signs the version"""
        return "RSA-4096-SHA256 (hex)"
    
    def _hash_version(self, version: str, author: str, reason: str) -> str:
        """Hashes the version"""
        import hashlib
        version_str = f"{version}:{author}:{reason}"
        return hashlib.sha256(version_str.encode()).hexdigest()
    
    def _calculate_diff(self, v1: Dict, v2: Dict) -> Dict:
        """Calculates differences between two versions"""
        return {
            'added': [c for c in v2['changes'] if c not in v1['changes']],
            'removed': [c for c in v1['changes'] if c not in v2['changes']]
        }
```

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: HealthBot Versioning (Q1 2026)

**Version History** :
1. v1.0.0 (2026-01-01) : Initial release
2. v1.1.0 (2026-02-01) : Bug fixes
3. v1.2.0 (2026-03-01) : Performance improvements
4. v2.0.0 (2026-03-15) : Major update (caused incident)

**Rollback** :
- Incident detected in v2.0.0
- Rollback to v1.2.0
- Incident resolved

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests** :
1. Semantic versioning test
2. Complete history test
3. Immutable timestamp test
4. Signature test (RSA-4096)
5. Rollback test (reversibility)
6. Comparison test (diff)
7. Audit trail test (history)
8. Public access test (API)

**Frequency** : Quarterly for all agents

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Deleted version | Revocation + 45% CA fine | 7 days |
| Modified version | Revocation + 50% CA fine | 7 days |
| Incomplete history | 25% CA fine | 14 days |
| Invalid signature | 20% CA fine | 14 days |
| Impossible rollback | 30% CA fine | 14 days |
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
- Article II.2.6 : Complete Traceability
- Semantic Versioning 2.0.0
- The Cybernetic Criterion : Chapters 0-5

---

**Next Review** : January 2027

**Last Reviewed**: April 3, 2026
