# Options Guide

The YAML is organized by gameplay purpose instead of by raw data order. Most options are simple toggles: set `'true'` to include the content, or `'false'` to remove it from the seed logic.

## Goal Options
`goal` chooses the win condition. Token variants require the selected objective plus the configured MKTV Token count.

`mktv_tokens_required` controls how many MKTV Tokens are needed when the goal uses tokens. `mktv_tokens_available_percentage` controls surplus token placement. Tokens are not added to the pool when the selected goal does not need them.

## Game Modes
`game_modes` is the global parent for Grand Prix, VS Race, Time Trial, and Battle. The individual options let a player remove a mode they do not want to play.

Keep at least one mode enabled. If a location only depends on disabled modes, it is removed from the generated world.

## DLC Options
`dlc` is the master switch. When it is false, all DLC cups, DLC characters, DLC checks, and wave-specific content are removed.

The wave options let players include only the Booster Course Pass waves they own. They are ignored when `dlc` is false.

## Gameplay Options
`difficulty_items` controls whether 50cc, 100cc, 150cc, Mirror, and 200cc exist as progression. When disabled, engine-specific checks are hidden and clean no-difficulty variants are shown instead.

`race_items` controls all race item progression as one block. `kart` controls kart bodies, wheels, and gliders as one block.

`character_variants` controls shared character slots:
- `separate`: every color or form is its own item.
- `progressive`: repeated `Progressive - Character` items unlock the variants in order.
- `character_only`: one base character item unlocks every variant in that group.

## Check Options
These toggles add or remove optional check families:
- `track_challenges`: course-specific and character-course challenges.
- `item_challenges`: checks for using race items.
- `kart_challenges`: checks for winning with kart bodies, wheels, and gliders.
- `vs_race_challenges`: VS Race race-count challenges.
- `battle_challenges`: Battle Mode round-count challenges.

`time_trial_checks` chooses between one Nintendo ghost check per course or split 150cc/200cc Time Trial checks.

## Mode Setting Options
Mode settings are grouped by family instead of one YAML option per item:
- `mode_setting_teams`: Team Game and No Teams.
- `mode_setting_items`: Battle and VS Race item-rule settings, including No Items or Coins and item-only rules.
- `mode_setting_round_time`: 1 through 5 Minute Battle timers.
- `mode_setting_com`: Easy, Normal, and Hard COM.
- `mode_setting_com_vehicles`: All Vehicles, Kart Only, and Bikes Only.
- `mode_setting_courses`: Choose Courses, In Order Courses, and Random Courses.
- `mode_setting_rounds`: 4 through 24 Battle rounds.
- `mode_setting_races`: 4 through 48 VS Races.

Turning one of these off removes the related setting items and the checks that directly require that family.

## Battle Mode Options
`battle_modes` is the parent option for the five Battle modes. Individual Battle mode options remove the matching mode item and checks that directly require it.

## Item And Location Options
The final YAML block contains standard Archipelago options such as local items, non-local items, start inventory, hints, excluded locations, priority locations, and item links.
