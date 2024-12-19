"""Handles setting up whiptail for terminal usage"""

import os

from whiptail import Whiptail

from config.settings import APP_NAME, VERSION

TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

WHIPTAIL_SETTINGS = {
    "title": f"{APP_NAME} ({VERSION})",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10,
}

wt = Whiptail(**WHIPTAIL_SETTINGS)


def input_box(question: str, default=""):
    """Prompt user for an input given a question"""
    value, response = wt.inputbox(question, default)
    return False if response == 1 else value
