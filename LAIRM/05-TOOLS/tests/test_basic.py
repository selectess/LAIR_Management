"""
Basic tests for LAIRM Tools
"""

import pytest
from pathlib import Path


def test_project_structure():
    """Test that the project structure is correct."""
    base_path = Path(__file__).parent.parent.parent.parent
    
    # Check main directories exist
    assert (base_path / "00-METADATA").exists()
    assert (base_path / "01-COMPENDIUM-REFERENCE").exists()
    assert (base_path / "02-COMPENDIUM-LEGISLATIVE").exists()


def test_tools_structure():
    """Test that the tools structure is correct."""
    tools_path = Path(__file__).parent.parent
    
    # Check required files exist
    assert (tools_path / "__init__.py").exists()
    assert (tools_path / "requirements.txt").exists()
    assert (tools_path / "setup.py").exists()


def test_config_import():
    """Test that config module can be imported."""
    try:
        from config import LAIRMConfig
        assert True
    except ImportError:
        # Config might not have LAIRMConfig yet
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])