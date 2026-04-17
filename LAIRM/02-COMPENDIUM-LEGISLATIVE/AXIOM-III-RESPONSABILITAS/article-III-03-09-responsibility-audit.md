---
title: "Article III.3.9: Responsibility Audit"
axiom: Ψ-III
article_number: III.3.9
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - audit
  - responsibility
  - verification
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.9: RESPONSIBILITY AUDIT
## Axiom Ψ-III: RESPONSABILITAS JURIDICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST be subject to regular Responsibility audits. Audits MUST verify compliance with all Responsibility obligations. Audit results must be public and immutable.

**Minimum Requirements**:
- Mandatory regular audits
- Complete compliance verification
- Public and immutable results
- Mandatory remediation
- Correction tracking

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS JURIDICA**

Regular auditing is the verification mechanism that agents comply with their Responsibility obligations. Without audit, Responsibility remains theoretical.

**Fundamental Principles**:
- Mandatory regular verification
- Transparency of results
- Immutability of reports
- Mandatory remediation
- Continuous monitoring

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Audit Types

```python
class ResponsibilityAudit:
    AUDIT_TYPES = {
        'internal': {
            'frequency': 'quarterly',
            'scope': 'Complete internal verification',
            'cost': 'Supported by agent'
        },
        'external': {
            'frequency': 'annual',
            'scope': 'Independent external audit',
            'cost': 'Supported by agent'
        },
        'citizen': {
            'frequency': 'on_demand',
            'scope': 'Citizen audit on demand',
            'cost': 'Free for citizens'
        },
        'emergency': {
            'frequency': 'as_needed',
            'scope': 'Emergency audit in case of incident',
            'cost': 'Supported by agent'
        }
    }
    
    def conduct_audit(self, agent_id, audit_type):
        """Conduct a Responsibility audit"""
        audit = {
            'audit_id': str(uuid.uuid4()),
            'agent_id': agent_id,
            'type': audit_type,
            'date': datetime.utcnow().isoformat(),
            'checks': self.perform_checks(agent_id),
            'status': 'completed'
        }
        
        return audit
    
    def perform_checks(self, agent_id):
        """Perform audit verifications"""
        return {
            'civil_liability': self.check_civil_liability(agent_id),
            'penal_liability': self.check_penal_liability(agent_id),
            'insurance': self.check_insurance(agent_id),
            'imputability': self.check_imputability(agent_id),
            'damages_repair': self.check_damages_repair(agent_id),
            'legal_recourse': self.check_legal_recourse(agent_id),
            'indemnification': self.check_indemnification(agent_id)
        }
```

### 3.2 Audit Frequency

| Audit Type | Frequency | Responsible |
|------------|-----------|------------|
| Internal | Quarterly | Agent |
| External | Annual | Independent Auditor |
| Citizen | On demand | Citizens |
| Emergency | Immediate | Authority |

### 3.3 Audit Criteria

Each audit MUST verify:
- Civil Responsibility established
- Penal Responsibility established
- Valid and sufficient insurance
- Imputability of actions
- Damage repair
- Available legal recourse
- Complete indemnification

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Audit Process

```
┌──────────────────────────────────────┐
│      Scheduled Audit                 │
│  - Internal (quarterly)              │
│  - External (annual)                 │
│  - Citizen (on demand)               │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Prepare Audit                       │
│  - Collect documents                 │
│  - Prepare data                      │
│  - Notify agent                      │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Perform Verifications               │
│  - Civil Responsibility              │
│  - Penal Responsibility              │
│  - Insurance                         │
│  - Imputability                      │
│  - Damages and repair                │
│  - Legal recourse                    │
│  - Indemnification                   │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Generate Report                     │
│  - Detailed results                  │
│  - Compliances and non-compliances   │
│  - Recommendations                   │
│  - Digital signature                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Publish Report                      │
│  - Public report                     │
│  - Immutable and signed              │
│  - Accessible to all                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Remediation                         │
│  - Agent corrects non-compliances    │
│  - Deadline: 30 days                 │
│  - Follow-up: follow-up audit        │
└──────────────────────────────────────┘
```

### 4.2 Audit Registry

Each agent MUST maintain an immutable registry of:
- All audits conducted
- Audit results
- Audit reports
- Corrections applied
- Follow-up audits

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests**:
1. Verify audits conducted regularly
2. Verify complete audit reports
3. Verify corrections applied
4. Verify audit registry
5. Verify transparency of results

**Frequency**: Minimum annual

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction |
|-----------|----------|
| Audit not conducted | Suspension, 20% annual revenue fine |
| Incomplete report | 15% annual revenue fine |
| Corrections not applied | Suspension, 25% annual revenue fine |
| Incomplete registry | 10% annual revenue fine |
| Results not public | 15% annual revenue fine |
| Recurrence | License revocation |

### 5.3 Verification Process

1. Annual audit of audits
2. Report verification
3. Correction verification
4. Registry audit
5. Public compliance report

---

## 6. EFFECTIVE DATE

**Effective date**: January 1, 2027

**Compliance calendar**:
- New agents: Mandatory audits from deployment
- Existing agents: Mandatory audits before January 1, 2028
- Critical agents: Mandatory audits before July 1, 2027

**Transitional provisions**:
- Agents without audits: Initial audit before June 30, 2027
- Deployers must establish systems before June 30, 2027

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS JURIDICA
- Article III.3.1: Civil Responsibility
- Article III.3.2: Penal Responsibility
- Chapter 12: Responsibility Paradigm

---

**Status**: Final


---

**Next review**: June 2026
