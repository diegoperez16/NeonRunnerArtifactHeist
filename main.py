import pygame
import sys

from game.level import Level
from game.hud import HUD
from game.sprites import SpriteManager
from game.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    PLAYER_SPEED, TILE_SIZE, COIN_SIZE,
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Neon Runner: Artifact Heist")
        self.screen  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock   = pygame.time.Clock()
        self.sprites = SpriteManager()

        self.running   = True
        self.game_over = False
        self.game_time = 0.0

        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.game_time = 0.0
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
        self.level.update(dt)
        self.game_time += dt
        if self.level.player.health <= 0:
            self.game_over = True

    def _draw(self):
        self.screen.blit(self.sprites.background, (0, 0))

        # Draw artifacts
        for coin in self.level.coins:
            draw_x = int(coin.x) - COIN_SIZE // 2 - self.sprites.coin_offset
            draw_y = int(coin.y) - COIN_SIZE // 2 - self.sprites.coin_offset
            self.screen.blit(self.sprites.coin, (draw_x, draw_y))

        # Draw enemies
        for enemy in self.level.enemies:
            draw_x = int(enemy.x) - TILE_SIZE // 2 - self.sprites.enemy_offset
            draw_y = int(enemy.y) - TILE_SIZE // 2 - self.sprites.enemy_offset
            self.screen.blit(self.sprites.enemy, (draw_x, draw_y))

        # Draw player
        draw_x = int(self.level.player.x) - TILE_SIZE // 2 - self.sprites.player_offset
        draw_y = int(self.level.player.y) - TILE_SIZE // 2 - self.sprites.player_offset
        self.screen.blit(self.sprites.player, (draw_x, draw_y))

        self.hud.draw(self.level.player, self.game_time)

        if self.game_over:
            self.hud.draw_game_over(self.level.player.score, self.game_time)

        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
