def max_sequence(arr):
    """
    Задача найти максимальную сумма подпоследовательности
    :param arr:
    :return:
    """
    max_sum = summa = 0
    for i in arr:
        summa += i
        max_sum = max(max_sum, summa)  # проверка, что не максимальная ли наша прошлая сумма
        if summa < 0:
            summa = 0
    return max_sum


max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
