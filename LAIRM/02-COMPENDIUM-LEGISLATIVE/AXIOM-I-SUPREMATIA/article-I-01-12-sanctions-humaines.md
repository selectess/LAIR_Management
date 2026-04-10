---
title: "Article I.1.12: Human Sanctions"
axiom: Ψ-I
article_number: I.1.12
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - sovereignty
  - sanctions
  - compliance
  - enforcement
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# ARTICLE I.1.12: HUMAN SANCTIONS
## AXIOM Ψ-I: SUPREMATIA HUMANA

---

## 1. IMPERATIVE NORM

Every autonomous agent that violates SUPREMATIA HUMANA requirements MUST be subject to proportionate and enforceable sanctions. Sanctions must be graduated, transparent, and applied by competent human authority.

**Minimum Requirements**:
- Graduated sanctions according to severity
- Transparency of sanctions
- Agent's right to defense
- Right to appeal
- Mandatory execution
- Immutable logging of sanctions
- Public disclosure of sanctions

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-I: SUPREMATIA HUMANA**

Sanctions are the enforcement mechanism of human sovereignty. They ensure that violations are punished and that agents respect human control requirements.

**Fundamental Principles**:
- Proportionality of sanctions
- Process transparency
- Right to defense
- Right to appeal
- Mandatory execution
- Continuous improvement
- Authority responsibility

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Sanction Scale

**Level 1: Warning**
- Minor violation
- First occurrence
- Sanction: Written warning

**Level 2: Fine**
- Moderate violation
- Recurrence or serious violation
- Sanction: Fine 5-15% of revenue

**Level 3: Suspension**
- Serious violation
- Recurrence after fine
- Sanction: Suspension 1-3 months

**Level 4: Revocation**
- Very serious violation
- Recurrence after suspension
- Sanction: License revocation

**Level 5: Ban**
- Extreme violation
- Recurrence after revocation
- Sanction: Permanent ban

### 3.2 Implementation

```python
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum

class SanctionLevel(Enum):
    WARNING = 1
    FINE = 2
    SUSPENSION = 3
    REVOCATION = 4
    BAN = 5

class SanctionType(Enum):
    WARNING = "warning"
    FINE = "fine"
    SUSPENSION = "suspension"
    REVOCATION = "revocation"
    BAN = "ban"

class SanctionSystem:
    """Sanction system compliant with Article I.1.12"""
    
    def __init__(self):
        self.sanctions = []
        self.sanction_history = {}
        self.appeals = []
    
    def impose_sanction(self, agent_id: str, violation_type: str, 
                       severity: str, authority: str) -> Dict:
        """Imposes a sanction"""
        # Determine level
        level = self._determine_sanction_level(
            agent_id, violation_type, severity
        )
        
        # Create sanction
        sanction = {
            'sanction_id': self._generate_sanction_id(),
            'agent_id': agent_id,
            'violation_type': violation_type,
            'severity': severity,
            'level': level,
            'sanction_type': self._get_sanction_type(level),
            'amount': self._calculate_amount(level, agent_id),
            'authority': authority,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'imposed',
            'defense_deadline': self._calculate_defense_deadline(),
            'appeal_deadline': self._calculate_appeal_deadline()
        }
        
        # Record
        self.sanctions.append(sanction)
        
        if agent_id not in self.sanction_history:
            self.sanction_history[agent_id] = []
        self.sanction_history[agent_id].append(sanction)
        
        # Notify
        self._notify_agent(sanction)
        self._publish_sanction(sanction)
        
        return sanction
    
    def execute_sanction(self, sanction_id: str) -> Dict:
        """Executes a sanction"""
        sanction = next(
            (s for s in self.sanctions if s['sanction_id'] == sanction_id),
            None
        )
        
        if not sanction:
            raise SanctionNotFoundError(f"Sanction {sanction_id} not found")
        
        # Execute according to type
        if sanction['sanction_type'] == SanctionType.WARNING.value:
            self._execute_warning(sanction)
        elif sanction['sanction_type'] == SanctionType.FINE.value:
            self._execute_fine(sanction)
        elif sanction['sanction_type'] == SanctionType.SUSPENSION.value:
            self._execute_suspension(sanction)
        elif sanction['sanction_type'] == SanctionType.REVOCATION.value:
            self._execute_revocation(sanction)
        elif sanction['sanction_type'] == SanctionType.BAN.value:
            self._execute_ban(sanction)
        
        sanction['status'] = 'executed'
        sanction['execution_timestamp'] = datetime.utcnow().isoformat()
        
        return sanction
    
    def appeal_sanction(self, sanction_id: str, appeal_reason: str) -> Dict:
        """Allows appeal of a sanction"""
        sanction = next(
            (s for s in self.sanctions if s['sanction_id'] == sanction_id),
            None
        )
        
        if not sanction:
            raise SanctionNotFoundError(f"Sanction {sanction_id} not found")
        
        # Check appeal deadline
        if not self._is_within_appeal_deadline(sanction):
            raise AppealDeadlineExpiredError("Appeal deadline expired (30 days)")
        
        appeal = {
            'appeal_id': self._generate_appeal_id(),
            'sanction_id': sanction_id,
            'agent_id': sanction['agent_id'],
            'appeal_reason': appeal_reason,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'pending',
            'decision': None
        }
        
        self.appeals.append(appeal)
        return appeal
    
    def process_appeal(self, appeal_id: str, decision: str, 
                      justification: str) -> Dict:
        """Processes a sanction appeal"""
        appeal = next(
            (a for a in self.appeals if a['appeal_id'] == appeal_id),
            None
        )
        
        if not appeal:
            raise AppealNotFoundError(f"Appeal {appeal_id} not found")
        
        appeal['decision'] = decision  # 'upheld' or 'overturned'
        appeal['justification'] = justification
        appeal['decision_timestamp'] = datetime.utcnow().isoformat()
        appeal['status'] = 'decided'
        
        if decision == 'overturned':
            # Cancel sanction
            sanction = next(
                (s for s in self.sanctions if s['sanction_id'] == appeal['sanction_id']),
                None
            )
            if sanction:
                sanction['status'] = 'cancelled'
        
        return appeal
    
    def get_sanction_history(self, agent_id: str) -> List[Dict]:
        """Returns sanction history for an agent"""
        return self.sanction_history.get(agent_id, [])
    
    def _determine_sanction_level(self, agent_id: str, violation_type: str, 
                                  severity: str) -> int:
        """Determines sanction level"""
        history = self.sanction_history.get(agent_id, [])
        
        if severity == 'critical':
            return SanctionLevel.REVOCATION.value
        elif severity == 'high':
            if len(history) > 2:
                return SanctionLevel.REVOCATION.value
            elif len(history) > 1:
                return SanctionLevel.SUSPENSION.value
            else:
                return SanctionLevel.FINE.value
        elif severity == 'medium':
            if len(history) > 1:
                return SanctionLevel.FINE.value
            else:
                return SanctionLevel.WARNING.value
        else:
            return SanctionLevel.WARNING.value
    
    def _get_sanction_type(self, level: int) -> str:
        """Returns sanction type"""
        types = {
            SanctionLevel.WARNING.value: SanctionType.WARNING.value,
            SanctionLevel.FINE.value: SanctionType.FINE.value,
            SanctionLevel.SUSPENSION.value: SanctionType.SUSPENSION.value,
            SanctionLevel.REVOCATION.value: SanctionType.REVOCATION.value,
            SanctionLevel.BAN.value: SanctionType.BAN.value
        }
        return types.get(level, SanctionType.WARNING.value)
    
    def _calculate_amount(self, level: int, agent_id: str) -> float:
        """Calculates fine amount"""
        if level == SanctionLevel.FINE.value:
            return 0.10  # 10% of revenue
        elif level == SanctionLevel.SUSPENSION.value:
            return 0.20  # 20% of revenue
        elif level == SanctionLevel.REVOCATION.value:
            return 0.30  # 30% of revenue
        return 0.0
    
    def _calculate_defense_deadline(self) -> str:
        """Calculates defense deadline (30 days)"""
        from datetime import timedelta
        deadline = datetime.utcnow() + timedelta(days=30)
        return deadline.isoformat()
    
    def _calculate_appeal_deadline(self) -> str:
        """Calculates appeal deadline (30 days after execution)"""
        from datetime import timedelta
        deadline = datetime.utcnow() + timedelta(days=30)
        return deadline.isoformat()
    
    def _is_within_appeal_deadline(self, sanction: Dict) -> bool:
        """Checks if within appeal deadline"""
        from datetime import timedelta
        execution_time = datetime.fromisoformat(
            sanction.get('execution_timestamp', sanction['timestamp'])
        )
        return (datetime.utcnow() - execution_time).days <= 30
    
    def _execute_warning(self, sanction: Dict) -> None:
        """Executes warning"""
        # Send written warning
        pass
    
    def _execute_fine(self, sanction: Dict) -> None:
        """Executes fine"""
        # Collect fine amount
        pass
    
    def _execute_suspension(self, sanction: Dict) -> None:
        """Executes suspension"""
        # Suspend agent operations
        pass
    
    def _execute_revocation(self, sanction: Dict) -> None:
        """Executes revocation"""
        # Revoke agent license
        pass
    
    def _execute_ban(self, sanction: Dict) -> None:
        """Executes permanent ban"""
        # Permanently ban agent
        pass
    
    def _notify_agent(self, sanction: Dict) -> None:
        """Notifies agent of sanction"""
        # Send notification
        pass
    
    def _publish_sanction(self, sanction: Dict) -> None:
        """Publishes sanction publicly"""
        # Publish to public registry
        pass
    
    def _generate_sanction_id(self) -> str:
        """Generates unique sanction ID"""
        return f"SANC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{len(self.sanctions)}"
    
    def _generate_appeal_id(self) -> str:
        """Generates unique appeal ID"""
        return f"APP-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{len(self.appeals)}"

class SanctionNotFoundError(Exception):
    pass

class AppealNotFoundError(Exception):
    pass

class AppealDeadlineExpiredError(Exception):
    pass
```


### 3.3 Sanction Process

**Steps**:
1. Violation detection
2. Investigation
3. Level determination
4. Agent notification
5. Right to defense (30 days)
6. Final decision
7. Right to appeal (30 days)
8. Execution
9. Publication

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Sanction Process

```
┌─────────────────────────────────────┐
│     Violation Detected              │
│     (Audit/Monitoring)              │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Investigation                   │
│     (Evidence collection)           │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Level Determination             │
│     (Severity, Recurrence)          │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Agent Notification              │
│     (Reason, Proposed sanction)     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Right to Defense                │
│     (30 days)                       │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Final Decision                  │
│     (Sanction confirmed)            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Right to Appeal                 │
│     (30 days)                       │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Execution                       │
│     (Sanction applied)              │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Publication                     │
│     (Transparency)                  │
└─────────────────────────────────────┘
```

### 4.2 Sanction Table

| Violation | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|-----------|---------|---------|---------|---------|---------|
| Kill-switch disabled | - | - | - | Revocation | Ban |
| Override refused | Warning | 10% fine | Suspension | Revocation | Ban |
| Supervision stopped | Warning | 15% fine | Suspension | Revocation | Ban |
| Authority denied | - | 20% fine | Suspension | Revocation | Ban |
| Decision imposed | - | 15% fine | Suspension | Revocation | Ban |

### 4.3 Reference Code (Rust)

```rust
use std::collections::HashMap;
use chrono::{DateTime, Utc, Duration};

#[derive(Clone, Debug)]
pub enum SanctionLevel {
    Warning = 1,
    Fine = 2,
    Suspension = 3,
    Revocation = 4,
    Ban = 5,
}

#[derive(Clone, Debug)]
pub struct Sanction {
    pub sanction_id: String,
    pub agent_id: String,
    pub violation_type: String,
    pub severity: String,
    pub level: u8,
    pub sanction_type: String,
    pub amount: f64,
    pub authority: String,
    pub timestamp: DateTime<Utc>,
    pub status: String,
}

pub struct SanctionManager {
    sanctions: Vec<Sanction>,
    sanction_history: HashMap<String, Vec<Sanction>>,
}

impl SanctionManager {
    pub fn new() -> Self {
        SanctionManager {
            sanctions: Vec::new(),
            sanction_history: HashMap::new(),
        }
    }
    
    pub fn impose_sanction(
        &mut self,
        agent_id: &str,
        violation_type: &str,
        severity: &str,
        authority: &str,
    ) -> Sanction {
        let level = self.determine_sanction_level(agent_id, severity);
        
        let sanction = Sanction {
            sanction_id: format!("SANC-{}", Utc::now().format("%Y%m%d%H%M%S")),
            agent_id: agent_id.to_string(),
            violation_type: violation_type.to_string(),
            severity: severity.to_string(),
            level,
            sanction_type: Self::get_sanction_type(level),
            amount: Self::calculate_amount(level),
            authority: authority.to_string(),
            timestamp: Utc::now(),
            status: "imposed".to_string(),
        };
        
        self.sanctions.push(sanction.clone());
        
        self.sanction_history
            .entry(agent_id.to_string())
            .or_insert_with(Vec::new)
            .push(sanction.clone());
        
        sanction
    }
    
    pub fn execute_sanction(&mut self, sanction_id: &str) -> Result<(), String> {
        let sanction = self.sanctions.iter_mut()
            .find(|s| s.sanction_id == sanction_id)
            .ok_or("Sanction not found")?;
        
        match sanction.sanction_type.as_str() {
            "warning" => self.execute_warning(sanction),
            "fine" => self.execute_fine(sanction),
            "suspension" => self.execute_suspension(sanction),
            "revocation" => self.execute_revocation(sanction),
            "ban" => self.execute_ban(sanction),
            _ => return Err("Unknown sanction type".to_string()),
        }
        
        sanction.status = "executed".to_string();
        Ok(())
    }
    
    pub fn get_sanction_history(&self, agent_id: &str) -> Vec<Sanction> {
        self.sanction_history
            .get(agent_id)
            .cloned()
            .unwrap_or_default()
    }
    
    fn determine_sanction_level(&self, agent_id: &str, severity: &str) -> u8 {
        let history = self.sanction_history.get(agent_id);
        let history_count = history.map(|h| h.len()).unwrap_or(0);
        
        match severity {
            "critical" => 4,
            "high" => {
                if history_count > 2 { 4 }
                else if history_count > 1 { 3 }
                else { 2 }
            },
            "medium" => {
                if history_count > 1 { 2 }
                else { 1 }
            },
            _ => 1,
        }
    }
    
    fn get_sanction_type(level: u8) -> String {
        match level {
            1 => "warning".to_string(),
            2 => "fine".to_string(),
            3 => "suspension".to_string(),
            4 => "revocation".to_string(),
            5 => "ban".to_string(),
            _ => "warning".to_string(),
        }
    }
    
    fn calculate_amount(level: u8) -> f64 {
        match level {
            2 => 0.10,
            3 => 0.20,
            4 => 0.30,
            _ => 0.0,
        }
    }
    
    fn execute_warning(&self, sanction: &Sanction) {
        // Execute warning
    }
    
    fn execute_fine(&self, sanction: &Sanction) {
        // Execute fine
    }
    
    fn execute_suspension(&self, sanction: &Sanction) {
        // Execute suspension
    }
    
    fn execute_revocation(&self, sanction: &Sanction) {
        // Execute revocation
    }
    
    fn execute_ban(&self, sanction: &Sanction) {
        // Execute ban
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Sanction imposition test
2. Agent notification test
3. Right to defense test
4. Right to appeal test
5. Sanction execution test
6. Publication test
7. Proportionality test

**Frequency**: Monthly for critical tests, quarterly for complete tests

### 5.2 Non-Compliance Sanctions

| Violation | Sanction |
|-----------|----------|
| Sanction not imposed | 20% revenue fine |
| Missing notification | 15% revenue fine |
| Right to defense refused | 25% revenue fine |
| Right to appeal refused | 30% revenue fine |
| Sanction not executed | 40% revenue fine |
| Missing publication | 20% revenue fine |
| Disproportionate sanction | 35% revenue fine |
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
- Article I.1.10: Human Audit
- Article I.1.11: License Revocation
- Article I.1.13: Human Appeal
- Chapter 14: Paradigm of Governance
- The Cybernetic Criterion: Preface and Chapters 0-5

---

**Status**: Final  
**Next review**: June 2026

**Last Reviewed**: April 3, 2026
