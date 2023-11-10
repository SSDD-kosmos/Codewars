# https://www.codewars.com/kata/5981ff1daf72e8747d000091/train/python

import math


class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        new_volume = other.volume + self.volume

        x = self.volume/new_volume
        y = other.volume/new_volume

        new_color1 = math.ceil(x*self.color[0] + y*other.color[0])
        new_color2 = math.ceil(x*self.color[1] + y*other.color[1])
        new_color3 = math.ceil(x*self.color[2] + y*other.color[2])
        return Potion((new_color1, new_color2, new_color3), new_volume)

