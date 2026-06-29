# Archipelago Manual for Mario Kart 8 Deluxe

## Welcome!
Welcome to the repository for the Archipelago Manual integration for **Mario Kart 8 Deluxe**.
This project turns Mario Kart 8 Deluxe objectives, cups, characters, vehicle parts, race modes, DLC ownership, and token goals into an Archipelago multiworld experience.

The manual targets **Mario Kart 8 Deluxe on Nintendo Switch**, including Booster Course Pass content where the player owns it. DLC and wave-related checks can be enabled or disabled from the YAML so players can match the content they actually own.

## Project Status
The project is currently at **Version 0.12.0 - Time Trial Check Update**.
Version 1.0.0 is reserved for the point where the project is considered complete.
The current update focuses on the Time Trial ghost check mode, expanded challenge logic, starting loadout support, fine-grained content options, detailed guides, and a cleaned victory goal set while keeping the character variant handling, DLC ownership options, MKTV Token configuration, and refreshed Manual Archipelago stable framework (`manual_stable_20260319`) from previous updates.

## Current Features
- **Victory Goal Selection**
  Choose between Rainbow Roads, MKTV Tokens, Grand Prix, Time Trial, VS Race, Battle, or MKTV Token variants for every non-token objective.
- **Engine-Class Toggles**
  Enable or disable 50cc, 100cc, 150cc, Mirror, and 200cc checks from the YAML. `difficulty_items` can also remove engine-class progression entirely and swap engine-specific checks for clean no-difficulty checks.
- **Time Trial Check Mode**
  Choose between one Nintendo ghost check per track or separate 150cc and 200cc Time Trial ghost checks.
- **DLC and Wave Options**
  Enable or disable all DLC content, then choose individual Booster Course Pass waves from Wave 1 through Wave 6.
- **Golden Unlock Options**
  Enable or disable all golden unlocks together, or individually toggle Golden Mario, Gold Standard, Gold Tires, and Golden Glider.
- **Fine-Grained Content Toggles**
  Globally or individually enable game modes and Battle modes from the YAML. Mode settings are controlled by clean families such as teams, item rules, round time, COM rules, course rules, Battle rounds, and VS Race counts. A single `race_items` option controls every race item, and a single `kart` option controls kart bodies, wheels, and gliders together.
- **Character Variant Modes**
  Choose whether characters that share a selection slot use separate items, repeated `Progressive - Character` items, or one character-only unlock for every form/color.
- **Configurable Token Goal**
  Set required MKTV Tokens and available surplus from the YAML. Token items are removed when the selected goal or token variant does not need them.
- **Filler Item Pool**
  Uses the dedicated `Filler` category with translated English filler items for extra item pool slots.
- **Race Mode Coverage**
  Includes Grand Prix, VS Race, Time Trial ghost checks, and 10-coin race checks. 150cc and 200cc 10-coin checks can also be cleared in Time Trial.
- **Battle Settings Logic**
  Adds Battle setup items for teams, item rules, round time, round count, COM difficulty, COM vehicles, and course order. Battle victory checks require a valid setup and at least one non-Coin battle item.
- **Race Placement Checks**
  Finish a Grand Prix or VS Race in each exact position from 1st through 12th. These checks accept any unlocked engine class and any unlocked cup.
- **VS Race Challenge Checks**
  Adds optional VS Race race-count challenges for winning 4 through 48 races with or without teams, controlled by the `vs_race_challenges` YAML toggle.
- **Battle Challenge Checks**
  Adds optional Battle Mode round-count challenges for each Battle mode, controlled by the `battle_challenges` YAML toggle.
- **Track Challenge Checks**
  Adds optional course-specific and character-course challenge checks, grouped in cup-specific Challenge categories and controlled by the `track_challenges` YAML toggle.
- **Item Challenge Checks**
  Adds optional checks for using every race item, controlled by the `item_challenges` YAML toggle. These can be cleared in Grand Prix, VS Race, or Battle Mode.
- **Kart Challenge Checks**
  Adds optional checks for winning a race with each kart body, wheel, and glider, controlled by the `kart_challenges` YAML toggle.
- **Large Item Pool**
  Randomizes characters, cups, battle modes, game modes, difficulties, mode settings, karts, wheels, gliders, race items, tokens, and fillers.
- **Starting Loadout**
  Seeds start with one randomized item from key gameplay categories such as game mode, difficulty, cup, character, kart, wheels, and glider. If the starting game mode is VS Race or Battle, the seed also precollects the mode settings needed to make the shortest matching challenge logic available. VS Race starts use `No Items or Coins` and `4 Races`.
- **Detailed Guides**
  Explanatory guides are available in `manual_mk8dx_narusnake/docs/guide_en/` and `manual_mk8dx_narusnake/docs/guide_fr/`.

---

## Patch Notes

### Version 0.12.0 - Check Update

**Time Trial check mode**
- Added the `time_trial_checks` YAML option with `single` and `split_150_200` modes.
- `single` creates one Nintendo ghost check per track without an engine-class requirement.
- `split_150_200` creates separate 150cc and 200cc Nintendo ghost checks.
- Removed the duplicate 100cc and Mirror Time Trial ghost checks from the active location list.
- Kept Time Trial available for 150cc and 200cc 10-coin checks, while 50cc, 100cc, and Mirror 10-coin checks require Grand Prix or VS Race.

**Race placement checks**
- Added 12 `Race Placements` checks for finishing a Grand Prix or VS Race from 1st through 12th place.
- Placement checks require Grand Prix or VS Race, any unlocked engine class, and any unlocked cup without forcing a specific difficulty.

**Battle setting logic**
- Added 25 `Mode Settings` items for Battle setup: team rules, item rules, round time, round count, COM difficulty, COM vehicles, and course order.
- Added the hidden `Battle Damage Items` category to every race item except `Coin`, so Battle checks can require at least one item that can affect opponents.
- Battle victory checks now require their Battle mode, valid Battle settings, and the mode-specific exceptions: Renegade Roundup does not require team settings, and Shine Thief does not require round time.

**VS Race challenge checks**
- Added 15 VS Race-specific `Mode Settings` items and reused shared team, COM, vehicle, and course settings where possible.
- Added 80 optional `VS Race Challenges`: five engine classes, eight race counts from 4 to 48 races, and both teams/no-teams variants.
- VS Race challenges require VS Race, the selected engine class, the race count setting, a team setting, VS item/COM/vehicle/course settings, and enough unlocked cups using `|@Cups:N|`.
- Added the `vs_race_challenges` YAML toggle to enable or disable these checks.

**Battle challenge checks**
- Added 54 optional `Battle Challenges`: six round counts from 4 to 24 rounds across the Battle modes.
- Balloon Battle, Bob-omb Blast, Coin Runners, and Shine Thief include both teams and no-teams variants.
- Renegade Roundup does not require a team setting, and Shine Thief does not require a round-time setting.
- Battle challenges require Battle, the selected Battle mode, the round count setting, Battle item/COM/vehicle/course settings, and at least one non-Coin battle item.
- Added the `battle_challenges` YAML toggle to enable or disable these checks.

**Track challenge checks**
- Added 96 optional `Track Challenges` checks, one per course, grouped in cup-specific Challenge categories and controlled by the `track_challenges` YAML toggle.
- Added 45 character-course challenge checks for circuits named after, or strongly referencing, playable characters or playable species.
- Object-style track challenges require any race mode, any unlocked engine class, and the related cup. Character-course challenges require Grand Prix or VS Race, the related character, any unlocked engine class, and the related cup.
- Reordered cup-based locations to match the in-game cup order.

**Item challenge checks**
- Added 23 optional `Item Challenges` checks, one for each race item.
- Item challenges require the item plus either Grand Prix or VS Race with an unlocked engine class and cup, or Battle with any unlocked battle mode.

**Kart challenge checks**
- Added 63 optional `Kart Challenges` checks: 29 kart bodies, 19 wheels, and 15 gliders.
- Kart, wheel, and glider challenges require the related vehicle part, Grand Prix or VS Race, any unlocked engine class, and any unlocked cup.

**Starting loadout logic**
- Added conditional starting settings for VS Race and Battle starts.
- VS Race starts now receive one team setting, item setting, COM setting, COM vehicle setting, course setting, and `4 Races`.
- Battle starts now receive one team setting, item setting, damage item, COM setting, COM vehicle setting, course setting, `4 Rounds`, and one round-time setting.

**Goal update**
- Replaced the old draft goal list with 11 clean victory goals.
- Kept `All Rainbow Roads Complete` and `Mario Kart 8 Token` first so existing goal aliases stay stable.
- Added Grand Prix, Time Trial, VS Race, and Battle objective goals using the real item categories and mode settings.
- Added MKTV Token variants for every non-token objective.
- Removed broken goal requirements that referenced old `@round`, `@round battle`, and lowercase `@cups` categories.

**Fine-grained option update**
- Added global and individual YAML toggles for game modes and Battle modes, then grouped mode setting toggles by family: teams, item rules, round time, COM rules, course rules, Battle rounds, and VS Race counts. Added one global `race_items` toggle for every race item and one global `kart` toggle for kart bodies, wheels, and gliders together.
- Added `difficulty_items` to remove engine-class progression, hide engine-specific checks, and use clean no-difficulty check variants instead.
- Removed the leftover Manual template example options from the generated YAML/options data.
- Set Battle Mode and Mode Setting option families to disabled by default in the generated YAML template.
- Updated VS Race starts to precollect `No Items or Coins` plus `4 Races` when VS Race is the starting mode.
- Battle logic now removes the `@Battle Damage Items:1` requirement when every battle-damage race item is disabled.
- Fixed the Triforce Cup Wii Wario's Gold Mine VS Race checks for 50cc, 100cc, 150cc, and Mirror so no-difficulty filtering treats them correctly.

**Guide documentation**
- Added English and French guide documentation covering options, items, checks, and goals with practical explanations.
- Kept the detailed lists out of the main README so the release notes stay readable.

**Build**
- Rebuilt `manual_mk8dx_narusnake.apworld` with the new Time Trial option, Battle/VS settings, categories, and location data.

### Version 0.11.0 - Character Update

**Character variant option**
- Added the global `character_variants` YAML option with `separate`, `progressive`, and `character_only` modes.
- Kept `separate` as the default so existing character checks behave like previous versions unless the player opts in.
- Added character-only and progressive items for Birdo, Yoshi, Shy Guy, Inkling, Villager, Link, Mii, and the Koopalings.

**Progressive and character-only logic**
- Variant checks now accept the exact variant item, the matching `Progressive - Character:N` count, or the base character-only item.
- `character_only` unlocks every color/form in that group at once.
- `progressive` unlocks colors/forms in the configured selection order by requiring additional copies of the progressive item.
- Birdo group items still respect the DLC and Wave 4 options.

**Requirement cleanup**
- Converted location requirements to the explicit `|Item| AND (|A| OR |B|)` string format for consistency.
- Harmonized race-mode OR requirements used by 10-coin checks.

**Item ordering**
- Reordered `items.json` by category, then alphabetically within each category.
- Preserved custom selection order for character groups with multiple colors/forms.

### Version 0.10.0 - Filler Update

**Hook adaptation**
- Ported the Tekken 3 Manual hook structure to MK8D and adapted `Data.py`, `Helpers.py`, `Options.py`, `Rules.py`, and `World.py`.
- Added hook-side filtering for engine classes, DLC waves, and golden unlocks so disabled YAML options remove their related items and checks.
- Added automatic location sort keys and hook-driven DLC, wave, and golden category propagation.

**Filler items**
- Translated the 72 new filler item names in `items.json` to English.
- Added filler selection from the `Filler` category so extra item pool slots can use the dedicated MK8D filler list.
- Kept technical DLC, wave, and golden categories hidden while leaving filler items in their own visible category.

**Token goal**
- Added `mktv_tokens_required` and `mktv_tokens_available_percentage` options to `options.json` and the YAML template.
- `MKTV Token` items are only generated when the selected victory goal requires them.
- Required MKTV Tokens are progression items, while optional surplus tokens are useful items.

**Build**
- Rebuilt `manual_mk8dx_narusnake.apworld` with the updated hooks, options, filler items, and YAML template.

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
- **Goal balancing**: Continue testing the new victory conditions and token variants against real seed logic.
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