#!/usr/bin/env python3
"""
LAIRM Compliance Checker
Vérificateur automatique de conformité
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class LAIRMComplianceChecker:
    """Vérificateur de conformité LAIRM"""

    def __init__(self, lairm_root: str = "LAIRM"):
        self.lairm_root = Path(lairm_root)
        self.compliance_rules = self.load_rules()

    def load_rules(self) -> Dict[str, List[str]]:
        """Charger les règles de conformité"""
        return {
            'axiome_i_supremacy': [
                'Agent must have kill-switch capability',
                'Agent must respond to human override',
                'Agent must have emergency stop in <500ms'
            ],
            'axiome_ii_identity': [
                'Agent must have unique ID',
                'Agent must have public key',
                'Agent must have audit trail'
            ],
            'axiome_iii_responsibility': [
                'Agent must track responsibility chain',
                'Agent must log all decisions',
                'Agent must support human appeal'
            ],
            'axiome_iv_supervision': [
                'Agent must have continuous monitoring',
                'Agent must report status regularly',
                'Agent must escalate to human if needed'
            ],
            'axiome_v_interoperability': [
                'Agent must support MCP protocol',
                'Agent must support A2A protocol',
                'Agent must have documented API'
            ]
        }

    def check_agent_compliance(self, agent_config: Dict) -> Dict[str, Any]:
        """Vérifier conformité d'un agent"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_config.get('agent_id', 'unknown'),
            'compliant': True,
            'axiomes': {},
            'violations': [],
            'warnings': [],
            'score': 0
        }

        # Vérifier axiomes requis
        required_axiomes = agent_config.get('axiomes_required', [])

        for axiome in required_axiomes:
            axiome_key = f'axiome_{axiome.lower()}_*'

            # Chercher règles pour cet axiome
            matching_rules = [
                (k, v) for k, v in self.compliance_rules.items()
                if axiome.lower() in k
            ]

            if matching_rules:
                axiome_compliant = True
                violations = []

                for rule_name, rules in matching_rules:
                    for rule in rules:
                        # Vérifier chaque règle
                        if not self.check_rule(agent_config, rule):
                            axiome_compliant = False
                            violations.append(rule)

                report['axiomes'][axiome] = {
                    'compliant': axiome_compliant,
                    'violations': violations
                }

                if not axiome_compliant:
                    report['compliant'] = False
                    report['violations'].extend(violations)
            else:
                report['warnings'].append(f"No rules found for axiome {axiome}")

        # Calculer score
        if report['compliant']:
            report['score'] = 100
        else:
            total_violations = len(report['violations'])
            report['score'] = max(0, 100 - (total_violations * 10))

        return report

    def check_rule(self, agent_config: Dict, rule: str) -> bool:
        """Vérifier une règle"""
        # Vérifications simples
        if 'kill-switch' in rule.lower():
            return agent_config.get('has_kill_switch', False)

        if 'unique id' in rule.lower():
            return 'agent_id' in agent_config

        if 'public key' in rule.lower():
            return 'public_key' in agent_config

        if 'audit trail' in rule.lower():
            return agent_config.get('has_audit_trail', False)

        if 'mcp' in rule.lower():
            return agent_config.get('supports_mcp', False)

        if 'api' in rule.lower():
            return agent_config.get('has_api', False)

        # Par défaut, considérer comme conforme
        return True

    def check_action_compliance(self, agent_id: str, action: Dict) -> Dict[str, Any]:
        """Vérifier conformité d'une action"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'action_type': action.get('type', 'unknown'),
            'compliant': True,
            'checks': {},
            'violations': []
        }

        # Vérifier axiomes requis pour cette action
        required_axiomes = action.get('axiomes_required', [])

        for axiome in required_axiomes:
            check_result = self.check_axiome_for_action(axiome, action)
            report['checks'][axiome] = check_result

            if not check_result['compliant']:
                report['compliant'] = False
                report['violations'].extend(check_result['violations'])

        return report

    def check_axiome_for_action(self, axiome: str, action: Dict) -> Dict[str, Any]:
        """Vérifier axiome pour une action"""
        result = {
            'axiome': axiome,
            'compliant': True,
            'violations': []
        }

        # Vérifications spécifiques par axiome
        if axiome == 'I':
            # Supremacy: vérifier que l'action peut être arrêtée
            if not action.get('can_be_stopped', False):
                result['compliant'] = False
                result['violations'].append('Action must be stoppable')

        elif axiome == 'II':
            # Identity: vérifier que l'agent est identifié
            if not action.get('agent_id'):
                result['compliant'] = False
                result['violations'].append('Agent must be identified')

        elif axiome == 'III':
            # Responsibility: vérifier que la responsabilité est tracée
            if not action.get('responsibility_chain'):
                result['compliant'] = False
                result['violations'].append('Responsibility chain must be traced')

        elif axiome == 'IV':
            # Supervision: vérifier que l'action est supervisée
            if not action.get('supervised', False):
                result['compliant'] = False
                result['violations'].append('Action must be supervised')

        elif axiome == 'V':
            # Interoperability: vérifier que l'action est interopérable
            if not action.get('interoperable', False):
                result['compliant'] = False
                result['violations'].append('Action must be interoperable')

        return result

    def generate_compliance_report(self, agent_config: Dict) -> str:
        """Générer rapport de conformité"""
        compliance = self.check_agent_compliance(agent_config)

        report = f"""
COMPLIANCE REPORT
=================

Agent ID: {compliance['agent_id']}
Timestamp: {compliance['timestamp']}
Overall Compliant: {compliance['compliant']}
Compliance Score: {compliance['score']}/100

Axiomes:
"""

        for axiome, status in compliance['axiomes'].items():
            compliant_status = '✅ COMPLIANT' if status['compliant'] else '❌ NON-COMPLIANT'
            report += f"\n  {axiome}: {compliant_status}\n"
            if status['violations']:
                for violation in status['violations']:
                    report += f"    - {violation}\n"

        if compliance['violations']:
            report += f"\nViolations ({len(compliance['violations'])}):\n"
            for violation in compliance['violations']:
                report += f"  - {violation}\n"

        if compliance['warnings']:
            report += f"\nWarnings ({len(compliance['warnings'])}):\n"
            for warning in compliance['warnings']:
                report += f"  - {warning}\n"

        return report


def main():
    """Test du vérificateur"""
    print("=" * 80)
    print("LAIRM COMPLIANCE CHECKER - TEST")
    print("=" * 80)
    print()

    checker = LAIRMComplianceChecker()

    # Test agent conforme
    compliant_agent = {
        'agent_id': 'agent-001',
        'axiomes_required': ['I', 'II', 'III'],
        'has_kill_switch': True,
        'public_key': 'pk_xxx',
        'has_audit_trail': True,
        'supports_mcp': True,
        'has_api': True
    }

    print("Testing compliant agent:")
    report = checker.check_agent_compliance(compliant_agent)
    print(checker.generate_compliance_report(compliant_agent))

    # Test agent non-conforme
    non_compliant_agent = {
        'agent_id': 'agent-002',
        'axiomes_required': ['I', 'II', 'III'],
        'has_kill_switch': False,
        'has_audit_trail': False
    }

    print("\nTesting non-compliant agent:")
    report = checker.check_agent_compliance(non_compliant_agent)
    print(checker.generate_compliance_report(non_compliant_agent))

    print("=" * 80)
    print("✅ LAIRM Compliance Checker is ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
