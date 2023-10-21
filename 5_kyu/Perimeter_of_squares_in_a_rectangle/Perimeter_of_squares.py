def perimeter(n):
    side_len = 1
    counter = 0
    a, b = 0, 1
    while n != counter:
        a, b = b, a + b
        side_len += b
        counter += 1
    print(side_len * 4)
    return side_len * 4


perimeter(7)
