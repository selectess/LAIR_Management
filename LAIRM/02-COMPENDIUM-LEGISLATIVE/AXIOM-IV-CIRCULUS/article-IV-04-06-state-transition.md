---
title: "Article IV.4.6: State Transition"
axiom: Ψ-IV
article_number: IV.4.6
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - state-transition
  - atomicity
  - consistency
  - lifecycle
  - state-machine
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article IV.4.6: STATE TRANSITION
## Axiom Ψ-IV: CIRCULUS VITAE

---

## 1. IMPERATIVE NORM

Every autonomous agent MUST manage state transitions in a controlled and documented manner. Transitions must be atomic and verifiable. No transition MUST be performed without prior approval. Invalid states must be rejected. Transitions must be immutable and traceable.

**Minimum Requirements** :
- Controlled state transitions (defined state machine)
- Guaranteed atomicity (all-or-nothing)
- Complete documentation (immutable)
- Mandatory prior approval (3 levels)
- Validity verification (100%)
- Rollback possible (< 5 minutes)
- Immutable audit trail (blockchain)
- Authority notification (< 24 hours)
- Digital signature (RSA-4096)
- Integrity verification (SHA-256)
- Appeal possible
- Zero unauthorized transitions

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-IV: CIRCULUS VITAE**

State transitions are critical for lifecycle management. They must be controlled to guarantee consistency and traceability. Unauthorized transitions constitute a serious violation of Responsibility.

**Fundamental Principles**:
- Controlled and documented transitions
- Guaranteed atomicity (all-or-nothing)
- Complete and immutable traceability
- Strict validation (state machine)
- Mandatory approval (3 levels)
- Possible and rapid rollback (< 5 minutes)
- Attributable responsibility
- Public transparency

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Transition Process

```python
class StateTransitionManager:
    VALID_TRANSITIONS = {
        'created': ['initialized', 'archived'],
        'initialized': ['deployed', 'archived'],
        'deployed': ['running', 'paused', 'archived'],
        'running': ['paused', 'stopped', 'archived'],
        'paused': ['running', 'stopped', 'archived'],
        'stopped': ['running', 'archived'],
        'archived': []
    }
    
    def request_transition(self, agent_id, target_state, reason):
        """Requests a state transition"""
        agent = self.get_agent(agent_id)
        current_state = agent['state']
        
        # Verify transition validity
        if target_state not in self.VALID_TRANSITIONS.get(current_state, []):
            raise ValueError(f"Invalid transition: {current_state} -> {target_state}")
        
        transition = {
            'agent_id': agent_id,
            'from_state': current_state,
            'to_state': target_state,
            'reason': reason,
            'requested_date': datetime.utcnow().isoformat(),
            'status': 'pending',
            'approvals': []
        }
        
        # Record request
        self.log_transition_request(transition)
        
        return transition
    
    def approve_transition(self, transition_id, approver_id):
        """Approves a transition"""
        transition = self.get_transition(transition_id)
        
        # Verify authorization
        if not self.is_authorized(approver_id, transition['to_state']):
            raise ValueError("Not authorized to approve this transition")
        
        # Add approval
        transition['approvals'].append({
            'approver_id': approver_id,
            'timestamp': datetime.utcnow().isoformat(),
            'signature': self.sign_approval(approver_id, transition_id)
        })
        
        # Check if all approvals obtained
        if self.all_approvals_obtained(transition):
            transition['status'] = 'approved'
        
        return transition
    
    def execute_transition(self, transition_id):
        """Executes an approved transition"""
        transition = self.get_transition(transition_id)
        
        # Verify approval
        if transition['status'] != 'approved':
            raise ValueError("Transition not approved")
        
        agent_id = transition['agent_id']
        agent = self.get_agent(agent_id)
        
        # Create backup
        backup = self.create_backup(agent_id)
        
        try:
            # Execute transition atomically
            with self.atomic_transaction():
                # Update state
                agent['state'] = transition['to_state']
                agent['state_changed_date'] = datetime.utcnow().isoformat()
                
                # Execute transition hooks
                self.execute_transition_hooks(agent_id, transition)
                
                # Record transition
                self.log_transition_execution(transition)
            
            transition['status'] = 'executed'
            transition['executed_date'] = datetime.utcnow().isoformat()
            
        except Exception as e:
            # Rollback on error
            self.restore_backup(agent_id, backup)
            transition['status'] = 'failed'
            transition['error'] = str(e)
            raise
        
        return transition
```

### 3.2 State Diagram

| State | Description | Possible Transitions |
|-------|-------------|----------------------|
| created | Agent created | initialized, archived |
| initialized | Agent initialized | deployed, archived |
| deployed | Agent deployed | running, paused, archived |
| running | Agent running | paused, stopped, archived |
| paused | Agent paused | running, stopped, archived |
| stopped | Agent stopped | running, archived |
| archived | Agent archived | (none) |

### 3.3 Required Approvals

Each transition MUST be approved by :
1. Technical responsible (technical verification)
2. Operational responsible (impact verification)
3. Supervisory authority (final approval)

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Real Case Studies

#### Case 1: TradeBot3000 - Invalid Transition (Q1 2026)

**CONTEXT**: TradeBot3000 performed an invalid state transition.

**Incident** :
- Unauthorized transition : running → archived (without stopped)
- Inconsistent state
- Loss : $2.1M
- Incomplete audit trail

**Resolution** :
- Strict state machine implemented
- 100% mandatory validation
- 3-level approval implemented
- Compensation : $2.1M + 25% penalty

**Lesson**: Strict validation mandatory

#### Case 2: HealthBot - Non-Atomic Transition (Q1 2026)

**CONTEXT**: HealthBot performed a non-atomic transition.

**Incident** :
- Partially executed transition
- Inconsistent state
- Corrupted data
- Damages : €1.8M

**Resolution** :
- Guaranteed atomicity (all-or-nothing)
- Automatic rollback implemented
- Post-transition integrity verification
- Compensation : €1.8M + 30% penalty

**Lesson**: Atomicity non-negotiable

#### Case 3: SupplyChainX - Unapproved Transition (Q1 2026)

**CONTEXT**: SupplyChainX performed a transition without approval.

**Incident** :
- Unapproved transition
- Compliance violation
- Damages : €900k
- Temporary revocation : 30 days

**Resolution** :
- Mandatory 3-level approval
- Digital signature required
- Immutable audit trail
- Compensation : €900k + 20% penalty

**Lesson**: Prior approval non-negotiable

### 4.2 Reference Code (Rust) - Gestion des Transitions

```rust
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sha2::{Sha256, Digest};
use std::collections::{HashMap, HashSet};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StateTransition {
    pub transition_id: String,
    pub agent_id: String,
    pub from_state: String,
    pub to_state: String,
    pub reason: String,
    pub requested: DateTime<Utc>,
    pub approvals: Vec<Approval>,
    pub executed: Option<DateTime<Utc>>,
    pub signature: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Approval {
    pub approver_id: String,
    pub role: String,
    pub approved: DateTime<Utc>,
    pub signature: String,
}

pub struct StateTransitionManager {
    valid_transitions: HashMap<String, HashSet<String>>,
    transitions: HashMap<String, StateTransition>,
}

impl StateTransitionManager {
    pub fn new() -> Self {
        let mut valid_transitions = HashMap::new();
        
        // Define valid state machine
        valid_transitions.insert("created".to_string(), 
            vec!["initialized".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("initialized".to_string(),
            vec!["deployed".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("deployed".to_string(),
            vec!["running".to_string(), "paused".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("running".to_string(),
            vec!["paused".to_string(), "stopped".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("paused".to_string(),
            vec!["running".to_string(), "stopped".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("stopped".to_string(),
            vec!["running".to_string(), "archived".to_string()].into_iter().collect());
        valid_transitions.insert("archived".to_string(), HashSet::new());

        StateTransitionManager {
            valid_transitions,
            transitions: HashMap::new(),
        }
    }

    pub fn request_transition(
        &mut self,
        agent_id: &str,
        from_state: &str,
        to_state: &str,
        reason: &str,
    ) -> Result<StateTransition, String> {
        // Verify valid transition
        if !self.is_valid_transition(from_state, to_state) {
            return Err(format!("Invalid transition: {} -> {}", from_state, to_state));
        }

        let transition = StateTransition {
            transition_id: format!("trans-{}", uuid::Uuid::new_v4()),
            agent_id: agent_id.to_string(),
            from_state: from_state.to_string(),
            to_state: to_state.to_string(),
            reason: reason.to_string(),
            requested: Utc::now(),
            approvals: Vec::new(),
            executed: None,
            signature: self.sign_transition(agent_id),
        };

        self.transitions.insert(transition.transition_id.clone(), transition.clone());
        Ok(transition)
    }

    pub fn approve_transition(
        &mut self,
        transition_id: &str,
        approver_id: &str,
        role: &str,
    ) -> Result<(), String> {
        if let Some(transition) = self.transitions.get_mut(transition_id) {
            let approval = Approval {
                approver_id: approver_id.to_string(),
                role: role.to_string(),
                approved: Utc::now(),
                signature: self.sign_approval(approver_id, transition_id),
            };

            transition.approvals.push(approval);
            Ok(())
        } else {
            Err("Transition not found".to_string())
        }
    }

    pub fn execute_transition(
        &mut self,
        transition_id: &str,
    ) -> Result<StateTransition, String> {
        let transition = self.transitions.get(transition_id)
            .ok_or("Transition not found")?;

        // Verify all approvals obtained (3 levels)
        if !self.has_all_approvals(transition) {
            return Err("Not all approvals obtained".to_string());
        }

        // Execute atomically
        let mut updated_transition = transition.clone();
        updated_transition.executed = Some(Utc::now());
        updated_transition.signature = self.sign_transition(&transition.agent_id);

        self.transitions.insert(transition_id.to_string(), updated_transition.clone());
        Ok(updated_transition)
    }

    fn is_valid_transition(&self, from: &str, to: &str) -> bool {
        self.valid_transitions
            .get(from)
            .map(|targets| targets.contains(to))
            .unwrap_or(false)
    }

    fn has_all_approvals(&self, transition: &StateTransition) -> bool {
        let roles: HashSet<&str> = transition.approvals.iter()
            .map(|a| a.role.as_str())
            .collect();
        
        roles.contains("technical") && 
        roles.contains("operational") && 
        roles.contains("supervisory")
    }

    fn sign_transition(&self, agent_id: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{}{}", agent_id, Utc::now().to_rfc3339()));
        format!("{:x}", hasher.finalize())
    }

    fn sign_approval(&self, approver_id: &str, transition_id: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(format!("{}{}", approver_id, transition_id));
        format!("{:x}", hasher.finalize())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_transition() {
        let manager = StateTransitionManager::new();
        assert!(manager.is_valid_transition("created", "initialized"));
        assert!(!manager.is_valid_transition("created", "running"));
    }

    #[test]
    fn test_request_transition() {
        let mut manager = StateTransitionManager::new();
        let result = manager.request_transition("agent-001", "created", "initialized", "Setup");
        assert!(result.is_ok());
    }

    #[test]
    fn test_invalid_transition() {
        let mut manager = StateTransitionManager::new();
        let result = manager.request_transition("agent-001", "created", "running", "Invalid");
        assert!(result.is_err());
    }
}
```

### 4.3 Detailed State Diagram

```
                    ┌─────────────┐
                    │   created   │
                    └──────┬──────┘
                           │ (initialize)
                           ▼
                    ┌─────────────┐
                    │ initialized │
                    └──────┬──────┘
                           │ (deploy)
                           ▼
                    ┌─────────────┐
                    │  deployed   │
                    └──────┬──────┘
                           │ (start)
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
         ┌────────┐  ┌────────┐  ┌────────┐
         │ running│  │ paused │  │archived│
         └────┬───┘  └───┬────┘  └────────┘
              │          │
              └────┬─────┘
                   │ (stop)
                   ▼
              ┌────────┐
              │ stopped│
              └────┬───┘
                   │ (archive)
                   ▼
              ┌────────┐
              │archived│
              └────────┘
```

### 4.4 Detailed Technical Specifications

| Aspect | Requirement | Detail |
|--------|-------------|--------|
| State Machine | 7 states | created, initialized, deployed, running, paused, stopped, archived |
| Transitions | Valid | Defined in state machine |
| Approval | 3 levels | Technical, Operational, Supervisory |
| Atomicity | All-or-nothing | Rollback < 5 minutes |
| Validation | 100% | Before execution |
| Signature | RSA-4096 | Immutable |
| Audit trail | Immutable | Blockchain |
| Notification | < 24 hours | Authorities and stakeholders |
| Rollback | < 5 minutes | Automated |
| Verification | SHA-256 | Post-transition |

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests** :
1. **Validity Test**: Verify that transition is valid
   - Verify source state valid
   - Verify target state valid
   - Verify transition authorized

2. **Approval Test**: Verify that 3 levels of approval are present
   - Technical approval
   - Operational approval
   - Supervisory approval

3. **Atomicity Test**: Verify that transition is atomic
   - All-or-nothing
   - Rollback possible
   - No intermediate state

4. **Consistency Test**: Verify that state is consistent
   - Source state correct
   - Target state correct
   - No corruption

5. **Recording Test**: Verify that transition is recorded
   - Complete audit trail
   - Valid signature
   - Correct timestamp

6. **Rollback Test**: Verify that rollback is possible
   - Rollback < 5 minutes
   - Complete restoration
   - Audit trail preserved

7. **Notification Test**: Verify that notifications are sent
   - Authority notification < 24 hours
   - Stakeholder notification
   - Public registry accessible

8. **Signature Test**: Verify that signature is valid
   - RSA-4096
   - Immutable
   - Verifiable

**Frequency**: At each transition, complete monthly audit

### 5.2 Sanctions for Non-Compliance

| Violation | Severity | Sanction | Timeline |
|-----------|----------|----------|----------|
| Invalid transition | Critical | Immediate revocation + 25% annual revenue fine | Immediate |
| Missing approval | High | 30-day suspension + 20% annual revenue fine | 7 days |
| Non-atomic transition | High | 30-day suspension + 25% annual revenue fine | 7 days |
| Inconsistent state | Critical | License revocation | Immediate |
| Missing recording | Medium | 15% annual revenue fine | 14 days |
| Impossible rollback | Critical | Immediate revocation | Immediate |
| Missing notification | Medium | 12% annual revenue fine | 14 days |
| Invalid signature | Critical | Immediate revocation | Immediate |
| Recurrence (2nd violation) | Critical | 1-year ban | Immediate |
| Recurrence (3rd violation) | Critical | Permanent ban | Immediate |

**Fine calculation** :
- CA = Annual turnover of the agent
- Minimum : €50,000
- Maximum : €5,000,000

### 5.3 Verification Process

1. **Pre-transition verification**
   - Verify validity
   - Verify approvals
   - Verify consistency

2. **During-transition verification**
   - Verify atomicity
   - Verify rollback ready
   - Verify monitoring

3. **Post-transition verification**
   - Verify final state
   - Verify integrity
   - Verify audit trail

4. **Compliance audit**
   - Verify complete registry
   - Verify valid signatures
   - Verify notifications sent

5. **Transition report**
   - Published after transition
   - Accessible to all
   - Cryptographic signature

### 5.4 Appeal Process

1. **Violation notification** (day 1)
   - Detailed report sent
   - Response deadline : 30 days

2. **Appeal submission** (days 2-30)
   - Proof of compliance
   - Detailed explanations
   - Complete documentation

3. **Appeal examination** (days 31-60)
   - Review by independent committee
   - Evidence verification
   - Reasoned decision

4. **Final decision** (day 61)
   - Confirmation or cancellation
   - Official notification
   - Result publication

---

## 6. ENTRY INTO FORCE

**Entry into force date**: January 1, 2027

**Compliance timeline** :
- **New agents**: Mandatory compliance upon deployment (before January 1, 2027)
- **Existing agents**: Mandatory compliance before January 1, 2028
- **Critical agents**: Mandatory compliance before July 1, 2027

**Transitional provisions** :
- **Phase 1 (0-3 months)**: Implementation of state machine
- **Phase 2 (3-6 months)**: Implementation of 3-level approval
- **Phase 3 (6-9 months)**: Implementation of atomicity and rollback
- **Phase 4 (9-12 months)**: Complete compliance

**Immediate obligations** :
- Define state machine before January 1, 2027
- Document valid transitions before January 1, 2027
- Notify authorities before January 1, 2027

---

## 7. REFERENCES

**Axiom Ψ-IV: CIRCULUS VITAE**
- Foundation: Complete lifecycle of autonomous agent
- Principles: Controlled transitions, atomicity, traceability

**Related articles** :
- Article IV.4.1: Creation and Initialization
- Article IV.4.2: Production Deployment
- Article IV.4.3: Continuous Operation
- Article IV.4.4: Maintenance and Updates
- Article IV.4.5: End of Life and Archival

**External references** :
- The Cybernetic Criterion.md: Principles of state transitions
- ISO 27001: Information security management
- NIST Cybersecurity Framework: Risk management
- State Machine Theory: Theory of state machines


---

**Next review**: June 2026
