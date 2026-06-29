# Manuel Archipelago pour Mario Kart 8 Deluxe

## Bienvenue !
Bienvenue dans le dépôt de l'intégration Manual Archipelago pour **Mario Kart 8 Deluxe**.
Ce projet transforme les objectifs de Mario Kart 8 Deluxe, les coupes, les personnages, les pièces de véhicule, les modes de course, la gestion du DLC et les objectifs de jetons en expérience Archipelago multiworld.

Le manuel vise **Mario Kart 8 Deluxe sur Nintendo Switch**, avec le contenu du Pass circuits additionnels lorsque le joueur le possède. Les checks liés au DLC et aux vagues peuvent être activés ou désactivés depuis le YAML afin de correspondre au contenu réellement possédé par le joueur.

## État du projet
Le projet est actuellement en **Version 1.0.0 - Release Update**.
La Version 1.0.0 est la première base de release complète du manuel Mario Kart 8 Deluxe.
Cette release se concentre sur un filtrage stable du contenu depuis le YAML, un comportement propre du pool d'items, la classification dynamique de la progression, les guides détaillés, la logique de challenges élargie, les checks fantôme Time Trial, le départ de seed, les options DLC, les variantes de personnages, la configuration MKTV Token et la base stable Manual Archipelago rafraîchie (`manual_stable_20260319`).

## Fonctionnalités actuelles
- **Choix de l'objectif de victoire**
  Choisir entre Rainbow Roads, MKTV Tokens, Grand Prix, Time Trial, VS Race, Battle, ou une variante MKTV Token pour chaque objectif non-token.
- **Options de cylindrée**
  Activer ou désactiver les checks 50cc, 100cc, 150cc, Mirror et 200cc depuis le YAML. `difficulty_items` peut aussi retirer totalement la progression par cylindrée, retirer ces items du pool et remplacer les checks avec cylindrée par des checks propres sans difficulté.
- **Mode de checks Time Trial**
  Choisir entre un check de fantôme Nintendo par circuit ou des checks Time Trial séparés en 150cc et 200cc.
- **Options DLC et vagues**
  Activer ou désactiver tout le contenu DLC, puis choisir individuellement les vagues du Pass circuits additionnels de la Wave 1 à la Wave 6.
- **Options d'unlocks dorés**
  Activer ou désactiver tous les unlocks dorés ensemble, ou gérer individuellement Golden Mario, Gold Standard, Gold Tires et Golden Glider.
- **Options fines de contenu**
  Activer globalement ou individuellement les modes de jeu et les modes Battle depuis le YAML. Les settings de mode sont contrôlés par familles propres : teams, règles d'items, durée de round, COM, véhicules COM, règles de course, rounds Battle et courses VS Race. Une seule option `race_items` contrôle tous les items de course, et une seule option `kart` contrôle ensemble les karts, roues et ailes.
- **Modes de variantes de personnages**
  Choisir si les personnages partageant une case de sélection utilisent des items séparés, des items `Progressive - Character` répétés ou un seul unlock character-only pour toutes les formes/couleurs.
- **Objectif jetons configurable**
  Définir le nombre de MKTV Tokens requis et le surplus disponible depuis le YAML. Les tokens sont retirés du pool quand l'objectif choisi ou sa variante token n'en a pas besoin.
- **Pool d'objets filler**
  Utilise la catégorie dédiée `Filler` avec les fillers traduits en anglais pour remplir les emplacements supplémentaires du pool.
- **Modes de course couverts**
  Inclut Grand Prix, VS Race, les checks fantôme Time Trial et les checks de 10 pièces. Les checks 10 pièces en 150cc et 200cc peuvent aussi être faits en Time Trial.
- **Logique des settings Battle**
  Ajoute des items de configuration Battle pour les équipes, règles d'items, durée des rounds, nombre de rounds, difficulté COM, véhicules COM et ordre des arènes. Les checks Battle demandent une configuration valide et au moins un item de combat non-Coin.
- **Checks de placement**
  Terminer une course Grand Prix ou VS Race à chaque position exacte, de la 1re à la 12e place. Ces checks utilisent les requirements de catégorie `|@Difficulty:1|` et `|@Cups:1|`, afin de garder une logique compacte tout en acceptant n'importe quelle cylindrée et n'importe quelle coupe débloquée.
- **Challenges VS Race**
  Ajoute des challenges optionnels VS Race pour gagner de 4 à 48 courses avec ou sans teams, contrôlés par l'option YAML `vs_race_challenges`.
- **Challenges Battle**
  Ajoute des challenges optionnels Battle Mode par nombre de rounds pour chaque mode Battle, contrôlés par l'option YAML `battle_challenges`.
- **Challenges de circuits**
  Ajoute des petits challenges optionnels de circuit et des challenges liés aux personnages, rangés par catégorie de coupe et contrôlés par l'option YAML `track_challenges`.
- **Challenges d'items**
  Ajoute des checks optionnels pour utiliser chaque item de course, contrôlés par l'option YAML `item_challenges`. Ils peuvent être faits en Grand Prix, VS Race ou Battle Mode.
- **Challenges de karts**
  Ajoute des checks optionnels pour gagner une course avec chaque kart, roue et aile, contrôlés par l'option YAML `kart_challenges`.
- **Grand pool d'objets**
  Randomise personnages, coupes, modes bataille, modes de jeu, difficultés, settings de modes, karts, roues, ailes, objets de course, tokens et fillers.
- **Départ de seed**
  La seed commence avec un objet aléatoire de catégories importantes comme mode de jeu, difficulté, coupe, personnage, kart, roues et aile. Si le mode de départ est VS Race ou Battle, la seed précollecte aussi les settings nécessaires pour rendre la logique du challenge le plus court accessible. Les starts VS Race utilisent `No Items or Coins` et `4 Races`.
- **Guides détaillés**
  Des guides explicatifs sont disponibles dans `docs/guide_en/` et `docs/guide_fr/`.

---

## Notes de version

### Version 1.0.0 - Release Update

**Base de release**
- Passage du projet en Version 1.0.0 comme première base complète de release.
- Finalisation de la structure YAML pour les objectifs, modes de jeu, DLC, options de gameplay, unlocks, checks, settings de mode, settings Battle et contrôles items/locations.
- Suppression des options exemple restantes du template Manual dans le YAML et les données d'options générées afin que la configuration exemple ne contienne que de vraies options MK8DX.

**Polissage des exclusions de contenu**
- Les catégories désactivées par option retirent maintenant leurs items et checks liés de la seed active, au lieu de laisser de faux items progression visibles.
- `difficulty_items: false` retire les items 50cc, 100cc, 150cc, Mirror et 200cc du pool, cache les checks avec cylindrée et utilise des variantes propres sans difficulté.
- `race_items: false` retire tous les items de course, et `kart: false` retire ensemble les karts, roues et ailes.
- Les toggles de modes de jeu et de modes Battle fonctionnent maintenant comme des options de release plutôt que comme des settings brouillons par item.

**Classification progression**
- La classification des items suit maintenant la logique YAML active : un item activé reste progression uniquement s'il peut satisfaire un requirement actif de location, catégorie, région ou objectif.
- Un item progression encore activé mais devenu inutile pour tous les requirements actifs est rétrogradé en filler afin de ne pas afficher une fausse progression au joueur.

**Documentation et build**
- Mise à jour des README anglais/français et des guides items pour expliquer la différence entre les items retirés du pool et les items rétrogradés en filler.
- Déplacement du README français et des guides détaillés dans le dossier `docs/` à la racine du dépôt afin qu'ils ne soient pas embarqués dans le package `.apworld`, tout en gardant les docs de setup Archipelago dans `manual_mk8dx_narusnake/docs/` pour le support WebWorld/tutorials.
- Reconstruction de `manual_mk8dx_narusnake.apworld` avec les hooks de release mis à jour.

### Version 0.12.0 - Mise à jour des checks

**Mode de checks Time Trial**
- Ajout de l'option YAML `time_trial_checks` avec les modes `single` et `split_150_200`.
- `single` crée un check de fantôme Nintendo par circuit, sans requirement de cylindrée.
- `split_150_200` crée des checks de fantôme Nintendo séparés pour le 150cc et le 200cc.
- Retrait des doublons de checks fantôme Time Trial en 100cc et Mirror de la liste active des locations.
- Time Trial reste disponible pour les checks 10 pièces en 150cc et 200cc, tandis que les checks 50cc, 100cc et Mirror demandent Grand Prix ou VS Race.

**Checks de placement**
- Ajout de 12 checks `Race Placements` pour terminer une course Grand Prix ou VS Race de la 1re à la 12e place.
- Les checks de placement demandent Grand Prix ou VS Race, une cylindrée débloquée et une coupe débloquée, sans forcer une difficulté précise.

**Logique des settings Battle**
- Ajout de 25 items `Mode Settings` pour configurer Battle : équipes, règles d'items, durée des rounds, nombre de rounds, difficulté COM, véhicules COM et ordre des arènes.
- Ajout de la catégorie cachée `Battle Damage Items` à tous les items de course sauf `Coin`, afin que les checks Battle demandent au moins un item capable d'affecter les adversaires.
- Les checks de victoire Battle demandent maintenant leur mode Battle, une configuration Battle valide et les exceptions propres aux modes : Renegade Roundup ne demande pas les teams, et Shine Thief ne demande pas la durée des rounds.

**Challenges VS Race**
- Ajout de 15 items `Mode Settings` spécifiques à VS Race, en réutilisant les settings partagés d'équipes, COM, véhicules et ordre de courses quand c'est possible.
- Ajout de 80 checks optionnels `VS Race Challenges` : cinq cylindrées, huit longueurs de 4 à 48 courses, et les variantes teams/no teams.
- Les challenges VS Race demandent VS Race, la cylindrée choisie, le nombre de courses, un setting de team, les settings VS item/COM/véhicule/course et assez de coupes débloquées via `|@Cups:N|`.
- Ajout de l'option YAML `vs_race_challenges` pour activer ou désactiver ces checks.

**Challenges Battle**
- Ajout de 54 checks optionnels `Battle Challenges` : six nombres de rounds de 4 à 24 rounds sur les modes Battle.
- Balloon Battle, Bob-omb Blast, Coin Runners et Shine Thief ont des variantes teams et no teams.
- Renegade Roundup ne demande pas de setting de team, et Shine Thief ne demande pas de setting de durée de round.
- Les challenges Battle demandent Battle, le mode Battle choisi, le nombre de rounds, les settings Battle item/COM/véhicule/course et au moins un item Battle non-Coin.
- Ajout de l'option YAML `battle_challenges` pour activer ou désactiver ces checks.

**Challenges de circuits**
- Ajout de 96 checks optionnels `Track Challenges`, un par circuit, rangés par catégorie de coupe et contrôlés par l'option YAML `track_challenges`.
- Ajout de 45 challenges course-personnage pour les circuits nommés d'après, ou fortement liés à, un personnage jouable ou une espèce jouable.
- Les challenges d'objet de circuit demandent un mode de course, une cylindrée débloquée et la coupe concernée. Les challenges course-personnage demandent Grand Prix ou VS Race, le personnage lié, une cylindrée débloquée et la coupe concernée.
- Réorganisation des locations de coupe pour respecter l'ordre des coupes en jeu.

**Challenges d'items**
- Ajout de 23 checks optionnels `Item Challenges`, un pour chaque item de course.
- Les challenges d'items demandent l'item et soit Grand Prix ou VS Race avec une cylindrée et une coupe débloquées, soit Battle avec un mode Battle débloqué.

**Challenges de karts**
- Ajout de 63 checks optionnels `Kart Challenges` : 29 karts, 19 roues et 15 ailes.
- Les challenges de karts, roues et ailes demandent la pièce de véhicule liée, Grand Prix ou VS Race, une cylindrée débloquée et une coupe débloquée.

**Logique de départ**
- Ajout de settings de départ conditionnels pour les starts VS Race et Battle.
- Les starts VS Race reçoivent maintenant un setting de team, item, COM, véhicule COM, ordre de courses et `4 Races`.
- Les starts Battle reçoivent maintenant un setting de team, item, item de combat, COM, véhicule COM, ordre des arènes, `4 Rounds` et une durée de round.

**Mise à jour des objectifs**
- Remplacement de l'ancienne liste de goals brouillons par 11 objectifs de victoire propres.
- `All Rainbow Roads Complete` et `Mario Kart 8 Token` restent en première position afin de garder les alias existants stables.
- Ajout d'objectifs Grand Prix, Time Trial, VS Race et Battle basés sur les vraies catégories d'items et les settings de mode.
- Ajout de variantes MKTV Token pour chaque objectif non-token.
- Retrait des requirements cassés qui utilisaient les anciennes catégories `@round`, `@round battle` et `@cups` en minuscules.

**Mise à jour des options fines**
- Ajout de toggles YAML globaux et individuels pour les modes de jeu et modes Battle, puis regroupement des settings de mode par familles : teams, règles d'items, durée de round, COM, véhicules COM, règles de course, rounds Battle et courses VS Race. Ajout d'une option globale `race_items` pour tous les items de course et d'une option globale `kart` pour les karts, roues et ailes ensemble.
- Ajout de `difficulty_items` pour retirer les items de cylindrée du pool, cacher les checks avec cylindrée et utiliser des variantes propres sans difficulté.
- Suppression des options exemple restantes du template Manual dans le YAML et les données d'options générées.
- Les familles d'options Battle Mode et Mode Setting sont maintenant désactivées par défaut dans le template YAML généré.
- Correction des checks VS Race de Wii Wario's Gold Mine en Triforce Cup pour 50cc, 100cc, 150cc et Mirror afin que le filtrage sans difficulté les traite correctement.
- La classification des items suit maintenant la logique YAML active : les catégories désactivées par option sont retirées du pool, tandis qu'un item activé reste progression uniquement s'il peut satisfaire un requirement actif de location, catégorie, région ou objectif. Un item progression encore activé mais devenu inutile est rétrogradé en filler.
- Les starts VS Race précollectent maintenant `No Items or Coins` et `4 Races` lorsque VS Race est le mode de départ.
- La logique Battle retire le requirement `@Battle Damage Items:1` quand tous les items de dégâts Battle sont désactivés.

**Documentation guide**
- Ajout de guides anglais et français couvrant les options, objets, checks et objectifs avec de vraies explications pratiques.
- Les listes détaillées restent hors du README principal afin de garder les notes de version lisibles.

**Build**
- Reconstruction de `manual_mk8dx_narusnake.apworld` avec la nouvelle option Time Trial, les settings Battle/VS, les catégories et les données de locations.

### Version 0.11.0 - Character Update

**Option de variantes de personnages**
- Ajout de l'option globale `character_variants` avec les modes `separate`, `progressive` et `character_only`.
- `separate` reste le défaut afin que les checks personnages gardent le comportement des versions précédentes tant que le joueur ne change pas l'option.
- Ajout des items character-only et progressifs pour Birdo, Yoshi, Shy Guy, Inkling, Villager, Link, Mii et les Koopalings.

**Logique progressive et character-only**
- Les checks de variantes acceptent maintenant l'item exact, le compteur `Progressive - Character:N` correspondant ou l'item character-only de base.
- `character_only` débloque toutes les couleurs/formes du groupe en une fois.
- `progressive` débloque les couleurs/formes dans l'ordre de sélection configuré en demandant plusieurs copies de l'item progressif.
- Le groupe Birdo respecte toujours les options DLC et Wave 4.

**Nettoyage des requirements**
- Conversion des requirements de locations au format explicite `|Item| AND (|A| OR |B|)` pour harmoniser la logique.
- Harmonisation des requirements OR des modes de course utilisés par les checks de 10 pièces.

**Ordre des items**
- Réorganisation de `items.json` par catégorie, puis par ordre alphabétique dans chaque catégorie.
- Conservation de l'ordre de sélection personnalisé pour les groupes de personnages à plusieurs couleurs/formes.

### Version 0.10.0 - Filler Update

**Adaptation des hooks**
- Reprise de la structure de hooks du manuel Tekken 3 et adaptation à MK8D pour `Data.py`, `Helpers.py`, `Options.py`, `Rules.py` et `World.py`.
- Ajout d'un filtrage côté hooks pour les cylindrées, les vagues DLC et les unlocks dorés afin que les options YAML désactivées retirent bien les objets et checks liés.
- Ajout de clés de tri automatiques pour les locations et propagation des catégories DLC, waves et golden via hooks.

**Objets filler**
- Traduction en anglais des 72 nouveaux objets filler dans `items.json`.
- Ajout d'une sélection de filler basée sur la catégorie `Filler`, afin que les emplacements supplémentaires utilisent la liste dédiée MK8D.
- Les catégories techniques DLC, waves et golden restent cachées, tandis que les fillers restent dans leur catégorie visible.

**Objectif token**
- Ajout des options `mktv_tokens_required` et `mktv_tokens_available_percentage` dans `options.json` et dans le template YAML.
- Les objets `MKTV Token` sont générés uniquement lorsque l'objectif de victoire sélectionné les demande.
- Les MKTV Tokens requis sont en progression, tandis que les tokens de surplus sont classés utiles.

**Build**
- Reconstruction de `manual_mk8dx_narusnake.apworld` avec les hooks, options, fillers et template YAML mis à jour.

### Version 0.9.0 - DLC Update

**Options DLC et vagues**
- Ajout de l'option YAML `dlc` pour activer ou désactiver tout le contenu DLC et Pass circuits additionnels.
- Ajout de `dlc_wave_1` à `dlc_wave_6` pour permettre aux joueurs d'inclure uniquement les vagues du Pass circuits additionnels qu'ils possèdent.
- `dlc = false` désactive toutes les vagues individuelles, même si une wave est réglée sur true.
- Ajout de catégories techniques cachées pour `DLC` et chaque wave afin de filtrer les objets et checks sans afficher d'onglets supplémentaires dans le client.

**Options d'unlocks dorés**
- Ajout de l'option YAML `golden` pour activer ou désactiver tous les unlocks dorés en une seule fois.
- Ajout d'options individuelles pour `golden_mario`, `gold_standard`, `gold_tires` et `golden_glider`.
- `golden = false` désactive toutes les options dorées individuelles.
- Les catégories techniques DLC, waves et golden restent cachées afin que l'affichage du client reste centré sur les catégories d'origine.

**Logique et objectifs**
- Propagation des catégories DLC, waves et golden vers les locations liées via hooks, au lieu de dupliquer manuellement ces données dans chaque check.
- Mise à jour de `All Rainbow Roads Complete` afin qu'il ne demande plus les coupes DLC lorsque le DLC ou la wave concernée est désactivée.
- Reconstruction de `manual_mk8dx_narusnake.apworld` avec les options, hooks et documents mis à jour.

---

### Version 0.8.0 - Mise à jour Manual stable

**Mise à jour du framework Manual**
- Synchronisation du package source avec la base stable récente de Manual Archipelago (`manual_stable_20260319`).
- Mise à jour des fichiers principaux de Manual pour le chargement des données, la création d'objets, les règles, les régions, les options, la validation, les helpers et le client.
- Ajout de `container.py` pour le support moderne des conteneurs `.apmanual` au format zip.
- Ajout d'un `data/events.json` vide afin de préparer le projet au système d'événements actuel de Manual.
- Ajout du package de tests stable dans `manual_mk8dx_narusnake/test/`.
- Mise à jour de la base du client Manual avec un meilleur support tracker, les réglages client, le tri des objets/locations, le rafraîchissement de recherche, le support UI DeathLink et la lecture moderne des `.apmanual`.
- Reconstruction de `manual_mk8dx_narusnake.apworld` depuis le package source mis à jour.

**Données et options MK8DX**
- Conservation des données d'objets et de locations Mario Kart 8 Deluxe pendant la mise à jour du framework autour du projet.
- Conservation des options YAML 50cc, 100cc, 150cc, Mirror et 200cc pour contrôler les checks générés.
- Conservation des deux objectifs principaux : `All Rainbow Roads Complete` et `Mario Kart 8 Token`.
- Correction d'une location VS Race en 200cc dans la Triforce Cup afin qu'elle demande bien la catégorie 200cc et apparaisse dans la catégorie attendue.
- Suppression de l'ancien flag metadata `enable_region_diagram`; le framework Manual actuel expose maintenant la génération du diagramme via une option cachée.

**Documentation**
- Réécriture du README principal avec la mise en page plus claire du manuel Super Street Fighter II.
- Ajout de ce README français dans `docs/README_FR.md`.
- Suppression des changelogs inutilisés dans `docs/`.

**Notes pour cette version**
- Reconstruire le `.apworld` après toute modification des sources avant de préparer une version distribuable.
- Un import runtime complet demande que l'environnement Archipelago soit disponible dans le `PYTHONPATH`.

---

### Version 0.7.0 - Mise à jour CC
- Restructuration de `items.json`.
- Ajout des objets pour 50cc, 100cc, 150cc, Mirror et 200cc.
- Mise à jour du template YAML avec les options 50cc, 100cc, 150cc, Mirror et 200cc.
- Mise à jour des checks pour utiliser les nouvelles catégories de cylindrée.

---

### Version 0.6.0 - Mise à jour des objets
- Ajout de tous les objets du jeu dans le pool Archipelago.
- Passage du filler à la configuration `MKFan`.

---

### Version 0.5.0 - Mise à jour Time Trial
- Ajout des checks Time Trial et de l'objet correspondant.
- Ajout des checks de 10 pièces en course.
- Mise à jour de `game.json` pour inclure Battle Mode dans la génération des objets de départ.

---

### Version 0.4.1 - Correctifs
- Correction de problèmes causés par une migration Archipelago.

---

### Version 0.4.0 - Migration
- Mise à jour du code vers le framework Manual Archipelago utilisé à ce moment-là.

---

### Version 0.3.0 - Mise à jour VS Race
- Ajout d'une catégorie d'objets **Game Modes**.
- Ajout de la catégorie de checks **VS Race**.
- Renommage des checks **Win the cups with...** en **Win a race with...**.
- Ajout d'options de mode de jeu dans la configuration de seed.
- Ajustement du nombre de jetons à 100.

---

### Version 0.2.0 - Mise à jour personnages
- Ajout des variantes de couleur de Birdo, Yoshi et Shy Guy.
- Ajout de Golden Mario.
- Ajout des variantes Inkling.
- Ajout de Male Villager et Female Villager.
- Ajout des variantes de Link.
- Ajout de tous les Miis.
- Ajout de 25 Tokens comme objets.
- Ajout de l'objectif **Mario Kart 8 Token**.
- Ajout des checks **Win any Cup with...** pour la liste de personnages.

**Note connue**
- Si Golden Mario n'est pas débloqué, le check correspondant peut être validé avec Metal Mario.

---

### Version 0.1.0 - Version initiale
- Ajout des objets dans les catégories **Characters**, **Karts**, **Wheels** et **Gliders**.
- Ajout des checks de complétion de coupes, avec 1re place et trophées bronze, argent et or.
- Ajout des checks de victoire avec les personnages.

---

## Feuille de route
- **Équilibrage des objectifs** : continuer à tester les nouvelles conditions de victoire et leurs variantes token sur de vraies seeds.
- **Polissage des catégories** : revoir la visibilité et le groupement des catégories dans le client Manual.
- **Revue de logique** : continuer à vérifier la cohérence des checks 200cc, VS Race, Time Trial, pièces et cas limites DLC.
- **Modernisation du YAML** : rafraîchir le template YAML avec des patterns Archipelago plus récents et des commentaires plus clairs.

---

## Contribution
Les retours et contributions sont les bienvenus.
- Signaler les bugs ou proposer des idées via les issues GitHub.
- Envoyer des PRs avec des corrections de données, de logique ou de compatibilité framework.
- Améliorer la documentation, les instructions de setup ou les exemples YAML.

---

## Remerciements
Ce manuel est inspiré par le travail de RampantEpsilon et JokerFactor, ainsi que par la communauté Manual for Archipelago.

---

## Contact
Questions, streams ou bugs ? Passez par le Discord Archipelago ou ouvrez une issue GitHub.
