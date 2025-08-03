class GameObject:
    """
    GameObject is a parent class for all types of game objects

    Attributes:
        max_health (int): maximum health
        health (int): current health
    """
    def __init__(self, max_health: int) -> None:
        self.health: int = max_health
        self.max_health: int = max_health

    def take_damage(self, amt: int):
        # take damage equal to amount
        self.health -= amt
