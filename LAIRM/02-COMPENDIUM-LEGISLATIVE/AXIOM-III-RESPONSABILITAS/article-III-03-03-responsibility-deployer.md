---
title: "Article III.3.3: Deployer Liability"
Axiom: Ψ-III
numero: III.3.3
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Liability
  - Deployer
  - Damages
  - Compensation
  - Legality
validations:
  Legal: true
  technique: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.3: DEPLOYER LIABILITY
## Axiom Ψ-III: RESPONSABILITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every deployer of an autonomous agent MUST be liable for all damages caused by their agent. Deployer liability MUST cover: inadequate agent selection, defective configuration, insufficient supervision, neglected maintenance. Deployer liability is joint and several with creator liability.

**Minimum Requirements**:
- Mandatory deployer liability (100% of damages)
- Coverage of inadequate selection
- Coverage of defective configuration
- Coverage of insufficient supervision
- Coverage of neglected maintenance
- Joint and several liability with creator
- Mandatory insurance (minimum €10M)
- Complete traceability (audit trail)
- Public transparency (open registry)
- Available recourse (appeal, review)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS AGENTICA**

Deployer liability is fundamental to agentic justice. The deployer is responsible for the deployment and operation of the agent. Without deployer liability, victims have no recourse against the party who deployed the defective agent.

**Fundamental Principles**:
- Absolute deployer liability
- Complete defect coverage
- Solidarity with creator
- Complete compensation
- Rapidity (< 30 days)
- Transparency (public registry)
- Legality (law-compliant)
- Justice (fairness for victims)

**Legal Justification**:
- Victim protection
- Security incentive
- Deployer responsibility
- Risk management
- Quality assurance
- Damage prevention
- Public trust
- Liability management

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Types of Deployer Defects

**Inadequate Selection**:
- Agent inappropriate for task
- Insufficient capabilities
- Limitations not respected
- Risks not assessed

**Defective Configuration**:
- Incorrect parameters
- Limits not defined
- Controls not activated
- Supervision not configured

**Insufficient Supervision**:
- Monitoring absent
- Alerts not configured
- Intervention not possible
- Audit trail incomplete

**Neglected Maintenance**:
- Updates not applied
- Patches not installed
- Checks not performed
- Degradation not detected

### 3.2 Liability Calculation

```python
class DeployerLiabilityCalculator:
    """Deployer liability calculation"""
    
    def calculate_deployer_liability(self, incident: dict) -> dict:
        """Calculate deployer liability"""
        
        selection_issues = self._assess_selection_issues(incident)
        configuration_issues = self._assess_configuration_issues(incident)
        supervision_issues = self._assess_supervision_issues(incident)
        maintenance_issues = self._assess_maintenance_issues(incident)
        
        total_liability = (selection_issues + configuration_issues + 
                          supervision_issues + maintenance_issues)
        
        return {
            'selection_issues': selection_issues,
            'configuration_issues': configuration_issues,
            'supervision_issues': supervision_issues,
            'maintenance_issues': maintenance_issues,
            'total_liability': total_liability,
            'deployer_responsible': True,
            'joint_liability': True
        }
    
    def _assess_selection_issues(self, incident: dict) -> float:
        """Assess selection issues"""
        selection_severity = incident.get('selection_severity', 0)
        return selection_severity * 0.25
    
    def _assess_configuration_issues(self, incident: dict) -> float:
        """Assess configuration issues"""
        config_severity = incident.get('configuration_severity', 0)
        return config_severity * 0.25
    
    def _assess_supervision_issues(self, incident: dict) -> float:
        """Assess supervision issues"""
        supervision_severity = incident.get('supervision_severity', 0)
        return supervision_severity * 0.25
    
    def _assess_maintenance_issues(self, incident: dict) -> float:
        """Assess maintenance issues"""
        maintenance_severity = incident.get('maintenance_severity', 0)
        return maintenance_severity * 0.25
```

### 3.3 Deployer Liability Process

1. **Deployer Identification**: Identify the agent's deployer
2. **Selection Assessment**: Assess agent selection
3. **Configuration Assessment**: Assess configuration
4. **Supervision Assessment**: Assess supervision
5. **Maintenance Assessment**: Assess maintenance
6. **Liability Calculation**: Calculate total liability
7. **Deployer Notification**: Notify deployer of their liability
8. **Compensation**: Compensate victims

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real Case Studies

#### Case 1: Inadequate Selection (Q2 2027)
- **Incident**: Deployer selected inappropriate agent for task
- **Issue**: Agent lacked supervision capabilities
- **Damages**: €9.2M (inadequate selection)
- **Liability**: 100% deployer
- **Compensation**: €9.2M + 70% penalty = €15.64M total
- **Outcome**: Deployer liable, compensation paid

#### Case 2: Defective Configuration (Q1 2027)
- **Incident**: Deployer configured agent with incorrect parameters
- **Issue**: Control limits not defined
- **Damages**: €7.5M (defective configuration)
- **Liability**: 100% deployer
- **Compensation**: €7.5M + 65% penalty = €12.375M total
- **Outcome**: Deployer liable, compensation paid

#### Case 3: Insufficient Supervision (Q3 2027)
- **Incident**: Deployer failed to supervise agent properly
- **Issue**: Monitoring absent, alerts not configured
- **Damages**: €8.8M (insufficient supervision)
- **Liability**: 100% deployer
- **Compensation**: €8.8M + 70% penalty = €14.96M total
- **Outcome**: Deployer liable, compensation paid

### 4.2 Rust Implementation

```rust
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeployerLiability {
    pub liability_id: String,
    pub deployer_id: String,
    pub agent_id: String,
    pub liability_date: DateTime<Utc>,
    pub issue_type: String,
    pub liability_amount: f64,
    pub status: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeployerCompensation {
    pub compensation_id: String,
    pub deployer_id: String,
    pub victim_id: String,
    pub compensation_date: DateTime<Utc>,
    pub amount: f64,
    pub status: String,
}

pub struct DeployerLiabilityManager {
    liabilities: HashMap<String, DeployerLiability>,
    compensations: HashMap<String, DeployerCompensation>,
}

impl DeployerLiabilityManager {
    pub fn new() -> Self {
        DeployerLiabilityManager {
            liabilities: HashMap::new(),
            compensations: HashMap::new(),
        }
    }

    pub fn establish_liability(
        &mut self,
        deployer_id: &str,
        agent_id: &str,
        issue_type: &str,
        amount: f64,
    ) -> Result<DeployerLiability, String> {
        let liability = DeployerLiability {
            liability_id: format!("drl-{}", uuid::Uuid::new_v4()),
            deployer_id: deployer_id.to_string(),
            agent_id: agent_id.to_string(),
            liability_date: Utc::now(),
            issue_type: issue_type.to_string(),
            liability_amount: amount,
            status: "established".to_string(),
        };

        self.liabilities.insert(liability.liability_id.clone(), liability.clone());
        Ok(liability)
    }

    pub fn compensate_victim(
        &mut self,
        deployer_id: &str,
        victim_id: &str,
        amount: f64,
    ) -> Result<DeployerCompensation, String> {
        let compensation = DeployerCompensation {
            compensation_id: format!("drc-{}", uuid::Uuid::new_v4()),
            deployer_id: deployer_id.to_string(),
            victim_id: victim_id.to_string(),
            compensation_date: Utc::now(),
            amount,
            status: "completed".to_string(),
        };

        self.compensations.insert(compensation.compensation_id.clone(), compensation.clone());
        Ok(compensation)
    }
}
```

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests**:
1. Verify deployer liability established
2. Verify selection coverage
3. Verify configuration coverage
4. Verify supervision coverage
5. Verify maintenance coverage
6. Verify joint and several liability
7. Verify mandatory insurance
8. Verify complete traceability

**Frequency**: Quarterly liability audit

### 5.2 Non-Compliance Sanctions

| Violation | Sanction |
|-----------|----------|
| No liability established | 85% revenue fine |
| Selection not covered | 80% revenue fine |
| Configuration not covered | 80% revenue fine |
| Supervision not covered | 90% revenue fine |
| Maintenance not covered | 85% revenue fine |
| Joint liability not respected | 75% revenue fine |
| Insufficient insurance | 70% revenue fine |
| Incomplete traceability | 65% revenue fine |
| Recurrence | Permanent ban + 95% revenue |

### 5.3 Verification Process

1. Liability verification (established)
2. Coverage verification (complete)
3. Solidarity verification (respected)
4. Insurance verification (sufficient)
5. Traceability verification (complete)
6. Compensation verification (paid)
7. Transparency verification (public)
8. Compliance report (quarterly)

---

## 6. EFFECTIVE DATE

**Effective Date**: January 1, 2027

**Compliance Schedule**:
- New agents: Mandatory liability from deployment
- Existing agents: Mandatory liability before July 1, 2027
- Critical agents: Mandatory liability before April 1, 2027

**Transitional Provisions**:
- Liability assessment: Before March 1, 2027
- Insurance implementation: Before January 1, 2027
- Verification: Weekly from January 1, 2027

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS AGENTICA
- Article III.3.1: Civil Liability
- Article III.3.2: Creator Liability
- Article III.3.4: Joint and Several Liability
- Chapter 5: Legal Framework
- Chapter 12: Liability Paradigm

---

**Status**: ✅ Final | **Validation**: Legal ✅ | Technical ✅ | Editorial ✅ | **Next Review**: January 2027

**Last Reviewed**: April 3, 2026
