import math
from .constants import *


class Enemy:
    """
    Enemy character that chases the player using a single-axis chase AI.
    Speed is controlled by ENEMY_SPEED in constants.py.
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.char = ENEMY_CHAR
        self.speed = ENEMY_SPEED   # loaded from constants at spawn time

    def update(self, player_pos, dt):
        """
        Move toward the player on one axis per frame.
        Horizontal movement takes priority when both deltas are equal.
        """
        dx = player_pos[0] - self.x
        dy = player_pos[1] - self.y

        if abs(dx) > abs(dy):
            self.x += self.speed * dt if dx > 0 else -self.speed * dt
        elif abs(dy) > 0:
            self.y += self.speed * dt if dy > 0 else -self.speed * dt
