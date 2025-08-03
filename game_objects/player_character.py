from .blueprints.character import Character

class PlayerCharacter(Character):
    """
    PlayerCharacter is an object for the player

    Attributes:
        max_health (int): maximum health
        health (int): current health
        damage (tuple[int]): damage range
        inventory (list[GameItem]): all items held by player
    """
    def __init__(self, max_health):
        super().__init__(max_health)
