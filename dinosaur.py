import random


class Dinosaur:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_power = random.randint(10, 20)