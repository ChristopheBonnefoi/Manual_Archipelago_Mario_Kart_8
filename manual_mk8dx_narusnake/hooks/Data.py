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


def _build_location_sort_key(location_index: int) -> str:
    return f"{location_index:06d}"


def _ensure_category(entry: dict, category: str) -> None:
    categories = entry.setdefault("category", [])
    if isinstance(categories, str):
        categories = [categories]
        entry["category"] = categories
    if category not in categories:
        categories.append(category)


def _entry_mentions(entry: dict, text: str) -> bool:
    haystacks = [entry.get("name", ""), entry.get("requires", []), entry.get("category", [])]
    return any(text in str(haystack) for haystack in haystacks)


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
    for item in item_table:
        _add_dlc_categories(item, DLC_CUP_WAVES)
        _add_dlc_categories(item, DLC_CHARACTER_WAVES)
        _add_golden_categories(item)
    return item_table


def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table


def after_load_location_file(location_table: list) -> list:
    for location_index, location in enumerate(location_table):
        location["sort-key"] = _build_location_sort_key(location_index)
        _add_dlc_categories(location, DLC_CUP_WAVES)
        _add_dlc_categories(location, DLC_CHARACTER_WAVES)
        _add_golden_categories(location)
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

    category_table.setdefault("Filler", {})
    category_table["Filler"].setdefault("hidden", False)

    return category_table


def after_load_option_file(option_table: dict) -> dict:
    return option_table


def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
