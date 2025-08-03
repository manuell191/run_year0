from .blueprints.character import Character

class PlayerCharacter(Character):
    """
    PlayerCharacter is an object for the player

    Attributes:
        max_health (int): maximum health
        health (int): current health
        damage (tuple[int]): damage range
        inventory (list[GameItem]): all items held by player
        location (int): current location
        stats(dict[str, int]): all stats
        multipliers (dict[str, int]): multipliers for battle
        level = (int): current level
    """
    def __init__(self, player_class: int):
        self.level: int
        if player_class == 1:
            # warrior
            stats = {
                        "vig": 9,
                        "end": 8,
                        "str": 7,
                        "dex": 7
                    }
            self.level = 11
        elif player_class == 2:
            # knight
            stats = {
                        "vig": 10,
                        "end": 7,
                        "str": 8,
                        "dex": 6
                    }
            self.level = 11
        elif player_class == 3:
            # thief
            stats = {
                        "vig": 7,
                        "end": 8,
                        "str": 7,
                        "dex": 10
                    }
            self.level = 12
        else:
            # deprived
            stats = {
                        "vig": 6,
                        "end": 6,
                        "str": 6,
                        "dex": 6
                    }
            self.level = 4
        super().__init__(1, stats)
