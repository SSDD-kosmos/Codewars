from collections import Counter


def count_test():
    s = 'aba'
    count(s)


def count(s):
    """
    Требуется посчитать сколько раз повторяется каждый символ и вывести
    Пример подсчета: {'a': 2, 'b': 1}
    :param s:
    :return:
    """
    if len(s) > 0:
        counter = {}
        for el in s:
            if el in counter:
                counter[el] += 1
            else:
                counter[el] = 1
        print(counter)
        return counter
    else:
        return {}


# Более легкий способ
# def count(s):
#     return Counter(s)


count_test()
