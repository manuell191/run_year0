class Character:
    def __init__(self) -> None:
        self.health: int
        self.max_health: int
        self.damage: tuple[int]
        self.inventory: list[None] = []

    def heal(self, num: int) -> None:
        # add new value to health
        self.health += num

        # set health to max health if new health is above max_health
        if self.health > max_health:
            self.health = max_health
    
