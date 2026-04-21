# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Unit Tests for LAIRM Agent Framework
Comprehensive coverage for Agent SDK, decorators, and compliance checking
"""

import pytest
import json
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock

# Import the modules to test
import sys
sys.path.insert(0, '/Users/mehdiwhb/Desktop/ARAM/LAIRM/05-TOOLS')

from agent_framework.lairm_agent_sdk import (
    LAIRMAgentSDK,
    compliant,
    auditable,
    responsible,
    supervised
)


class TestLAIRMAgentSDK:
    """Test suite for LAIRM Agent SDK"""
    
    @pytest.fixture
    def agent(self):
        """Create a test agent"""
        return LAIRMAgentSDK(
            agent_id="test-agent-001",
            axiomes=['I', 'II', 'III', 'VI']
        )
    
    @pytest.fixture
    def agent_no_axiomes(self):
        """Create agent without axiomes"""
        return LAIRMAgentSDK(agent_id="test-agent-002")
    
    def test_initialization(self, agent):
        """Test agent initialization"""
        assert agent.agent_id == "test-agent-001"
        assert agent.axiomes == ['I', 'II', 'III', 'VI']
        assert agent.audit_log == []
        assert agent.compliance_checks == []
    
    def test_initialization_default_agent_id(self):
        """Test initialization with default agent ID"""
        agent = LAIRMAgentSDK()
        assert agent.agent_id is not None
        assert len(agent.agent_id) > 0
    
    def test_initialization_default_axiomes(self):
        """Test initialization with default axiomes"""
        agent = LAIRMAgentSDK()
        assert agent.axiomes == []
    
    def test_log_action(self, agent):
        """Test logging an action"""
        record = agent.log_action('test_action', {'param': 'value'})
        
        assert record is not None
        assert record['agent_id'] == 'test-agent-001'
        assert record['action_type'] == 'test_action'
        assert record['details'] == {'param': 'value'}
        assert 'timestamp' in record
        assert len(agent.audit_log) == 1
    
    def test_log_action_without_details(self, agent):
        """Test logging action without details"""
        record = agent.log_action('simple_action')
        
        assert record['details'] == {}
        assert len(agent.audit_log) == 1
    
    def test_log_multiple_actions(self, agent):
        """Test logging multiple actions"""
        agent.log_action('action1', {'data': 1})
        agent.log_action('action2', {'data': 2})
        agent.log_action('action3', {'data': 3})
        
        assert len(agent.audit_log) == 3
        assert agent.audit_log[0]['action_type'] == 'action1'
        assert agent.audit_log[1]['action_type'] == 'action2'
        assert agent.audit_log[2]['action_type'] == 'action3'
    
    def test_check_compliance_valid(self, agent):
        """Test compliance check with valid axiomes"""
        is_compliant = agent.check_compliance(['I', 'II'])
        assert is_compliant is True
    
    def test_check_compliance_partial(self, agent):
        """Test compliance check with partial axiomes"""
        is_compliant = agent.check_compliance(['I', 'II', 'III'])
        assert is_compliant is True
    
    def test_check_compliance_invalid(self, agent):
        """Test compliance check with invalid axiomes"""
        is_compliant = agent.check_compliance(['I', 'II', 'X'])
        assert is_compliant is False
    
    def test_check_compliance_empty_agent(self, agent_no_axiomes):
        """Test compliance check on agent without axiomes"""
        is_compliant = agent_no_axiomes.check_compliance(['I'])
        assert is_compliant is False
    
    def test_compliant_decorator_success(self, agent):
        """Test compliant decorator with valid axiomes"""
        @agent.compliant(['I', 'II'])
        def test_func():
            return "success"
        
        result = test_func()
        assert result == "success"
        assert len(agent.audit_log) > 0
    
    def test_compliant_decorator_failure(self, agent):
        """Test compliant decorator with invalid axiomes"""
        @agent.compliant(['I', 'II', 'X'])
        def test_func():
            return "success"
        
        with pytest.raises(ValueError):
            test_func()
    
    def test_compliant_decorator_logs_action(self, agent):
        """Test that compliant decorator logs action"""
        @agent.compliant(['I', 'II'])
        def test_func():
            return "result"
        
        test_func()
        
        # Should have logged the compliant action
        assert any('compliant_test_func' in entry['action_type'] for entry in agent.audit_log)
    
    def test_auditable_decorator_success(self, agent):
        """Test auditable decorator on successful function"""
        @agent.auditable
        def test_func():
            return "success"
        
        result = test_func()
        assert result == "success"
        assert len(agent.audit_log) >= 2  # start and success
    
    def test_auditable_decorator_failure(self, agent):
        """Test auditable decorator on failing function"""
        @agent.auditable
        def test_func():
            raise ValueError("Test error")
        
        with pytest.raises(ValueError):
            test_func()
        
        # Should have logged the error
        assert any('audit_error' in entry['action_type'] for entry in agent.audit_log)
    
    def test_auditable_decorator_logs_start_and_success(self, agent):
        """Test that auditable decorator logs start and success"""
        @agent.auditable
        def test_func():
            return "result"
        
        test_func()
        
        action_types = [entry['action_type'] for entry in agent.audit_log]
        assert any('audit_start' in at for at in action_types)
        assert any('audit_success' in at for at in action_types)
    
    def test_responsible_decorator(self, agent):
        """Test responsible decorator"""
        @agent.responsible
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
        assert any('responsible_test_func' in entry['action_type'] for entry in agent.audit_log)
    
    def test_supervised_decorator(self, agent):
        """Test supervised decorator"""
        @agent.supervised
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
        
        # Should have logged supervision and approval
        action_types = [entry['action_type'] for entry in agent.audit_log]
        assert any('supervised_test_func' in at for at in action_types)
        assert any('human_approval' in at for at in action_types)
    
    def test_supervised_decorator_approval_record(self, agent):
        """Test that supervised decorator creates approval record"""
        @agent.supervised
        def test_func():
            return "result"
        
        test_func()
        
        # Find approval record
        approval_entries = [e for e in agent.audit_log if 'human_approval' in e['action_type']]
        assert len(approval_entries) > 0
        
        approval = approval_entries[0]['details']
        assert approval['required'] is True
        assert approval['obtained'] is True
        assert approval['approver_id'] == 'human-supervisor'
    
    def test_get_audit_log(self, agent):
        """Test getting audit log"""
        agent.log_action('action1')
        agent.log_action('action2')
        
        log = agent.get_audit_log()
        assert len(log) == 2
        assert log[0]['action_type'] == 'action1'
        assert log[1]['action_type'] == 'action2'
    
    def test_get_compliance_status(self, agent):
        """Test getting compliance status"""
        agent.log_action('action1')
        
        status = agent.get_compliance_status()
        
        assert status['agent_id'] == 'test-agent-001'
        assert status['axiomes'] == ['I', 'II', 'III', 'VI']
        assert status['audit_log_size'] == 1
        assert status['compliant'] is True
    
    def test_get_compliance_status_no_axiomes(self, agent_no_axiomes):
        """Test compliance status for agent without axiomes"""
        status = agent_no_axiomes.get_compliance_status()
        
        assert status['axiomes'] == []
        assert status['compliant'] is False
    
    def test_decorator_stacking(self, agent):
        """Test stacking multiple decorators"""
        @agent.compliant(['I', 'II'])
        @agent.auditable
        @agent.responsible
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
        assert len(agent.audit_log) > 0
    
    def test_decorator_preserves_function_name(self, agent):
        """Test that decorators preserve function name"""
        @agent.auditable
        def my_function():
            return "result"
        
        assert my_function.__name__ == 'my_function'
    
    def test_decorator_preserves_function_docstring(self, agent):
        """Test that decorators preserve function docstring"""
        @agent.auditable
        def my_function():
            """This is my function"""
            return "result"
        
        assert my_function.__doc__ == "This is my function"


class TestGlobalDecorators:
    """Test suite for global decorators"""
    
    def test_global_compliant_decorator(self):
        """Test global compliant decorator"""
        @compliant(['I', 'II'])
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
    
    def test_global_compliant_decorator_invalid_axiome(self):
        """Test global compliant decorator with invalid axiome"""
        @compliant(['I', 'II', None])
        def test_func():
            return "result"
        
        with pytest.raises(ValueError):
            test_func()
    
    def test_global_auditable_decorator(self):
        """Test global auditable decorator"""
        @auditable
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
    
    def test_global_auditable_decorator_error(self):
        """Test global auditable decorator with error"""
        @auditable
        def test_func():
            raise ValueError("Test error")
        
        with pytest.raises(ValueError):
            test_func()
    
    def test_global_responsible_decorator(self):
        """Test global responsible decorator"""
        @responsible
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"
    
    def test_global_supervised_decorator(self):
        """Test global supervised decorator"""
        @supervised
        def test_func():
            return "result"
        
        result = test_func()
        assert result == "result"


class TestAgentFrameworkIntegration:
    """Integration tests for Agent Framework"""
    
    def test_full_agent_workflow(self):
        """Test complete agent workflow"""
        agent = LAIRMAgentSDK(
            agent_id="workflow-agent",
            axiomes=['I', 'II', 'III', 'VI']
        )
        
        # Define compliant action
        @agent.compliant(['I', 'II'])
        @agent.auditable
        def deploy_agent():
            return "deployed"
        
        # Execute
        result = deploy_agent()
        assert result == "deployed"
        
        # Verify audit trail
        assert len(agent.audit_log) > 0
        assert agent.check_compliance(['I', 'II'])
    
    def test_multiple_agents_independent_logs(self):
        """Test that multiple agents have independent audit logs"""
        agent1 = LAIRMAgentSDK(agent_id="agent-1", axiomes=['I', 'II'])
        agent2 = LAIRMAgentSDK(agent_id="agent-2", axiomes=['III', 'VI'])
        
        agent1.log_action('action1')
        agent2.log_action('action2')
        
        assert len(agent1.audit_log) == 1
        assert len(agent2.audit_log) == 1
        assert agent1.audit_log[0]['agent_id'] == 'agent-1'
        assert agent2.audit_log[0]['agent_id'] == 'agent-2'
    
    def test_agent_compliance_matrix(self):
        """Test compliance matrix for multiple axiomes"""
        agent = LAIRMAgentSDK(
            agent_id="matrix-agent",
            axiomes=['I', 'II', 'III', 'VI', 'VII', 'VIII']
        )
        
        # Test various compliance checks
        assert agent.check_compliance(['I']) is True
        assert agent.check_compliance(['I', 'II']) is True
        assert agent.check_compliance(['I', 'II', 'III', 'VI', 'VII', 'VIII']) is True
        assert agent.check_compliance(['I', 'II', 'III', 'VI', 'VII', 'VIII', 'X']) is False
    
    def test_audit_trail_completeness(self):
        """Test that audit trail captures all actions"""
        agent = LAIRMAgentSDK(agent_id="audit-agent", axiomes=['I', 'II'])
        
        @agent.auditable
        @agent.responsible
        def complex_action():
            agent.log_action('internal_action')
            return "done"
        
        complex_action()
        
        # Should have multiple entries
        assert len(agent.audit_log) >= 3
        
        # Verify action types
        action_types = [e['action_type'] for e in agent.audit_log]
        assert any('audit_start' in at for at in action_types)
        assert any('responsible' in at for at in action_types)
        assert any('internal_action' in at for at in action_types)
        assert any('audit_success' in at for at in action_types)


class TestAgentFrameworkEdgeCases:
    """Edge case tests for Agent Framework"""
    
    def test_agent_with_many_axiomes(self):
        """Test agent with many axiomes"""
        axiomes = [str(i) for i in range(100)]
        agent = LAIRMAgentSDK(agent_id="many-axiomes", axiomes=axiomes)
        
        assert len(agent.axiomes) == 100
        assert agent.check_compliance(axiomes) is True
    
    def test_agent_with_special_characters_in_id(self):
        """Test agent with special characters in ID"""
        agent = LAIRMAgentSDK(agent_id="agent@#$%^&*()")
        assert agent.agent_id == "agent@#$%^&*()"
    
    def test_action_with_large_details(self):
        """Test logging action with large details"""
        agent = LAIRMAgentSDK(agent_id="large-agent")
        
        large_details = {'data': 'x' * 10000}
        record = agent.log_action('large_action', large_details)
        
        assert record['details'] == large_details
    
    def test_action_with_nested_details(self):
        """Test logging action with nested details"""
        agent = LAIRMAgentSDK(agent_id="nested-agent")
        
        nested_details = {
            'level1': {
                'level2': {
                    'level3': {
                        'data': 'value'
                    }
                }
            }
        }
        record = agent.log_action('nested_action', nested_details)
        
        assert record['details'] == nested_details
    
    def test_decorator_with_args_and_kwargs(self):
        """Test decorator with function arguments"""
        agent = LAIRMAgentSDK(agent_id="args-agent", axiomes=['I'])
        
        @agent.auditable
        def func_with_args(a, b, c=None):
            return a + b + (c or 0)
        
        result = func_with_args(1, 2, c=3)
        assert result == 6
    
    def test_compliance_check_empty_list(self):
        """Test compliance check with empty axiomes list"""
        agent = LAIRMAgentSDK(agent_id="empty-agent", axiomes=['I', 'II'])
        
        is_compliant = agent.check_compliance([])
        assert is_compliant is True
    
    def test_audit_log_timestamp_ordering(self):
        """Test that audit log maintains timestamp ordering"""
        agent = LAIRMAgentSDK(agent_id="timestamp-agent")
        
        for i in range(5):
            agent.log_action(f'action_{i}')
        
        # Verify timestamps are in order
        for i in range(len(agent.audit_log) - 1):
            ts1 = agent.audit_log[i]['timestamp']
            ts2 = agent.audit_log[i + 1]['timestamp']
            assert ts1 <= ts2


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
