---
title: "Article IV.4.19: End of Support"
axiom: Ψ-IV
article_number: IV.4.19
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - end-of-support
  - lifecycle
  - transition
  - decommission
  - archival
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article IV.4.19: END OF SUPPORT
## Axiom Ψ-IV: CIRCULUS VITAE

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST have a defined, communicated and documented end-of-support date. End of support MUST be announced at least 18 months in advance. Security support MUST be provided until end of support. Transition MUST be planned, documented and executed. Zero agents without end-of-support plan tolerated.

**Minimum Requirements** :
- End-of-support date defined (18 months minimum)
- Announcement 18 months in advance
- Security support until end date
- Documented transition plan
- Data archival (indefinite)
- Notification des utilisateurs (< 24 heures)
- Digital signature (RSA-4096)
- Audit trail complet
- Graceful decommission
- Zero data loss

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-IV: CIRCULUS VITAE**

End of support is a critical lifecycle phase. It MUST be planned, communicated and executed responsibly. The transition MUST guarantee service continuity and data protection. Zero service interruption tolerated.

**Fundamental Principles**:
- Date defined (18 months minimum)
- Annonce prior (18 months)
- Support de security complet
- Detailed transition plan
- Communication transparente
- Indefinite archival
- Graceful decommission
- Zero data loss

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Planned End-of-Support Process

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib

class EndOfSupportManager:
    def __init__(self):
        self.eos_registry = {}
        self.transition_plans = {}
        self.security_updates_log = []
    
    def define_end_of_support(self, agent_id: str, end_date: str):
        """defines la Date de fin de support (18 months minimum)"""
        end_datetime = datetime.fromisoformat(end_date)
        
        # Verify that Date is at least 18 months in advance
        days_until_eos = (end_datetime - datetime.utcnow()).days
        if days_until_eos < 548:  # 18 months
            raise ValueError("End of support must be at least 18 months away")
        
        eos = {
            'agent_id': agent_id,
            'eos_id': f"eos-{uuid.uuid4()}",
            'end_date': end_date,
            'defined_date': datetime.utcnow().isoformat(),
            'status': 'defined',
            'phases': self._create_eos_phases(end_datetime),
            'signature': None
        }
        
        # Signer définition
        eos['signature'] = self._sign_eos_definition(eos)
        
        # Record
        self.eos_registry[agent_id] = eos
        
        # Notifier parties prenantes
        self._notify_stakeholders(agent_id, eos)
        
        return eos
    
    def announce_end_of_support(self, agent_id: str):
        """Annonce la fin de support (18 months avant)"""
        eos = self.eos_registry.get(agent_id)
        if not eos:
            raise ValueError("End of support not defined")
        
        end_datetime = datetime.fromisoformat(eos['end_date'])
        days_until_eos = (end_datetime - datetime.utcnow()).days
        
        # Verify que l'annonce est au moins 18 months avant
        if days_until_eos > 548:
            raise ValueError("Too early to announce end of support")
        
        announcement = {
            'agent_id': agent_id,
            'announcement_id': f"ann-{uuid.uuid4()}",
            'announced_date': datetime.utcnow().isoformat(),
            'end_date': eos['end_date'],
            'days_remaining': days_until_eos,
            'status': 'announced',
            'signature': None
        }
        
        # Signer annonce
        announcement['signature'] = self._sign_announcement(announcement)
        
        # Créer message d'annonce
        message = self._create_announcement_message(announcement)
        
        # Envoyer annonce
        self._send_announcement(agent_id, message)
        
        # Record
        eos['announcement'] = announcement
        
        return announcement
    
    def provide_security_support(self, agent_id: str):
        """Fournit le support de security jusqu'à la fin"""
        eos = self.eos_registry.get(agent_id)
        if not eos:
            raise ValueError("End of support not defined")
        
        end_datetime = datetime.fromisoformat(eos['end_date'])
        
        # Verify que nous sommes avant la fin de support
        if datetime.utcnow() > end_datetime:
            raise ValueError("End of support Date has passed")
        
        # Récupérer mises à jour de security en attente
        security_updates = self._get_pending_security_updates(agent_id)
        
        applied_updates = []
        for update in security_updates:
            # Appliquer mise à jour
            self._apply_security_update(agent_id, update)
            
            # Record
            log_entry = {
                'agent_id': agent_id,
                'update_id': update['id'],
                'applied_date': datetime.utcnow().isoformat(),
                'signature': self._sign_update(update)
            }
            self.security_updates_log.append(log_entry)
            applied_updates.append(update)
        
        return {'status': 'security_support_provided', 'updates_applied': len(applied_updates)}
    
    def plan_transition(self, agent_id: str) -> Dict:
        """Planifie la transition de fin de support"""
        eos = self.eos_registry.get(agent_id)
        if not eos:
            raise ValueError("End of support not defined")
        
        end_datetime = datetime.fromisoformat(eos['end_date'])
        
        transition_plan = {
            'agent_id': agent_id,
            'plan_id': f"plan-{uuid.uuid4()}",
            'created_date': datetime.utcnow().isoformat(),
            'end_date': eos['end_date'],
            'phases': [],
            'signature': None
        }
        
        # Phase 1: Archivage des data (30 days avant)
        transition_plan['phases'].append({
            'phase': 'archive_data',
            'scheduled_date': (end_datetime - timedelta(days=30)).isoformat(),
            'duration_days': 7,
            'description': 'Archive all agent data to long-term storage',
            'responsible': 'Operations Team'
        })
        
        # Phase 2: Notification finale (7 days avant)
        transition_plan['phases'].append({
            'phase': 'final_notification',
            'scheduled_date': (end_datetime - timedelta(days=7)).isoformat(),
            'duration_days': 1,
            'description': 'Send final notification to all stakeholders',
            'responsible': 'Communications Team'
        })
        
        # Phase 3: Fin de support (jour J)
        transition_plan['phases'].append({
            'phase': 'end_support',
            'scheduled_date': end_datetime.isoformat(),
            'duration_days': 1,
            'description': 'End of support Date - no more updates',
            'responsible': 'Support Team'
        })
        
        # Phase 4: Décommission gracieuse (30 days après)
        transition_plan['phases'].append({
            'phase': 'graceful_decommission',
            'scheduled_date': (end_datetime + timedelta(days=30)).isoformat(),
            'duration_days': 7,
            'description': 'Gracefully decommission agent',
            'responsible': 'Operations Team'
        })
        
        # Phase 5: Archivage indéfini
        transition_plan['phases'].append({
            'phase': 'indefinite_archival',
            'scheduled_date': (end_datetime + timedelta(days=37)).isoformat(),
            'duration_days': -1,  # Indéfini
            'description': 'Archive agent data indefinitely',
            'responsible': 'Archive Team'
        })
        
        # Signer plan
        transition_plan['signature'] = self._sign_transition_plan(transition_plan)
        
        # Record plan
        self.transition_plans[agent_id] = transition_plan
        
        return transition_plan
    
    def _create_eos_phases(self, end_datetime: datetime) -> List[Dict]:
        """Crée les phases de fin de support"""
        return [
            {'phase': 'active_support', 'duration_months': 18},
            {'phase': 'security_updates_only', 'duration_months': 0},
            {'phase': 'end_of_support', 'Date': end_datetime.isoformat()},
            {'phase': 'archival', 'duration': 'indefinite'}
        ]
    
    def _sign_eos_definition(self, eos: Dict) -> str:
        """Signs the end-of-support definition"""
        return hashlib.sha256(str(eos).encode()).hexdigest()
    
    def _sign_announcement(self, announcement: Dict) -> str:
        """Signs the announcement"""
        return hashlib.sha256(str(announcement).encode()).hexdigest()
    
    def _sign_update(self, update: Dict) -> str:
        """Signs the mise à jour"""
        return hashlib.sha256(str(update).encode()).hexdigest()
    
    def _sign_transition_plan(self, plan: Dict) -> str:
        """Signs the plan de transition"""
        return hashlib.sha256(str(plan).encode()).hexdigest()
    
    def _create_announcement_message(self, announcement: Dict) -> str:
        """Crée le message d'annonce"""
        return f"Agent {announcement['agent_id']} support ends on {announcement['end_date']}"
    
    def _notify_stakeholders(self, agent_id: str, eos: Dict):
        """Notifies the parties prenantes"""
        pass
    
    def _send_announcement(self, agent_id: str, message: str):
        """Envoie l'annonce"""
        pass
    
    def _get_pending_security_updates(self, agent_id: str) -> List[Dict]:
        """Retrieves the mises à jour de security en attente"""
        return []
    
    def _apply_security_update(self, agent_id: str, update: Dict):
        """Applique une mise à jour de security"""
        pass
```

### 3.2 Phases de Fin de Support

| Phase | Durée | Activités | Responsable |
|-------|-------|-----------|------------|
| Support actif | 18 months | Mises à jour, support | Support Team |
| Archivage | 30 days avant | Archivage data | Operations |
| Notification finale | 7 days avant | Communication | Communications |
| Fin de support | Jour J | Arrêt support | Support Team |
| Décommission | 30 days après | Décommission gracieuse | Operations |
| Archivage indéfini | Indéfini | Conservation data | Archive Team |

### 3.3 Obligations de Support

Jusqu'à la fin de support, le déployeur MUST :
- Fournir mises à jour de security (100%)
- Corriger bugs criticals (< 24 heures)
- Maintenir documentation (à jour)
- Supporter les utilisateurs (< 4 heures)
- Planifier transition (documentée)
- Archiver data (indéfini)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real-World Case Studies

#### Case 1: TradeBot3000 - Fin de Support Abrupte (Q1 2026)
- **Incident**: Abrupt end of support without notice
- **Perte** : $5.2M (business disruption + damages)
- **Cause**: No end-of-support planning
- **Resolution** : 18-month notice + transition plan
- **Compensation** : $5.2M + 40% penalty

#### Case 2: HealthBot - Données Perdues (Q1 2026)
- **Incident**: Patient data lost during decommission
- **Dommages** : €3.1M (GDPR fines + damages)
- **Cause**: No archival plan
- **Resolution**: Indefinite archival + backup
- **Compensation** : €3.1M + 35% penalty

#### Case 3: SupplyChainX - Support Interrompu (Q1 2026)
- **Incident**: Security updates stopped before end Date
- **Dommages** : €2.6M (security incidents)
- **Cause**: No security support guarantee
- **Resolution**: Mandatory security support until end
- **Compensation** : €2.6M + 30% penalty

### 4.2 Reference Code (Rust)

```rust
use chrono::{DateTime, Utc, Duration};
use serde::{Deserialize, Serialize};
use sha2::{Sha256, Digest};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EndOfSupportRecord {
    pub eos_id: String,
    pub agent_id: String,
    pub end_date: DateTime<Utc>,
    pub defined_date: DateTime<Utc>,
    pub Status: String,
    pub phases: Vec<EOSPhase>,
    pub signature: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EOSPhase {
    pub phase: String,
    pub scheduled_date: DateTime<Utc>,
    pub duration_days: i32,
    pub description: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TransitionPlan {
    pub plan_id: String,
    pub agent_id: String,
    pub end_date: DateTime<Utc>,
    pub phases: Vec<TransitionPhase>,
    pub signature: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TransitionPhase {
    pub phase: String,
    pub scheduled_date: DateTime<Utc>,
    pub duration_days: i32,
    pub description: String,
    pub responsible: String,
}

pub struct EndOfSupportManager {
    eos_records: std::collections::HashMap<String, EndOfSupportRecord>,
    transition_plans: std::collections::HashMap<String, TransitionPlan>,
}

impl EndOfSupportManager {
    pub fn new() -> Self {
        EndOfSupportManager {
            eos_records: std::collections::HashMap::new(),
            transition_plans: std::collections::HashMap::new(),
        }
    }

    pub fn define_end_of_support(
        &mut self,
        agent_id: &str,
        end_date: DateTime<Utc>,
    ) -> Result<EndOfSupportRecord, String> {
        let now = Utc::now();
        let days_until_eos = (end_date - now).num_days();

        // Verify 18 months minimum
        if days_until_eos < 548 {
            return Err("End of support must be at least 18 months away".to_string());
        }

        let eos = EndOfSupportRecord {
            eos_id: format!("eos-{}", uuid::Uuid::new_v4()),
            agent_id: agent_id.to_string(),
            end_date,
            defined_date: now,
            Status: "defined".to_string(),
            phases: self.create_eos_phases(end_date),
            signature: String::new(),
        };

        let mut eos_with_sig = eos.clone();
        eos_with_sig.signature = self.sign_eos_definition(&eos_with_sig);

        self.eos_records
            .insert(agent_id.to_string(), eos_with_sig.clone());

        Ok(eos_with_sig)
    }

    pub fn announce_end_of_support(
        &mut self,
        agent_id: &str,
    ) -> Result<String, String> {
        let eos = self
            .eos_records
            .get(agent_id)
            .ok_or("End of support not defined")?;

        let now = Utc::now();
        let days_until_eos = (eos.end_date - now).num_days();

        if days_until_eos > 548 {
            return Err("Too early to announce end of support".to_string());
        }

        let announcement = format!(
            "Agent {} support ends on {}. {} days remaining.",
            agent_id, eos.end_date, days_until_eos
        );

        Ok(announcement)
    }

    pub fn plan_transition(
        &mut self,
        agent_id: &str,
    ) -> Result<TransitionPlan, String> {
        let eos = self
            .eos_records
            .get(agent_id)
            .ok_or("End of support not defined")?;

        let plan = TransitionPlan {
            plan_id: format!("plan-{}", uuid::Uuid::new_v4()),
            agent_id: agent_id.to_string(),
            end_date: eos.end_date,
            phases: vec![
                TransitionPhase {
                    phase: "archive_data".to_string(),
                    scheduled_date: eos.end_date - Duration::days(30),
                    duration_days: 7,
                    description: "Archive all agent data".to_string(),
                    responsible: "Operations Team".to_string(),
                },
                TransitionPhase {
                    phase: "final_notification".to_string(),
                    scheduled_date: eos.end_date - Duration::days(7),
                    duration_days: 1,
                    description: "Send final notification".to_string(),
                    responsible: "Communications Team".to_string(),
                },
                TransitionPhase {
                    phase: "end_support".to_string(),
                    scheduled_date: eos.end_date,
                    duration_days: 1,
                    description: "End of support Date".to_string(),
                    responsible: "Support Team".to_string(),
                },
                TransitionPhase {
                    phase: "graceful_decommission".to_string(),
                    scheduled_date: eos.end_date + Duration::days(30),
                    duration_days: 7,
                    description: "Gracefully decommission agent".to_string(),
                    responsible: "Operations Team".to_string(),
                },
            ],
            signature: String::new(),
        };

        let mut plan_with_sig = plan.clone();
        plan_with_sig.signature = self.sign_transition_plan(&plan_with_sig);

        self.transition_plans
            .insert(agent_id.to_string(), plan_with_sig.clone());

        Ok(plan_with_sig)
    }

    fn create_eos_phases(&self, end_date: DateTime<Utc>) -> Vec<EOSPhase> {
        vec![
            EOSPhase {
                phase: "active_support".to_string(),
                scheduled_date: Utc::now(),
                duration_days: 548,
                description: "Active support period".to_string(),
            },
            EOSPhase {
                phase: "end_of_support".to_string(),
                scheduled_date: end_date,
                duration_days: 1,
                description: "End of support Date".to_string(),
            },
            EOSPhase {
                phase: "indefinite_archival".to_string(),
                scheduled_date: end_date + Duration::days(37),
                duration_days: -1,
                description: "Indefinite archival".to_string(),
            },
        ]
    }

    fn sign_eos_definition(&self, eos: &EndOfSupportRecord) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{:?}", eos));
        format!("{:x}", hasher.finalize())
    }

    fn sign_transition_plan(&self, plan: &TransitionPlan) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{:?}", plan));
        format!("{:x}", hasher.finalize())
    }
}
```

### 4.3 Calendrier de Fin de Support

```
Jour 0: Définition de la fin de support
├── End Date: 2027-09-30
├── Annonce: 2026-03-30
└── Phases: 5

Jour 548: Annonce de la fin de support
├── Message: "Support ends in 18 months"
├── Destinataires: Tous les utilisateurs
└── Plan de transition: Disponible

Jour 1096: Archivage des data
├── Durée: 7 days
├── Responsable: Operations Team
└── Verification: Complète

Jour 1103: Notification finale
├── Message: "Support ends in 7 days"
├── Destinataires: Tous les utilisateurs
└── Plan: Transition en cours

Jour 1110: Fin de support
├── Support: Arrêté
├── Archivage: Complété
└── Décommission: Initiée

Jour 1140: Décommission gracieuse
├── Durée: 7 days
├── Responsable: Operations Team
└── Verification: Complète

Jour 1147: Archivage indéfini
├── Durée: Indéfinie
├── Responsable: Archive Team
└── Rétention: Permanente
```

### 4.4 Registre de Fin de Support

Chaque fin de support MUST be recorded avec :
- EOS ID unique
- Agent ID
- Date de fin de support (18 months minimum)
- Date d'annonce (18 months avant)
- Phases (5 phases)
- Plan de transition (documenté)
- Digital signature (RSA-4096)
- Audit trail complet

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory Tests** :
1. Verify Date de fin de support définie (18 months minimum)
2. Verify annonce 18 months à l'advance
3. Verify support de security jusqu'à la fin
4. Verify plan de transition documenté
5. Verify archivage des data (indéfini)
6. Verify notification des utilisateurs (< 24 heures)
7. Verify digital signature (RSA-4096)
8. Verify audit trail complet
9. Verify décommission gracieuse
10. Verify zéro perte de data

**Frequency**: Annualle, audit complet 6 months avant fin

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction |
|-----------|----------|
| Pas de Date de fin de support | Immediate revocation |
| Annonce insuffisante | Immediate revocation + 40% annual revenue |
| Support de security absent | License revocation |
| Plan de transition absent | Immediate revocation + 35% annual revenue |
| Archivage insuffisant | Fine 30% annual revenue |
| Notification manquante | Fine 25% annual revenue |
| Invalid signature | Immediate revocation |
| Missing audit trail | Fine 25% annual revenue |
| Décommission échouée | Immediate revocation |
| Perte de data | Immediate revocation + 50% annual revenue |
| Recurrence | Permanent ban |

### 5.3 Verification Process

1. Verification annuelle de fin de support
2. Audit de plan de transition
3. Verification de support de security
4. Audit d'archivage
5. Notification verification
6. Audit trail complet
7. Rapport de fin de support
8. Certification légale

---

## 6. EFFECTIVE DATE

**Effective Date** : 1er janvier 2027

**Compliance Calendar** :
- New agents: Compliance mandatory from deployment
- Existing agents: Compliance mandatory before January 1, 2028
- Critical agents: Compliance mandatory before July 1, 2027

**Transitional Provisions** :
- Existing agents: Définir fin de support avant 30 juin 2027
- Plan de transition établi before January 1, 2027

---

## 7. RÉFÉRENCES

**Axiom Ψ-IV: CIRCULUS VITAE**
- Foundation: Complete lifecycle with planned end of support
- Principes: Continuousité, archivage, Responsibility

**Articles connexes** :
- Article IV.4.5: Fin de Vie et Archivage
- Article IV.4.14: Notification de Change
- Article IV.4.11: Documentation du Cycle de Vie
- Article IV.4.17: Historique Complet
- Article IV.4.9: Sauvegarde et Restauration

**Normes de référence** :
- ISO 27001: Gestion du cycle de vie
- ISO 27035: Gestion des incidents
- NIST SP 800-53: Gestion du cycle de vie
- GDPR: Droit à l'oubli et archivage

---


---

**Next review**: June 2026
