# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python

class Vector:

    def __init__(self, cords: list):
        self.cords = cords

    def __str__(self):
        return str(tuple(self.cords)).replace(' ', '')

    def check_length(self, other):
        if len(self.cords) == len(other.cords):
            return True
        return 'Different length'

    def add(self, other):
        if Vector.check_length(self, other):
            cords = []
            for i in range(len(self.cords)):
                cords.append(self.cords[i] + other.cords[i])
            return Vector(cords)

    def subtract(self, other):
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

    def norm(self):
        return sum(el ** 2 for el in self.cords) ** 0.5

    def equals(self, other):
        if Vector.check_length(self, other):
            return self.cords == other.cords
