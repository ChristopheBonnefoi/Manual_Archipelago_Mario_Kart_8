from typing import Optional, Any
from BaseClasses import MultiWorld
import re


ENGINE_OPTION_BY_ITEM = {
    "50CC": "run_50cc",
    "100CC": "run_100cc",
    "150CC": "run_150cc",
    "Mirror": "run_mirror",
    "200CC": "run_200cc",
}

ENGINE_CATEGORIES = {"50CC", "100CC", "150CC", "Mirror", "200CC"}
ENGINE_REQUIREMENT_PATTERN = re.compile(r"\|(?:50CC|100CC|150CC|Mirror|200CC)\|")
NO_DIFFICULTY_CATEGORY = "No Difficulty Checks"
GAME_MODE_ITEMS = ("Grand Prix", "VS Race", "Time Trial", "Battle")
DIFFICULTY_ITEMS_OPTION_NAME = "difficulty_items"

GLOBAL_OPTION_BY_CATEGORY = {
    "Game_Mode": "game_modes",
    "Battle Modes": "battle_modes",
    "Items": "race_items",
    "Karts": "kart",
    "Wheels": "kart",
    "Gliders": "kart",
    "Difficulty": DIFFICULTY_ITEMS_OPTION_NAME,
}

TECHNICAL_OPTION_CATEGORY_PREFIXES = {
    "Game Mode Option - ": ("game_modes", "game_mode"),
    "Battle Mode Option - ": ("battle_modes", "battle_mode"),
}
MODE_SETTING_OPTION_BY_NAME = {
    "Team Game": "mode_setting_teams",
    "No Teams": "mode_setting_teams",
    "Team Rules": "mode_setting_teams",
    "Frantic Items": "mode_setting_items",
    "Custom Items": "mode_setting_items",
    "Normal Items": "mode_setting_items",
    "Skilled Items": "mode_setting_items",
    "No Items": "mode_setting_items",
    "No Items or Coins": "mode_setting_items",
    "Shell Only": "mode_setting_items",
    "Bananas Only": "mode_setting_items",
    "Mushroom Only": "mode_setting_items",
    "Bob-ombs Only": "mode_setting_items",
    "Item Rules": "mode_setting_items",
    "1 Minute": "mode_setting_round_time",
    "2 Minutes": "mode_setting_round_time",
    "3 Minutes": "mode_setting_round_time",
    "4 Minutes": "mode_setting_round_time",
    "5 Minutes": "mode_setting_round_time",
    "Round Time": "mode_setting_round_time",
    "Easy COM": "mode_setting_com",
    "Normal COM": "mode_setting_com",
    "Hard COM": "mode_setting_com",
    "COM Difficulty": "mode_setting_com",
    "All Vehicles": "mode_setting_com_vehicles",
    "Kart Only": "mode_setting_com_vehicles",
    "Bikes Only": "mode_setting_com_vehicles",
    "COM Vehicle Rules": "mode_setting_com_vehicles",
    "Choose Courses": "mode_setting_courses",
    "In Order Courses": "mode_setting_courses",
    "Random Courses": "mode_setting_courses",
    "Course Rules": "mode_setting_courses",
    "4 Rounds": "mode_setting_rounds",
    "6 Rounds": "mode_setting_rounds",
    "8 Rounds": "mode_setting_rounds",
    "12 Rounds": "mode_setting_rounds",
    "16 Rounds": "mode_setting_rounds",
    "24 Rounds": "mode_setting_rounds",
    "Battle Rounds": "mode_setting_rounds",
    "4 Races": "mode_setting_races",
    "6 Races": "mode_setting_races",
    "8 Races": "mode_setting_races",
    "12 Races": "mode_setting_races",
    "16 Races": "mode_setting_races",
    "24 Races": "mode_setting_races",
    "32 Races": "mode_setting_races",
    "48 Races": "mode_setting_races",
    "VS Races": "mode_setting_races",
}

OPTION_BY_EXTRA_CATEGORY = {
    "50CC": "run_50cc",
    "100CC": "run_100cc",
    "150CC": "run_150cc",
    "Mirror": "run_mirror",
    "200CC": "run_200cc",
    "DLC": "dlc",
    "Waves 1": "dlc_wave_1",
    "Waves 2": "dlc_wave_2",
    "Waves 3": "dlc_wave_3",
    "Waves 4": "dlc_wave_4",
    "Waves 5": "dlc_wave_5",
    "Waves 6": "dlc_wave_6",
    "golden": "golden",
    "Golden Mario Option": "golden_mario",
    "Gold Standard Option": "gold_standard",
    "Gold Tires Option": "gold_tires",
    "Golden Glider Option": "golden_glider",
    "Race Item Option": "race_items",
    "Kart Option": "kart",
    "Track Challenges": "track_challenges",
    "Item Challenges": "item_challenges",
    "Kart Challenges": "kart_challenges",
    "VS Race Challenges": "vs_race_challenges",
    "Battle Challenges": "battle_challenges",
}

TIME_TRIAL_OPTION_NAME = "time_trial_checks"
TIME_TRIAL_SINGLE = 0
TIME_TRIAL_SPLIT_150_200 = 1
TIME_TRIAL_SINGLE_CATEGORY = "Time Trial Single"
TIME_TRIAL_SPLIT_CATEGORY = "Time Trial Split"


def _is_option_enabled(multiworld: MultiWorld, player: int, option_name: str, default: bool = True) -> bool:
    option = getattr(multiworld.worlds[player].options, option_name, None)
    if option is None:
        return default
    return bool(option.value > 0)


def _option_value(multiworld: MultiWorld, player: int, option_name: str, default: int = 0) -> int:
    option = getattr(multiworld.worlds[player].options, option_name, None)
    if option is None:
        return default
    return int(option.value)


def _time_trial_check_mode(multiworld: MultiWorld, player: int) -> int:
    mode = _option_value(multiworld, player, TIME_TRIAL_OPTION_NAME, TIME_TRIAL_SINGLE)
    if mode not in {TIME_TRIAL_SINGLE, TIME_TRIAL_SPLIT_150_200}:
        return TIME_TRIAL_SINGLE
    return mode


def _option_slug(name: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower())


def _technical_category_options(category_name: str) -> tuple[str | None, str | None]:
    for category_prefix, (global_option, option_prefix) in TECHNICAL_OPTION_CATEGORY_PREFIXES.items():
        if category_name.startswith(category_prefix):
            item_name = category_name[len(category_prefix):]
            return global_option, f"{option_prefix}_{_option_slug(item_name)}"

    mode_setting_prefix = "Mode Setting Option - "
    if category_name.startswith(mode_setting_prefix):
        setting_name = category_name[len(mode_setting_prefix):]
        return None, MODE_SETTING_OPTION_BY_NAME.get(setting_name)

    return None, None


def _enabled_game_modes(multiworld: MultiWorld, player: int) -> set[str]:
    if not _is_option_enabled(multiworld, player, "game_modes"):
        return set()
    return {
        mode_name
        for mode_name in GAME_MODE_ITEMS
        if _is_option_enabled(multiworld, player, f"game_mode_{_option_slug(mode_name)}")
    }


def _required_game_modes(requirements: str) -> set[str]:
    return {mode_name for mode_name in GAME_MODE_ITEMS if f"|{mode_name}|" in requirements}


def _requires_engine_item(requirements: str) -> bool:
    return ENGINE_REQUIREMENT_PATTERN.search(requirements) is not None


def _category_list(categories: list[str] | str | None) -> list[str]:
    if categories is None:
        return []
    if isinstance(categories, str):
        return [categories]
    return categories


def _has_disabled_category(multiworld: MultiWorld, player: int, categories: list[str] | str | None) -> bool:
    categories = _category_list(categories)
    difficulty_items_enabled = _is_option_enabled(multiworld, player, DIFFICULTY_ITEMS_OPTION_NAME)

    for category in categories:
        global_option_name = GLOBAL_OPTION_BY_CATEGORY.get(category)
        if global_option_name and not _is_option_enabled(multiworld, player, global_option_name):
            return True

        parent_option_name, item_option_name = _technical_category_options(category)
        if parent_option_name and not _is_option_enabled(multiworld, player, parent_option_name):
            return True
        if item_option_name and not _is_option_enabled(multiworld, player, item_option_name):
            return True

        option_name = OPTION_BY_EXTRA_CATEGORY.get(category)
        if category in ENGINE_CATEGORIES and not difficulty_items_enabled:
            continue
        if option_name and not _is_option_enabled(multiworld, player, option_name):
            return True

    # Parent options override child options.
    if "DLC" in categories and not _is_option_enabled(multiworld, player, "dlc"):
        return True
    if "golden" in categories and not _is_option_enabled(multiworld, player, "golden"):
        return True

    return False


def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None


def before_is_item_enabled(multiworld: MultiWorld, player: int, item: dict[str, Any]) -> Optional[bool]:
    item_name = item.get("name", "")
    if item_name in ENGINE_OPTION_BY_ITEM and not _is_option_enabled(multiworld, player, ENGINE_OPTION_BY_ITEM[item_name]):
        return False

    if _has_disabled_category(multiworld, player, item.get("category", [])):
        return False

    return None


def before_is_location_enabled(multiworld: MultiWorld, player: int, location: dict[str, Any]) -> Optional[bool]:
    if location.get("victory"):
        return True

    categories = _category_list(location.get("category", []))
    difficulty_items_enabled = _is_option_enabled(multiworld, player, DIFFICULTY_ITEMS_OPTION_NAME)
    if NO_DIFFICULTY_CATEGORY in categories and difficulty_items_enabled:
        return False
    if NO_DIFFICULTY_CATEGORY not in categories and not difficulty_items_enabled:
        requirements = str(location.get("requires", ""))
        if any(category in ENGINE_CATEGORIES for category in categories) or _requires_engine_item(requirements):
            return False

    if _has_disabled_category(multiworld, player, categories):
        return False

    required_modes = _required_game_modes(str(location.get("requires", "")))
    if required_modes and not (required_modes & _enabled_game_modes(multiworld, player)):
        return False

    time_trial_mode = _time_trial_check_mode(multiworld, player)
    if TIME_TRIAL_SINGLE_CATEGORY in categories:
        return time_trial_mode == TIME_TRIAL_SINGLE or not difficulty_items_enabled
    if TIME_TRIAL_SPLIT_CATEGORY in categories:
        return time_trial_mode == TIME_TRIAL_SPLIT_150_200 and difficulty_items_enabled

    return None


def before_is_event_enabled(multiworld: MultiWorld, player: int, event: dict[str, Any]) -> Optional[bool]:
    if _has_disabled_category(multiworld, player, event.get("category", [])):
        return False

    return None
