def dirReduc(arr):
    d = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    for i in range(len(arr) - 1):
        if d[arr[i]] == arr[i + 1]:
            del arr[i: i+2]
            return dirReduc(arr)
    return arr


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
