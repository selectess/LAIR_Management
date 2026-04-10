"""
---
title: "LAIRM Workflow Example - Reference Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Workflow Example - Reference Implementation

This module demonstrates LAIRM-compliant multi-agent workflow orchestration,
showing how multiple agents can collaborate while maintaining compliance
and audit trails.

Features demonstrated:
- Multi-agent workflow orchestration
- Agent registration and management
- Step-by-step workflow execution
- Compliance verification at each step
- Comprehensive audit trail for entire workflow
- Error handling and workflow recovery

This serves as a reference implementation for developers building
LAIRM-compliant multi-agent systems and workflows.
"""

import sys
import logging
from typing import Dict, List, Any
from datetime import datetime

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


class WorkflowStep:
    """Represents a step in a LAIRM workflow"""
    
    def __init__(self, step_id: str, step_name: str, agent_id: str, 
                 action: str, params: Dict[str, Any]):
        self.step_id = step_id
        self.step_name = step_name
        self.agent_id = agent_id
        self.action = action
        self.params = params
        self.status = "pending"
        self.result = None
        self.error = None
        self.executed_at = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "step_id": self.step_id,
            "step_name": self.step_name,
            "agent_id": self.agent_id,
            "action": self.action,
            "status": self.status,
            "result": self.result,
            "error": self.error,
            "executed_at": self.executed_at
        }


class LAIRMWorkflow:
    """LAIRM-compliant workflow orchestrator"""
    
    def __init__(self, workflow_id: str, workflow_name: str):
        self.workflow_id = workflow_id
        self.workflow_name = workflow_name
        self.steps: List[WorkflowStep] = []
        self.agents: Dict[str, LAIRMFramework] = {}
        self.audit_engine = LAIRMAuditEngine(workflow_id)
        self.created_at = datetime.utcnow().isoformat()
        self.status = "created"
        
        logger.info(f"Workflow {workflow_name} created")
    
    def register_agent(self, agent_id: str, agent_name: str) -> None:
        """Register an agent in the workflow"""
        framework = LAIRMFramework(agent_id, agent_name)
        self.agents[agent_id] = framework
        
        logger.info(f"Agent {agent_name} registered in workflow")
    
    def add_step(self, step_id: str, step_name: str, agent_id: str,
                action: str, params: Dict[str, Any]) -> None:
        """Add a step to the workflow"""
        
        if agent_id not in self.agents:
            raise ValueError(f"Agent {agent_id} not registered")
        
        step = WorkflowStep(step_id, step_name, agent_id, action, params)
        self.steps.append(step)
        
        logger.info(f"Step {step_name} added to workflow")
    
    def execute(self) -> Dict[str, Any]:
        """Execute the workflow"""
        
        logger.info(f"Starting workflow execution: {self.workflow_name}")
        self.status = "executing"
        
        results = {
            "workflow_id": self.workflow_id,
            "workflow_name": self.workflow_name,
            "started_at": datetime.utcnow().isoformat(),
            "steps": [],
            "status": "success",
            "errors": []
        }
        
        for step in self.steps:
            try:
                logger.info(f"Executing step: {step.step_name}")
                
                # Get agent
                agent = self.agents[step.agent_id]
                
                # Check compliance
                axiomes = [ax.value for ax in AxiomeType]
                compliance = agent.check_compliance(axiomes)
                
                if compliance["status"] != "compliant":
                    raise RuntimeError(f"Agent {step.agent_id} is not compliant")
                
                # Execute action
                result = agent.execute_action(step.action, step.params)
                
                step.status = "completed"
                step.result = result
                step.executed_at = datetime.utcnow().isoformat()
                
                # Record in audit
                self.audit_engine.record_action(
                    f"workflow_step_{step.step_id}",
                    step.params,
                    "success"
                )
                
                logger.info(f"Step {step.step_name} completed successfully")
            
            except Exception as e:
                step.status = "failed"
                step.error = str(e)
                step.executed_at = datetime.utcnow().isoformat()
                
                results["status"] = "failed"
                results["errors"].append({
                    "step": step.step_name,
                    "error": str(e)
                })
                
                # Record error in audit
                self.audit_engine.record_error(
                    type(e).__name__,
                    str(e),
                    None
                )
                
                logger.error(f"Step {step.step_name} failed: {str(e)}")
                
                # Stop workflow on error
                break
            
            results["steps"].append(step.to_dict())
        
        self.status = "completed"
        results["completed_at"] = datetime.utcnow().isoformat()
        
        logger.info(f"Workflow execution completed with status: {results['status']}")
        
        return results
    
    def get_audit_trail(self) -> Dict[str, Any]:
        """Get workflow audit trail"""
        return self.audit_engine.generate_audit_report()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert workflow to dictionary"""
        return {
            "workflow_id": self.workflow_id,
            "workflow_name": self.workflow_name,
            "created_at": self.created_at,
            "status": self.status,
            "agents": list(self.agents.keys()),
            "steps": [step.to_dict() for step in self.steps]
        }


def main():
    """Main workflow example"""
    
    logger.info("=" * 60)
    logger.info("LAIRM Workflow Example")
    logger.info("=" * 60)
    
    # Create workflow
    workflow = LAIRMWorkflow("workflow-001", "DataProcessingPipeline")
    
    # Register agents
    logger.info("\n--- Registering Agents ---\n")
    workflow.register_agent("agent-extractor", "DataExtractor")
    workflow.register_agent("agent-transformer", "DataTransformer")
    workflow.register_agent("agent-validator", "DataValidator")
    workflow.register_agent("agent-loader", "DataLoader")
    
    # Add workflow steps
    logger.info("\n--- Adding Workflow Steps ---\n")
    
    workflow.add_step(
        "step-1",
        "Extract Data",
        "agent-extractor",
        "extract",
        {"source": "database-001", "query": "SELECT * FROM data"}
    )
    
    workflow.add_step(
        "step-2",
        "Transform Data",
        "agent-transformer",
        "transform",
        {"format": "json", "schema": "standard"}
    )
    
    workflow.add_step(
        "step-3",
        "Validate Data",
        "agent-validator",
        "validate",
        {"rules": ["required_fields", "data_types"]}
    )
    
    workflow.add_step(
        "step-4",
        "Load Data",
        "agent-loader",
        "load",
        {"destination": "warehouse-001", "mode": "append"}
    )
    
    # Execute workflow
    logger.info("\n--- Executing Workflow ---\n")
    execution_result = workflow.execute()
    
    # Display results
    logger.info("\n--- Execution Results ---\n")
    logger.info(f"Workflow Status: {execution_result['status']}")
    logger.info(f"Steps Executed: {len(execution_result['steps'])}")
    
    for step in execution_result['steps']:
        logger.info(f"  - {step['step_name']}: {step['status']}")
    
    if execution_result['errors']:
        logger.info("\nErrors:")
        for error in execution_result['errors']:
            logger.info(f"  - {error['step']}: {error['error']}")
    
    # Get audit trail
    logger.info("\n--- Audit Trail ---\n")
    audit_report = workflow.get_audit_trail()
    logger.info(f"Total audit entries: {audit_report['audit_log']['entry_count']}")
    logger.info(f"Audit integrity verified: {audit_report['integrity_verified']}")
    
    logger.info("\n" + "=" * 60)
    logger.info("Workflow example completed")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
