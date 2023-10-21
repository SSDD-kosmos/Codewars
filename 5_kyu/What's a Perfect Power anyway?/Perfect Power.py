# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

def isPP(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]
    return None


isPP(27)
