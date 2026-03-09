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
ENEMY_SPEED  = 600      # pixels per second
ENEMY_DAMAGE = 10

# Coin / artifact settings
COIN_SCORE = 10

# Level and spawning
MAX_ENEMIES      = 8
ENEMY_SPAWN_RATE = 2.0      # seconds between spawns
MAX_COINS        = 10
COIN_SPAWN_RATE  = 1.5      # seconds between spawns

# Collision detection radius in pixels
COLLISION_RADIUS = 26

# Enemy separation — prevents enemies from stacking into one blob
ENEMY_SEPARATION_RADIUS = 56    # pixels: enemies push apart within this range
ENEMY_SEPARATION_WEIGHT = 0.45  # how strongly repulsion blends with the chase direction

# Projectile settings
PROJECTILE_SPEED    = 480   # pixels per second
PROJECTILE_RADIUS   = 5     # collision radius in pixels
AMMO_SCORE_INTERVAL = 50    # score points between ammo grants
AMMO_GRANT          = 3     # projectiles granted per interval

DUMMY_CONSTANT = 'dummy'
