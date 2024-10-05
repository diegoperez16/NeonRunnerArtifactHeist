import math
from .constants import *


class Enemy:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.char = ENEMY_CHAR
        self.speed = ENEMY_SPEED

    def update(self, player_pos, dt):
        # Chase AI that moves on one axis at a time
        dx = player_pos[0] - self.x
        dy = player_pos[1] - self.y

        if abs(dx) > abs(dy):
            self.x += self.speed * dt if dx > 0 else -self.speed * dt
        elif abs(dy) > 0:
            self.y += self.speed * dt if dy > 0 else -self.speed * dt
