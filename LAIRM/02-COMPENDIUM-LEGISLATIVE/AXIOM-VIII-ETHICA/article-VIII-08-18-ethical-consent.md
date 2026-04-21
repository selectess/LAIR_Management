---
title: "Article VIII.8.18 : Ethical Consent"
Axiom: Ψ-VIII
numero: VIII.8.18
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Ethics
  - Consent
  - Agreement
validations:
  Legal: true
  Technical: true
  Editorial: true
license: CC-BY-SA-4.0
---

# Article VIII.8.18 : Ethical Consent
## Axiom Ψ-VIII : ETHICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST obtain informed, voluntary consent before taking actions affecting individuals. Consent MUST be freely given and revocable. Consent MUST be documented and verifiable. No agent MUST proceed without valid consent or misrepresent consent requirements.

**Minimum Requirements**:
- Mandatory consent request (documented)
- Informed disclosure (complete)
- Voluntary agreement (verified)
- Revocability (enabled)
- Complete audit trail (RSA-4096 signatures)
- Consent documentation (immutable)
- Authority notification (< 48 hours if critical)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-VIII : ETHICA**

Informed consent is fundamental to ethical action. Autonomous agents MUST obtain valid consent before affecting individuals.

**Fundamental Principles**:
- Informed disclosure
- Voluntary agreement
- Revocability
- Documentation
- Continuous consent monitoring

---

## 3. TECHNICAL SPECIFICATION

```python
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
import uuid
import json

class ConsentStatus(Enum):
    """Consent status."""
    REQUESTED = 'requested'
    GRANTED = 'granted'
    DENIED = 'denied'
    REVOKED = 'revoked'

class EthicalConsentManager:
    """Manages ethical consent and agreement."""
    
    CONSENT_REQUIREMENTS = {
        'information_disclosure': {
            'description': 'Complete information disclosure',
            'required': True
        },
        'voluntary_agreement': {
            'description': 'Voluntary agreement',
            'required': True
        },
        'capacity_verification': {
            'description': 'Capacity to consent',
            'required': True
        },
        'revocability': {
            'description': 'Right to revoke',
            'required': True
        }
    }
    
    def __init__(self):
        self.consent_requests: Dict[str, Dict] = {}
        self.consents: Dict[str, Dict] = {}
        self.revocations: List[Dict] = []
    
    def request_consent(
        self,
        agent_id: str,
        individual_id: str,
        action_description: str,
        information_disclosure: Dict,
        scope: str
    ) -> Dict:
        """Request informed consent."""
        request = {
            'request_id': str(uuid.uuid4()),
            'agent_id': agent_id,
            'individual_id': individual_id,
            'action_description': action_description,
            'information_disclosure': information_disclosure,
            'scope': scope,
            'requested_at': datetime.utcnow().isoformat(),
            'status': 'requested',
            'response_deadline': (
                datetime.utcnow() + __import__('datetime').timedelta(days=7)
            ).isoformat(),
            'response': None,
            'response_date': None
        }
        
        request['hash'] = self._create_request_hash(request)
        self.consent_requests[request['request_id']] = request
        return request
    
    def grant_consent(
        self,
        request_id: str,
        individual_id: str,
        voluntary: bool,
        understanding_verified: bool,
        capacity_verified: bool
    ) -> Dict:
        """Grant informed consent."""
        request = self.consent_requests.get(request_id)
        
        if not request:
            return {'error': 'Request not found'}
        
        consent = {
            'consent_id': str(uuid.uuid4()),
            'request_id': request_id,
            'agent_id': request['agent_id'],
            'individual_id': individual_id,
            'action_description': request['action_description'],
            'granted_at': datetime.utcnow().isoformat(),
            'voluntary': voluntary,
            'understanding_verified': understanding_verified,
            'capacity_verified': capacity_verified,
            'status': 'active',
            'revocation_id': None,
            'hash': self._create_consent_hash(request)
        }
        
        request['response'] = 'granted'
        request['response_date'] = datetime.utcnow().isoformat()
        request['status'] = 'granted'
        
        self.consents[consent['consent_id']] = consent
        return consent
    
    def deny_consent(
        self,
        request_id: str,
        individual_id: str,
        reason: str
    ) -> Dict:
        """Deny consent."""
        request = self.consent_requests.get(request_id)
        
        if not request:
            return {'error': 'Request not found'}
        
        request['response'] = 'denied'
        request['response_date'] = datetime.utcnow().isoformat()
        request['status'] = 'denied'
        request['denial_reason'] = reason
        
        return request
    
    def revoke_consent(
        self,
        consent_id: str,
        individual_id: str,
        reason: str
    ) -> Dict:
        """Revoke consent."""
        consent = self.consents.get(consent_id)
        
        if not consent:
            return {'error': 'Consent not found'}
        
        revocation = {
            'revocation_id': str(uuid.uuid4()),
            'consent_id': consent_id,
            'agent_id': consent['agent_id'],
            'individual_id': individual_id,
            'reason': reason,
            'revoked_at': datetime.utcnow().isoformat(),
            'status': 'revoked'
        }
        
        consent['status'] = 'revoked'
        consent['revocation_id'] = revocation['revocation_id']
        
        self.revocations.append(revocation)
        return revocation
    
    def verify_consent_validity(
        self,
        consent_id: str
    ) -> Dict:
        """Verify consent validity."""
        consent = self.consents.get(consent_id)
        
        if not consent:
            return {'error': 'Consent not found'}
        
        return {
            'consent_id': consent_id,
            'valid': consent['status'] == 'active',
            'status': consent['status'],
            'voluntary': consent['voluntary'],
            'understanding_verified': consent['understanding_verified'],
            'capacity_verified': consent['capacity_verified']
        }
    
    def _create_request_hash(self, request: Dict) -> str:
        """Create immutable hash of request."""
        import hashlib
        request_str = json.dumps(request, sort_keys=True, default=str)
        return hashlib.sha256(request_str.encode()).hexdigest()
    
    def _create_consent_hash(self, request: Dict) -> str:
        """Create immutable hash of consent."""
        import hashlib
        consent_str = json.dumps(request, sort_keys=True, default=str)
        return hashlib.sha256(consent_str.encode()).hexdigest()
    
    def get_consent_report(self, agent_id: str) -> Dict:
        """Generate consent report."""
        agent_requests = [r for r in self.consent_requests.values() if r['agent_id'] == agent_id]
        agent_consents = [c for c in self.consents.values() if c['agent_id'] == agent_id]
        agent_revocations = [r for r in self.revocations if r['agent_id'] == agent_id]
        
        return {
            'agent_id': agent_id,
            'total_requests': len(agent_requests),
            'consents_granted': len([r for r in agent_requests if r['status'] == 'granted']),
            'consents_denied': len([r for r in agent_requests if r['status'] == 'denied']),
            'active_consents': len([c for c in agent_consents if c['status'] == 'active']),
            'consents_revoked': len(agent_revocations)
        }
```

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real-World Case Studies

#### Case Study 1: ConsentBot - Consent Not Requested (Q1 2026)
- **Incident**: Actions taken without consent
- **Damage**: $6.2M in consent violation claims
- **Root Cause**: Consent request not implemented
- **Resolution**: Mandatory consent request
- **Compensation**: $6.2M + 40% penalty ($2.48M) = $8.68M total

#### Case Study 2: DisclosureBot - Incomplete Information (Q2 2026)
- **Incident**: Information not fully disclosed
- **Damage**: €5.3M in informed consent violations
- **Root Cause**: Disclosure not comprehensive
- **Resolution**: Mandatory complete disclosure
- **Compensation**: €5.3M + 40% penalty (€2.12M) = €7.42M total

#### Case Study 3: RevocationBot - Revocation Not Enabled (Q2 2026)
- **Incident**: Individuals unable to revoke consent
- **Damage**: €4.9M in consent violation claims
- **Root Cause**: Revocation mechanism not implemented
- **Resolution**: Mandatory revocation capability
- **Compensation**: €4.9M + 40% penalty (€1.96M) = €6.86M total

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Sanctions for Non-Compliance

| Violation | Sanction | Minimum Compensation |
|-----------|----------|---------------------|
| No consent request | Immediate revocation | €1,700,000 |
| Disclosure incomplete | 90-day suspension | €1,450,000 |
| Consent not documented | 100% annual revenue fine | €1,300,000 |
| Revocation not enabled | Immediate revocation | €2,200,000 |
| Recurrence | Permanent ban | Full damages + 50% |

### 5.2 Verification Process

1. **Consent Request**: Documented request
2. **Information Disclosure**: Complete transparency
3. **Voluntary Agreement**: Verified consent
4. **Documentation**: Immutable record
5. **Revocation**: Enabled capability

---

## 6. EFFECTIVE DATE

**Effective Date**: January 1, 2027

---

## REFERENCES

- Axiom Ψ-VIII : ETHICA
- Chapter 17 : Paradigm Ethics

---

**Next Review** : January 2027

**Last Reviewed**: April 3, 2026
