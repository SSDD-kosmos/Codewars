# https://www.codewars.com/kata/532a69ee484b0e27120000b6/train/python

class Vector:

    def __init__(self, cords: list):
        self.cords = cords
        self.x = cords[0]
        self.y = cords[1]
        self.z = cords[2]

    def check_length(self, other):
        if len(self.cords) == len(other.cords):
            return True
        return 'Different length cords'

    def add(self, other):
        if Vector.check_length(self, other):
            cords = []
            for i in range(len(self.cords)):
                cords.append(self.cords[i] + other.cords[i])
            return Vector(cords)

    def subtraction(self, other):
        if Vector.check_length(self, other):
            cords = []
            for i in range(len(self.cords)):
                cords.append(self.cords[i] - other.cords[i])
            return Vector(cords)

    def dot(self, other):
        if Vector.check_length(self, other):
            cords = []
            for i in range(len(self.cords)):
                cords.append(self.cords[i] * other.cords[i])
            return sum(cords)

    def __str__(self):
        return f'<{self.cords[0]}, {self.cords[1]}, {self.cords[2]}'








