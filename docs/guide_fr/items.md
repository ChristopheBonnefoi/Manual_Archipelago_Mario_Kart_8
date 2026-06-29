# Guide des objets

Les objets représentent ce que le joueur a le droit d'utiliser pour les checks. Si un check demande `|VS Race|`, le joueur doit avoir reçu l'item VS Race avant que ce check soit logiquement disponible.

La classification progression est ajustée selon le YAML actif. Les catégories désactivées par option sont retirées du pool ; un item activé reste progression uniquement s'il peut satisfaire un requirement actif de location, catégorie, région ou objectif. Un item progression encore activé mais devenu inutile est rétrogradé en filler.

## Catégories principales
**Game Modes** débloque Grand Prix, VS Race, Time Trial et Battle. Ces items décident quelles grandes parties du jeu peuvent être utilisées.

**Cups** débloque les groupes de circuits. Les requirements de coupe apparaissent soit avec le nom exact de la coupe, soit avec un format compact comme `|@Cups:1|`.

**Difficulty** contient 50cc, 100cc, 150cc, Mirror et 200cc quand `difficulty_items` est actif. Quand `difficulty_items` est désactivé, ces items sont retirés du pool et les checks sans difficulté sont utilisés à la place.

**Characters** débloque les pilotes. Certains personnages qui partagent une case peuvent être séparés, progressifs ou débloqués avec un seul item selon `character_variants`.

## Items de course
Les items de course sont contrôlés par `race_items`. Si cette option est désactivée, le pool ne contient plus ces items de progression et les checks qui demandent directement un item de course sont retirés.

Pour Battle, tous les items de course sauf Coin comptent comme item pouvant toucher un adversaire. Si les items de course sont désactivés, les checks Battle ne demandent plus `@Battle Damage Items:1`.

## Pièces de véhicule
Les karts, roues et ailes sont contrôlés ensemble par `kart`. Côté client, ils restent dans leurs catégories normales, mais côté YAML un seul switch suffit pour éviter une configuration interminable.

## Settings de mode
Les settings de mode sont aussi des items. Ils représentent les réglages de menu comme Team Game, No Items or Coins, Hard COM, 4 Rounds ou 12 Races.

Le YAML les contrôle par familles. Par exemple, `mode_setting_races` active tous les items de nombre de courses VS Race, de 4 Races à 48 Races.

## MKTV Tokens
Les MKTV Tokens sont générés uniquement quand le goal choisi les demande. Les tokens requis sont en progression; les tokens en surplus sont utiles.

## Filler
Les fillers remplissent les emplacements restants après les items de progression et utiles. Ils ne servent pas à la logique.
