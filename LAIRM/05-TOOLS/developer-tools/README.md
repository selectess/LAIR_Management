---
title: "Developer Tools LAIRM"
type: component
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---

# DEVELOPER TOOLS LAIRM
## Tools for Contributors and Developers

### Description

The Developer Tools provide a CLI interface and utilities for contributors and developers working with the LAIRM framework.

### Files

- `lairm_cli.py` - Main CLI interface (250+ lines)
- `README.md` - This documentation

### Features

#### CLI Commands

1. **lairm validate**
   - Validate LAIRM structure
   - Verify all articles
   - Generate validation report

2. **lairm search**
   - Search articles
   - Filter by axiom, status
   - Display results

3. **lairm get-article**
   - Retrieve complete article
   - Display metadata
   - Display content

4. **lairm compliance**
   - Verify compliance
   - Generate report
   - Display violations

5. **lairm audit**
   - Audit framework
   - Verify integrity
   - Generate audit report

6. **lairm generate**
   - Generate reports
   - Generate documentation
   - Generate statistics

### Usage

#### Validation

```bash
# Validate complete structure
lairm validate

# Validate specific axiom
lairm validate --axiom I

# Validate with detailed report
lairm validate --verbose

# Save report
lairm validate --output validation_report.json
```

#### Search

```bash
# Search articles
lairm search "kill-switch"

# Search by axiom
lairm search --axiom I

# Search by status
lairm search --status Enriched

# Search with multiple filters
lairm search "supervision" --axiom II --status Enriched

# Limit results
lairm search "agent" --limit 10
```

#### Retrieve Article

```bash
# Retrieve article
lairm get-article I-01-01

# Display with metadata
lairm get-article I-01-01 --metadata

# Display with links
lairm get-article I-01-01 --links

# Export to Markdown
lairm get-article I-01-01 --output article.md
```

#### Verify Compliance

```bash
# Verify global compliance
lairm compliance

# Verify specific agent
lairm compliance --agent agent-001

# Verify axiom
lairm compliance --axiom I

# Generate detailed report
lairm compliance --verbose --output compliance_report.json
```

#### Audit Framework

```bash
# Audit complete framework
lairm audit

# Audit specific agent
lairm audit --agent agent-001

# Verify integrity
lairm audit --verify-chain

# Generate audit report
lairm audit --output audit_report.json
```

#### Generate Reports

```bash
# Generate compliance report
lairm generate --type compliance

# Generate audit report
lairm generate --type audit

# Generate documentation
lairm generate --type documentation

# Generate statistics
lairm generate --type statistics

# Generate all reports
lairm generate --all
```

### Complete Examples

#### Validation Workflow

```bash
# 1. Validate structure
lairm validate

# 2. Search specific articles
lairm search "kill-switch" --axiom I

# 3. Retrieve article
lairm get-article I-01-01

# 4. Verify compliance
lairm compliance --verbose

# 5. Audit framework
lairm audit --verify-chain

# 6. Generate complete report
lairm generate --all --output reports/
```

#### Development Workflow

```bash
# 1. Search relevant articles
lairm search "agent_supervision"

# 2. Retrieve articles
lairm get-article II-02-05
lairm get-article III-03-01

# 3. Verify compliance
lairm compliance --axiom II --axiom III

# 4. Generate documentation
lairm generate --type documentation --output docs/

# 5. Audit changes
lairm audit --agent my-agent
```

### Configuration

File `.lairm/config.yaml`:

```yaml
cli:
  verbose: false
  output_format: json
  
search:
  max_results: 100
  timeout: 30
  
validation:
  strict_mode: true
  check_links: true
  
audit:
  verify_chain: true
  generate_report: true
```

### Output

#### JSON Format
```json
{
  "status": "success",
  "data": [...],
  "timestamp": "2026-03-30T10:30:00Z"
}
```

#### Text Format
```
✓ Validation successful
  - Total articles: 399
  - Valid: 399
  - Invalid: 0
  - Score: 100/100
```

### Performance

- Validation: ~2s (399 articles)
- Search: ~100ms
- Article retrieval: ~10ms
- Compliance: ~500ms
- Audit: ~1s

### Status

- **Implementation** : ✅ Complete
- **Tests** : ✅ Passed
- **Production** : ✅ Ready

### Contributors

- Mehdi Wahbi (Founder)

---

**Version** : 1.0.0-final

