def test():
    n = 30
    count_zeros_n_double_fact(n)


def count_zeros_n_double_fact(n):
    numbers_list = []
    if n % 2 == 0:
        counter = 2
    else:
        counter = 1

    while counter != n+2:
        numbers_list.append(counter)
        counter += 2

    while len(numbers_list) != 1:
        result_number = numbers_list.pop(0) * numbers_list.pop(0)
        numbers_list.append(result_number)

    count_zero = 0
    while numbers_list[0] % 10 == 0:
        numbers_list[0] //= 10
        count_zero += 1

    return count_zero


test()
