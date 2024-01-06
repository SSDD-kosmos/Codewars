# https://www.codewars.com/kata/52eb114b2d55f0e69800078d/train/python

class Cipher(object):
    def __init__(self, map1: str, map2: str):
        self.map1 = map1
        self.map2 = map2

    def encode(self, abc):
        res_str = ''
        for el in abc:
            try:
                res_str += self.map2[(self.map1.index(el))]
            except ValueError:
                res_str += el
        return res_str

    def decode(self, abc):
        res_str = ''
        for el in abc:
            try:
                res_str += self.map1[(self.map2.index(el))]
            except ValueError:
                res_str += el
        return res_str


cipher = Cipher("abcdefghijklmnopqrstuvwxyz", "et")
print(cipher.encode('abc'))
