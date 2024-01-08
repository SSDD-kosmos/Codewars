# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    for el in set(seq):
        if seq.count(el) % 2 == 1:
            return el
    return None
