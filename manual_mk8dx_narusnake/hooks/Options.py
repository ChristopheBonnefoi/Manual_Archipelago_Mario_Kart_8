from Options import Option, OptionGroup, PerGameCommonOptions
from typing import Type, Any


GOAL_ALIASES = {
    "rainbow_roads": 0,
    "all_rainbow_roads": 0,
    "tokens": 1,
    "token": 1,
    "mktv_tokens": 1,
    "grand_prix": 2,
    "all_grand_prix": 2,
    "time_trial": 3,
    "all_time_trial": 3,
    "vs_race": 4,
    "all_vs_race": 4,
    "battle": 5,
    "all_battle": 5,
    "rainbow_roads_tokens": 6,
    "grand_prix_tokens": 7,
    "time_trial_tokens": 8,
    "vs_race_tokens": 9,
    "battle_tokens": 10,
}


def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    return options


def after_options_defined(options: Type[PerGameCommonOptions]):
    goal_option = options.type_hints.get("goal")
    if goal_option:
        goal_option.aliases.update(GOAL_ALIASES)
        goal_option.options.update(goal_option.aliases)


def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    return groups


def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
