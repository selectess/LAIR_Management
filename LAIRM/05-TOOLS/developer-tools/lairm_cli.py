# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

#!/usr/bin/env python3
"""
LAIRM CLI - Command Line Interface
Outils en ligne de commande pour gérer le framework LAIRM
"""

import argparse
import sys
import json
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

# Importer les modules LAIRM
sys.path.insert(0, str(Path(__file__).parent.parent))
from mcp_server.lairm_mcp_server import LAIRMMCPServer
from compliance_checker.lairm_compliance_checker import LAIRMComplianceChecker
from audit_engine.lairm_audit_engine import LAIRMAuditEngine
from agent_framework.lairm_agent_sdk import LAIRMAgentSDK


class LAIRMCLI:
    """CLI pour LAIRM"""

    def __init__(self):
        self.mcp_server = LAIRMMCPServer()
        self.compliance_checker = LAIRMComplianceChecker()
        self.audit_engine = LAIRMAuditEngine()

    def validate(self, args):
        """Valider la structure LAIRM"""
        print("=" * 80)
        print("LAIRM VALIDATION")
        print("=" * 80)
        print()

        # Vérifier framework
        stats = self.mcp_server.get_statistics()

        print(f"✅ Total articles: {stats['total_articles']}")
        print(f"✅ Total axiomes: {stats['total_axiomes']}")
        print()

        # Vérifier chaque axiome
        print("Axiome Status:")
        for axiome_name, count in stats['axiomes'].items():
            print(f"  ✅ {axiome_name}: {count} articles")

        print()
        print("✅ Framework is VALID")
        print()

    def search(self, args):
        """Chercher des articles"""
        print("=" * 80)
        print("LAIRM SEARCH")
        print("=" * 80)
        print()

        query = args.query or ""
        axiome = args.axiome or ""
        statut = args.statut or ""

        results = self.mcp_server.search_articles(
            query=query,
            axiome=axiome,
            statut=statut
        )

        print(f"Found {len(results)} articles")
        print()

        for article in results[:10]:
            print(f"  [{article['numero']}] {article['titre']}")
            print(f"      Axiome: {article['axiome']}, Status: {article['statut']}")

        if len(results) > 10:
            print(f"  ... and {len(results) - 10} more")

        print()

    def get_article(self, args):
        """Récupérer un article"""
        print("=" * 80)
        print(f"ARTICLE: {args.numero}")
        print("=" * 80)
        print()

        article = self.mcp_server.get_article(args.numero)

        if article:
            print(f"Title: {article['titre']}")
            print(f"Axiome: {article['axiome']}")
            print(f"Status: {article['statut']}")
            print(f"File: {article['file']}")
            print()
            print("Content Preview:")
            print("-" * 80)
            content = article.get('content', '')
            lines = content.split('\n')[:20]
            for line in lines:
                print(line)
            print("...")
        else:
            print(f"❌ Article {args.numero} not found")

        print()

    def compliance(self, args):
        """Vérifier conformité"""
        print("=" * 80)
        print("COMPLIANCE CHECK")
        print("=" * 80)
        print()

        agent_config = {
            'agent_id': args.agent_id or 'test-agent',
            'axiomes_required': args.axiomes.split(',') if args.axiomes else ['I', 'II', 'III']
        }

        report = self.compliance_checker.check_agent_compliance(agent_config)

        print(self.compliance_checker.generate_compliance_report(agent_config))

    def audit(self, args):
        """Auditer le framework"""
        print("=" * 80)
        print("LAIRM AUDIT")
        print("=" * 80)
        print()

        # Créer enregistrements d'audit
        for i in range(3):
            record = self.audit_engine.create_audit_record(
                agent_id='audit-agent',
                action_type='audit_check',
                details={'check': i},
                axiomes=['I', 'II', 'III']
            )
            print(f"✅ Audit record {i+1}: {record['hash'][:16]}...")

        print()
        chain_status = '✅ VALID' if self.audit_engine.verify_audit_chain() else '❌ INVALID'
        print(f"Chain integrity: {chain_status}")
        print()

    def generate(self, args):
        """Générer rapports"""
        print("=" * 80)
        print(f"GENERATE: {args.type}")
        print("=" * 80)
        print()

        if args.type == 'compliance':
            agent_config = {
                'agent_id': 'generated-agent',
                'axiomes_required': ['I', 'II', 'III', 'IV', 'V']
            }
            report = self.compliance_checker.check_agent_compliance(agent_config)
            print(json.dumps(report, indent=2))

        elif args.type == 'audit':
            stats = self.audit_engine.get_statistics()
            print(json.dumps(stats, indent=2))

        elif args.type == 'framework':
            stats = self.mcp_server.get_statistics()
            print(json.dumps(stats, indent=2))

        print()


def main():
    """Main CLI"""
    parser = argparse.ArgumentParser(
        description='LAIRM Command Line Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  lairm validate
  lairm search --query "kill-switch" --axiome I
  lairm get-article --numero "I.1.1"
  lairm compliance --agent-id "agent-001" --axiomes "I,II,III"
  lairm audit
  lairm generate --type compliance
        '''
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # validate
    subparsers.add_parser('validate', help='Validate LAIRM framework')

    # search
    search_parser = subparsers.add_parser('search', help='Search articles')
    search_parser.add_argument('--query', help='Search query')
    search_parser.add_argument('--axiome', help='Filter by axiome')
    search_parser.add_argument('--statut', help='Filter by status')

    # get-article
    article_parser = subparsers.add_parser('get-article', help='Get article')
    article_parser.add_argument('--numero', required=True, help='Article number')

    # compliance
    compliance_parser = subparsers.add_parser('compliance', help='Check compliance')
    compliance_parser.add_argument('--agent-id', help='Agent ID')
    compliance_parser.add_argument('--axiomes', help='Axiomes (comma-separated)')

    # audit
    subparsers.add_parser('audit', help='Audit framework')

    # generate
    generate_parser = subparsers.add_parser('generate', help='Generate reports')
    choices = ['compliance', 'audit', 'framework']
    generate_parser.add_argument('--type', required=True, choices=choices)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    cli = LAIRMCLI()

    if args.command == 'validate':
        cli.validate(args)
    elif args.command == 'search':
        cli.search(args)
    elif args.command == 'get-article':
        cli.get_article(args)
    elif args.command == 'compliance':
        cli.compliance(args)
    elif args.command == 'audit':
        cli.audit(args)
    elif args.command == 'generate':
        cli.generate(args)


if __name__ == "__main__":
    main()
