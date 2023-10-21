s = []
for i in range(ord('a'), ord('z')+1):
    s += chr(i)


def word_1():
    word = 'CodEWaRs'

    capitals(word)


def capitals(word):
    index_of_letter = 0
    res_list = []
    while index_of_letter != len(word):
        if word[index_of_letter] not in s:
            res_list.append(index_of_letter)

        index_of_letter += 1

    # print(res_list)
    return res_list


# def capitals(word):
#     uppers = []
#     for i in range(len(word)):
#         if word[i].isupper():
#             uppers.append(i)
#     return uppers


word_1()
