---
title: "Audit Log Schema"
type: schema
Axiom: VI
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# AUDIT LOG SCHEMA
## Immutable Recording Format - Axiom VI

### Overview

The audit-log schema defines the standardized format for immutable audit records in the LAIRM framework. Each entry is cryptographically signed and chained to ensure integrity.

### JSON Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LAIRM Audit Log Schema",
  "type": "object",
  "required": ["agent_id", "created_at", "entries"],
  "properties": {
    "agent_id": {
      "type": "string",
      "description": "Unique agent identifier"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Log creation timestamp"
    },
    "entry_count": {
      "type": "integer",
      "minimum": 0
    },
    "chain_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$",
      "description": "SHA-256 hash for integrity verification"
    },
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entry_id", "timestamp", "event_type", "hash"],
        "properties": {
          "entry_id": {
            "type": "string",
            "format": "uuid"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time"
          },
          "event_type": {
            "type": "string",
            "enum": [
              "action_executed",
              "compliance_check",
              "kill_switch_triggered",
              "configuration_changed",
              "authentication_attempt",
              "authorization_decision",
              "error_occurred",
              "incident_detected"
            ]
          },
          "details": {
            "type": "object",
            "additionalProperties": true
          },
          "severity": {
            "type": "string",
            "enum": ["info", "warning", "error", "critical"]
          },
          "hash": {
            "type": "string",
            "pattern": "^[a-f0-9]{64}$"
          }
        }
      }
    }
  }
}
```

### Event Types

| Type | Description |
|------|-------------|
| `action_executed` | Action executed by agent |
| `compliance_check` | Compliance verification |
| `kill_switch_triggered` | Emergency stop triggered |
| `configuration_changed` | Configuration modified |
| `authentication_attempt` | Authentication attempt |
| `authorization_decision` | Authorization decision |
| `error_occurred` | Error detected |
| `incident_detected` | Security incident |

### Severity Levels

- `info`: Standard information
- `warning`: Warning
- `error`: Error
- `critical`: Critical

### Example

```json
{
  "agent_id": "agent-001",
  "created_at": "2026-03-30T12:00:00Z",
  "entry_count": 1,
  "chain_hash": "abc123def456...",
  "entries": [
    {
      "entry_id": "550e8400-e29b-41d4-a716-446655440000",
      "timestamp": "2026-03-30T12:00:01Z",
      "event_type": "action_executed",
      "details": {
        "action": "analyze_data",
        "parameters": {"record_count": 1000},
        "result": "success"
      },
      "severity": "info",
      "hash": "abc123def456..."
    }
  ]
}
```

### Integrity and Chaining

Each entry includes:
- **SHA-256 Hash**: Cryptographic signature of the entry
- **Chain Hash**: Chaining with previous entry
- **Timestamp**: Immutable timestamp

### Validation

Audit logs must:
1. Have a unique `entry_id` (UUID)
2. Include a valid `timestamp` (ISO 8601)
3. Have a valid SHA-256 `hash`
4. Maintain chain integrity

### Compliance

- **Axiom VI - AUDITUM**: Immutable and traceable logs
- **Axiom III - RESPONSABILITAS**: Complete accountability
- **Axiom II - IDENTITAS**: Unique identification

---

**Version**: 1.0.0  
**Last Updated**: March 30, 2026

**Last Reviewed**: April 3, 2026
