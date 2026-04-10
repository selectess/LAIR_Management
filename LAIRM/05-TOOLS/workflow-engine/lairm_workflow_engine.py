#!/usr/bin/env python3
"""
LAIRM Workflow Engine
Orchestration des workflows LAIRM
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Callable
from enum import Enum
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from compliance_checker.lairm_compliance_checker import LAIRMComplianceChecker

logger = logging.getLogger(__name__)
from audit_engine.lairm_audit_engine import LAIRMAuditEngine


class WorkflowStatus(Enum):
    """Statut d'un workflow"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    ESCALATED = "escalated"


class LAIRMWorkflowEngine:
    """Moteur de workflows LAIRM"""

    def __init__(self):
        self.compliance_checker = LAIRMComplianceChecker()
        self.audit_engine = LAIRMAuditEngine()
        self.workflows = []
        self.callbacks = {}

    def create_workflow(
        self,
        workflow_id: str,
        workflow_type: str,
        agent_id: str,
        data: Dict = None
    ) -> Dict[str, Any]:
        """Créer un workflow"""

        workflow = {
            'id': workflow_id,
            'type': workflow_type,
            'agent_id': agent_id,
            'status': WorkflowStatus.PENDING.value,
            'created_at': datetime.now().isoformat(),
            'data': data or {},
            'steps': [],
            'result': None
        }

        self.workflows.append(workflow)
        return workflow

    def compliance_workflow(self, agent_config: Dict) -> Dict[str, Any]:
        """Workflow de vérification de conformité"""

        workflow = self.create_workflow(
            workflow_id=f"compliance-{agent_config['agent_id']}",
            workflow_type='compliance',
            agent_id=agent_config['agent_id'],
            data=agent_config
        )

        workflow['status'] = WorkflowStatus.RUNNING.value

        # Étape 1: Vérifier conformité
        compliance_result = self.compliance_checker.check_agent_compliance(agent_config)
        workflow['steps'].append({
            'name': 'check_compliance',
            'status': 'completed',
            'result': compliance_result
        })

        # Étape 2: Auditer vérification
        audit_record = self.audit_engine.audit_compliance_check(
            agent_config['agent_id'],
            compliance_result
        )
        workflow['steps'].append({
            'name': 'audit_compliance',
            'status': 'completed',
            'result': audit_record
        })

        # Étape 3: Déterminer résultat
        if compliance_result['compliant']:
            workflow['status'] = WorkflowStatus.COMPLETED.value
            workflow['result'] = 'COMPLIANT'
        else:
            if compliance_result['score'] < 50:
                workflow['status'] = WorkflowStatus.ESCALATED.value
                workflow['result'] = 'ESCALATED_TO_HUMAN'
            else:
                workflow['status'] = WorkflowStatus.COMPLETED.value
                workflow['result'] = 'NON_COMPLIANT_REMEDIABLE'

        return workflow

    def audit_workflow(self, agent_id: str, action: Dict) -> Dict[str, Any]:
        """Workflow d'audit d'action"""

        workflow = self.create_workflow(
            workflow_id=f"audit-{agent_id}-{datetime.now().timestamp()}",
            workflow_type='audit',
            agent_id=agent_id,
            data=action
        )

        workflow['status'] = WorkflowStatus.RUNNING.value

        # Étape 1: Auditer action
        audit_record = self.audit_engine.audit_agent_action(agent_id, action)
        workflow['steps'].append({
            'name': 'audit_action',
            'status': 'completed',
            'result': audit_record
        })

        # Étape 2: Vérifier intégrité
        chain_valid = self.audit_engine.verify_audit_chain()
        workflow['steps'].append({
            'name': 'verify_chain',
            'status': 'completed',
            'result': {'chain_valid': chain_valid}
        })

        workflow['status'] = WorkflowStatus.COMPLETED.value
        workflow['result'] = 'AUDITED'

        return workflow

    def approval_workflow(
        self,
        agent_id: str,
        action: Dict,
        approval_callback: Callable = None
    ) -> Dict[str, Any]:
        """Workflow d'approbation humaine"""

        workflow = self.create_workflow(
            workflow_id=f"approval-{agent_id}",
            workflow_type='approval',
            agent_id=agent_id,
            data=action
        )

        workflow['status'] = WorkflowStatus.RUNNING.value

        # Étape 1: Préparer pour approbation
        workflow['steps'].append({
            'name': 'prepare_approval',
            'status': 'completed',
            'result': {
                'action': action.get('type'),
                'requires_approval': True
            }
        })

        # Étape 2: Attendre approbation
        approved = False
        if approval_callback:
            approved = approval_callback(action)

        workflow['steps'].append({
            'name': 'wait_approval',
            'status': 'completed',
            'result': {'approved': approved}
        })

        # Étape 3: Auditer décision
        audit_record = self.audit_engine.create_audit_record(
            agent_id=agent_id,
            action_type='approval_decision',
            details={'approved': approved}
        )
        workflow['steps'].append({
            'name': 'audit_decision',
            'status': 'completed',
            'result': audit_record
        })

        workflow['status'] = WorkflowStatus.COMPLETED.value
        workflow['result'] = 'APPROVED' if approved else 'REJECTED'

        return workflow

    def escalation_workflow(
        self,
        agent_id: str,
        reason: str,
        escalation_callback: Callable = None
    ) -> Dict[str, Any]:
        """Workflow d'escalade"""

        workflow = self.create_workflow(
            workflow_id=f"escalation-{agent_id}",
            workflow_type='escalation',
            agent_id=agent_id,
            data={'reason': reason}
        )

        workflow['status'] = WorkflowStatus.RUNNING.value

        # Étape 1: Créer incident
        workflow['steps'].append({
            'name': 'create_incident',
            'status': 'completed',
            'result': {'incident_created': True}
        })

        # Étape 2: Auditer escalade
        audit_record = self.audit_engine.audit_incident(
            agent_id=agent_id,
            incident_type='escalation',
            description=reason,
            severity='high'
        )
        workflow['steps'].append({
            'name': 'audit_escalation',
            'status': 'completed',
            'result': audit_record
        })

        # Étape 3: Notifier humain
        if escalation_callback:
            escalation_callback(agent_id, reason)

        workflow['steps'].append({
            'name': 'notify_human',
            'status': 'completed',
            'result': {'notified': True}
        })

        workflow['status'] = WorkflowStatus.ESCALATED.value
        workflow['result'] = 'ESCALATED_TO_HUMAN'

        return workflow

    def get_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """Récupérer un workflow"""
        for workflow in self.workflows:
            if workflow['id'] == workflow_id:
                return workflow
        return None

    def get_workflows_by_agent(self, agent_id: str) -> List[Dict]:
        """Récupérer workflows d'un agent"""
        return [w for w in self.workflows if w['agent_id'] == agent_id]

    def get_statistics(self) -> Dict[str, Any]:
        """Obtenir statistiques"""
        stats = {
            'total_workflows': len(self.workflows),
            'by_status': {},
            'by_type': {}
        }

        for workflow in self.workflows:
            # Par statut
            status = workflow['status']
            if status not in stats['by_status']:
                stats['by_status'][status] = 0
            stats['by_status'][status] += 1

            # Par type
            wf_type = workflow['type']
            if wf_type not in stats['by_type']:
                stats['by_type'][wf_type] = 0
            stats['by_type'][wf_type] += 1

        return stats


def main():
    """Test du moteur de workflows"""
    print("=" * 80)
    print("LAIRM WORKFLOW ENGINE - TEST")
    print("=" * 80)
    print()

    engine = LAIRMWorkflowEngine()

    # Test compliance workflow
    print("Testing compliance workflow...")
    agent_config = {
        'agent_id': 'test-agent-001',
        'axiomes_required': ['I', 'II', 'III'],
        'has_kill_switch': True,
        'public_key': 'pk_xxx',
        'has_audit_trail': True
    }

    workflow = engine.compliance_workflow(agent_config)
    print(f"  Workflow ID: {workflow['id']}")
    print(f"  Status: {workflow['status']}")
    print(f"  Result: {workflow['result']}")
    print()

    # Test audit workflow
    print("Testing audit workflow...")
    action = {
        'type': 'test_action',
        'axiomes_checked': ['I', 'II']
    }

    workflow = engine.audit_workflow('test-agent-001', action)
    print(f"  Workflow ID: {workflow['id']}")
    print(f"  Status: {workflow['status']}")
    print(f"  Result: {workflow['result']}")
    print()

    # Statistiques
    stats = engine.get_statistics()
    print(f"Total workflows: {stats['total_workflows']}")
    print(f"By status: {stats['by_status']}")
    print(f"By type: {stats['by_type']}")
    print()

    print("=" * 80)
    print("✅ LAIRM Workflow Engine is ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
