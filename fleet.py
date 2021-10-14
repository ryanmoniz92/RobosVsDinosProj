from robot import Robot


class Fleet:

    def __init__(self, name):
        self.name = name 
        self.robot_fleet = []
        self.size = len(self.robot_fleet)

    def create_fleet(self):
        robot_one = Robot('Optimus Prime', 100)
        robot_two = Robot('Bumblebee', 100)
        robot_three = Robot('Megatron', 100)
        self.robot_fleet.extend([robot_one, robot_two, robot_three])