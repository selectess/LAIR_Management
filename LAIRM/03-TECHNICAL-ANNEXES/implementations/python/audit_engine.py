"""
---
title: "LAIRM Audit Engine - Python Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Audit Engine - Python Implementation

This module implements the audit trail management engine for LAIRM framework,
implementing Axiom VI (Auditum) - Immutable audit logging.

Features:
- Immutable audit entries with SHA-256 hash verification
- Chain hashing for log integrity
- Multiple event types (actions, compliance checks, incidents, errors)
- Incident response logging and tracking
- Comprehensive audit report generation
- Full integrity verification

The engine ensures complete traceability and tamper-proof audit trails
for all agent operations.
"""

import json
import logging
import hashlib
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum
import uuid

logger = logging.getLogger(__name__)


class AuditEventType(Enum):
    """Types of audit events"""
    ACTION_EXECUTED = "action_executed"
    COMPLIANCE_CHECK = "compliance_check"
    KILL_SWITCH_TRIGGERED = "kill_switch_triggered"
    CONFIGURATION_CHANGED = "configuration_changed"
    AUTHENTICATION_ATTEMPT = "authentication_attempt"
    AUTHORIZATION_DECISION = "authorization_decision"
    ERROR_OCCURRED = "error_occurred"
    INCIDENT_DETECTED = "incident_detected"


class AuditEntry:
    """Immutable audit entry"""
    
    def __init__(self, agent_id: str, event_type: AuditEventType, 
                 details: Dict[str, Any], severity: str = "info"):
        self.entry_id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.event_type = event_type.value
        self.timestamp = datetime.utcnow().isoformat()
        self.details = details
        self.severity = severity
        self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        """Calculate SHA-256 hash for immutability"""
        data = {
            "entry_id": self.entry_id,
            "agent_id": self.agent_id,
            "event_type": self.event_type,
            "timestamp": self.timestamp,
            "details": self.details,
            "severity": self.severity
        }
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "entry_id": self.entry_id,
            "agent_id": self.agent_id,
            "event_type": self.event_type,
            "timestamp": self.timestamp,
            "details": self.details,
            "severity": self.severity,
            "hash": self.hash
        }
    
    def verify_integrity(self) -> bool:
        """Verify entry integrity"""
        original_hash = self.hash
        recalculated_hash = self._calculate_hash()
        return original_hash == recalculated_hash


class AuditLog:
    """Immutable audit log per Axiome VI"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.entries: List[AuditEntry] = []
        self.created_at = datetime.utcnow().isoformat()
        self.chain_hash = ""
    
    def add_entry(self, event_type: AuditEventType, details: Dict[str, Any],
                  severity: str = "info") -> str:
        """Add entry to audit log"""
        entry = AuditEntry(self.agent_id, event_type, details, severity)
        self.entries.append(entry)
        self._update_chain_hash()
        
        logger.info(f"Audit entry added: {entry.entry_id} ({event_type.value})")
        return entry.entry_id
    
    def _update_chain_hash(self) -> None:
        """Update chain hash for log integrity"""
        if not self.entries:
            self.chain_hash = ""
            return
        
        last_entry = self.entries[-1]
        chain_data = f"{self.chain_hash}{last_entry.hash}"
        self.chain_hash = hashlib.sha256(chain_data.encode()).hexdigest()
    
    def get_entries(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get audit entries"""
        entries = [entry.to_dict() for entry in self.entries]
        if limit:
            return entries[-limit:]
        return entries
    
    def verify_integrity(self) -> bool:
        """Verify entire log integrity"""
        for entry in self.entries:
            if not entry.verify_integrity():
                logger.error(f"Integrity violation in entry {entry.entry_id}")
                return False
        
        # Verify chain integrity
        recalculated_chain = ""
        for entry in self.entries:
            chain_data = f"{recalculated_chain}{entry.hash}"
            recalculated_chain = hashlib.sha256(chain_data.encode()).hexdigest()
        
        if recalculated_chain != self.chain_hash:
            logger.error("Chain integrity violation detected")
            return False
        
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert log to dictionary"""
        return {
            "agent_id": self.agent_id,
            "created_at": self.created_at,
            "entry_count": len(self.entries),
            "chain_hash": self.chain_hash,
            "entries": self.get_entries()
        }


class IncidentLog:
    """Incident response log"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.incidents: List[Dict[str, Any]] = []
    
    def record_incident(self, incident_type: str, description: str,
                       severity: str, response: str) -> str:
        """Record security incident"""
        incident_id = str(uuid.uuid4())
        incident = {
            "incident_id": incident_id,
            "agent_id": self.agent_id,
            "type": incident_type,
            "description": description,
            "severity": severity,
            "response": response,
            "timestamp": datetime.utcnow().isoformat(),
            "resolved": False
        }
        
        self.incidents.append(incident)
        logger.warning(f"Incident recorded: {incident_id} ({incident_type})")
        return incident_id
    
    def resolve_incident(self, incident_id: str, resolution: str) -> bool:
        """Mark incident as resolved"""
        for incident in self.incidents:
            if incident["incident_id"] == incident_id:
                incident["resolved"] = True
                incident["resolution"] = resolution
                incident["resolved_at"] = datetime.utcnow().isoformat()
                logger.info(f"Incident resolved: {incident_id}")
                return True
        
        return False
    
    def get_incidents(self, unresolved_only: bool = False) -> List[Dict[str, Any]]:
        """Get incidents"""
        if unresolved_only:
            return [i for i in self.incidents if not i.get("resolved", False)]
        return self.incidents.copy()


class LAIRMAuditEngine:
    """Main audit engine for LAIRM framework"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.audit_log = AuditLog(agent_id)
        self.incident_log = IncidentLog(agent_id)
    
    def record_action(self, action: str, params: Dict[str, Any],
                     result: str = "success") -> str:
        """Record agent action"""
        details = {
            "action": action,
            "parameters": params,
            "result": result
        }
        
        return self.audit_log.add_entry(
            AuditEventType.ACTION_EXECUTED,
            details,
            "info"
        )
    
    def record_compliance_check(self, axiomes: List[str],
                               status: str) -> str:
        """Record compliance check"""
        details = {
            "axiomes": axiomes,
            "status": status
        }
        
        return self.audit_log.add_entry(
            AuditEventType.COMPLIANCE_CHECK,
            details,
            "info"
        )
    
    def record_kill_switch(self, reason: str, authority: str) -> str:
        """Record kill-switch trigger"""
        details = {
            "reason": reason,
            "authority": authority
        }
        
        return self.audit_log.add_entry(
            AuditEventType.KILL_SWITCH_TRIGGERED,
            details,
            "critical"
        )
    
    def record_error(self, error_type: str, message: str,
                    traceback: Optional[str] = None) -> str:
        """Record error"""
        details = {
            "error_type": error_type,
            "message": message,
            "traceback": traceback
        }
        
        return self.audit_log.add_entry(
            AuditEventType.ERROR_OCCURRED,
            details,
            "error"
        )
    
    def record_incident(self, incident_type: str, description: str,
                       severity: str, response: str) -> str:
        """Record security incident"""
        return self.incident_log.record_incident(
            incident_type, description, severity, response
        )
    
    def get_audit_trail(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get audit trail"""
        return self.audit_log.get_entries(limit)
    
    def verify_audit_integrity(self) -> bool:
        """Verify audit log integrity"""
        return self.audit_log.verify_integrity()
    
    def generate_audit_report(self) -> Dict[str, Any]:
        """Generate comprehensive audit report"""
        return {
            "agent_id": self.agent_id,
            "timestamp": datetime.utcnow().isoformat(),
            "audit_log": self.audit_log.to_dict(),
            "incidents": self.incident_log.get_incidents(),
            "integrity_verified": self.verify_audit_integrity()
        }
