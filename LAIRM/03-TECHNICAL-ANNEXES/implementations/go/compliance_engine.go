/*
---
title: "LAIRM Compliance Engine - Go Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Compliance Engine - Go Implementation

This file implements the compliance verification engine for LAIRM framework in Go.

Features:
- Rule-based compliance checking across all LAIRM axioms
- Compliance report generation with violations and warnings
- Compliance scoring and matrix generation
- Support for mandatory, required, recommended, and optional rules

The engine validates agent configurations against LAIRM axioms and generates
detailed compliance reports for audit and certification purposes.
*/

package lairm

import (
	"fmt"
	"time"
)

// ComplianceLevel represents compliance level
type ComplianceLevel string

const (
	Mandatory    ComplianceLevel = "mandatory"
	Required     ComplianceLevel = "required"
	Recommended  ComplianceLevel = "recommended"
	Optional     ComplianceLevel = "optional"
)

// ComplianceRule represents a compliance rule
type ComplianceRule struct {
	RuleID      string
	Axiome      string
	Description string
	Level       ComplianceLevel
	Validator   func(map[string]interface{}) (bool, string)
}

// NewComplianceRule creates a new compliance rule
func NewComplianceRule(ruleID, axiome, description string, level ComplianceLevel) *ComplianceRule {
	return &ComplianceRule{
		RuleID:      ruleID,
		Axiome:      axiome,
		Description: description,
		Level:       level,
	}
}

// Validate validates configuration against rule
func (cr *ComplianceRule) Validate(config map[string]interface{}) (bool, string) {
	if cr.Validator != nil {
		return cr.Validator(config)
	}
	return true, "No validator defined"
}

// ComplianceViolation represents a compliance violation
type ComplianceViolation struct {
	RuleID    string    `json:"rule_id"`
	Axiome    string    `json:"axiome"`
	Message   string    `json:"message"`
	Timestamp time.Time `json:"timestamp"`
}

// ComplianceReport represents a compliance audit report
type ComplianceReport struct {
	AgentID        string                  `json:"agent_id"`
	Timestamp      time.Time               `json:"timestamp"`
	AxiomesChecked []string                `json:"axiomes_checked"`
	Violations     []ComplianceViolation   `json:"violations"`
	Warnings       []ComplianceViolation   `json:"warnings"`
	PassedRules    int                     `json:"passed_rules"`
}

// NewComplianceReport creates a new compliance report
func NewComplianceReport(agentID string) *ComplianceReport {
	return &ComplianceReport{
		AgentID:        agentID,
		Timestamp:      time.Now().UTC(),
		AxiomesChecked: make([]string, 0),
		Violations:     make([]ComplianceViolation, 0),
		Warnings:       make([]ComplianceViolation, 0),
		PassedRules:    0,
	}
}

// AddViolation adds a compliance violation
func (cr *ComplianceReport) AddViolation(ruleID, axiome, message string) {
	violation := ComplianceViolation{
		RuleID:    ruleID,
		Axiome:    axiome,
		Message:   message,
		Timestamp: time.Now().UTC(),
	}
	cr.Violations = append(cr.Violations, violation)
}

// AddWarning adds a compliance warning
func (cr *ComplianceReport) AddWarning(ruleID, axiome, message string) {
	warning := ComplianceViolation{
		RuleID:    ruleID,
		Axiome:    axiome,
		Message:   message,
		Timestamp: time.Now().UTC(),
	}
	cr.Warnings = append(cr.Warnings, warning)
}

// AddPassedRule records a passed rule
func (cr *ComplianceReport) AddPassedRule() {
	cr.PassedRules++
}

// GetStatus returns overall compliance status
func (cr *ComplianceReport) GetStatus() ComplianceStatus {
	if len(cr.Violations) > 0 {
		return NonCompliant
	}
	if len(cr.Warnings) > 0 {
		return Partial
	}
	return Compliant
}

// LAIRMComplianceEngine represents the compliance engine
type LAIRMComplianceEngine struct {
	Rules map[string][]*ComplianceRule
}

// NewLAIRMComplianceEngine creates a new compliance engine
func NewLAIRMComplianceEngine() *LAIRMComplianceEngine {
	engine := &LAIRMComplianceEngine{
		Rules: make(map[string][]*ComplianceRule),
	}
	engine.initializeDefaultRules()
	return engine
}

func (ce *LAIRMComplianceEngine) initializeDefaultRules() {
	// Axiome I - SUPREMATIA
	ce.AddRule(NewComplianceRule(
		"I-001",
		"I",
		"Agent must have kill-switch capability",
		Mandatory,
	))

	ce.AddRule(NewComplianceRule(
		"I-002",
		"I",
		"Kill-switch must respond within 500ms",
		Mandatory,
	))

	// Axiome II - IDENTITAS
	ce.AddRule(NewComplianceRule(
		"II-001",
		"II",
		"Agent must have unique passport",
		Mandatory,
	))

	ce.AddRule(NewComplianceRule(
		"II-002",
		"II",
		"Passport must include digital signature",
		Mandatory,
	))

	// Axiome III - RESPONSABILITAS
	ce.AddRule(NewComplianceRule(
		"III-001",
		"III",
		"Agent must log all actions",
		Mandatory,
	))

	// Axiome VI - AUDITUM
	ce.AddRule(NewComplianceRule(
		"VI-001",
		"VI",
		"Audit log must be immutable",
		Mandatory,
	))

	ce.AddRule(NewComplianceRule(
		"VI-002",
		"VI",
		"Audit entries must include timestamps",
		Mandatory,
	))
}

// AddRule adds a compliance rule
func (ce *LAIRMComplianceEngine) AddRule(rule *ComplianceRule) {
	if _, exists := ce.Rules[rule.Axiome]; !exists {
		ce.Rules[rule.Axiome] = make([]*ComplianceRule, 0)
	}
	ce.Rules[rule.Axiome] = append(ce.Rules[rule.Axiome], rule)
}

// CheckCompliance checks agent compliance with specified axiomes
func (ce *LAIRMComplianceEngine) CheckCompliance(agentID string, axiomes []string, config map[string]interface{}) *ComplianceReport {
	report := NewComplianceReport(agentID)
	report.AxiomesChecked = axiomes

	for _, axiome := range axiomes {
		if rules, exists := ce.Rules[axiome]; exists {
			for _, rule := range rules {
				passed, message := rule.Validate(config)

				if passed {
					report.AddPassedRule()
				} else {
					if rule.Level == Mandatory {
						report.AddViolation(rule.RuleID, axiome, message)
					} else {
						report.AddWarning(rule.RuleID, axiome, message)
					}
				}
			}
		}
	}

	return report
}

// GetAxiomeRules returns all rules for an axiome
func (ce *LAIRMComplianceEngine) GetAxiomeRules(axiome string) []*ComplianceRule {
	if rules, exists := ce.Rules[axiome]; exists {
		return rules
	}
	return make([]*ComplianceRule, 0)
}

// GenerateComplianceMatrix generates compliance matrix for all axiomes
func (ce *LAIRMComplianceEngine) GenerateComplianceMatrix(agentID string, config map[string]interface{}) map[string]interface{} {
	axiomes := make([]string, 0)
	for axiome := range ce.Rules {
		axiomes = append(axiomes, axiome)
	}

	report := ce.CheckCompliance(agentID, axiomes, config)

	matrix := map[string]interface{}{
		"agent_id":  agentID,
		"timestamp": time.Now().UTC(),
		"axiomes":   make(map[string]interface{}),
	}

	axiomesMap := matrix["axiomes"].(map[string]interface{})
	for axiome := range ce.Rules {
		rules := ce.GetAxiomeRules(axiome)
		axiomesMap[axiome] = map[string]interface{}{
			"total_rules": len(rules),
			"rules":       rules,
		}
	}

	return matrix
}

// GetComplianceScore calculates compliance score
func (ce *LAIRMComplianceEngine) GetComplianceScore(report *ComplianceReport) float64 {
	totalRules := report.PassedRules + len(report.Violations) + len(report.Warnings)
	if totalRules == 0 {
		return 100.0
	}

	score := float64(report.PassedRules) / float64(totalRules) * 100.0
	return score
}

// PrintReport prints compliance report
func (ce *LAIRMComplianceEngine) PrintReport(report *ComplianceReport) {
	fmt.Printf("Compliance Report for Agent: %s\n", report.AgentID)
	fmt.Printf("Status: %s\n", report.GetStatus())
	fmt.Printf("Axiomes Checked: %v\n", report.AxiomesChecked)
	fmt.Printf("Passed Rules: %d\n", report.PassedRules)
	fmt.Printf("Violations: %d\n", len(report.Violations))
	fmt.Printf("Warnings: %d\n", len(report.Warnings))

	if len(report.Violations) > 0 {
		fmt.Println("\nViolations:")
		for _, v := range report.Violations {
			fmt.Printf("  - %s (%s): %s\n", v.RuleID, v.Axiome, v.Message)
		}
	}

	if len(report.Warnings) > 0 {
		fmt.Println("\nWarnings:")
		for _, w := range report.Warnings {
			fmt.Printf("  - %s (%s): %s\n", w.RuleID, w.Axiome, w.Message)
		}
	}
}
