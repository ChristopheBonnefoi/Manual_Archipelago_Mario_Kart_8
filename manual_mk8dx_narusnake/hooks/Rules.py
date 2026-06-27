from worlds.AutoWorld import World
from BaseClasses import CollectionState


RACE_MODE_ITEMS = ["Grand Prix", "VS Race", "Time Trial"]
ENGINE_CLASS_ITEMS = ["50CC", "100CC", "150CC", "Mirror", "200CC"]


def hasAnyRaceMode(world: World, state: CollectionState, player: int) -> bool:
    """Has the player unlocked at least one standard race mode?"""
    return any(state.has(item_name, player) for item_name in RACE_MODE_ITEMS)


def hasAnyEngineClass(world: World, state: CollectionState, player: int) -> bool:
    """Has the player unlocked at least one engine class?"""
    return any(state.has(item_name, player) for item_name in ENGINE_CLASS_ITEMS)


def hasBattleMode(world: World, state: CollectionState, player: int) -> bool:
    """Has the player unlocked Battle Mode?"""
    return state.has("Battle", player)


def requiresAnyRaceMode() -> str:
    """Returns a Manual requires string for any standard race mode."""
    return "|Grand Prix| or |VS Race| or |Time Trial|"


def requiresAnyEngineClass() -> str:
    """Returns a Manual requires string for any engine class."""
    return "|50CC| or |100CC| or |150CC| or |Mirror| or |200CC|"
