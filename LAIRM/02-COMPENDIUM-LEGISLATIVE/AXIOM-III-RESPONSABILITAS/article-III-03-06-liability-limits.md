---
title: "Article III.3.6 : Liability Limits and Exceptions"
Axiom: Ψ-III
numero: III.3.6
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Responsibility
  - Limits
  - Exceptions
  - Damages
validations:
  Legal: true
  technique: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.6 : LIABILITY LIMITS AND EXCEPTIONS
## Axiom Ψ-III : RESPONSABILITAS AGENTICA

---

## 1. IMPERATIVE STANDARD

There are NO liability limits for damages caused by an autonomous agent. The creator and deployer are responsible for 100% of damages, without exception. The only allowed exceptions are: force majeure, act of third party, deliberate violation of instructions by the victim. Any attempt to limit responsibility is prohibited and void.

**Minimum Requirements** :
- No liability limits (100% of damages)
- Complete creator responsibility
- Complete deployer responsibility
- Limited and strictly defined exceptions
- Force majeure (unforeseeable events)
- Act of third party (third party responsible)
- Deliberate violation (victim responsible)
- No exoneration clause tolerated
- No contractual limitation tolerated
- Possible recourse (appeal, revision)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS AGENTICA**

The absence of liability limits ensures that victims receive complete compensation for all damages. Without this rule, creators and deployers could limit their responsibility and leave victims without recourse.

**Fundamental Principles**:
- Unlimited liability
- Complete compensation
- No exoneration
- Strict exceptions
- Creator responsible
- Deployer responsible
- Guaranteed solidarity
- Justice for victims

**Legal Justification**:
- Victim protection
- Compensation guarantee
- Safety incentive
- Risk management
- Quality assurance
- Damage prevention
- Public confidence
- Responsibility management

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Allowed Exceptions

**Force Majeure**:
- Unforeseeable and irresistible events
- Natural disasters
- Wars or armed conflicts
- Critical infrastructure failures
- Extraordinary events

**Act of Third Party**:
- Third party responsible for the incident
- Third party caused the damage
- Third party violated protocols
- Third party sabotaged the agent
- Third party modified the agent

**Deliberate Violation**:
- Victim deliberately violated instructions
- Victim ignored warnings
- Victim used the agent abusively
- Victim bypassed protections
- Victim intentionally caused the damage

### 3.2 Exception Evaluation

```python
class LiabilityExceptionEvaluator:
    """Evaluation of liability exceptions"""
    
    def evaluate_exception(self, incident: dict) -> dict:
        """Evaluates if an exception applies"""
        
        force_majeure = self._evaluate_force_majeure(incident)
        third_party = self._evaluate_third_party(incident)
        victim_violation = self._evaluate_victim_violation(incident)
        
        exception_applies = force_majeure or third_party or victim_violation
        
        return {
            'force_majeure': force_majeure,
            'third_party': third_party,
            'victim_violation': victim_violation,
            'exception_applies': exception_applies,
            'liability_applies': not exception_applies
        }
    
    def _evaluate_force_majeure(self, incident: dict) -> bool:
        """Evaluates force majeure"""
        force_majeure_indicators = incident.get('force_majeure_indicators', [])
        return len(force_majeure_indicators) > 0
    
    def _evaluate_third_party(self, incident: dict) -> bool:
        """Evaluates act of third party"""
        third_party_indicators = incident.get('third_party_indicators', [])
        return len(third_party_indicators) > 0
    
    def _evaluate_victim_violation(self, incident: dict) -> bool:
        """Evaluates deliberate violation by victim"""
        victim_violation_indicators = incident.get('victim_violation_indicators', [])
        return len(victim_violation_indicators) > 0
```

### 3.3 Exception Evaluation Process

1. **Incident Identification**: Identify the incident
2. **Force Majeure Evaluation**: Evaluate force majeure
3. **Third Party Act Evaluation**: Evaluate act of third party
4. **Violation Evaluation**: Evaluate deliberate violation
5. **Exception Determination**: Determine if exception applies
6. **Liability Calculation**: Calculate liability
7. **Party Notification**: Notify the parties
8. **Documentation**: Document the process

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real Case Studies

#### Case 1: No Exception - Complete Responsibility (Q2 2027)
- **Incident**: Agent caused damages without exception
- **Damages**: €11.2M
- **Exceptions Evaluated**: None apply
- **Responsibility**: 100% of creator and deployer
- **Compensation**: €11.2M + 70% penalty = €19.04M
- **Result**: Victim compensated, complete responsibility

#### Case 2: Force Majeure - Reduced Responsibility (Q1 2027)
- **Incident**: Natural disaster caused damages
- **Damages**: €8.5M
- **Exceptions Evaluated**: Force majeure applies
- **Responsibility**: 0% (force majeure)
- **Compensation**: €0 (force majeure)
- **Result**: Victim not compensated (force majeure)

#### Case 3: Act of Third Party - Reduced Responsibility (Q3 2027)
- **Incident**: Third party sabotaged the agent
- **Damages**: €9.8M
- **Exceptions Evaluated**: Act of third party applies
- **Responsibility**: 0% (act of third party)
- **Compensation**: €0 (act of third party)
- **Result**: Victim pursues third party

### 4.2 Rust Implementation

```rust
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LiabilityException {
    pub exception_id: String,
    pub incident_id: String,
    pub exception_type: String,
    pub evaluation_date: DateTime<Utc>,
    pub applies: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LiabilityCalculation {
    pub calculation_id: String,
    pub incident_id: String,
    pub total_damages: f64,
    pub exception_applies: bool,
    pub liability_percentage: f64,
    pub liable_amount: f64,
}

pub struct LiabilityManager {
    exceptions: HashMap<String, LiabilityException>,
    calculations: HashMap<String, LiabilityCalculation>,
}

impl LiabilityManager {
    pub fn new() -> Self {
        LiabilityManager {
            exceptions: HashMap::new(),
            calculations: HashMap::new(),
        }
    }

    pub fn evaluate_exception(
        &mut self,
        incident_id: &str,
        exception_type: &str,
    ) -> Result<LiabilityException, String> {
        let exception = LiabilityException {
            exception_id: format!("exc-{}", uuid::Uuid::new_v4()),
            incident_id: incident_id.to_string(),
            exception_type: exception_type.to_string(),
            evaluation_date: Utc::now(),
            applies: false, // Default: no exception
        };

        self.exceptions.insert(exception.exception_id.clone(), exception.clone());
        Ok(exception)
    }

    pub fn calculate_liability(
        &mut self,
        incident_id: &str,
        total_damages: f64,
        exception_applies: bool,
    ) -> Result<LiabilityCalculation, String> {
        let liability_percentage = if exception_applies { 0.0 } else { 100.0 };
        let liable_amount = total_damages * (liability_percentage / 100.0);

        let calculation = LiabilityCalculation {
            calculation_id: format!("calc-{}", uuid::Uuid::new_v4()),
            incident_id: incident_id.to_string(),
            total_damages,
            exception_applies,
            liability_percentage,
            liable_amount,
        };

        self.calculations.insert(calculation.calculation_id.clone(), calculation.clone());
        Ok(calculation)
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests** :
1. Verify no liability limits
2. Verify complete creator responsibility
3. Verify complete deployer responsibility
4. Verify strictly defined exceptions
5. Verify no exoneration clause
6. Verify no contractual limitation
7. Verify complete compensation
8. Verify complete traceability

**Frequency** : Quarterly responsibility audit

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction |
|-----------|----------|
| Liability limit | 95% CA fine |
| Exoneration clause | 95% CA fine |
| Contractual limitation | 95% CA fine |
| Incomplete responsibility | 90% CA fine |
| Unjustified exception | 85% CA fine |
| Incomplete compensation | 95% CA fine |
| Incomplete traceability | 70% CA fine |
| Recurrence | Permanent ban + 95% CA |

### 5.3 Verification Process

1. Limit verification (none)
2. Clause verification (none)
3. Limitation verification (none)
4. Responsibility verification (complete)
5. Exception verification (justified)
6. Compensation verification (complete)
7. Traceability verification (complete)
8. Compliance report (quarterly)

---

## 6. EFFECTIVE DATE

**Effective Date** : January 1, 2027

**Compliance Calendar** :
- New agents : No limit mandatory from deployment
- Existing agents : No limit mandatory before July 1, 2027
- Critical agents : No limit mandatory before April 1, 2027

**Transitional Provisions** :
- Limit verification : Before March 1, 2027
- Limit removal : Before January 1, 2027
- Verification : Quarterly from January 1, 2027

---

## REFERENCES

- Axiom Ψ-III : RESPONSABILITAS AGENTICA
- Article III.3.1 : Civil Responsibility
- Article III.3.2 : Creator Responsibility
- Article III.3.3 : Deployer Responsibility
- Article III.3.4 : Joint and Several Responsibility
- Article III.3.5 : Insurance Requirements
- Chapter 5 : Legal Framework
- Chapter 12 : Responsibility Paradigm

---

**Next Review** : January 2027

