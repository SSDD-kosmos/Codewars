def zeros(n):
    pow_of_5 = 5
    zero = 0

    while n >= pow_of_5:
        zero += n // pow_of_5
        pow_of_5 *= 5
    print(zero)
    return zero

# def zeros(n):
#   x = n/5
#   return x+zeros(x) if x else 0


zeros(150)
