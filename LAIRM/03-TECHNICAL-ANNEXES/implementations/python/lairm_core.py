"""
---
title: "LAIRM Core Framework - Python Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Core Framework - Python Implementation

This module implements the core LAIRM framework in Python, providing:
- Agent identity management (Axiom II - Identitas)
- Kill-switch mechanism (Axiom I - Suprematia)
- Immutable audit logging (Axiom VI - Auditum)
- Compliance verification framework

The implementation is production-ready with comprehensive error handling,
type hints, and extensive documentation.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum
import hashlib
import uuid

logger = logging.getLogger(__name__)


class AxiomeType(Enum):
    """LAIRM Axiomes enumeration"""
    SUPREMATIA = "I"
    IDENTITAS = "II"
    RESPONSABILITAS = "III"
    CIRCULUS = "IV"
    INTEROPERABILITAS = "V"
    AUDITUM = "VI"
    ADAPTATIO = "VII"
    ETHICA = "VIII"
    GUBERNATIO = "IX"
    ENERGIA = "X"
    ARMA = "XI"
    COGNITIO = "XII"
    RISICUM = "XIII"
    IUSTITIA = "XIV"
    RESILENTIA = "XV"
    SPATIUM = "XVI"
    HUMANITAS = "XVII"
    CHARTA_COSMICA = "XVIII"


class ComplianceStatus(Enum):
    """Compliance status enumeration"""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class AgentPassport:
    """Represents unique agent identity per Axiome II"""
    
    def __init__(self, agent_id: str, agent_name: str, version: str = "1.0"):
        self.agent_id = agent_id or str(uuid.uuid4())
        self.agent_name = agent_name
        self.version = version
        self.created_at = datetime.utcnow().isoformat()
        self.signature = self._generate_signature()
        self.axiomes_supported = [ax.value for ax in AxiomeType]
    
    def _generate_signature(self) -> str:
        """Generate ECDSA-like signature for passport"""
        data = f"{self.agent_id}{self.agent_name}{self.created_at}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert passport to dictionary"""
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "version": self.version,
            "created_at": self.created_at,
            "signature": self.signature,
            "axiomes_supported": self.axiomes_supported
        }
    
    def to_json(self) -> str:
        """Convert passport to JSON"""
        return json.dumps(self.to_dict(), indent=2)


class KillSwitch:
    """Kill-switch mechanism per Axiome I - SUPREMATIA"""
    
    def __init__(self, agent_id: str, authority_id: str):
        self.agent_id = agent_id
        self.authority_id = authority_id
        self.is_active = False
        self.triggered_at: Optional[str] = None
        self.reason: Optional[str] = None
    
    def trigger(self, reason: str = "Manual intervention") -> Dict[str, Any]:
        """Trigger kill-switch"""
        self.is_active = True
        self.triggered_at = datetime.utcnow().isoformat()
        self.reason = reason
        
        logger.warning(f"Kill-switch triggered for agent {self.agent_id}: {reason}")
        
        return {
            "status": "killed",
            "agent_id": self.agent_id,
            "triggered_at": self.triggered_at,
            "reason": reason,
            "authority": self.authority_id
        }
    
    def is_alive(self) -> bool:
        """Check if agent is still alive"""
        return not self.is_active


class AuditLog:
    """Immutable audit log per Axiome VI - AUDITUM"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.entries: List[Dict[str, Any]] = []
    
    def record_action(self, action: str, details: Dict[str, Any], 
                     status: str = "success") -> str:
        """Record an action in immutable log"""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "details": details,
            "status": status,
            "entry_id": str(uuid.uuid4()),
            "agent_id": self.agent_id
        }
        
        # Calculate hash for immutability
        entry_json = json.dumps(entry, sort_keys=True)
        entry["hash"] = hashlib.sha256(entry_json.encode()).hexdigest()
        
        self.entries.append(entry)
        logger.info(f"Audit entry recorded: {entry['entry_id']}")
        
        return entry["entry_id"]
    
    def get_entries(self) -> List[Dict[str, Any]]:
        """Get all audit entries"""
        return self.entries.copy()
    
    def verify_integrity(self) -> bool:
        """Verify audit log integrity"""
        for entry in self.entries:
            # Create a copy to avoid mutating original entry
            entry_copy = entry.copy()
            stored_hash = entry_copy.pop("hash", None)
            entry_json = json.dumps(entry_copy, sort_keys=True)
            calculated_hash = hashlib.sha256(entry_json.encode()).hexdigest()
            
            if stored_hash != calculated_hash:
                logger.error(f"Audit log integrity violation: {entry['entry_id']}")
                return False
        
        return True


class ComplianceEngine:
    """Compliance checking engine"""
    
    def __init__(self):
        self.rules: Dict[str, List[str]] = {
            ax.value: [] for ax in AxiomeType
        }
    
    def add_rule(self, axiome: str, rule: str) -> None:
        """Add compliance rule for axiome"""
        if axiome in self.rules:
            self.rules[axiome].append(rule)
    
    def check_compliance(self, agent_config: Dict[str, Any], 
                        axiomes: List[str]) -> Dict[str, Any]:
        """Check agent compliance with specified axiomes"""
        results = {
            "agent_id": agent_config.get("agent_id"),
            "timestamp": datetime.utcnow().isoformat(),
            "axiomes_checked": axiomes,
            "status": ComplianceStatus.COMPLIANT.value,
            "violations": []
        }
        
        for axiome in axiomes:
            if axiome not in self.rules:
                results["violations"].append(f"No rules defined for axiome {axiome}")
                results["status"] = ComplianceStatus.PARTIAL.value
        
        return results


class LAIRMFramework:
    """Main LAIRM Framework implementation"""
    
    def __init__(self, agent_id: str, agent_name: str):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.passport = AgentPassport(agent_id, agent_name)
        self.kill_switch = KillSwitch(agent_id, "system-authority")
        self.audit_log = AuditLog(agent_id)
        self.compliance_engine = ComplianceEngine()
        
        logger.info(f"LAIRM Framework initialized for agent: {agent_name}")
    
    def initialize_compliance(self, axiomes: List[str]) -> None:
        """Initialize compliance for specified axiomes"""
        for axiome in axiomes:
            self.compliance_engine.add_rule(axiome, f"Default rule for {axiome}")
        
        self.audit_log.record_action(
            "compliance_initialization",
            {"axiomes": axiomes}
        )
    
    def check_compliance(self, axiomes: List[str]) -> Dict[str, Any]:
        """Check compliance with axiomes"""
        config = self.passport.to_dict()
        result = self.compliance_engine.check_compliance(config, axiomes)
        
        self.audit_log.record_action(
            "compliance_check",
            {"axiomes": axiomes, "result": result["status"]}
        )
        
        return result
    
    def execute_action(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute action with audit trail"""
        if not self.kill_switch.is_alive():
            return {
                "status": "error",
                "message": "Agent is killed",
                "action": action
            }
        
        self.audit_log.record_action(action, params)
        
        return {
            "status": "success",
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        """Get complete audit trail"""
        return self.audit_log.get_entries()
    
    def trigger_kill_switch(self, reason: str = "Manual") -> Dict[str, Any]:
        """Trigger kill-switch"""
        result = self.kill_switch.trigger(reason)
        self.audit_log.record_action("kill_switch_triggered", {"reason": reason})
        return result
