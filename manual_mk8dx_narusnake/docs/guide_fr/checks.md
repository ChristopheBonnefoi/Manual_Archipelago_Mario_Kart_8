# Guide des checks

Un check est une location que le joueur peut valider dans le client Manual. Le champ `requires` décrit les items nécessaires pour que le check soit logiquement disponible.

## Lire les requirements
`|Nom de l'item|` veut dire que l'item exact est requis.

`|@Catégorie:1|` veut dire qu'au moins un item de cette catégorie est requis. Par exemple, `|@Cups:1|` accepte n'importe quelle coupe débloquée.

`|@Catégorie:all|` veut dire que tous les items actifs de cette catégorie sont requis.

`AND` veut dire que tout est requis. `OR` veut dire qu'une des possibilités suffit.

## Checks Grand Prix et VS Race
Les checks de coupe, victoire, 10 pièces et placement demandent généralement un mode, une coupe et parfois une difficulté. VS Race utilise bien 12 participants, donc les checks de placement de la 1re à la 12e place sont valides en Grand Prix et en VS Race.

Quand `difficulty_items` est false, les checks avec cylindrée sont cachés et des variantes propres sans difficulté sont affichées à la place. Ces checks actifs peuvent être faits dans n'importe quelle cylindrée.

## Checks Time Trial
`time_trial_checks: single` crée un seul check de fantôme Nintendo par circuit sans logique de cylindrée.

`time_trial_checks: split_150_200` crée des checks fantôme séparés en 150cc et 200cc. Time Trial reste aussi valide pour les checks 10 pièces en 150cc et 200cc, car les pièces sont disponibles dans ce mode.

## Track Challenges
Les Track Challenges sont des checks optionnels liés aux circuits. Certains sont des actions simples sur un circuit, d'autres utilisent des références de personnage ou d'univers comme Mario, Toad, Bowser, Yoshi, Animal Crossing, Hyrule, F-Zero, Excitebike et autres circuits thématiques.

Ils sont contrôlés par `track_challenges` et rangés par coupe dans le client Manual.

## Item Challenges
Les Item Challenges demandent d'utiliser un item de course précis. Ils peuvent généralement être faits en Grand Prix, VS Race ou Battle lorsque les modes nécessaires sont débloqués.

Si `race_items` ou `item_challenges` est false, ces checks sont retirés.

## Kart Challenges
Les Kart Challenges demandent de gagner avec un kart, une roue ou une aile précise. Ils restent dans une seule catégorie côté client et sont contrôlés par `kart_challenges`.

Si `kart` est false, les pièces de véhicule et les challenges directs liés aux véhicules sont retirés ensemble.

## VS Race Challenges
Les VS Race Challenges demandent de gagner un nombre de courses configuré avec ou sans teams. Ils demandent VS Race, un nombre de courses, un setting de team, des settings d'items/COM/courses, assez de coupes débloquées et la difficulté choisie quand la progression par difficulté est active.

Les nombres de courses sont contrôlés ensemble par `mode_setting_races`.

## Checks Battle
Les checks de victoire Battle et les Battle Challenges demandent Battle, le mode Battle choisi et des settings valides. La plupart demandent aussi au moins un item de dégâts non-Coin, sauf si `race_items` est false.

Renegade Roundup ne demande pas de setting de team. Shine Thief ne demande pas de durée de round.
