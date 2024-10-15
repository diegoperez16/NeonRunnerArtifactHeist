# Title screen / main menu - work in progress
import pygame
from .constants import NEON_CYAN, COLOR_BG, WINDOW_WIDTH, WINDOW_HEIGHT


class Menu:
    """Title screen shown before the game starts."""

    def __init__(self, screen):
        self.screen = screen
        self.active = True

    def draw(self):
        # TODO: implement title screen layout
        self.screen.fill(COLOR_BG)

    def handle_event(self, event):
        """Return True when the player presses start."""
        return False
