""" Robot simulator. """

# Globals for the directions
# Change the values as you see fit
EAST = ["X", "+", "NORTH", "SOUTH"]
NORTH = ["Y", "+", "WEST", "EAST"]
WEST = ["X", "-", "SOUTH", "NORTH"]
SOUTH = ["Y", "-", "EAST", "WEST"]


class Robot:
    """ Class for robot simulator """
    def __init__(self, direction = None, x_pos = None, y_pos = None):
        self.direction = direction if direction else NORTH
        self.x_pos = x_pos if x_pos else 0
        self.y_pos = y_pos if y_pos else 0


    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)


    def move(self, instructions):
        """ Function to move the robot simulator """
        directions = {"NORTH": NORTH, "EAST": EAST, "SOUTH": SOUTH, "WEST": WEST}
        for instruction in instructions:
            if instruction == "L":
                self.direction = directions[self.direction[2]]
            elif instruction == "R":
                self.direction = directions[self.direction[3]]
            elif instruction == "A":
                if self.direction[0] == "X":
                    self.x_pos = self.x_pos + 1 if self.direction[1] == "+" else self.x_pos - 1
                else:
                    self.y_pos = self.y_pos + 1 if self.direction[1] == "+" else self.y_pos - 1


    def get_position(self):
        """Return current position as tuple"""
        return self.coordinates

    
    def reset(self):
        """Reset robot to origin facing north"""
        self.direction = NORTH
        self.x_pos = 0
        self.y_pos = 0
        self.coordinates = (0, 0)
