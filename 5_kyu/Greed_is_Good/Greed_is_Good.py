from collections import Counter


def score(dice):
    res_score = 0
    for keys, value in Counter(dice).items():
        if value >= 3 and keys != 1:
            res_score += keys * 100
            value -= 3
        elif value >= 3 and keys == 1:
            res_score += 1000
            value -= 3

        if keys == 1 and value != 0:
            res_score += value * 100
        elif keys == 5 and value != 0:
            res_score += value * 50
    print(res_score)
    return res_score


# def score(dice):
#     score, data = 0, {1:(0,100,200,1000,1100,1200),
#                       2:(0,0,0,200,200,200),
#                       3:(0,0,0,300,300,300),
#                       4:(0,0,0,400,400,400),
#                       5:(0,50,100,500,550,600),
#                       6:(0,0,0,600,600,600)}
#     for i in data:
#         score += (data[i][dice.count(i)])
#     return score


score([5, 1, 3, 4, 1])
