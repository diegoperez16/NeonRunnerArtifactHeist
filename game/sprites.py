import os
import pygame
from .constants import (
    TILE_SIZE, COIN_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT,
    NEON_CYAN, NEON_RED, NEON_GOLD,
    COLOR_BG, COLOR_GRID,
)

_GAME_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_GAME_DIR)
_PACK_64   = os.path.join(_REPO_ROOT, 'assets', 'kenney_scribble-dungeons', 'PNG', 'Default (64px)')
_CHARS = os.path.join(_PACK_64, 'Characters')
_ITEMS = os.path.join(_PACK_64, 'Items')


def _load(path, size=None):
    try:
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        return img
    except (pygame.error, FileNotFoundError, OSError):
        return None


def _tint_gold(surface):
    tinted = surface.copy()
    tinted.fill(NEON_GOLD, special_flags=pygame.BLEND_RGB_MULT)
    return tinted


def _add_glow(surface, glow_color, radius=16, intensity=95):
    sw, sh = surface.get_size()
    out    = pygame.Surface((sw + radius * 2, sh + radius * 2), pygame.SRCALPHA)
    cx, cy = out.get_width() // 2, out.get_height() // 2
    steps  = max(radius // 3, 1)
    for step in range(steps):
        r     = radius - step * (radius // steps)
        alpha = int(intensity * (step + 1) / steps)
        pygame.draw.circle(out, (*glow_color, alpha), (cx, cy), r + sw // 2)
    out.blit(surface, (radius, radius))
    return out


def _circle_fallback(color, size):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(surf, (*color, 255), (size[0] // 2, size[1] // 2), min(size) // 2 - 2)
    return surf


class SpriteManager:
    def __init__(self):
        ts = (TILE_SIZE, TILE_SIZE)
        cs = (COIN_SIZE, COIN_SIZE)

        player_base = _load(os.path.join(_CHARS, 'green_character.png'), ts) or _circle_fallback(NEON_CYAN, ts)
        enemy_base  = _load(os.path.join(_CHARS, 'red_character.png'),   ts) or _circle_fallback(NEON_RED,  ts)
        dagger_raw  = _load(os.path.join(_ITEMS, 'weapon_dagger.png'),   cs)
        coin_base   = _tint_gold(dagger_raw) if dagger_raw else _circle_fallback(NEON_GOLD, cs)

        player_glow, enemy_glow, coin_glow = 18, 18, 14

        self.player = _add_glow(player_base, NEON_CYAN, radius=player_glow, intensity=100)
        self.enemy  = _add_glow(enemy_base,  NEON_RED,  radius=enemy_glow,  intensity=100)
        self.coin   = _add_glow(coin_base,   NEON_GOLD, radius=coin_glow,   intensity=110)

        self.player_offset = player_glow
        self.enemy_offset  = enemy_glow
        self.coin_offset   = coin_glow

        self.background = self._make_background()

    def _make_background(self):
        surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        surf.fill(COLOR_BG)
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            pygame.draw.line(surf, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            pygame.draw.line(surf, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))
        return surf
