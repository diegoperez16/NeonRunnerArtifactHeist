# Game Design Notes

## Core Loop

- Player navigates dungeon collecting artifacts
- Enemies spawn from screen edges and chase player
- Health depletes on enemy contact
- Game ends when health reaches zero, score is tallied

## Difficulty Curve

Starting gentle, escalating as time passes:
- 0-30s: slow spawns, 2-3 enemies max
- 30-60s: faster spawns, up to 5 enemies
- 60s+: max pressure, full enemy cap active

Linking difficulty to score rather than time is worth considering
so skilled players get a harder game sooner.

## Sound Design Ideas

- Looping ambient dungeon track (moody, low)
- Artifact pickup: short satisfying chime
- Enemy hit: low thud or buzz
- Game over: brief descending tone

Will integrate once Vivi has the audio module ready.

## Future Ideas

- Multiple dungeon layouts or procedural rooms
- Boss enemies with special attack patterns
- Power-ups: speed boost, temporary shield, artifact magnet
- Online leaderboard integration
