# s = []
# for i in range(ord('a'), ord('z')+1):
#     s += chr(i)
#
#
# def pig_it(text):
#     """
#     Требовалось первую букву слова переместить в конец слова и добавить ay,
#     не трогая знаки препинания
#     :param text:
#     :return:
#     """
#     if text[-1] in s:
#         result = ("{}".format(
#             ' '.join([''.join((x[1:], x[0], 'ay'))
#                       for x in text.replace('.', '').split()])))
#         print(result)
#     else:
#         symbol = [text[-1]]
#         text = text.replace(text[-1], '')
#         result = ("{}".format(
#             ' '.join([''.join((x[1:], x[0], 'ay'))
#                       for x in text.replace('.', '').split()])))
#         symbol = ' '.join(map(str, symbol))
#         result = result + ' ' + str(symbol)
#         print(result)

def pig_it(text):
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split()])


pig_it('Pig Latin is cool !')
