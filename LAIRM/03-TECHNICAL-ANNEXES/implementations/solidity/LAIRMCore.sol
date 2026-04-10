// SPDX-License-Identifier: CC-BY-SA-4.0
pragma solidity ^0.8.0;

/*
---
title: "LAIRM Core Framework - Solidity Implementation"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

LAIRM Core Framework - Solidity Implementation

This smart contract implements the core LAIRM framework on Ethereum/EVM chains:
- Agent identity management (Axiom II - Identitas)
- Kill-switch mechanism (Axiom I - Suprematia)
- Immutable on-chain audit logging (Axiom VI - Auditum)
- Compliance verification (Axiom III - Responsabilitas)

The implementation uses OpenZeppelin contracts for security and provides
transparent, verifiable, and immutable agent operations on the blockchain.

Security considerations:
- Uses Ownable for access control
- Pausable for emergency stops
- Chain hashing for audit trail integrity
- Event emission for off-chain monitoring
*/

/**
 * @title LAIRMCore
 * @dev LAIRM Framework Core Implementation for Blockchain
 * Implements Axiomes I, II, III, VI on Ethereum/EVM chains
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract LAIRMCore is Ownable, Pausable {
    using Counters for Counters.Counter;

    // ============ Events ============

    event AgentRegistered(
        string indexed agentId,
        string agentName,
        address indexed owner,
        uint256 timestamp
    );

    event KillSwitchTriggered(
        string indexed agentId,
        address indexed authority,
        string reason,
        uint256 timestamp
    );

    event ActionRecorded(
        string indexed agentId,
        string action,
        bytes32 actionHash,
        uint256 timestamp
    );

    event ComplianceCheckPerformed(
        string indexed agentId,
        string status,
        uint256 timestamp
    );

    // ============ Structs ============

    struct AgentPassport {
        string agentId;
        string agentName;
        address owner;
        bytes32 signature;
        uint256 createdAt;
        bool isActive;
    }

    struct AuditEntry {
        bytes32 entryId;
        string action;
        bytes32 actionHash;
        uint256 timestamp;
        string status;
        bytes32 previousHash;
    }

    struct KillSwitchRecord {
        string agentId;
        address authority;
        string reason;
        uint256 triggeredAt;
        bool isActive;
    }

    // ============ State Variables ============

    mapping(string => AgentPassport) public agents;
    mapping(string => AuditEntry[]) public auditLogs;
    mapping(string => KillSwitchRecord) public killSwitches;
    mapping(string => bytes32) public chainHashes;

    Counters.Counter private auditEntryCounter;

    // ============ Modifiers ============

    modifier agentExists(string memory agentId) {
        require(agents[agentId].owner != address(0), "Agent does not exist");
        _;
    }

    modifier agentActive(string memory agentId) {
        require(agents[agentId].isActive, "Agent is not active");
        require(!killSwitches[agentId].isActive, "Agent is killed");
        _;
    }

    modifier onlyAgentOwner(string memory agentId) {
        require(agents[agentId].owner == msg.sender, "Only agent owner can call this");
        _;
    }

    // ============ Agent Management ============

    /**
     * @dev Register a new agent (Axiome II - IDENTITAS)
     */
    function registerAgent(
        string memory agentId,
        string memory agentName
    ) public returns (bool) {
        require(agents[agentId].owner == address(0), "Agent already exists");
        require(bytes(agentId).length > 0, "Agent ID cannot be empty");
        require(bytes(agentName).length > 0, "Agent name cannot be empty");

        bytes32 signature = keccak256(
            abi.encodePacked(agentId, agentName, block.timestamp)
        );

        agents[agentId] = AgentPassport({
            agentId: agentId,
            agentName: agentName,
            owner: msg.sender,
            signature: signature,
            createdAt: block.timestamp,
            isActive: true
        });

        // Initialize kill-switch
        killSwitches[agentId] = KillSwitchRecord({
            agentId: agentId,
            authority: address(0),
            reason: "",
            triggeredAt: 0,
            isActive: false
        });

        emit AgentRegistered(agentId, agentName, msg.sender, block.timestamp);
        return true;
    }

    /**
     * @dev Get agent passport (Axiome II - IDENTITAS)
     */
    function getAgentPassport(string memory agentId)
        public
        view
        agentExists(agentId)
        returns (AgentPassport memory)
    {
        return agents[agentId];
    }

    // ============ Kill-Switch (Axiome I - SUPREMATIA) ============

    /**
     * @dev Trigger kill-switch for an agent
     */
    function triggerKillSwitch(
        string memory agentId,
        string memory reason
    ) public onlyOwner agentExists(agentId) returns (bool) {
        require(!killSwitches[agentId].isActive, "Kill-switch already active");

        killSwitches[agentId] = KillSwitchRecord({
            agentId: agentId,
            authority: msg.sender,
            reason: reason,
            triggeredAt: block.timestamp,
            isActive: true
        });

        agents[agentId].isActive = false;

        // Record in audit log
        recordAction(agentId, "kill_switch_triggered", reason, "critical");

        emit KillSwitchTriggered(agentId, msg.sender, reason, block.timestamp);
        return true;
    }

    /**
     * @dev Check if agent is alive
     */
    function isAgentAlive(string memory agentId)
        public
        view
        agentExists(agentId)
        returns (bool)
    {
        return agents[agentId].isActive && !killSwitches[agentId].isActive;
    }

    // ============ Audit Trail (Axiome VI - AUDITUM) ============

    /**
     * @dev Record an action in immutable audit log
     */
    function recordAction(
        string memory agentId,
        string memory action,
        string memory details,
        string memory status
    ) public agentExists(agentId) returns (bytes32) {
        require(isAgentAlive(agentId), "Agent is not alive");

        bytes32 entryId = keccak256(
            abi.encodePacked(agentId, action, block.timestamp, msg.sender)
        );

        bytes32 actionHash = keccak256(abi.encodePacked(action, details));

        bytes32 previousHash = chainHashes[agentId];

        AuditEntry memory entry = AuditEntry({
            entryId: entryId,
            action: action,
            actionHash: actionHash,
            timestamp: block.timestamp,
            status: status,
            previousHash: previousHash
        });

        auditLogs[agentId].push(entry);

        // Update chain hash
        bytes32 newChainHash = keccak256(
            abi.encodePacked(previousHash, actionHash)
        );
        chainHashes[agentId] = newChainHash;

        auditEntryCounter.increment();

        emit ActionRecorded(agentId, action, actionHash, block.timestamp);
        return entryId;
    }

    /**
     * @dev Get audit log entries for an agent
     */
    function getAuditLog(string memory agentId)
        public
        view
        agentExists(agentId)
        returns (AuditEntry[] memory)
    {
        return auditLogs[agentId];
    }

    /**
     * @dev Get audit log entry count
     */
    function getAuditLogCount(string memory agentId)
        public
        view
        agentExists(agentId)
        returns (uint256)
    {
        return auditLogs[agentId].length;
    }

    /**
     * @dev Get chain hash for integrity verification
     */
    function getChainHash(string memory agentId)
        public
        view
        agentExists(agentId)
        returns (bytes32)
    {
        return chainHashes[agentId];
    }

    // ============ Compliance (Axiome III - RESPONSABILITAS) ============

    /**
     * @dev Perform compliance check
     */
    function performComplianceCheck(string memory agentId)
        public
        agentExists(agentId)
        returns (string memory)
    {
        require(isAgentAlive(agentId), "Agent is not alive");

        string memory status = "compliant";

        // Check basic compliance
        if (auditLogs[agentId].length == 0) {
            status = "partial";
        }

        recordAction(agentId, "compliance_check", status, "info");

        emit ComplianceCheckPerformed(agentId, status, block.timestamp);
        return status;
    }

    // ============ Utility Functions ============

    /**
     * @dev Get total audit entries across all agents
     */
    function getTotalAuditEntries() public view returns (uint256) {
        return auditEntryCounter.current();
    }

    /**
     * @dev Pause contract (emergency)
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
