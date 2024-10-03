# Window
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
TILE_SIZE     = 64          # matches the 64px kenney sprite pack
COIN_SIZE     = 48          # artifacts are slightly smaller than characters
FPS           = 60

# Character representations (referenced by workshop missions)
PLAYER_CHAR = '@'
ENEMY_CHAR  = 'E'
COIN_CHAR   = '$'

# Neon color palette - used for glow effects, HUD, and UI
NEON_CYAN   = (0,   230, 200)
NEON_RED    = (255,  60,  60)
NEON_GOLD   = (255, 200,  40)
NEON_PURPLE = (160,  80, 255)
COLOR_BG    = (8,    8,   18)
COLOR_GRID  = (18,  18,   34)

# Player settings
PLAYER_SPEED        = 250       # pixels per second
PLAYER_START_HEALTH = 100

# Enemy settings
ENEMY_SPEED  = 150      # pixels per second
ENEMY_DAMAGE = 10

# Coin / artifact settings
COIN_SCORE = 10

# Level and spawning
MAX_ENEMIES      = 5
ENEMY_SPAWN_RATE = 3.0      # seconds between spawns
MAX_COINS        = 8
COIN_SPAWN_RATE  = 2.5      # seconds between spawns

# Collision detection radius in pixels
COLLISION_RADIUS = 26

DUMMY_CONSTANT = 'dummy'
