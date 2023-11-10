# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python

def valid_ISBN10(isbn):
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[:-1].isdigit() or isbn[:-1] == 'X')):
        return False
    return sum(i * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn, 1)) % 11 == 0


valid_ISBN10('X123456738')
