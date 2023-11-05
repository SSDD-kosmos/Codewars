import bisect


def test():
    list_abc = [1, 2, 3, 4, 5]
    bisect.insort(list_abc, 2.23)
    print(list_abc)


test()
