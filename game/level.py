import random
from .constants import *
from .player import Player
from .coin import Coin
from .enemy import Enemy
from .projectile import Projectile


class Level:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.enemies     = []
        self.coins       = []
        self.projectiles = []

        # Player starts at the center of the screen
        self.player = Player(width // 2, height // 2)

        # Timers track seconds since last spawn
        self.enemy_spawn_timer = 0
        self.coin_spawn_timer  = 0

    def fire_projectile(self):
        """Fire one projectile in the player's last movement direction."""
        if self.player.ammo <= 0:
            return
        self.player.ammo -= 1
        dx, dy = self.player.fire_dir
        self.projectiles.append(Projectile(self.player.x, self.player.y, dx, dy))

    def update(self, dt):
        player_pos = (self.player.x, self.player.y)
        for enemy in self.enemies:
            enemy.update(player_pos, dt, others=self.enemies)
        for proj in self.projectiles:
            proj.update(dt, self.width, self.height)
        self.projectiles = [p for p in self.projectiles if p.active]
        self._spawn_manager(dt)
        self._handle_collisions()

    def _spawn_manager(self, dt):
        # ---- enemy spawning ----
        self.enemy_spawn_timer += dt
        if len(self.enemies) < MAX_ENEMIES and self.enemy_spawn_timer > ENEMY_SPAWN_RATE:
            self.enemy_spawn_timer = 0
            side = random.randint(0, 3)
            if side == 0:
                x, y = random.randint(0, self.width), -TILE_SIZE
            elif side == 1:
                x, y = random.randint(0, self.width), self.height + TILE_SIZE
            elif side == 2:
                x, y = -TILE_SIZE, random.randint(0, self.height)
            else:
                x, y = self.width + TILE_SIZE, random.randint(0, self.height)
            self._spawn_enemy(x, y)

        # ---- coin spawning ----
        self.coin_spawn_timer += dt
        if len(self.coins) < MAX_COINS and self.coin_spawn_timer > COIN_SPAWN_RATE:
            self.coin_spawn_timer = 0
            margin = TILE_SIZE * 2
            x = random.randint(margin, self.width  - margin)
            y = random.randint(margin + 80, self.height - margin)
            self._spawn_coin(x, y)

    def _spawn_enemy(self, x, y):
        self.enemies.append(Enemy(x, y))

    def _spawn_coin(self, x, y):
        self.coins.append(Coin(x, y))

    def _handle_collisions(self):
        # Enemy contact damages the player and removes the enemy
        for enemy in self.enemies[:]:
            dx = enemy.x - self.player.x
            dy = enemy.y - self.player.y
            if dx * dx + dy * dy < COLLISION_RADIUS * COLLISION_RADIUS:
                self.player.take_damage(ENEMY_DAMAGE)
                self.enemies.remove(enemy)

        # Projectile contact destroys the enemy
        for proj in self.projectiles[:]:
            for enemy in self.enemies[:]:
                dx = proj.x - enemy.x
                dy = proj.y - enemy.y
                hit_r = PROJECTILE_RADIUS + COLLISION_RADIUS
                if dx * dx + dy * dy < hit_r * hit_r:
                    proj.active = False
                    self.enemies.remove(enemy)
                    break

        # Coin contact awards points and removes the coin
        for coin in self.coins[:]:
            dx = coin.x - self.player.x
            dy = coin.y - self.player.y
            if dx * dx + dy * dy < COLLISION_RADIUS * COLLISION_RADIUS:
                self.player.add_score(COIN_SCORE)
                self.coins.remove(coin)
