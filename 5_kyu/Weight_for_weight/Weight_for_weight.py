def order_weight(strng):
    weight = sorted(sorted(strng.split()), key=summa)
    return ' '.join(weight)


def summa(n):
    return sum([int(i) for i in n])


order_weight("103 123 4444 99 2000")
