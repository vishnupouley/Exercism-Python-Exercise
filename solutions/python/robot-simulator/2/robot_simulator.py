""" Robot simulator. """

# Globals for the directions
# Change the values as you see fit
EAST = ["X", "+", "NORTH", "SOUTH"]
NORTH = ["Y", "+", "WEST", "EAST"]
WEST = ["X", "-", "SOUTH", "NORTH"]
SOUTH = ["Y", "-", "EAST", "WEST"]

DIRECTIONS = {"NORTH": NORTH, "EAST": EAST, "SOUTH": SOUTH, "WEST": WEST}


class Robot:
    """ Class for robot simulator """
    def __init__(self, direction: list = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)


    def move(self, instructions: str):
        """ Function to move the robot simulator """
        instructions = list(instructions)
        for instruction in instructions:
            if instruction == "L":
                self.direction = DIRECTIONS[self.direction[2]]
            elif instruction == "R":
                self.direction = DIRECTIONS[self.direction[3]]
            elif instruction == "A":
                if self.direction[0] == "X":
                    self.x_pos = self.x_pos + 1 if self.direction[1] == "+" else self.x_pos - 1
                else:
                    self.y_pos = self.y_pos + 1 if self.direction[1] == "+" else self.y_pos - 1
                self.coordinates = (self.x_pos, self.y_pos)


    def get_position(self):
        """Return current position as tuple"""
        return self.coordinates

    
    def reset(self):
        """Reset robot to origin facing north"""
        self.direction = NORTH
        self.x_pos = 0
        self.y_pos = 0
        self.coordinates = (0, 0)
