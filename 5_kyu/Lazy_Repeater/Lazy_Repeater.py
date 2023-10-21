from itertools import cycle


def make_looper(string):
    """
    Требовалось каждый раз выводить следующий элемент строки
    :param string:
    :return: каждый раз следующий элемент строки
    """
    return cycle(string).__next__
