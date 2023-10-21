import math


def test():
    a, b, c = [8, 5, 7]
    triangle_type(a, b, c)


def triangle_type(a: float, b: float, c: float):
    if a + b > c and a + c > b and b + c > a:
        cos_a = round(math.degrees(math.acos(float(a**2 + c**2 - b**2) / float(2*a*c))))
        cos_b = round(math.degrees(math.acos(float(a**2 + b**2 - c**2) / float(2*a*b))))
        cos_c = round(180 - cos_a - cos_b)
        if cos_c < 90 and cos_b < 90 and cos_a < 90:
            return 1
        elif cos_c == 90 or cos_b == 90 or cos_a == 90:
            return 2
        else:
            return 3
    else:
        return 0


test()
