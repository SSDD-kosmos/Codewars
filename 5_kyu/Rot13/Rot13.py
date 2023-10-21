# def rot13(message):
#     """
#     Задача реализовать простой шифр, и сместить все буквы на 13 символов, другие знаки не трогаем
#     :param message:
#     :return:
#     """
#     result_list = []
#     for i in message:
#         if i.isalpha():
#             if i.isupper():
#                 if ord(i) + 13 > 90:
#                     result_list.append(ord(i) - 13)
#                 else:
#                     result_list.append(ord(i) + 13)
#             if i.islower():
#                 if ord(i) + 13 > 122:
#                     result_list.append(ord(i) - 13)
#                 else:
#                     result_list.append(ord(i) + 13)
#         else:
#             result_list.append(ord(i))
#     result = [''.join([chr(i) for i in result_list])]
#     print(result[0])
#     return result[0]

def rot13(message):
    """
    Задача реализовать простой шифр, и сместить все буквы на 13 символов, другие знаки не трогаем
    :param message:
    :return:
    """
    result = ''
    for i in message:
        if ord('A') <= ord(i) <= ord('M') or ord('a') <= ord(i) <= ord('m'):
            result += chr(ord(i) + 13)
        elif ord('N') <= ord(i) <= ord('Z') or ord('n') <= ord(i) <= ord('z'):
            result += chr(ord(i) - 13)
        else:
            result += i
    return result


rot13('Test!')
