# Globals for the directions
# Change the values as you see fit
EAST = ["X", "+", "NORTH", "SOUTH"]
NORTH = ["Y", "+", "WEST", "EAST"]
WEST = ["X", "-", "SOUTH", "NORTH"]
SOUTH = ["Y", "-", "EAST", "WEST"]

DIRECTIONS = {"NORTH": NORTH, "EAST": EAST, "SOUTH": SOUTH, "WEST": WEST}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)


    def move(self, instructions):
        instructions = list(instructions)
        for instruction in instructions:
            if instruction == "L":
                self.direction = DIRECTIONS[self.direction[2]]
            elif instruction == "R":
                self.direction = DIRECTIONS[self.direction[3]]
            elif instruction == "A":
                if self.direction[0] == "X":
                    if self.direction[1] == "+":
                        self.x_pos += 1
                    else:
                        self.x_pos -= 1
                else:
                    if self.direction[1] == "+":
                        self.y_pos += 1
                    else:
                        self.y_pos -= 1
                self.coordinates = (self.x_pos, self.y_pos)
