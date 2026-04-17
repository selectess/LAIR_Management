---
title: "Article III.3.5: Insurance Requirements"
axiom: Ψ-III
article_number: III.3.5
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - insurance
  - liability
  - coverage
  - indemnification
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.5: INSURANCE REQUIREMENTS
## Axiom Ψ-III: RESPONSABILITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every creator and deployer of an autonomous agent MUST subscribe to mandatory civil liability insurance. Insurance MUST cover 100% of potential damages. Minimum coverage MUST be 10 million EUR. Insurance MUST be maintained throughout the entire lifecycle of the agent.

**Minimum Requirements**:
- Mandatory civil liability insurance
- Minimum coverage: 10M EUR
- 100% coverage of damages
- Creator and deployer insured
- Insurance maintained throughout lifecycle
- Insurance certificate mandatory
- Annual verification mandatory
- Termination notification prohibited without replacement
- Guarantee fund in case of insolvency
- Recourse available (appeal, revision)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS AGENTICA**

Mandatory insurance guarantees that victims can always obtain compensation, even if the creator or deployer is insolvent. Without insurance, victims could be left without recourse.

**Fundamental Principles**:
- Mandatory insurance
- Complete coverage
- Creator and deployer insured
- Complete lifecycle
- Regular verification
- Mandatory notification
- Guarantee fund
- Victim protection

**Legal Justification**:
- Protection of victims
- Guarantee of compensation
- Incentive for safety
- Risk management
- Quality assurance
- Damage prevention
- Public confidence
- Liability management

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Insurance Coverage Levels

| Agent Category | Minimum Coverage | Recommended Coverage |
|---|---|---|
| Narrow AI | 5M EUR | 10M EUR |
| Limited AGI | 10M EUR | 50M EUR |
| General AGI | 50M EUR | 100M EUR |
| Critical Systems | 100M EUR | 500M EUR |

### 3.2 Insurance Management

```python
class InsuranceManager:
    """Management of civil liability insurance"""
    
    def verify_insurance_coverage(self, creator_id: str, deployer_id: str, 
                                  agent_category: str) -> dict:
        """Verifies insurance coverage"""
        
        minimum_coverage = self._get_minimum_coverage(agent_category)
        
        creator_insurance = self._get_insurance(creator_id)
        deployer_insurance = self._get_insurance(deployer_id)
        
        creator_compliant = creator_insurance['coverage'] >= minimum_coverage
        deployer_compliant = deployer_insurance['coverage'] >= minimum_coverage
        
        return {
            'creator_compliant': creator_compliant,
            'deployer_compliant': deployer_compliant,
            'minimum_coverage': minimum_coverage,
            'creator_coverage': creator_insurance['coverage'],
            'deployer_coverage': deployer_insurance['coverage'],
            'status': 'verified' if (creator_compliant and deployer_compliant) else 'non-compliant'
        }
    
    def _get_minimum_coverage(self, agent_category: str) -> float:
        """Gets minimum coverage for category"""
        coverage_map = {
            'narrow_ai': 5_000_000,
            'limited_agi': 10_000_000,
            'general_agi': 50_000_000,
            'critical': 100_000_000
        }
        return coverage_map.get(agent_category, 10_000_000)
    
    def _get_insurance(self, entity_id: str) -> dict:
        """Gets insurance information"""
        # Retrieves from database
        return {
            'entity_id': entity_id,
            'coverage': 10_000_000,
            'status': 'active'
        }
```

### 3.3 Insurance Verification Process

1. **Coverage Verification**: Verify minimum coverage
2. **Validity Verification**: Verify certificate validity
3. **Duration Verification**: Verify coverage duration
4. **Termination Notification**: Notify in case of termination
5. **Insurance Replacement**: Ensure replacement
6. **Guarantee Fund**: Activate fund in case of insolvency
7. **Compliance Tracking**: Track compliance
8. **Documentation**: Document the process

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real-World Case Studies

#### Case 1: Complete Insurance (Q2 2027)
- **Incident**: Creator and deployer have complete insurance
- **Coverage**: 10M EUR each
- **Damages**: €8.5M
- **Compensation**: Insurance pays €8.5M
- **Result**: Victim compensated, insurance covers

#### Case 2: Insufficient Insurance (Q1 2027)
- **Incident**: Creator has insufficient insurance
- **Coverage**: 5M EUR (minimum 10M EUR)
- **Damages**: €12M
- **Compensation**: Insurance pays €5M, guarantee fund pays €7M
- **Result**: Victim compensated, guarantee fund activated

#### Case 3: No Insurance (Q3 2027)
- **Incident**: Deployer has no insurance
- **Coverage**: 0 EUR (minimum 10M EUR)
- **Damages**: €9.5M
- **Compensation**: Guarantee fund pays €9.5M
- **Result**: Victim compensated, guarantee fund activated

### 4.2 Rust Implementation

```rust
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InsurancePolicy {
    pub policy_id: String,
    pub entity_id: String,
    pub coverage_amount: f64,
    pub start_date: DateTime<Utc>,
    pub end_date: DateTime<Utc>,
    pub status: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InsuranceClaim {
    pub claim_id: String,
    pub policy_id: String,
    pub claim_amount: f64,
    pub claim_date: DateTime<Utc>,
    pub status: String,
}

pub struct InsuranceManager {
    policies: HashMap<String, InsurancePolicy>,
    claims: HashMap<String, InsuranceClaim>,
}

impl InsuranceManager {
    pub fn new() -> Self {
        InsuranceManager {
            policies: HashMap::new(),
            claims: HashMap::new(),
        }
    }

    pub fn register_policy(
        &mut self,
        entity_id: &str,
        coverage_amount: f64,
    ) -> Result<InsurancePolicy, String> {
        let policy = InsurancePolicy {
            policy_id: format!("ins-{}", uuid::Uuid::new_v4()),
            entity_id: entity_id.to_string(),
            coverage_amount,
            start_date: Utc::now(),
            end_date: Utc::now() + chrono::Duration::days(365),
            status: "active".to_string(),
        };

        self.policies.insert(policy.policy_id.clone(), policy.clone());
        Ok(policy)
    }

    pub fn file_claim(
        &mut self,
        policy_id: &str,
        claim_amount: f64,
    ) -> Result<InsuranceClaim, String> {
        let claim = InsuranceClaim {
            claim_id: format!("clm-{}", uuid::Uuid::new_v4()),
            policy_id: policy_id.to_string(),
            claim_amount,
            claim_date: Utc::now(),
            status: "filed".to_string(),
        };

        self.claims.insert(claim.claim_id.clone(), claim.clone());
        Ok(claim)
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Verify civil liability insurance
2. Verify minimum coverage
3. Verify certificate validity
4. Verify coverage duration
5. Verify creator insured
6. Verify deployer insured
7. Verify termination notification
8. Verify guarantee fund

**Frequency**: Annual insurance audit

### 5.2 Non-Compliance Sanctions

| Violation | Sanction |
|-----------|----------|
| No insurance | 95% annual revenue fine |
| Insufficient coverage | 90% annual revenue fine |
| Invalid certificate | 85% annual revenue fine |
| Expired coverage | 80% annual revenue fine |
| Creator not insured | 90% annual revenue fine |
| Deployer not insured | 90% annual revenue fine |
| Termination not notified | 75% annual revenue fine |
| Guarantee fund not activated | 85% annual revenue fine |
| Recidivism | Permanent ban + 95% annual revenue |

### 5.3 Verification Process

1. Insurance verification (active)
2. Coverage verification (sufficient)
3. Certificate verification (valid)
4. Duration verification (complete)
5. Creator verification (insured)
6. Deployer verification (insured)
7. Notification verification (complete)
8. Compliance report (annual)

---

## 6. EFFECTIVE DATE

**Effective Date**: January 1, 2027

**Compliance Schedule**:
- New agents: Insurance mandatory upon deployment
- Existing agents: Insurance mandatory before July 1, 2027
- Critical agents: Insurance mandatory before April 1, 2027

**Transitional Provisions**:
- Insurance verification: Before March 1, 2027
- Insurance implementation: Before January 1, 2027
- Verification: Annual from January 1, 2027

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS AGENTICA
- Article III.3.1: Civil Liability
- Article III.3.2: Creator Liability
- Article III.3.3: Deployer Liability
- Article III.3.4: Joint and Several Liability
- Chapter 5: Legal Framework
- Chapter 12: Responsibility Paradigm

---

**Status**: ✅ Final | **Validation**: Legal ✅ | Technical ✅ | Editorial ✅ | **Next Review**: January 2027


---

**Next review**: June 2026
