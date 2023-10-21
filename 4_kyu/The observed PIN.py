# https://www.codewars.com/kata/5263c6999e0f40dee200059d

import itertools


def get_pins(pin):
    variation = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8'],
    }
    L = [[digit]+variation[digit] for digit in pin]
    return [''.join(el) for el in list(itertools.product(*L))]


get_pins('11')
