# import bisect
#
#
# def test():
#     list_abc = [1, 2, 3, 4, 5]
#     bisect.insort(list_abc, 2.23)
#     print(list_abc)
#
#
# test()


# ---------------------

def solution(array):
    return [number ** 2 if number >= 0 else -(number ** 2) for number in array]


solution([-3, 1, 2, 3])
