def test():
    lst = [-0, 1, 2, -3, 4, 5, -6]
    max_diff(lst)


def max_diff(lst):
    if len(lst) > 1:
        min_number = min(lst)
        max_number = max(lst)
        result_sum = max_number - min_number
        return result_sum
    else:
        return 0


test()
