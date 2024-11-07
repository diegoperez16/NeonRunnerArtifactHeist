from .constants import *
import random

# I DID THIS COMPLETELY< EVERTHING HERE WAZ ME


class Player:
    """
    Player character controlled by the user.

    Attributes:
        x (float): X position on screen
        y (float): Y position on screen
        char (str): Visual character representation
        speed (int): Movement speed
        health (int): Current health points
        score (int): Current score from collecting coins
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = PLAYER_CHAR
        self.speed = PLAYER_SPEED
        self.health = PLAYER_START_HEALTH
        self.score = 0

    def move(self, dx, dy, max_x, max_y):
        """
        Move the player by the given delta values while keeping them within bounds.

        Args:
            dx: Change in x position (negative = left, positive = right)
            dy: Change in y position (negative = up, positive = down)
            max_x: Maximum x boundary (screen width)
            max_y: Maximum y boundary (screen height)
        """
        # Apply movement delta
        self.x += dy
        self.y += dx

        # Keep player on screen
        if self.x < 0:
            self.x = 0
        if self.x >= max_x:
            self.x = max_x - 1
        if self.y < 0:
            self.y = 0
        if self.y >= max_y:
            self.y = max_y - 1

    def take_damage(self, amount):
        """Reduce player health by the specified amount."""
        self.health -= amount
        if self.health < 0:
            self.health = 0
        dizzy_chars = ['@', '#', '%', '&', '?', '!']
        self.char = random.choice(dizzy_chars)

    def add_score(self, amount):
        """Increase the player's score."""
        self.score += amount
