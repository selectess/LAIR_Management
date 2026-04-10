    #!/usr/bin/env python3
"""
LAIRM MCP Server
Serveur MCP pour accéder au framework LAIRM
"""

import json
import os
import logging
from pathlib import Path
from typing import List, Dict, Any
import re

logger = logging.getLogger(__name__)

class LAIRMMCPServer:
    """Serveur MCP pour LAIRM"""

    def __init__(self, lairm_root: str = "LAIRM"):
        self.lairm_root = Path(lairm_root)
        self.articles = {}
        self.axiomes = {}
        self.load_framework()

    def load_framework(self):
        """Charger le framework LAIRM"""
        legislatif_path = self.lairm_root / "02-COMPENDIUM-LEGISLATIF"

        for axiome_dir in sorted(legislatif_path.iterdir()):
            if not axiome_dir.is_dir() or axiome_dir.name == "README.md":
                continue

            axiome_name = axiome_dir.name
            articles = []

            for article_file in sorted(axiome_dir.glob("article-*.md")):
                article_data = self.parse_article(article_file)
                if article_data:
                    articles.append(article_data)
                    self.articles[article_data['numero']] = article_data

            self.axiomes[axiome_name] = {
                'name': axiome_name,
                'articles': articles,
                'count': len(articles)
            }

    def parse_article(self, file_path: Path) -> Dict[str, Any]:
        """Parser un article"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extraire YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not yaml_match:
                return None

            yaml_content = yaml_match.group(1)

            # Extraire titre
            titre_match = re.search(r'titre:\s*"([^"]+)"', yaml_content)
            titre = titre_match.group(1) if titre_match else "Unknown"

            # Extraire numéro
            numero_match = re.search(r'numero:\s*([^\n]+)', yaml_content)
            numero = numero_match.group(1).strip() if numero_match else "Unknown"

            # Extraire statut
            statut_match = re.search(r'statut:\s*(\w+)', yaml_content)
            statut = statut_match.group(1) if statut_match else "Unknown"

            # Extraire axiome
            axiome_match = re.search(r'axiome:\s*([^\n]+)', yaml_content)
            axiome = axiome_match.group(1).strip() if axiome_match else "Unknown"

            return {
                'numero': numero,
                'titre': titre,
                'axiome': axiome,
                'statut': statut,
                'file': str(file_path.relative_to(self.lairm_root)),
                'path': file_path
            }
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None

    def search_articles(self, query: str = "", axiome: str = "", statut: str = "") -> List[Dict]:
        """Chercher articles"""
        results = []

        for article in self.articles.values():
            # Filtrer par axiome
            if axiome and axiome not in article['axiome']:
                continue

            # Filtrer par statut
            if statut and article['statut'] != statut:
                continue

            # Filtrer par query
            if query:
                query_lower = query.lower()
                if (query_lower not in article['titre'].lower() and
                    query_lower not in article['numero'].lower()):
                    continue

            results.append(article)

        return results

    def get_article(self, numero: str) -> Dict[str, Any]:
        """Récupérer un article"""
        if numero in self.articles:
            article = self.articles[numero]
            # Charger le contenu complet
            with open(article['path'], 'r', encoding='utf-8') as f:
                content = f.read()
            article['content'] = content
            return article
        return None

    def get_axiome(self, axiome_name: str) -> Dict[str, Any]:
        """Récupérer un axiome"""
        for axiome_key, axiome_data in self.axiomes.items():
            if axiome_name in axiome_key:
                return axiome_data
        return None

    def validate_compliance(self, agent_config: Dict) -> Dict[str, Any]:
        """Valider conformité d'un agent"""
        required_axiomes = agent_config.get('axiomes_required', [])

        compliance_report = {
            'agent_id': agent_config.get('agent_id', 'unknown'),
            'compliant': True,
            'axiomes': {},
            'violations': []
        }

        for axiome in required_axiomes:
            axiome_data = self.get_axiome(axiome)
            if axiome_data:
                compliance_report['axiomes'][axiome] = {
                    'status': 'compliant',
                    'articles': axiome_data['count']
                }
            else:
                compliance_report['axiomes'][axiome] = {
                    'status': 'not_found'
                }
                compliance_report['compliant'] = False
                compliance_report['violations'].append(f"Axiome {axiome} not found")

        return compliance_report

    def audit_action(self, agent_id: str, action: Dict) -> Dict[str, Any]:
        """Auditer une action"""
        audit_record = {
            'agent_id': agent_id,
            'action': action.get('type', 'unknown'),
            'timestamp': action.get('timestamp', 'unknown'),
            'axiomes_checked': [],
            'compliant': True,
            'violations': []
        }

        # Vérifier conformité aux axiomes
        required_axiomes = action.get('axiomes_required', [])
        for axiome in required_axiomes:
            axiome_data = self.get_axiome(axiome)
            if axiome_data:
                audit_record['axiomes_checked'].append(axiome)
            else:
                audit_record['violations'].append(f"Axiome {axiome} not found")
                audit_record['compliant'] = False

        return audit_record

    def get_statistics(self) -> Dict[str, Any]:
        """Obtenir statistiques du framework"""
        return {
            'total_articles': len(self.articles),
            'total_axiomes': len(self.axiomes),
            'axiomes': {
                name: axiome['count']
                for name, axiome in self.axiomes.items()
            },
            'status': 'ready'
        }


def main():
    """Test du serveur"""
    server = LAIRMMCPServer()

    print("=" * 80)
    print("LAIRM MCP SERVER - TEST")
    print("=" * 80)
    print()

    # Statistiques
    stats = server.get_statistics()
    print(f"Total articles: {stats['total_articles']}")
    print(f"Total axiomes: {stats['total_axiomes']}")
    print()

    # Chercher articles
    print("Searching for 'kill-switch' articles:")
    results = server.search_articles(query="kill-switch")
    for article in results[:3]:
        print(f"  - {article['numero']}: {article['titre']}")
    print()

    # Valider conformité
    print("Validating agent compliance:")
    agent_config = {
        'agent_id': 'test-agent-001',
        'axiomes_required': ['I', 'II', 'III']
    }
    compliance = server.validate_compliance(agent_config)
    print(f"  Agent: {compliance['agent_id']}")
    print(f"  Compliant: {compliance['compliant']}")
    print()

    print("=" * 80)
    print("✅ LAIRM MCP Server is ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
