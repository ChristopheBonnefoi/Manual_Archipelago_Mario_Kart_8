# Guide des objectifs

L'option `goal` choisit quelle location de victoire doit être validée. Les variantes avec MKTV Tokens ajoutent une demande de tokens au-dessus de l'objectif de base.

## Objectifs disponibles
- `All Rainbow Roads Complete` : compléter les Rainbow Roads actifs selon les options DLC.
- `Mario Kart 8 Token` : collecter le nombre configuré de MKTV Tokens.
- `All Grand Prix Cups` : compléter les objectifs Grand Prix actifs.
- `All Time Trial Ghosts` : compléter le set actif de fantômes Time Trial.
- `All VS Race Challenges` : compléter les VS Race Challenges actifs.
- `All Battle Challenges` : compléter les Battle Challenges actifs.
- `All Rainbow Roads Complete + MKTV Tokens` : Rainbow Roads plus tokens.
- `All Grand Prix Cups + MKTV Tokens` : Grand Prix plus tokens.
- `All Time Trial Ghosts + MKTV Tokens` : Time Trial plus tokens.
- `All VS Race Challenges + MKTV Tokens` : VS Race plus tokens.
- `All Battle Challenges + MKTV Tokens` : Battle plus tokens.

## Objectifs compatibles DLC
Les objectifs Rainbow Road s'adaptent au DLC. Si le DLC ou une wave est désactivé, les Rainbow Roads de ce contenu ne sont pas demandées pour la victoire.

## Objectif Time Trial
L'objectif Time Trial suit `time_trial_checks`. En mode single, il demande le set unique de fantômes. En mode split, il suit les checks 150cc et 200cc actifs.

Quand `difficulty_items` est false, l'objectif Time Trial ne demande pas de progression par difficulté.

## Objectifs avec tokens
Les goals avec tokens utilisent `mktv_tokens_required` pour le montant requis. `mktv_tokens_available_percentage` peut placer des tokens en surplus, avec un maximum de 100 tokens disponibles au total.
