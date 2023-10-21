def test():
    s = "test case"
    camel_case(s)


def camel_case(s):
    s_list = []
    result_list = []
    s = s.split()
    for el in s:
        s_list.append(el)
    for el in s_list:
        el = el.title()
        result_list.append(el)
    return ''.join(result_list)


# def camel_case(string):
#     return string.title().replace(" ", "")


test()
