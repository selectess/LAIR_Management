# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Complete Test Suite for LAIRM Distributed Storage
Tests IPFS, Blockchain, Multi-Node Replication, and Hybrid Storage
"""

import pytest
import json
import hashlib
from datetime import datetime
from audit_engine.distributed_storage import (
    IPFSAuditStorage,
    BlockchainAuditStorage,
    DistributedAuditStorage,
    HybridDistributedStorage
)


class TestIPFSAuditStorage:
    """Test suite for IPFS Audit Storage"""
    
    @pytest.fixture
    def ipfs(self):
        """Initialize IPFS storage"""
        return IPFSAuditStorage()
    
    def test_ipfs_initialization(self, ipfs):
        """Test IPFS storage initialization"""
        assert ipfs is not None
        assert ipfs.ipfs_host == "/ip4/127.0.0.1/tcp/5001"
        assert isinstance(ipfs.mappings, dict)
    
    def test_ipfs_custom_host(self):
        """Test IPFS with custom host"""
        custom_host = "/ip4/192.168.1.1/tcp/5001"
        ipfs = IPFSAuditStorage(ipfs_host=custom_host)
        assert ipfs.ipfs_host == custom_host
    
    def test_store_audit_log(self, ipfs):
        """Test storing audit log on IPFS"""
        log_data = {
            'agent_id': 'agent-001',
            'action': 'test_action',
            'timestamp': datetime.now().isoformat()
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        assert ipfs_hash is not None
        assert isinstance(ipfs_hash, str)
        assert len(ipfs_hash) == 64  # SHA256 hex digest
    
    def test_store_multiple_logs(self, ipfs):
        """Test storing multiple logs for same agent"""
        log_data_1 = {'agent_id': 'agent-001', 'action': 'action1'}
        log_data_2 = {'agent_id': 'agent-001', 'action': 'action2'}
        
        hash1 = ipfs.store_audit_log('agent-001', log_data_1)
        hash2 = ipfs.store_audit_log('agent-001', log_data_2)
        
        assert hash1 != hash2
        assert len(ipfs.mappings['agent-001']) == 2
    
    def test_retrieve_audit_log(self, ipfs):
        """Test retrieving audit log from IPFS"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        retrieved = ipfs.retrieve_audit_log(ipfs_hash)
        
        assert retrieved is not None
        assert isinstance(retrieved, dict)
        assert 'ipfs_hash' in retrieved
        assert retrieved['retrieved'] == True
    
    def test_pin_audit_log(self, ipfs):
        """Test pinning audit log"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        pinned = ipfs.pin_audit_log(ipfs_hash)
        
        assert pinned == True
    
    def test_get_agent_logs(self, ipfs):
        """Test getting all logs for an agent"""
        log_data_1 = {'agent_id': 'agent-001', 'action': 'action1'}
        log_data_2 = {'agent_id': 'agent-001', 'action': 'action2'}
        log_data_3 = {'agent_id': 'agent-002', 'action': 'action3'}
        
        hash1 = ipfs.store_audit_log('agent-001', log_data_1)
        hash2 = ipfs.store_audit_log('agent-001', log_data_2)
        hash3 = ipfs.store_audit_log('agent-002', log_data_3)
        
        agent_001_logs = ipfs.get_agent_logs('agent-001')
        agent_002_logs = ipfs.get_agent_logs('agent-002')
        
        assert len(agent_001_logs) == 2
        assert len(agent_002_logs) == 1
        assert hash1 in agent_001_logs
        assert hash2 in agent_001_logs
        assert hash3 in agent_002_logs
    
    def test_get_agent_logs_nonexistent(self, ipfs):
        """Test getting logs for nonexistent agent"""
        logs = ipfs.get_agent_logs('nonexistent-agent')
        
        assert logs == []
    
    def test_verify_ipfs_hash_valid(self, ipfs):
        """Test verifying valid IPFS hash"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        is_valid = ipfs.verify_ipfs_hash(ipfs_hash, log_data)
        
        assert is_valid == True
    
    def test_verify_ipfs_hash_invalid(self, ipfs):
        """Test verifying invalid IPFS hash"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        # Modify data
        modified_data = {'agent_id': 'agent-001', 'action': 'modified'}
        
        is_valid = ipfs.verify_ipfs_hash(ipfs_hash, modified_data)
        
        assert is_valid == False
    
    def test_verify_ipfs_hash_wrong_hash(self, ipfs):
        """Test verifying with wrong hash"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        wrong_hash = 'a' * 64
        
        is_valid = ipfs.verify_ipfs_hash(wrong_hash, log_data)
        
        assert is_valid == False
    
    def test_ipfs_hash_consistency(self, ipfs):
        """Test that same data produces same hash"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        hash1 = ipfs.store_audit_log('agent-001', log_data)
        hash2 = ipfs.store_audit_log('agent-002', log_data)
        
        assert hash1 == hash2
    
    def test_ipfs_with_empty_data(self, ipfs):
        """Test IPFS with empty data"""
        log_data = {}
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        assert ipfs_hash is not None
        assert len(ipfs_hash) == 64
    
    def test_ipfs_with_large_data(self, ipfs):
        """Test IPFS with large data"""
        log_data = {
            'agent_id': 'agent-001',
            'action': 'test',
            'data': 'x' * 100000  # 100KB
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        assert ipfs_hash is not None
        assert len(ipfs_hash) == 64


class TestBlockchainAuditStorage:
    """Test suite for Blockchain Audit Storage"""
    
    @pytest.fixture
    def blockchain(self):
        """Initialize blockchain storage"""
        return BlockchainAuditStorage()
    
    def test_blockchain_initialization(self, blockchain):
        """Test blockchain storage initialization"""
        assert blockchain is not None
        assert blockchain.network == "ethereum"
        assert isinstance(blockchain.audit_chain, dict)
    
    def test_blockchain_custom_network(self):
        """Test blockchain with custom network"""
        blockchain = BlockchainAuditStorage(network="polygon")
        assert blockchain.network == "polygon"
    
    def test_store_audit_hash(self, blockchain):
        """Test storing audit hash on blockchain"""
        audit_hash = 'a' * 64
        
        tx_hash = blockchain.store_audit_hash('agent-001', audit_hash)
        
        assert tx_hash is not None
        assert isinstance(tx_hash, str)
        assert len(tx_hash) == 64
    
    def test_store_audit_hash_with_timestamp(self, blockchain):
        """Test storing audit hash with custom timestamp"""
        audit_hash = 'a' * 64
        timestamp = 1234567890
        
        tx_hash = blockchain.store_audit_hash('agent-001', audit_hash, timestamp)
        
        assert tx_hash is not None
        records = blockchain.get_audit_history('agent-001')
        assert len(records) == 1
        assert records[0]['timestamp'] == timestamp
    
    def test_store_multiple_hashes(self, blockchain):
        """Test storing multiple hashes for same agent"""
        hash1 = 'a' * 64
        hash2 = 'b' * 64
        
        tx_hash1 = blockchain.store_audit_hash('agent-001', hash1)
        tx_hash2 = blockchain.store_audit_hash('agent-001', hash2)
        
        assert tx_hash1 != tx_hash2
        records = blockchain.get_audit_history('agent-001')
        assert len(records) == 2
    
    def test_verify_audit_on_chain_valid(self, blockchain):
        """Test verifying valid audit on chain"""
        audit_hash = 'a' * 64
        
        blockchain.store_audit_hash('agent-001', audit_hash)
        is_valid = blockchain.verify_audit_on_chain('agent-001', audit_hash)
        
        assert is_valid == True
    
    def test_verify_audit_on_chain_invalid(self, blockchain):
        """Test verifying invalid audit on chain"""
        audit_hash = 'a' * 64
        wrong_hash = 'b' * 64
        
        blockchain.store_audit_hash('agent-001', audit_hash)
        is_valid = blockchain.verify_audit_on_chain('agent-001', wrong_hash)
        
        assert is_valid == False
    
    def test_verify_audit_nonexistent_agent(self, blockchain):
        """Test verifying audit for nonexistent agent"""
        audit_hash = 'a' * 64
        
        is_valid = blockchain.verify_audit_on_chain('nonexistent', audit_hash)
        
        assert is_valid == False
    
    def test_get_audit_history(self, blockchain):
        """Test getting audit history"""
        hash1 = 'a' * 64
        hash2 = 'b' * 64
        
        blockchain.store_audit_hash('agent-001', hash1)
        blockchain.store_audit_hash('agent-001', hash2)
        
        history = blockchain.get_audit_history('agent-001')
        
        assert len(history) == 2
        assert history[0]['audit_hash'] == hash1
        assert history[1]['audit_hash'] == hash2
    
    def test_get_audit_history_nonexistent(self, blockchain):
        """Test getting history for nonexistent agent"""
        history = blockchain.get_audit_history('nonexistent')
        
        assert history == []
    
    def test_get_block_by_number(self, blockchain):
        """Test getting block by number"""
        hash1 = 'a' * 64
        hash2 = 'b' * 64
        
        blockchain.store_audit_hash('agent-001', hash1)
        blockchain.store_audit_hash('agent-001', hash2)
        
        block1 = blockchain.get_block_by_number('agent-001', 1)
        block2 = blockchain.get_block_by_number('agent-001', 2)
        
        assert block1['audit_hash'] == hash1
        assert block2['audit_hash'] == hash2
    
    def test_get_block_by_number_invalid(self, blockchain):
        """Test getting block with invalid number"""
        hash1 = 'a' * 64
        blockchain.store_audit_hash('agent-001', hash1)
        
        block = blockchain.get_block_by_number('agent-001', 999)
        
        assert block == {}
    
    def test_block_number_sequence(self, blockchain):
        """Test that block numbers are sequential"""
        for i in range(5):
            blockchain.store_audit_hash('agent-001', f'{i}' * 64)
        
        history = blockchain.get_audit_history('agent-001')
        
        for i, record in enumerate(history, 1):
            assert record['block_number'] == i


class TestDistributedAuditStorage:
    """Test suite for Distributed Audit Storage"""
    
    @pytest.fixture
    def distributed(self):
        """Initialize distributed storage"""
        nodes = ['node-1', 'node-2', 'node-3']
        return DistributedAuditStorage(nodes)
    
    def test_distributed_initialization(self, distributed):
        """Test distributed storage initialization"""
        assert distributed is not None
        assert len(distributed.nodes) == 3
        assert 'node-1' in distributed.nodes
    
    def test_distributed_single_node(self):
        """Test distributed storage with single node"""
        distributed = DistributedAuditStorage(['node-1'])
        assert len(distributed.nodes) == 1
    
    def test_replicate_audit_log(self, distributed):
        """Test replicating audit log"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = distributed.replicate_audit_log('agent-001', log_data)
        
        assert result is not None
        assert 'log_hash' in result
        assert 'nodes' in result
        assert len(result['nodes']) == 3
    
    def test_replicate_audit_log_all_nodes_success(self, distributed):
        """Test that all nodes receive replication"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = distributed.replicate_audit_log('agent-001', log_data)
        
        for node in distributed.nodes:
            assert node in result['nodes']
            assert result['nodes'][node]['status'] == 'success'
    
    def test_send_to_node(self, distributed):
        """Test sending to node"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        success = distributed.send_to_node('node-1', 'agent-001', log_data)
        
        assert success == True
    
    def test_verify_replication_valid(self, distributed):
        """Test verifying valid replication"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = distributed.replicate_audit_log('agent-001', log_data)
        log_hash = result['log_hash']
        
        is_valid = distributed.verify_replication('agent-001', log_hash)
        
        assert is_valid == True
    
    def test_verify_replication_nonexistent(self, distributed):
        """Test verifying nonexistent replication"""
        is_valid = distributed.verify_replication('agent-001', 'nonexistent_hash')
        
        assert is_valid == False
    
    def test_check_node_has_log(self, distributed):
        """Test checking if node has log"""
        has_log = distributed.check_node_has_log('node-1', 'agent-001')
        
        assert has_log == True
    
    def test_get_replication_status(self, distributed):
        """Test getting replication status"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = distributed.replicate_audit_log('agent-001', log_data)
        log_hash = result['log_hash']
        
        status = distributed.get_replication_status(log_hash)
        
        assert status is not None
        assert 'nodes' in status
    
    def test_get_replication_status_nonexistent(self, distributed):
        """Test getting status for nonexistent replication"""
        status = distributed.get_replication_status('nonexistent_hash')
        
        assert status == {}
    
    def test_get_node_status(self, distributed):
        """Test getting node status"""
        status = distributed.get_node_status()
        
        assert status is not None
        assert 'total_nodes' in status
        assert status['total_nodes'] == 3
        assert 'nodes' in status
        assert len(status['nodes']) == 3
    
    def test_multiple_replications(self, distributed):
        """Test multiple replications"""
        log_data_1 = {'agent_id': 'agent-001', 'action': 'action1'}
        log_data_2 = {'agent_id': 'agent-002', 'action': 'action2'}
        
        result1 = distributed.replicate_audit_log('agent-001', log_data_1)
        result2 = distributed.replicate_audit_log('agent-002', log_data_2)
        
        assert result1['log_hash'] != result2['log_hash']
        assert len(distributed.replication_status) == 2


class TestHybridDistributedStorage:
    """Test suite for Hybrid Distributed Storage"""
    
    @pytest.fixture
    def hybrid(self):
        """Initialize hybrid storage"""
        nodes = ['node-1', 'node-2', 'node-3']
        return HybridDistributedStorage(nodes)
    
    def test_hybrid_initialization(self, hybrid):
        """Test hybrid storage initialization"""
        assert hybrid is not None
        assert hybrid.ipfs is not None
        assert hybrid.blockchain is not None
        assert hybrid.distributed is not None
    
    def test_hybrid_custom_network(self):
        """Test hybrid storage with custom network"""
        nodes = ['node-1', 'node-2']
        hybrid = HybridDistributedStorage(nodes, network="polygon")
        
        assert hybrid.blockchain.network == "polygon"
    
    def test_store_audit_log_hybrid(self, hybrid):
        """Test storing audit log using hybrid storage"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert result is not None
        assert 'storage_methods' in result
        assert 'ipfs' in result['storage_methods']
        assert 'blockchain' in result['storage_methods']
        assert 'distributed' in result['storage_methods']
    
    def test_store_audit_log_hybrid_all_methods_success(self, hybrid):
        """Test that all storage methods succeed"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert result['storage_methods']['ipfs']['status'] == 'success'
        assert result['storage_methods']['blockchain']['status'] == 'success'
        assert result['storage_methods']['distributed']['status'] == 'success'
    
    def test_store_audit_log_hybrid_ipfs_hash(self, hybrid):
        """Test that IPFS hash is stored"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert 'hash' in result['storage_methods']['ipfs']
        assert len(result['storage_methods']['ipfs']['hash']) == 64
    
    def test_store_audit_log_hybrid_blockchain_tx(self, hybrid):
        """Test that blockchain transaction hash is stored"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert 'tx_hash' in result['storage_methods']['blockchain']
        assert len(result['storage_methods']['blockchain']['tx_hash']) == 64
    
    def test_store_audit_log_hybrid_distributed_nodes(self, hybrid):
        """Test that distributed storage has correct node count"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert result['storage_methods']['distributed']['nodes_count'] == 3
    
    def test_verify_audit_log_hybrid(self, hybrid):
        """Test verifying audit log using hybrid storage"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        store_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        ipfs_hash = store_result['storage_methods']['ipfs']['hash']
        
        verify_result = hybrid.verify_audit_log_hybrid('agent-001', ipfs_hash)
        
        assert verify_result is not None
        assert 'verification' in verify_result
    
    def test_verify_audit_log_hybrid_all_methods(self, hybrid):
        """Test that all verification methods are checked"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        store_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        ipfs_hash = store_result['storage_methods']['ipfs']['hash']
        
        verify_result = hybrid.verify_audit_log_hybrid('agent-001', ipfs_hash)
        
        assert 'ipfs' in verify_result['verification']
        assert 'blockchain' in verify_result['verification']
        assert 'distributed' in verify_result['verification']
    
    def test_verify_audit_log_hybrid_overall_valid(self, hybrid):
        """Test overall verification result"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        store_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        ipfs_hash = store_result['storage_methods']['ipfs']['hash']
        
        verify_result = hybrid.verify_audit_log_hybrid('agent-001', ipfs_hash)
        
        assert 'overall_valid' in verify_result
        assert verify_result['overall_valid'] == True
    
    def test_get_storage_status(self, hybrid):
        """Test getting storage status"""
        status = hybrid.get_storage_status()
        
        assert status is not None
        assert 'ipfs' in status
        assert 'blockchain' in status
        assert 'distributed' in status
    
    def test_get_storage_status_ipfs_operational(self, hybrid):
        """Test IPFS status is operational"""
        status = hybrid.get_storage_status()
        
        assert status['ipfs']['status'] == 'operational'
    
    def test_get_storage_status_blockchain_operational(self, hybrid):
        """Test blockchain status is operational"""
        status = hybrid.get_storage_status()
        
        assert status['blockchain']['status'] == 'operational'
        assert status['blockchain']['network'] == 'ethereum'
    
    def test_get_storage_status_distributed_nodes(self, hybrid):
        """Test distributed status has node information"""
        status = hybrid.get_storage_status()
        
        assert 'distributed' in status
        assert 'total_nodes' in status['distributed']
        assert status['distributed']['total_nodes'] == 3
    
    def test_multiple_hybrid_stores(self, hybrid):
        """Test multiple hybrid storage operations"""
        log_data_1 = {'agent_id': 'agent-001', 'action': 'action1'}
        log_data_2 = {'agent_id': 'agent-002', 'action': 'action2'}
        
        result1 = hybrid.store_audit_log_hybrid('agent-001', log_data_1)
        result2 = hybrid.store_audit_log_hybrid('agent-002', log_data_2)
        
        assert result1['storage_methods']['ipfs']['hash'] != result2['storage_methods']['ipfs']['hash']
    
    def test_hybrid_with_large_data(self, hybrid):
        """Test hybrid storage with large data"""
        log_data = {
            'agent_id': 'agent-001',
            'action': 'test',
            'data': 'x' * 100000
        }
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert result['storage_methods']['ipfs']['status'] == 'success'
        assert result['storage_methods']['blockchain']['status'] == 'success'
    
    def test_hybrid_with_empty_data(self, hybrid):
        """Test hybrid storage with empty data"""
        log_data = {}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert result['storage_methods']['ipfs']['status'] == 'success'
    
    def test_hybrid_timestamp_consistency(self, hybrid):
        """Test that timestamps are consistent"""
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        
        assert 'timestamp' in result
        assert isinstance(result['timestamp'], str)


class TestEdgeCases:
    """Test edge cases and error conditions"""
    
    def test_ipfs_with_special_characters(self):
        """Test IPFS with special characters in data"""
        ipfs = IPFSAuditStorage()
        log_data = {
            'agent_id': 'agent-001',
            'action': 'test',
            'data': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        assert ipfs_hash is not None
        assert len(ipfs_hash) == 64
    
    def test_ipfs_with_unicode(self):
        """Test IPFS with unicode characters"""
        ipfs = IPFSAuditStorage()
        log_data = {
            'agent_id': 'agent-001',
            'action': 'test',
            'data': '你好世界 🌍 مرحبا'
        }
        
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        assert ipfs_hash is not None
        assert len(ipfs_hash) == 64
    
    def test_blockchain_with_many_records(self):
        """Test blockchain with many records"""
        blockchain = BlockchainAuditStorage()
        
        for i in range(100):
            blockchain.store_audit_hash('agent-001', f'{i}' * 64)
        
        history = blockchain.get_audit_history('agent-001')
        
        assert len(history) == 100
    
    def test_distributed_with_many_nodes(self):
        """Test distributed storage with many nodes"""
        nodes = [f'node-{i}' for i in range(100)]
        distributed = DistributedAuditStorage(nodes)
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        result = distributed.replicate_audit_log('agent-001', log_data)
        
        assert len(result['nodes']) == 100
    
    def test_hybrid_concurrent_operations(self):
        """Test hybrid storage with concurrent-like operations"""
        hybrid = HybridDistributedStorage(['node-1', 'node-2'])
        
        results = []
        for i in range(10):
            log_data = {'agent_id': f'agent-{i:03d}', 'action': f'action-{i}'}
            result = hybrid.store_audit_log_hybrid(f'agent-{i:03d}', log_data)
            results.append(result)
        
        assert len(results) == 10
        for result in results:
            assert result['storage_methods']['ipfs']['status'] == 'success'


class TestIntegration:
    """Integration tests for distributed storage"""
    
    def test_full_workflow_ipfs_to_blockchain(self):
        """Test full workflow: IPFS -> Blockchain"""
        ipfs = IPFSAuditStorage()
        blockchain = BlockchainAuditStorage()
        
        log_data = {'agent_id': 'agent-001', 'action': 'deploy'}
        
        # Store on IPFS
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        # Store hash on blockchain
        tx_hash = blockchain.store_audit_hash('agent-001', ipfs_hash)
        
        # Verify on blockchain
        is_valid = blockchain.verify_audit_on_chain('agent-001', ipfs_hash)
        
        assert is_valid == True
    
    def test_full_workflow_hybrid_storage(self):
        """Test full workflow with hybrid storage"""
        nodes = ['node-1', 'node-2', 'node-3']
        hybrid = HybridDistributedStorage(nodes)
        
        log_data = {'agent_id': 'agent-001', 'action': 'deploy'}
        
        # Store using hybrid
        store_result = hybrid.store_audit_log_hybrid('agent-001', log_data)
        ipfs_hash = store_result['storage_methods']['ipfs']['hash']
        
        # Verify using hybrid
        verify_result = hybrid.verify_audit_log_hybrid('agent-001', ipfs_hash)
        
        assert verify_result['overall_valid'] == True
    
    def test_multi_agent_workflow(self):
        """Test workflow with multiple agents"""
        hybrid = HybridDistributedStorage(['node-1', 'node-2'])
        
        agents = ['agent-001', 'agent-002', 'agent-003']
        
        for agent_id in agents:
            log_data = {'agent_id': agent_id, 'action': 'deploy'}
            result = hybrid.store_audit_log_hybrid(agent_id, log_data)
            assert result['storage_methods']['ipfs']['status'] == 'success'
        
        status = hybrid.get_storage_status()
        assert status['ipfs']['status'] == 'operational'
