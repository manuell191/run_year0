class GameObject:
    def __init__(self, max_health: int) -> None:
        self.health: int = max_health
        self.max_health: int = max_health

    def take_damage(self, amt: int):
        self.health -= amt
