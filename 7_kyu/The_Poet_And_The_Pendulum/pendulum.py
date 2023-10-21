def test():
    values = [94, 84, -6, -19, 3]
    pendulum(values)


def pendulum(values):
    """
    Задача расположить элементы списка в порядке маятника,
    по центру минимальный
    :param values:
    :return:
    """
    n = len(values)
    index = 0
    result_list = [0] * n
    values.sort()
    if n % 2 != 0:
        ind = 1
        result_list[n // 2] = values[0]
        if n // 2 % 2 != 0:
            while ind != n//2+1:
                result_list[n // 2 + ind] = values[index + 1]
                result_list[n // 2 - ind] = values[index + 2]
                index += 2
                ind += 1
        else:
            while ind != n//2+1:
                result_list[n // 2 + ind] = values[index + 1]
                result_list[n // 2 - ind] = values[index + 2]
                index += 2
                ind += 1
    else:
        ind = 0
        result_list[n // 2 - 1] = values[0]
        while ind != n//2-1:
            result_list[n // 2 + ind] = values[index + 1]
            result_list[n // 2 - ind - 2] = values[index + 2]
            result_list[-1] = values[-1]
            index += 2
            ind += 1
    print(result_list)
    return result_list


test()
