from typing import Any
from worlds.AutoWorld import World
import json
import re
from BaseClasses import MultiWorld, CollectionState, Item

from ..Items import ManualItem
from ..Locations import ManualLocation
from ..Data import game_table, item_table, location_table, region_table
from ..Helpers import get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item

import logging

TOKEN_ITEM_NAME = "MKTV Token"
TOKEN_OPTION_NAME = "mktv_tokens_required"
TOKEN_AVAILABLE_PERCENTAGE_OPTION_NAME = "mktv_tokens_available_percentage"
FILLER_CATEGORY_NAME = "Filler"
FILLER_ITEM_NAMES = tuple(
    item["name"]
    for item in item_table
    if FILLER_CATEGORY_NAME in item.get("category", [])
)

CHARACTER_VARIANT_OPTION_NAME = "character_variants"
CHARACTER_VARIANT_SEPARATE = 0
CHARACTER_VARIANT_PROGRESSIVE = 1
CHARACTER_VARIANT_ONLY = 2
CHARACTER_VARIANT_GROUPS = (
    {
        "base": 'Birdo',
        "progressive": 'Progressive - Birdo',
        "variants": ('Birdo (Pink)', 'Birdo (Light Blue)', 'Birdo (Black)', 'Birdo (Red)', 'Birdo (Yellow)', 'Birdo (White)', 'Birdo (Dark Blue)', 'Birdo (Green)', 'Birdo (Orange)'),
        "required_options": ('dlc', 'dlc_wave_4'),
    },
    {
        "base": 'Yoshi',
        "progressive": 'Progressive - Yoshi',
        "variants": ('Yoshi (Green)', 'Yoshi (Light Blue)', 'Yoshi (Black)', 'Yoshi (Red)', 'Yoshi (Yellow)', 'Yoshi (White)', 'Yoshi (Dark Blue)', 'Yoshi (Pink)', 'Yoshi (Orange)'),
        "required_options": (),
    },
    {
        "base": 'Shy Guy',
        "progressive": 'Progressive - Shy Guy',
        "variants": ('Shy Guy (Red)', 'Shy Guy (Light Blue)', 'Shy Guy (Black)', 'Shy Guy (Green)', 'Shy Guy (Yellow)', 'Shy Guy (White)', 'Shy Guy (Dark Blue)', 'Shy Guy (Pink)', 'Shy Guy (Orange)'),
        "required_options": (),
    },
    {
        "base": 'Inkling',
        "progressive": 'Progressive - Inkling',
        "variants": ('Inkling Girl (Orange Hair)', 'Inkling Girl (Green Hair)', 'Inkling Girl (Pink Hair)', 'Inkling Boy (Dark Blue Hair)', 'Inkling Boy (Purple Hair)', 'Inkling Boy (Cyan Hair)'),
        "required_options": (),
    },
    {
        "base": 'Villager',
        "progressive": 'Progressive - Villager',
        "variants": ('Male Villager', 'Female Villager'),
        "required_options": (),
    },
    {
        "base": 'Link',
        "progressive": 'Progressive - Link',
        "variants": ('Link (Green Tunic)', 'Link (BOTW)'),
        "required_options": (),
    },
    {
        "base": 'Mii',
        "progressive": 'Progressive - Mii',
        "variants": ('Mii (Yours)', 'Mii (male player in a red outfit)', 'Mii (female player in a pink outfit)', 'Mii (male player in a green outfit)', 'Mii (female player in a yellow outfit)', 'Mii (male player in a dark blue outfit)', 'Mii (female player in a light blue outfit)'),
        "required_options": (),
    },
    {
        "base": 'Koopalings',
        "progressive": 'Progressive - Koopalings',
        "variants": ('Lemmy', 'Larry', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton'),
        "required_options": (),
    },
)

RAINBOW_ROAD_GOAL_REQUIREMENTS = [
    ("Special Cup", None),
    ("Lightning Cup", None),
    ("Triforce Cup", None),
    ("Moon Cup", "dlc_wave_3"),
    ("Spiny Cup", "dlc_wave_6"),
]
RAINBOW_ROAD_GOAL_NAMES = (
    "All Rainbow Roads Complete",
    "All Rainbow Roads Complete + MKTV Tokens",
)
TIME_TRIAL_GOAL_NAMES = (
    "All Time Trial Ghosts",
    "All Time Trial Ghosts + MKTV Tokens",
)
TIME_TRIAL_CHECKS_OPTION_NAME = "time_trial_checks"
TIME_TRIAL_SPLIT_150_200 = 1
DIFFICULTY_ITEMS_OPTION_NAME = "difficulty_items"
RACE_ITEMS_OPTION_NAME = "race_items"
DIFFICULTY_REQUIREMENT_ATOMS = (
    "|50CC|",
    "|100CC|",
    "|150CC|",
    "|Mirror|",
    "|200CC|",
    "|@Difficulty:1|",
    "|@Difficulty:all|",
)
BATTLE_DAMAGE_REQUIREMENT_ATOM = "|@Battle Damage Items:1|"
REQUIREMENT_ATOM_PATTERN = re.compile(r"\|([^|]+)\|")
DOWNGRADED_CLASSIFICATION = "filler"


def _selected_goal_name(world: World, multiworld: MultiWorld, player: int) -> str:
    goal_index = int(get_option_value(multiworld, player, "goal"))
    if 0 <= goal_index < len(world.victory_names):
        return world.victory_names[goal_index]
    return world.victory_names[0]


def _selected_goal_requires_tokens(world: World, multiworld: MultiWorld, player: int) -> bool:
    goal_name = _selected_goal_name(world, multiworld, player)
    goal_location = world.location_name_to_location.get(goal_name, {})
    return TOKEN_ITEM_NAME in str(goal_location.get("requires", ""))


def _int_option(world: World, multiworld: MultiWorld, player: int, option_name: str, default: int) -> int:
    if not hasattr(world.options, option_name):
        return default
    return int(get_option_value(multiworld, player, option_name) or default)


def _required_token_count(world: World, multiworld: MultiWorld, player: int) -> int:
    return max(1, min(100, _int_option(world, multiworld, player, TOKEN_OPTION_NAME, 100)))


def _available_token_count(world: World, multiworld: MultiWorld, player: int) -> int:
    required_count = _required_token_count(world, multiworld, player)
    percentage = max(100, _int_option(world, multiworld, player, TOKEN_AVAILABLE_PERCENTAGE_OPTION_NAME, 100))
    return max(required_count, min(100, (required_count * percentage + 99) // 100))


def _is_manual_option_enabled(world: World, multiworld: MultiWorld, player: int, option_name: str) -> bool:
    if not hasattr(world.options, option_name):
        return True
    return bool(get_option_value(multiworld, player, option_name))


def _remove_requirement_atom(requirement: str, atom: str) -> str:
    updated = requirement.replace(f"{atom} AND ", "")
    updated = updated.replace(f" AND {atom}", "")
    updated = updated.replace(atom, "")
    updated = re.sub(r"\s+AND\s+AND\s+", " AND ", updated)
    updated = updated.replace("( AND ", "(").replace(" AND )", ")")
    return updated.strip()


def _remove_requirement_atoms(requirement: str, atoms: tuple[str, ...]) -> str:
    for atom in atoms:
        requirement = _remove_requirement_atom(requirement, atom)
    return requirement


def _enabled_battle_damage_items(world: World, multiworld: MultiWorld, player: int) -> bool:
    return _is_manual_option_enabled(world, multiworld, player, RACE_ITEMS_OPTION_NAME)


def _character_variant_mode(world: World, multiworld: MultiWorld, player: int) -> int:
    mode = _int_option(world, multiworld, player, CHARACTER_VARIANT_OPTION_NAME, CHARACTER_VARIANT_SEPARATE)
    if mode not in {CHARACTER_VARIANT_SEPARATE, CHARACTER_VARIANT_PROGRESSIVE, CHARACTER_VARIANT_ONLY}:
        return CHARACTER_VARIANT_SEPARATE
    return mode


def _character_group_enabled(world: World, multiworld: MultiWorld, player: int, group: dict) -> bool:
    return all(_is_manual_option_enabled(world, multiworld, player, option_name) for option_name in group["required_options"])


def _sync_character_variant_item_counts(item_config: dict[str, int | dict], world: World, multiworld: MultiWorld, player: int) -> None:
    mode = _character_variant_mode(world, multiworld, player)

    for group in CHARACTER_VARIANT_GROUPS:
        base_item = group["base"]
        progressive_item = group["progressive"]
        variants = group["variants"]
        enabled = _character_group_enabled(world, multiworld, player, group)

        item_config[base_item] = 0
        item_config[progressive_item] = 0

        if mode == CHARACTER_VARIANT_SEPARATE:
            continue

        for variant_item in variants:
            item_config[variant_item] = 0

        if not enabled:
            continue

        if mode == CHARACTER_VARIANT_PROGRESSIVE:
            item_config[progressive_item] = len(variants)
        elif mode == CHARACTER_VARIANT_ONLY:
            item_config[base_item] = 1


def _sync_rainbow_road_goal_requirements(world: World, multiworld: MultiWorld, player: int) -> None:
    dlc_enabled = _is_manual_option_enabled(world, multiworld, player, "dlc")
    requirements: list[str] = []
    for cup_name, wave_option in RAINBOW_ROAD_GOAL_REQUIREMENTS:
        if wave_option is None or (dlc_enabled and _is_manual_option_enabled(world, multiworld, player, wave_option)):
            requirements.append(cup_name)

    base_requires = " AND ".join(f"|{requirement}|" for requirement in requirements)
    for goal_name in RAINBOW_ROAD_GOAL_NAMES:
        goal = world.location_name_to_location.get(goal_name)
        if not goal:
            continue
        goal["requires"] = base_requires
        if TOKEN_ITEM_NAME in goal_name:
            goal["requires"] = f"({base_requires}) AND |{TOKEN_ITEM_NAME}:ALL|"


def _sync_time_trial_goal_requirements(world: World, multiworld: MultiWorld, player: int) -> None:
    requirements = ["|Time Trial|", "|@Cups:all|"]
    if (
        _is_manual_option_enabled(world, multiworld, player, DIFFICULTY_ITEMS_OPTION_NAME)
        and _int_option(world, multiworld, player, TIME_TRIAL_CHECKS_OPTION_NAME, 0) == TIME_TRIAL_SPLIT_150_200
    ):
        if _is_manual_option_enabled(world, multiworld, player, "run_150cc"):
            requirements.append("|150CC|")
        if _is_manual_option_enabled(world, multiworld, player, "run_200cc"):
            requirements.append("|200CC|")

    base_requires = " AND ".join(requirements)
    for goal_name in TIME_TRIAL_GOAL_NAMES:
        goal = world.location_name_to_location.get(goal_name)
        if not goal:
            continue
        goal["requires"] = base_requires
        if TOKEN_ITEM_NAME in goal_name:
            goal["requires"] = f"({base_requires}) AND |{TOKEN_ITEM_NAME}:ALL|"


def _sync_optional_requirement_filters(world: World, multiworld: MultiWorld, player: int) -> None:
    strip_difficulty = not _is_manual_option_enabled(world, multiworld, player, DIFFICULTY_ITEMS_OPTION_NAME)
    strip_battle_damage = not _enabled_battle_damage_items(world, multiworld, player)
    if not strip_difficulty and not strip_battle_damage:
        return

    for location in world.location_name_to_location.values():
        requirements = str(location.get("requires", ""))
        if not requirements:
            continue
        if strip_difficulty:
            requirements = _remove_requirement_atoms(requirements, DIFFICULTY_REQUIREMENT_ATOMS)
        if strip_battle_damage:
            requirements = _remove_requirement_atom(requirements, BATTLE_DAMAGE_REQUIREMENT_ATOM)
        location["requires"] = requirements


def _requirement_to_text(requirement: Any) -> str:
    if isinstance(requirement, str):
        return requirement
    return json.dumps(requirement)


def _iter_active_requirement_strings(world: World, multiworld: MultiWorld, player: int):
    for location in multiworld.get_locations(player):
        manual_location = world.location_name_to_location.get(location.name)
        if manual_location is None:
            manual_location = world.event_name_to_event.get(location.name)
        if manual_location and manual_location.get("requires"):
            yield _requirement_to_text(manual_location["requires"])

    for region in multiworld.regions:
        if region.player != player:
            continue
        manual_region = region_table.get(region.name, {})
        if manual_region.get("requires"):
            yield _requirement_to_text(manual_region["requires"])
        for requirement in manual_region.get("entrance_requires", {}).values():
            yield _requirement_to_text(requirement)
        for requirement in manual_region.get("exit_requires", {}).values():
            yield _requirement_to_text(requirement)


def _required_items_and_categories(world: World, multiworld: MultiWorld, player: int) -> tuple[set[str], set[str]]:
    required_items: set[str] = set()
    required_categories: set[str] = set()

    for requirement_text in _iter_active_requirement_strings(world, multiworld, player):
        for atom in REQUIREMENT_ATOM_PATTERN.findall(requirement_text):
            atom_name = atom.split(":", 1)[0].strip()
            if not atom_name:
                continue
            if atom_name.startswith("@"):
                required_categories.add(atom_name[1:])
            else:
                required_items.add(atom_name)

    return required_items, required_categories


def _item_config_count(config: int | dict) -> int:
    if isinstance(config, dict):
        return sum(int(count) for count in config.values())
    return int(config)


def _item_config_has_progression(config: int | dict) -> bool:
    if not isinstance(config, dict):
        return False
    return any("progression" in str(classification).lower() and int(count) > 0 for classification, count in config.items())


def _item_is_progression(item: dict, config: int | dict) -> bool:
    return (
        bool(item.get("progression"))
        or bool(item.get("progression_skip_balancing"))
        or _item_config_has_progression(config)
    )


def _logical_progression_item_names(item_config: dict[str, int | dict], world: World, multiworld: MultiWorld, player: int) -> set[str]:
    required_items, required_categories = _required_items_and_categories(world, multiworld, player)
    logical_items = set(required_items)

    for item_name, config in item_config.items():
        if _item_config_count(config) <= 0:
            continue
        item = world.item_name_to_item.get(item_name)
        if not item:
            continue
        if required_categories.intersection(item.get("category", [])):
            logical_items.add(item_name)

    return logical_items


def _sync_dynamic_item_classifications(item_config: dict[str, int | dict], world: World, multiworld: MultiWorld, player: int) -> None:
    logical_progression_items = _logical_progression_item_names(item_config, world, multiworld, player)

    for item_name, config in list(item_config.items()):
        count = _item_config_count(config)
        if count <= 0:
            continue

        item = world.item_name_to_item.get(item_name)
        if not item:
            continue

        if item_name in logical_progression_items:
            if not _item_is_progression(item, config):
                item_config[item_name] = {"progression": count}
            continue

        if _item_is_progression(item, config):
            item_config[item_name] = {DOWNGRADED_CLASSIFICATION: count}


def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    if FILLER_ITEM_NAMES:
        return world.random.choice(FILLER_ITEM_NAMES)
    return False


def before_generate_early(world: World, multiworld: MultiWorld, player: int) -> None:
    pass


def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass


def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    locationNamesToRemove: list[str] = []

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)


def before_create_items_all(item_config: dict[str, int | dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int | dict]:
    _sync_rainbow_road_goal_requirements(world, multiworld, player)
    _sync_time_trial_goal_requirements(world, multiworld, player)
    _sync_optional_requirement_filters(world, multiworld, player)
    _sync_character_variant_item_counts(item_config, world, multiworld, player)

    if _selected_goal_requires_tokens(world, multiworld, player):
        required_count = _required_token_count(world, multiworld, player)
        available_count = _available_token_count(world, multiworld, player)
        extra_count = available_count - required_count
        item_config[TOKEN_ITEM_NAME] = {"progression": required_count, "useful": extra_count} if extra_count else required_count
    else:
        item_config[TOKEN_ITEM_NAME] = 0

    _sync_dynamic_item_classifications(item_config, world, multiworld, player)

    return item_config


def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool


def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    itemNamesToRemove: list[str] = []

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        remove_specific_item(item_pool, item)

    return item_pool


def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool


def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    _sync_rainbow_road_goal_requirements(world, multiworld, player)
    _sync_time_trial_goal_requirements(world, multiworld, player)
    _sync_optional_requirement_filters(world, multiworld, player)


def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    def Example_Rule(state: CollectionState) -> bool:
        return True


def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name


def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item


def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass


def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass


def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass


def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass


def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data


def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data


def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass


def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass


def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass


def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    return slot_data
