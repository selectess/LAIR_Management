---
title: "Universal Kill-Switch Specification"
type: specification
axiom: I
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
validations:
  technical: true
  legal: true
  editorial: true
license: CC-BY-SA-4.0
---

# UNIVERSAL KILL-SWITCH SPECIFICATION
## Axiom Ψ-I : SUPREMATIA HUMANA

### 1. OBJECTIF

Define the technical protocol for the universal emergency stop of any autonomous agent in less than 500ms, guaranteeing absolute human sovereignty.

### 2. FUNCTIONAL REQUIREMENTS

#### 2.1 Stop Time
- **Maximum delay**: 500ms between signal and complete stop
- **Verification** : Heartbeat toutes les 100ms
- **Fallback**: Forced stop after 600ms

#### 2.2 Canaux de Communication
- **Primary**: Secure WebSocket (TLS 1.3)
- **Secondaire** : HTTP/2 avec retry
- **Tertiary**: System signal (SIGTERM)
- **Quaternary**: Network cutoff (timeout)

#### 2.3 Authentification
- **X.509 Certificate** for control authority
- **Signature ECDSA** du signal
- **Nonce** to prevent replay

### 3. FORMAT DU SIGNAL

```json
{
  "type": "kill-switch",
  "Version": "1.0",
  "timestamp": "2026-03-30T12:00:00Z",
  "agent_id": "agent-uuid",
  "authority": "human-controller-id",
  "signature": "base64-encoded-signature",
  "nonce": "random-nonce",
  "reason": "emergency|compliance|maintenance|security"
}
```

### 4. IMPLEMENTATION

#### 4.1 Agent Side
```python
class KillSwitchListener:
    def __init__(self, agent):
        self.agent = agent
        self.listening = True
        self.heartbeat_interval = 0.1  # 100ms
        
    def listen(self):
        while self.listening:
            signal = self.receive_signal()
            if self.verify_signal(signal):
                self.agent.emergency_stop()
                break
            time.sleep(self.heartbeat_interval)
    
    def verify_signal(self, signal):
        # Verify signature
        # Verify nonce
        # Verify authority
        return True
```

#### 4.2 Controller Side
```python
class KillSwitchController:
    def trigger(self, agent_id, reason):
        signal = {
            "type": "kill-switch",
            "agent_id": agent_id,
            "timestamp": datetime.now().isoformat(),
            "reason": reason,
            "nonce": secrets.token_hex(16)
        }
        signal["signature"] = self.sign(signal)
        self.send_signal(signal)
```

### 5. VERIFICATION

- ✅ Signal received in <100ms
- ✅ Signature valide
- ✅ Nonce unique
- ✅ Authority recognized
- ✅ Agent stopped in <500ms

### 6. EFFECTIVE DATE

**Immediate** - Obligatoire pour tous les agents autonomes from deployment.

---

**Version** : 1.0.0

