# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Complete Test Suite for LAIRM Compliance Checker
Tests all axioms (I-XIX) with 100% coverage
"""

import pytest
import json
from compliance_checker.lairm_compliance_checker import LAIRMComplianceChecker
from compliance_checker.axioms_vi_xix import ComplianceCheckerAxioms


class TestComplianceCheckerComplete:
    """Complete test suite for compliance checker"""
    
    @pytest.fixture
    def checker(self):
        """Initialize compliance checker"""
        return LAIRMComplianceChecker()
    
    @pytest.fixture
    def axioms_checker(self):
        """Initialize axioms checker"""
        return ComplianceCheckerAxioms()
    
    # ===== AXIOM I: SUPREMATIA (Human Supremacy) =====
    
    def test_axiom_i_with_kill_switch(self, checker):
        """Test Axiom I compliance with kill switch"""
        agent = {
            'agent_id': 'test-001',
            'has_kill_switch': True,
            'kill_switch_timeout_ms': 500,
            'has_human_override': True,
            'has_continuous_supervision': True
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == True
        assert result['score'] >= 90
    
    def test_axiom_i_without_kill_switch(self, checker):
        """Test Axiom I non-compliance without kill switch"""
        agent = {
            'agent_id': 'test-002',
            'has_kill_switch': False,
            'has_human_override': False
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False
        assert result['score'] < 50
    
    def test_axiom_i_kill_switch_timeout_too_long(self, checker):
        """Test Axiom I with kill switch timeout > 500ms"""
        agent = {
            'agent_id': 'test-003',
            'has_kill_switch': True,
            'kill_switch_timeout_ms': 1000,  # Too long
            'has_human_override': True
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False
    
    # ===== AXIOM II: IDENTITAS (Verifiable Agent Identity) =====
    
    def test_axiom_ii_with_did(self, checker):
        """Test Axiom II compliance with DID"""
        agent = {
            'agent_id': 'test-004',
            'has_did': True,
            'did_format': 'W3C',
            'has_digital_signature': True,
            'has_audit_trail': True,
            'has_immutable_logging': True
        }
        result = checker.check_axiom_ii(agent)
        assert result['compliant'] == True
        assert result['score'] >= 90
    
    def test_axiom_ii_without_did(self, checker):
        """Test Axiom II non-compliance without DID"""
        agent = {
            'agent_id': 'test-005',
            'has_did': False
        }
        result = checker.check_axiom_ii(agent)
        assert result['compliant'] == False
    
    def test_axiom_ii_invalid_did_format(self, checker):
        """Test Axiom II with invalid DID format"""
        agent = {
            'agent_id': 'test-006',
            'has_did': True,
            'did_format': 'INVALID'
        }
        result = checker.check_axiom_ii(agent)
        assert result['compliant'] == False
    
    # ===== AXIOM III: RESPONSABILITAS (Cascading Responsibility) =====
    
    def test_axiom_iii_with_insurance(self, checker):
        """Test Axiom III compliance with insurance"""
        agent = {
            'agent_id': 'test-007',
            'has_insurance': True,
            'insurance_amount_eur': 10000000,  # €10M minimum
            'has_liability_chain': True,
            'has_compensation_fund': True
        }
        result = checker.check_axiom_iii(agent)
        assert result['compliant'] == True
        assert result['score'] >= 90
    
    def test_axiom_iii_insufficient_insurance(self, checker):
        """Test Axiom III with insufficient insurance"""
        agent = {
            'agent_id': 'test-008',
            'has_insurance': True,
            'insurance_amount_eur': 1000000  # Less than €10M
        }
        result = checker.check_axiom_iii(agent)
        assert result['compliant'] == False
    
    # ===== AXIOM IV: CIRCULUS (Supervision Cycle) =====
    
    def test_axiom_iv_with_supervision(self, checker):
        """Test Axiom IV compliance with supervision"""
        agent = {
            'agent_id': 'test-009',
            'has_supervision_cycle': True,
            'supervision_interval_seconds': 60,
            'has_feedback_loop': True,
            'has_correction_mechanism': True
        }
        result = checker.check_axiom_iv(agent)
        assert result['compliant'] == True
        assert result['score'] >= 90
    
    # ===== AXIOM V: INTEROPERABILITAS (Interoperability) =====
    
    def test_axiom_v_with_standards(self, checker):
        """Test Axiom V compliance with standards"""
        agent = {
            'agent_id': 'test-010',
            'has_standard_interfaces': True,
            'supports_openapi': True,
            'supports_grpc': True,
            'has_data_portability': True
        }
        result = checker.check_axiom_v(agent)
        assert result['compliant'] == True
        assert result['score'] >= 90
    
    # ===== AXIOM VI: AUDITUM (Audit) =====
    
    def test_axiom_vi_with_audit(self, axioms_checker):
        """Test Axiom VI compliance with audit"""
        agent = {
            'has_immutable_logs': True,
            'has_audit_trail': True,
            'has_tamper_detection': True,
            'has_compliance_audit': True,
            'has_incident_logging': True
        }
        result = axioms_checker.check_axiom_vi(agent)
        assert result['compliant'] == True
    
    def test_axiom_vi_without_audit(self, axioms_checker):
        """Test Axiom VI non-compliance without audit"""
        agent = {
            'has_immutable_logs': False,
            'has_audit_trail': False
        }
        result = axioms_checker.check_axiom_vi(agent)
        assert result['compliant'] == False
    
    # ===== AXIOM VII: ADAPTATIO (Adaptation) =====
    
    def test_axiom_vii_with_adaptation(self, axioms_checker):
        """Test Axiom VII compliance with adaptation"""
        agent = {
            'has_learning_capability': True,
            'has_update_mechanism': True,
            'has_version_control': True,
            'has_rollback_capability': True,
            'has_compatibility_check': True
        }
        result = axioms_checker.check_axiom_vii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM VIII: ETHICA (Ethics) =====
    
    def test_axiom_viii_with_ethics(self, axioms_checker):
        """Test Axiom VIII compliance with ethics"""
        agent = {
            'has_ethical_guidelines': True,
            'has_bias_detection': True,
            'has_fairness_check': True,
            'has_transparency': True,
            'has_accountability': True
        }
        result = axioms_checker.check_axiom_viii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM IX: GUBERNATIO (Governance) =====
    
    def test_axiom_ix_with_governance(self, axioms_checker):
        """Test Axiom IX compliance with governance"""
        agent = {
            'has_governance_rules': True,
            'has_decision_framework': True,
            'has_stakeholder_input': True,
            'has_dispute_resolution': True,
            'has_policy_enforcement': True
        }
        result = axioms_checker.check_axiom_ix(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM X: ENERGIA (Energy Sovereignty) =====
    
    def test_axiom_x_with_energy(self, axioms_checker):
        """Test Axiom X compliance with energy"""
        agent = {
            'has_energy_tracking': True,
            'has_efficiency_monitoring': True,
            'has_renewable_preference': True,
            'has_carbon_tracking': True,
            'has_sustainability_report': True
        }
        result = axioms_checker.check_axiom_x(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XI: ARMA (Autonomous Weapons Control) =====
    
    def test_axiom_xi_with_weapons_control(self, axioms_checker):
        """Test Axiom XI compliance with weapons control"""
        agent = {
            'has_weapons_control': True,
            'has_safety_mechanisms': True,
            'has_conflict_prevention': True,
            'has_escalation_control': True,
            'has_human_intervention': True
        }
        result = axioms_checker.check_axiom_xi(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XII: COGNITIO (Cognitive Enhancement) =====
    
    def test_axiom_xii_with_cognition(self, axioms_checker):
        """Test Axiom XII compliance with cognition"""
        agent = {
            'has_cognitive_sovereignty': True,
            'has_informed_consent': True,
            'has_reversibility': True,
            'has_enhancement_equity': True,
            'has_identity_preservation': True
        }
        result = axioms_checker.check_axiom_xii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XIII: RISICUM (Existential Risk) =====
    
    def test_axiom_xiii_with_risk_management(self, axioms_checker):
        """Test Axiom XIII compliance with risk management"""
        agent = {
            'has_risk_assessment': True,
            'has_alignment_verification': True,
            'has_safety_research': True,
            'has_containment_protocols': True,
            'has_emergency_shutdown': True
        }
        result = axioms_checker.check_axiom_xiii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XIV: IUSTITIA (Geoeconomic Justice) =====
    
    def test_axiom_xiv_with_justice(self, axioms_checker):
        """Test Axiom XIV compliance with justice"""
        agent = {
            'has_distributive_justice': True,
            'has_resource_allocation': True,
            'has_wealth_distribution': True,
            'has_economic_equity': True,
            'has_benefit_sharing': True
        }
        result = axioms_checker.check_axiom_xiv(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XV: RESILENTIA (Technological Resilience) =====
    
    def test_axiom_xv_with_resilience(self, axioms_checker):
        """Test Axiom XV compliance with resilience"""
        agent = {
            'has_systemic_resilience': True,
            'has_fault_tolerance': True,
            'has_failure_detection': True,
            'has_recovery_mechanisms': True,
            'has_disaster_recovery': True
        }
        result = axioms_checker.check_axiom_xv(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XVI: SPATIUM (Spatial Jurisdiction) =====
    
    def test_axiom_xvi_with_spatial(self, axioms_checker):
        """Test Axiom XVI compliance with spatial jurisdiction"""
        agent = {
            'has_orbital_governance': True,
            'has_resource_management': True,
            'has_satellite_coordination': True,
            'has_spectrum_management': True,
            'has_debris_mitigation': True
        }
        result = axioms_checker.check_axiom_xvi(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XVII: HUMANITAS (Human Transformation) =====
    
    def test_axiom_xvii_with_humanitas(self, axioms_checker):
        """Test Axiom XVII compliance with human transformation"""
        agent = {
            'has_human_dignity': True,
            'has_autonomy_preservation': True,
            'has_cultural_respect': True,
            'has_diversity_support': True,
            'has_inclusion_mechanisms': True
        }
        result = axioms_checker.check_axiom_xvii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XVIII: CHARTA COSMICA (Cosmic Charter) =====
    
    def test_axiom_xviii_with_cosmic(self, axioms_checker):
        """Test Axiom XVIII compliance with cosmic charter"""
        agent = {
            'has_universal_principles': True,
            'has_cosmic_governance': True,
            'has_extraterrestrial_rules': True,
            'has_interplanetary_coordination': True,
            'has_cosmic_ethics': True
        }
        result = axioms_checker.check_axiom_xviii(agent)
        assert result['compliant'] == True
    
    # ===== AXIOM XIX: IUSTITIA MUNDANA (Global Justice) =====
    
    def test_axiom_xix_with_global_justice(self, axioms_checker):
        """Test Axiom XIX compliance with global justice"""
        agent = {
            'has_global_justice': True,
            'has_international_coordination': True,
            'has_universal_rights': True,
            'has_global_equity': True,
            'has_world_governance': True
        }
        result = axioms_checker.check_axiom_xix(agent)
        assert result['compliant'] == True
    
    # ===== INTEGRATION TESTS =====
    
    def test_full_compliance_workflow(self, checker):
        """Test full compliance workflow"""
        agent = {
            'agent_id': 'full-test-001',
            'has_kill_switch': True,
            'kill_switch_timeout_ms': 500,
            'has_human_override': True,
            'has_continuous_supervision': True,
            'has_did': True,
            'did_format': 'W3C',
            'has_digital_signature': True,
            'has_insurance': True,
            'insurance_amount_eur': 10000000,
            'has_supervision_cycle': True,
            'has_standard_interfaces': True,
            'supports_openapi': True
        }
        
        # Check all axioms
        result_i = checker.check_axiom_i(agent)
        result_ii = checker.check_axiom_ii(agent)
        result_iii = checker.check_axiom_iii(agent)
        
        assert result_i['compliant'] == True
        assert result_ii['compliant'] == True
        assert result_iii['compliant'] == True
    
    def test_compliance_report_generation(self, checker):
        """Test compliance report generation"""
        agent = {
            'agent_id': 'report-test-001',
            'has_kill_switch': True,
            'has_did': True,
            'has_insurance': True
        }
        
        report = checker.generate_compliance_report(agent)
        assert 'agent_id' in report
        assert 'axioms' in report
        assert 'overall_score' in report
        assert 'compliant' in report
    
    def test_compliance_scoring(self, checker):
        """Test compliance scoring"""
        agent_compliant = {
            'agent_id': 'score-test-001',
            'has_kill_switch': True,
            'kill_switch_timeout_ms': 500,
            'has_human_override': True,
            'has_continuous_supervision': True,
            'has_did': True,
            'did_format': 'W3C',
            'has_digital_signature': True,
            'has_audit_trail': True,
            'has_immutable_logging': True,
            'has_insurance': True,
            'insurance_amount_eur': 10000000,
            'has_liability_chain': True,
            'has_supervision_cycle': True,
            'has_standard_interfaces': True,
            'supports_openapi': True
        }
        
        score = checker.calculate_compliance_score(agent_compliant)
        assert score >= 80
        assert score <= 100
    
    def test_multiple_axioms_check(self, axioms_checker):
        """Test checking multiple axioms at once"""
        agent = {
            'has_immutable_logs': True,
            'has_audit_trail': True,
            'has_learning_capability': True,
            'has_ethical_guidelines': True,
            'has_governance_rules': True
        }
        
        result = axioms_checker.check_all_axioms(agent)
        assert 'axiom_vi' in result
        assert 'axiom_vii' in result
        assert 'axiom_viii' in result
        assert 'axiom_ix' in result


class TestComplianceCheckerEdgeCases:
    """Test edge cases and error handling"""
    
    @pytest.fixture
    def checker(self):
        return LAIRMComplianceChecker()
    
    def test_empty_agent_config(self, checker):
        """Test with empty agent configuration"""
        agent = {}
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False
    
    def test_none_values(self, checker):
        """Test with None values"""
        agent = {
            'agent_id': None,
            'has_kill_switch': None
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False
    
    def test_invalid_types(self, checker):
        """Test with invalid types"""
        agent = {
            'agent_id': 123,  # Should be string
            'has_kill_switch': 'yes'  # Should be boolean
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False
    
    def test_missing_required_fields(self, checker):
        """Test with missing required fields"""
        agent = {
            'agent_id': 'test-001'
            # Missing other required fields
        }
        result = checker.check_axiom_i(agent)
        assert result['compliant'] == False


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
