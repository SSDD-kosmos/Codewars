def two_are_positive(a, b, c):
    positive_list = []
    if a > 0:
        positive_list.append(a)
    if b > 0:
        positive_list.append(b)
    if c > 0:
        positive_list.append(c)

    if len(positive_list) == 2:
        return True
    else:
        return False
