---
title: "Article III.3.13: Deployer Recourse"
axiom: Ψ-III
article_number: III.3.13
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - recourse
  - deployer
  - responsibility
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.13: DEPLOYER RECOURSE
## Axiom Ψ-III: RESPONSABILITAS JURIDICA

---

## 1. IMPERATIVE NORM

The deployer of an autonomous agent must be responsible for damages caused by that agent. Victims MUST have recourse against the deployer in case of supervision failure, maintenance failure, or deployment failure. The Responsibility of the deployer MUST be clearly established.

**Minimum Requirements**:
- Deployer Responsibility established
- Recourse against deployer possible
- Deployer imputability
- Mandatory deployer insurance
- Right to complete redress

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS JURIDICA**

The deployer is responsible for supervision and maintenance of the agent. Failures in supervision or maintenance engage the Responsibility of the deployer.

**Fundamental Principles**:
- Deployer Responsibility
- Mandatory supervision
- Mandatory maintenance
- Established imputability
- Effective recourse

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Deployer Responsibility

```python
class DeployerResponsibility:
    RESPONSIBILITY_TYPES = {
        'supervision_failure': {
            'description': 'Supervision failure',
            'deployer_liability': 0.60,
            'agent_liability': 0.40
        },
        'maintenance_failure': {
            'description': 'Maintenance failure',
            'deployer_liability': 0.70,
            'agent_liability': 0.30
        },
        'deployment_failure': {
            'description': 'Deployment failure',
            'deployer_liability': 0.80,
            'agent_liability': 0.20
        },
        'training_failure': {
            'description': 'Training failure',
            'deployer_liability': 0.75,
            'agent_liability': 0.25
        }
    }
    
    def calculate_deployer_liability(self, failure_type, total_damages):
        """Calculate deployer Responsibility"""
        if failure_type not in self.RESPONSIBILITY_TYPES:
            raise ValueError(f"Unknown failure type: {failure_type}")
        
        liability_rate = self.RESPONSIBILITY_TYPES[failure_type]['deployer_liability']
        deployer_liability = total_damages * liability_rate
        
        return {
            'failure_type': failure_type,
            'total_damages': total_damages,
            'deployer_liability': deployer_liability,
            'agent_liability': total_damages - deployer_liability
        }
```

### 3.2 Deployer Responsibility Criteria

| Criterion | Responsibility |
|-----------|----------------|
| Insufficient supervision | 60% |
| Insufficient maintenance | 70% |
| Defective deployment | 80% |
| Insufficient training | 75% |
| Inadequate agent selection | 85% |

### 3.3 Recourse Against Deployer

Victims MUST be able to:
- Pursue the deployer directly
- Obtain redress from the deployer
- Access deployer insurance
- Request damages and interest
- Obtain late payment interest

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Recourse Process

```
┌──────────────────────────────────────┐
│      Damage Caused by Agent          │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Identify Deployer Failure           │
│  - Insufficient supervision          │
│  - Insufficient maintenance          │
│  - Defective deployment              │
│  - Insufficient training             │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Calculate Responsibility            │
│  - Deployer Responsibility           │
│  - Agent Responsibility              │
│  - Respective amounts                │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Pursue Deployer                     │
│  - Legal action                      │
│  - Indemnification request           │
│  - Access to insurance               │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Obtain Redress                      │
│  - Amount per Responsibility         │
│  - Late payment interest             │
│  - Damages and interest              │
└──────────────────────────────────────┘
```

### 4.2 Deployer Responsibility Registry

Each deployer MUST maintain an immutable registry of:
- All damages caused by its agents
- Established responsibilities
- Repairs performed
- Subscribed insurance
- Responsibility history

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests**:
1. Verify deployer Responsibility established
2. Verify recourse against deployer possible
3. Verify deployer insurance
4. Verify Responsibility registry
5. Verify repairs performed

**Frequency**: Minimum annual

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction |
|-----------|----------|
| Responsibility not established | 20% annual revenue fine |
| Recourse refused | 25% annual revenue fine |
| Insufficient insurance | Suspension, 20% annual revenue fine |
| Incomplete registry | 10% annual revenue fine |
| Repairs not performed | License revocation |
| Recurrence | Permanent ban |

### 5.3 Verification Process

1. Annual Responsibility audit
2. Recourse verification
3. Insurance verification
4. Registry audit
5. Public compliance report

---

## 6. EFFECTIVE DATE

**Effective date**: January 1, 2027

**Compliance calendar**:
- New deployers: Mandatory compliance from deployment
- Existing deployers: Mandatory compliance before January 1, 2028
- Critical deployers: Mandatory compliance before July 1, 2027

**Transitional provisions**:
- Prior damages: Recourse under new rules
- Non-compliant deployers: Suspension until compliance

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS JURIDICA
- Article III.3.1: Civil Responsibility
- Article III.3.4: Direct Imputability
- Chapter 12: Responsibility Paradigm

---

**Status**: Final


---

**Next review**: June 2026
