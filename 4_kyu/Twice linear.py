# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_linear(n):
    num_list = [1]
    for i in num_list:
        num_list.append((i * 2) + 1)
        num_list.append((i * 3) + 1)
        if len(num_list) > n * 10:
            break
    return sorted(list(set(num_list)))[n]


dbl_linear(20)
