from .blueprints.game_item import GameItem

"""
Item type:

1: weapon
2: weapon
3: weapon
4: weapon
5: weapon

"""

class GameWeapon(GameItem):
    """
    GameWeapon is a class that holds data for any type of weapon

    Attributes:
        weght (int): Weight value
        type (int): A value that explains the type of weapon
        damage (int): Damage values for the weapon
    """
    def __init__(self, item_type: int):
        super().__init__(item_type)
        self.damage: list[int] = [1,2]
