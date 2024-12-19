"""Handles fetching config information from user"""

import os
from configparser import ConfigParser

from terminal.whiptail import input_box

VERSION = "1.1.0"

TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

WHIPTAIL_SETTINGS = {
    "title": f"Testify ({VERSION})",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10,
}


def get_configuration(config_path):
    """
    Ensures that configuration for the use of Jira has been done.
    Returns true on a success, false on cancellation.
    """

    # Get the config object as it exists
    config = ConfigParser()
    config.read(config_path)

    config_items = {
        "GMAIL": [
            "CLIENT_ID",
            "CLIENT_SECRET",
        ]
    }

    # Set up config and prompt if needed
    for section, options in config_items.items():
        if not config.has_section(section):
            config.add_section(section)
        for option in options:
            if not config.has_option(section, option):
                response = input_box(f"Enter value for: {option}")
                if not response:
                    return False
                config.set(section, option, response)

    # Make sure the .testify directory exists
    config_path.parents[0].mkdir(parents=True, exist_ok=True)
    with open(config_path, "w", encoding="UTF-8") as conf:
        config.write(conf)

    return True
