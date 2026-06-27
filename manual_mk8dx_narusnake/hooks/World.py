from typing import Any
from worlds.AutoWorld import World
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

RAINBOW_ROAD_GOAL_REQUIREMENTS = [
    ("Special Cup", None),
    ("Lightning Cup", None),
    ("Triforce Cup", None),
    ("Moon Cup", "dlc_wave_3"),
    ("Spiny Cup", "dlc_wave_6"),
]


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


def _sync_rainbow_road_goal_requirements(world: World, multiworld: MultiWorld, player: int) -> None:
    goal = world.location_name_to_location.get("All Rainbow Roads Complete")
    if not goal:
        return

    dlc_enabled = _is_manual_option_enabled(world, multiworld, player, "dlc")
    requirements: list[str] = []
    for cup_name, wave_option in RAINBOW_ROAD_GOAL_REQUIREMENTS:
        if wave_option is None or (dlc_enabled and _is_manual_option_enabled(world, multiworld, player, wave_option)):
            requirements.append(cup_name)

    goal["requires"] = requirements


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
    if _selected_goal_requires_tokens(world, multiworld, player):
        required_count = _required_token_count(world, multiworld, player)
        available_count = _available_token_count(world, multiworld, player)
        extra_count = available_count - required_count
        item_config[TOKEN_ITEM_NAME] = {"progression": required_count, "useful": extra_count} if extra_count else required_count
    else:
        item_config[TOKEN_ITEM_NAME] = 0

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
