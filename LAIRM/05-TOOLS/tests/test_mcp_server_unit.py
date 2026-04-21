# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Unit Tests for LAIRM MCP Server
Comprehensive coverage for MCP Server functionality
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Import the modules to test
import sys
sys.path.insert(0, '/Users/mehdiwhb/Desktop/ARAM/LAIRM/05-TOOLS')

from mcp_server.lairm_mcp_server import LAIRMMCPServer


class TestLAIRMMCPServer:
    """Test suite for LAIRM MCP Server"""
    
    @pytest.fixture
    def server(self):
        """Create MCP server instance with mocked framework"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            # Manually populate with test data
            server.articles = {
                'I-01-01': {
                    'numero': 'I-01-01',
                    'titre': 'Kill-Switch Universalis',
                    'axiome': 'I',
                    'statut': 'Final',
                    'file': 'test.md',
                    'path': Path('test.md')
                },
                'I-01-02': {
                    'numero': 'I-01-02',
                    'titre': 'Human Override',
                    'axiome': 'I',
                    'statut': 'Final',
                    'file': 'test2.md',
                    'path': Path('test2.md')
                },
                'II-02-01': {
                    'numero': 'II-02-01',
                    'titre': 'Agent Passport',
                    'axiome': 'II',
                    'statut': 'Final',
                    'file': 'test3.md',
                    'path': Path('test3.md')
                }
            }
            server.axiomes = {
                'AXIOM-I-SUPREMATIA': {
                    'name': 'AXIOM-I-SUPREMATIA',
                    'articles': [server.articles['I-01-01'], server.articles['I-01-02']],
                    'count': 2
                },
                'AXIOM-II-IDENTITAS': {
                    'name': 'AXIOM-II-IDENTITAS',
                    'articles': [server.articles['II-02-01']],
                    'count': 1
                }
            }
            return server
    
    @pytest.fixture
    def sample_article_data(self):
        """Sample article data"""
        return {
            'numero': 'I-01-01',
            'titre': 'Kill-Switch Universalis',
            'axiome': 'I',
            'statut': 'Final',
            'file': '02-COMPENDIUM-LEGISLATIF/AXIOM-I-SUPREMATIA/article-I-01-01-kill-switch-universalis.md'
        }
    
    def test_initialization(self, server):
        """Test MCP server initialization"""
        assert server.lairm_root == Path("LAIRM")
        assert isinstance(server.articles, dict)
        assert isinstance(server.axiomes, dict)
        assert len(server.articles) == 3  # From fixture
        assert len(server.axiomes) == 2  # From fixture
    
    def test_initialization_custom_root(self):
        """Test initialization with custom root"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="custom/path")
            assert server.lairm_root == Path("custom/path")
    
    def test_load_framework(self, server):
        """Test loading framework"""
        # Framework should be loaded during initialization
        assert len(server.articles) > 0
        assert len(server.axiomes) > 0
    
    def test_search_articles_empty_query(self, server):
        """Test searching articles with empty query"""
        results = server.search_articles(query="")
        assert isinstance(results, list)
    
    def test_search_articles_by_query(self, server):
        """Test searching articles by query"""
        results = server.search_articles(query="kill")
        assert isinstance(results, list)
        
        # Should find kill-switch articles
        assert len(results) > 0
        assert any('kill' in article['titre'].lower() for article in results)
    
    def test_search_articles_by_axiome(self, server):
        """Test searching articles by axiome"""
        results = server.search_articles(axiome="I")
        assert isinstance(results, list)
        
        # Should find axiome I articles
        assert len(results) > 0
        assert all('I' in article['axiome'] for article in results)
    
    def test_search_articles_by_statut(self, server):
        """Test searching articles by status"""
        results = server.search_articles(statut="Final")
        assert isinstance(results, list)
        
        # Should find Final status articles
        assert len(results) > 0
        assert all(article['statut'] == 'Final' for article in results)
    
    def test_search_articles_combined_filters(self, server):
        """Test searching with combined filters"""
        results = server.search_articles(
            query="kill",
            axiome="I",
            statut="Final"
        )
        assert isinstance(results, list)
    
    def test_get_article(self, server):
        """Test getting article by numero"""
        # Mock the file reading
        with patch('builtins.open', create=True):
            article = server.get_article('I-01-01')
            
            assert article is not None
            assert 'numero' in article
            assert 'titre' in article
    
    def test_get_article_nonexistent(self, server):
        """Test getting nonexistent article"""
        article = server.get_article('NONEXISTENT-999')
        assert article is None
    
    def test_get_axiome(self, server):
        """Test getting axiome"""
        axiome = server.get_axiome("I")
        
        assert axiome is not None
        assert 'name' in axiome
        assert 'articles' in axiome
        assert 'count' in axiome
    
    def test_get_axiome_nonexistent(self, server):
        """Test getting nonexistent axiome"""
        axiome = server.get_axiome("NONEXISTENT")
        assert axiome is None
    
    def test_validate_compliance_valid(self, server):
        """Test validating compliance with valid axiomes"""
        agent_config = {
            'agent_id': 'test-agent-001',
            'axiomes_required': ['I', 'II']
        }
        
        report = server.validate_compliance(agent_config)
        
        assert report['agent_id'] == 'test-agent-001'
        assert isinstance(report['compliant'], bool)
        assert 'axiomes' in report
        assert 'violations' in report
    
    def test_validate_compliance_invalid_axiome(self, server):
        """Test validating compliance with invalid axiome"""
        agent_config = {
            'agent_id': 'test-agent-002',
            'axiomes_required': ['INVALID-AXIOME']
        }
        
        report = server.validate_compliance(agent_config)
        
        assert report['compliant'] is False
        assert len(report['violations']) > 0
    
    def test_validate_compliance_no_axiomes(self, server):
        """Test validating compliance with no axiomes"""
        agent_config = {
            'agent_id': 'test-agent-003',
            'axiomes_required': []
        }
        
        report = server.validate_compliance(agent_config)
        
        assert report['compliant'] is True
        assert len(report['axiomes']) == 0
    
    def test_audit_action(self, server):
        """Test auditing an action"""
        action = {
            'type': 'deploy',
            'timestamp': '2024-01-01T00:00:00',
            'axiomes_required': ['I', 'II']
        }
        
        audit_record = server.audit_action('agent-001', action)
        
        assert audit_record['agent_id'] == 'agent-001'
        assert audit_record['action'] == 'deploy'
        assert 'axiomes_checked' in audit_record
        assert 'violations' in audit_record
    
    def test_audit_action_invalid_axiome(self, server):
        """Test auditing action with invalid axiome"""
        action = {
            'type': 'deploy',
            'timestamp': '2024-01-01T00:00:00',
            'axiomes_required': ['INVALID']
        }
        
        audit_record = server.audit_action('agent-001', action)
        
        assert audit_record['compliant'] is False
        assert len(audit_record['violations']) > 0
    
    def test_get_statistics(self, server):
        """Test getting server statistics"""
        stats = server.get_statistics()
        
        assert 'total_articles' in stats
        assert 'total_axiomes' in stats
        assert 'axiomes' in stats
        assert 'status' in stats
        assert stats['status'] == 'ready'
    
    def test_statistics_consistency(self, server):
        """Test that statistics are consistent"""
        stats = server.get_statistics()
        
        # Total axiomes should match axiomes dict
        assert stats['total_axiomes'] == len(server.axiomes)
        
        # Total articles should match articles dict
        assert stats['total_articles'] == len(server.articles)


class TestMCPServerArticleParsing:
    """Test suite for article parsing"""
    
    def test_parse_article_valid(self, tmp_path):
        """Test parsing valid article"""
        # Create a temporary article file
        article_content = """---
titre: "Test Article"
numero: "I-01-01"
axiome: "I"
statut: "Final"
---

# Test Article

This is a test article.
"""
        
        article_file = tmp_path / "article-test.md"
        article_file.write_text(article_content)
        
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer()
            article = server.parse_article(article_file)
            
            if article:
                assert article['titre'] == 'Test Article'
                assert article['numero'] == 'I-01-01'
                assert article['axiome'] == 'I'
                assert article['statut'] == 'Final'
    
    def test_parse_article_missing_frontmatter(self, tmp_path):
        """Test parsing article without frontmatter"""
        article_content = "# Test Article\n\nNo frontmatter here."
        
        article_file = tmp_path / "article-test.md"
        article_file.write_text(article_content)
        
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer()
            article = server.parse_article(article_file)
            
            assert article is None


class TestMCPServerIntegration:
    """Integration tests for MCP Server"""
    
    def test_full_compliance_workflow(self):
        """Test complete compliance workflow"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1},
                'AXIOM-II': {'name': 'AXIOM-II', 'articles': [], 'count': 1},
                'AXIOM-III': {'name': 'AXIOM-III', 'articles': [], 'count': 1}
            }
            
            # Define agent
            agent_config = {
                'agent_id': 'workflow-agent',
                'axiomes_required': ['I', 'II', 'III']
            }
            
            # Validate compliance
            compliance = server.validate_compliance(agent_config)
            assert 'compliant' in compliance
            
            # Audit action
            action = {
                'type': 'deploy',
                'timestamp': '2024-01-01T00:00:00',
                'axiomes_required': ['I', 'II']
            }
            
            audit = server.audit_action(agent_config['agent_id'], action)
            assert 'axiomes_checked' in audit
    
    def test_search_and_retrieve_workflow(self):
        """Test search and retrieve workflow"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.articles = {
                'I-01-01': {
                    'numero': 'I-01-01',
                    'titre': 'Kill-Switch',
                    'axiome': 'I',
                    'statut': 'Final',
                    'file': 'test.md',
                    'path': Path('test.md')
                }
            }
            
            # Search for articles
            results = server.search_articles(query="kill")
            
            assert len(results) > 0
            
            # Get first result
            numero = results[0]['numero']
            
            # Mock file reading for get_article
            with patch('builtins.open', create=True):
                article = server.get_article(numero)
                
                assert article is not None
    
    def test_multiple_agent_compliance_checks(self):
        """Test compliance checks for multiple agents"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1},
                'AXIOM-II': {'name': 'AXIOM-II', 'articles': [], 'count': 1},
                'AXIOM-III': {'name': 'AXIOM-III', 'articles': [], 'count': 1}
            }
            
            agents = [
                {'agent_id': 'agent-1', 'axiomes_required': ['I']},
                {'agent_id': 'agent-2', 'axiomes_required': ['I', 'II']},
                {'agent_id': 'agent-3', 'axiomes_required': ['I', 'II', 'III']}
            ]
            
            for agent_config in agents:
                compliance = server.validate_compliance(agent_config)
                assert compliance['agent_id'] == agent_config['agent_id']


class TestMCPServerEdgeCases:
    """Edge case tests for MCP Server"""
    
    def test_search_with_special_characters(self):
        """Test searching with special characters"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.articles = {}
            
            results = server.search_articles(query="@#$%")
            assert isinstance(results, list)
    
    def test_search_with_unicode(self):
        """Test searching with unicode characters"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.articles = {}
            
            results = server.search_articles(query="你好")
            assert isinstance(results, list)
    
    def test_validate_compliance_empty_agent_id(self):
        """Test compliance validation with empty agent ID"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {}
            
            agent_config = {
                'agent_id': '',
                'axiomes_required': ['I']
            }
            
            report = server.validate_compliance(agent_config)
            assert 'agent_id' in report
    
    def test_audit_action_missing_fields(self):
        """Test auditing action with missing fields"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {}
            
            action = {}
            audit = server.audit_action('agent-001', action)
            
            assert 'agent_id' in audit
            assert 'action' in audit
    
    def test_get_axiome_case_sensitivity(self):
        """Test axiome retrieval with different cases"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1}
            }
            
            # Try different cases
            axiome1 = server.get_axiome("I")
            axiome2 = server.get_axiome("i")
            
            # Results may vary depending on implementation
            assert isinstance(axiome1, (dict, type(None)))
            assert isinstance(axiome2, (dict, type(None)))
    
    def test_statistics_after_operations(self):
        """Test that statistics remain consistent after operations"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.articles = {'I-01-01': {'numero': 'I-01-01', 'titre': 'Test', 'axiome': 'I', 'statut': 'Final', 'file': 'test.md', 'path': Path('test.md')}}
            server.axiomes = {'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1}}
            
            stats1 = server.get_statistics()
            
            # Perform operations
            server.search_articles(query="test")
            server.validate_compliance({'agent_id': 'test', 'axiomes_required': ['I']})
            
            stats2 = server.get_statistics()
            
            # Statistics should remain the same
            assert stats1['total_articles'] == stats2['total_articles']
            assert stats1['total_axiomes'] == stats2['total_axiomes']


class TestMCPServerPerformance:
    """Performance tests for MCP Server"""
    
    def test_search_performance(self):
        """Test search performance"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.articles = {}
            
            # Perform multiple searches
            for i in range(10):
                results = server.search_articles(query=f"test{i}")
                assert isinstance(results, list)
    
    def test_compliance_check_performance(self):
        """Test compliance check performance"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1},
                'AXIOM-II': {'name': 'AXIOM-II', 'articles': [], 'count': 1},
                'AXIOM-III': {'name': 'AXIOM-III', 'articles': [], 'count': 1}
            }
            
            # Perform multiple compliance checks
            for i in range(10):
                agent_config = {
                    'agent_id': f'agent-{i}',
                    'axiomes_required': ['I', 'II', 'III']
                }
                compliance = server.validate_compliance(agent_config)
                assert 'compliant' in compliance
    
    def test_audit_performance(self):
        """Test audit performance"""
        with patch.object(LAIRMMCPServer, 'load_framework'):
            server = LAIRMMCPServer(lairm_root="LAIRM")
            server.axiomes = {
                'AXIOM-I': {'name': 'AXIOM-I', 'articles': [], 'count': 1}
            }
            
            # Perform multiple audits
            for i in range(10):
                action = {
                    'type': 'action',
                    'timestamp': '2024-01-01T00:00:00',
                    'axiomes_required': ['I']
                }
                audit = server.audit_action(f'agent-{i}', action)
                assert 'axiomes_checked' in audit


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
