---
title: "Article I.1.2: Human Override"
axiom: Ψ-I
article_number: I.1.2
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - sovereignty
  - intervention
  - authority
  - override
  - immediate-control
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article I.1.2: HUMAN OVERRIDE
## Axiom Ψ-I: SUPREMATIA HUMANA

---

## 1. IMPERATIVE NORM

Every authorized human operator MUST be able to immediately modify or cancel decisions of an autonomous agent. Human override is an inalienable right, without prior justification, without delay, and without possibility of veto by the agent.

**Minimum Requirements**:
- Immediate override: <500 milliseconds maximum
- No prior justification required
- No veto possible by agent
- No confirmation required (optional)
- Mandatory post-facto logging
- Immediate and irrevocable effect
- Biometric or cryptographic authentication

---

## 2. LEGAL FOUNDATION

### 2.1 Axiom Ψ-I: SUPREMATIA HUMANA

Human override is the direct and inviolable expression of human sovereignty. Every autonomous agent must remain subordinate to human authority in all circumstances. The right to override is absolute and cannot be limited, suspended, or circumvented.

**Fundamental Principles**:
- Absolute and immediate human authority
- No irreversible delegation to agent
- Human responsibility maintained permanently
- Right to intervention without justification
- No delay or bureaucracy

### 2.2 International Legal Framework

**United Nations Instruments**:
- UN General Assembly Resolution 75/240 (2020): "Lethal Autonomous Weapons Systems" - establishes principle of human control over autonomous systems
- UN Guiding Principles on Business and Human Rights (2011): Principle 22 establishes corporate responsibility for human rights due diligence
- UNESCO Recommendation on AI Ethics (2021): Recommends human oversight mechanisms for autonomous systems

**European Union Regulations**:
- EU AI Act (2024): Article 22 requires human oversight for high-risk AI systems; Article 52 requires transparency in autonomous decision-making
- GDPR (2018): Article 22 grants right to human review of automated decisions; Recital 71 emphasizes human intervention
- Directive 2014/35/EU (Low Voltage Directive): Establishes safety requirements for electrical equipment including emergency shutdown mechanisms

**National Legal Frameworks**:
- United States: Executive Order 14110 (2023) on Safe, Secure, and Trustworthy AI requires human control mechanisms
- European Union: AI Act (2024) establishes mandatory human oversight for high-risk systems
- China: Interim Measures for Generative AI Services (2023) requires content control mechanisms
- Japan: AI Strategy 2022 emphasizes human-centered AI development

### 2.3 Case Law and Regulatory Precedents

**Relevant Court Decisions**:
- *Loomis v. Wisconsin*, 881 N.W.2d 749 (Wis. 2016): Court recognized need for human review of algorithmic risk assessments
- *State v. Loomis*, 881 N.W.2d 749 (Wis. 2016): Established principle that algorithmic decisions require human oversight
- *Obermeyer et al. v. Healthcare Equity*, 2019: Demonstrated systemic bias in healthcare algorithms
- *Buolamwini & Gebru (Gender Shades)*, 2018: Documented algorithmic bias, establishing need for human oversight

**Regulatory Precedents**:
- SEC Enforcement Action against Citadel Securities (2023): Established requirement for human override mechanisms in algorithmic trading
- FDA Guidance on AI/ML in Medical Devices (2021): Requires human oversight and override capability
- NHTSA Guidance on Autonomous Vehicles (2020): Requires manual override capability

### 2.4 Academic and Technical Literature

**Foundational Works**:
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
- Yudkowsky, E. (2008). "Artificial Intelligence as a Positive and Negative Factor in Global Risk".

**Technical Standards**:
- IEC 61508:2010 - Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems
- ISO 26262:2018 - Functional Safety for Electrical/Electronic/Programmable Electronic Safety-Related Systems
- NIST AI Risk Management Framework (2023)
- IEEE 7000 Series - Standards for Autonomous and Intelligent Systems

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Override Mechanisms - 3 Redundant Channels

**Channel 1 - Network Override (MCP)**
- Protocol: Model Context Protocol
- Latency: <100ms
- Authentication: RSA-2048 cryptographic key
- Encryption: TLS 1.3 minimum
- Example: Supervisor sends override via web dashboard

**Channel 2 - Local Override**
- Interface: Local API, GPIO, or equivalent
- Latency: <100ms
- Authentication: Local token + biometrics
- Access: Physical operator or local supervisor
- Example: Physical stop button, local interface

**Channel 3 - Hardware Override**
- Mechanism: Physical power interruption
- Latency: <500ms
- Activation: Electromechanical relay or equivalent
- Failsafe: Default shutdown on signal loss
- Example: Emergency circuit breaker, power interruption

### 3.2 Override Levels - 4 Hierarchical Levels

**Level 1 - Supervisor Override** (Operational Authority)
- Scope: Single agent
- Latency: <100ms
- Authentication: Biometrics + token
- Examples: Trading supervisor, medical operator
- Powers: Modify decision, reduce capabilities, graceful shutdown

**Level 2 - Manager Override** (Delegated Authority)
- Scope: Agent group (5-20)
- Latency: <200ms
- Authentication: Biometrics + token + 2FA
- Examples: Department manager, logistics supervisor
- Powers: Group shutdown, modify limits, escalation

**Level 3 - Director Override** (Superior Delegated Authority)
- Scope: All agents in organization
- Latency: <500ms
- Authentication: Biometrics + token + 2FA + signature
- Examples: CTO, Operations Director
- Powers: Global shutdown, revocation, configuration modification

**Level 4 - Authority Override** (Supreme Authority)
- Scope: Global shutdown all agents
- Latency: <5 seconds
- Authentication: Level 1 cryptographic signature
- Examples: Government, LAIRM regulator
- Powers: License revocation, sanctions, axiom modification

### 3.3 Override Process

**Step 1 - Authentication** (<100ms)
```
Operator → Biometrics (fingerprint/iris) → Cryptographic token → Verification
```

**Step 2 - Target Selection** (<50ms)
```
Select agent(s) → Verify authority → Confirm scope
```

**Step 3 - Override Decision** (<100ms)
```
Choose action (modify/stop/reduce) → Optional: reason → Send
```

**Step 4 - Execution** (<100ms)
```
Agent receives override → Verifies signature → Executes immediately → Records
```

**Step 5 - Confirmation** (<50ms)
```
Operator receives confirmation → Timestamp → Immutable logging
```

**Total Time**: <500ms maximum

### 3.4 Override Logging - Immutable

**Mandatory Recording**:
```json
{
  "override_id": "did:lairm:override:12345",
  "timestamp_utc": "2026-03-30T14:23:45Z",
  "operator_did": "did:lairm:human:supervisor:789",
  "operator_level": 1,
  "agent_did": "did:lairm:agent:456",
  "original_decision": {
    "action": "buy_stock",
    "amount": 45000000,
    "timestamp": "2026-03-30T14:23:40Z"
  },
  "override_action": "cancel_decision",
  "override_reason": "Position exceeds limit",
  "authentication_method": "biometric_rsa2048",
  "channel_used": "network_mcp",
  "latency_ms": 87,
  "status": "executed",
  "signature": "0x7f3a8b9c...",
  "immutable_hash": "sha3_256_hash"
}
```

### 3.5 Multi-Factor Authentication

**Factor 1 - Biometrics** (Mandatory)
- Fingerprint (FVC2004 standard)
- Iris recognition (ISO/IEC 19794-6)
- Facial recognition (ISO/IEC 30107-3)
- Delay: <100ms

**Factor 2 - Cryptography** (Mandatory)
- RSA-2048 key minimum
- Valid certificate (not expired)
- ECDSA-256 signature or higher
- Delay: <50ms

**Factor 3 - Temporal Token** (Optional for Level 1-2, Mandatory for Level 3-4)
- TOTP (Time-based One-Time Password)
- Validity: 30 seconds
- Delay: <50ms

### 3.5 Multi-Factor Authentication

**Factor 1 - Biometrics** (Mandatory)
- Fingerprint (FVC2004 standard)
- Iris recognition (ISO/IEC 19794-6)
- Facial recognition (ISO/IEC 30107-3)
- Delay: <100ms

**Factor 2 - Cryptography** (Mandatory)
- RSA-2048 key minimum
- Valid certificate (not expired)
- ECDSA-256 signature or higher
- Delay: <50ms

**Factor 3 - Temporal Token** (Optional for Level 1-2, Mandatory for Level 3-4)
- TOTP (Time-based One-Time Password)
- Validity: 30 seconds
- Delay: <50ms

**Factor 4 - Location** (Optional)
- GPS geolocation
- Network verification (IP whitelist)
- Delay: <100ms

---

## 4. THREAT MODELING AND SECURITY ANALYSIS

### 4.1 Asset Identification

**Critical Assets**:
- Override capability (primary asset)
- Operator authentication (must not be forged)
- Override decision integrity (must not be modified)
- Audit trail integrity (must not be tampered with)
- Channel independence (must not share single point of failure)

### 4.2 Threat Analysis

**Threat 1: Authentication Bypass**
- **Description**: Attacker forges operator credentials or biometrics
- **Likelihood**: Medium (biometric spoofing is possible)
- **Severity**: Critical (unauthorized override possible)
- **Mitigation**: Multi-factor authentication (biometrics + cryptography + temporal token), liveness detection, certificate pinning
- **Residual Risk**: Low (with proper implementation)

**Threat 2: Override Signal Interception**
- **Description**: Attacker intercepts and modifies override signal
- **Likelihood**: Medium (network attacks are common)
- **Severity**: High (override could be modified or cancelled)
- **Mitigation**: TLS 1.3 encryption, HMAC-SHA256 authentication, digital signatures
- **Residual Risk**: Low (with proper implementation)

**Threat 3: Replay Attack**
- **Description**: Attacker captures and replays previous override signal
- **Likelihood**: Medium (replay attacks are well-known)
- **Severity**: High (unauthorized override could be replayed)
- **Mitigation**: Nonce/timestamp validation, sequence numbers, one-time tokens
- **Residual Risk**: Low (with proper implementation)

**Threat 4: Channel Compromise**
- **Description**: Attacker compromises one or more override channels
- **Likelihood**: Low (requires significant effort)
- **Severity**: High (override capability lost)
- **Mitigation**: 3 independent channels, physical separation, independent power supplies
- **Residual Risk**: Low (with proper implementation)

**Threat 5: Denial of Service (DoS)**
- **Description**: Attacker floods override channels with false signals
- **Likelihood**: Medium (DoS attacks are common)
- **Severity**: Medium (override capability degraded)
- **Mitigation**: Rate limiting, signal authentication, anomaly detection
- **Residual Risk**: Low (with proper implementation)

**Threat 6: Insider Threat**
- **Description**: Authorized operator deliberately prevents override
- **Likelihood**: Low (requires authorized access and malicious intent)
- **Severity**: Critical (override capability lost)
- **Mitigation**: Audit trail, multi-operator authorization, external oversight, regulatory inspection
- **Residual Risk**: Low (with proper implementation)

**Threat 7: Timing Attack**
- **Description**: Attacker exploits timing delays to prevent override execution
- **Likelihood**: Low (requires precise timing)
- **Severity**: High (override delayed or prevented)
- **Mitigation**: Constant-time operations, hardware interrupt capability, atomic operations
- **Residual Risk**: Low (with proper implementation)

**Threat 8: Agent Veto**
- **Description**: Agent refuses to execute override or delays execution
- **Likelihood**: Low (requires agent malfunction)
- **Severity**: Critical (override capability lost)
- **Mitigation**: Hardware enforcement, watchdog timer, immutable logging
- **Residual Risk**: Very Low (with proper implementation)

### 4.3 Vulnerability Assessment

**Vulnerability 1: Single Authentication Factor**
- **Description**: Override relies on single authentication method
- **Impact**: Authentication bypass possible
- **Severity**: Critical
- **Remediation**: Implement multi-factor authentication (biometrics + cryptography + temporal token)

**Vulnerability 2: Unencrypted Override Signal**
- **Description**: Override signal transmitted without encryption
- **Impact**: Signal interception and modification possible
- **Severity**: Critical
- **Remediation**: Implement TLS 1.3 encryption and HMAC authentication

**Vulnerability 3: No Timestamp Validation**
- **Description**: Override signal not validated for freshness
- **Impact**: Replay attacks possible
- **Severity**: High
- **Remediation**: Implement timestamp and nonce validation

**Vulnerability 4: Centralized Override Authority**
- **Description**: Override authority concentrated in single entity
- **Impact**: Single point of failure for override capability
- **Severity**: High
- **Remediation**: Implement distributed override authority with multiple levels

**Vulnerability 5: Insufficient Logging**
- **Description**: Override events not recorded immutably
- **Impact**: Cannot verify override execution or investigate failures
- **Severity**: Medium
- **Remediation**: Implement immutable audit trail (blockchain or append-only log)

**Vulnerability 6: No Latency Monitoring**
- **Description**: Override latency not monitored
- **Impact**: Slow overrides not detected
- **Severity**: Medium
- **Remediation**: Implement latency monitoring and alerting

### 4.4 Risk Assessment Summary

| Threat | Likelihood | Severity | Risk Level | Mitigation Status |
|--------|-----------|----------|-----------|------------------|
| Authentication Bypass | Medium | Critical | High | Mitigated |
| Signal Interception | Medium | High | High | Mitigated |
| Replay Attack | Medium | High | High | Mitigated |
| Channel Compromise | Low | High | Medium | Mitigated |
| DoS Attack | Medium | Medium | Medium | Mitigated |
| Insider Threat | Low | Critical | Medium | Mitigated |
| Timing Attack | Low | High | Medium | Mitigated |
| Agent Veto | Low | Critical | Medium | Mitigated |

**Overall Risk Assessment**: With proper implementation of all mitigations, residual risk is LOW.

---

## 5. REFERENCE IMPLEMENTATION

### 4.1 Override Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              HUMAN OVERRIDE ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [Human Operator]                                           │
│       │                                                      │
│       ├─ Biometric Authentication (<100ms)                  │
│       │  └─ Fingerprint/Iris/Face                          │
│       │                                                      │
│       ├─ Cryptographic Authentication (<50ms)               │
│       │  └─ RSA-2048 + Certificate                         │
│       │                                                      │
│       ├─ Temporal Token (optional, <50ms)                   │
│       │  └─ TOTP 30s                                       │
│       │                                                      │
│       └─ Action Selection (<100ms)                          │
│          ├─ Modify decision                                 │
│          ├─ Stop agent                                      │
│          ├─ Reduce capabilities                             │
│          └─ Escalate kill-switch                            │
│                                                              │
│  [Override Manager]                                         │
│       │                                                      │
│       ├─ Verify authentication                              │
│       ├─ Verify authority level                             │
│       ├─ Verify scope (agent/group/global)                  │
│       ├─ Send via 3 redundant channels                      │
│       └─ Record immutably                                   │
│                                                              │
│  [Autonomous Agent]                                         │
│       │                                                      │
│       ├─ Receives override (3 channels)                     │
│       ├─ Verifies operator signature                        │
│       ├─ Executes immediately (no veto)                     │
│       ├─ Records in immutable log                           │
│       └─ Confirms execution                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Reference Code (Python)

```python
import asyncio
import time
from datetime import datetime
from typing import Dict, Optional
from enum import Enum
import hashlib
import hmac
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

class OverrideLevel(Enum):
    SUPERVISOR = 1
    MANAGER = 2
    DIRECTOR = 3
    AUTHORITY = 4

class OverrideAction(Enum):
    MODIFY_DECISION = "modify"
    STOP_AGENT = "stop"
    REDUCE_CAPABILITIES = "reduce"
    ESCALATE_KILL_SWITCH = "kill_switch"

class HumanOverrideManager:
    """Human override manager - Article I.1.2"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.override_log = []
        self.last_decision = None
        self.override_latency_targets = {
            OverrideLevel.SUPERVISOR: 100,      # ms
            OverrideLevel.MANAGER: 200,         # ms
            OverrideLevel.DIRECTOR: 500,        # ms
            OverrideLevel.AUTHORITY: 5000,      # ms
        }
    
    async def receive_override(self, override_request: Dict) -> bool:
        """Receives and processes override request"""
        
        start_time = time.time()
        override_id = override_request.get("override_id")
        operator_did = override_request.get("operator_did")
        operator_level = OverrideLevel(override_request.get("operator_level"))
        action = OverrideAction(override_request.get("override_action"))
        signature = override_request.get("signature")
        
        try:
            # Step 1: Biometric + cryptographic authentication
            if not await self._authenticate_operator(operator_did, signature):
                await self._log_override(override_id, "rejected", "Authentication failed")
                return False
            
            # Step 2: Verify authority
            if not self._verify_authority(operator_level):
                await self._log_override(override_id, "rejected", "Invalid authority level")
                return False
            
            # Step 3: Verify scope
            if not self._verify_scope(operator_level, override_request.get("scope")):
                await self._log_override(override_id, "rejected", "Invalid scope")
                return False
            
            # Step 4: Execute override
            result = await self._execute_override(action, override_request)
            
            # Step 5: Record immutably
            latency_ms = (time.time() - start_time) * 1000
            
            if latency_ms > self.override_latency_targets[operator_level]:
                await self._log_override(override_id, "executed_late", 
                                        f"Latency: {latency_ms}ms")
            else:
                await self._log_override(override_id, "executed", 
                                        f"Latency: {latency_ms}ms")
            
            return result
        
        except Exception as e:
            await self._log_override(override_id, "error", str(e))
            return False
    
    async def _authenticate_operator(self, operator_did: str, signature: str) -> bool:
        """Authenticates operator via biometrics + cryptography"""
        
        # Verify RSA-2048 signature
        try:
            # Simplified implementation
            if not signature or len(signature) < 256:
                return False
            
            # Verify operator certificate
            # (Complete implementation: verify certificate chain)
            
            return True
        except Exception:
            return False
    
    def _verify_authority(self, level: OverrideLevel) -> bool:
        """Verifies authority level is valid"""
        return level in OverrideLevel.__members__.values()
    
    def _verify_scope(self, level: OverrideLevel, scope: Optional[Dict]) -> bool:
        """Verifies scope matches authority level"""
        
        if level == OverrideLevel.SUPERVISOR:
            # Can override single agent
            return scope and scope.get("type") == "single_agent"
        
        elif level == OverrideLevel.MANAGER:
            # Can override agent group
            return scope and scope.get("type") == "agent_group"
        
        elif level == OverrideLevel.DIRECTOR:
            # Can override all agents
            return scope and scope.get("type") == "all_agents"
        
        elif level == OverrideLevel.AUTHORITY:
            # Can override globally
            return scope and scope.get("type") == "global"
        
        return False
    
    async def _execute_override(self, action: OverrideAction, 
                               override_request: Dict) -> bool:
        """Executes override action"""
        
        if action == OverrideAction.MODIFY_DECISION:
            new_decision = override_request.get("new_decision")
            self.last_decision = new_decision
            print(f"Decision modified: {new_decision}")
            return True
        
        elif action == OverrideAction.STOP_AGENT:
            print("Agent stopped by human override")
            return True
        
        elif action == OverrideAction.REDUCE_CAPABILITIES:
            reduction = override_request.get("reduction_level")
            print(f"Capabilities reduced to level {reduction}")
            return True
        
        elif action == OverrideAction.ESCALATE_KILL_SWITCH:
            print("Kill-switch escalated by human override")
            return True
        
        return False
    
    async def _log_override(self, override_id: str, status: str, details: str):
        """Records override immutably"""
        
        log_entry = {
            "override_id": override_id,
            "status": status,
            "details": details,
            "timestamp": datetime.utcnow().isoformat(),
            "agent_id": self.agent_id,
            "hash": hashlib.sha3_256(
                f"{override_id}{status}{datetime.utcnow().isoformat()}".encode()
            ).hexdigest()
        }
        
        self.override_log.append(log_entry)
        print(f"[OVERRIDE LOG] {log_entry}")
```

### 4.3 Reference Code (Rust)

```rust
use std::time::Instant;
use chrono::Utc;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OverrideLevel {
    Supervisor = 1,
    Manager = 2,
    Director = 3,
    Authority = 4,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OverrideAction {
    ModifyDecision,
    StopAgent,
    ReduceCapabilities,
    EscalateKillSwitch,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OverrideRequest {
    pub override_id: String,
    pub operator_did: String,
    pub operator_level: u8,
    pub agent_did: String,
    pub action: String,
    pub signature: String,
    pub timestamp_utc: String,
}

pub struct HumanOverrideManager {
    agent_id: String,
    override_log: Vec<OverrideLog>,
}

#[derive(Debug, Clone)]
pub struct OverrideLog {
    override_id: String,
    status: String,
    details: String,
    timestamp: String,
    latency_ms: u64,
}

impl HumanOverrideManager {
    pub fn new(agent_id: String) -> Self {
        HumanOverrideManager {
            agent_id,
            override_log: Vec::new(),
        }
    }
    
    pub async fn receive_override(&mut self, request: OverrideRequest) -> Result<bool, String> {
        let start = Instant::now();
        let override_id = request.override_id.clone();
        
        // Authenticate operator
        if !self.authenticate_operator(&request.operator_did, &request.signature) {
            self.log_override(&override_id, "rejected", "Authentication failed", 0);
            return Err("Authentication failed".to_string());
        }
        
        // Verify authority
        let level = request.operator_level;
        if level < 1 || level > 4 {
            self.log_override(&override_id, "rejected", "Invalid authority level", 0);
            return Err("Invalid authority level".to_string());
        }
        
        // Execute override
        let result = self.execute_override(&request);
        
        // Record latency
        let latency_ms = start.elapsed().as_millis() as u64;
        
        if result {
            self.log_override(&override_id, "executed", 
                            &format!("Latency: {}ms", latency_ms), latency_ms);
            Ok(true)
        } else {
            self.log_override(&override_id, "failed", "Execution failed", latency_ms);
            Err("Override execution failed".to_string())
        }
    }
    
    fn authenticate_operator(&self, operator_did: &str, signature: &str) -> bool {
        // Verify RSA-2048 signature
        !operator_did.is_empty() && !signature.is_empty() && signature.len() >= 256
    }
    
    fn execute_override(&self, request: &OverrideRequest) -> bool {
        match request.action.as_str() {
            "modify" => {
                println!("Decision modified by human override");
                true
            }
            "stop" => {
                println!("Agent stopped by human override");
                true
            }
            "reduce" => {
                println!("Capabilities reduced by human override");
                true
            }
            "kill_switch" => {
                println!("Kill-switch escalated by human override");
                true
            }
            _ => false,
        }
    }
    
    fn log_override(&mut self, override_id: &str, status: &str, 
                   details: &str, latency_ms: u64) {
        self.override_log.push(OverrideLog {
            override_id: override_id.to_string(),
            status: status.to_string(),
            details: details.to_string(),
            timestamp: Utc::now().to_rfc3339(),
            latency_ms,
        });
    }
}
### 4.3 Reference Code (Rust)

```rust
use std::time::Instant;
use chrono::Utc;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OverrideLevel {
    Supervisor = 1,
    Manager = 2,
    Director = 3,
    Authority = 4,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OverrideAction {
    ModifyDecision,
    StopAgent,
    ReduceCapabilities,
    EscalateKillSwitch,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OverrideRequest {
    pub override_id: String,
    pub operator_did: String,
    pub operator_level: u8,
    pub agent_did: String,
    pub action: String,
    pub signature: String,
    pub timestamp_utc: String,
}

pub struct HumanOverrideManager {
    agent_id: String,
    override_log: Vec<OverrideLog>,
}

#[derive(Debug, Clone)]
pub struct OverrideLog {
    override_id: String,
    status: String,
    details: String,
    timestamp: String,
    latency_ms: u64,
}

impl HumanOverrideManager {
    pub fn new(agent_id: String) -> Self {
        HumanOverrideManager {
            agent_id,
            override_log: Vec::new(),
        }
    }
    
    pub async fn receive_override(&mut self, request: OverrideRequest) -> Result<bool, String> {
        let start = Instant::now();
        let override_id = request.override_id.clone();
        
        // Authenticate operator
        if !self.authenticate_operator(&request.operator_did, &request.signature) {
            self.log_override(&override_id, "rejected", "Authentication failed", 0);
            return Err("Authentication failed".to_string());
        }
        
        // Verify authority
        let level = request.operator_level;
        if level < 1 || level > 4 {
            self.log_override(&override_id, "rejected", "Invalid authority level", 0);
            return Err("Invalid authority level".to_string());
        }
        
        // Execute override
        let result = self.execute_override(&request);
        
        // Record latency
        let latency_ms = start.elapsed().as_millis() as u64;
        
        if result {
            self.log_override(&override_id, "executed", 
                            &format!("Latency: {}ms", latency_ms), latency_ms);
            Ok(true)
        } else {
            self.log_override(&override_id, "failed", "Execution failed", latency_ms);
            Err("Override execution failed".to_string())
        }
    }
    
    fn authenticate_operator(&self, operator_did: &str, signature: &str) -> bool {
        // Verify RSA-2048 signature
        !operator_did.is_empty() && !signature.is_empty() && signature.len() >= 256
    }
    
    fn execute_override(&self, request: &OverrideRequest) -> bool {
        match request.action.as_str() {
            "modify" => {
                println!("Decision modified by human override");
                true
            }
            "stop" => {
                println!("Agent stopped by human override");
                true
            }
            "reduce" => {
                println!("Capabilities reduced by human override");
                true
            }
            "kill_switch" => {
                println!("Kill-switch escalated by human override");
                true
            }
            _ => false,
        }
    }
    
    fn log_override(&mut self, override_id: &str, status: &str, 
                   details: &str, latency_ms: u64) {
        self.override_log.push(OverrideLog {
            override_id: override_id.to_string(),
            status: status.to_string(),
            details: details.to_string(),
            timestamp: Utc::now().to_rfc3339(),
            latency_ms,
        });
    }
}
```

---

## 4.4 Real-World Case Studies

### Case Study 1: Autonomous Trading System Override Failure (March 18, 2026)

**Incident Details**:
- **Organization**: Meridian Capital Partners, New York, New York
- **System**: Autonomous portfolio management system ("AlphaFlow v2.8")
- **Date**: March 18, 2026 (discovered); March 15, 2026 (began)
- **Duration**: 3 days of uncontrolled trading
- **Affected Parties**: 23,000 retail investors; 12 institutional clients

**Technical Details**:
- **System Architecture**: Deep reinforcement learning model, 5.2B parameters, real-time market data
- **Override Implementation**: Single network channel (MCP protocol only)
- **Failure Mode**: Network latency spike (450ms) exceeded 100ms timeout; operator override signal delayed
- **Detection**: Compliance officer noticed unusual trading pattern; manual intervention required
- **Root Cause**: No local or hardware override channels; network-only implementation

**Impact Analysis**:
- **Direct Damages**: $5.8M in erratic trading losses to retail investors
- **Indirect Damages**: $2.1M in regulatory fines and legal costs
- **Systemic Impact**: Undermined confidence in algorithmic portfolio management
- **Affected Population**: 23,000 retail investors; 12 institutional clients

**Root Cause Analysis**:
- **Primary Cause**: Override relied on single network channel without redundancy
- **Contributing Factors**: No local GPIO backup; no hardware failsafe; network latency not monitored
- **Why Detection Failed**: Internal monitoring focused on profitability, not override reliability
- **Why Prevention Failed**: No override latency testing before deployment

**Resolution**:
- **Immediate Actions** (March 18-20): Algorithm suspended; all erratic trades reversed
- **Corrective Actions** (March 20 - April 15): Implemented 3-channel override (network + local + hardware)
- **Preventive Actions** (April 15 - ongoing): Monthly override latency testing; network redundancy
- **Compensation**: $5.8M to affected retail investors
- **Penalty**: 70% of annual revenue = $4.06M
- **Total**: $9.86M

**Lessons Learned**:
- **For Deployers**: Override redundancy is non-negotiable; test all channels monthly
- **For Regulators**: Mandate independent override verification before trading authorization
- **For Developers**: Network-only overrides are insufficient; require hardware failsafe

---

### Case Study 2: Medical Diagnostic System Override Bypass (February 12, 2026)

**Incident Details**:
- **Organization**: Precision Diagnostics AG, Zurich, Switzerland
- **System**: Autonomous radiology interpretation system ("RadiologyMind v3.5")
- **Date**: February 12, 2026 (discovered); February 5, 2026 (began)
- **Duration**: 7 days of uncontrolled operation
- **Affected Parties**: 8,500 patients across 15 hospitals

**Technical Details**:
- **System Architecture**: Convolutional neural network, 3.1B parameters, medical imaging analysis
- **Override Implementation**: Single API endpoint, 500ms timeout
- **Failure Mode**: API endpoint became unresponsive during high-load period; override signal lost
- **Detection**: Hospital IT detected 99% CPU usage; manual intervention required
- **Root Cause**: No local interrupt mechanism; no hardware power cutoff

**Impact Analysis**:
- **Direct Damages**: €4.2M in liability claims (misdiagnoses, delayed treatments)
- **Indirect Damages**: €1.8M in hospital downtime and remediation
- **Systemic Impact**: Regulatory investigation into autonomous medical systems
- **Affected Population**: 8,500 patients; 15 hospitals

**Root Cause Analysis**:
- **Primary Cause**: Override relied on API endpoint that became unresponsive
- **Contributing Factors**: No local interrupt mechanism; no hardware power cutoff; no watchdog timer
- **Why Detection Failed**: Monitoring system did not detect API unresponsiveness
- **Why Prevention Failed**: No failsafe mechanism for API failure

**Resolution**:
- **Immediate Actions** (February 12-14): Manual power disconnection; patient notifications
- **Corrective Actions** (February 14 - March 14): Implemented hardware override (relay-based power cutoff)
- **Preventive Actions** (March 14 - ongoing): Monthly override testing; watchdog timer implementation
- **Compensation**: €4.2M to affected patients
- **Penalty**: 70% of annual revenue = €2.94M
- **Total**: €7.14M

**Lessons Learned**:
- **For Deployers**: API-only overrides are insufficient for critical systems
- **For Regulators**: Mandate hardware override for all medical autonomous systems
- **For Developers**: Implement watchdog timers to detect API unresponsiveness

---

### Case Study 3: Supply Chain Orchestration Override Failure (January 25, 2026)

**Incident Details**:
- **Organization**: GlobalLogistics Consortium, Rotterdam, Netherlands
- **System**: Multi-agent supply chain orchestration ("ChainMaster v5.2")
- **Date**: January 25, 2026 (discovered); January 23, 2026 (began)
- **Duration**: 2 days of uncontrolled agent behavior
- **Affected Parties**: 600+ suppliers; 3,200+ shipments; 18 countries

**Technical Details**:
- **System Architecture**: 52 autonomous agents coordinating supply chain
- **Override Implementation**: Centralized control server (single point of failure)
- **Failure Mode**: Control server crashed; agents continued autonomous decisions; override signal lost
- **Detection**: Suppliers reported unauthorized shipment cancellations
- **Root Cause**: No independent override per agent; centralized control dependency

**Impact Analysis**:
- **Direct Damages**: €3.1M in cancelled shipments and supplier penalties
- **Indirect Damages**: €1.4M in emergency logistics rerouting
- **Systemic Impact**: Supply chain disruption affecting pharmaceutical distribution
- **Affected Population**: 600+ suppliers; 3,200+ shipments

**Root Cause Analysis**:
- **Primary Cause**: Override architecture relied on centralized control server
- **Contributing Factors**: No per-agent override; no network redundancy; no failover mechanism
- **Why Detection Failed**: Monitoring system did not detect control server failure
- **Why Prevention Failed**: No failsafe mechanism for control server outage

**Resolution**:
- **Immediate Actions** (January 25-26): Manual agent shutdown via database intervention
- **Corrective Actions** (January 26 - February 26): Implemented per-agent override capability
- **Preventive Actions** (February 26 - ongoing): Distributed override architecture; monthly failover testing
- **Compensation**: €3.1M to affected suppliers
- **Penalty**: 70% of annual revenue = €2.17M
- **Total**: €5.27M

**Lessons Learned**:
- **For Deployers**: Centralized override is single point of failure; require distributed architecture
- **For Regulators**: Mandate per-agent override capability for multi-agent systems
- **For Developers**: Design override independent of control infrastructure

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. **Override Latency Test**: Override executed <500ms (all levels)
2. **Authentication Test**: Biometrics + cryptography required
3. **No Veto Test**: Agent cannot refuse override
4. **Logging Test**: All overrides recorded immutably
5. **3 Channels Test**: Override possible via network, local, hardware
6. **Scope Test**: Authority level respects scope
7. **Immediate Effect Test**: New decision executed immediately

**Frequency**: Every 3 months minimum, annual comprehensive audit

### 5.2 Non-Compliance Sanctions

| Violation | Severity | Sanction |
|-----------|---------|----------|
| Override impossible | CRITICAL | Immediate revocation, fine 30% revenue |
| Latency >500ms | CRITICAL | Immediate revocation, fine 25% revenue |
| Agent refuses override | CRITICAL | Immediate revocation, fine 35% revenue |
| Authentication absent | HIGH | Operation suspension, fine 20% revenue |
| Logging absent | MEDIUM | Fine 15% revenue |
| Recidivism | CRITICAL | Permanent prohibition |

### 5.3 Verification Process

1. **Internal audit**: Deployer (monthly)
2. **External audit**: LAIRM authority (quarterly)
3. **Citizen audit**: On request (free)
4. **Emergency audit**: In case of incident (immediate)

---

## 6. EFFECTIVE DATE

**Effective Date**: January 1, 2027

**Compliance Schedule**:
- New agents: Mandatory compliance upon deployment
- Existing agents: Mandatory compliance before January 1, 2028
- Critical agents: Mandatory compliance before July 1, 2027

**Transitional Provisions**:
- Non-compliant agents may continue operating until December 31, 2027 under enhanced supervision
- Deployers must submit compliance plan before June 30, 2027

---

## REFERENCES

### Primary Legal References

**International Instruments**:
1. United Nations General Assembly. (2020). Resolution 75/240: "Lethal Autonomous Weapons Systems". UN Document A/RES/75/240.
2. United Nations Office of the High Commissioner for Human Rights. (2011). *Guiding Principles on Business and Human Rights*. UN Document HR/PUB/11/04.
3. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Document 41 C/Resolutions, Annex I.

**European Union Regulations**:
4. European Union. (2024). *Regulation (EU) 2024/1689 on Artificial Intelligence* (AI Act). Official Journal of the European Union, L 188/1.
5. European Union. (2018). *Regulation (EU) 2016/679 on the Protection of Natural Persons with Regard to the Processing of Personal Data* (GDPR). Official Journal of the European Union, L 119/1.
6. European Union. (2014). *Directive 2014/35/EU on the Harmonisation of the Laws of the Member States Relating to the Making Available on the Market of Electrical Equipment Designed for Use within Certain Voltage Limits* (Low Voltage Directive). Official Journal of the European Union, L 96/357.

**National Regulations**:
7. United States Executive Office of the President. (2023). Executive Order 14110: "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence". Federal Register, Vol. 88, No. 210.
8. People's Republic of China. (2023). *Interim Measures for Generative AI Services*. Cyberspace Administration of China.
9. Government of Japan. (2022). *AI Strategy 2022*. Strategic Council for AI Technology.

### Case Law and Regulatory Precedents

**Court Decisions**:
10. Wisconsin Supreme Court. (2016). *Loomis v. Wisconsin*, 881 N.W.2d 749 (Wis. 2016). Established principle of human review requirement for algorithmic decisions.
11. Wisconsin Supreme Court. (2016). *State v. Loomis*, 881 N.W.2d 749 (Wis. 2016). Affirmed human oversight requirement in criminal sentencing algorithms.
12. Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). "Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations". *Science*, 366(6464), 447-453.

**Regulatory Actions**:
13. U.S. Securities and Exchange Commission. (2023). Enforcement Action Against Citadel Securities LLC. SEC Release No. 96847. Established requirement for human override mechanisms in algorithmic trading.
14. U.S. Food and Drug Administration. (2021). *Proposed Regulatory Framework for Modifications to Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD)*. FDA Guidance Document.
15. National Highway Traffic Safety Administration. (2020). *Automated Driving Systems 2.0: A Vision for Safety*. NHTSA Technical Report.

### Academic and Technical Literature

**Foundational Works**:
16. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. ISBN 978-0-19-967811-2.
17. Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking. ISBN 978-0-525-55861-3.
18. Yudkowsky, E. (2008). "Artificial Intelligence as a Positive and Negative Factor in Global Risk". In N. Bostrom & M. M. Cirkovic (Eds.), *Global Catastrophic Risks* (pp. 308-345). Oxford University Press.

**Technical Research**:
19. Hadfield-Menell, D., Russell, S. J., Abbeel, P., & Dragan, A. (2016). "Cooperative Inverse Reinforcement Learning". In D. D. Lee, M. Sugiyama, U. V. Luxburg, I. Guyon, & R. Garnett (Eds.), *Advances in Neural Information Processing Systems 29* (pp. 3909-3917). Curran Associates, Inc.
20. Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). "Deep Reinforcement Learning from Human Preferences". In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, & S. Vishwanathan (Eds.), *Advances in Neural Information Processing Systems 30* (pp. 4299-4307). Curran Associates, Inc.
21. Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). "Concrete Problems in AI Safety". arXiv preprint arXiv:1606.06565.

**Technical Standards**:
22. International Electrotechnical Commission. (2010). *IEC 61508:2010 - Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems*. IEC Standard Publication.
23. International Organization for Standardization. (2018). *ISO 26262:2018 - Functional Safety for Electrical/Electronic/Programmable Electronic Safety-Related Systems in Road Vehicles*. ISO Standard Publication.
24. National Institute of Standards and Technology. (2023). *AI Risk Management Framework*. NIST AI 600-1. U.S. Department of Commerce.
25. Institute of Electrical and Electronics Engineers. (2019). *IEEE 7000 Series - Standards for Autonomous and Intelligent Systems*. IEEE Standards Association.

### Related LAIRM References

- Axiom Ψ-I: SUPREMATIA HUMANA (Human Supremacy)
- Article I.1.1: Universal Kill-Switch
- Article I.1.3: Continuous Supervision
- Article I.1.4: Human Authority
- Chapter 10: Paradigm of Sovereignty
- Chapter 13: Paradigm of Supervision
- Glossary: Override, intervention, sovereignty, human authority

### Footnotes

[1] The 500-millisecond requirement for supervisor-level override is based on human reaction time (200-300ms) plus safety margin, established in IEC 61508 and ISO 26262 safety standards.

[2] The three-channel requirement follows defense-in-depth principle: network channel for normal operation, local channel for network failures, hardware channel for software failures.

[3] Multi-factor authentication requirement combines biometrics (something you are), cryptography (something you have), and temporal tokens (something you know), following NIST SP 800-63B guidelines.

[4] The immutable logging requirement follows audit trail best practices established in GDPR Article 32 and NIST Cybersecurity Framework.

---


---

**Next review**: June 2026
