from fleet import Fleet
from herd import Herd
import random


class Battlefield:

    def __init__(self, name, arena):
        self.name = name
        self.arena = arena
        self.fleet = Fleet('Robo Rampages')
        self.herd = Herd('Dino Destroyers')

    def run_game(self):
        self.herd.create_herd()
        self.fleet.create_fleet()
        self.display_welcome(self.herd.dinosaur_herd)

    def display_welcome(self, list_of_dinos, list_of_robos):
        print('Welcome to Robots VS Dinosaurs, where anything goes! Battles are 3v3. Who will prevail?')

    def battle(self):
        pass

    def dino_turn(self, dinosaur, robot):
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass