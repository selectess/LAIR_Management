# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
LAIRM MCP Server
Model Context Protocol server for LAIRM compliance checking and audit
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import re
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compliance_checker.lairm_compliance_checker import LAIRMComplianceChecker
from audit_engine.lairm_audit_engine import LAIRMAuditEngine
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK


class LAIRMMCPServer:
    """
    MCP Server for LAIRM Framework
    Provides compliance checking, audit logging, and agent management via MCP protocol
    """
    
    def __init__(self, server_id: str = "lairm-mcp-server", port: int = 8080, lairm_root: str = None):
        """
        Initialize LAIRM MCP Server
        
        Args:
            server_id: Unique identifier for this server instance
            port: Port number for the server
            lairm_root: Root directory of LAIRM framework (optional)
        """
        self.server_id = server_id
        self.port = port
        self.lairm_root = Path(lairm_root) if lairm_root else None
        self.compliance_checker = LAIRMComplianceChecker()
        self.audit_engine = LAIRMAuditEngine()
        self.agents: Dict[str, LAIRMAgentSDK] = {}
        self.is_running = False
        
        # Framework data
        self.articles: Dict[str, Dict[str, Any]] = {}
        self.axiomes: Dict[str, Dict[str, Any]] = {}
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Load framework if root provided
        if lairm_root:
            self.load_framework()
        
        self.logger.info(f"LAIRM MCP Server initialized: {server_id} on port {port}")
    
    def load_framework(self) -> None:
        """
        Load LAIRM framework articles from filesystem
        """
        if not self.lairm_root:
            self.logger.warning("No LAIRM root specified, skipping framework load")
            return
        
        # Look for legislative compendium
        legislative_path = self.lairm_root / "02-COMPENDIUM-LEGISLATIVE"
        
        if not legislative_path.exists():
            self.logger.warning(f"Legislative path not found: {legislative_path}")
            return
        
        # Load all axiom directories
        for axiom_dir in legislative_path.iterdir():
            if axiom_dir.is_dir() and axiom_dir.name.startswith("AXIOM-"):
                axiom_name = axiom_dir.name
                axiom_articles = []
                
                # Load all articles in this axiom
                for article_file in axiom_dir.glob("article-*.md"):
                    article = self.parse_article(article_file)
                    if article:
                        self.articles[article['numero']] = article
                        axiom_articles.append(article)
                
                # Store axiom info
                if axiom_articles:
                    self.axiomes[axiom_name] = {
                        'name': axiom_name,
                        'articles': axiom_articles,
                        'count': len(axiom_articles)
                    }
        
        self.logger.info(f"Loaded {len(self.articles)} articles across {len(self.axiomes)} axiomes")
    
    def parse_article(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Parse an article markdown file
        
        Args:
            file_path: Path to the article file
        
        Returns:
            dict: Parsed article data or None if parsing fails
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Extract frontmatter
            frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            
            if not frontmatter_match:
                return None
            
            frontmatter = frontmatter_match.group(1)
            
            # Parse frontmatter fields
            article = {
                'file': file_path.name,
                'path': file_path
            }
            
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    article[key] = value
            
            return article
            
        except Exception as e:
            self.logger.error(f"Error parsing article {file_path}: {e}")
            return None
    
    def search_articles(self, query: str = "", axiome: str = None, statut: str = None) -> List[Dict[str, Any]]:
        """
        Search articles by query, axiome, or status
        
        Args:
            query: Search query string
            axiome: Filter by axiome (e.g., 'I', 'II')
            statut: Filter by status (e.g., 'Final', 'Draft')
        
        Returns:
            list: List of matching articles
        """
        results = []
        
        for article in self.articles.values():
            # Apply filters
            if axiome and article.get('axiome') != axiome:
                continue
            
            if statut and article.get('statut') != statut:
                continue
            
            if query:
                # Search in title and numero
                query_lower = query.lower()
                titre = article.get('titre', '').lower()
                numero = article.get('numero', '').lower()
                
                if query_lower not in titre and query_lower not in numero:
                    continue
            
            results.append(article)
        
        return results
    
    def get_article(self, numero: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific article by numero
        
        Args:
            numero: Article numero (e.g., 'I-01-01')
        
        Returns:
            dict: Article data or None if not found
        """
        article = self.articles.get(numero)
        
        if not article:
            return None
        
        # Return a copy with full content if available
        result = article.copy()
        
        # Try to read full content
        if 'path' in article:
            try:
                result['content'] = article['path'].read_text(encoding='utf-8')
            except Exception as e:
                self.logger.error(f"Error reading article content: {e}")
        
        return result
    
    def get_axiome(self, axiome_id: str) -> Optional[Dict[str, Any]]:
        """
        Get axiome information
        
        Args:
            axiome_id: Axiome identifier (e.g., 'I', 'II', 'VI')
        
        Returns:
            dict: Axiome data or None if not found
        """
        # Try exact match first
        for axiome_name, axiome_data in self.axiomes.items():
            if axiome_name == f"AXIOM-{axiome_id}-" or axiome_name.startswith(f"AXIOM-{axiome_id}-"):
                return axiome_data
        
        # Try case-insensitive match
        axiome_id_upper = axiome_id.upper()
        for axiome_name, axiome_data in self.axiomes.items():
            if axiome_id_upper in axiome_name.upper():
                return axiome_data
        
        return None
    
    def validate_compliance(self, agent_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate agent compliance with required axiomes
        
        Args:
            agent_config: Agent configuration with agent_id and axiomes_required
        
        Returns:
            dict: Compliance validation report
        """
        agent_id = agent_config.get('agent_id', 'unknown')
        axiomes_required = agent_config.get('axiomes_required', [])
        
        report = {
            'agent_id': agent_id,
            'axiomes': [],
            'violations': [],
            'compliant': True
        }
        
        # Check each required axiome
        for axiome_id in axiomes_required:
            axiome = self.get_axiome(axiome_id)
            
            if not axiome:
                report['violations'].append({
                    'axiome': axiome_id,
                    'error': 'Axiome not found'
                })
                report['compliant'] = False
            else:
                report['axiomes'].append({
                    'axiome': axiome_id,
                    'name': axiome['name'],
                    'articles_count': axiome['count']
                })
        
        return report
    
    def audit_action(self, agent_id: str, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Audit an agent action
        
        Args:
            agent_id: Agent identifier
            action: Action data with type, timestamp, axiomes_required
        
        Returns:
            dict: Audit record
        """
        action_type = action.get('type', 'unknown')
        axiomes_required = action.get('axiomes_required', [])
        
        audit_record = {
            'agent_id': agent_id,
            'action': action_type,
            'timestamp': action.get('timestamp', datetime.now().isoformat()),
            'axiomes_checked': [],
            'violations': [],
            'compliant': True
        }
        
        # Check each required axiome
        for axiome_id in axiomes_required:
            axiome = self.get_axiome(axiome_id)
            
            if not axiome:
                audit_record['violations'].append({
                    'axiome': axiome_id,
                    'error': 'Axiome not found'
                })
                audit_record['compliant'] = False
            else:
                audit_record['axiomes_checked'].append(axiome_id)
        
        # Log to audit engine
        try:
            self.audit_engine.audit_agent_action(
                agent_id=agent_id,
                action=action
            )
        except Exception as e:
            self.logger.error(f"Error logging to audit engine: {e}")
        
        return audit_record
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get server statistics
        
        Returns:
            dict: Server statistics
        """
        return {
            'status': 'ready',
            'total_articles': len(self.articles),
            'total_axiomes': len(self.axiomes),
            'axiomes': {
                name: data['count']
                for name, data in self.axiomes.items()
            }
        }
    
    def start(self) -> bool:
        """
        Start the MCP server
        
        Returns:
            bool: True if server started successfully
        """
        if self.is_running:
            self.logger.warning("Server is already running")
            return False
        
        self.is_running = True
        self.logger.info(f"LAIRM MCP Server started on port {self.port}")
        return True
    
    def stop(self) -> bool:
        """
        Stop the MCP server
        
        Returns:
            bool: True if server stopped successfully
        """
        if not self.is_running:
            self.logger.warning("Server is not running")
            return False
        
        self.is_running = False
        self.logger.info("LAIRM MCP Server stopped")
        return True
    
    def register_agent(self, agent_id: str, axiomes: List[str]) -> Dict[str, Any]:
        """
        Register a new agent with the server
        
        Args:
            agent_id: Unique identifier for the agent
            axiomes: List of LAIRM axiomes the agent complies with
        
        Returns:
            dict: Registration result with agent details
        """
        if agent_id in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} already registered'
            }
        
        agent = LAIRMAgentSDK(agent_id=agent_id, axiomes=axiomes)
        self.agents[agent_id] = agent
        
        self.logger.info(f"Agent registered: {agent_id} with axiomes {axiomes}")
        
        return {
            'success': True,
            'agent_id': agent_id,
            'axiomes': axiomes,
            'registered_at': datetime.now().isoformat()
        }
    
    def unregister_agent(self, agent_id: str) -> Dict[str, Any]:
        """
        Unregister an agent from the server
        
        Args:
            agent_id: Unique identifier for the agent
        
        Returns:
            dict: Unregistration result
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        del self.agents[agent_id]
        
        self.logger.info(f"Agent unregistered: {agent_id}")
        
        return {
            'success': True,
            'agent_id': agent_id,
            'unregistered_at': datetime.now().isoformat()
        }
    
    def check_compliance(self, agent_id: str, axiomes: List[str]) -> Dict[str, Any]:
        """
        Check if an agent complies with specified axiomes
        
        Args:
            agent_id: Unique identifier for the agent
            axiomes: List of axiomes to check
        
        Returns:
            dict: Compliance check result
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        agent = self.agents[agent_id]
        is_compliant = agent.check_compliance(axiomes)
        
        result = {
            'success': True,
            'agent_id': agent_id,
            'requested_axiomes': axiomes,
            'agent_axiomes': agent.axiomes,
            'compliant': is_compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        # Log compliance check
        agent.log_action('compliance_check', {
            'requested_axiomes': axiomes,
            'result': is_compliant
        })
        
        return result
    
    def log_agent_action(self, agent_id: str, action_type: str, details: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Log an action for an agent
        
        Args:
            agent_id: Unique identifier for the agent
            action_type: Type of action being logged
            details: Additional details about the action
        
        Returns:
            dict: Action logging result
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        agent = self.agents[agent_id]
        record = agent.log_action(action_type, details or {})
        
        return {
            'success': True,
            'agent_id': agent_id,
            'action_record': record
        }
    
    def get_agent_audit_log(self, agent_id: str) -> Dict[str, Any]:
        """
        Get the audit log for an agent
        
        Args:
            agent_id: Unique identifier for the agent
        
        Returns:
            dict: Audit log for the agent
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        agent = self.agents[agent_id]
        audit_log = agent.get_audit_log()
        
        return {
            'success': True,
            'agent_id': agent_id,
            'audit_log': audit_log,
            'log_size': len(audit_log)
        }
    
    def get_agent_status(self, agent_id: str) -> Dict[str, Any]:
        """
        Get the status of an agent
        
        Args:
            agent_id: Unique identifier for the agent
        
        Returns:
            dict: Agent status information
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        agent = self.agents[agent_id]
        status = agent.get_compliance_status()
        
        return {
            'success': True,
            'agent_status': status
        }
    
    def list_agents(self) -> Dict[str, Any]:
        """
        List all registered agents
        
        Returns:
            dict: List of all registered agents
        """
        agents_list = []
        
        for agent_id, agent in self.agents.items():
            agents_list.append({
                'agent_id': agent_id,
                'axiomes': agent.axiomes,
                'audit_log_size': len(agent.audit_log)
            })
        
        return {
            'success': True,
            'total_agents': len(agents_list),
            'agents': agents_list
        }
    
    def verify_axiom_compliance(self, agent_id: str, axiom_id: str, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Verify if an action complies with a specific axiom
        
        Args:
            agent_id: Unique identifier for the agent
            axiom_id: Axiom identifier (e.g., 'I', 'II', 'VI')
            action_data: Data about the action to verify
        
        Returns:
            dict: Verification result
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        # Use compliance checker to verify
        result = self.compliance_checker.check_axiom(axiom_id, action_data)
        
        # Log verification
        agent = self.agents[agent_id]
        agent.log_action('axiom_verification', {
            'axiom_id': axiom_id,
            'action_data': action_data,
            'result': result
        })
        
        return {
            'success': True,
            'agent_id': agent_id,
            'axiom_id': axiom_id,
            'compliant': result.get('compliant', False),
            'details': result
        }
    
    def create_audit_record(self, agent_id: str, action_type: str, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create an audit record for an agent action
        
        Args:
            agent_id: Unique identifier for the agent
            action_type: Type of action
            action_data: Data about the action
        
        Returns:
            dict: Audit record creation result
        """
        if agent_id not in self.agents:
            return {
                'success': False,
                'error': f'Agent {agent_id} not found'
            }
        
        # Create audit record using audit engine
        audit_record = self.audit_engine.create_audit_record(
            agent_id=agent_id,
            action_type=action_type,
            details=action_data
        )
        
        # Also log in agent's local log
        agent = self.agents[agent_id]
        agent.log_action(action_type, action_data)
        
        return {
            'success': True,
            'agent_id': agent_id,
            'audit_record': audit_record
        }
    
    def get_server_status(self) -> Dict[str, Any]:
        """
        Get the status of the MCP server
        
        Returns:
            dict: Server status information
        """
        return {
            'server_id': self.server_id,
            'port': self.port,
            'is_running': self.is_running,
            'total_agents': len(self.agents),
            'agents': list(self.agents.keys()),
            'timestamp': datetime.now().isoformat()
        }
    
    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle an MCP request
        
        Args:
            request: MCP request dictionary
        
        Returns:
            dict: Response to the request
        """
        method = request.get('method')
        params = request.get('params', {})
        
        if method == 'register_agent':
            return self.register_agent(
                agent_id=params.get('agent_id'),
                axiomes=params.get('axiomes', [])
            )
        
        elif method == 'unregister_agent':
            return self.unregister_agent(agent_id=params.get('agent_id'))
        
        elif method == 'check_compliance':
            return self.check_compliance(
                agent_id=params.get('agent_id'),
                axiomes=params.get('axiomes', [])
            )
        
        elif method == 'log_action':
            return self.log_agent_action(
                agent_id=params.get('agent_id'),
                action_type=params.get('action_type'),
                details=params.get('details')
            )
        
        elif method == 'get_audit_log':
            return self.get_agent_audit_log(agent_id=params.get('agent_id'))
        
        elif method == 'get_agent_status':
            return self.get_agent_status(agent_id=params.get('agent_id'))
        
        elif method == 'list_agents':
            return self.list_agents()
        
        elif method == 'verify_axiom':
            return self.verify_axiom_compliance(
                agent_id=params.get('agent_id'),
                axiom_id=params.get('axiom_id'),
                action_data=params.get('action_data', {})
            )
        
        elif method == 'create_audit_record':
            return self.create_audit_record(
                agent_id=params.get('agent_id'),
                action_type=params.get('action_type'),
                action_data=params.get('action_data', {})
            )
        
        elif method == 'get_server_status':
            return self.get_server_status()
        
        else:
            return {
                'success': False,
                'error': f'Unknown method: {method}'
            }


def main():
    """Main entry point for the MCP server"""
    server = LAIRMMCPServer()
    server.start()
    
    print(f"LAIRM MCP Server running on port {server.port}")
    print("Press Ctrl+C to stop")
    
    try:
        while server.is_running:
            pass
    except KeyboardInterrupt:
        server.stop()
        print("\nServer stopped")


if __name__ == '__main__':
    main()
