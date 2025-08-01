class GameObject:
    def __init__(self, max_health: int) -> None:
        self.health: int
        self.max_health: int

    def take_damage(self, amt: int):
        self.health -= amt
