# Archipelago Manual for Mario Kart 8 Deluxe

## Welcome!
Welcome to the repository for the Archipelago Manual integration for **Mario Kart 8 Deluxe**.
This project turns Mario Kart 8 Deluxe objectives, cups, characters, vehicle parts, race modes, DLC ownership, and token goals into an Archipelago multiworld experience.

The manual targets **Mario Kart 8 Deluxe on Nintendo Switch**, including Booster Course Pass content where the player owns it. DLC and wave-related checks can be enabled or disabled from the YAML so players can match the content they actually own.

## Project Status
The project is currently at **Version 0.9.0 - DLC Update**.
Version 1.0.0 is reserved for the point where the project is considered complete.
The current update focuses on DLC ownership options, Booster Course Pass wave filtering, golden unlock options, and cleaner documentation on top of the refreshed Manual Archipelago stable framework (`manual_stable_20260319`).

## Current Features
- **All Rainbow Roads Complete**
  Complete every Rainbow Road objective included in the generated seed.
- **Mario Kart 8 Token**
  Collect Mario Kart 8 Tokens as the token-based victory objective.
- **Engine-Class Toggles**
  Enable or disable 50cc, 100cc, 150cc, Mirror, and 200cc checks from the YAML.
- **DLC and Wave Options**
  Enable or disable all DLC content, then choose individual Booster Course Pass waves from Wave 1 through Wave 6.
- **Golden Unlock Options**
  Enable or disable all golden unlocks together, or individually toggle Golden Mario, Gold Standard, Gold Tires, and Golden Glider.
- **Race Mode Coverage**
  Includes Grand Prix, VS Race, Time Trial, and 10-coin race checks.
- **Large Item Pool**
  Randomizes characters, cups, battle modes, game modes, difficulties, karts, wheels, gliders, race items, and tokens.
- **Starting Loadout**
  Seeds start with one randomized item from key gameplay categories such as game mode, difficulty, cup, character, kart, wheels, and glider.

---

## Patch Notes

### Version 0.9.0 - DLC Update

**DLC and wave options**
- Added the `dlc` YAML option to enable or disable all DLC and Booster Course Pass content.
- Added `dlc_wave_1` through `dlc_wave_6` so players can include only the Booster Course Pass waves they own.
- Made `dlc = false` override every individual wave option, even if a wave is set to true.
- Added hidden technical categories for `DLC` and each wave so items and checks can be filtered without showing extra client tabs.

**Golden unlock options**
- Added the `golden` YAML option to enable or disable all golden unlocks at once.
- Added individual YAML options for `golden_mario`, `gold_standard`, `gold_tires`, and `golden_glider`.
- Made `golden = false` override every individual golden option.
- Kept DLC, wave, and golden technical categories hidden so client display stays focused on the original item categories.

**Logic and goals**
- Propagated DLC, wave, and golden categories to related locations through hooks instead of manually duplicating that data across every check.
- Updated `All Rainbow Roads Complete` so it no longer requires DLC cups when DLC or the relevant wave is disabled.
- Rebuilt `manual_mk8dx_narusnake.apworld` with the updated options, hooks, and documentation.

---

### Version 0.8.0 - Manual Stable Update

**Manual framework update**
- Synced the source package with the newer Manual Archipelago stable base (`manual_stable_20260319`).
- Updated the Manual core files for data loading, item creation, rules, regions, options, validation, helper APIs, and client support.
- Added `container.py` for modern `.apmanual` zip container support.
- Added an empty `data/events.json` so the project is ready for the current Manual event system.
- Added the stable Manual test package under `manual_mk8dx_narusnake/test/`.
- Updated the Manual client foundation with newer tracker support, client settings, item/location sorting, search refresh behavior, DeathLink UI support, and modern `.apmanual` reading.
- Rebuilt `manual_mk8dx_narusnake.apworld` from the refreshed source package.

**MK8DX data and options**
- Preserved the Mario Kart 8 Deluxe item and location data while updating the Manual framework around it.
- Kept 50cc, 100cc, 150cc, Mirror, and 200cc YAML toggles for controlling generated checks.
- Kept the two main goals: `All Rainbow Roads Complete` and `Mario Kart 8 Token`.
- Corrected a 200cc Triforce Cup VS Race location so it requires the 200cc category and appears in the intended category.
- Removed the old `enable_region_diagram` metadata flag; the current Manual framework now exposes region diagram generation through a hidden option.

**Documentation**
- Rewrote this README using the cleaner release-note layout used by the Super Street Fighter II manual.
- Added a French README at `manual_mk8dx_narusnake/docs/README_FR.md`.
- Removed the unused changelog files from `manual_mk8dx_narusnake/docs/`.

**Notes for this release**
- Rebuild the `.apworld` after changing source files when preparing a distributable release.
- A full runtime import requires the Archipelago environment to be available on `PYTHONPATH`.

---

### Version 0.7.0 - CC Update
- Restructured `items.json`.
- Added items for 50cc, 100cc, 150cc, Mirror, and 200cc.
- Updated the YAML template with the new 50cc, 100cc, 150cc, Mirror, and 200cc options.
- Updated checks to use the new engine-class categories.

---

### Version 0.6.0 - Item Update
- Added all in-game items to the Archipelago item pool.
- Switched the filler item setup to use `MKFan`.

---

### Version 0.5.0 - Time Trial Update
- Added Time Trial mode checks and the matching item.
- Added 10-coin race checks.
- Updated `game.json` so Battle Mode can be included in starting seed generation.

---

### Version 0.4.1 - Bugfix Release
- Fixed issues caused by an Archipelago migration.

---

### Version 0.4.0 - Migration Release
- Updated the codebase to the newer Manual Archipelago framework used at the time.

---

### Version 0.3.0 - VS Race Update
- Added a **Game Modes** item category.
- Added the **VS Race** check category.
- Renamed **Win the cups with...** checks to **Win a race with...**.
- Added game-mode options in the seed configuration.
- Adjusted token count to 100.

---

### Version 0.2.0 - Character Update
- Added Birdo, Yoshi, and Shy Guy color variants.
- Added Golden Mario.
- Added Inkling variants.
- Added Male Villager and Female Villager.
- Added Link variants.
- Added all Miis.
- Added 25 Tokens as items.
- Added the **Mario Kart 8 Token** goal.
- Added **Win any Cup with...** checks for the character roster.

**Known note**
- If Golden Mario is not unlocked, the related check can be completed with Metal Mario instead.

---

### Version 0.1.0 - Initial Release
- Added items in the **Characters**, **Karts**, **Wheels**, and **Gliders** categories.
- Added cup-completion checks, including 1st place and bronze, silver, and gold trophy checks.
- Added character win checks.

---

## Future Roadmap
- **Goal variety**: Add more victory conditions around cups, engine classes, Time Trials, tokens, or mixed objectives.
- **Category polish**: Review category visibility and grouping in the Manual client for easier tracking.
- **Logic review**: Continue checking 200cc, VS Race, Time Trial, coin checks, and DLC edge cases for consistency.
- **YAML modernization**: Refresh the YAML template with newer Archipelago option patterns and clearer comments.

---

## Contributing
Feedback and contributions are welcome.
- Report bugs or suggest features through GitHub issues.
- Submit PRs with data fixes, logic updates, or framework compatibility improvements.
- Improve documentation, setup instructions, or YAML examples.

---

## Acknowledgements
This manual was inspired by the work of RampantEpsilon and JokerFactor, and by the wider Manual for Archipelago community.

---

## Contact
Questions, streams, or bug reports? Reach out on the Archipelago Discord or open an issue on GitHub.