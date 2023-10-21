def test():
    r, g, b = -20, 275, 125
    rgb(r, g, b)


def color(RGB):
    if RGB > 255:
        RGB = 255
    elif RGB < 0:
        RGB = 0
    RGB = hex(RGB)[2:].upper()
    if len(RGB) < 2:
        RGB = '0' + RGB
    return RGB


def rgb(r, g, b):
    return color(r) + color(g) + color(b)


test()
