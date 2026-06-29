# Guide des options

Le YAML est rangé par usage de jeu plutôt que par ordre brut des données. La plupart des options sont des toggles : `'true'` inclut le contenu, `'false'` le retire de la logique de seed.

## Goal Options
`goal` choisit la condition de victoire. Les variantes avec tokens demandent l'objectif choisi plus le nombre configuré de MKTV Tokens.

`mktv_tokens_required` règle le nombre de MKTV Tokens requis quand le goal en utilise. `mktv_tokens_available_percentage` règle le surplus placé. Si le goal choisi n'a pas besoin de tokens, les MKTV Tokens ne sont pas ajoutés au pool.

## Game Modes
`game_modes` est le parent global pour Grand Prix, VS Race, Time Trial et Battle. Les options individuelles permettent de retirer un mode que le joueur ne veut pas faire.

Il faut garder au moins un mode actif. Si une location dépend uniquement de modes désactivés, elle est retirée du monde généré.

## DLC Options
`dlc` est l'interrupteur principal. S'il est à false, toutes les coupes DLC, personnages DLC, checks DLC et vagues sont retirés.

Les options de wave permettent d'inclure uniquement les vagues possédées par le joueur. Elles sont ignorées quand `dlc` est false.

## Gameplay Options
`difficulty_items` contrôle l'existence des items 50cc, 100cc, 150cc, Mirror et 200cc. Quand cette option est désactivée, les checks avec cylindrée sont cachés et des variantes propres sans difficulté sont affichées à la place.

`race_items` contrôle tous les items de course en un seul bloc. `kart` contrôle ensemble les karts, roues et ailes.

`character_variants` contrôle les personnages qui partagent une case de sélection :
- `separate` : chaque couleur ou forme est un item séparé.
- `progressive` : des items `Progressive - Character` répétés débloquent les variantes dans l'ordre.
- `character_only` : un seul item de personnage de base débloque toutes les variantes du groupe.

## Check Options
Ces toggles ajoutent ou retirent des familles de checks optionnels :
- `track_challenges` : challenges de circuits et références personnage/circuit.
- `item_challenges` : checks d'utilisation des items de course.
- `kart_challenges` : checks de victoire avec karts, roues et ailes.
- `vs_race_challenges` : challenges de nombre de courses en VS Race.
- `battle_challenges` : challenges de nombre de rounds en Battle.

`time_trial_checks` choisit entre un check de fantôme Nintendo par circuit ou des checks Time Trial séparés 150cc/200cc.

## Mode Setting Options
Les settings de mode sont regroupés par familles au lieu d'avoir une option YAML par item :
- `mode_setting_teams` : Team Game et No Teams.
- `mode_setting_items` : règles d'items Battle et VS Race, dont No Items or Coins et les règles item-only.
- `mode_setting_round_time` : timers Battle de 1 à 5 minutes.
- `mode_setting_com` : Easy, Normal et Hard COM.
- `mode_setting_com_vehicles` : All Vehicles, Kart Only et Bikes Only.
- `mode_setting_courses` : Choose Courses, In Order Courses et Random Courses.
- `mode_setting_rounds` : nombres de rounds Battle de 4 à 24.
- `mode_setting_races` : nombres de courses VS Race de 4 à 48.

Désactiver une famille retire les settings liés et les checks qui demandent directement cette famille.

## Battle Mode Options
`battle_modes` est le parent des cinq modes Battle. Les options individuelles retirent le mode Battle correspondant et les checks qui le demandent directement.

## Item And Location Options
Le dernier bloc du YAML contient les options Archipelago standard : local items, non-local items, start inventory, hints, excluded locations, priority locations et item links.
