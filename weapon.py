import random

robot_weapons = ['Electric Shock', 'Plasma Projectile', 'Circuit Board Crusher']

class Weapon:
    
    def __init__(self):
        self.name = random.choice(list(robot_weapons))