def test():
    arr = [3, 3, 2, 9, 7]
    cut_the_ropes(arr)


def cut_the_ropes(arr):
    arr = sorted(arr)
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        arr = [el - arr[0] for el in arr]
        try:
            while True:
                arr.remove(0)
        except ValueError:
            pass
    print(result)
    return result


test()
