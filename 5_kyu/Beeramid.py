# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

def beeramid(bonus, price):
    remains = bonus
    counter = 1

    if bonus <= 0:
        return 0
    else:
        while remains > 0:
            remains = remains - counter ** 2 * price
            if remains > 0:
                counter += 1
            elif remains == 0:
                counter = counter
            else:
                counter -= 1

    return counter


beeramid(21, 1.5)
