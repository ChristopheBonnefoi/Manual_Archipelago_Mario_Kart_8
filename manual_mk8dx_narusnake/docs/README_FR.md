# Manuel Archipelago pour Mario Kart 8 Deluxe

## Bienvenue !
Bienvenue dans le dépôt de l'intégration Manual Archipelago pour **Mario Kart 8 Deluxe**.
Ce projet transforme les objectifs de Mario Kart 8 Deluxe, les coupes, les personnages, les pièces de véhicule, les modes de course, la gestion du DLC et les objectifs de jetons en expérience Archipelago multiworld.

Le manuel vise **Mario Kart 8 Deluxe sur Nintendo Switch**, avec le contenu du Pass circuits additionnels lorsque le joueur le possède. Les checks liés au DLC et aux vagues peuvent être activés ou désactivés depuis le YAML afin de correspondre au contenu réellement possédé par le joueur.

## État du projet
Le projet est actuellement en **Version 0.10.0 - Filler Update**.
La Version 1.0.0 reste réservée au moment où le projet sera considéré comme terminé.
Cette mise à jour se concentre sur la gestion des fillers, la configuration de l'objectif MKTV Token et l'adaptation des hooks MK8D à partir du manuel Tekken 3. Elle conserve les options de possession du DLC, le filtrage des vagues du Pass circuits additionnels, les options d'unlocks dorés et la base stable Manual Archipelago déjà rafraîchie (`manual_stable_20260319`).

## Fonctionnalités actuelles
- **All Rainbow Roads Complete**
  Terminer tous les objectifs Rainbow Road inclus dans la seed.
- **Mario Kart 8 Token**
  Récupérer des MKTV Tokens configurables pour l'objectif basé sur les jetons.
- **Options de cylindrée**
  Activer ou désactiver les checks 50cc, 100cc, 150cc, Mirror et 200cc depuis le YAML.
- **Options DLC et vagues**
  Activer ou désactiver tout le contenu DLC, puis choisir individuellement les vagues du Pass circuits additionnels de la Wave 1 à la Wave 6.
- **Options d'unlocks dorés**
  Activer ou désactiver tous les unlocks dorés ensemble, ou gérer individuellement Golden Mario, Gold Standard, Gold Tires et Golden Glider.
- **Objectif jetons configurable**
  Définir le nombre de MKTV Tokens requis et le surplus disponible depuis le YAML. Les tokens sont retirés du pool quand l'objectif choisi n'en a pas besoin.
- **Pool d'objets filler**
  Utilise la catégorie dédiée `Filler` avec les fillers traduits en anglais pour remplir les emplacements supplémentaires du pool.
- **Modes de course couverts**
  Inclut Grand Prix, VS Race, Time Trial et les checks de 10 pièces en course.
- **Grand pool d'objets**
  Randomise personnages, coupes, modes bataille, modes de jeu, difficultés, karts, roues, ailes, objets de course, tokens et fillers.
- **Départ de seed**
  La seed commence avec un objet aléatoire de catégories importantes comme mode de jeu, difficulté, coupe, personnage, kart, roues et aile.

---

## Notes de version

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
- Ajout de ce README français dans `manual_mk8dx_narusnake/docs/README_FR.md`.
- Suppression des changelogs inutilisés dans `manual_mk8dx_narusnake/docs/`.

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
- **Variété des objectifs** : ajouter des conditions de victoire autour des coupes, cylindrées, Time Trials, jetons ou objectifs mixtes.
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