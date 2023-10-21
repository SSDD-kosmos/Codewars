# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    result_list = []
    while len(snail_map) > 0:
        for el in snail_map[0]:
            result_list.append(el)
        del snail_map[0]

        for el in range(len(snail_map)):
            result_list.append(snail_map[el][-1])
            del snail_map[el][-1]

        if len(snail_map) > 1:
            for el in snail_map[-1][::-1]:
                result_list.append(el)
            del snail_map[-1]

        for el in reversed(range(len(snail_map))):
            result_list.append(snail_map[el][0])
            del snail_map[el][0]

    print(result_list)
    return result_list


snail([[1, 2, 3, 4],
       [12, 13, 14, 5],
       [11, 16, 15, 6],
       [10, 9, 8, 7]])
