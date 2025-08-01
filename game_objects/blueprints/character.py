from random import randint
from game_object import GameObject

class Character(GameObject):
    def __init__(self, max_health) -> None:
        super().__init__(max_health)
        self.damage: tuple[int]
        self.inventory: list[None] = []

    def heal(self, num: int) -> None:
        # add new value to health
        self.health += num

        # set health to max health if new health is above max_health
        if self.health > max_health:
            self.health = max_health
    
    def attack(self, target: GameObject) -> None:
        # damage is a random amount between the two self.damage values
        dmg = randint(self.damage[0], self.damage[1])

        # target takes damage equal to dmg
        target.take_damage(dmg)

    def add_inv(self, item):
        # add an item to the inventory
        self.inventory.append(item)

    def rm_inv(self, item):
        # remove an item from the inventory
        self.inventory.remove(item)
