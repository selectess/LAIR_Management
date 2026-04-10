"""
---
title: "LAIRM Compliance Engine - Python Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Compliance Engine - Python Implementation

This module implements the compliance verification engine for LAIRM framework.

Features:
- Rule-based compliance checking across all LAIRM axioms
- Compliance report generation with violations and warnings
- Support for mandatory, required, recommended, and optional rules
- Comprehensive validation framework with custom validators

The engine validates agent configurations against LAIRM axioms and generates
detailed compliance reports for audit and certification purposes.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Tuple
from enum import Enum

logger = logging.getLogger(__name__)


class AxiomeCompliance(Enum):
    """Axiome compliance levels"""
    MANDATORY = "mandatory"
    REQUIRED = "required"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"


class ComplianceRule:
    """Represents a compliance rule"""
    
    def __init__(self, rule_id: str, axiome: str, description: str, 
                 level: AxiomeCompliance, validator_func=None):
        self.rule_id = rule_id
        self.axiome = axiome
        self.description = description
        self.level = level
        self.validator_func = validator_func
    
    def validate(self, config: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate configuration against rule"""
        if self.validator_func:
            return self.validator_func(config)
        return True, "No validator defined"


class ComplianceReport:
    """Compliance audit report"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.timestamp = datetime.utcnow().isoformat()
        self.axiomes_checked: List[str] = []
        self.violations: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.passed_rules: List[str] = []
    
    def add_violation(self, rule_id: str, axiome: str, message: str) -> None:
        """Add compliance violation"""
        self.violations.append({
            "rule_id": rule_id,
            "axiome": axiome,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    def add_warning(self, rule_id: str, axiome: str, message: str) -> None:
        """Add compliance warning"""
        self.warnings.append({
            "rule_id": rule_id,
            "axiome": axiome,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    def add_passed_rule(self, rule_id: str) -> None:
        """Record passed rule"""
        self.passed_rules.append(rule_id)
    
    def get_status(self) -> str:
        """Get overall compliance status"""
        if self.violations:
            return "non_compliant"
        elif self.warnings:
            return "partial"
        else:
            return "compliant"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert report to dictionary"""
        return {
            "agent_id": self.agent_id,
            "timestamp": self.timestamp,
            "status": self.get_status(),
            "axiomes_checked": self.axiomes_checked,
            "violations": self.violations,
            "warnings": self.warnings,
            "passed_rules": len(self.passed_rules),
            "total_rules": len(self.passed_rules) + len(self.violations) + len(self.warnings)
        }
    
    def to_json(self) -> str:
        """Convert report to JSON"""
        return json.dumps(self.to_dict(), indent=2)


class LAIRMComplianceEngine:
    """Main compliance engine for LAIRM framework"""
    
    def __init__(self):
        self.rules: Dict[str, List[ComplianceRule]] = {}
        self._initialize_default_rules()
    
    def _initialize_default_rules(self) -> None:
        """Initialize default compliance rules"""
        
        # Axiome I - SUPREMATIA: Human supremacy
        self.add_rule(ComplianceRule(
            "I-001",
            "I",
            "Agent must have kill-switch capability",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                "kill_switch" in cfg,
                "Kill-switch not found in configuration"
            )
        ))
        
        self.add_rule(ComplianceRule(
            "I-002",
            "I",
            "Kill-switch must respond within 500ms",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                cfg.get("kill_switch_timeout", 1000) <= 500,
                f"Kill-switch timeout {cfg.get('kill_switch_timeout')}ms exceeds 500ms limit"
            )
        ))
        
        # Axiome II - IDENTITAS: Unique identity
        self.add_rule(ComplianceRule(
            "II-001",
            "II",
            "Agent must have unique passport",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                "agent_id" in cfg and "passport" in cfg,
                "Agent passport not found"
            )
        ))
        
        self.add_rule(ComplianceRule(
            "II-002",
            "II",
            "Passport must include digital signature",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                cfg.get("passport", {}).get("signature") is not None,
                "Passport signature missing"
            )
        ))
        
        # Axiome III - RESPONSABILITAS: Responsibility
        self.add_rule(ComplianceRule(
            "III-001",
            "III",
            "Agent must log all actions",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                "audit_log" in cfg,
                "Audit log not configured"
            )
        ))
        
        # Axiome VI - AUDITUM: Audit trail
        self.add_rule(ComplianceRule(
            "VI-001",
            "VI",
            "Audit log must be immutable",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                cfg.get("audit_log", {}).get("immutable", False),
                "Audit log is not immutable"
            )
        ))
        
        self.add_rule(ComplianceRule(
            "VI-002",
            "VI",
            "Audit entries must include timestamps",
            AxiomeCompliance.MANDATORY,
            lambda cfg: (
                cfg.get("audit_log", {}).get("include_timestamps", False),
                "Audit log does not include timestamps"
            )
        ))
    
    def add_rule(self, rule: ComplianceRule) -> None:
        """Add compliance rule"""
        axiome = rule.axiome
        if axiome not in self.rules:
            self.rules[axiome] = []
        self.rules[axiome].append(rule)
        logger.info(f"Added compliance rule {rule.rule_id} for axiome {axiome}")
    
    def check_compliance(self, agent_config: Dict[str, Any], 
                        axiomes: List[str]) -> ComplianceReport:
        """Check agent compliance with specified axiomes"""
        report = ComplianceReport(agent_config.get("agent_id", "unknown"))
        report.axiomes_checked = axiomes
        
        for axiome in axiomes:
            if axiome not in self.rules:
                logger.warning(f"No rules defined for axiome {axiome}")
                continue
            
            for rule in self.rules[axiome]:
                try:
                    passed, message = rule.validate(agent_config)
                    
                    if passed:
                        report.add_passed_rule(rule.rule_id)
                    else:
                        if rule.level == AxiomeCompliance.MANDATORY:
                            report.add_violation(rule.rule_id, axiome, message)
                        else:
                            report.add_warning(rule.rule_id, axiome, message)
                
                except Exception as e:
                    logger.error(f"Error validating rule {rule.rule_id}: {str(e)}")
                    report.add_warning(rule.rule_id, axiome, f"Validation error: {str(e)}")
        
        logger.info(f"Compliance check completed for agent {agent_config.get('agent_id')}: {report.get_status()}")
        return report
    
    def get_axiome_rules(self, axiome: str) -> List[Dict[str, Any]]:
        """Get all rules for an axiome"""
        if axiome not in self.rules:
            return []
        
        return [
            {
                "rule_id": rule.rule_id,
                "description": rule.description,
                "level": rule.level.value
            }
            for rule in self.rules[axiome]
        ]
    
    def generate_compliance_matrix(self, agent_config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate compliance matrix for all axiomes"""
        axiomes = list(self.rules.keys())
        report = self.check_compliance(agent_config, axiomes)
        
        matrix = {
            "agent_id": agent_config.get("agent_id"),
            "timestamp": datetime.utcnow().isoformat(),
            "axiomes": {}
        }
        
        for axiome in axiomes:
            axiome_rules = self.get_axiome_rules(axiome)
            matrix["axiomes"][axiome] = {
                "total_rules": len(axiome_rules),
                "rules": axiome_rules
            }
        
        return matrix
