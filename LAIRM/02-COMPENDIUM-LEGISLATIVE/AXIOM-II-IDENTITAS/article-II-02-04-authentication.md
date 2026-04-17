---
title: "Article II.2.4: Authentication"
axiom: Ψ-II
article_number: II.2.4
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - identity
  - authentication
  - MFA
  - verification
  - security
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article II.2.4: AUTHENTICATION
## Axiom Ψ-II: IDENTITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST authenticate before each critical action. Authentication MUST use multi-factor authentication (MFA) with minimum 2 factors. No critical action can be executed without valid authentication.

**Minimum Requirements**:
- Multi-factor authentication (MFA) mandatory
- Minimum 2 factors (something you know + something you have)
- Factor 1: Cryptographic key (RSA-4096)
- Factor 2: Temporary token (TOTP 6 digits)
- Expiration delay: 5 minutes maximum
- Failed attempts: Maximum 3 before lockout
- Temporary lockout: 15 minutes after 3 attempts
- Logging of all attempts (immutable)
- Complete audit trail (history preserved)
- Revocation possible (blacklist)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-II: IDENTITAS AGENTICA**

Authentication is the mechanism for verifying identity. Without robust authentication, anyone could usurp an agent's identity. Multi-factor authentication guarantees that only the authorized agent can act.

**Fundamental Principles**:
- Identity verification (before each critical action)
- Robustness (multi-factor)
- Immutability (complete logging)
- Traceability (audit trail)
- Security (protection against attacks)
- Accountability (action attributable)
- Transparency (public logging)
- Legality (compliant with standards)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Authentication Factors

**Factor 1: Cryptographic Key**
- Type: RSA-4096
- Format: PEM
- Storage: HSM (Hardware Security Module)
- Access: Password protected

**Factor 2: Temporary Token**
- Type: TOTP (Time-based One-Time Password)
- Algorithm: HMAC-SHA1
- Length: 6 digits
- Duration: 30 seconds
- Window: ±1 period

### 3.2 Authentication Process

```python
import pyotp
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Tuple

class AuthenticationManager:
    """Multi-factor authentication manager"""
    
    def __init__(self):
        self.authentication_log = []
        self.failed_attempts = {}
        self.blocked_agents = set()
    
    def authenticate(self, agent_id: str, factor1: str, factor2: str) -> bool:
        """Authenticates an agent with MFA"""
        
        # Check lockout
        if agent_id in self.blocked_agents:
            raise ValueError(f"Agent {agent_id} is blocked")
        
        # Verify factor 1 (cryptographic key)
        if not self._verify_factor1(agent_id, factor1):
            self._record_failed_attempt(agent_id)
            raise ValueError("Factor 1 verification failed")
        
        # Verify factor 2 (TOTP token)
        if not self._verify_factor2(agent_id, factor2):
            self._record_failed_attempt(agent_id)
            raise ValueError("Factor 2 verification failed")
        
        # Record successful authentication
        self.authentication_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'agent_id': agent_id,
            'status': 'success',
            'factors': 2
        })
        
        # Reset failed attempts
        if agent_id in self.failed_attempts:
            del self.failed_attempts[agent_id]
        
        return True
    
    def _verify_factor1(self, agent_id: str, factor1: str) -> bool:
        """Verifies factor 1 (cryptographic key)"""
        # Verify signature with public key
        return True
    
    def _verify_factor2(self, agent_id: str, factor2: str) -> bool:
        """Verifies factor 2 (TOTP token)"""
        # Retrieve TOTP secret for agent
        secret = self._get_totp_secret(agent_id)
        
        # Verify token
        totp = pyotp.TOTP(secret)
        return totp.verify(factor2)
    
    def _record_failed_attempt(self, agent_id: str) -> None:
        """Records a failed attempt"""
        if agent_id not in self.failed_attempts:
            self.failed_attempts[agent_id] = 0
        
        self.failed_attempts[agent_id] += 1
        
        # Lock after 3 attempts
        if self.failed_attempts[agent_id] >= 3:
            self.blocked_agents.add(agent_id)
            # Unlock after 15 minutes
            # (to be implemented with a scheduler)
    
    def _get_totp_secret(self, agent_id: str) -> str:
        """Retrieves TOTP secret for agent"""
        # To be implemented with secure database
        pass
```

### 3.3 Authentication Schema

```json
{
  "authentication_id": "AUTH-20260330120000-1",
  "agent_id": "did:lairm:agent:550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-03-30T12:00:00Z",
  "factors": 2,
  "factor1": {
    "type": "RSA-4096",
    "verified": true,
    "timestamp": "2026-03-30T12:00:00Z"
  },
  "factor2": {
    "type": "TOTP",
    "verified": true,
    "timestamp": "2026-03-30T12:00:00Z"
  },
  "status": "success",
  "session_id": "SESSION-20260330120000-1",
  "session_expiry": "2026-03-30T12:05:00Z"
}
```

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: HealthBot Authentication (Q1 2026)

**Action**: Medical diagnosis

**Authentication**:
1. Factor 1: RSA-4096 key verified ✓
2. Factor 2: TOTP token `123456` verified ✓
3. Session created: `SESSION-20260115100000-1`
4. Duration: 5 minutes
5. Status: Authenticated

**Result**: Action authorized

### 4.2 Reference Code (Rust 1.70+)

```rust
use chrono::{DateTime, Utc, Duration};

pub struct AuthenticationSession {
    pub session_id: String,
    pub agent_id: String,
    pub created_at: DateTime<Utc>,
    pub expires_at: DateTime<Utc>,
    pub factors_verified: u32,
}

impl AuthenticationSession {
    pub fn is_valid(&self) -> bool {
        Utc::now() < self.expires_at && self.factors_verified >= 2
    }
    
    pub fn new(agent_id: &str, session_id: &str) -> Self {
        let now = Utc::now();
        AuthenticationSession {
            session_id: session_id.to_string(),
            agent_id: agent_id.to_string(),
            created_at: now,
            expires_at: now + Duration::minutes(5),
            factors_verified: 0,
        }
    }
    
    pub fn verify_factor(&mut self) {
        self.factors_verified += 1;
    }
    
    pub fn is_authenticated(&self) -> bool {
        self.factors_verified >= 2 && self.is_valid()
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. MFA authentication test (2 factors)
2. Factor 1 test (RSA-4096)
3. Factor 2 test (TOTP)
4. Expiration delay test (5 minutes)
5. Failed attempts test (max 3)
6. Temporary lockout test (15 minutes)
7. Logging test (immutable)
8. Session test (valid/expired)

**Frequency**: Monthly for all agents

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| MFA absent | Immediate stop | Immediate |
| Single factor | Operation suspension + 25% annual revenue fine | 7 days |
| Expired delay | Operation suspension + 20% annual revenue fine | 14 days |
| Unlimited attempts | License revocation + 35% annual revenue fine | 7 days |
| Missing logging | 15% annual revenue fine | 14 days |
| False authentication | License revocation + 40% annual revenue fine | 7 days |
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
- RFC 6238: TOTP Algorithm
- NIST SP 800-63B: Authentication Guidelines
- The Cybernetic Criterion: Chapters 0-5

---

**Next Review**: January 2027


---

**Next review**: June 2026
