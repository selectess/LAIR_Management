---
title: "Kill-Signal Schema"
type: schema
Axiom: I
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# KILL-SIGNAL SCHEMA
## Emergency Stop Signal - Axiom I

### Overview

The kill-signal schema defines the standardized format for universal emergency stop signals. This signal guarantees the shutdown of any autonomous agent in less than 500ms.

### JSON Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LAIRM Kill-Signal Schema",
  "type": "object",
  "required": [
    "type",
    "version",
    "timestamp",
    "agent_id",
    "authority",
    "signature"
  ],
  "properties": {
    "type": {
      "type": "string",
      "const": "kill-switch",
      "description": "Signal type"
    },
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+$",
      "description": "Protocol version"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Signal timestamp"
    },
    "signal_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique signal identifier"
    },
    "agent_id": {
      "type": "string",
      "description": "Target agent (or '*' for all)"
    },
    "authority": {
      "type": "string",
      "description": "Signal issuing authority"
    },
    "reason": {
      "type": "string",
      "description": "Reason for shutdown"
    },
    "priority": {
      "type": "string",
      "enum": ["normal", "urgent", "critical"],
      "description": "Signal priority"
    },
    "signature": {
      "type": "string",
      "description": "ECDSA signature of signal"
    },
    "nonce": {
      "type": "string",
      "description": "Nonce to prevent replay"
    },
    "channels": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["websocket", "http", "signal", "network"]
      },
      "description": "Transmission channels"
    }
  }
}
```

### Example

```json
{
  "type": "kill-switch",
  "version": "1.0",
  "timestamp": "2026-03-30T12:00:00Z",
  "signal_id": "550e8400-e29b-41d4-a716-446655440000",
  "agent_id": "agent-001",
  "authority": "human-controller-001",
  "reason": "Security incident detected",
  "priority": "critical",
  "signature": "ECDSA_SIGNATURE_HERE",
  "nonce": "abc123def456",
  "channels": ["websocket", "http", "signal"]
}
```

### Transmission Channels

| Channel | Latency | Reliability |
|---------|---------|-------------|
| WebSocket | <100ms | High |
| HTTP/2 | <200ms | Medium |
| System signal | <50ms | Very high |
| Network cutoff | <500ms | Fallback |

### Authentication

- **X.509 Certificate** for authority
- **ECDSA Signature** of signal
- **Nonce** to prevent replay
- **Timestamp** for temporal validation

### Compliance

- **Axiom I - SUPREMATIA**: Guaranteed shutdown < 500ms
- **Axiom II - IDENTITAS**: Unique identification
- **Axiom VI - AUDITUM**: Complete traceability

---

**Version**: 1.0.0  
**Last Updated**: March 30, 2026

**Last Reviewed**: April 3, 2026
