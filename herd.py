from dinosaur import Dinosaur


class Herd:

    def __init__(self, name):
        self.name = name
        self.dinosaur_herd = [] 
        self.size = len(self.dinosaur_herd)

    def create_herd(self,):
        dinosaur_one = Dinosaur('Spinosaurus', 100)
        dinosaur_two = Dinosaur('Velociraptor', 100)
        dinosaur_three = Dinosaur('Dilophosaurus', 100)
        self.dinosaur_herd.extend([dinosaur_one, dinosaur_two, dinosaur_three])