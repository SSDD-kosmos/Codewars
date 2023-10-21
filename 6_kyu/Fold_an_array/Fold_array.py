def test():
    array = [1, 2, 3, 4, 5]
    runs = 2
    fold_array(array, runs)


def fold_array(array, runs):
    counter = 0
    while counter != runs:
        counter_inside = 0
        len_arr = len(array)//2
        while counter_inside != len_arr:
            sum_el = array[counter_inside] + array[-1]
            array[counter_inside] = sum_el
            array.remove(array[-1])
            counter_inside += 1
        counter += 1
    print(array)
    return array


test()
