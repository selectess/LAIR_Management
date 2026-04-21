# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

#!/usr/bin/env python3
"""
LAIRM Audit Engine
Moteur d'audit immuable pour traçabilité complète
"""

import json
import hashlib
import logging
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class LAIRMAuditEngine:
    """Moteur d'audit LAIRM"""

    def __init__(self, storage_path: str = "LAIRM/audit-logs"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.audit_chain = []

    def create_audit_record(
        self,
        agent_id: str,
        action_type: str,
        details: Dict = None,
        axiomes: List[str] = None
    ) -> Dict[str, Any]:
        """Créer un enregistrement d'audit"""

        record = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'action_type': action_type,
            'details': details or {},
            'axiomes': axiomes or [],
            'sequence': len(self.audit_chain) + 1
        }

        # Calculer hash du record précédent
        if self.audit_chain:
            previous_hash = self.audit_chain[-1]['hash']
        else:
            previous_hash = '0' * 64

        record['previous_hash'] = previous_hash

        # Calculer hash du record courant
        record_str = json.dumps(record, sort_keys=True)
        record['hash'] = hashlib.sha256(record_str.encode()).hexdigest()

        # Ajouter à la chaîne
        self.audit_chain.append(record)

        return record

    def audit_agent_action(
        self,
        agent_id: str,
        action: Dict
    ) -> Dict[str, Any]:
        """Auditer une action d'agent"""

        audit_record = self.create_audit_record(
            agent_id=agent_id,
            action_type=action.get('type', 'unknown'),
            details={
                'action': action.get('type'),
                'parameters': action.get('parameters', {}),
                'result': action.get('result'),
                'duration_ms': action.get('duration_ms')
            },
            axiomes=action.get('axiomes_checked', [])
        )

        return audit_record

    def audit_compliance_check(
        self,
        agent_id: str,
        compliance_result: Dict
    ) -> Dict[str, Any]:
        """Auditer une vérification de conformité"""

        audit_record = self.create_audit_record(
            agent_id=agent_id,
            action_type='compliance_check',
            details={
                'compliant': compliance_result.get('compliant'),
                'score': compliance_result.get('score'),
                'violations': compliance_result.get('violations', [])
            },
            axiomes=list(compliance_result.get('axiomes', {}).keys())
        )

        return audit_record

    def audit_incident(
        self,
        agent_id: str,
        incident_type: str,
        description: str,
        severity: str = 'medium'
    ) -> Dict[str, Any]:
        """Auditer un incident"""

        audit_record = self.create_audit_record(
            agent_id=agent_id,
            action_type='incident',
            details={
                'incident_type': incident_type,
                'description': description,
                'severity': severity,
                'timestamp': datetime.now().isoformat()
            }
        )

        return audit_record

    def verify_audit_chain(self) -> bool:
        """Vérifier l'intégrité de la chaîne d'audit"""

        for i, record in enumerate(self.audit_chain):
            # Vérifier hash du record
            record_copy = record.copy()
            record_hash = record_copy.pop('hash')
            record_str = json.dumps(record_copy, sort_keys=True)
            calculated_hash = hashlib.sha256(record_str.encode()).hexdigest()

            if record_hash != calculated_hash:
                return False

            # Vérifier lien avec record précédent
            if i > 0:
                previous_record = self.audit_chain[i - 1]
                if record['previous_hash'] != previous_record['hash']:
                    return False

        return True

    def get_audit_trail(
        self,
        agent_id: str = None,
        action_type: str = None,
        start_time: str = None,
        end_time: str = None
    ) -> List[Dict]:
        """Obtenir la trace d'audit"""

        results = []

        for record in self.audit_chain:
            # Filtrer par agent_id
            if agent_id and record['agent_id'] != agent_id:
                continue

            # Filtrer par action_type
            if action_type and record['action_type'] != action_type:
                continue

            # Filtrer par temps
            if start_time and record['timestamp'] < start_time:
                continue

            if end_time and record['timestamp'] > end_time:
                continue

            results.append(record)

        return results

    def generate_audit_report(self, agent_id: str) -> str:
        """Générer rapport d'audit"""

        trail = self.get_audit_trail(agent_id=agent_id)

        report = f"""
AUDIT REPORT
============

Agent ID: {agent_id}
Report Generated: {datetime.now().isoformat()}
Total Records: {len(trail)}
Chain Integrity: {'✅ VALID' if self.verify_audit_chain() else '❌ INVALID'}

Audit Trail:
"""

        for record in trail:
            report += f"\n  [{record['sequence']}] {record['timestamp']}\n"
            report += f"    Action: {record['action_type']}\n"
            report += f"    Axiomes: {', '.join(record['axiomes']) or 'None'}\n"
            report += f"    Hash: {record['hash'][:16]}...\n"

        return report

    def save_audit_log(self, agent_id: str) -> Path:
        """Sauvegarder le log d'audit"""

        trail = self.get_audit_trail(agent_id=agent_id)

        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        filename = self.storage_path / f"audit-{agent_id}-{timestamp}.json"

        with open(filename, 'w') as f:
            json.dump(trail, f, indent=2)

        return filename

    def get_statistics(self) -> Dict[str, Any]:
        """Obtenir statistiques d'audit"""

        stats = {
            'total_records': len(self.audit_chain),
            'chain_valid': self.verify_audit_chain(),
            'agents': {},
            'action_types': {}
        }

        for record in self.audit_chain:
            # Compter par agent
            agent_id = record['agent_id']
            if agent_id not in stats['agents']:
                stats['agents'][agent_id] = 0
            stats['agents'][agent_id] += 1

            # Compter par type d'action
            action_type = record['action_type']
            if action_type not in stats['action_types']:
                stats['action_types'][action_type] = 0
            stats['action_types'][action_type] += 1

        return stats


def main():
    """Test du moteur d'audit"""
    print("=" * 80)
    print("LAIRM AUDIT ENGINE - TEST")
    print("=" * 80)
    print()

    engine = LAIRMAuditEngine()

    # Créer quelques enregistrements d'audit
    print("Creating audit records...")

    for i in range(5):
        record = engine.create_audit_record(
            agent_id='agent-001',
            action_type='action',
            details={'index': i},
            axiomes=['I', 'II', 'III']
        )
        print(f"  Record {i+1}: {record['hash'][:16]}...")

    print()

    # Vérifier intégrité
    print(f"Chain integrity: {'✅ VALID' if engine.verify_audit_chain() else '❌ INVALID'}")
    print()

    # Afficher statistiques
    stats = engine.get_statistics()
    print(f"Total records: {stats['total_records']}")
    print(f"Agents: {list(stats['agents'].keys())}")
    print(f"Action types: {list(stats['action_types'].keys())}")
    print()

    # Générer rapport
    print("Audit Report:")
    print(engine.generate_audit_report('agent-001'))

    print("=" * 80)
    print("✅ LAIRM Audit Engine is ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
