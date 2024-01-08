# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    total_list = []
    for el in a:
        if el not in b:
            total_list.append(el)
    return total_list


# def array_diff(a, b):
#     return [x for x in a if x not in b]
