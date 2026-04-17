---
title: "Article III.3.15: Public Incident Registry"
axiom: Ψ-III
article_number: III.3.15
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
tags:
  - registry
  - incidents
  - transparency
validations:
  legal: true
  technical: true
  editorial: true
license: CC-BY-SA-4.0
---

# Article III.3.15: PUBLIC INCIDENT REGISTRY
## Axiom Ψ-III: RESPONSABILITAS JURIDICA

---

## 1. IMPERATIVE NORM

A public incident registry MUST be maintained for all autonomous agents. Each incident causing damage MUST be recorded and published. The registry MUST be publicly accessible and immutable. Citizens MUST be able to consult the incident history.

**Minimum Requirements**:
- Public registry established
- All incidents recorded
- Public accessibility
- Data immutability
- Regular updates

---

## 2. LEGAL FOUNDATION

**Axiom Ψ-III: RESPONSABILITAS JURIDICA**

Transparency on incidents is essential to maintain public confidence. Citizens have the right to know the incidents caused by autonomous agents.

**Fundamental Principles**:
- Right to information
- Complete transparency
- Public accessibility
- Data immutability
- Public Responsibility

---

## 3. TECHNICAL SPECIFICATION

### 3.1 Incident Recording

```python
class IncidentRegistry:
    def register_incident(self, agent_id, incident_data):
        """Record an incident"""
        incident = {
            'incident_id': str(uuid.uuid4()),
            'agent_id': agent_id,
            'date': incident_data['date'],
            'type': incident_data['type'],
            'severity': incident_data['severity'],
            'description': incident_data['description'],
            'damages': incident_data.get('damages', 0),
            'victims': incident_data.get('victims', 0),
            'registered_date': datetime.utcnow().isoformat(),
            'status': 'registered',
            'public': True
        }
        
        return incident
    
    def publish_incident(self, incident_id):
        """Publish an incident"""
        incident = self.get_incident(incident_id)
        
        incident['published_date'] = datetime.utcnow().isoformat()
        incident['public_url'] = f"https://registry.lairm.org/incidents/{incident_id}"
        incident['status'] = 'published'
        
        return incident
```

### 3.2 Incident Categories

| Category | Severity | Typical Damages |
|----------|----------|-----------------|
| Minor | 1 | <10k€ |
| Moderate | 2 | 10k-100k€ |
| Serious | 3 | 100k-1M€ |
| Critical | 4 | >1M€ |

### 3.3 Mandatory Information

Each incident MUST include:
- Unique ID
- Responsible agent
- Date and time
- Incident type
- Severity
- Description
- Estimated damages
- Number of victims
- Resolution status

---

## 4. REFERENCE IMPLEMENTATION

### 4.1 Recording Process

```
┌──────────────────────────────────────┐
│      Incident Occurs                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Collect Information                 │
│  - Incident type                     │
│  - Severity                          │
│  - Damages                           │
│  - Victims                           │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Record Incident                     │
│  - Generate unique ID                │
│  - Digital signature                 │
│  - UTC timestamp                     │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Publish in Registry                 │
│  - Public registry                   │
│  - Immutable and signed              │
│  - Accessible to all                 │
└────────────┬─────────────────────────┘
             │
             ▼
┌──────────────────────────────────────┐
│  Archive Incident                    │
│  - Complete history                  │
│  - Search available                  │
│  - Permanent access                  │
└──────────────────────────────────────┘
```

### 4.2 Public Registry

The public registry MUST allow:
- Search by agent
- Search by date
- Search by type
- Filter by severity
- Data download

---

## 5. VERIFICATION & SANCTIONS

### 5.1 Compliance Verification

**Mandatory tests**:
1. Verify all incidents recorded
2. Verify public registry accessible
3. Verify data immutability
4. Verify information completeness
5. Verify no hidden incidents

**Frequency**: Minimum monthly

### 5.2 Sanctions for Non-Compliance

| Violation | Sanction |
|-----------|----------|
| Incident not recorded | 25% annual revenue fine |
| Registry not public | 20% annual revenue fine |
| Data modified | License revocation |
| Incomplete information | 15% annual revenue fine |
| Hidden incident | Immediate revocation |
| Recurrence | Permanent ban |

### 5.3 Verification Process

1. Monthly registry audit
2. Accessibility verification
3. Immutability verification
4. Completeness audit
5. Public compliance report

---

## 6. EFFECTIVE DATE

**Effective date**: January 1, 2027

**Compliance calendar**:
- Registry established: January 1, 2027
- All incidents recorded: January 1, 2027
- Public registry: January 1, 2027

**Transitional provisions**:
- Prior incidents: Retroactive recording before June 30, 2027
- Temporary registry established before January 1, 2027

---

## REFERENCES

- Axiom Ψ-III: RESPONSABILITAS JURIDICA
- Article III.3.10: Responsibility Transparency
- Article III.3.15: Public Incident Registry
- Chapter 12: Responsibility Paradigm

---

**Status**: Final


---

**Next review**: June 2026
