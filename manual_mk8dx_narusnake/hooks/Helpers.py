from typing import Optional, Any
from BaseClasses import MultiWorld


ENGINE_OPTION_BY_ITEM = {
    "50CC": "run_50cc",
    "100CC": "run_100cc",
    "150CC": "run_150cc",
    "Mirror": "run_mirror",
    "200CC": "run_200cc",
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
}


def _is_option_enabled(multiworld: MultiWorld, player: int, option_name: str, default: bool = True) -> bool:
    option = getattr(multiworld.worlds[player].options, option_name, None)
    if option is None:
        return default
    return bool(option.value > 0)


def _category_list(categories: list[str] | str | None) -> list[str]:
    if categories is None:
        return []
    if isinstance(categories, str):
        return [categories]
    return categories


def _has_disabled_category(multiworld: MultiWorld, player: int, categories: list[str] | str | None) -> bool:
    categories = _category_list(categories)
    for category in categories:
        option_name = OPTION_BY_EXTRA_CATEGORY.get(category)
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

    if _has_disabled_category(multiworld, player, location.get("category", [])):
        return False

    return None


def before_is_event_enabled(multiworld: MultiWorld, player: int, event: dict[str, Any]) -> Optional[bool]:
    if _has_disabled_category(multiworld, player, event.get("category", [])):
        return False

    return None
