---
title: "Article III.3.11: Prescription and Deadlines"
axiom: Ψ-III
article_number: III.3.11
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - prescription
  - deadlines
  - procedure
  - justice
  - recourse
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.11: PRESCRIPTION AND DEADLINES
## Axiom Ψ-III: RESPONSABILITAS JURIDICA

---

## 1. IMPERATIVE NORM

Prescription deadlines for actions in Responsibility against an autonomous agent must be sufficiently long to allow victims to obtain redress. Prescription MUST be suspended in case of fraud or concealment. Deadlines must be clear, immutable, and notified to victims.

**Minimum Requirements**:
- Prescription deadline of minimum 10 years (Civil Responsibility)
- Prescription deadline of 20 years (Penal Responsibility)
- Suspension in case of fraud (unlimited)
- Clear and immutable deadlines (mandatory notification)
- Mandatory notification of deadlines (to victim)
- Recourse in case of expiration (appeal)
- Immutable registry (traceability)
- Public transparency (open registry)
- Zero unjustified prescription
- Victim assistance (support)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS AGENTICA**

Prescription deadlines must be sufficiently long to allow victims to discover damages and obtain redress. A deadline that is too short would make Responsibility illusory. Suspension in case of fraud ensures that victims are not penalized by concealment.

**Fundamental Principles**:
- Sufficiently long deadlines (10-20 years)
- Suspension in case of fraud (unlimited)
- Clarity of deadlines (notification)
- Mandatory notification (to victim)
- Effective recourse (appeal, revision)
- Transparency (public registry)
- Justice (fairness for victims)
- Prevention (deterrence)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Prescription Periods

```python
class PrescriptionPeriod:
    PERIODS = {
        'civil_liability': 10,  # years
        'penal_liability': 20,  # years
        'discovery_rule': 3,    # years after discovery
        'fraud_suspension': None  # unlimited
    }
    
    def calculate_prescription_deadline(self, damage_date, damage_type):
        """Calculate prescription deadline date"""
        if damage_type == 'fraud':
            return None  # No prescription
        
        period = self.PERIODS.get(damage_type, 10)
        deadline = damage_date + timedelta(days=period*365)
        
        return deadline
    
    def check_prescription_status(self, damage_date, damage_type, current_date):
        """Check prescription status"""
        deadline = self.calculate_prescription_deadline(damage_date, damage_type)
        
        if deadline is None:
            return 'no_prescription'
        
        if current_date > deadline:
            return 'prescribed'
        else:
            days_remaining = (deadline - current_date).days
            return f'active_{days_remaining}_days'
```

### 3.2 Deadlines by Damage Type

| Damage Type | Deadline | Suspension |
|------------|----------|-----------|
| Civil Responsibility | 10 years | Fraud |
| Penal Responsibility | 20 years | Fraud |
| Late discovery | 3 years after discovery | Fraud |
| Fraud | Unlimited | N/A |

### 3.3 Prescription Suspension

Prescription MUST be suspended in case of:
- Fraud or concealment
- Recognition of Responsibility
- Legal action initiated
- Formal indemnification request

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: TradeBot3000 ($45M)

**Incident**: Unauthorized position of $45M
**Damage date**: 2026-01-15
**Discovery**: 2026-01-16 (1 day)
**Civil deadline**: 10 years (2036-01-15)
**Penal deadline**: 20 years (2046-01-15)
**Suspension**: No (no fraud)
**Status**: Active (prescription ongoing)

### 4.2 Use Case: HealthBot (Incorrect Diagnosis)

**Incident**: Incorrect diagnosis causing hospitalization
**Damage date**: 2026-02-20
**Discovery**: 2026-03-15 (23 days)
**Civil deadline**: 10 years (2036-02-20)
**Penal deadline**: 20 years (2046-02-20)
**Suspension**: Yes (fraud detected 2026-04-01)
**Status**: Suspended (unlimited)

### 4.3 Reference Code (Rust)

```rust
use chrono::{DateTime, Utc, Duration};

pub struct PrescriptionPeriod {
    pub civil_liability_years: i32,
    pub penal_liability_years: i32,
    pub discovery_rule_years: i32,
}

impl PrescriptionPeriod {
    pub fn calculate_deadline(
        &self,
        damage_date: DateTime<Utc>,
        damage_type: &str,
        fraud_detected: bool,
    ) -> Option<DateTime<Utc>> {
        if fraud_detected {
            return None; // No prescription for fraud
        }
        
        let years = match damage_type {
            "civil" => self.civil_liability_years,
            "penal" => self.penal_liability_years,
            _ => self.civil_liability_years,
        };
        
        Some(damage_date + Duration::days(years as i64 * 365))
    }
    
    pub fn check_status(
        &self,
        damage_date: DateTime<Utc>,
        damage_type: &str,
        current_date: DateTime<Utc>,
        fraud_detected: bool,
    ) -> String {
        if fraud_detected {
            return "no_prescription".to_string();
        }
        
        if let Some(deadline) = self.calculate_deadline(damage_date, damage_type, false) {
            if current_date > deadline {
                "prescribed".to_string()
            } else {
                let days_remaining = (deadline - current_date).num_days();
                format!("active_{}_days", days_remaining)
            }
        } else {
            "no_prescription".to_string()
        }
    }
}
```

### 4.4 Deadline Management

```
┌──────────────────────────────────────┐
│      Damage Caused                   │
│      Date: T0                        │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Calculate Prescription Deadline     │
│  - Damage type                       │
│  - Applicable deadline (10 or 20 yrs)│
│  - Deadline date: T0 + deadline      │
│  - Deadline: < 1 day                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Notify Victim (< 5 days)            │
│  - Prescription deadline             │
│  - Exact deadline date               │
│  - Victim rights                     │
│  - Available recourse                │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Monitor Deadline (continuous)       │
│  - Verify suspension                 │
│  - Alert before expiration (30d)     │
│  - Record actions                    │
│  - Immutable audit trail             │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  At Deadline Date                    │
│  - Prescription acquired             │
│  - Or legal action initiated         │
│  - Or suspension applied             │
│  - Final notification                │
└──────────────────────────────────────┘
```

### 4.5 Prescription Registry

Each agent MUST maintain an immutable registry of:
- All damages and dates (100%)
- Prescription deadlines (civil + penal)
- Suspensions applied (fraud)
- Legal actions (dates)
- Prescriptions acquired (history)
- Notifications sent (traceability)
- Recourse initiated (appeals)

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests**:
1. Verify prescription deadlines respected (10 years civil, 20 years penal)
2. Verify notifications sent (< 5 days)
3. Verify suspensions applied (fraud)
4. Verify complete registry (100% of damages)
5. Verify absence of fraud
6. Verify available recourse (appeal)
7. Verify immutable audit trail
8. Verify transparency (public registry)

**Frequency**: Minimum annual

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Prescription not respected | Immediate revocation | Immediate |
| Notification not sent | 15% annual revenue fine | 14 days |
| Suspension not applied | 20% annual revenue fine | 14 days |
| Incomplete registry | 10% annual revenue fine | 14 days |
| Fraud detected | License revocation | 7 days |
| Recourse refused | 15% annual revenue fine | 14 days |
| Audit trail modified | 25% annual revenue fine | 7 days |
| Recurrence | Permanent ban | Immediate |

### 5.3 Verification Process

1. Annual audit of deadlines (before December 31)
2. Notification verification (traceability)
3. Suspension verification (fraud)
4. Registry audit (completeness)
5. Recourse audit (availability)
6. Immutability audit (audit trail)
7. Public compliance report (open registry)
8. Violation notification (immediate)

---

## 6. EFFECTIVE DATE

**Effective date**: January 1, 2027

**Compliance calendar**:
- New agents: Mandatory compliance from deployment (0 days)
- Existing agents: Mandatory compliance before January 1, 2028 (9 months)
- Critical agents: Mandatory compliance before July 1, 2027 (3 months)

**Transitional provisions**:
- Prior damages: Deadlines recalculated under new rules
- Non-compliant agents: Suspension until compliance
- Notifications: Retroactive (minimum 6 months)

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS AGENTICA
- Article III.3.1: Civil Responsibility
- Article III.3.2: Penal Responsibility
- Article III.3.7: Victim Indemnification
- Chapter 12: Responsibility Paradigm
- The Cybernetic Criterion: Chapters 0-5

---


---

**Next review**: June 2026
