def move_zeros(lst):
    """
    Задача переместить все нули в конец списка
    :param lst:
    :return:
    """
    return [i for i in lst if i != 0] + [0] * lst.count(0)


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
