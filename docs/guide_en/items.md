# Items Guide

Items represent what the player is allowed to use for checks. If a check requires `|VS Race|`, the player must have received the VS Race item before that check is logically available.

Progression classification is adjusted for the active YAML. Option-disabled categories are removed from the pool; an enabled item only stays progression when it can satisfy an active location, category, region, or goal requirement. Enabled progression items that are no longer needed are downgraded to filler.

## Main Progression Categories
**Game Modes** unlock Grand Prix, VS Race, Time Trial, and Battle. They decide which large parts of the game can be used.

**Cups** unlock the course groups. Cup requirements usually appear as exact cup names or compact category requirements like `|@Cups:1|`.

**Difficulty** contains 50cc, 100cc, 150cc, Mirror, and 200cc when `difficulty_items` is enabled. When `difficulty_items` is disabled, those items are removed from the pool and no-difficulty checks are used instead.

**Characters** unlock racers. Some shared selection slots can be handled separately, progressively, or as one character-only unlock depending on `character_variants`.

## Race Items
Race items are grouped behind `race_items`. If that option is disabled, the item pool no longer contains race item progression, and checks that directly ask for a specific item are removed.

Battle logic treats every race item except Coin as a possible damage item. If race items are disabled, Battle checks no longer require `@Battle Damage Items:1`.

## Vehicle Parts
Karts, wheels, and gliders are controlled together by `kart`. The client still shows them in their normal categories, but the YAML only has one switch because splitting every part individually would make the config noisy.

## Mode Settings
Mode settings are items too. They represent menu rules such as Team Game, No Items or Coins, Hard COM, 4 Rounds, or 12 Races.

The YAML controls these settings by family. For example, `mode_setting_races` enables every VS Race count item from 4 Races through 48 Races.

## MKTV Tokens
MKTV Tokens are only generated when the selected goal needs them. Required tokens are progression items; surplus tokens are useful items.

## Filler
Filler items fill empty item slots after progression and useful items have been placed. They are intentionally non-progression.
