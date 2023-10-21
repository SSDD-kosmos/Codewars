# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

def per(items):
    if len(items) == 1:
        return [items]
    return [[v]+j for k, v in enumerate(items) for j in per(items[:k] + items[k+1:])]


def permutations(s):
    return list(set([''.join(i) for i in per(list(s))]))


permutations('abcd')
