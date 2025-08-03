from random import randint
from .game_object import GameObject
from .game_item import GameItem
from ..game_weapon import GameWeapon

class Character(GameObject):
    """
    Character is a parent class for all types of characters

    Attributes:
        max_heatlh (int): maximum health
        health(int): current health
        damage(typle[int]): damage range
        inventory (list[GameItem]): all items held by a character
    """
    def __init__(self, max_health: int) -> None:
        super().__init__(max_health)
        self.damage: tuple[int]
        self.inventory: list[GameItem] = []

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

    def add_inv(self, item: GameItem) -> None:
        # add an item to the inventory
        self.inventory.append(item)

    def rm_inv(self, item: GameItem) -> None:
        # remove an item from the inventory
        self.inventory.remove(item)

    def update_damage(self, weapon: GameWeapon, add_item: bool = True) -> None:
        # sets this character damage to be equal to the weapon damage
        self.damage = weapon.damage # TODO: add a way to randomize weapons

        # adds the weapon to the inventory if not already added, and if allowed to add
        if weapon not in self.inventory and add_item:
            self.add_inv(weapon)

    def set_exact_damage(self, damage: list[int]) -> None:
        # set the exact damage when damage is unusual
        self.damage = damage

    # TODO: optional character death message?
    def death(self) -> None | list[GameItem]:
        if self.inventory != []:
            # return all inventory items when killed
            return self.inventory
        # return None as a way to say that the character had no items
        return None
