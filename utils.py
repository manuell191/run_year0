import os
import math

def clear_screen() -> None:
    # check OS
    if os.name == "nt": # if windows
        os.system("cls")
    else:
        os.system("clear")

def clean_input(user_in) -> str:
    # return an easier string to process
    return user_in.lower().strip()

def calc_stats(stats: dict[str, int]) -> tuple[int]:
    """
    Vigor stat returns final health
    Endurance stat return final Endurance
    Strength stat returns attack adder
    Dexterity stat returns attack adder
    """

    # vigor math
    if stats["vig"] < 20:
        # first 20 points are worth 10
        vigor = stats["vig"] * 10
    elif stats["vig"] < 50:
        # next 30 are worth 5
        vigor = ((stats["vig"] - 20) * 5) + 200
    elif stats["vig"] == 99:
        # at the end it adds up to an even 500
        vigor = 500
    else:
        # but the last 48 points are worth 3
        vigor = ((stats["vig"] - 50) * 3) + 350

    # endurance math
    if stats["end"] < 20:
        # first 20 points are worth 2
        endurance = stats["end"] * 2
    elif stats["end"] < 50:
        # next 30 are worth 1
        endurance = (stats["end"] - 20) + 40
    else:
        # the last 49 points are only worth 0.6
        endurance = ((stats["end"] - 50) * 0.6) + 70

    # round down endurance
    endurance = math.floor(endurance)

    # weopon multipliers:
    # A: 2, B: 1.5, C: 1, D: 0.75, E: 0.25

    # strength math
    if stats["str"] < 20:
        # first 20 points are worth 2
        strength = stats["str"] * 2
    elif stats["str"] < 50:
        # next 30 are worth 1
        strength = (stats["str"] - 20) + 40
    else:
        # the last 49 points are only worth 0.6
        strength = ((stats["str"] - 50) * 0.6) + 70

    # round down strength
    strength = math.floor(strength)

    # dexterity math
    if stats["dex"] < 20:
        # first 20 points are worth 2
        dexterity = stats["dex"] * 2
    elif stats["dex"] < 50:
        # next 30 are worth 1
        dexterity = (stats["dex"] - 20) + 40
    else:
        # the last 49 points are only worth 0.6
        dexterity = ((stats["dex"] - 50) * 0.6) + 70

    dexterity = math.floor(dexterity)

    return (vigor, endurance, strength, dexterity)
