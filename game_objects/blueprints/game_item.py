"""
Item type explainations:

0: any
1: weapon
2: weapon
3: weapon
4: weapon
5: weapon
6: armor
7: potion
8: tokens
TBD

"""

class GameItem:
    """
    GameItem is a parent class for multiple types of items.

    Attributes:
        weight (int): Weight value
        type (int): A value that explains the type of item
    """
    def __init__(self, item_type: int = 0):
        self.weight: int
        self.type: int = item_type

    def set_weight(self, value: int):
        # set the weight value for the item
        self.weight = value
