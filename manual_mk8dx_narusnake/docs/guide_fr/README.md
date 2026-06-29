# Guide Manual Mario Kart 8 Deluxe

Ce guide explique comment le monde Manual MK8DX est pensé côté options, objets, checks et objectifs. Il ne recopie pas chaque ligne de `locations.json`; les fichiers de données existent déjà pour ça. Ici, le but est d'expliquer la logique pour que le joueur comprenne quoi activer dans son YAML et pourquoi.

## Fichiers
- [Options](options.md) : ce que chaque groupe YAML contrôle et comment les options interagissent.
- [Objets](items.md) : le rôle des catégories d'objets dans la logique.
- [Checks](checks.md) : les familles de checks et la lecture des requirements.
- [Objectifs](goals.md) : les conditions de victoire disponibles.

## Portée actuelle
- 11 objectifs de victoire.
- Logique Grand Prix, VS Race, Time Trial et Battle Mode.
- Filtrage du DLC et des vagues du Pass circuits additionnels.
- Gestion des variantes de personnages : séparées, progressives ou personnage seul.
- Options globales pour les items de course et les pièces de véhicule.
- Settings de mode regroupés par familles pour garder un YAML lisible.

## Comportements importants
`difficulty_items: false` retire la progression par cylindrée, cache les checks avec cylindrée et affiche des variantes propres sans difficulté. Les checks actifs peuvent donc être validés dans la cylindrée que le joueur veut.

`dlc: false` désactive toutes les vagues, même si une option comme `dlc_wave_3` est sur true.

`race_items: false` retire les items de course et les checks qui demandent directement ces items. Les checks Battle ne demandent plus d'item de dégâts Battle.

`kart: false` retire ensemble les karts, roues, ailes et les challenges qui demandent directement ces pièces.
