# Goals Guide

The goal option decides which victory location must be completed. Token variants add an MKTV Token requirement on top of the base objective.

## Available Goals
- `All Rainbow Roads Complete`: complete every enabled Rainbow Road cup requirement.
- `Mario Kart 8 Token`: collect the configured amount of MKTV Tokens.
- `All Grand Prix Cups`: complete all enabled Grand Prix cup goals.
- `All Time Trial Ghosts`: complete the enabled Time Trial ghost set.
- `All VS Race Challenges`: complete the enabled VS Race challenge set.
- `All Battle Challenges`: complete the enabled Battle challenge set.
- `All Rainbow Roads Complete + MKTV Tokens`: Rainbow Roads plus tokens.
- `All Grand Prix Cups + MKTV Tokens`: Grand Prix plus tokens.
- `All Time Trial Ghosts + MKTV Tokens`: Time Trial plus tokens.
- `All VS Race Challenges + MKTV Tokens`: VS Race plus tokens.
- `All Battle Challenges + MKTV Tokens`: Battle plus tokens.

## DLC-Aware Goals
Rainbow Road goals adapt to DLC ownership. If the DLC or a wave is disabled, Rainbow Road checks from that disabled content are not required for the goal.

## Time Trial Goal
The Time Trial goal follows `time_trial_checks`. In single mode, it asks for the single ghost set. In split mode, it follows the enabled 150cc and 200cc ghost checks.

When `difficulty_items` is false, the Time Trial goal does not ask for difficulty progression.

## Token Goals
Token goals use `mktv_tokens_required` for the required amount. `mktv_tokens_available_percentage` can place extra tokens, capped at 100 total available tokens.
