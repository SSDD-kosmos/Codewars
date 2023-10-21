def test():
    s = "312"
    explode(s)


def explode(s):
    n = 0
    list_s = []
    while n != len(s):
        list_s.append(s[n])
        list_s[n] = list_s[n] * int(list_s[n])
        n += 1
    res = ''.join(list_s)
    return res


test()
