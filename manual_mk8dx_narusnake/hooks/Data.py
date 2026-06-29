import re
from copy import deepcopy


DLC_CUP_WAVES = {
    "Golden Dash Cup": "Waves 1",
    "Lucky Cat Cup": "Waves 1",
    "Turnip Cup": "Waves 2",
    "Propeller Cup": "Waves 2",
    "Rock Cup": "Waves 3",
    "Moon Cup": "Waves 3",
    "Fruit Cup": "Waves 4",
    "Boomerang Cup": "Waves 4",
    "Feather Cup": "Waves 5",
    "Cherry Cup": "Waves 5",
    "Acorn Cup": "Waves 6",
    "Spiny Cup": "Waves 6",
}

DLC_CHARACTER_WAVES = {
    "Birdo (Pink)": "Waves 4",
    "Birdo (Light Blue)": "Waves 4",
    "Birdo (Black)": "Waves 4",
    "Birdo (Red)": "Waves 4",
    "Birdo (Yellow)": "Waves 4",
    "Birdo (White)": "Waves 4",
    "Birdo (Dark Blue)": "Waves 4",
    "Birdo (Green)": "Waves 4",
    "Birdo (Orange)": "Waves 4",
    "Petey Piranha": "Waves 5",
    "Wiggler": "Waves 5",
    "Kamek": "Waves 5",
    "Peachette": "Waves 6",
    "Diddy Kong": "Waves 6",
    "Funky Kong": "Waves 6",
    "Pauline": "Waves 6",
}

GOLDEN_ITEM_OPTIONS = {
    "Golden Mario": ("Golden Mario Option", "golden_mario"),
    "Gold Standard": ("Gold Standard Option", "gold_standard"),
    "Gold Tires": ("Gold Tires Option", "gold_tires"),
    "Golden Glider": ("Golden Glider Option", "golden_glider"),
}

TIME_TRIAL_MODE_CATEGORIES = ("Time Trial Single", "Time Trial Split")
ENGINE_CATEGORIES = ("50CC", "100CC", "150CC", "Mirror", "200CC")
CANONICAL_ENGINE_CATEGORY = "150CC"
CANONICAL_ENGINE_REQUIREMENT = f"|{CANONICAL_ENGINE_CATEGORY}|"
NO_DIFFICULTY_CATEGORY = "No Difficulty Checks"
TRACK_CHALLENGE_CATEGORY = "Track Challenges"
TRACK_CHALLENGE_OPTION = "track_challenges"
ITEM_CHALLENGE_CATEGORY = "Item Challenges"
ITEM_CHALLENGE_OPTION = "item_challenges"
KART_CHALLENGE_CATEGORY = "Kart Challenges"
KART_CHALLENGE_OPTION = "kart_challenges"
VS_RACE_CHALLENGE_CATEGORY = "VS Race Challenges"
VS_RACE_CHALLENGE_OPTION = "vs_race_challenges"
BATTLE_CHALLENGE_CATEGORY = "Battle Challenges"
BATTLE_CHALLENGE_OPTION = "battle_challenges"
INDIVIDUAL_OPTION_CATEGORY_CONFIG = {
    "Game_Mode": ("Game Mode Option", "game_mode", "game_modes"),
    "Battle Modes": ("Battle Mode Option", "battle_mode", "battle_modes"),
}
MODE_SETTING_OPTION_BY_ITEM_NAME = {
    "Team Game": "mode_setting_teams",
    "No Teams": "mode_setting_teams",
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
    "1 Minute": "mode_setting_round_time",
    "2 Minutes": "mode_setting_round_time",
    "3 Minutes": "mode_setting_round_time",
    "4 Minutes": "mode_setting_round_time",
    "5 Minutes": "mode_setting_round_time",
    "Easy COM": "mode_setting_com",
    "Normal COM": "mode_setting_com",
    "Hard COM": "mode_setting_com",
    "All Vehicles": "mode_setting_com_vehicles",
    "Kart Only": "mode_setting_com_vehicles",
    "Bikes Only": "mode_setting_com_vehicles",
    "Choose Courses": "mode_setting_courses",
    "In Order Courses": "mode_setting_courses",
    "Random Courses": "mode_setting_courses",
    "4 Rounds": "mode_setting_rounds",
    "6 Rounds": "mode_setting_rounds",
    "8 Rounds": "mode_setting_rounds",
    "12 Rounds": "mode_setting_rounds",
    "16 Rounds": "mode_setting_rounds",
    "24 Rounds": "mode_setting_rounds",
    "4 Races": "mode_setting_races",
    "6 Races": "mode_setting_races",
    "8 Races": "mode_setting_races",
    "12 Races": "mode_setting_races",
    "16 Races": "mode_setting_races",
    "24 Races": "mode_setting_races",
    "32 Races": "mode_setting_races",
    "48 Races": "mode_setting_races",
}
MODE_SETTING_GROUP_OPTION_CATEGORIES = {
    "Team Rules": "mode_setting_teams",
    "Item Rules": "mode_setting_items",
    "Round Time": "mode_setting_round_time",
    "COM Difficulty": "mode_setting_com",
    "COM Vehicle Rules": "mode_setting_com_vehicles",
    "Course Rules": "mode_setting_courses",
    "Battle Rounds": "mode_setting_rounds",
    "VS Races": "mode_setting_races",
}
MODE_SETTING_REQUIREMENT_CATEGORY_OPTIONS = {
    "Team Settings": ("Team Rules", "mode_setting_teams"),
    "VS Team Settings": ("Team Rules", "mode_setting_teams"),
    "Battle Item Settings": ("Item Rules", "mode_setting_items"),
    "VS Item Settings": ("Item Rules", "mode_setting_items"),
    "Battle Round Time Settings": ("Round Time", "mode_setting_round_time"),
    "COM Settings": ("COM Difficulty", "mode_setting_com"),
    "VS COM Settings": ("COM Difficulty", "mode_setting_com"),
    "COM Vehicle Settings": ("COM Vehicle Rules", "mode_setting_com_vehicles"),
    "VS COM Vehicle Settings": ("COM Vehicle Rules", "mode_setting_com_vehicles"),
    "Battle Course Settings": ("Course Rules", "mode_setting_courses"),
    "VS Course Settings": ("Course Rules", "mode_setting_courses"),
    "Battle Round Count Settings": ("Battle Rounds", "mode_setting_rounds"),
    "VS Race Count Settings": ("VS Races", "mode_setting_races"),
}
RACE_ITEM_OPTION_CATEGORY = "Race Item Option"
RACE_ITEM_OPTION = "race_items"
VEHICLE_PART_CATEGORIES = {"Karts", "Wheels", "Gliders"}
VEHICLE_PART_OPTION_CATEGORY = "Kart Option"
VEHICLE_PART_OPTION = "kart"
OPTION_CATEGORIES_BY_ITEM_NAME: dict[str, list[tuple[str, str | None, str]]] = {}
TRACK_CHALLENGE_CUP_ORDER = (
    "Mushroom Cup",
    "Flower Cup",
    "Star Cup",
    "Special Cup",
    "Egg Cup",
    "Crossing Cup",
    "Shell Cup",
    "Banana Cup",
    "Leaf Cup",
    "Lightning Cup",
    "Triforce Cup",
    "Bell Cup",
    "Golden Dash Cup",
    "Lucky Cat Cup",
    "Turnip Cup",
    "Propeller Cup",
    "Rock Cup",
    "Moon Cup",
    "Fruit Cup",
    "Boomerang Cup",
    "Feather Cup",
    "Cherry Cup",
    "Acorn Cup",
    "Spiny Cup",
)


def _build_location_sort_key(location_index: int) -> str:
    return f"{location_index:06d}"


def _ensure_category(entry: dict, category: str) -> None:
    categories = entry.setdefault("category", [])
    if isinstance(categories, str):
        categories = [categories]
        entry["category"] = categories
    if category not in categories:
        categories.append(category)


def _option_slug(name: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower())


def _entry_mentions(entry: dict, text: str) -> bool:
    haystacks = [entry.get("name", ""), entry.get("requires", []), entry.get("category", [])]
    return any(text in str(haystack) for haystack in haystacks)


def _entry_requires_item(entry: dict, item_name: str) -> bool:
    requires = str(entry.get("requires", ""))
    return re.search(rf"\|{re.escape(item_name)}(?::(?:ALL|\d+))?\|", requires) is not None


def _entry_requires_category(entry: dict, category_name: str) -> bool:
    requires = str(entry.get("requires", ""))
    return re.search(rf"\|@{re.escape(category_name)}(?::(?:all|ALL|\d+))?\|", requires) is not None


def _remove_requirement_atom(requirement: str, atom: str) -> str:
    updated = requirement.replace(f"{atom} AND ", "")
    updated = updated.replace(f" AND {atom}", "")
    updated = updated.replace(atom, "")
    updated = re.sub(r"\s+AND\s+AND\s+", " AND ", updated)
    updated = updated.replace("( AND ", "(").replace(" AND )", ")")
    return updated.strip()


def _clean_no_difficulty_name(name: str) -> str:
    updated = re.sub(r"\b150cc\s*", "", name, flags=re.IGNORECASE)
    updated = re.sub(r"\(\s+", "(", updated)
    updated = re.sub(r"\|\s+", "|", updated)
    updated = re.sub(r"\s+\)", ")", updated)
    updated = re.sub(r"\s{2,}", " ", updated)
    return updated.strip()


def _is_no_difficulty_clone_source(location: dict) -> bool:
    if location.get("victory"):
        return False
    if CANONICAL_ENGINE_REQUIREMENT not in str(location.get("requires", "")):
        return False
    categories = location.get("category", [])
    return "Time Trial Split" not in categories


def _build_no_difficulty_location(location: dict) -> dict:
    clone = deepcopy(location)
    clone["name"] = _clean_no_difficulty_name(clone["name"])
    clone["requires"] = _remove_requirement_atom(str(clone.get("requires", "")), CANONICAL_ENGINE_REQUIREMENT)
    clone["category"] = [
        category
        for category in clone.get("category", [])
        if category not in ENGINE_CATEGORIES
    ]
    _ensure_category(clone, NO_DIFFICULTY_CATEGORY)
    clone["sort-key"] = f"{location['sort-key']}-no-difficulty"
    return clone


def _item_option_categories(item: dict) -> list[tuple[str, str | None, str]]:
    categories = item.get("category", [])
    option_categories: list[tuple[str, str | None, str]] = []
    for source_category, (category_prefix, option_prefix, global_option) in INDIVIDUAL_OPTION_CATEGORY_CONFIG.items():
        if source_category in categories:
            option_name = f"{option_prefix}_{_option_slug(item['name'])}"
            option_categories.append((f"{category_prefix} - {item['name']}", global_option, option_name))

    if "Mode Settings" in categories:
        option_name = MODE_SETTING_OPTION_BY_ITEM_NAME.get(item["name"])
        if option_name:
            option_categories.append((f"Mode Setting Option - {item['name']}", None, option_name))

    if "Items" in categories:
        option_categories.append((RACE_ITEM_OPTION_CATEGORY, None, RACE_ITEM_OPTION))

    if any(category in VEHICLE_PART_CATEGORIES for category in categories):
        option_categories.append((VEHICLE_PART_OPTION_CATEGORY, None, VEHICLE_PART_OPTION))

    return option_categories


def _add_dlc_categories(entry: dict, name_to_wave: dict[str, str]) -> None:
    for name, wave in name_to_wave.items():
        if _entry_mentions(entry, name):
            _ensure_category(entry, "DLC")
            _ensure_category(entry, wave)


def _add_golden_categories(entry: dict) -> None:
    for name, (category, _) in GOLDEN_ITEM_OPTIONS.items():
        if _entry_mentions(entry, name):
            _ensure_category(entry, "golden")
            _ensure_category(entry, category)


def after_load_game_file(game_table: dict) -> dict:
    return game_table


def after_load_item_file(item_table: list) -> list:
    OPTION_CATEGORIES_BY_ITEM_NAME.clear()
    for item in item_table:
        _add_dlc_categories(item, DLC_CUP_WAVES)
        _add_dlc_categories(item, DLC_CHARACTER_WAVES)
        _add_golden_categories(item)
        option_categories = _item_option_categories(item)
        if option_categories:
            OPTION_CATEGORIES_BY_ITEM_NAME[item["name"]] = option_categories
            for option_category, _, _ in option_categories:
                _ensure_category(item, option_category)
    return item_table


def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table


def after_load_location_file(location_table: list) -> list:
    no_difficulty_locations: list[dict] = []
    for location_index, location in enumerate(location_table):
        location["sort-key"] = _build_location_sort_key(location_index)
        _add_dlc_categories(location, DLC_CUP_WAVES)
        _add_dlc_categories(location, DLC_CHARACTER_WAVES)
        _add_golden_categories(location)
        for item_name, option_categories in OPTION_CATEGORIES_BY_ITEM_NAME.items():
            if _entry_requires_item(location, item_name):
                for option_category, _, _ in option_categories:
                    if not option_category.startswith("Game Mode Option - "):
                        _ensure_category(location, option_category)
        for requirement_category, (group_label, _) in MODE_SETTING_REQUIREMENT_CATEGORY_OPTIONS.items():
            if _entry_requires_category(location, requirement_category):
                _ensure_category(location, f"Mode Setting Option - {group_label}")
        if _is_no_difficulty_clone_source(location):
            no_difficulty_locations.append(_build_no_difficulty_location(location))
    location_table.extend(no_difficulty_locations)
    return location_table


def after_load_event_file(event_table: list) -> list:
    return event_table


def after_load_region_file(region_table: dict) -> dict:
    return region_table


def after_load_category_file(category_table: dict) -> dict:
    category_table.setdefault("DLC", {})
    category_table["DLC"].update({"hidden": True, "yaml_option": ["dlc"]})

    for wave_number in range(1, 7):
        category = f"Waves {wave_number}"
        option = f"dlc_wave_{wave_number}"
        category_table.setdefault(category, {})
        category_table[category].update({"hidden": True, "yaml_option": ["dlc", option]})

    category_table.setdefault("golden", {})
    category_table["golden"].update({"hidden": True, "yaml_option": ["golden"]})

    for category, option in GOLDEN_ITEM_OPTIONS.values():
        category_table.setdefault(category, {})
        category_table[category].update({"hidden": True, "yaml_option": ["golden", option]})

    for category in TIME_TRIAL_MODE_CATEGORIES:
        category_table.setdefault(category, {})
        category_table[category].update({"hidden": True})

    category_table.setdefault(NO_DIFFICULTY_CATEGORY, {})
    category_table[NO_DIFFICULTY_CATEGORY].update({"hidden": True})

    category_table.setdefault("Filler", {})
    category_table["Filler"].setdefault("hidden", False)

    for cup_name in TRACK_CHALLENGE_CUP_ORDER:
        category = f"{cup_name} Challenge"
        category_table.setdefault(category, {})
        category_table[category].update({"hidden": False, "yaml_option": [TRACK_CHALLENGE_OPTION]})

    category_table.setdefault(TRACK_CHALLENGE_CATEGORY, {})
    category_table[TRACK_CHALLENGE_CATEGORY].update({"hidden": True, "yaml_option": [TRACK_CHALLENGE_OPTION]})

    category_table.setdefault(ITEM_CHALLENGE_CATEGORY, {})
    category_table[ITEM_CHALLENGE_CATEGORY].update({"hidden": False, "yaml_option": [ITEM_CHALLENGE_OPTION]})

    category_table.setdefault(KART_CHALLENGE_CATEGORY, {})
    category_table[KART_CHALLENGE_CATEGORY].update({"hidden": False, "yaml_option": [KART_CHALLENGE_OPTION]})

    category_table.setdefault(VS_RACE_CHALLENGE_CATEGORY, {})
    category_table[VS_RACE_CHALLENGE_CATEGORY].update({"hidden": False, "yaml_option": [VS_RACE_CHALLENGE_OPTION]})

    category_table.setdefault(BATTLE_CHALLENGE_CATEGORY, {})
    category_table[BATTLE_CHALLENGE_CATEGORY].update({"hidden": False, "yaml_option": [BATTLE_CHALLENGE_OPTION]})

    for group_label, option_name in MODE_SETTING_GROUP_OPTION_CATEGORIES.items():
        option_category = f"Mode Setting Option - {group_label}"
        category_table.setdefault(option_category, {})
        category_table[option_category].update({"hidden": True, "yaml_option": [option_name]})

    for option_categories in OPTION_CATEGORIES_BY_ITEM_NAME.values():
        for option_category, global_option, option_name in option_categories:
            yaml_options = [option_name] if global_option is None else [global_option, option_name]
            category_table.setdefault(option_category, {})
            category_table[option_category].update({"hidden": True, "yaml_option": yaml_options})

    return category_table


def after_load_option_file(option_table: dict) -> dict:
    return option_table


def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
