import math
import random
from .constants import *


class Enemy:
    """
    Enemy character that chases the player using diagonal movement with
    separation forces to prevent grouping. Speed varies slightly per enemy.
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.char = ENEMY_CHAR
        self.speed = ENEMY_SPEED * random.uniform(0.82, 1.18)

    def update(self, player_pos, dt, others=None):
        """
        Move toward the player using a normalized direction vector (diagonal
        movement). Nearby enemies apply a separation force to avoid grouping.
        """
        dx = player_pos[0] - self.x
        dy = player_pos[1] - self.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        nx, ny = dx / dist, dy / dist

        sx, sy = 0.0, 0.0
        if others:
            for other in others:
                if other is self:
                    continue
                ox = self.x - other.x
                oy = self.y - other.y
                d = math.hypot(ox, oy)
                if 0 < d < ENEMY_SEPARATION_RADIUS:
                    strength = (ENEMY_SEPARATION_RADIUS - d) / ENEMY_SEPARATION_RADIUS
                    sx += (ox / d) * strength
                    sy += (oy / d) * strength

        mx = nx + sx * ENEMY_SEPARATION_WEIGHT
        my = ny + sy * ENEMY_SEPARATION_WEIGHT
        mag = math.hypot(mx, my)
        if mag > 0:
            mx /= mag
            my /= mag

        self.x += mx * self.speed * dt
        self.y += my * self.speed * dt
