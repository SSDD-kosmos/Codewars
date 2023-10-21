from collections import Counter


def test():
    dice = [1,1,1]
    get_score(dice)


scores = {
    1: [100, 200, 1000, 2000, 3000, 4000],
    2: [0, 0, 200, 400, 600, 800],
    3: [0, 0, 300, 600, 900, 1200],
    4: [0, 0, 400, 800, 1200, 1600],
    5: [50, 100, 500, 1000, 1500, 2000],
    6: [0, 0, 600, 1200, 1800, 2400]
}


def get_score(dice):
    dice = dict(Counter(dice))
    print(dice)
    dice_len = len(dice)
    if dice_len == 6:
        return 1000
    if dice_len == 3 and all([x == 2 for x in dice.values()]):
        return 750
    return sum([scores[x][y-1] for x, y in dice.items()]) or 'Zonk'


test()
