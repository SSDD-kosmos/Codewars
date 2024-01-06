# https://www.codewars.com/kata/572bbd7c72a38bd878000a73/train/python

class Fraction:

    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.top = numerator / g
        self.bottom = denominator / g

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        numerator = self.top * other.bottom + self.bottom * other.top
        denominator = self.bottom * other.bottom
        return Fraction(numerator, denominator)

    def __str__(self):
        return str(int(self.top)) + "/" + str(int(self.bottom))


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
