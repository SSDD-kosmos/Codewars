# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python

def josephus(items, k):
    res_list = []
    counter = 0
    while len(items) > 0:
        j = (counter + k - 1) % len(items)
        res_list.append(items[j])
        del items[j]
        counter = j if j < len(items) else 0
    return res_list


josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
