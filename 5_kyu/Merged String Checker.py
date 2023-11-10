# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

def is_merge(s, p1, p2):
    return \
        p1 and p1[0] == s[0] and is_merge(s[1:], p1[1:], p2) or \
        p2 and p2[0] == s[0] and is_merge(s[1:], p1, p2[1:]) or \
        False if s else not p1 and not p2


is_merge("Can we merge it? Yes, we can!", "Canwe it, ", "  merge? Yeswe can!")
