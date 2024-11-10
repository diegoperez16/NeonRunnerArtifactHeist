# Title screen / main menu
import pygame
from .constants import (
    NEON_CYAN, NEON_PURPLE, COLOR_BG,
    WINDOW_WIDTH, WINDOW_HEIGHT,
)


class Menu:
    """Title screen shown before the game starts."""

    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont('monospace', 56, bold=True)
        self.font_sub   = pygame.font.SysFont('monospace', 22)
        self.font_hint  = pygame.font.SysFont('monospace', 16)
        self.active = True

    def draw(self):
        self.screen.fill(COLOR_BG)
        cx = WINDOW_WIDTH // 2

        title = self.font_title.render("NEON RUNNER", True, NEON_CYAN)
        sub   = self.font_sub.render("Artifact Heist", True, NEON_PURPLE)
        hint  = self.font_hint.render("Press ENTER to start", True, (100, 100, 140))

        self.screen.blit(title, (cx - title.get_width() // 2, 180))
        self.screen.blit(sub,   (cx - sub.get_width()   // 2, 258))
        self.screen.blit(hint,  (cx - hint.get_width()  // 2, 340))

    def handle_event(self, event):
        """Return True when the player presses start."""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.active = False
            return True
        return False
