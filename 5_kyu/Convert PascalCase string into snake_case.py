# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

def to_underscore(string):
    string = str(string)
    res_str = ''.join([el if el.islower() or el.isdigit() else '_' + el.lower() for el in string])
    if string[0].isupper():
        print(res_str[1:])
        return res_str[1:]
    else:
        return res_str


to_underscore(1)
