from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dinosaur_one = Dinosaur()
        dinosaur_two = Dinosaur()
        dinosaur_three = Dinosaur()
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)