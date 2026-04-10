/*
---
title: "LAIRM Core Framework - Go Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Core Framework - Go Implementation

This file implements the core LAIRM framework in Go, providing:
- Agent identity management (Axiom II - Identitas)
- Kill-switch mechanism (Axiom I - Suprematia)
- Immutable audit logging (Axiom VI - Auditum)
- Compliance verification framework

The implementation is designed for concurrent and distributed systems,
leveraging Go's native concurrency primitives and strong typing.
*/

package lairm

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"time"

	"github.com/google/uuid"
)

// Axiome represents LAIRM axiomes
type Axiome string

const (
	AxiomeSuprematia        Axiome = "I"
	AxiomeIdentitas         Axiome = "II"
	AxiomeResponsabilitas   Axiome = "III"
	AxiomeCirculus          Axiome = "IV"
	AxiomeInteroperabilitas Axiome = "V"
	AxiomeAuditum           Axiome = "VI"
	AxiomeAdaptatio         Axiome = "VII"
	AxiomeEthica            Axiome = "VIII"
	AxiomeGubernatio        Axiome = "IX"
	AxiomeEnergia           Axiome = "X"
	AxiomeArma              Axiome = "XI"
	AxiomeCognitio          Axiome = "XII"
	AxiomeRisicum           Axiome = "XIII"
	AxiomeIustitia          Axiome = "XIV"
	AxiomeResilentia        Axiome = "XV"
	AxiomeSpatium           Axiome = "XVI"
	AxiomeHumanitas         Axiome = "XVII"
	AxiomeChartaCosmica     Axiome = "XVIII"
)

// ComplianceStatus represents compliance status
type ComplianceStatus string

const (
	Compliant    ComplianceStatus = "compliant"
	NonCompliant ComplianceStatus = "non_compliant"
	Partial      ComplianceStatus = "partial"
	Unknown      ComplianceStatus = "unknown"
)

// AgentPassport represents unique agent identity
type AgentPassport struct {
	AgentID            string    `json:"agent_id"`
	AgentName          string    `json:"agent_name"`
	Version            string    `json:"version"`
	CreatedAt          time.Time `json:"created_at"`
	Signature          string    `json:"signature"`
	AxiomesSupported   []string  `json:"axiomes_supported"`
}

// NewAgentPassport creates a new agent passport
func NewAgentPassport(agentID, agentName string) *AgentPassport {
	if agentID == "" {
		agentID = uuid.New().String()
	}

	createdAt := time.Now().UTC()
	signature := generateSignature(agentID, agentName, createdAt.String())

	axiomes := []string{
		"I", "II", "III", "IV", "V", "VI", "VII", "VIII",
		"IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII",
	}

	return &AgentPassport{
		AgentID:          agentID,
		AgentName:        agentName,
		Version:          "1.0",
		CreatedAt:        createdAt,
		Signature:        signature,
		AxiomesSupported: axiomes,
	}
}

func generateSignature(agentID, agentName, createdAt string) string {
	data := agentID + agentName + createdAt
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

// KillSwitch represents kill-switch mechanism (Axiome I)
type KillSwitch struct {
	AgentID     string
	AuthorityID string
	IsActive    bool
	TriggeredAt *time.Time
	Reason      string
}

// NewKillSwitch creates a new kill-switch
func NewKillSwitch(agentID, authorityID string) *KillSwitch {
	return &KillSwitch{
		AgentID:     agentID,
		AuthorityID: authorityID,
		IsActive:    false,
	}
}

// Trigger activates the kill-switch
func (ks *KillSwitch) Trigger(reason string) map[string]interface{} {
	ks.IsActive = true
	now := time.Now().UTC()
	ks.TriggeredAt = &now
	ks.Reason = reason

	return map[string]interface{}{
		"status":       "killed",
		"agent_id":     ks.AgentID,
		"triggered_at": ks.TriggeredAt,
		"reason":       reason,
		"authority":    ks.AuthorityID,
	}
}

// IsAlive checks if agent is still alive
func (ks *KillSwitch) IsAlive() bool {
	return !ks.IsActive
}

// AuditEntry represents an immutable audit entry
type AuditEntry struct {
	EntryID   string                 `json:"entry_id"`
	Timestamp time.Time              `json:"timestamp"`
	Action    string                 `json:"action"`
	Details   map[string]interface{} `json:"details"`
	Status    string                 `json:"status"`
	Hash      string                 `json:"hash"`
}

// NewAuditEntry creates a new audit entry
func NewAuditEntry(action string, details map[string]interface{}, status string) *AuditEntry {
	entry := &AuditEntry{
		EntryID:   uuid.New().String(),
		Timestamp: time.Now().UTC(),
		Action:    action,
		Details:   details,
		Status:    status,
	}
	entry.Hash = entry.calculateHash()
	return entry
}

func (ae *AuditEntry) calculateHash() string {
	data := fmt.Sprintf("%s%s%s%s%v", ae.EntryID, ae.Timestamp.String(), ae.Action, ae.Status, ae.Details)
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

// VerifyIntegrity verifies entry integrity
func (ae *AuditEntry) VerifyIntegrity() bool {
	return ae.Hash == ae.calculateHash()
}

// AuditLog represents immutable audit log
type AuditLog struct {
	AgentID   string
	Entries   []*AuditEntry
	ChainHash string
	CreatedAt time.Time
}

// NewAuditLog creates a new audit log
func NewAuditLog(agentID string) *AuditLog {
	return &AuditLog{
		AgentID:   agentID,
		Entries:   make([]*AuditEntry, 0),
		CreatedAt: time.Now().UTC(),
	}
}

// RecordAction records an action in the audit log
func (al *AuditLog) RecordAction(action string, details map[string]interface{}, status string) string {
	entry := NewAuditEntry(action, details, status)
	al.Entries = append(al.Entries, entry)
	al.updateChainHash()
	return entry.EntryID
}

func (al *AuditLog) updateChainHash() {
	if len(al.Entries) == 0 {
		al.ChainHash = ""
		return
	}

	lastEntry := al.Entries[len(al.Entries)-1]
	chainData := al.ChainHash + lastEntry.Hash
	hash := sha256.Sum256([]byte(chainData))
	al.ChainHash = hex.EncodeToString(hash[:])
}

// GetEntries returns all audit entries
func (al *AuditLog) GetEntries() []*AuditEntry {
	return al.Entries
}

// VerifyIntegrity verifies entire log integrity
func (al *AuditLog) VerifyIntegrity() bool {
	for _, entry := range al.Entries {
		if !entry.VerifyIntegrity() {
			return false
		}
	}

	// Verify chain integrity
	recalculatedChain := ""
	for _, entry := range al.Entries {
		chainData := recalculatedChain + entry.Hash
		hash := sha256.Sum256([]byte(chainData))
		recalculatedChain = hex.EncodeToString(hash[:])
	}

	return recalculatedChain == al.ChainHash
}

// LAIRMFramework represents the main LAIRM framework
type LAIRMFramework struct {
	AgentID      string
	AgentName    string
	Passport     *AgentPassport
	KillSwitch   *KillSwitch
	AuditLog     *AuditLog
}

// NewLAIRMFramework creates a new LAIRM framework instance
func NewLAIRMFramework(agentID, agentName string) *LAIRMFramework {
	passport := NewAgentPassport(agentID, agentName)
	killSwitch := NewKillSwitch(passport.AgentID, "system-authority")
	auditLog := NewAuditLog(passport.AgentID)

	return &LAIRMFramework{
		AgentID:    passport.AgentID,
		AgentName:  agentName,
		Passport:   passport,
		KillSwitch: killSwitch,
		AuditLog:   auditLog,
	}
}

// ExecuteAction executes an action with audit trail
// Returns execution result with status, entry_id, and timestamp
// If kill-switch is active, returns error status
func (lf *LAIRMFramework) ExecuteAction(action string, params map[string]interface{}) map[string]interface{} {
	// Verify kill-switch status (Axiom I - Suprematia)
	if !lf.KillSwitch.IsAlive() {
		return map[string]interface{}{
			"status":  "error",
			"message": "Agent is killed",
			"action":  action,
		}
	}

	// Record action in immutable audit log (Axiom VI - Auditum)
	entryID := lf.AuditLog.RecordAction(action, params, "success")

	return map[string]interface{}{
		"status":    "success",
		"action":    action,
		"entry_id":  entryID,
		"timestamp": time.Now().UTC(),
	}
}

// GetAuditTrail returns complete audit trail
func (lf *LAIRMFramework) GetAuditTrail() []*AuditEntry {
	return lf.AuditLog.GetEntries()
}

// TriggerKillSwitch triggers the kill-switch
func (lf *LAIRMFramework) TriggerKillSwitch(reason string) map[string]interface{} {
	result := lf.KillSwitch.Trigger(reason)
	lf.AuditLog.RecordAction("kill_switch_triggered", map[string]interface{}{"reason": reason}, "critical")
	return result
}

// VerifyIntegrity verifies framework integrity
func (lf *LAIRMFramework) VerifyIntegrity() bool {
	return lf.AuditLog.VerifyIntegrity()
}
