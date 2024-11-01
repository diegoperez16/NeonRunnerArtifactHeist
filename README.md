# Neon Runner: Artifact Heist

## Description

Neon Runner: Artifact Heist is a fast-paced arcade game. You are a runner
navigating a dark dungeon, collecting stolen artifacts and dodging relentless
enemies in a race for the high score.

## Gameplay

Collect as many artifacts as possible while avoiding enemies. Your health drops
on contact with an enemy. The game ends when your health reaches zero.

### Game Elements

- **Player** - the green character you control
- **Enemies** - red characters that chase and damage you
- **Artifacts** - collectibles that increase your score

## Controls

| Key                  | Action                    |
|----------------------|---------------------------|
| W / Up Arrow         | Move up                   |
| S / Down Arrow       | Move down                 |
| A / Left Arrow       | Move left                 |
| D / Right Arrow      | Move right                |
| Q / Escape           | Quit                      |
| R                    | Restart (after game over) |

## Requirements

- Python 3.8 or newer
- pygame 2.5 or newer

Works on macOS, Linux, and Windows.

## How to Run

```sh
# Install dependencies
pip install -r requirements.txt

# Run the game
python3 main.py
```

## Project Structure

```
main.py              entry point and game loop
game/
  constants.py       all tunable game values
  player.py          player movement and stats
  enemy.py           enemy AI and movement
  coin.py            artifact/collectible object
  level.py           spawning, updates, collision
  hud.py             on-screen display
  sprites.py         sprite loading and glow effects
assets/
  kenney_scribble-dungeons/   sprite pack (Kenney, CC0)
```
