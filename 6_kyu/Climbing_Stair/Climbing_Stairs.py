def test_cost():
    cost = [0, 2, 2, 1, 0]
    climbing_stairs(cost)


def climbing_stairs(cost):
    """
    Требуется найти наименьшую стоимость лестницы,
    можно двигаться только на один или два шага вперед
    :param cost:
    :return:
    """
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    new_list = [0] * n  # заполняем список первым элементом
    new_list[0] = cost[0]  # первый эл-т равен первому эл-ту из списка
    new_list[1] = cost[1]  # второй эл-т равен второму эл-ту из списка
    for i in range(2, n):
        new_list[i] = cost[i] + min(new_list[i - 1], new_list[i - 2])
    return min(new_list[-1], new_list[-2])


test_cost()
