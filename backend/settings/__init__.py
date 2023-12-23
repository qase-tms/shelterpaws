from importlib import import_module
from os import environ

from backend.settings.base_settings import BaseSettings

env = environ.get("ENV_TYPE", "local")
module = import_module(name=f"backend.settings.{env}")
Settings = module.Settings

__all__ = [
    "BaseSettings",
    "Settings",
]
