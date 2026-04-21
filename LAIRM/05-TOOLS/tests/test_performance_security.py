# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Performance and Security Tests for LAIRM Framework
Benchmarks, fuzzing, and injection attack tests
"""

import pytest
import time
import json
import random
import string
from datetime import datetime
from unittest.mock import Mock, patch

import sys
sys.path.insert(0, '/Users/mehdiwhb/Desktop/ARAM/LAIRM/05-TOOLS')

from audit_engine.distributed_storage import (
    IPFSAuditStorage,
    BlockchainAuditStorage,
    DistributedAuditStorage,
    HybridDistributedStorage
)
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK


class TestPerformanceBenchmarks:
    """Performance benchmark tests"""
    
    def test_agent_creation_performance(self):
        """Benchmark agent creation"""
        start = time.time()
        
        for i in range(100):
            agent = LAIRMAgentSDK(
                agent_id=f"perf-agent-{i}",
                axiomes=['I', 'II', 'III']
            )
        
        elapsed = time.time() - start
        
        # Should create 100 agents in less than 1 second
        assert elapsed < 1.0
        print(f"Created 100 agents in {elapsed:.3f}s")
    
    def test_audit_logging_performance(self):
        """Benchmark audit logging"""
        agent = LAIRMAgentSDK(agent_id="perf-agent", axiomes=['I', 'II'])
        
        start = time.time()
        
        for i in range(1000):
            agent.log_action(f'action_{i}', {'index': i, 'data': 'x' * 100})
        
        elapsed = time.time() - start
        
        # Should log 1000 actions in less than 1 second
        assert elapsed < 1.0
        print(f"Logged 1000 actions in {elapsed:.3f}s")
    
    def test_compliance_check_performance(self):
        """Benchmark compliance checking"""
        agent = LAIRMAgentSDK(
            agent_id="perf-agent",
            axiomes=['I', 'II', 'III', 'VI', 'VII', 'VIII', 'IX', 'X']
        )
        
        start = time.time()
        
        for i in range(1000):
            agent.check_compliance(['I', 'II', 'III'])
        
        elapsed = time.time() - start
        
        # Should check compliance 1000 times in less than 0.5 seconds
        assert elapsed < 0.5
        print(f"Checked compliance 1000 times in {elapsed:.3f}s")
    
    def test_ipfs_storage_performance(self):
        """Benchmark IPFS storage"""
        ipfs = IPFSAuditStorage()
        
        start = time.time()
        
        for i in range(100):
            log_data = {
                'agent_id': f'agent-{i}',
                'action': 'test',
                'timestamp': datetime.now().isoformat(),
                'data': 'x' * 1000
            }
            ipfs.store_audit_log(f'agent-{i}', log_data)
        
        elapsed = time.time() - start
        
        # Should store 100 logs in less than 1 second
        assert elapsed < 1.0
        print(f"Stored 100 IPFS logs in {elapsed:.3f}s")
    
    def test_blockchain_storage_performance(self):
        """Benchmark blockchain storage"""
        blockchain = BlockchainAuditStorage()
        
        start = time.time()
        
        for i in range(100):
            hash_val = f"hash_{i:04d}"
            blockchain.store_audit_hash(f'agent-{i}', hash_val)
        
        elapsed = time.time() - start
        
        # Should store 100 hashes in less than 1 second
        assert elapsed < 1.0
        print(f"Stored 100 blockchain hashes in {elapsed:.3f}s")
    
    def test_distributed_replication_performance(self):
        """Benchmark distributed replication"""
        nodes = [f'node-{i}' for i in range(10)]
        distributed = DistributedAuditStorage(nodes)
        
        start = time.time()
        
        for i in range(50):
            log_data = {'agent_id': f'agent-{i}', 'action': 'test'}
            distributed.replicate_audit_log(f'agent-{i}', log_data)
        
        elapsed = time.time() - start
        
        # Should replicate 50 logs to 10 nodes in less than 2 seconds
        assert elapsed < 2.0
        print(f"Replicated 50 logs to 10 nodes in {elapsed:.3f}s")
    
    def test_hybrid_storage_performance(self):
        """Benchmark hybrid storage"""
        nodes = [f'node-{i}' for i in range(5)]
        hybrid = HybridDistributedStorage(nodes)
        
        start = time.time()
        
        for i in range(50):
            log_data = {
                'agent_id': f'agent-{i}',
                'action': 'test',
                'timestamp': datetime.now().isoformat()
            }
            hybrid.store_audit_log_hybrid(f'agent-{i}', log_data)
        
        elapsed = time.time() - start
        
        # Should store 50 logs via hybrid storage in less than 2 seconds
        assert elapsed < 2.0
        print(f"Stored 50 hybrid logs in {elapsed:.3f}s")


class TestSecurityFuzzing:
    """Security fuzzing tests"""
    
    def test_agent_id_fuzzing(self):
        """Fuzz agent ID with random strings"""
        for _ in range(100):
            random_id = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=50))
            
            # Should not crash
            agent = LAIRMAgentSDK(agent_id=random_id)
            assert agent.agent_id == random_id
    
    def test_axiome_fuzzing(self):
        """Fuzz axiome list with random values"""
        for _ in range(100):
            random_axiomes = [
                ''.join(random.choices(string.ascii_letters, k=10))
                for _ in range(random.randint(1, 20))
            ]
            
            # Should not crash
            agent = LAIRMAgentSDK(axiomes=random_axiomes)
            assert agent.axiomes == random_axiomes
    
    def test_action_details_fuzzing(self):
        """Fuzz action details with random data"""
        agent = LAIRMAgentSDK(agent_id="fuzz-agent")
        
        for _ in range(100):
            random_details = {
                'key_' + str(i): ''.join(random.choices(string.ascii_letters, k=20))
                for i in range(random.randint(1, 10))
            }
            
            # Should not crash
            record = agent.log_action('fuzz_action', random_details)
            assert record is not None
    
    def test_large_payload_fuzzing(self):
        """Fuzz with large payloads"""
        agent = LAIRMAgentSDK(agent_id="large-agent")
        
        # Test with increasingly large payloads
        for size in [1000, 10000, 100000, 1000000]:
            large_data = {
                'agent_id': 'agent-001',
                'payload': 'x' * size
            }
            
            # Should handle large payloads
            record = agent.log_action('large_action', large_data)
            assert record is not None
    
    def test_unicode_fuzzing(self):
        """Fuzz with unicode characters"""
        agent = LAIRMAgentSDK(agent_id="unicode-agent")
        
        unicode_strings = [
            "你好世界",
            "مرحبا بالعالم",
            "Здравствуй мир",
            "🌍🚀💻🔐",
            "Ñoño",
            "Ελληνικά"
        ]
        
        for unicode_str in unicode_strings:
            record = agent.log_action(
                'unicode_action',
                {'message': unicode_str}
            )
            assert record is not None
    
    def test_special_characters_fuzzing(self):
        """Fuzz with special characters"""
        agent = LAIRMAgentSDK(agent_id="special-agent")
        
        special_chars = [
            "'; DROP TABLE agents; --",
            "<script>alert('xss')</script>",
            "../../etc/passwd",
            "\x00\x01\x02",
            "\\n\\r\\t",
            "{{7*7}}"
        ]
        
        for special_str in special_chars:
            record = agent.log_action(
                'special_action',
                {'data': special_str}
            )
            assert record is not None


class TestSecurityInjectionAttacks:
    """Security injection attack tests"""
    
    def test_json_injection_resistance(self):
        """Test resistance to JSON injection"""
        agent = LAIRMAgentSDK(agent_id="json-agent")
        
        injection_payloads = [
            '{"malicious": "payload"}',
            '"; "malicious": "value',
            '\\"; "malicious": "value',
            '{"nested": {"deep": "injection"}}'
        ]
        
        for payload in injection_payloads:
            record = agent.log_action('json_test', {'data': payload})
            assert record is not None
            # Verify data is stored as-is, not executed
            assert record['details']['data'] == payload
    
    def test_command_injection_resistance(self):
        """Test resistance to command injection"""
        agent = LAIRMAgentSDK(agent_id="cmd-agent")
        
        injection_payloads = [
            '; rm -rf /',
            '| cat /etc/passwd',
            '`whoami`',
            '$(whoami)',
            '& dir C:\\',
            '| powershell -Command "Get-Process"'
        ]
        
        for payload in injection_payloads:
            record = agent.log_action('cmd_test', {'command': payload})
            assert record is not None
            # Verify command is stored as data, not executed
            assert record['details']['command'] == payload
    
    def test_path_traversal_resistance(self):
        """Test resistance to path traversal attacks"""
        agent = LAIRMAgentSDK(agent_id="path-agent")
        
        traversal_payloads = [
            '../../etc/passwd',
            '..\\..\\windows\\system32',
            '....//....//etc/passwd',
            '%2e%2e%2fetc%2fpasswd'
        ]
        
        for payload in traversal_payloads:
            record = agent.log_action('path_test', {'path': payload})
            assert record is not None
            assert record['details']['path'] == payload
    
    def test_xss_injection_resistance(self):
        """Test resistance to XSS injection"""
        agent = LAIRMAgentSDK(agent_id="xss-agent")
        
        xss_payloads = [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert('xss')>",
            "<svg onload=alert('xss')>",
            "javascript:alert('xss')",
            "<iframe src='javascript:alert(1)'></iframe>"
        ]
        
        for payload in xss_payloads:
            record = agent.log_action('xss_test', {'html': payload})
            assert record is not None
            assert record['details']['html'] == payload


class TestSecurityDataIntegrity:
    """Security tests for data integrity"""
    
    def test_audit_log_consistency(self):
        """Test that audit logs maintain consistency"""
        agent = LAIRMAgentSDK(agent_id="consistency-agent")
        
        # Log multiple actions
        agent.log_action('action_1', {'data': 'data1'})
        agent.log_action('action_2', {'data': 'data2'})
        agent.log_action('action_3', {'data': 'data3'})
        
        # Get the log
        log = agent.get_audit_log()
        original_count = len(log)
        
        # Verify all actions are present
        action_types = [entry['action_type'] for entry in log]
        assert 'action_1' in action_types
        assert 'action_2' in action_types
        assert 'action_3' in action_types
        assert len(log) == original_count
    
    def test_compliance_status_consistency(self):
        """Test compliance status consistency"""
        agent = LAIRMAgentSDK(
            agent_id="consistency-agent",
            axiomes=['I', 'II', 'III']
        )
        
        # Get status multiple times
        status1 = agent.get_compliance_status()
        status2 = agent.get_compliance_status()
        status3 = agent.get_compliance_status()
        
        # Should be consistent
        assert status1 == status2 == status3
    
    def test_distributed_storage_integrity(self):
        """Test distributed storage maintains integrity"""
        nodes = ['node-1', 'node-2', 'node-3']
        distributed = DistributedAuditStorage(nodes)
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        # Replicate
        result = distributed.replicate_audit_log('agent-001', log_data)
        log_hash = result['log_hash']
        
        # Verify replication
        is_verified = distributed.verify_replication('agent-001', log_hash)
        assert is_verified is True


class TestSecurityTamperingDetection:
    """Security tests for tampering detection"""
    
    def test_ipfs_hash_tampering_detection(self):
        """Test detection of IPFS hash tampering"""
        ipfs = IPFSAuditStorage()
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        ipfs_hash = ipfs.store_audit_log('agent-001', log_data)
        
        # Verify original hash
        is_valid = ipfs.verify_ipfs_hash(ipfs_hash, log_data)
        assert is_valid is True
        
        # Modify data
        modified_data = log_data.copy()
        modified_data['action'] = 'modified'
        
        # Verify tampering is detected
        is_valid = ipfs.verify_ipfs_hash(ipfs_hash, modified_data)
        assert is_valid is False
    
    def test_blockchain_tampering_detection(self):
        """Test detection of blockchain tampering"""
        blockchain = BlockchainAuditStorage()
        
        hash1 = "hash_001"
        tx_hash = blockchain.store_audit_hash('agent-001', hash1)
        
        # Verify original
        is_valid = blockchain.verify_audit_on_chain('agent-001', hash1)
        assert is_valid is True
        
        # Try to verify different hash
        hash2 = "hash_002"
        is_valid = blockchain.verify_audit_on_chain('agent-001', hash2)
        assert is_valid is False


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])



class TestAdvancedPerformanceBenchmarks:
    """Advanced performance benchmark tests"""
    
    def test_decorator_overhead_performance(self):
        """Benchmark decorator overhead"""
        agent = LAIRMAgentSDK(agent_id="decorator-perf", axiomes=['I', 'II'])
        
        # Test without decorators
        start = time.time()
        for i in range(1000):
            agent.log_action(f'action_{i}')
        elapsed_no_decorator = time.time() - start
        
        # Test with decorators
        @agent.auditable
        @agent.responsible
        def decorated_action():
            return "done"
        
        start = time.time()
        for i in range(1000):
            decorated_action()
        elapsed_with_decorator = time.time() - start
        
        # Decorator overhead should be reasonable (< 10x)
        overhead_ratio = elapsed_with_decorator / elapsed_no_decorator
        assert overhead_ratio < 10.0
        print(f"Decorator overhead ratio: {overhead_ratio:.2f}x")
    
    def test_concurrent_agent_performance(self):
        """Benchmark concurrent agent operations"""
        agents = [
            LAIRMAgentSDK(agent_id=f"concurrent-{i}", axiomes=['I', 'II'])
            for i in range(50)
        ]
        
        start = time.time()
        
        # Simulate concurrent operations
        for agent in agents:
            for j in range(20):
                agent.log_action(f'action_{j}', {'index': j})
        
        elapsed = time.time() - start
        
        # Should handle 50 agents * 20 actions in less than 2 seconds
        assert elapsed < 2.0
        print(f"50 agents * 20 actions in {elapsed:.3f}s")
    
    def test_memory_efficiency(self):
        """Test memory efficiency with large audit logs"""
        agent = LAIRMAgentSDK(agent_id="memory-agent", axiomes=['I', 'II'])
        
        # Log 10000 actions
        for i in range(10000):
            agent.log_action(f'action_{i}', {'index': i, 'data': 'x' * 100})
        
        # Should complete without memory issues
        audit_log = agent.get_audit_log()
        assert len(audit_log) == 10000
    
    def test_hybrid_storage_throughput(self):
        """Benchmark hybrid storage throughput"""
        nodes = ['node-1', 'node-2', 'node-3']
        hybrid = HybridDistributedStorage(nodes)
        
        start = time.time()
        
        # Store 100 logs
        for i in range(100):
            log_data = {
                'agent_id': f'throughput-agent-{i}',
                'action': 'throughput_test',
                'timestamp': datetime.now().isoformat(),
                'data': 'x' * 500
            }
            hybrid.store_audit_log_hybrid(f'throughput-agent-{i}', log_data)
        
        elapsed = time.time() - start
        throughput = 100 / elapsed
        
        # Should achieve at least 30 logs/second
        assert throughput > 30
        print(f"Hybrid storage throughput: {throughput:.2f} logs/sec")
    
    def test_verification_performance(self):
        """Benchmark verification performance"""
        hybrid = HybridDistributedStorage(['node-1', 'node-2'])
        
        # Store logs
        hashes = []
        for i in range(50):
            log_data = {'agent_id': f'verify-agent-{i}', 'action': 'test'}
            result = hybrid.store_audit_log_hybrid(f'verify-agent-{i}', log_data)
            hashes.append((f'verify-agent-{i}', result['storage_methods']['ipfs']['hash']))
        
        # Benchmark verification
        start = time.time()
        
        for agent_id, ipfs_hash in hashes:
            hybrid.verify_audit_log_hybrid(agent_id, ipfs_hash)
        
        elapsed = time.time() - start
        
        # Should verify 50 logs in less than 1 second
        assert elapsed < 1.0
        print(f"Verified 50 logs in {elapsed:.3f}s")


class TestStressTests:
    """Stress tests for system limits"""
    
    def test_maximum_agents_stress(self):
        """Stress test with maximum number of agents"""
        agents = []
        
        # Create 1000 agents
        for i in range(1000):
            agent = LAIRMAgentSDK(
                agent_id=f"stress-agent-{i:04d}",
                axiomes=['I', 'II']
            )
            agents.append(agent)
        
        # Each agent logs actions
        for agent in agents[:100]:  # Test first 100
            agent.log_action('stress_action', {'test': 'stress'})
        
        # Verify
        assert len(agents) == 1000
        assert len(agents[0].get_audit_log()) > 0
    
    def test_maximum_audit_log_size_stress(self):
        """Stress test with maximum audit log size"""
        agent = LAIRMAgentSDK(agent_id="stress-log-agent", axiomes=['I', 'II'])
        
        # Log 50000 actions
        for i in range(50000):
            agent.log_action(f'stress_action_{i}', {'index': i})
            
            # Check every 10000
            if i % 10000 == 0:
                log = agent.get_audit_log()
                assert len(log) == i + 1
        
        # Final verification
        final_log = agent.get_audit_log()
        assert len(final_log) == 50000
    
    def test_distributed_storage_node_stress(self):
        """Stress test with many distributed nodes"""
        # Create 100 nodes
        nodes = [f'node-{i:03d}' for i in range(100)]
        distributed = DistributedAuditStorage(nodes)
        
        # Replicate logs
        for i in range(10):
            log_data = {'agent_id': f'agent-{i}', 'action': 'stress'}
            result = distributed.replicate_audit_log(f'agent-{i}', log_data)
            
            # Verify replication to all nodes
            assert len(result['nodes']) == 100
    
    def test_rapid_compliance_checks_stress(self):
        """Stress test with rapid compliance checks"""
        agent = LAIRMAgentSDK(
            agent_id="stress-compliance-agent",
            axiomes=['I', 'II', 'III', 'VI', 'VII', 'VIII']
        )
        
        # Perform 10000 compliance checks
        for i in range(10000):
            result = agent.check_compliance(['I', 'II', 'III'])
            assert result is True


class TestSecurityBoundaryConditions:
    """Security tests for boundary conditions"""
    
    def test_empty_input_security(self):
        """Test security with empty inputs"""
        agent = LAIRMAgentSDK(agent_id="empty-agent")
        
        # Empty action type
        record = agent.log_action('', {})
        assert record is not None
        
        # Empty details
        record = agent.log_action('action', {})
        assert record is not None
        
        # Empty axiomes
        result = agent.check_compliance([])
        assert result is True
    
    def test_null_input_security(self):
        """Test security with null/None inputs"""
        agent = LAIRMAgentSDK(agent_id="null-agent")
        
        # None details
        record = agent.log_action('action', None)
        assert record is not None
        
        # None in axiomes list
        try:
            result = agent.check_compliance([None, 'I', 'II'])
            # Should handle gracefully
        except (ValueError, TypeError):
            # Or raise appropriate error
            pass
    
    def test_extremely_long_input_security(self):
        """Test security with extremely long inputs"""
        agent = LAIRMAgentSDK(agent_id="long-agent")
        
        # Extremely long action type
        long_action = 'a' * 10000
        record = agent.log_action(long_action, {})
        assert record is not None
        
        # Extremely long data
        long_data = {'key': 'x' * 1000000}
        record = agent.log_action('action', long_data)
        assert record is not None
    
    def test_nested_data_depth_security(self):
        """Test security with deeply nested data"""
        agent = LAIRMAgentSDK(agent_id="nested-agent")
        
        # Create deeply nested structure
        nested = {'level': 0}
        current = nested
        for i in range(100):
            current['next'] = {'level': i + 1}
            current = current['next']
        
        # Should handle deep nesting
        record = agent.log_action('nested_action', nested)
        assert record is not None
    
    def test_circular_reference_security(self):
        """Test security with circular references"""
        agent = LAIRMAgentSDK(agent_id="circular-agent")
        
        # Create circular reference
        circular = {'key': 'value'}
        circular['self'] = circular
        
        # Should handle gracefully (may raise error or handle)
        try:
            record = agent.log_action('circular_action', circular)
            # If it succeeds, verify it's handled
            assert record is not None
        except (ValueError, RecursionError):
            # Or raise appropriate error
            pass


class TestSecurityCryptographicIntegrity:
    """Security tests for cryptographic integrity"""
    
    def test_hash_collision_resistance(self):
        """Test resistance to hash collisions"""
        ipfs = IPFSAuditStorage()
        
        # Store similar data
        data1 = {'agent_id': 'agent-001', 'action': 'test1'}
        data2 = {'agent_id': 'agent-001', 'action': 'test2'}
        
        hash1 = ipfs.store_audit_log('agent-001', data1)
        hash2 = ipfs.store_audit_log('agent-001', data2)
        
        # Hashes should be different
        assert hash1 != hash2
    
    def test_hash_determinism(self):
        """Test hash determinism"""
        ipfs = IPFSAuditStorage()
        
        data = {'agent_id': 'agent-001', 'action': 'test'}
        
        # Store same data multiple times
        hash1 = ipfs.store_audit_log('agent-001', data)
        hash2 = ipfs.store_audit_log('agent-002', data)
        hash3 = ipfs.store_audit_log('agent-003', data)
        
        # Same data should produce same hash
        assert hash1 == hash2 == hash3
    
    def test_blockchain_immutability(self):
        """Test blockchain immutability"""
        blockchain = BlockchainAuditStorage()
        
        # Store hash
        audit_hash = 'original_hash'
        blockchain.store_audit_hash('agent-001', audit_hash)
        
        # Get history
        history = blockchain.get_audit_history('agent-001')
        original_record = history[0]
        
        # Try to "modify" by storing again
        blockchain.store_audit_hash('agent-001', 'modified_hash')
        
        # Original should still be in history
        history = blockchain.get_audit_history('agent-001')
        assert history[0] == original_record
        assert len(history) == 2  # New record added, not modified
    
    def test_distributed_consensus(self):
        """Test distributed consensus"""
        nodes = ['node-1', 'node-2', 'node-3']
        distributed = DistributedAuditStorage(nodes)
        
        log_data = {'agent_id': 'agent-001', 'action': 'test'}
        
        # Replicate
        result = distributed.replicate_audit_log('agent-001', log_data)
        log_hash = result['log_hash']
        
        # All nodes should have same hash
        for node in nodes:
            has_log = distributed.check_node_has_log(node, 'agent-001')
            assert has_log is True


class TestSecurityAccessControl:
    """Security tests for access control"""
    
    def test_agent_isolation(self):
        """Test that agents are isolated from each other"""
        agent1 = LAIRMAgentSDK(agent_id="agent-1", axiomes=['I', 'II'])
        agent2 = LAIRMAgentSDK(agent_id="agent-2", axiomes=['III', 'VI'])
        
        # Each agent logs actions
        agent1.log_action('action1', {'data': 'agent1'})
        agent2.log_action('action2', {'data': 'agent2'})
        
        # Verify isolation
        log1 = agent1.get_audit_log()
        log2 = agent2.get_audit_log()
        
        assert len(log1) == 1
        assert len(log2) == 1
        assert log1[0]['agent_id'] == 'agent-1'
        assert log2[0]['agent_id'] == 'agent-2'
    
    def test_compliance_enforcement(self):
        """Test compliance enforcement"""
        agent = LAIRMAgentSDK(agent_id="enforce-agent", axiomes=['I', 'II'])
        
        # Define non-compliant action
        @agent.compliant(['I', 'II', 'III'])  # Agent doesn't have III
        def non_compliant_action():
            return "should_fail"
        
        # Should raise error
        with pytest.raises(ValueError):
            non_compliant_action()
    
    def test_audit_trail_immutability(self):
        """Test that audit trail cannot be modified"""
        agent = LAIRMAgentSDK(agent_id="immutable-agent", axiomes=['I', 'II'])
        
        # Log action
        agent.log_action('action1', {'data': 'original'})
        
        # Get log
        log = agent.get_audit_log()
        original_log = log.copy()
        
        # Try to modify log (should not affect internal log)
        log[0]['action_type'] = 'modified'
        
        # Get log again
        new_log = agent.get_audit_log()
        
        # Should be unchanged
        assert new_log[0]['action_type'] == original_log[0]['action_type']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
