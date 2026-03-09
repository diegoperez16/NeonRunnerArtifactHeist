import pygame
import sys
import math

from game.level import Level
from game.hud import HUD
from game.sprites import SpriteManager
from game.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    PLAYER_SPEED, TILE_SIZE, COIN_SIZE,
    NEON_CYAN, NEON_PURPLE,
)
from game.leaderboard import get_username, save_username, submit_score


def _prompt_username() -> str | None:
    """Ask for username in the terminal before the window opens."""
    saved = get_username()
    if saved:
        print(f"Welcome back, {saved}!  (press Enter to keep, or type a new name)")
        entered = input("Username: ").strip()
        name = entered if entered else saved
    else:
        print("Enter a username to track your score on the leaderboard.")
        print("(Leave blank to play anonymously)")
        name = input("Username: ").strip()

    if name:
        save_username(name)
        return name
    return None


class Game:
    def __init__(self, username: str | None):
        pygame.init()
        pygame.display.set_caption("Neon Runner: Artifact Heist")
        self.screen  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock   = pygame.time.Clock()
        self.sprites = SpriteManager()

        self.username = username
        self.running   = True
        self.game_over = False
        self.game_time = 0.0
        self._score_submitted = False

        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.game_time = 0.0
        self._score_submitted = False
        self.level = Level(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.hud   = HUD(self.screen)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self._handle_events(dt)
            if not self.game_over:
                self._update(dt)
            self._draw()
        pygame.quit()
        sys.exit()

    def _handle_events(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    self.running = False
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                elif event.key == pygame.K_SPACE and not self.game_over:
                    self.level.fire_projectile()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.game_over:
                self.level.fire_projectile()

        if not self.game_over:
            keys = pygame.key.get_pressed()
            dx = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
            dy = int(keys[pygame.K_DOWN]  or keys[pygame.K_s]) - int(keys[pygame.K_UP]   or keys[pygame.K_w])
            if dx or dy:
                self.level.player.move(
                    dx * PLAYER_SPEED * dt,
                    dy * PLAYER_SPEED * dt,
                    WINDOW_WIDTH,
                    WINDOW_HEIGHT,
                )

    def _update(self, dt):
        # Aim toward mouse cursor every frame
        mx, my = pygame.mouse.get_pos()
        px, py = self.level.player.x, self.level.player.y
        adx, ady = mx - px, my - py
        dist = math.hypot(adx, ady)
        if dist > 0:
            self.level.player.fire_dir = (adx / dist, ady / dist)

        self.level.update(dt)
        self.game_time += dt

        if self.level.player.health <= 0:
            self.game_over = True
            if not self._score_submitted and self.username:
                self._score_submitted = True
                submit_score(self.username, self.level.player.score, self.game_time)

    def _draw(self):
        self.screen.blit(self.sprites.background, (0, 0))

        # Draw artifacts
        for coin in self.level.coins:
            draw_x = int(coin.x) - COIN_SIZE // 2 - self.sprites.coin_offset
            draw_y = int(coin.y) - COIN_SIZE // 2 - self.sprites.coin_offset
            pass

        # Draw enemies
        for enemy in self.level.enemies:
            draw_x = int(enemy.x) - TILE_SIZE // 2 - self.sprites.enemy_offset
            draw_y = int(enemy.y) - TILE_SIZE // 2 - self.sprites.enemy_offset
            self.screen.blit(self.sprites.enemy, (draw_x, draw_y))

        # Draw aim line toward mouse cursor
        if not self.game_over:
            px, py = int(self.level.player.x), int(self.level.player.y)
            mx, my = pygame.mouse.get_pos()
            fdx, fdy = self.level.player.fire_dir
            has_ammo = self.level.player.ammo > 0
            dot_color = (*NEON_CYAN, 180) if has_ammo else (40, 90, 90, 100)
            aim_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            line_len = math.hypot(mx - px, my - py)
            if line_len > 0:
                step = 14
                for i in range(step, int(line_len), step):
                    dot_x = int(px + fdx * i)
                    dot_y = int(py + fdy * i)
                    r = 3 if has_ammo else 2
                    pygame.draw.circle(aim_surf, dot_color, (dot_x, dot_y), r)
                # Crosshair at mouse position
                ch_r = 8
                pygame.draw.circle(aim_surf, dot_color, (mx, my), ch_r, 1)
                pygame.draw.line(aim_surf, dot_color, (mx - ch_r - 4, my), (mx + ch_r + 4, my), 1)
                pygame.draw.line(aim_surf, dot_color, (mx, my - ch_r - 4), (mx, my + ch_r + 4), 1)
            self.screen.blit(aim_surf, (0, 0))

        # Draw player
        draw_x = int(self.level.player.x) - TILE_SIZE // 2 - self.sprites.player_offset
        draw_y = int(self.level.player.y) - TILE_SIZE // 2 - self.sprites.player_offset
        self.screen.blit(self.sprites.player, (draw_x, draw_y))

        # Draw projectiles
        for proj in self.level.projectiles:
            pygame.draw.circle(
                self.screen, NEON_CYAN,
                (int(proj.x), int(proj.y)), proj.radius,
            )
            pygame.draw.circle(
                self.screen, NEON_PURPLE,
                (int(proj.x), int(proj.y)), proj.radius - 2,
            )

        self.hud.draw(self.level.player, self.game_time)

        if self.game_over:
            self.hud.draw_game_over(
                self.level.player.score, self.game_time,
                submitted=(self._score_submitted and self.username is not None),
                username=self.username,
            )

        pygame.display.flip()


if __name__ == '__main__':
    username = _prompt_username()
    game = Game(username)
    game.run()
