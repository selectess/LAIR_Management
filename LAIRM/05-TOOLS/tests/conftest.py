# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Pytest configuration for LAIRM tests
Adds parent directory to path for imports
"""

import sys
from pathlib import Path

# Add parent directory to path so imports work
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
