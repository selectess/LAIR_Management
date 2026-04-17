---
title: "Action Record Schema"
type: schema
axiom: III
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# ACTION RECORD SCHEMA
## Agent Action Recording Format - Axiom III

### Overview

The action-record schema defines the standardized format for recording actions executed by autonomous agents. Each action is documented with complete context for accountability.

### JSON Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LAIRM Action Record Schema",
  "type": "object",
  "required": [
    "action_id",
    "agent_id",
    "timestamp",
    "action_type",
    "status"
  ],
  "properties": {
    "action_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique action identifier"
    },
    "agent_id": {
      "type": "string",
      "description": "Agent that executed the action"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Action timestamp"
    },
    "action_type": {
      "type": "string",
      "description": "Type of action executed"
    },
    "description": {
      "type": "string",
      "description": "Detailed action description"
    },
    "parameters": {
      "type": "object",
      "description": "Action input parameters",
      "additionalProperties": true
    },
    "result": {
      "type": "object",
      "description": "Action result",
      "properties": {
        "status": {
          "type": "string",
          "enum": ["success", "failure", "partial", "timeout"]
        },
        "output": {
          "type": "object",
          "additionalProperties": true
        },
        "error": {
          "type": "string"
        }
      }
    },
    "status": {
      "type": "string",
      "enum": ["pending", "executing", "completed", "failed", "cancelled"],
      "description": "Action status"
    },
    "duration_ms": {
      "type": "integer",
      "minimum": 0,
      "description": "Execution duration in milliseconds"
    },
    "compliance": {
      "type": "object",
      "description": "Compliance verification",
      "properties": {
        "axioms_checked": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "compliant": {
          "type": "boolean"
        },
        "violations": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "authorization": {
      "type": "object",
      "description": "Authorization information",
      "properties": {
        "authorized_by": {
          "type": "string"
        },
        "authorization_timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "authorization_level": {
          "type": "string",
          "enum": ["user", "admin", "system"]
        }
      }
    },
    "audit_trail": {
      "type": "array",
      "description": "Action audit trail",
      "items": {
        "type": "object",
        "properties": {
          "timestamp": {
            "type": "string",
            "format": "date-time"
          },
          "event": {
            "type": "string"
          },
          "details": {
            "type": "object",
            "additionalProperties": true
          }
        }
      }
    },
    "impact": {
      "type": "object",
      "description": "Action impact",
      "properties": {
        "resources_affected": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "data_modified": {
          "type": "boolean"
        },
        "risk_level": {
          "type": "string",
          "enum": ["low", "medium", "high", "critical"]
        }
      }
    },
    "hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$",
      "description": "SHA-256 hash for integrity"
    }
  }
}
```

### Example

```json
{
  "action_id": "550e8400-e29b-41d4-a716-446655440000",
  "agent_id": "agent-001",
  "timestamp": "2026-03-30T12:00:00Z",
  "action_type": "data_analysis",
  "description": "Analyze customer data for patterns",
  "parameters": {
    "dataset": "customers_2026",
    "analysis_type": "clustering",
    "threshold": 0.8
  },
  "result": {
    "status": "success",
    "output": {
      "clusters_found": 5,
      "confidence": 0.92
    }
  },
  "status": "completed",
  "duration_ms": 2500,
  "compliance": {
    "axioms_checked": ["I", "II", "III", "VI"],
    "compliant": true,
    "violations": []
  },
  "authorization": {
    "authorized_by": "user-001",
    "authorization_timestamp": "2026-03-30T11:59:00Z",
    "authorization_level": "user"
  },
  "impact": {
    "resources_affected": ["database-001"],
    "data_modified": false,
    "risk_level": "low"
  },
  "hash": "abc123def456..."
}
```

### Action Statuses

| Status | Meaning |
|--------|---------|
| `pending` | Awaiting execution |
| `executing` | Currently executing |
| `completed` | Completed successfully |
| `failed` | Failed |
| `cancelled` | Cancelled |

### Risk Levels

- `low` : Low risk
- `medium` : Medium risk
- `high` : High risk
- `critical` : Critical risk

### Compliance

- **Axiom III - RESPONSABILITAS** : Complete accountability
- **Axiom VI - AUDITUM** : Complete traceability
- **Axiom I - SUPREMATIA** : Human supervision

---

**Version** : 1.0.0  

