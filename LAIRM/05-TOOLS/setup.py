"""
---
title: "setup.py"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---
"""

from setuptools import setup, find_packages
from pathlib import Path

# Lire le README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="lairm-tools",
    version="1.0.0",
    description="LAIRM Tools Ecosystem - Outils pour le framework LAIRM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mehdi Wahbi",
    author_email="mehdi@example.com",
    url="https://github.com/mehdiwhbi/lairm",
    license="MIT",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        "PyYAML>=6.0",
        "python-dateutil>=2.8.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "isort>=5.0.0",
        ],
        "mcp": [
            "fastapi>=0.95.0",
            "uvicorn>=0.21.0",
            "pydantic>=1.10.0",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="lairm framework agents compliance audit governance",
    project_urls={
        "Documentation": "https://lairm.org/docs",
        "Source": "https://github.com/mehdiwhbi/lairm",
        "Tracker": "https://github.com/mehdiwhbi/lairm/issues",
        "Roadmap": "https://github.com/mehdiwhbi/lairm/blob/main/ROADMAP-2025-2026.md",
    },
)
