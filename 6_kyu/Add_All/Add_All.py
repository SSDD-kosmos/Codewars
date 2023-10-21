def test():
    lst = [1, 2, 3, 4, 5]
    add_all(lst)


def add_all(lst):
    result = []
    while len(lst) > 1:
        lst.sort()
        first_two_from_list = lst.pop(0) + lst.pop(0)
        lst.append(first_two_from_list)
        result.append(first_two_from_list)
    return sum(result)


test()
