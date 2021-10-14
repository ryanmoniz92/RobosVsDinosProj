from weapon import Weapon
import random


class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon
        self.weapon_damage = random.randint(10, 20)