# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Unit Tests for LAIRM Distributed Storage Module
Comprehensive coverage for IPFS, Blockchain, and Multi-Node Replication
"""

import pytest
import json
import hashlib
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock

# Import the modules to test
import sys
sys.path.insert(0, '/Users/mehdiwhb/Desktop/ARAM/LAIRM/05-TOOLS')

from audit_engine.distributed_storage import (
    IPFSAuditStorage,
    BlockchainAuditStorage,
    DistributedAuditStorage,
    HybridDistributedStorage
)


class TestIPFSAuditStorage:
    """Test suite for IPFS Audit Storage"""
    
    @pytest.fixture
    def ipfs_storage(self):
        """Create IPFS storage instance"""
        return IPFSAuditStorage()
    
    @pytest.fixture
    def sample_log_data(self):
        """Sample audit log data"""
        return {
            'agent_id': 'agent-001',
            'action': 'deploy',
            'timestamp': datetime.now().isoformat(),
            'details': {'version': '1.0', 'status': 'success'}
        }
    
    def test_initialization(self, ipfs_storage):
        """Test IPFS storage initialization"""
        assert ipfs_storage.ipfs_host == "/ip4/127.0.0.1/tcp/5001"
        assert ipfs_storage.mappings == {}
    
    def test_store_audit_log(self, ipfs_storage, sample_log_data):
        """Test storing audit log on IPFS"""
        ipfs_hash = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        
        assert ipfs_hash is not None
        assert len(ipfs_hash) == 64  # SHA-256 hex length
        assert 'agent-001' in ipfs_storage.mappings
        assert ipfs_hash in ipfs_storage.mappings['agent-001']
    
    def test_store_multiple_logs_same_agent(self, ipfs_storage, sample_log_data):
        """Test storing multiple logs for same agent"""
        data1 = sample_log_data.copy()
        data1['action'] = 'action1'
        data2 = sample_log_data.copy()
        data2['action'] = 'action2'
        
        hash1 = ipfs_storage.store_audit_log('agent-001', data1)
        hash2 = ipfs_storage.store_audit_log('agent-001', data2)
        
        assert hash1 != hash2  # Different data
        assert len(ipfs_storage.mappings['agent-001']) == 2
    
    def test_retrieve_audit_log(self, ipfs_storage, sample_log_data):
        """Test retrieving audit log from IPFS"""
        ipfs_hash = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        retrieved = ipfs_storage.retrieve_audit_log(ipfs_hash)
        
        assert retrieved is not None
        assert retrieved['ipfs_hash'] == ipfs_hash
        assert retrieved['retrieved'] is True
    
    def test_pin_audit_log(self, ipfs_storage, sample_log_data):
        """Test pinning audit log for persistence"""
        ipfs_hash = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        pinned = ipfs_storage.pin_audit_log(ipfs_hash)
        
        assert pinned is True
    
    def test_get_agent_logs(self, ipfs_storage, sample_log_data):
        """Test retrieving all logs for an agent"""
        hash1 = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        hash2 = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        
        logs = ipfs_storage.get_agent_logs('agent-001')
        assert len(logs) == 2
        assert hash1 in logs
        assert hash2 in logs
    
    def test_get_agent_logs_nonexistent(self, ipfs_storage):
        """Test retrieving logs for nonexistent agent"""
        logs = ipfs_storage.get_agent_logs('nonexistent-agent')
        assert logs == []
    
    def test_verify_ipfs_hash_valid(self, ipfs_storage, sample_log_data):
        """Test verifying valid IPFS hash"""
        ipfs_hash = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        is_valid = ipfs_storage.verify_ipfs_hash(ipfs_hash, sample_log_data)
        
        assert is_valid is True
    
    def test_verify_ipfs_hash_invalid(self, ipfs_storage, sample_log_data):
        """Test verifying invalid IPFS hash"""
        ipfs_hash = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        
        modified_data = sample_log_data.copy()
        modified_data['action'] = 'modified'
        
        is_valid = ipfs_storage.verify_ipfs_hash(ipfs_hash, modified_data)
        assert is_valid is False
    
    def test_hash_consistency(self, ipfs_storage, sample_log_data):
        """Test that same data produces same hash"""
        hash1 = ipfs_storage.store_audit_log('agent-001', sample_log_data)
        
        # Create new storage instance
        ipfs_storage2 = IPFSAuditStorage()
        hash2 = ipfs_storage2.store_audit_log('agent-001', sample_log_data)
        
        assert hash1 == hash2


class TestBlockchainAuditStorage:
    """Test suite for Blockchain Audit Storage"""
    
    @pytest.fixture
    def blockchain_storage(self):
        """Create blockchain storage instance"""
        return BlockchainAuditStorage()
    
    @pytest.fixture
    def sample_audit_hash(self):
        """Sample audit hash"""
        return hashlib.sha256(b"test_audit_data").hexdigest()
    
    def test_initialization(self, blockchain_storage):
        """Test blockchain storage initialization"""
        assert blockchain_storage.network == "ethereum"
        assert blockchain_storage.audit_chain == {}
    
    def test_initialization_custom_network(self):
        """Test blockchain storage with custom network"""
        storage = BlockchainAuditStorage(network="polygon")
        assert storage.network == "polygon"
    
    def test_store_audit_hash(self, blockchain_storage, sample_audit_hash):
        """Test storing audit hash on blockchain"""
        tx_hash = blockchain_storage.store_audit_hash('agent-001', sample_audit_hash)
        
        assert tx_hash is not None
        assert len(tx_hash) == 64  # SHA-256 hex length
        assert 'agent-001' in blockchain_storage.audit_chain
        assert len(blockchain_storage.audit_chain['agent-001']) == 1
    
    def test_store_multiple_hashes(self, blockchain_storage, sample_audit_hash):
        """Test storing multiple hashes for same agent"""
        hash1 = hashlib.sha256(b"data1").hexdigest()
        hash2 = hashlib.sha256(b"data2").hexdigest()
        
        tx1 = blockchain_storage.store_audit_hash('agent-001', hash1)
        tx2 = blockchain_storage.store_audit_hash('agent-001', hash2)
        
        assert tx1 != tx2
        assert len(blockchain_storage.audit_chain['agent-001']) == 2
    
    def test_verify_audit_on_chain_valid(self, blockchain_storage, sample_audit_hash):
        """Test verifying valid audit on blockchain"""
        blockchain_storage.store_audit_hash('agent-001', sample_audit_hash)
        is_valid = blockchain_storage.verify_audit_on_chain('agent-001', sample_audit_hash)
        
        assert is_valid is True
    
    def test_verify_audit_on_chain_invalid(self, blockchain_storage, sample_audit_hash):
        """Test verifying invalid audit on blockchain"""
        blockchain_storage.store_audit_hash('agent-001', sample_audit_hash)
        
        invalid_hash = hashlib.sha256(b"invalid").hexdigest()
        is_valid = blockchain_storage.verify_audit_on_chain('agent-001', invalid_hash)
        
        assert is_valid is False
    
    def test_verify_audit_nonexistent_agent(self, blockchain_storage, sample_audit_hash):
        """Test verifying audit for nonexistent agent"""
        is_valid = blockchain_storage.verify_audit_on_chain('nonexistent', sample_audit_hash)
        assert is_valid is False
    
    def test_get_audit_history(self, blockchain_storage):
        """Test retrieving audit history"""
        hash1 = hashlib.sha256(b"data1").hexdigest()
        hash2 = hashlib.sha256(b"data2").hexdigest()
        
        blockchain_storage.store_audit_hash('agent-001', hash1)
        blockchain_storage.store_audit_hash('agent-001', hash2)
        
        history = blockchain_storage.get_audit_history('agent-001')
        assert len(history) == 2
        assert history[0]['audit_hash'] == hash1
        assert history[1]['audit_hash'] == hash2
    
    def test_get_audit_history_nonexistent(self, blockchain_storage):
        """Test retrieving history for nonexistent agent"""
        history = blockchain_storage.get_audit_history('nonexistent')
        assert history == []
    
    def test_get_block_by_number(self, blockchain_storage):
        """Test retrieving block by number"""
        hash1 = hashlib.sha256(b"data1").hexdigest()
        blockchain_storage.store_audit_hash('agent-001', hash1)
        
        block = blockchain_storage.get_block_by_number('agent-001', 1)
        assert block['block_number'] == 1
        assert block['audit_hash'] == hash1
    
    def test_get_block_by_number_invalid(self, blockchain_storage):
        """Test retrieving invalid block number"""
        block = blockchain_storage.get_block_by_number('agent-001', 999)
        assert block == {}
    
    def test_block_numbering_sequence(self, blockchain_storage):
        """Test that block numbers are sequential"""
        for i in range(5):
            hash_val = hashlib.sha256(f"data{i}".encode()).hexdigest()
            blockchain_storage.store_audit_hash('agent-001', hash_val)
        
        history = blockchain_storage.get_audit_history('agent-001')
        for i, record in enumerate(history, 1):
            assert record['block_number'] == i


class TestDistributedAuditStorage:
    """Test suite for Distributed Audit Storage"""
    
    @pytest.fixture
    def distributed_storage(self):
        """Create distributed storage instance"""
        nodes = ['node-1', 'node-2', 'node-3']
        return DistributedAuditStorage(nodes)
    
    @pytest.fixture
    def sample_log_data(self):
        """Sample audit log data"""
        return {
            'agent_id': 'agent-001',
            'action': 'deploy',
            'timestamp': datetime.now().isoformat()
        }
    
    def test_initialization(self, distributed_storage):
        """Test distributed storage initialization"""
        assert len(distributed_storage.nodes) == 3
        assert 'node-1' in distributed_storage.nodes
        assert distributed_storage.local_storage == {}
        assert distributed_storage.replication_status == {}
    
    def test_replicate_audit_log(self, distributed_storage, sample_log_data):
        """Test replicating audit log to all nodes"""
        result = distributed_storage.replicate_audit_log('agent-001', sample_log_data)
        
        assert result['agent_id'] == 'agent-001'
        assert 'log_hash' in result
        assert len(result['nodes']) == 3
        assert all(node in result['nodes'] for node in distributed_storage.nodes)
    
    def test_replication_status_tracking(self, distributed_storage, sample_log_data):
        """Test that replication status is tracked"""
        result = distributed_storage.replicate_audit_log('agent-001', sample_log_data)
        log_hash = result['log_hash']
        
        status = distributed_storage.get_replication_status(log_hash)
        assert status == result
    
    def test_verify_replication_success(self, distributed_storage, sample_log_data):
        """Test verifying successful replication"""
        result = distributed_storage.replicate_audit_log('agent-001', sample_log_data)
        log_hash = result['log_hash']
        
        is_verified = distributed_storage.verify_replication('agent-001', log_hash)
        assert is_verified is True
    
    def test_verify_replication_nonexistent(self, distributed_storage):
        """Test verifying nonexistent replication"""
        is_verified = distributed_storage.verify_replication('agent-001', 'nonexistent_hash')
        assert is_verified is False
    
    def test_check_node_has_log(self, distributed_storage, sample_log_data):
        """Test checking if node has log"""
        has_log = distributed_storage.check_node_has_log('node-1', 'agent-001')
        assert has_log is True
    
    def test_get_node_status(self, distributed_storage):
        """Test getting node status"""
        status = distributed_storage.get_node_status()
        
        assert status['total_nodes'] == 3
        assert len(status['nodes']) == 3
        assert 'timestamp' in status
    
    def test_multiple_replications(self, distributed_storage, sample_log_data):
        """Test multiple replications"""
        data1 = sample_log_data.copy()
        data1['action'] = 'action1'
        data2 = sample_log_data.copy()
        data2['action'] = 'action2'
        
        result1 = distributed_storage.replicate_audit_log('agent-001', data1)
        result2 = distributed_storage.replicate_audit_log('agent-002', data2)
        
        assert result1['log_hash'] != result2['log_hash']
        assert len(distributed_storage.replication_status) == 2


class TestHybridDistributedStorage:
    """Test suite for Hybrid Distributed Storage"""
    
    @pytest.fixture
    def hybrid_storage(self):
        """Create hybrid storage instance"""
        nodes = ['node-1', 'node-2', 'node-3']
        return HybridDistributedStorage(nodes)
    
    @pytest.fixture
    def sample_log_data(self):
        """Sample audit log data"""
        return {
            'agent_id': 'agent-001',
            'action': 'deploy',
            'timestamp': datetime.now().isoformat(),
            'details': {'version': '1.0'}
        }
    
    def test_initialization(self, hybrid_storage):
        """Test hybrid storage initialization"""
        assert hybrid_storage.ipfs is not None
        assert hybrid_storage.blockchain is not None
        assert hybrid_storage.distributed is not None
    
    def test_store_audit_log_hybrid(self, hybrid_storage, sample_log_data):
        """Test storing audit log using hybrid storage"""
        result = hybrid_storage.store_audit_log_hybrid('agent-001', sample_log_data)
        
        assert result['agent_id'] == 'agent-001'
        assert 'storage_methods' in result
        assert 'ipfs' in result['storage_methods']
        assert 'blockchain' in result['storage_methods']
        assert 'distributed' in result['storage_methods']
    
    def test_hybrid_storage_all_methods_succeed(self, hybrid_storage, sample_log_data):
        """Test that all storage methods succeed"""
        result = hybrid_storage.store_audit_log_hybrid('agent-001', sample_log_data)
        
        assert result['storage_methods']['ipfs']['status'] == 'success'
        assert result['storage_methods']['blockchain']['status'] == 'success'
        assert result['storage_methods']['distributed']['status'] == 'success'
    
    def test_verify_audit_log_hybrid(self, hybrid_storage, sample_log_data):
        """Test verifying audit log using hybrid storage"""
        store_result = hybrid_storage.store_audit_log_hybrid('agent-001', sample_log_data)
        ipfs_hash = store_result['storage_methods']['ipfs']['hash']
        
        verify_result = hybrid_storage.verify_audit_log_hybrid('agent-001', ipfs_hash)
        
        assert 'verification' in verify_result
        assert 'overall_valid' in verify_result
    
    def test_get_storage_status(self, hybrid_storage):
        """Test getting overall storage status"""
        status = hybrid_storage.get_storage_status()
        
        assert 'ipfs' in status
        assert 'blockchain' in status
        assert 'distributed' in status
        assert status['ipfs']['status'] == 'operational'
        assert status['blockchain']['status'] == 'operational'
    
    def test_hybrid_storage_redundancy(self, hybrid_storage, sample_log_data):
        """Test that hybrid storage provides redundancy"""
        result = hybrid_storage.store_audit_log_hybrid('agent-001', sample_log_data)
        
        # Data is stored in 3 different ways
        assert 'ipfs' in result['storage_methods']
        assert 'blockchain' in result['storage_methods']
        assert 'distributed' in result['storage_methods']
        
        # Each method has its own hash/identifier
        assert result['storage_methods']['ipfs']['hash'] is not None
        assert result['storage_methods']['blockchain']['tx_hash'] is not None
        assert result['storage_methods']['distributed']['nodes_count'] == 3


class TestDistributedStorageIntegration:
    """Integration tests for distributed storage"""
    
    def test_ipfs_to_blockchain_workflow(self):
        """Test workflow: Store on IPFS, then on blockchain"""
        ipfs = IPFSAuditStorage()
        blockchain = BlockchainAuditStorage()
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        # Store on IPFS
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        # Store IPFS hash on blockchain
        tx_hash = blockchain.store_audit_hash('agent-001', ipfs_hash)
        
        # Verify on blockchain
        is_valid = blockchain.verify_audit_on_chain('agent-001', ipfs_hash)
        assert is_valid is True
    
    def test_full_hybrid_workflow(self):
        """Test complete hybrid storage workflow"""
        nodes = ['node-1', 'node-2', 'node-3']
        hybrid = HybridDistributedStorage(nodes)
        
        log_data = {
            'agent_id': 'agent-001',
            'action': 'deploy',
            'timestamp': datetime.now().isoformat()
        }
        
        # Store
        store_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        # Verify that all storage methods were called
        assert store_result['storage_methods']['ipfs']['status'] == 'success'
        assert store_result['storage_methods']['blockchain']['status'] == 'success'
        assert store_result['storage_methods']['distributed']['status'] == 'success'
        
        # Verify that we got hashes/identifiers
        assert 'hash' in store_result['storage_methods']['ipfs']
        assert 'tx_hash' in store_result['storage_methods']['blockchain']
        assert store_result['storage_methods']['distributed']['nodes_count'] == 3
    
    def test_multiple_agents_distributed_storage(self):
        """Test distributed storage with multiple agents"""
        nodes = ['node-1', 'node-2', 'node-3']
        distributed = DistributedAuditStorage(nodes)
        
        agents = ['agent-001', 'agent-002', 'agent-003']
        
        for agent in agents:
            log_data = {'agent_id': agent, 'action': 'test'}
            distributed.replicate_audit_log(agent, log_data)
        
        assert len(distributed.replication_status) == 3


class TestDistributedStorageEdgeCases:
    """Edge case tests for distributed storage"""
    
    def test_empty_log_data(self):
        """Test storing empty log data"""
        ipfs = IPFSAuditStorage()
        empty_data = {}
        
        ipfs_hash = ipfs.store_audit_log('agent-001', empty_data)
        assert ipfs_hash is not None
    
    def test_large_log_data(self):
        """Test storing large log data"""
        ipfs = IPFSAuditStorage()
        large_data = {
            'agent_id': 'agent-001',
            'data': 'x' * 10000  # 10KB of data
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', large_data)
        assert ipfs_hash is not None
    
    def test_special_characters_in_agent_id(self):
        """Test with special characters in agent ID"""
        ipfs = IPFSAuditStorage()
        log_data = {'action': 'test'}
        
        special_agent_id = 'agent-001@#$%'
        ipfs_hash = ipfs.store_audit_log(special_agent_id, log_data)
        
        logs = ipfs.get_agent_logs(special_agent_id)
        assert ipfs_hash in logs
    
    def test_unicode_in_log_data(self):
        """Test with unicode characters in log data"""
        ipfs = IPFSAuditStorage()
        log_data = {
            'agent_id': 'agent-001',
            'message': '你好世界 🌍 مرحبا'
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        assert ipfs_hash is not None
    
    def test_concurrent_replication(self):
        """Test concurrent replication to multiple nodes"""
        nodes = ['node-1', 'node-2', 'node-3', 'node-4', 'node-5']
        distributed = DistributedAuditStorage(nodes)
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        result = distributed.replicate_audit_log('agent-001', log_data)
        
        # All nodes should have the log
        assert len(result['nodes']) == 5
        assert all(node in result['nodes'] for node in nodes)


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
