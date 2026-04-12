# LAIRM Technical Specifications & Implementations

## Technical Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    LAIRM TECHNICAL STACK                    │
├─────────────────────────────────────────────────────────────┤
│  Specifications    │  Implementations    │  Schemas         │
│  ─────────────     │  ──────────────     │  ───────         │
│  kill-switch-spec  │  Python SDK         │  agent-passport  │
│  did-agent-spec    │  Rust Core          │  audit-log       │
│  mcp-protocol-spec │  Go Framework       │  kill-signal     │
│  a2a-protocol-spec │  Solidity Contract  │  compliance      │
│  audit-log-spec    │  Reference Examples │  action-record   │
└─────────────────────────────────────────────────────────────┘
```

## Kill-Switch Specification (Ψ-I)

### Requirements
- **Response Time**: < 500ms from signal to termination
- **Channels**: 3 redundant (network, local, hardware)
- **Scope**: All agents, category-specific, or individual
- **Verification**: Cryptographic confirmation of termination

### Implementation Pattern
```python
class UniversalKillSwitch:
    """
    Universal Kill-Switch implementation per Ψ-I-01-01
    Response time: < 500ms
    Channels: network, local, hardware (redundant)
    """
    
    CHANNELS = ['network', 'local', 'hardware']
    MAX_RESPONSE_TIME_MS = 500
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.active = True
        self.channel_status = {ch: 'ready' for ch in self.CHANNELS}
    
    async def activate(self, scope: str = 'all', reason: str = None) -> KillResult:
        """
        Activate kill-switch across all channels
        
        Args:
            scope: 'all' | 'category' | 'individual'
            reason: Optional reason for audit trail
        
        Returns:
            KillResult with confirmation and timing
        """
        start_time = time.monotonic()
        
        # Parallel activation across all channels
        tasks = [
            self._send_signal(channel, scope, reason)
            for channel in self.CHANNELS
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Verify termination
        verified = await self._verify_termination()
        
        elapsed_ms = (time.monotonic() - start_time) * 1000
        
        return KillResult(
            agent_id=self.agent_id,
            channels_activated=sum(1 for r in results if r.success),
            verified=verified,
            elapsed_ms=elapsed_ms,
            within_sla=elapsed_ms < self.MAX_RESPONSE_TIME_MS
        )
    
    async def _send_signal(self, channel: str, scope: str, reason: str):
        """Send kill signal through specific channel"""
        # Implementation varies by channel
        pass
    
    async def _verify_termination(self) -> bool:
        """Cryptographic verification of agent termination"""
        pass
```

### Hardware Kill-Switch
```python
class HardwareKillSwitch:
    """
    Hardware-level kill-switch for critical infrastructure
    Independent of software stack
    """
    
    def __init__(self, gpio_pin: int):
        self.gpio_pin = gpio_pin
        self.setup_gpio()
    
    def setup_gpio(self):
        """Configure GPIO for hardware interrupt"""
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=GPIO.HIGH)
    
    def activate(self):
        """Trigger hardware-level termination"""
        GPIO.output(self.gpio_pin, GPIO.LOW)
        # Cuts power to agent hardware
```

---

## Agent Passport Specification (Ψ-II)

### DID Format
```
did:lairm:agent:{uuid}
did:lairm:entity:{uuid}
did:lairm:human:{uuid}
```

### Schema
```json
{
  "$schema": "https://w3id.org/did-resolution/v1",
  "didDocument": {
    "id": "did:lairm:agent:550e8400-e29b-41d4-a716-446655440000",
    "verificationMethod": [{
      "id": "did:lairm:agent:550e8400...#key-1",
      "type": "Ed25519VerificationKey2020",
      "controller": "did:lairm:agent:550e8400...",
      "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
    }],
    "authentication": ["did:lairm:agent:550e8400...#key-1"],
    "service": [{
      "id": "did:lairm:agent:550e8400...#audit",
      "type": "AuditTrail",
      "serviceEndpoint": "https://audit.lairm.org/agent/550e8400..."
    }]
  },
  "metadata": {
    "name": "TradingAgent-v1",
    "version": "1.0.0",
    "creator": "did:lairm:entity:1234...",
    "created_at": "2026-01-01T00:00:00Z",
    "axioms": ["I", "II", "III", "IV", "V"],
    "capabilities": ["trading", "analysis"],
    "risk_level": "high"
  }
}
```

### Python Implementation
```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import uuid
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

@dataclass
class AgentPassport:
    """
    Agent Passport per Ψ-II-02-01
    W3C DID-compliant identity
    """
    did: str
    name: str
    version: str
    creator_did: str
    axioms: List[str]
    capabilities: List[str]
    risk_level: str
    created_at: datetime
    public_key: bytes
    
    @classmethod
    def create(cls, name: str, creator_did: str, axioms: List[str]) -> 'AgentPassport':
        """Create new agent passport with cryptographic identity"""
        # Generate Ed25519 key pair
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        
        return cls(
            did=f"did:lairm:agent:{uuid.uuid4()}",
            name=name,
            version="1.0.0",
            creator_did=creator_did,
            axioms=axioms,
            capabilities=[],
            risk_level="medium",
            created_at=datetime.utcnow(),
            public_key=public_key
        )
    
    def sign(self, message: bytes) -> bytes:
        """Sign message with agent's private key"""
        # Implementation with stored private key
        pass
    
    def verify(self, message: bytes, signature: bytes) -> bool:
        """Verify signature with public key"""
        pass
```

---

## MCP Protocol Integration (Ψ-V)

### Server Configuration
```python
from mcp.server import Server
from mcp.types import Tool, TextContent

class LAIRMMCPServer(Server):
    """
    MCP Server for LAIRM framework access
    Implements Ψ-V interoperability requirements
    """
    
    def __init__(self):
        super().__init__("lairm-mcp-server")
        self.framework = LAIRMFramework()
    
    @Tool
    async def search_articles(
        self,
        query: str,
        axiom: Optional[str] = None,
        status: Optional[str] = None
    ) -> list[TextContent]:
        """Search LAIRM articles by query and filters"""
        results = self.framework.search_articles(query, axiom, status)
        return [TextContent(type="text", text=str(r)) for r in results]
    
    @Tool
    async def get_article(self, number: str) -> TextContent:
        """Retrieve specific article by number (e.g., 'I-01-01')"""
        article = self.framework.get_article(number)
        return TextContent(type="text", text=article.to_json())
    
    @Tool
    async def validate_compliance(self, agent_config: dict) -> TextContent:
        """Validate agent configuration against LAIRM axioms"""
        result = self.framework.validate_compliance(agent_config)
        return TextContent(type="text", text=result.to_json())
    
    @Tool
    async def audit_action(
        self,
        agent_id: str,
        action: dict
    ) -> TextContent:
        """Record and audit agent action"""
        record = self.framework.audit_action(agent_id, action)
        return TextContent(type="text", text=record.to_json())
```

---

## Audit Log Specification (Ψ-VI)

### Schema
```json
{
  "schema": "lairm-audit-log-v1",
  "entries": [{
    "sequence": 1,
    "timestamp": "2026-01-01T00:00:00.000Z",
    "agent_id": "did:lairm:agent:xxx",
    "action_type": "decision",
    "action": {
      "type": "trade_execution",
      "parameters": {...},
      "result": {...}
    },
    "context": {
      "session_id": "sess-xxx",
      "parent_action": "act-xxx",
      "human_approved": true,
      "confidence": 0.95
    },
    "hash": "sha256:abc123...",
    "previous_hash": "sha256:def456...",
    "signature": "ed25519:xyz789..."
  }]
}
```

### Blockchain Storage
```python
class BlockchainAuditLog:
    """
    Immutable audit log on blockchain
    Implements Ψ-VI requirements
    """
    
    def __init__(self, web3_provider: str, contract_address: str):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=LAIRM_AUDIT_ABI
        )
    
    async def record_action(
        self,
        agent_id: str,
        action: dict,
        previous_hash: str
    ) -> str:
        """Record action to immutable audit log"""
        entry = {
            "agent_id": agent_id,
            "action": action,
            "timestamp": int(time.time()),
            "previous_hash": previous_hash
        }
        
        # Calculate hash
        entry_hash = self._hash_entry(entry)
        
        # Submit to blockchain
        tx_hash = await self.contract.functions.recordAction(
            entry["agent_id"],
            entry["action"],
            entry["timestamp"],
            entry["previous_hash"],
            entry_hash
        ).transact()
        
        return entry_hash
    
    def _hash_entry(self, entry: dict) -> str:
        """Calculate SHA-256 hash of entry"""
        import hashlib
        import json
        return "sha256:" + hashlib.sha256(
            json.dumps(entry, sort_keys=True).encode()
        ).hexdigest()
```

---

## Compliance Engine

### Core Implementation
```python
from dataclasses import dataclass
from typing import List, Dict, Any
from enum import Enum

class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partial"
    PENDING = "pending"

@dataclass
class ComplianceResult:
    axiom: str
    status: ComplianceStatus
    score: float
    violations: List[str]
    recommendations: List[str]

class ComplianceEngine:
    """
    LAIRM Compliance Engine
    Validates agent configurations against axioms
    """
    
    def __init__(self):
        self.axiom_checkers = {
            'I': self._check_supremacia,
            'II': self._check_identitas,
            'III': self._check_responsabilitas,
            'IV': self._check_circulus,
            'V': self._check_interoperabilitas,
            'VI': self._check_auditum,
            'VII': self._check_adaptatio,
            'VIII': self._check_ethica,
            'IX': self._check_gubernatio,
        }
    
    def validate(self, agent_config: Dict[str, Any]) -> Dict[str, ComplianceResult]:
        """Validate agent against all required axioms"""
        results = {}
        
        for axiom in agent_config.get('axioms', []):
            if axiom in self.axiom_checkers:
                results[axiom] = self.axiom_checkers[axiom](agent_config)
        
        return results
    
    def _check_supremacia(self, config: Dict) -> ComplianceResult:
        """Check Ψ-I: Human Supremacy compliance"""
        violations = []
        
        # Check kill-switch
        if not config.get('kill_switch'):
            violations.append("Missing kill-switch configuration")
        
        # Check human override
        if not config.get('human_override_enabled'):
            violations.append("Human override not enabled")
        
        # Check supervision
        if not config.get('supervisor_did'):
            violations.append("No human supervisor assigned")
        
        return ComplianceResult(
            axiom='I',
            status=ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT,
            score=1.0 - (len(violations) * 0.33),
            violations=violations,
            recommendations=self._get_recommendations('I', violations)
        )
    
    # Additional axiom checkers...
```

---

## Decorator Pattern for Agents

```python
from functools import wraps
from typing import List, Callable

def compliant(axioms: List[str]):
    """
    Decorator to enforce LAIRM compliance
    Validates agent action against specified axioms
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Pre-execution compliance check
            agent = args[0] if args else None
            if agent:
                compliance = agent.validate_compliance(axioms)
                if not compliance.is_compliant:
                    raise ComplianceViolationError(
                        f"Action violates axioms: {compliance.violations}"
                    )
            
            # Execute action
            result = await func(*args, **kwargs)
            
            # Post-execution audit
            if agent:
                await agent.audit_action(
                    action=func.__name__,
                    args=args,
                    kwargs=kwargs,
                    result=result
                )
            
            return result
        return wrapper
    return decorator

def auditable(func: Callable):
    """
    Decorator to enable audit trail for agent actions
    Implements Ψ-VI requirements
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        agent = args[0] if args else None
        
        # Pre-action timestamp
        start_time = time.monotonic()
        
        try:
            result = await func(*args, **kwargs)
            
            # Record successful action
            if agent:
                await agent.record_audit({
                    'action': func.__name__,
                    'status': 'success',
                    'duration_ms': (time.monotonic() - start_time) * 1000,
                    'timestamp': datetime.utcnow().isoformat()
                })
            
            return result
            
        except Exception as e:
            # Record failed action
            if agent:
                await agent.record_audit({
                    'action': func.__name__,
                    'status': 'failed',
                    'error': str(e),
                    'duration_ms': (time.monotonic() - start_time) * 1000,
                    'timestamp': datetime.utcnow().isoformat()
                })
            raise
    
    return wrapper

def supervised(escalation_threshold: float = 0.8):
    """
    Decorator to enforce human supervision
    Implements Ψ-IV requirements
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            agent = args[0] if args else None
            
            # Check confidence level
            confidence = kwargs.get('confidence', 1.0)
            
            if confidence < escalation_threshold:
                # Escalate to human supervisor
                if agent:
                    approval = await agent.request_human_approval(
                        action=func.__name__,
                        args=args,
                        kwargs=kwargs,
                        reason=f"Low confidence: {confidence}"
                    )
                    
                    if not approval.granted:
                        raise HumanRejectionError(
                            f"Human supervisor rejected action: {approval.reason}"
                        )
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
```

---

## CLI Commands

```bash
# Validate LAIRM structure
lairm validate

# Search articles
lairm search --axiom I --query "kill-switch"

# Generate compliance report
lairm generate --type compliance --output report.json

# Audit framework
lairm audit --all --verbose

# Create agent passport
lairm passport create --name "MyAgent" --axioms I,II,III

# Verify compliance
lairm compliance check --config agent.yaml

# Start MCP server
lairm mcp start --port 8080
```

---

## File Locations

```
03-TECHNICAL-ANNEXES/
├── specifications/
│   ├── kill-switch-spec.md
│   ├── did-agent-spec.md
│   ├── mcp-protocol-spec.md
│   ├── a2a-protocol-spec.md
│   └── audit-log-spec.md
├── implementations/
│   ├── python/
│   │   ├── lairm_core.py
│   │   ├── compliance_engine.py
│   │   └── audit_engine.py
│   ├── rust/
│   ├── go/
│   └── solidity/
└── schemas/
    ├── agent-passport-schema.json
    ├── audit-log-schema.json
    ├── kill-signal-schema.json
    ├── compliance-report-schema.json
    └── action-record-schema.json
```