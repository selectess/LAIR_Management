---
title: "Article III.3.7: Victim Indemnification"
axiom: Ψ-III
article_number: III.3.7
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Indemnification
  - Victims
  - Compensation
  - Damages
  - Justice
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.7: VICTIM INDEMNIFICATION
## Axiom Ψ-III: RESPONSABILITAS JURIDICA

---

## 1. IMPERATIVE NORM

Every victim of damages caused by an autonomous agent MUST receive complete and rapid indemnification. Indemnification MUST cover all damages, including foreseeable future damages. The indemnification period MUST be minimal and not exceed 30 days.

**Minimum Requirements**:
- Complete and rapid indemnification (100% of damages)
- Coverage of all damages (direct, indirect, moral, future)
- Maximum period of 30 days (< 30 days)
- Late payment interest applicable (10% annual after 30 days)
- Recourse in case of refusal (appeal, revision)
- Automatic payment (without conditions)
- Immutable registry (traceability)
- Public transparency (open registry)
- Zero unjustified refusals
- Victim assistance (support)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS AGENTICA**

Rapid indemnification of victims is a fundamental moral and legal duty. No victim should wait long to receive compensation. Indemnification MUST be complete and cover all damages, without exception. This is the heart of agentic justice.

**Fundamental Principles** :
- Complete indemnification (100% of damages)
- Speed of process (< 30 days)
- Complete coverage (all types)
- Late payment interest (10% annual)
- Effective recourse (appeal, revision)
- Transparency (public registry)
- Justice (fairness for victims)
- Prevention (incentive for safety)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Indemnification Calculation

```python
class IndemnificationCalculator:
    def calculate_total_indemnification(self, victim_profile, damage_assessment):
        """Calculate total indemnification"""
        direct_damages = self.calculate_direct_damages(damage_assessment)
        indirect_damages = self.calculate_indirect_damages(damage_assessment)
        moral_damages = self.calculate_moral_damages(damage_assessment)
        future_damages = self.calculate_future_damages(damage_assessment)
        
        total = direct_damages + indirect_damages + moral_damages + future_damages
        
        # Apply late payment interest if applicable
        if damage_assessment.get('days_since_damage', 0) > 30:
            days_late = damage_assessment['days_since_damage'] - 30
            interest = total * 0.10 * (days_late / 365)
            total += interest
        
        return {
            'direct_damages': direct_damages,
            'indirect_damages': indirect_damages,
            'moral_damages': moral_damages,
            'future_damages': future_damages,
            'interest': interest if damage_assessment.get('days_since_damage', 0) > 30 else 0,
            'total_indemnification': total
        }
    
    def calculate_direct_damages(self, assessment):
        """Calculate direct damages"""
        return assessment.get('direct_amount', 0)
    
    def calculate_indirect_damages(self, assessment):
        """Calculate indirect damages"""
        lost_profit = assessment.get('lost_profit', 0)
        lost_opportunity = assessment.get('lost_opportunity', 0)
        
        return lost_profit + (lost_opportunity * 0.5)
    
    def calculate_moral_damages(self, assessment):
        """Calculate moral damages"""
        severity = assessment.get('moral_severity', 'moderate')
        
        base_amounts = {
            'minor': 1000,
            'moderate': 5000,
            'severe': 20000,
            'critical': 100000
        }
        
        return base_amounts.get(severity, 5000)
    
    def calculate_future_damages(self, assessment):
        """Calculate foreseeable future damages"""
        annual_loss = assessment.get('annual_loss', 0)
        years_affected = assessment.get('years_affected', 1)
        
        return annual_loss * years_affected
```

### 3.2 Indemnification Process

| Step | Deadline | Responsible |
|------|----------|------------|
| Indemnification request | 5 days | Victim |
| Damage assessment | 15 days | Authority |
| Indemnification calculation | 10 days | Authority |
| Approval | 5 days | Authority |
| Payment | 10 days | Agent/Deployer |
| **Total** | **45 days** | |

### 3.3 Payment Methods

- Bank transfer (preferred)
- Certified check
- Cash (for amounts <5000€)
- Life annuity (for permanent damages)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: TradeBot3000 ($45M)

**Incident** : Unauthorized position of $45M
**Direct damages** : $2.3M actual loss
**Indirect damages** : $450k liquidation fees
**Moral damages** : €100k (stress, loss of confidence)
**Future damages** : €200k (loss of income 2 years)
**Total indemnification** : $3.05M + €300k
**Payment deadline** : 15 days (compliant)
**Status** : Paid in full

### 4.2 Use Case: HealthBot (Incorrect Diagnosis)

**Incident** : Incorrect diagnosis causing unnecessary hospitalization
**Direct damages** : €45k medical fees
**Indirect damages** : €120k loss of income
**Moral damages** : €685k (suffering, trauma)
**Future damages** : €50k (medical follow-up 1 year)
**Total indemnification** : €900k
**Payment deadline** : 22 days (compliant)
**Status** : Paid in full

### 4.3 Reference Code (Rust)

```rust
use chrono::{DateTime, Utc, Duration};

pub struct IndemnificationRequest {
    pub request_id: String,
    pub victim_id: String,
    pub agent_id: String,
    pub incident_date: DateTime<Utc>,
    pub direct_damages: f64,
    pub indirect_damages: f64,
    pub moral_damages: f64,
    pub future_damages: f64,
}

impl IndemnificationRequest {
    pub fn calculate_total_indemnification(&self) -> f64 {
        self.direct_damages + self.indirect_damages + 
        self.moral_damages + self.future_damages
    }
    
    pub fn calculate_late_interest(&self, payment_date: DateTime<Utc>) -> f64 {
        let days_late = (payment_date - self.incident_date).num_days();
        
        if days_late > 30 {
            let excess_days = days_late - 30;
            let annual_rate = 0.10;
            self.calculate_total_indemnification() * annual_rate * (excess_days as f64 / 365.0)
        } else {
            0.0
        }
    }
    
    pub fn verify_payment_deadline(&self, payment_date: DateTime<Utc>) -> Result<(), String> {
        let deadline = self.incident_date + Duration::days(30);
        
        if payment_date > deadline {
            let days_late = (payment_date - deadline).num_days();
            Err(format!("Payment {} days late", days_late))
        } else {
            Ok(())
        }
    }
}
```

### 4.4 Indemnification Process

```
┌──────────────────────────────────────┐
│      Victim Requests Indemnification │
│      (Day 0)                         │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Assess Damages (5 days)             │
│  - Direct (invoices)                 │
│  - Indirect (loss of income)         │
│  - Moral (expertise)                 │
│  - Future (forecasts)                │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Calculate Indemnification (10 days) │
│  - Total amount                      │
│  - Late payment interest (if applic.)│
│  - Payment method                    │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Approve Indemnification (5 days)    │
│  - Verify calculation                │
│  - Verify completeness               │
│  - Issue payment order               │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Make Payment (< 10 days)            │
│  - Bank transfer                     │
│  - Payment confirmation              │
│  - Immutable logging                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Confirm Receipt (1 day)             │
│  - Victim confirms payment           │
│  - Case closure                      │
│  - Archiving (7 years)               │
└──────────────────────────────────────┘
```

### 4.5 Indemnification Registry

Each agent MUST maintain an immutable registry of :
- All indemnifications paid (100%)
- Amounts and dates (digital signature)
- Beneficiaries (verified identity)
- Justifications (complete documentation)
- Indemnification history (record)
- Late payment interest applied
- Recourse initiated

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests** :
1. Verify complete indemnification (100% of damages)
2. Verify 30-day deadline respected (< 30 days)
3. Verify late payment interest applied (10% annual)
4. Verify immutable indemnification registry
5. Verify no refused indemnifications
6. Verify complete documentation
7. Verify Transparency (public registry)
8. Verify available recourse

**Frequency** : Minimum quarterly

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction | Deadline |
|-----------|----------|----------|
| Refusal to indemnify | Immediate revocation, 30% CA fine | 7 days |
| Partial indemnification | Suspension, 20% CA fine | 7 days |
| Deadline exceeded | 15% CA fine + interest | 14 days |
| Interest not applied | 10% CA fine | 14 days |
| Incomplete registry | 5% CA fine | 14 days |
| Missing documentation | 10% CA fine | 14 days |
| Recourse refused | 15% CA fine | 14 days |
| Recurrence | Permanent ban | Immediate |

### 5.3 Verification Process

1. Quarterly audit of indemnifications
2. Deadline verification (< 30 days)
3. Interest verification (10% annual)
4. Registry audit (immutability)
5. Documentation audit (completeness)
6. Recourse audit (availability)
7. Public compliance report (open registry)
8. Violation notification (immediate)

---

## 6. EFFECTIVE DATE

**Effective date** : January 1, 2027

**Compliance calendar** :
- New agents : Compliance mandatory from deployment (0 days)
- Existing agents : Compliance mandatory before January 1, 2028 (9 months)
- Critical agents : Compliance mandatory before July 1, 2027 (3 months)

**Transitional provisions** :
- Ongoing indemnifications : Processing under new rules (< 30 days)
- Non-compliant agents : Suspension until compliance
- 60-day deadline → 30-day deadline : Progressive transition (6 months)

---

## REFERENCES

- Axiom Ψ-III : RESPONSABILITAS AGENTICA
- Article III.3.1 : Civil Responsibility
- Article III.3.3 : Mandatory Insurance
- Article III.3.5 : Damages and Repair
- Chapter 12 : Responsibility Paradigm
- The Cybernetic Criterion : Chapters 0-5

---

