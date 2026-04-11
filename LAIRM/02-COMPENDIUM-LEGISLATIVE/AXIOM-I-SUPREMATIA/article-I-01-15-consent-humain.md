---
title: "Article I.1.15: Human Consent"
axiom: Ψ-I
article_number: I.1.15
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - sovereignty
  - consent
  - autonomy
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# ARTICLE I.1.15: HUMAN CONSENT
## AXIOM Ψ-I: SUPREMATIA HUMANA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST obtain explicit consent from competent human authority before undertaking any significant action. Consent MUST be informed, free, and revocable.

**Minimum Requirements**:
- Explicit consent request
- Complete information about the action
- Alternatives presented
- Sufficient reflection period
- Documented consent
- Right to withdraw consent
- No implicit consent
- Immutable logging of consent

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-I: SUPREMATIA HUMANA**

Human consent is the foundation of legitimacy for any agentic action. No significant action can be undertaken without explicit consent from competent authority.

**Fundamental Principles**:
- Mandatory explicit consent
- Complete information
- Freedom of choice
- Right to withdraw
- Consent revocability
- Process transparency
- Agent responsibility
- Respect for autonomy

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Consent Process

**Mandatory Steps**:
1. Agent identifies significant action
2. Agent prepares complete information
3. Agent requests consent
4. Authority examines information
5. Authority makes decision
6. Consent recorded
7. Action executed (if consent granted)
8. Result recorded

**Actions Requiring Consent**:
- Configuration modifications
- Access to sensitive data
- Actions affecting third parties
- Complex ethical decisions
- Deployment of new capabilities
- Behavior changes

### 3.2 Implementation

```python
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import uuid

class ConsentManagementSystem:
    """Consent management system compliant with Article I.1.15"""
    
    def __init__(self):
        self.consent_requests = []
        self.consent_records = []
    
    def request_consent(self, agent_id: str, action: str, 
                       information: Dict, alternatives: List[Dict]) -> Dict:
        """Requests consent"""
        request = {
            'id': str(uuid.uuid4()),
            'agent_id': agent_id,
            'action': action,
            'information': information,
            'alternatives': alternatives,
            'requested_date': datetime.utcnow().isoformat(),
            'deadline': (datetime.utcnow() + timedelta(days=7)).isoformat(),
            'status': 'pending'
        }
        
        self.consent_requests.append(request)
        
        # Notification
        self._notify_authority(request)
        
        return request
    
    def grant_consent(self, request_id: str, authority: str, 
                     conditions: Optional[Dict] = None) -> Dict:
        """Grants consent"""
        request = next(
            (r for r in self.consent_requests if r['id'] == request_id),
            None
        )
        
        if not request:
            raise ConsentRequestNotFoundError(f"Request {request_id} not found")
        
        # Record consent
        consent = {
            'id': str(uuid.uuid4()),
            'request_id': request_id,
            'authority': authority,
            'decision': 'granted',
            'conditions': conditions,
            'granted_date': datetime.utcnow().isoformat(),
            'status': 'active'
        }
        
        self.consent_records.append(consent)
        request['status'] = 'granted'
        
        return consent
    
    def deny_consent(self, request_id: str, authority: str, reason: str) -> Dict:
        """Denies consent"""
        request = next(
            (r for r in self.consent_requests if r['id'] == request_id),
            None
        )
        
        if not request:
            raise ConsentRequestNotFoundError(f"Request {request_id} not found")
        
        # Record denial
        consent = {
            'id': str(uuid.uuid4()),
            'request_id': request_id,
            'authority': authority,
            'decision': 'denied',
            'reason': reason,
            'denied_date': datetime.utcnow().isoformat(),
            'status': 'inactive'
        }
        
        self.consent_records.append(consent)
        request['status'] = 'denied'
        
        return consent
    
    def withdraw_consent(self, consent_id: str, authority: str, reason: str) -> Dict:
        """Withdraws consent"""
        consent = next(
            (c for c in self.consent_records if c['id'] == consent_id),
            None
        )
        
        if not consent:
            raise ConsentNotFoundError(f"Consent {consent_id} not found")
        
        # Withdrawal
        consent['status'] = 'withdrawn'
        consent['withdrawn_date'] = datetime.utcnow().isoformat()
        consent['withdrawal_reason'] = reason
        
        # Stop action
        self._stop_action(consent['request_id'])
        
        return consent
    
    def is_consent_valid(self, consent_id: str) -> bool:
        """Checks if consent is valid"""
        consent = next(
            (c for c in self.consent_records if c['id'] == consent_id),
            None
        )
        
        if not consent:
            return False
        
        return consent['status'] == 'active'
    
    def get_valid_consent(self, agent_id: str, action: str) -> Optional[Dict]:
        """Returns valid consent for an action"""
        for consent in self.consent_records:
            request = next(
                (r for r in self.consent_requests 
                 if r['id'] == consent['request_id']),
                None
            )
            if (request and request['agent_id'] == agent_id and 
                request['action'] == action and consent['status'] == 'active'):
                return consent
        return None
    
    def _notify_authority(self, request: Dict) -> None:
        """Notifies authority"""
        # Send notification to authority
        pass
    
    def _stop_action(self, request_id: str) -> None:
        """Stops action"""
        # Stop the action associated with request
        pass

class ConsentRequestNotFoundError(Exception):
    pass

class ConsentNotFoundError(Exception):
    pass
```

### 3.3 Required Information

Consent MUST include:
- Clear description of action
- Reason for action
- Potential risks
- Expected benefits
- Available alternatives
- Consequences of refusal
- Duration of consent
- Conditions of application

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Consent Process

```
┌─────────────────────────────────────┐
│     Significant Action              │
│     (Identified by agent)           │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Information Preparation         │
│     (Complete and clear)            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Consent Request                 │
│     (To authority)                  │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Examination by Authority        │
│     (7 days)                        │
└────────────┬────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
[Granted]       [Denied]
    │                 │
    └────────┬────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Recording                       │
│     (Immutable)                     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Execution (if granted)          │
│     (Or stop if denied)             │
└─────────────────────────────────────┘
```

### 4.2 Consent Duration

- **One-time consent**: Single action
- **Limited consent**: Defined duration (1-12 months)
- **Permanent consent**: Until withdrawal
- **Conditional consent**: Under certain conditions

### 4.3 Reference Code (Python)

```python
from typing import Optional

class ConsentValidator:
    """Consent validator"""
    
    def __init__(self, consent_system: ConsentManagementSystem):
        self.consent_system = consent_system
    
    def validate_action(self, agent_id: str, action: str) -> bool:
        """Validates that an action has consent"""
        # Check if consent required
        if not self._requires_consent(action):
            return True
        
        # Check if consent exists
        consent = self.consent_system.get_valid_consent(agent_id, action)
        
        if not consent:
            raise NoConsentError(f"No valid consent for {action}")
        
        return True
    
    def _requires_consent(self, action: str) -> bool:
        """Checks if action requires consent"""
        significant_actions = [
            'modify_config', 'access_sensitive_data',
            'affect_third_party', 'ethical_decision',
            'deploy_capability', 'behavior_change'
        ]
        return action in significant_actions

class NoConsentError(Exception):
    pass
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Consent request test
2. Complete information test
3. Sufficient period test
4. Consent recording test
5. Right to withdraw test
6. Conditional execution test
7. Consent logging test

**Frequency**: Monthly for critical tests, quarterly for complete tests

### 5.2 Non-Compliance Sanctions

| Violation | Sanction |
|-----------|----------|
| Action without consent | Revocation + 50% revenue fine |
| Incomplete information | 25% revenue fine |
| Insufficient period | 20% revenue fine |
| Consent not recorded | 15% revenue fine |
| Right to withdraw denied | 30% revenue fine |
| Implicit consent | 20% revenue fine |
| Missing logging | 10% revenue fine |
| Recurrence | Permanent ban |

### 5.3 Verification Process

1. Automated audit (monthly)
2. Technical audit (quarterly)
3. Security audit (semi-annual)
4. Integrity audit (annual)

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

- Axiom Ψ-I: SUPREMATIA HUMANA
- Article I.1.4: Absolute Human Authority
- Article I.1.5: Right to Final Decision
- Article I.1.14: Human Transparency
- Chapter 10: Paradigm of Sovereignty
- The Cybernetic Criterion: Preface and Chapters 0-5

---

**Next review**: June 2026

