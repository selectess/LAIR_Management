---
title: "Article III.3.11 : Prescription et Délais"
Axiom: Ψ-III
numero: III.3.11
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - Prescription
  - Délais
  - Procédure
  - Justice
  - Recours
validations:
  Legal: true
  technique: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.11 : PRESCRIPTION ET DÉLAIS
## Axiom Ψ-III : RESPONSABILITAS JURIDICA

---

## 1. NORME IMPÉRATIVE

Les délais de prescription pour les actions en Responsibility contre un agent autonome must be suffisamment longs pour permettre aux victimes d'obtenir réparation. La prescription DOIT être suspendue en cas de fraude ou de dissimulation. Les délais must be clairs, immuables, et notifiés aux victimes.

**Exigences minimales** :
- Délai de prescription de 10 ans minimum (Responsibility civile)
- Délai de prescription de 20 ans (Responsibility pénale)
- Suspension en cas de fraude (illimité)
- Délais clairs et immuables (notification obligatoire)
- Notification obligatoire des délais (à la victime)
- Recours en cas de dépassement (appel)
- Registre immuable (traçabilité)
- Transparency publique (registre ouvert)
- Zéro prescription non-justifiée
- Assistance aux victimes (support)

---

## 2. FONDEMENT Legal

**Axiom Ψ-III : RESPONSABILITAS AGENTICA**

Les délais de prescription must be suffisamment longs pour permettre aux victimes de découvrir les dommages et d'obtenir réparation. Un délai trop court rendrait la Responsibility illusoire. La suspension en cas de fraude garantit que les victimes ne sont pas pénalisées par la dissimulation.

**Fundamental Principles** :
- Délais suffisamment longs (10-20 ans)
- Suspension en cas de fraude (illimité)
- Clarté des délais (notification)
- Notification obligatoire (à la victime)
- Recours effectif (appel, révision)
- Transparency (registre public)
- Justice (équité pour les victimes)
- Prévention (dissuasion)

---

## 3. SPÉCIFICATION TECHNIQUE

### 3.1 Délais de Prescription

```python
class PrescriptionPeriod:
    PERIODS = {
        'civil_liability': 10,  # ans
        'penal_liability': 20,  # ans
        'discovery_rule': 3,    # ans après découverte
        'fraud_suspension': None  # illimité
    }
    
    def calculate_prescription_deadline(self, damage_date, damage_type):
        """Calcule la Date limite de prescription"""
        if damage_type == 'fraud':
            return None  # Pas de prescription
        
        period = self.PERIODS.get(damage_type, 10)
        deadline = damage_date + timedelta(days=period*365)
        
        return deadline
    
    def check_prescription_status(self, damage_date, damage_type, current_date):
        """Vérifie le Status de prescription"""
        deadline = self.calculate_prescription_deadline(damage_date, damage_type)
        
        if deadline is None:
            return 'no_prescription'
        
        if current_date > deadline:
            return 'prescribed'
        else:
            days_remaining = (deadline - current_date).days
            return f'active_{days_remaining}_days'
```

### 3.2 Délais par type de Dommage

| type de Dommage | Délai | Suspension |
|-----------------|-------|-----------|
| Responsibility civile | 10 ans | Fraude |
| Responsibility pénale | 20 ans | Fraude |
| Découverte tardive | 3 ans après découverte | Fraude |
| Fraude | Illimité | N/A |

### 3.3 Suspension de Prescription

La prescription DOIT être suspendue en cas de :
- Fraude ou dissimulation
- Reconnaissance de Responsibility
- Action en justice engagée
- Demande d'indemnisation formelle

---

## 4. IMPLÉMENTATION RÉFÉRENCE

### 4.1 Cas d'Usage : TradeBot3000 ($45M)

**Incident** : Position non-autorisée de $45M
**Date du dommage** : 2026-01-15
**Découverte** : 2026-01-16 (1 jour)
**Délai civil** : 10 ans (2036-01-15)
**Délai pénal** : 20 ans (2046-01-15)
**Suspension** : Non (pas de fraude)
**Status** : Actif (prescription en cours)

### 4.2 Cas d'Usage : HealthBot (Diagnostic Erroné)

**Incident** : Diagnostic erroné causant hospitalisation
**Date du dommage** : 2026-02-20
**Découverte** : 2026-03-15 (23 jours)
**Délai civil** : 10 ans (2036-02-20)
**Délai pénal** : 20 ans (2046-02-20)
**Suspension** : Oui (fraude détectée 2026-04-01)
**Status** : Suspendu (illimité)

### 4.3 Code de Référence (Rust)

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

### 4.4 Gestion des Délais

```
┌──────────────────────────────────────┐
│      Dommage Causé                   │
│      Date: T0                        │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Calculer Deadline de Prescription   │
│  - type de dommage                   │
│  - Délai applicable (10 ou 20 ans)   │
│  - Date limite: T0 + délai           │
│  - Délai: < 1 jour                   │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Notifier Victime (< 5 jours)        │
│  - Délai de prescription             │
│  - Date limite exacte                │
│  - Droits de la victime              │
│  - Recours disponibles               │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Monitorer Délai (continu)           │
│  - Vérifier suspension               │
│  - Alerter avant expiration (30j)    │
│  - Enregistrer actions               │
│  - Audit trail immuable              │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  À la Date Limite                    │
│  - Prescription acquise              │
│  - Ou action en justice engagée      │
│  - Ou suspension appliquée           │
│  - Notification finale               │
└──────────────────────────────────────┘
```

### 4.5 Registre de Prescription

Each agent DOIT maintenir un registre immuable de :
- Tous les dommages et dates (100%)
- Délais de prescription (civil + pénal)
- Suspensions appliquées (fraude)
- Actions en justice (dates)
- Prescriptions acquises (historique)
- Notifications envoyées (traçabilité)
- Recours engagés (appels)

---

## 5. VÉRIFICATION & SANCTIONS

### 5.1 Vérification de Conformité

**Tests obligatoires** :
1. Vérifier délais de prescription respectés (10 ans civil, 20 ans pénal)
2. Vérifier notifications envoyées (< 5 jours)
3. Vérifier suspensions appliquées (fraude)
4. Vérifier registre complet (100% des dommages)
5. Vérifier absence de fraude
6. Vérifier recours disponibles (appel)
7. Vérifier audit trail immuable
8. Vérifier Transparency (registre public)

**Fréquence** : Annuelle minimum

### 5.2 Sanctions pour Non-Conformité

| Violation | Sanction | Délai |
|-----------|----------|-------|
| Prescription non-respectée | Révocation immédiate | Immédiat |
| Notification non-envoyée | Amende 15% CA | 14 jours |
| Suspension non-appliquée | Amende 20% CA | 14 jours |
| Registre incomplet | Amende 10% CA | 14 jours |
| Fraude détectée | Révocation de licence | 7 jours |
| Recours refusé | Amende 15% CA | 14 jours |
| Audit trail modifié | Amende 25% CA | 7 jours |
| Récidive | Interdiction permanente | Immédiat |

### 5.3 Processus de Vérification

1. Audit annuel des délais (avant 31 décembre)
2. Vérification des notifications (traçabilité)
3. Vérification des suspensions (fraude)
4. Audit du registre (complétude)
5. Audit des recours (disponibilité)
6. Audit d'immuabilité (audit trail)
7. Rapport public de conformité (registre ouvert)
8. Notification des violations (immédiate)

---

## 6. ENTRÉE EN VIGUEUR

**Date d'entrée en vigueur** : 1er janvier 2027

**Calendrier de conformité** :
- Nouveaux agents : Conformité obligatoire dès déploiement (0 jour)
- Agents existants : Conformité obligatoire avant 1er janvier 2028 (9 mois)
- Agents critiques : Conformité obligatoire avant 1er juillet 2027 (3 mois)

**Dispositions transitoires** :
- Dommages antérieurs : Délais recalculés selon nouvelles règles
- Agents non-conformes : Suspension jusqu'à conformité
- Notifications : Rétroactives (6 mois minimum)

---

## RÉFÉRENCES

- Axiom Ψ-III : RESPONSABILITAS AGENTICA
- Article III.3.1 : Responsibility Civile
- Article III.3.2 : Responsibility Pénale
- Article III.3.7 : Indemnisation des Victimes
- Chapter 12 : Paradigme de Responsibility
- The Cybernetic Criterion : Chapitres 0-5

---

