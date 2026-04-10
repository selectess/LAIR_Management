"""
---
title: "LAIRM Agent Example - Reference Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Agent Example - Reference Implementation

This module demonstrates how to build a LAIRM-compliant autonomous agent
that integrates all core LAIRM axioms and compliance mechanisms.

Features demonstrated:
- Agent initialization with LAIRM framework
- Compliance verification before task execution
- Full audit trail for all operations
- Kill-switch integration for emergency stops
- Error handling and incident recording

This serves as a reference implementation for developers building
LAIRM-compliant autonomous agents.
"""

import sys
import logging
from typing import Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, '../python')

from lairm_core import LAIRMFramework, AxiomeType
from compliance_engine import LAIRMComplianceEngine
from audit_engine import LAIRMAuditEngine, AuditEventType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LAIRMCompliantAgent:
    """Example of a LAIRM-compliant autonomous agent"""
    
    def __init__(self, agent_name: str):
        """Initialize LAIRM-compliant agent"""
        self.agent_name = agent_name
        self.framework = LAIRMFramework(f"agent-{agent_name.lower()}", agent_name)
        self.compliance_engine = LAIRMComplianceEngine()
        self.audit_engine = LAIRMAuditEngine(self.framework.agent_id)
        
        logger.info(f"Agent {agent_name} initialized with LAIRM framework")
    
    def initialize_compliance(self) -> None:
        """Initialize compliance with all axiomes"""
        axiomes = [ax.value for ax in AxiomeType]
        self.framework.initialize_compliance(axiomes)
        
        logger.info(f"Agent {self.agent_name} initialized for axiomes: {axiomes}")
    
    def verify_compliance(self) -> bool:
        """Verify agent compliance before execution"""
        axiomes = [ax.value for ax in AxiomeType]
        result = self.framework.check_compliance(axiomes)
        
        self.audit_engine.record_compliance_check(axiomes, result["status"])
        
        logger.info(f"Compliance check: {result['status']}")
        return result["status"] == "compliant"
    
    def execute_task(self, task_name: str, task_params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task with full audit trail"""
        
        # Check compliance before execution
        if not self.verify_compliance():
            logger.error(f"Agent {self.agent_name} is not compliant")
            return {
                "status": "error",
                "message": "Agent compliance check failed",
                "task": task_name
            }
        
        # Execute task
        logger.info(f"Executing task: {task_name}")
        
        try:
            # Simulate task execution
            result = self._perform_task(task_name, task_params)
            
            # Record successful action
            self.audit_engine.record_action(task_name, task_params, "success")
            
            logger.info(f"Task {task_name} completed successfully")
            return {
                "status": "success",
                "task": task_name,
                "result": result
            }
        
        except Exception as e:
            # Record error
            self.audit_engine.record_error(
                type(e).__name__,
                str(e),
                None
            )
            
            logger.error(f"Task {task_name} failed: {str(e)}")
            return {
                "status": "error",
                "task": task_name,
                "error": str(e)
            }
    
    def _perform_task(self, task_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Perform the actual task (placeholder)"""
        
        if task_name == "analyze_data":
            return {
                "analysis": "Data analysis completed",
                "records_processed": params.get("record_count", 0)
            }
        
        elif task_name == "generate_report":
            return {
                "report_id": "report-001",
                "generated_at": "2026-03-30T12:00:00Z"
            }
        
        elif task_name == "make_decision":
            return {
                "decision": "approved",
                "confidence": 0.95
            }
        
        else:
            return {"result": "Task executed"}
    
    def get_audit_trail(self) -> Dict[str, Any]:
        """Get complete audit trail"""
        return self.audit_engine.generate_audit_report()
    
    def emergency_stop(self, reason: str = "Emergency") -> Dict[str, Any]:
        """Trigger emergency stop (kill-switch)"""
        logger.critical(f"Emergency stop triggered: {reason}")
        
        result = self.framework.trigger_kill_switch(reason)
        self.audit_engine.record_kill_switch(reason, "system")
        
        return result


def main():
    """Main example execution"""
    
    logger.info("=" * 60)
    logger.info("LAIRM Compliant Agent Example")
    logger.info("=" * 60)
    
    # Create agent
    agent = LAIRMCompliantAgent("DataAnalyzer")
    
    # Initialize compliance
    agent.initialize_compliance()
    
    # Verify compliance
    if not agent.verify_compliance():
        logger.error("Agent failed compliance check")
        return
    
    # Execute tasks
    logger.info("\n--- Executing Tasks ---\n")
    
    # Task 1: Analyze data
    result1 = agent.execute_task("analyze_data", {
        "record_count": 1000,
        "data_source": "database-001"
    })
    logger.info(f"Task 1 result: {result1}")
    
    # Task 2: Generate report
    result2 = agent.execute_task("generate_report", {
        "report_type": "summary",
        "format": "json"
    })
    logger.info(f"Task 2 result: {result2}")
    
    # Task 3: Make decision
    result3 = agent.execute_task("make_decision", {
        "decision_type": "approval",
        "threshold": 0.9
    })
    logger.info(f"Task 3 result: {result3}")
    
    # Get audit trail
    logger.info("\n--- Audit Trail ---\n")
    audit_report = agent.get_audit_trail()
    logger.info(f"Total audit entries: {audit_report['audit_log']['entry_count']}")
    logger.info(f"Audit integrity verified: {audit_report['integrity_verified']}")
    
    # Display audit entries
    for entry in audit_report['audit_log']['entries'][:5]:
        logger.info(f"  - {entry['event_type']}: {entry['timestamp']}")
    
    logger.info("\n" + "=" * 60)
    logger.info("Example completed successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
