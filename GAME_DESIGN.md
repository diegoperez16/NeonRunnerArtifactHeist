# Game Design Notes

## Core Loop

- Player navigates dungeon collecting artifacts
- Enemies spawn from screen edges and chase player
- Health depletes on enemy contact
- Game ends when health reaches zero, score is tallied

## Difficulty

- Enemy count caps at MAX_ENEMIES (see constants.py)
- Spawn rate and speed are tunable per playtesting feedback
- Current feel: manageable for first 30s, ramps up after that

## Future Ideas

- Multiple dungeon layouts or procedural rooms
- Boss enemies with special attack patterns
- Power-ups: speed boost, temporary shield, artifact magnet
- Online leaderboard integration
