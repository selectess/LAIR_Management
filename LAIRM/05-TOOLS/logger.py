"""
---
title: "logger.py"
type: Implementation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
license: CC-BY-SA-4.0
---
"""

import logging
import sys
from typing import Optional


class LAIRMLogger:
    """Logger structuré pour LAIRM"""

    _loggers = {}

    @staticmethod
    def get_logger(name: str, level: Optional[str] = None) -> logging.Logger:
        """Obtenir un logger configuré"""
        if name in LAIRMLogger._loggers:
            return LAIRMLogger._loggers[name]

        logger = logging.getLogger(name)

        # Éviter les doublons
        if logger.handlers:
            return logger

        # Handler
        handler = logging.StreamHandler(sys.stdout)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)

        # Level
        if level:
            logger.setLevel(getattr(logging, level.upper(), logging.INFO))
        else:
            logger.setLevel(logging.INFO)

        logger.addHandler(handler)

        LAIRMLogger._loggers[name] = logger
        return logger

    @staticmethod
    def set_level(name: str, level: str) -> None:
        """Définir le niveau de log"""
        logger = LAIRMLogger.get_logger(name)
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    @staticmethod
    def debug(name: str, message: str) -> None:
        """Log debug"""
        LAIRMLogger.get_logger(name).debug(message)

    @staticmethod
    def info(name: str, message: str) -> None:
        """Log info"""
        LAIRMLogger.get_logger(name).info(message)

    @staticmethod
    def warning(name: str, message: str) -> None:
        """Log warning"""
        LAIRMLogger.get_logger(name).warning(message)

    @staticmethod
    def error(name: str, message: str) -> None:
        """Log error"""
        LAIRMLogger.get_logger(name).error(message)

    @staticmethod
    def critical(name: str, message: str) -> None:
        """Log critical"""
        LAIRMLogger.get_logger(name).critical(message)


# Convenience function
def get_logger(name: str) -> logging.Logger:
    """Obtenir un logger (fonction de commodité)"""
    return LAIRMLogger.get_logger(name)
