# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Integration Tests for LAIRM Framework
Complete workflow testing across all modules
"""

import pytest
import json
from datetime import datetime
from unittest.mock import Mock, patch

import sys
sys.path.insert(0, '/Users/mehdiwhb/Desktop/ARAM/LAIRM/05-TOOLS')

from audit_engine.distributed_storage import HybridDistributedStorage
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK
from mcp_server.lairm_mcp_server import LAIRMMCPServer


class TestFullComplianceWorkflow:
    """Integration tests for complete compliance workflow"""
    
    def test_agent_creation_to_audit_workflow(self):
        """Test complete workflow from agent creation to audit"""
        # Create agent
        agent = LAIRMAgentSDK(
            agent_id="workflow-agent-001",
            axiomes=['I', 'II', 'III', 'VI']
        )
        
        # Define compliant action
        @agent.compliant(['I', 'II'])
        @agent.auditable
        def deploy_service():
            agent.log_action('service_deployed', {'service': 'auth-service'})
            return "deployed"
        
        # Execute action
        result = deploy_service()
        assert result == "deployed"
        
        # Verify audit trail
        audit_log = agent.get_audit_log()
        assert len(audit_log) > 0
        
        # Verify compliance status
        status = agent.get_compliance_status()
        assert status['compliant'] is True
        assert status['audit_log_size'] > 0
    
    def test_multi_agent_compliance_matrix(self):
        """Test compliance matrix across multiple agents"""
        agents = [
            LAIRMAgentSDK(agent_id="agent-1", axiomes=['I', 'II']),
            LAIRMAgentSDK(agent_id="agent-2", axiomes=['I', 'II', 'III']),
            LAIRMAgentSDK(agent_id="agent-3", axiomes=['I', 'II', 'III', 'VI'])
        ]
        
        # Verify each agent's compliance
        for agent in agents:
            assert agent.check_compliance(agent.axiomes) is True
            status = agent.get_compliance_status()
            assert status['compliant'] is True
    
    def test_distributed_storage_with_audit_trail(self):
        """Test distributed storage integration with audit trail"""
        # Create hybrid storage
        nodes = ['node-1', 'node-2', 'node-3']
        hybrid = HybridDistributedStorage(nodes)
        
        # Create audit data
        audit_data = {
            'agent_id': 'agent-001',
            'action': 'deploy',
            'timestamp': datetime.now().isoformat(),
            'axiomes_checked': ['I', 'II', 'III']
        }
        
        # Store audit log
        result = hybrid.store_audit_log_hybrid('agent-001', audit_data)
        
        # Verify storage
        assert result['storage_methods']['ipfs']['status'] == 'success'
        assert result['storage_methods']['blockchain']['status'] == 'success'
        assert result['storage_methods']['distributed']['status'] == 'success'
    
    def test_agent_to_mcp_server_workflow(self):
        """Test workflow from agent to MCP server"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            # Create agent
            agent = LAIRMAgentSDK(
                agent_id="mcp-agent",
                axiomes=['I', 'II', 'III']
            )
            
            # Create MCP server
            server = LAIRMMCPServer()
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1},
                'AXIOM-II': {'name': 'AXIOM-II', 'articles': [], 'count': 1},
                'AXIOM-III': {'name': 'AXIOM-III', 'articles': [], 'count': 1}
            }
            
            # Validate agent compliance via MCP server
            agent_config = {
                'agent_id': agent.agent_id,
                'axiomes_required': agent.axiomes
            }
            
            compliance = server.validate_compliance(agent_config)
            assert compliance['compliant'] is True


class TestAuditTrailIntegration:
    """Integration tests for audit trail functionality"""
    
    def test_complete_audit_trail_workflow(self):
        """Test complete audit trail from action to storage"""
        # Create agent with audit
        agent = LAIRMAgentSDK(agent_id="audit-agent", axiomes=['I', 'II', 'III', 'VI'])
        
        # Perform multiple actions
        @agent.auditable
        def action1():
            agent.log_action('action_1', {'data': 'value1'})
            return "result1"
        
        @agent.auditable
        def action2():
            agent.log_action('action_2', {'data': 'value2'})
            return "result2"
        
        @agent.auditable
        def action3():
            agent.log_action('action_3', {'data': 'value3'})
            return "result3"
        
        # Execute actions
        action1()
        action2()
        action3()
        
        # Verify audit trail
        audit_log = agent.get_audit_log()
        assert len(audit_log) >= 9  # 3 actions * 3 entries each (start, internal, success)
        
        # Verify action sequence
        action_types = [entry['action_type'] for entry in audit_log]
        assert any('audit_start_action1' in at for at in action_types)
        assert any('audit_start_action2' in at for at in action_types)
        assert any('audit_start_action3' in at for at in action_types)
    
    def test_audit_trail_with_errors(self):
        """Test audit trail captures errors"""
        agent = LAIRMAgentSDK(agent_id="error-agent", axiomes=['I', 'II'])
        
        @agent.auditable
        def failing_action():
            raise ValueError("Test error")
        
        # Execute and catch error
        with pytest.raises(ValueError):
            failing_action()
        
        # Verify error was logged
        audit_log = agent.get_audit_log()
        assert any('audit_error' in entry['action_type'] for entry in audit_log)


class TestSecurityIntegration:
    """Integration tests for security features"""
    
    def test_supervised_action_workflow(self):
        """Test supervised action with human approval"""
        agent = LAIRMAgentSDK(agent_id="supervised-agent", axiomes=['I', 'II'])
        
        @agent.supervised
        def critical_action():
            return "action_completed"
        
        result = critical_action()
        assert result == "action_completed"
        
        # Verify supervision was logged
        audit_log = agent.get_audit_log()
        assert any('supervised_critical_action' in entry['action_type'] for entry in audit_log)
        assert any('human_approval' in entry['action_type'] for entry in audit_log)
    
    def test_responsible_action_tracking(self):
        """Test responsible action tracking"""
        agent = LAIRMAgentSDK(agent_id="responsible-agent", axiomes=['I', 'II'])
        
        @agent.responsible
        def tracked_action():
            return "tracked"
        
        result = tracked_action()
        assert result == "tracked"
        
        # Verify responsibility was tracked
        audit_log = agent.get_audit_log()
        assert any('responsible_tracked_action' in entry['action_type'] for entry in audit_log)


class TestPerformanceIntegration:
    """Integration tests for performance"""
    
    def test_high_volume_audit_logging(self):
        """Test performance with high volume of audit logs"""
        agent = LAIRMAgentSDK(agent_id="perf-agent", axiomes=['I', 'II'])
        
        # Log many actions
        for i in range(100):
            agent.log_action(f'action_{i}', {'index': i})
        
        # Verify all logged
        audit_log = agent.get_audit_log()
        assert len(audit_log) == 100
    
    def test_distributed_storage_performance(self):
        """Test distributed storage performance"""
        nodes = ['node-1', 'node-2', 'node-3', 'node-4', 'node-5']
        hybrid = HybridDistributedStorage(nodes)
        
        # Store multiple audit logs
        for i in range(10):
            audit_data = {
                'agent_id': f'agent-{i}',
                'action': 'test',
                'timestamp': datetime.now().isoformat()
            }
            result = hybrid.store_audit_log_hybrid(f'agent-{i}', audit_data)
            assert result['storage_methods']['ipfs']['status'] == 'success'


class TestComplexWorkflows:
    """Integration tests for complex workflows"""
    
    def test_multi_agent_coordination(self):
        """Test coordination between multiple agents"""
        # Create multiple agents
        agents = [
            LAIRMAgentSDK(agent_id=f"agent-{i}", axiomes=['I', 'II', 'III'])
            for i in range(3)
        ]
        
        # Each agent performs actions
        for agent in agents:
            @agent.auditable
            def coordinated_action():
                agent.log_action('coordination_action', {'agent': agent.agent_id})
                return "coordinated"
            
            result = coordinated_action()
            assert result == "coordinated"
        
        # Verify all agents have audit trails
        for agent in agents:
            audit_log = agent.get_audit_log()
            assert len(audit_log) > 0
    
    def test_compliance_verification_workflow(self):
        """Test complete compliance verification workflow"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            # Create agent
            agent = LAIRMAgentSDK(
                agent_id="compliance-agent",
                axiomes=['I', 'II', 'III', 'VI']
            )
            
            # Create MCP server
            server = LAIRMMCPServer()
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1},
                'AXIOM-II': {'name': 'AXIOM-II', 'articles': [], 'count': 1},
                'AXIOM-III': {'name': 'AXIOM-III', 'articles': [], 'count': 1},
                'AXIOM-VI': {'name': 'AXIOM-VI', 'articles': [], 'count': 1}
            }
            
            # Perform action
            @agent.compliant(['I', 'II'])
            @agent.auditable
            def compliant_action():
                return "success"
            
            result = compliant_action()
            assert result == "success"
            
            # Verify compliance
            agent_config = {
                'agent_id': agent.agent_id,
                'axiomes_required': agent.axiomes
            }
            
            compliance = server.validate_compliance(agent_config)
            assert compliance['compliant'] is True
            
            # Audit the action
            action = {
                'type': 'compliant_action',
                'timestamp': datetime.now().isoformat(),
                'axiomes_required': agent.axiomes
            }
            
            audit = server.audit_action(agent.agent_id, action)
            assert 'axiomes_checked' in audit


class TestErrorHandling:
    """Integration tests for error handling"""
    
    def test_error_recovery_workflow(self):
        """Test error recovery in workflow"""
        agent = LAIRMAgentSDK(agent_id="recovery-agent", axiomes=['I', 'II'])
        
        @agent.auditable
        def action_with_recovery():
            try:
                raise ValueError("Recoverable error")
            except ValueError:
                agent.log_action('error_recovered', {'error': 'ValueError'})
                return "recovered"
        
        result = action_with_recovery()
        assert result == "recovered"
        
        # Verify recovery was logged
        audit_log = agent.get_audit_log()
        assert any('error_recovered' in entry['action_type'] for entry in audit_log)
    
    def test_compliance_failure_handling(self):
        """Test handling of compliance failures"""
        agent = LAIRMAgentSDK(agent_id="fail-agent", axiomes=['I'])
        
        @agent.compliant(['I', 'II', 'III'])  # Agent doesn't have II, III
        def non_compliant_action():
            return "should_fail"
        
        # Should raise error
        with pytest.raises(ValueError):
            non_compliant_action()


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])



class TestEndToEndWorkflows:
    """End-to-end integration tests"""
    
    def test_complete_lairm_deployment_workflow(self):
        """Test complete LAIRM deployment workflow"""
        # Step 1: Create MCP Server
        server = LAIRMMCPServer(server_id="deployment-server")
        server.start()
        
        # Step 2: Register agent
        reg_result = server.register_agent('deploy-agent', ['I', 'II', 'III', 'VI'])
        assert reg_result['success'] is True
        
        # Step 3: Check compliance
        comp_result = server.check_compliance('deploy-agent', ['I', 'II'])
        assert comp_result['compliant'] is True
        
        # Step 4: Log deployment action
        action_result = server.log_agent_action(
            'deploy-agent',
            'deploy_service',
            {'service': 'auth', 'environment': 'production'}
        )
        assert action_result['success'] is True
        
        # Step 5: Create audit record
        audit_result = server.create_audit_record(
            'deploy-agent',
            'deployment_complete',
            {'status': 'success', 'timestamp': datetime.now().isoformat()}
        )
        assert audit_result['success'] is True
        
        # Step 6: Verify audit log
        log_result = server.get_agent_audit_log('deploy-agent')
        assert log_result['log_size'] >= 2
        
        # Step 7: Get agent status
        status_result = server.get_agent_status('deploy-agent')
        assert status_result['success'] is True
        
        # Step 8: Stop server
        server.stop()
        assert server.is_running is False
    
    def test_multi_agent_distributed_audit_workflow(self):
        """Test multi-agent workflow with distributed audit storage"""
        # Create distributed storage
        nodes = ['node-1', 'node-2', 'node-3']
        hybrid = HybridDistributedStorage(nodes)
        
        # Create multiple agents
        agents = []
        for i in range(5):
            agent = LAIRMAgentSDK(
                agent_id=f'distributed-agent-{i}',
                axiomes=['I', 'II', 'III']
            )
            agents.append(agent)
        
        # Each agent performs actions and stores audit
        for i, agent in enumerate(agents):
            # Perform action
            @agent.auditable
            def distributed_action():
                agent.log_action('distributed_task', {'task_id': i})
                return f"task_{i}_complete"
            
            result = distributed_action()
            assert f"task_{i}_complete" in result
            
            # Store audit in distributed storage
            audit_data = {
                'agent_id': agent.agent_id,
                'audit_log': agent.get_audit_log(),
                'timestamp': datetime.now().isoformat()
            }
            
            storage_result = hybrid.store_audit_log_hybrid(agent.agent_id, audit_data)
            assert storage_result['storage_methods']['ipfs']['status'] == 'success'
            assert storage_result['storage_methods']['blockchain']['status'] == 'success'
            assert storage_result['storage_methods']['distributed']['status'] == 'success'
        
        # Verify storage status
        status = hybrid.get_storage_status()
        assert status['ipfs']['status'] == 'operational'
        assert status['blockchain']['status'] == 'operational'
        assert status['distributed']['total_nodes'] == 3
    
    def test_compliance_audit_verification_chain(self):
        """Test complete compliance, audit, and verification chain"""
        # Create agent with full axiome set
        agent = LAIRMAgentSDK(
            agent_id="chain-agent",
            axiomes=['I', 'II', 'III', 'VI', 'VII', 'VIII']
        )
        
        # Create distributed storage
        hybrid = HybridDistributedStorage(['node-1', 'node-2'])
        
        # Define multi-decorator action
        @agent.compliant(['I', 'II', 'III'])
        @agent.auditable
        @agent.responsible
        @agent.supervised
        def critical_deployment():
            agent.log_action('critical_deploy', {
                'target': 'production',
                'service': 'payment-gateway',
                'risk_level': 'high'
            })
            return "deployment_successful"
        
        # Execute action
        result = critical_deployment()
        assert result == "deployment_successful"
        
        # Verify compliance
        assert agent.check_compliance(['I', 'II', 'III']) is True
        
        # Get audit log
        audit_log = agent.get_audit_log()
        assert len(audit_log) > 0
        
        # Verify all decorator actions were logged
        action_types = [entry['action_type'] for entry in audit_log]
        assert any('compliant' in at for at in action_types)
        assert any('audit_start' in at for at in action_types)
        assert any('responsible' in at for at in action_types)
        assert any('supervised' in at for at in action_types)
        assert any('human_approval' in at for at in action_types)
        
        # Store complete audit trail in distributed storage
        audit_data = {
            'agent_id': agent.agent_id,
            'action': 'critical_deployment',
            'audit_log': audit_log,
            'compliance_status': agent.get_compliance_status(),
            'timestamp': datetime.now().isoformat()
        }
        
        storage_result = hybrid.store_audit_log_hybrid(agent.agent_id, audit_data)
        assert storage_result['storage_methods']['ipfs']['status'] == 'success'
        
        # Verify stored audit
        ipfs_hash = storage_result['storage_methods']['ipfs']['hash']
        verify_result = hybrid.verify_audit_log_hybrid(agent.agent_id, ipfs_hash)
        assert verify_result['overall_valid'] is True


class TestCrossModuleIntegration:
    """Integration tests across all modules"""
    
    def test_agent_mcp_storage_integration(self):
        """Test integration between Agent, MCP Server, and Storage"""
        # Create components
        agent = LAIRMAgentSDK(agent_id="cross-agent", axiomes=['I', 'II', 'III'])
        server = LAIRMMCPServer(server_id="cross-server")
        hybrid = HybridDistributedStorage(['node-1', 'node-2'])
        
        # Start server
        server.start()
        
        # Register agent with server
        reg_result = server.register_agent(agent.agent_id, agent.axiomes)
        assert reg_result['success'] is True
        
        # Agent performs action
        @agent.auditable
        def cross_module_action():
            agent.log_action('cross_action', {'module': 'integration'})
            return "cross_complete"
        
        result = cross_module_action()
        assert result == "cross_complete"
        
        # Log action via MCP server
        server_log_result = server.log_agent_action(
            agent.agent_id,
            'mcp_logged_action',
            {'source': 'mcp_server'}
        )
        assert server_log_result['success'] is True
        
        # Get combined audit log
        audit_log = agent.get_audit_log()
        
        # Store in distributed storage
        audit_data = {
            'agent_id': agent.agent_id,
            'audit_log': audit_log,
            'server_id': server.server_id,
            'timestamp': datetime.now().isoformat()
        }
        
        storage_result = hybrid.store_audit_log_hybrid(agent.agent_id, audit_data)
        assert storage_result['storage_methods']['ipfs']['status'] == 'success'
        
        # Verify via MCP server
        server_audit_result = server.get_agent_audit_log(agent.agent_id)
        assert server_audit_result['success'] is True
        assert server_audit_result['log_size'] > 0
        
        # Stop server
        server.stop()
    
    def test_concurrent_agent_operations(self):
        """Test concurrent operations across multiple agents"""
        # Create MCP server
        server = LAIRMMCPServer(server_id="concurrent-server")
        server.start()
        
        # Register multiple agents
        agent_ids = [f'concurrent-agent-{i}' for i in range(10)]
        for agent_id in agent_ids:
            result = server.register_agent(agent_id, ['I', 'II'])
            assert result['success'] is True
        
        # Each agent logs multiple actions
        for agent_id in agent_ids:
            for j in range(5):
                result = server.log_agent_action(
                    agent_id,
                    f'action_{j}',
                    {'iteration': j}
                )
                assert result['success'] is True
        
        # Verify all agents have logs
        for agent_id in agent_ids:
            log_result = server.get_agent_audit_log(agent_id)
            assert log_result['log_size'] == 5
        
        # List all agents
        list_result = server.list_agents()
        assert list_result['total_agents'] == 10
        
        server.stop()


class TestRealWorldScenarios:
    """Integration tests for real-world scenarios"""
    
    def test_autonomous_vehicle_scenario(self):
        """Test autonomous vehicle compliance scenario"""
        # Create vehicle agent
        vehicle = LAIRMAgentSDK(
            agent_id="autonomous-vehicle-001",
            axiomes=['I', 'II', 'III', 'XI', 'XIII']  # Kill-switch, supervision
        )
        
        # Define critical actions
        @vehicle.compliant(['I', 'II'])
        @vehicle.supervised
        @vehicle.auditable
        def emergency_brake():
            vehicle.log_action('emergency_brake', {
                'speed': 60,
                'obstacle_detected': True,
                'brake_force': 'maximum'
            })
            return "braking_complete"
        
        @vehicle.compliant(['I', 'II', 'III'])
        @vehicle.auditable
        def navigate():
            vehicle.log_action('navigation', {
                'route': 'highway',
                'traffic': 'moderate'
            })
            return "navigating"
        
        # Execute actions
        brake_result = emergency_brake()
        assert brake_result == "braking_complete"
        
        nav_result = navigate()
        assert nav_result == "navigating"
        
        # Verify compliance
        assert vehicle.check_compliance(['I', 'II', 'III']) is True
        
        # Verify audit trail
        audit_log = vehicle.get_audit_log()
        assert len(audit_log) > 0
        assert any('emergency_brake' in entry['action_type'] for entry in audit_log)
        assert any('navigation' in entry['action_type'] for entry in audit_log)
    
    def test_medical_ai_scenario(self):
        """Test medical AI compliance scenario"""
        # Create medical AI agent
        medical_ai = LAIRMAgentSDK(
            agent_id="medical-ai-001",
            axiomes=['I', 'II', 'VIII', 'XII', 'XIV']  # Responsibility, consent
        )
        
        # Define medical actions
        @medical_ai.compliant(['I', 'II', 'VIII'])
        @medical_ai.responsible
        @medical_ai.supervised
        @medical_ai.auditable
        def diagnose_patient():
            medical_ai.log_action('diagnosis', {
                'patient_id': 'P12345',
                'symptoms': ['fever', 'cough'],
                'diagnosis': 'flu',
                'confidence': 0.92
            })
            return "diagnosis_complete"
        
        # Execute diagnosis
        result = diagnose_patient()
        assert result == "diagnosis_complete"
        
        # Verify compliance
        assert medical_ai.check_compliance(['I', 'II', 'VIII']) is True
        
        # Verify audit trail includes responsibility and supervision
        audit_log = medical_ai.get_audit_log()
        action_types = [entry['action_type'] for entry in audit_log]
        assert any('responsible' in at for at in action_types)
        assert any('supervised' in at for at in action_types)
        assert any('human_approval' in at for at in action_types)
    
    def test_financial_system_scenario(self):
        """Test financial system compliance scenario"""
        # Create financial agent
        financial = LAIRMAgentSDK(
            agent_id="financial-agent-001",
            axiomes=['I', 'II', 'VI', 'XIV', 'XIX']  # Audit, transparency
        )
        
        # Create distributed storage for immutable audit
        hybrid = HybridDistributedStorage(['node-1', 'node-2', 'node-3'])
        
        # Define financial actions
        @financial.compliant(['I', 'II', 'VI'])
        @financial.auditable
        @financial.responsible
        def process_transaction():
            financial.log_action('transaction', {
                'transaction_id': 'TXN-001',
                'amount': 10000,
                'currency': 'USD',
                'type': 'transfer',
                'fraud_score': 0.05
            })
            return "transaction_processed"
        
        # Execute transaction
        result = process_transaction()
        assert result == "transaction_processed"
        
        # Store audit in distributed storage
        audit_data = {
            'agent_id': financial.agent_id,
            'audit_log': financial.get_audit_log(),
            'compliance_status': financial.get_compliance_status(),
            'timestamp': datetime.now().isoformat()
        }
        
        storage_result = hybrid.store_audit_log_hybrid(financial.agent_id, audit_data)
        assert storage_result['storage_methods']['blockchain']['status'] == 'success'
        
        # Verify immutable audit trail
        ipfs_hash = storage_result['storage_methods']['ipfs']['hash']
        verify_result = hybrid.verify_audit_log_hybrid(financial.agent_id, ipfs_hash)
        assert verify_result['overall_valid'] is True


class TestScalabilityIntegration:
    """Integration tests for scalability"""
    
    def test_large_scale_agent_deployment(self):
        """Test large-scale agent deployment"""
        server = LAIRMMCPServer(server_id="scale-server")
        server.start()
        
        # Register 100 agents
        for i in range(100):
            result = server.register_agent(f'scale-agent-{i:03d}', ['I', 'II'])
            assert result['success'] is True
        
        # Each agent logs actions
        for i in range(100):
            for j in range(10):
                server.log_agent_action(
                    f'scale-agent-{i:03d}',
                    f'action_{j}',
                    {'index': j}
                )
        
        # Verify all agents
        list_result = server.list_agents()
        assert list_result['total_agents'] == 100
        
        # Verify random agent has correct log size
        log_result = server.get_agent_audit_log('scale-agent-050')
        assert log_result['log_size'] == 10
        
        server.stop()
    
    def test_high_throughput_audit_storage(self):
        """Test high throughput audit storage"""
        hybrid = HybridDistributedStorage(['node-1', 'node-2', 'node-3'])
        
        # Store 50 audit logs rapidly
        for i in range(50):
            audit_data = {
                'agent_id': f'throughput-agent-{i}',
                'action': 'high_throughput_test',
                'timestamp': datetime.now().isoformat(),
                'index': i
            }
            
            result = hybrid.store_audit_log_hybrid(f'throughput-agent-{i}', audit_data)
            assert result['storage_methods']['ipfs']['status'] == 'success'
        
        # Verify storage status
        status = hybrid.get_storage_status()
        assert status['ipfs']['status'] == 'operational'
        assert status['distributed']['total_nodes'] == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
