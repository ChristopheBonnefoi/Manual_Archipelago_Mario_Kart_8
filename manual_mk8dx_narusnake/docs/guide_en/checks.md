# Checks Guide

A check is a location the player can mark complete in the Manual client. The requirement string describes what items must be received before the check is logically available.

## Reading Requirements
`|Item Name|` means the exact item is required.

`|@Category:1|` means at least one item from that category is required. For example, `|@Cups:1|` means any unlocked cup works.

`|@Category:all|` means every enabled item from that category is required.

`AND` means all parts are required. `OR` means either side is acceptable.

## Grand Prix And VS Race Checks
Cup completion, race win, 10-coin, and placement checks usually require a mode, a cup, and sometimes a difficulty. VS Race uses 12 participants, so placement checks from 1st through 12th are valid for Grand Prix and VS Race.

When `difficulty_items` is false, engine-specific checks are hidden and clean no-difficulty variants are shown instead. Those active checks can be cleared in any engine class.

## Time Trial Checks
`time_trial_checks: single` creates one Nintendo ghost check per course without engine-class logic.

`time_trial_checks: split_150_200` creates 150cc and 200cc ghost checks. Time Trial is also valid for 150cc and 200cc 10-coin checks because coins are available in that mode.

## Track Challenges
Track challenges are optional checks tied to courses. Some are simple course actions, while others use broader character or universe references such as Mario, Toad, Bowser, Yoshi, Animal Crossing, Hyrule, F-Zero, Excitebike, and similar themed tracks.

These checks are controlled by `track_challenges` and are grouped by cup in the Manual client.

## Item Challenges
Item challenges ask the player to use a specific race item. They can usually be completed in Grand Prix, VS Race, or Battle when the required mode logic is unlocked.

If `race_items` or `item_challenges` is false, these checks are removed.

## Kart Challenges
Kart challenges ask the player to win with a specific kart body, wheel, or glider. They live under one client category and are controlled by `kart_challenges`.

If `kart` is false, the vehicle part items and direct vehicle challenges are removed together.

## VS Race Challenges
VS Race challenges ask the player to win a configured number of races with either teams or no teams. They require VS Race, a race count setting, a team setting, item/COM/course settings, enough unlocked cups, and the selected difficulty when difficulty progression is enabled.

The race count settings are controlled together by `mode_setting_races`.

## Battle Checks
Battle victory and Battle challenge checks require Battle, the selected Battle mode, and valid mode settings. Most Battle checks also require at least one non-Coin battle damage item unless `race_items` is false.

Renegade Roundup does not require team settings. Shine Thief does not require round-time settings.
