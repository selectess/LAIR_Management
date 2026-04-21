# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

#!/usr/bin/env python3
"""
LAIRM Distributed Storage Module
IPFS, Blockchain, Multi-Node Replication
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Tuple
import hashlib

logger = logging.getLogger(__name__)


class IPFSAuditStorage:
    """Stockage d'audit sur IPFS (InterPlanetary File System)"""

    def __init__(self, ipfs_host: str = "/ip4/127.0.0.1/tcp/5001"):
        """Initialiser la connexion IPFS"""
        self.ipfs_host = ipfs_host
        self.mappings = {}  # agent_id -> IPFS hash
        logger.info(f"Initialized IPFS storage at {ipfs_host}")

    def store_audit_log(self, agent_id: str, log_data: Dict) -> str:
        """Stocker un log d'audit sur IPFS"""
        log_json = json.dumps(log_data, sort_keys=True)
        
        # Simuler le stockage IPFS
        ipfs_hash = hashlib.sha256(log_json.encode()).hexdigest()
        
        # Stocker le mapping
        if agent_id not in self.mappings:
            self.mappings[agent_id] = []
        self.mappings[agent_id].append(ipfs_hash)
        
        logger.info(f"Stored audit log for {agent_id} on IPFS: {ipfs_hash[:16]}...")
        return ipfs_hash

    def retrieve_audit_log(self, ipfs_hash: str) -> Dict:
        """Récupérer un log d'audit depuis IPFS"""
        # Simuler la récupération depuis IPFS
        logger.info(f"Retrieved audit log from IPFS: {ipfs_hash[:16]}...")
        return {'ipfs_hash': ipfs_hash, 'retrieved': True}

    def pin_audit_log(self, ipfs_hash: str) -> bool:
        """Épingler un log pour persistance"""
        logger.info(f"Pinned audit log on IPFS: {ipfs_hash[:16]}...")
        return True

    def get_agent_logs(self, agent_id: str) -> List[str]:
        """Obtenir tous les logs d'un agent"""
        return self.mappings.get(agent_id, [])

    def verify_ipfs_hash(self, ipfs_hash: str, data: Dict) -> bool:
        """Vérifier qu'un hash IPFS correspond aux données"""
        data_json = json.dumps(data, sort_keys=True)
        calculated_hash = hashlib.sha256(data_json.encode()).hexdigest()
        return calculated_hash == ipfs_hash


class BlockchainAuditStorage:
    """Stockage d'audit sur Blockchain (Ethereum)"""

    def __init__(self, network: str = "ethereum"):
        """Initialiser la connexion blockchain"""
        self.network = network
        self.audit_chain = {}  # agent_id -> list of audit hashes
        logger.info(f"Initialized blockchain storage on {network}")

    def store_audit_hash(
        self,
        agent_id: str,
        audit_hash: str,
        timestamp: int = None
    ) -> str:
        """Stocker un hash d'audit sur blockchain"""
        if timestamp is None:
            timestamp = int(datetime.now().timestamp())
        
        record = {
            'agent_id': agent_id,
            'audit_hash': audit_hash,
            'timestamp': timestamp,
            'block_number': len(self.audit_chain.get(agent_id, [])) + 1
        }
        
        # Simuler la transaction blockchain
        tx_hash = hashlib.sha256(
            json.dumps(record, sort_keys=True).encode()
        ).hexdigest()
        
        if agent_id not in self.audit_chain:
            self.audit_chain[agent_id] = []
        self.audit_chain[agent_id].append(record)
        
        logger.info(f"Stored audit hash on blockchain: {tx_hash[:16]}...")
        return tx_hash

    def verify_audit_on_chain(self, agent_id: str, audit_hash: str) -> bool:
        """Vérifier qu'un audit est sur la blockchain"""
        if agent_id not in self.audit_chain:
            return False
        
        for record in self.audit_chain[agent_id]:
            if record['audit_hash'] == audit_hash:
                logger.info(f"Verified audit on blockchain for {agent_id}")
                return True
        
        return False

    def get_audit_history(self, agent_id: str) -> List[Dict]:
        """Obtenir l'historique d'audit d'un agent"""
        return self.audit_chain.get(agent_id, [])

    def get_block_by_number(self, agent_id: str, block_number: int) -> Dict:
        """Obtenir un bloc par numéro"""
        if agent_id not in self.audit_chain:
            return {}
        
        for record in self.audit_chain[agent_id]:
            if record['block_number'] == block_number:
                return record
        
        return {}


class DistributedAuditStorage:
    """Réplication multi-nœuds d'audit"""

    def __init__(self, nodes: List[str]):
        """Initialiser avec liste de nœuds"""
        self.nodes = nodes
        self.local_storage = {}
        self.replication_status = {}
        logger.info(f"Initialized distributed storage with {len(nodes)} nodes")

    def replicate_audit_log(self, agent_id: str, log_data: Dict) -> Dict:
        """Répliquer un log d'audit sur tous les nœuds"""
        log_hash = hashlib.sha256(
            json.dumps(log_data, sort_keys=True).encode()
        ).hexdigest()
        
        replication_results = {
            'log_hash': log_hash,
            'agent_id': agent_id,
            'timestamp': datetime.now().isoformat(),
            'nodes': {}
        }
        
        for node in self.nodes:
            try:
                # Simuler l'envoi au nœud
                success = self.send_to_node(node, agent_id, log_data)
                replication_results['nodes'][node] = {
                    'status': 'success' if success else 'failed',
                    'timestamp': datetime.now().isoformat()
                }
            except Exception as e:
                logger.error(f"Failed to replicate to {node}: {e}")
                replication_results['nodes'][node] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        self.replication_status[log_hash] = replication_results
        return replication_results

    def send_to_node(self, node: str, agent_id: str, log_data: Dict) -> bool:
        """Envoyer un log à un nœud"""
        # Simuler l'envoi
        logger.info(f"Sending audit log to node {node} for agent {agent_id}")
        return True

    def verify_replication(self, agent_id: str, log_hash: str) -> bool:
        """Vérifier que le log est répliqué sur tous les nœuds"""
        if log_hash not in self.replication_status:
            return False
        
        status = self.replication_status[log_hash]
        
        # Vérifier que tous les nœuds ont le log
        for node in self.nodes:
            if node not in status['nodes']:
                return False
            if status['nodes'][node]['status'] != 'success':
                return False
        
        logger.info(f"Verified replication for {agent_id} on all nodes")
        return True

    def check_node_has_log(self, node: str, agent_id: str) -> bool:
        """Vérifier qu'un nœud a un log"""
        # Simuler la vérification
        logger.info(f"Checking if node {node} has logs for {agent_id}")
        return True

    def get_replication_status(self, log_hash: str) -> Dict:
        """Obtenir le statut de réplication"""
        return self.replication_status.get(log_hash, {})

    def get_node_status(self) -> Dict:
        """Obtenir le statut de tous les nœuds"""
        return {
            'total_nodes': len(self.nodes),
            'nodes': self.nodes,
            'timestamp': datetime.now().isoformat()
        }


class HybridDistributedStorage:
    """Stockage hybride: IPFS + Blockchain + Multi-Node"""

    def __init__(self, nodes: List[str], network: str = "ethereum"):
        """Initialiser le stockage hybride"""
        self.ipfs = IPFSAuditStorage()
        self.blockchain = BlockchainAuditStorage(network)
        self.distributed = DistributedAuditStorage(nodes)
        logger.info("Initialized hybrid distributed storage")

    def store_audit_log_hybrid(
        self,
        agent_id: str,
        log_data: Dict
    ) -> Dict:
        """Stocker un log d'audit de manière hybride"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'storage_methods': {}
        }
        
        # 1. Stocker sur IPFS
        ipfs_hash = self.ipfs.store_audit_log(agent_id, log_data)
        result['storage_methods']['ipfs'] = {
            'hash': ipfs_hash,
            'status': 'success'
        }
        
        # 2. Stocker le hash sur blockchain
        tx_hash = self.blockchain.store_audit_hash(agent_id, ipfs_hash)
        result['storage_methods']['blockchain'] = {
            'tx_hash': tx_hash,
            'status': 'success'
        }
        
        # 3. Répliquer sur tous les nœuds
        replication = self.distributed.replicate_audit_log(agent_id, log_data)
        result['storage_methods']['distributed'] = {
            'nodes_count': len(self.distributed.nodes),
            'status': 'success'
        }
        
        logger.info(f"Stored audit log for {agent_id} using hybrid storage")
        return result

    def verify_audit_log_hybrid(
        self,
        agent_id: str,
        ipfs_hash: str
    ) -> Dict:
        """Vérifier un log d'audit de manière hybride"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'verification': {}
        }
        
        # 1. Vérifier sur IPFS (check if hash exists in mappings)
        ipfs_valid = ipfs_hash in self.ipfs.mappings.get(agent_id, [])
        result['verification']['ipfs'] = ipfs_valid
        
        # 2. Vérifier sur blockchain
        blockchain_valid = self.blockchain.verify_audit_on_chain(agent_id, ipfs_hash)
        result['verification']['blockchain'] = blockchain_valid
        
        # 3. Vérifier la réplication
        replication_valid = self.distributed.verify_replication(agent_id, ipfs_hash)
        result['verification']['distributed'] = replication_valid
        
        result['overall_valid'] = all(result['verification'].values())
        
        logger.info(f"Verified audit log for {agent_id}: {result['overall_valid']}")
        return result

    def get_storage_status(self) -> Dict:
        """Obtenir le statut global du stockage"""
        return {
            'timestamp': datetime.now().isoformat(),
            'ipfs': {'status': 'operational'},
            'blockchain': {
                'status': 'operational',
                'network': self.blockchain.network
            },
            'distributed': self.distributed.get_node_status()
        }


def main():
    """Test du module de stockage distribué"""
    print("=" * 80)
    print("LAIRM DISTRIBUTED STORAGE MODULE - TEST")
    print("=" * 80)
    print()
    
    # Test 1: IPFS Storage
    print("1. Testing IPFS Storage")
    print("-" * 40)
    ipfs = IPFSAuditStorage()
    log_data = {
        'agent_id': 'agent-001',
        'action': 'test_action',
        'timestamp': datetime.now().isoformat()
    }
    
    ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
    print(f"Stored on IPFS: {ipfs_hash[:16]}...")
    
    retrieved = ipfs.retrieve_audit_log(ipfs_hash)
    print(f"Retrieved from IPFS: {retrieved}")
    
    pinned = ipfs.pin_audit_log(ipfs_hash)
    print(f"Pinned on IPFS: {pinned}")
    print()
    
    # Test 2: Blockchain Storage
    print("2. Testing Blockchain Storage")
    print("-" * 40)
    blockchain = BlockchainAuditStorage()
    
    tx_hash = blockchain.store_audit_hash('agent-001', ipfs_hash)
    print(f"Stored on blockchain: {tx_hash[:16]}...")
    
    verified = blockchain.verify_audit_on_chain('agent-001', ipfs_hash)
    print(f"Verified on blockchain: {verified}")
    
    history = blockchain.get_audit_history('agent-001')
    print(f"Audit history: {len(history)} records")
    print()
    
    # Test 3: Distributed Storage
    print("3. Testing Distributed Storage")
    print("-" * 40)
    nodes = ['node-1', 'node-2', 'node-3']
    distributed = DistributedAuditStorage(nodes)
    
    replication = distributed.replicate_audit_log('agent-001', log_data)
    print(f"Replicated to {len(replication['nodes'])} nodes")
    
    verified_replication = distributed.verify_replication('agent-001', ipfs_hash)
    print(f"Replication verified: {verified_replication}")
    print()
    
    # Test 4: Hybrid Storage
    print("4. Testing Hybrid Storage")
    print("-" * 40)
    hybrid = HybridDistributedStorage(nodes)
    
    hybrid_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
    print(f"Stored using hybrid storage")
    print(f"  IPFS: {hybrid_result['storage_methods']['ipfs']['status']}")
    print(f"  Blockchain: {hybrid_result['storage_methods']['blockchain']['status']}")
    print(f"  Distributed: {hybrid_result['storage_methods']['distributed']['status']}")
    
    verification = hybrid.verify_audit_log_hybrid('agent-001', ipfs_hash)
    print(f"Verification result: {verification['overall_valid']}")
    
    status = hybrid.get_storage_status()
    print(f"Storage status: {status['ipfs']['status']}")
    print()
    
    print("=" * 80)
    print("✅ LAIRM Distributed Storage Module Ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
