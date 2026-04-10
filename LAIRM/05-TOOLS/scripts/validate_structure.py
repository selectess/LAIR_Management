#!/usr/bin/env python3
"""
LAIRM Structure Validation Script

Validates the LAIRM project structure according to the defined architecture.
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def validate_directory_structure():
    """Validate the LAIRM directory structure."""
    base_path = Path(__file__).parent.parent.parent
    
    required_dirs = [
        "00-METADATA",
        "01-COMPENDIUM-REFERENCE",
        "02-COMPENDIUM-LEGISLATIVE",
        "03-TECHNICAL-ANNEXES",
        "04-REPORTS-ANALYSES",
        "05-TOOLS",
    ]
    
    errors = []
    warnings = []
    
    # Check required directories
    for dir_name in required_dirs:
        dir_path = base_path / dir_name
        if not dir_path.exists():
            errors.append(f"Missing required directory: {dir_name}")
    
    # Check metadata files
    metadata_path = base_path / "00-METADATA"
    required_metadata = ["README.md", "INTRODUCTION.md", "glossary.md"]
    
    for file_name in required_metadata:
        file_path = metadata_path / file_name
        if not file_path.exists():
            warnings.append(f"Missing metadata file: {file_name}")
    
    # Check legislative compendium
    legislative_path = base_path / "02-COMPENDIUM-LEGISLATIVE"
    if legislative_path.exists():
        axiom_dirs = list(legislative_path.glob("AXIOM-*"))
        if len(axiom_dirs) < 19:
            warnings.append(f"Expected 19 axiom directories, found {len(axiom_dirs)}")
    
    # Generate report
    report = generate_report(errors, warnings)
    
    # Write report
    report_path = base_path / "validation_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(report)
    
    return len(errors) == 0


def generate_report(errors, warnings):
    """Generate validation report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# LAIRM Structure Validation Report

**Generated**: {timestamp}

## Summary

| Status | Count |
|--------|-------|
| Errors | {len(errors)} |
| Warnings | {len(warnings)} |

"""
    
    if errors:
        report += "## Errors\n\n"
        for error in errors:
            report += f"- ❌ {error}\n"
        report += "\n"
    
    if warnings:
        report += "## Warnings\n\n"
        for warning in warnings:
            report += f"- ⚠️ {warning}\n"
        report += "\n"
    
    if not errors and not warnings:
        report += "## Result\n\n✅ All validations passed!\n"
    elif not errors:
        report += "## Result\n\n✅ No critical errors found.\n"
    else:
        report += "## Result\n\n❌ Validation failed with errors.\n"
    
    return report


if __name__ == "__main__":
    success = validate_directory_structure()
    sys.exit(0 if success else 1)