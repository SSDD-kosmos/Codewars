def matrix():
    arr = [[1, 2, 3], [4, 5, 6]]
    transpose(arr)


def transpose(arr):
    return [list(el) for el in zip(*arr)]


matrix()
