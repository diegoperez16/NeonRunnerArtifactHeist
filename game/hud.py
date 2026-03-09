import pygame
from .constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    PLAYER_START_HEALTH,
    NEON_CYAN, NEON_RED, NEON_GOLD,
)


class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font_large  = pygame.font.SysFont('monospace', 28, bold=True)
        self.font_medium = pygame.font.SysFont('monospace', 20)
        self.font_small  = pygame.font.SysFont('monospace', 14)

    def draw(self, player, game_time):
        bar = pygame.Surface((WINDOW_WIDTH, 74), pygame.SRCALPHA)
        bar.fill((6, 6, 16, 215))
        self.screen.blit(bar, (0, 0))

        score_surf = self.font_large.render(f"SCORE  {player.score}", True, NEON_CYAN)
        self.screen.blit(score_surf, (16, 10))

        bx, by, bw, bh = 16, 48, 210, 14
        hp_pct = max(0.0, player.health / PLAYER_START_HEALTH)
        bar_color = (60, 210, 80) if hp_pct > 0.5 else (230, 180, 0) if hp_pct > 0.25 else NEON_RED

        pygame.draw.rect(self.screen, (28, 28, 48), (bx, by, bw, bh), border_radius=3)
        if hp_pct > 0:
            pygame.draw.rect(self.screen, bar_color,
                             (bx, by, int(bw * hp_pct), bh), border_radius=3)
        pygame.draw.rect(self.screen, (65, 65, 95), (bx, by, bw, bh), width=1, border_radius=3)

        hp_label = self.font_small.render(f"HP  {player.health}", True, (185, 185, 205))
        self.screen.blit(hp_label, (bx + bw + 10, by))

        timer_surf = self.font_large.render(f"{int(game_time):03d}s", True, (135, 135, 195))
        self.screen.blit(timer_surf, (WINDOW_WIDTH - timer_surf.get_width() - 16, 10))

        ammo_surf = self.font_medium.render(f"AMMO  {player.ammo}", True, NEON_GOLD)
        self.screen.blit(ammo_surf, (WINDOW_WIDTH // 2 - ammo_surf.get_width() // 2, 14))

        hint = self.font_small.render(
            "WASD / arrows to move   |   aim with mouse   |   click / SPACE to fire   |   Q to quit", True, (48, 48, 68))
        self.screen.blit(hint, (WINDOW_WIDTH // 2 - hint.get_width() // 2, WINDOW_HEIGHT - 18))

    def draw_game_over(self, score, game_time):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        font_big   = pygame.font.SysFont('monospace', 64, bold=True)
        font_med   = pygame.font.SysFont('monospace', 24)
        font_small = pygame.font.SysFont('monospace', 18)

        title = font_big.render("GAME OVER", True, NEON_RED)
        self.screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, WINDOW_HEIGHT // 2 - 95))

        info = font_med.render(f"Score: {score}     Time: {int(game_time)}s", True, NEON_CYAN)
        self.screen.blit(info, (WINDOW_WIDTH // 2 - info.get_width() // 2, WINDOW_HEIGHT // 2 - 5))

        restart = font_small.render("Press  R  to restart     Q  to quit", True, (160, 160, 185))
        self.screen.blit(restart, (WINDOW_WIDTH // 2 - restart.get_width() // 2, WINDOW_HEIGHT // 2 + 48))
