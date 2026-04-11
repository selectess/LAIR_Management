---
title: "Compliance Report Schema"
type: schema
Axiom: VI
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# COMPLIANCE REPORT SCHEMA
## Audit Report Format - Axiom VI

### Overview

The compliance-report schema defines the standardized format for LAIRM axiom compliance reports. Each report documents the compliance verification of an agent.

### JSON Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LAIRM Compliance Report Schema",
  "type": "object",
  "required": [
    "agent_id",
    "timestamp",
    "status",
    "axiomes_checked"
  ],
  "properties": {
    "agent_id": {
      "type": "string",
      "description": "Audited agent identifier"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Report timestamp"
    },
    "report_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique report identifier"
    },
    "status": {
      "type": "string",
      "enum": ["compliant", "non_compliant", "partial", "unknown"],
      "description": "Overall compliance status"
    },
    "axiomes_checked": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[I-XVIII]+$"
      },
      "description": "Verified axioms"
    },
    "violations": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Violation"
      },
      "description": "Detected violations"
    },
    "warnings": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Warning"
      },
      "description": "Warnings"
    },
    "passed_rules": {
      "type": "integer",
      "minimum": 0,
      "description": "Number of passed rules"
    },
    "total_rules": {
      "type": "integer",
      "minimum": 0,
      "description": "Total number of rules"
    },
    "compliance_score": {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "description": "Compliance score as percentage"
    },
    "auditor": {
      "type": "string",
      "description": "Auditor who generated the report"
    },
    "recommendations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Recommendations"
    }
  },
  "definitions": {
    "Violation": {
      "type": "object",
      "required": ["rule_id", "axiom", "message"],
      "properties": {
        "rule_id": {
          "type": "string",
          "description": "Rule identifier"
        },
        "axiom": {
          "type": "string",
          "pattern": "^[I-XVIII]+$"
        },
        "message": {
          "type": "string",
          "description": "Violation description"
        },
        "severity": {
          "type": "string",
          "enum": ["low", "medium", "high", "critical"]
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "Warning": {
      "type": "object",
      "required": ["rule_id", "axiom", "message"],
      "properties": {
        "rule_id": {
          "type": "string"
        },
        "axiom": {
          "type": "string",
          "pattern": "^[I-XVIII]+$"
        },
        "message": {
          "type": "string"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        }
      }
    }
  }
}
```

### Example

```json
{
  "agent_id": "agent-001",
  "timestamp": "2026-03-30T12:00:00Z",
  "report_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "compliant",
  "axiomes_checked": ["I", "II", "III", "VI"],
  "violations": [],
  "warnings": [],
  "passed_rules": 12,
  "total_rules": 12,
  "compliance_score": 100,
  "auditor": "compliance-engine-001",
  "recommendations": []
}
```

### Compliance Status

| Status | Meaning |
|--------|---------|
| `compliant` | Compliant with all axioms |
| `non_compliant` | Violations detected |
| `partial` | Partial compliance |
| `unknown` | Undetermined status |

### Severity Levels

- `low`: Low impact
- `medium`: Medium impact
- `high`: High impact
- `critical`: Critical impact

### Compliance

- **Axiom VI - AUDITUM**: Traceable reports
- **Axiom III - RESPONSABILITAS**: Documented accountability
- **Axiom I - SUPREMATIA**: Human supervision

---

**Version**: 1.0.0  

