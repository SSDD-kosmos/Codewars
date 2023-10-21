# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python

def custom_key(elems):
    return -len(elems), elems.lower()


def mix(s1, s2):
    res_list = []
    s1_set = {el for el in s1 if el.isalpha() and el.islower()}
    s2_set = {el for el in s2 if el.isalpha() and el.islower()}
    union_set = s1_set.union(s2_set)

    for el in union_set:
        if s1.count(el) > 1 or s2.count(el) > 1:
            if s1.count(el) > s2.count(el):
                res_list.append('1:' + str(el * s1.count(el)))
            elif s1.count(el) < s2.count(el):
                res_list.append('2:' + str(el * s2.count(el)))
            elif s1.count(el) == s2.count(el):
                res_list.append('=:' + str(el * s1.count(el)))
    res_list = sorted(res_list, key=custom_key)
    print('/'.join(res_list))
    return '/'.join(res_list)


mix("Are they here", "yes, they are here")
