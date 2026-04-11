---
title: "Article III.3.1 : Civil Responsibility"
Axiom: Ψ-III
numero: III.3.1
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Responsibility
  - Civil
  - Damages
  - Compensation
  - Legality
validations:
  Legal: true
  technique: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.1 : CIVIL RESPONSIBILITY
## Axiom Ψ-III : RESPONSABILITAS AGENTICA

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST be civilly responsible for all damages it causes. Civil responsibility MUST cover: material damages, immaterial damages, financial losses, moral prejudice. Creator and deployer are jointly and severally liable.

**Minimum Requirements** :
- Mandatory civil responsibility (100% of damages)
- Insurance coverage (minimum 10M EUR)
- Creator responsibility (joint and several)
- Deployer responsibility (joint and several)
- Prescription period: 5 years
- Automatic compensation (< 30 days)
- Guarantee fund (for insolvency)
- Complete audit trail (traceability)
- Public transparency (open registry)
- Possible recourse (appeal, revision)

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III : RESPONSABILITAS AGENTICA**

Civil responsibility is the foundation of agent justice. Without civil responsibility, victims have no recourse. Civil responsibility ensures that each agent can be held responsible for its actions and that victims can be compensated.

**Fundamental Principles** :
- Absolute responsibility (no exception)
- Solidarity (creator + deployer)
- Complete compensation (all damages)
- Speed (< 30 days)
- Transparency (public registry)
- Legality (compliant with law)
- Justice (equity for victims)
- Prevention (incentive for safety)

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Types of Damages

**Material Damages** :
- Destruction of property
- Data loss
- System damage
- Repair costs

**Immaterial Damages** :
- Financial losses
- Loss of income
- Replacement costs
- Litigation costs

**Moral Prejudice** :
- Physical suffering
- Psychological suffering
- Reputation damage
- Rights violation

### 3.2 Compensation Calculation

```python
class CivilLiabilityCalculator:
    """Civil liability calculator"""
    
    def calculate_damages(self, incident: dict) -> dict:
        """Calculates total damages"""
        
        material_damages = self._calculate_material_damages(incident)
        immaterial_damages = self._calculate_immaterial_damages(incident)
        moral_damages = self._calculate_moral_damages(incident)
        
        total_damages = material_damages + immaterial_damages + moral_damages
        
        return {
            'material_damages': material_damages,
            'immaterial_damages': immaterial_damages,
            'moral_damages': moral_damages,
            'total_damages': total_damages,
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def _calculate_material_damages(self, incident: dict) -> float:
        """Calculates material damages"""
        return incident.get('material_loss', 0)
    
    def _calculate_immaterial_damages(self, incident: dict) -> float:
        """Calculates immaterial damages"""
        return incident.get('financial_loss', 0)
    
    def _calculate_moral_damages(self, incident: dict) -> float:
        """Calculates moral prejudice"""
        return incident.get('moral_damage', 0)
```

### 3.3 Compensation Process

```
┌─────────────────────────────────────┐
│     Incident Reported               │
│     (Victim reports)                │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Damages Assessment              │
│     (Independent expert)            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Compensation Calculation        │
│     (Legal formula)                 │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     Payment (< 30 days)             │
│     (Insurance or fund)             │
└─────────────────────────────────────┘
```

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Use Case: TradeBot3000 ($45M)

**Incident** : Unauthorized position of $45M
**Damages** : $2.3M actual loss
**Compensation** : $2.3M + costs
**Timeline** : 15 days
**Next Review** : January 2027

