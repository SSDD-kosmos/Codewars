def tuple_1():
    pairs = [(2, 3), (3, 4), (1, 2)]

    len_longest_chain(pairs)


def len_longest_chain(pairs):
    p = sorted(pairs, key=lambda x: (x[1], x[0]))
    i = 1
    j = 0
    res_len = 1
    while len(pairs) > i:
        if p[j][1] < p[i][0]:
            res_len += 1
            j = i
        i += 1
    print(res_len)
    return res_len


tuple_1()
