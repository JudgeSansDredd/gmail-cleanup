"""A centralized location for version bumping"""

from pathlib import Path

APP_NAME = "Gmail Cleanup"
VERSION = "1.1.0"
CONFIG_PATH = Path(f"{Path.home()}/.gmail-cleanup/config.ini")
