def test_word():
    sentence = 'Hey fellow warriors'
    spin_words(sentence)


def spin_words(sentence):
    """
    Задача: если элемент больше пяти символов, то его требуется развернуть
    :param sentence:
    :return:
    """
    sentence_list = sentence.split()
    index_of_el = 0
    result_list = []
    while index_of_el != len(sentence_list):
        if len(sentence_list[index_of_el]) >= 5:
            sentence_list[index_of_el] = sentence_list[index_of_el][::-1]
            result_list.append(sentence_list[index_of_el])
        else:
            result_list.append(sentence_list[index_of_el])

        index_of_el += 1
    result_list = ' '.join(result_list)
    print(result_list)
    return result_list

# Второй вариант решения
# def spin_words(sentence):
#     L = sentence.split()
#     new = []
#     for word in L:
#         if len(word) >= 5:
#             new.append(word[::-1])
#         else:
#             new.append(word)
#     string = " ".join(new)
#     print(string)
#     return string


test_word()
