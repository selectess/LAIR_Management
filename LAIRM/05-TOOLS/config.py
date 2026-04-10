"""
---
title: "config.py"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---
"""

import os
from pathlib import Path
from typing import Optional


class Config:
    """Configuration centralisée LAIRM"""

    # Paths
    LAIRM_ROOT = os.getenv("LAIRM_ROOT", "LAIRM")
    ARTICLES_PATH = os.path.join(LAIRM_ROOT, "02-COMPENDIUM-LEGISLATIF")
    SCHEMAS_PATH = os.path.join(LAIRM_ROOT, "03-ANNEXES-TECHNIQUES", "schemas")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Cache
    CACHE_ENABLED = os.getenv("CACHE_ENABLED", "True").lower() == "true"
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))  # 1 hour
    CACHE_MAX_SIZE = int(os.getenv("CACHE_MAX_SIZE", "128"))

    # Performance
    MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))
    TIMEOUT = int(os.getenv("TIMEOUT", "30"))  # seconds

    # Compliance
    STRICT_MODE = os.getenv("STRICT_MODE", "True").lower() == "true"
    MIN_COMPLIANCE_SCORE = float(os.getenv("MIN_COMPLIANCE_SCORE", "70"))

    # Audit
    AUDIT_ENABLED = os.getenv("AUDIT_ENABLED", "True").lower() == "true"
    AUDIT_RETENTION_DAYS = int(os.getenv("AUDIT_RETENTION_DAYS", "365"))

    # MCP Server
    MCP_HOST = os.getenv("MCP_HOST", "localhost")
    MCP_PORT = int(os.getenv("MCP_PORT", "8000"))
    MCP_DEBUG = os.getenv("MCP_DEBUG", "False").lower() == "true"

    # Workflow
    WORKFLOW_TIMEOUT = int(os.getenv("WORKFLOW_TIMEOUT", "300"))  # 5 minutes
    WORKFLOW_MAX_RETRIES = int(os.getenv("WORKFLOW_MAX_RETRIES", "3"))

    @classmethod
    def validate(cls) -> bool:
        """Valider la configuration"""
        if not Path(cls.LAIRM_ROOT).exists():
            raise ValueError(f"LAIRM_ROOT path does not exist: {cls.LAIRM_ROOT}")
        if not Path(cls.ARTICLES_PATH).exists():
            raise ValueError(f"ARTICLES_PATH does not exist: {cls.ARTICLES_PATH}")
        return True

    @classmethod
    def to_dict(cls) -> dict:
        """Convertir la configuration en dictionnaire"""
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if not key.startswith("_") and key.isupper()
        }

    @classmethod
    def get(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        """Obtenir une valeur de configuration"""
        return getattr(cls, key, default)


# Configuration par environnement
class DevelopmentConfig(Config):
    """Configuration pour développement"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    STRICT_MODE = False


class ProductionConfig(Config):
    """Configuration pour production"""
    DEBUG = False
    LOG_LEVEL = "INFO"
    STRICT_MODE = True
    CACHE_ENABLED = True


class TestingConfig(Config):
    """Configuration pour tests"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    CACHE_ENABLED = False
    AUDIT_ENABLED = False


# Sélectionner la configuration
ENV = os.getenv("LAIRM_ENV", "development").lower()

if ENV == "production":
    config = ProductionConfig()
elif ENV == "testing":
    config = TestingConfig()
else:
    config = DevelopmentConfig()
