# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    if number >= 3:
        total_list = []
        for el in range(number):
            if el % 3 == 0 or el % 5 == 0:
                total_list.append(el)
        return sum(total_list)
    return 0
