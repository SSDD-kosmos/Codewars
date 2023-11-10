# https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python

def solution(array_a, array_b):
    res_list = []
    counter = 0
    for i in array_a:
        res_list.append((i - array_b[counter]) ** 2)
        counter += 1
    res = sum(res_list)/len(res_list)
    return int(res)


solution([1, 2, 3], [4, 5, 6])
