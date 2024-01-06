# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

class Block:

    def __init__(self, parameters):
        self.parameters = parameters

    def get_width(self):
        return self.parameters[0]

    def get_length(self):
        return self.parameters[1]

    def get_height(self):
        return self.parameters[2]

    def get_volume(self):
        return self.parameters[0] * self.parameters[1] * self.parameters[2]

    def get_surface_area(self):
        return 2 * (self.parameters[0] * self.parameters[1]
                    + self.parameters[1] * self.parameters[2]
                    + self.parameters[2] * self.parameters[0])


block1 = Block([2, 2, 2])

