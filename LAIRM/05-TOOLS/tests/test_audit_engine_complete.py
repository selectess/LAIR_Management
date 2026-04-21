# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Complete Test Suite for LAIRM Audit Engine
Tests audit chain integrity, tampering detection, and performance
"""

import pytest
import json
import time
from audit_engine.lairm_audit_engine import LAIRMAuditEngine


class TestAuditEngineComplete:
    """Complete test suite for audit engine"""
    
    @pytest.fixture
    def engine(self):
        """Initialize audit engine"""
        return LAIRMAuditEngine()
    
    # ===== BASIC FUNCTIONALITY =====
    
    def test_create_audit_record(self, engine):
        """Test creating a single audit record"""
        record = engine.create_audit_record(
            agent_id='agent-001',
            action_type='deploy',
            details={'version': '1.0'}
        )
        
        assert record is not None
        assert record['agent_id'] == 'agent-001'
        assert record['action_type'] == 'deploy'
        assert 'hash' in record
        assert 'timestamp' in record
    
    def test_create_multiple_records(self, engine):
        """Test creating multiple audit records"""
        for i in range(10):
            engine.create_audit_record(
                agent_id='agent-001',
                action_type='action',
                details={'index': i}
            )
        
        assert len(engine.audit_chain) == 10
    
    def test_audit_chain_integrity(self, engine):
        """Test audit chain integrity with 100 records"""
        for i in range(100):
            engine.create_audit_record(
                agent_id='agent-001',
                action_type='action',
                details={'index': i}
            )
        
        assert engine.verify_audit_chain() == True
    
    def test_audit_chain_with_1000_records(self, engine):
        """Test audit chain integrity with 1000 records"""
        for i in range(1000):
            engine.create_audit_record(
                agent_id='agent-001',
                action_type='action',
                details={'index': i}
            )
        
        assert engine.verify_audit_chain() == True
        assert len(engine.audit_chain) == 1000
    
    # ===== TAMPERING DETECTION =====
    
    def test_detect_tampering_single_record(self, engine):
        """Test detection of tampering in a single record"""
        engine.create_audit_record('agent-001', 'action', {})
        engine.create_audit_record('agent-001', 'action', {})
        
        # Tamper with first record
        engine.audit_chain[0]['details'] = {'tampered': True}
        
        assert engine.verify_audit_chain() == False
    
    def test_detect_tampering_hash(self, engine):
        """Test detection of hash tampering"""
        engine.create_audit_record('agent-001', 'action', {})
        
        # Tamper with hash
        engine.audit_chain[0]['hash'] = 'invalid_hash'
        
        assert engine.verify_audit_chain() == False
    
    def test_detect_tampering_previous_hash(self, engine):
        """Test detection of previous_hash tampering"""
        engine.create_audit_record('agent-001', 'action', {})
        engine.create_audit_record('agent-001', 'action', {})
        
        # Tamper with previous_hash
        engine.audit_chain[1]['previous_hash'] = 'invalid_hash'
        
        assert engine.verify_audit_chain() == False
    
    def test_detect_tampering_timestamp(self, engine):
        """Test detection of timestamp tampering"""
        engine.create_audit_record('agent-001', 'action', {})
        
        # Tamper with timestamp
        original_hash = engine.audit_chain[0]['hash']
        engine.audit_chain[0]['timestamp'] = '2020-01-01T00:00:00Z'
        
        # Hash should no longer match
        assert engine.audit_chain[0]['hash'] != original_hash
    
    # ===== AGENT-SPECIFIC AUDITS =====
    
    def test_audit_by_agent(self, engine):
        """Test retrieving audit records by agent"""
        engine.create_audit_record('agent-001', 'action', {})
        engine.create_audit_record('agent-002', 'action', {})
        engine.create_audit_record('agent-001', 'action', {})
        
        agent_001_records = engine.get_agent_audit_records('agent-001')
        assert len(agent_001_records) == 2
        
        agent_002_records = engine.get_agent_audit_records('agent-002')
        assert len(agent_002_records) == 1
    
    def test_audit_by_action_type(self, engine):
        """Test retrieving audit records by action type"""
        engine.create_audit_record('agent-001', 'deploy', {})
        engine.create_audit_record('agent-001', 'update', {})
        engine.create_audit_record('agent-001', 'deploy', {})
        
        deploy_records = engine.get_records_by_action_type('deploy')
        assert len(deploy_records) == 2
        
        update_records = engine.get_records_by_action_type('update')
        assert len(update_records) == 1
    
    def test_audit_by_time_range(self, engine):
        """Test retrieving audit records by time range"""
        import datetime
        
        start_time = datetime.datetime.utcnow()
        engine.create_audit_record('agent-001', 'action', {})
        time.sleep(0.1)
        engine.create_audit_record('agent-001', 'action', {})
        end_time = datetime.datetime.utcnow()
        
        records = engine.get_records_by_time_range(start_time, end_time)
        assert len(records) >= 2
    
    # ===== AUDIT REPORTS =====
    
    def test_generate_audit_report(self, engine):
        """Test generating audit report"""
        for i in range(10):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        report = engine.generate_audit_report('agent-001')
        
        assert 'agent_id' in report
        assert 'total_records' in report
        assert 'chain_valid' in report
        assert report['total_records'] == 10
        assert report['chain_valid'] == True
    
    def test_audit_report_with_tampering(self, engine):
        """Test audit report detects tampering"""
        engine.create_audit_record('agent-001', 'action', {})
        engine.create_audit_record('agent-001', 'action', {})
        
        # Tamper
        engine.audit_chain[0]['details'] = {'tampered': True}
        
        report = engine.generate_audit_report('agent-001')
        assert report['chain_valid'] == False
    
    def test_audit_statistics(self, engine):
        """Test audit statistics"""
        for i in range(50):
            engine.create_audit_record('agent-001', 'deploy', {})
        for i in range(30):
            engine.create_audit_record('agent-001', 'update', {})
        for i in range(20):
            engine.create_audit_record('agent-002', 'deploy', {})
        
        stats = engine.get_audit_statistics()
        
        assert stats['total_records'] == 100
        assert stats['total_agents'] == 2
        assert stats['action_types']['deploy'] == 70
        assert stats['action_types']['update'] == 30
    
    # ===== EXPORT & IMPORT =====
    
    def test_export_audit_chain(self, engine):
        """Test exporting audit chain"""
        for i in range(10):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        exported = engine.export_audit_chain()
        
        assert isinstance(exported, str)
        data = json.loads(exported)
        assert len(data) == 10
    
    def test_export_agent_audit(self, engine):
        """Test exporting agent-specific audit"""
        engine.create_audit_record('agent-001', 'action', {})
        engine.create_audit_record('agent-002', 'action', {})
        
        exported = engine.export_agent_audit('agent-001')
        data = json.loads(exported)
        
        assert len(data) == 1
        assert data[0]['agent_id'] == 'agent-001'
    
    # ===== PERFORMANCE TESTS =====
    
    def test_performance_create_records(self, engine):
        """Test performance of creating records"""
        start_time = time.time()
        
        for i in range(1000):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        elapsed = time.time() - start_time
        
        # Should complete in less than 5 seconds
        assert elapsed < 5.0
        assert len(engine.audit_chain) == 1000
    
    def test_performance_verify_chain(self, engine):
        """Test performance of verifying chain"""
        for i in range(1000):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        start_time = time.time()
        result = engine.verify_audit_chain()
        elapsed = time.time() - start_time
        
        # Should complete in less than 2 seconds
        assert elapsed < 2.0
        assert result == True
    
    def test_performance_generate_report(self, engine):
        """Test performance of generating report"""
        for i in range(1000):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        start_time = time.time()
        report = engine.generate_audit_report('agent-001')
        elapsed = time.time() - start_time
        
        # Should complete in less than 1 second
        assert elapsed < 1.0
        assert report['total_records'] == 1000
    
    # ===== EDGE CASES =====
    
    def test_empty_audit_chain(self, engine):
        """Test with empty audit chain"""
        assert engine.verify_audit_chain() == True
        assert len(engine.audit_chain) == 0
    
    def test_single_record(self, engine):
        """Test with single record"""
        engine.create_audit_record('agent-001', 'action', {})
        assert engine.verify_audit_chain() == True
        assert len(engine.audit_chain) == 1
    
    def test_special_characters_in_details(self, engine):
        """Test with special characters in details"""
        details = {
            'text': 'Special chars: !@#$%^&*()',
            'unicode': '你好世界',
            'emoji': '🚀🎯✅'
        }
        
        record = engine.create_audit_record('agent-001', 'action', details)
        assert engine.verify_audit_chain() == True
        assert record['details'] == details
    
    def test_large_details_payload(self, engine):
        """Test with large details payload"""
        large_details = {
            'data': 'x' * 10000,  # 10KB of data
            'nested': {
                'level1': {
                    'level2': {
                        'level3': 'deep'
                    }
                }
            }
        }
        
        record = engine.create_audit_record('agent-001', 'action', large_details)
        assert engine.verify_audit_chain() == True
    
    def test_concurrent_agents(self, engine):
        """Test with records from multiple agents"""
        agents = [f'agent-{i:03d}' for i in range(100)]
        
        for agent in agents:
            for j in range(10):
                engine.create_audit_record(agent, 'action', {'index': j})
        
        assert engine.verify_audit_chain() == True
        assert len(engine.audit_chain) == 1000
    
    # ===== RECOVERY & RESILIENCE =====
    
    def test_recovery_after_error(self, engine):
        """Test recovery after error"""
        engine.create_audit_record('agent-001', 'action', {})
        
        try:
            # Simulate error
            raise Exception("Simulated error")
        except:
            pass
        
        # Should still be able to create records
        engine.create_audit_record('agent-001', 'action', {})
        assert len(engine.audit_chain) == 2
        assert engine.verify_audit_chain() == True
    
    def test_chain_consistency_after_operations(self, engine):
        """Test chain consistency after various operations"""
        # Create records
        for i in range(100):
            engine.create_audit_record('agent-001', 'action', {'index': i})
        
        # Export
        exported = engine.export_audit_chain()
        
        # Verify
        assert engine.verify_audit_chain() == True
        
        # Generate report
        report = engine.generate_audit_report('agent-001')
        assert report['chain_valid'] == True
        
        # Get statistics
        stats = engine.get_audit_statistics()
        assert stats['total_records'] == 100


class TestAuditEngineIntegration:
    """Integration tests for audit engine"""
    
    @pytest.fixture
    def engine(self):
        return LAIRMAuditEngine()
    
    def test_full_audit_workflow(self, engine):
        """Test full audit workflow"""
        # 1. Create records
        for i in range(50):
            engine.create_audit_record('agent-001', 'deploy', {'version': f'1.{i}'})
        
        # 2. Verify integrity
        assert engine.verify_audit_chain() == True
        
        # 3. Generate report
        report = engine.generate_audit_report('agent-001')
        assert report['chain_valid'] == True
        assert report['total_records'] == 50
        
        # 4. Export
        exported = engine.export_audit_chain()
        assert len(exported) > 0
        
        # 5. Get statistics
        stats = engine.get_audit_statistics()
        assert stats['total_records'] == 50
    
    def test_multi_agent_audit_workflow(self, engine):
        """Test multi-agent audit workflow"""
        # Create records for multiple agents
        for agent_id in ['agent-001', 'agent-002', 'agent-003']:
            for i in range(20):
                engine.create_audit_record(agent_id, 'action', {'index': i})
        
        # Verify integrity
        assert engine.verify_audit_chain() == True
        
        # Get agent-specific records
        agent_001_records = engine.get_agent_audit_records('agent-001')
        assert len(agent_001_records) == 20
        
        # Get statistics
        stats = engine.get_audit_statistics()
        assert stats['total_records'] == 60
        assert stats['total_agents'] == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
