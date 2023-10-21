"""
https://www.codewars.com/kata/5511b2f550906349a70004e1
"""


def last_digit(n1, n2):
    if n2 > 0:
        last_digit_list = [n1 ** x % 10 for x in range(1, 5)]
        res_last_digit = n2 % 4
        print(last_digit_list[res_last_digit-1])
        return last_digit_list[res_last_digit-1]
    else:
        return 1


last_digit(2 ** 200, 2 ** 300)
