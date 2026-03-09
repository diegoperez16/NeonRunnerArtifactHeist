import math
from .constants import PROJECTILE_SPEED, PROJECTILE_RADIUS


class Projectile:
    """
    A projectile fired by the player. Moves in a straight line until it
    leaves the screen or hits an enemy.
    """

    def __init__(self, x, y, dx, dy):
        self.x = float(x)
        self.y = float(y)
        speed = PROJECTILE_SPEED
        self.vx = dx * speed
        self.vy = dy * speed
        self.radius = PROJECTILE_RADIUS
        self.active = True

    def update(self, dt, width, height):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            self.active = False
