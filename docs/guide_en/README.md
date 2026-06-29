# Mario Kart 8 Deluxe Manual Guide

This guide explains how the MK8DX Manual world is meant to be played and configured. It does not try to repeat every location line from `locations.json`; the data files already do that. The goal here is to explain the logic behind the options, items, checks, and goals so players can build a YAML that matches the content they own and the kind of seed they want.

## Files
- [Options](options.md): what each YAML group controls and how options interact.
- [Items](items.md): what the item categories represent in play.
- [Checks](checks.md): how check families work and how to read requirements.
- [Goals](goals.md): what each victory condition asks you to complete.

## Current Scope
- 11 victory goals.
- Grand Prix, VS Race, Time Trial, and Battle Mode logic.
- DLC and Booster Course Pass wave filtering.
- Character variant handling: separate, progressive, or character-only.
- Global race item and vehicle toggles.
- Grouped mode setting toggles so the YAML stays readable.

## Important Behavior
`difficulty_items: false` removes engine-class progression, hides the engine-specific checks, and shows clean no-difficulty variants instead. The active checks can be cleared in any engine class.

`dlc: false` overrides every wave option. Even if `dlc_wave_3` is true, Wave 3 content is removed when the global DLC option is false.

`race_items: false` removes race item progression and item checks that directly need those items. Battle checks also stop asking for a battle-damage item.

`kart: false` removes kart bodies, wheels, gliders, and their direct vehicle challenge checks together.
