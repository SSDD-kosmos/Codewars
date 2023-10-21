def test():
    message = 'Hello World!'
    key = -5
    encryptor(key, message)


def encryptor(key, message):
    """
    Суть задачи реализовать шифр цезаря
    :param key: Шаг сдвига
    :param message: Строка
    :return: Зашифрованная строка, все символы перемещены на key элементов
    """
    result_text = ''
    for el in message:
        if el.isupper():
            index_ascii = ord(el) - ord('A')
            new_index = (index_ascii + key) % 26
            new_ascii = new_index + ord('A')
            new_letter = chr(new_ascii)
            result_text = result_text + new_letter
        elif el.islower():
            index_ascii = ord(el) - ord('a')
            new_index = (index_ascii + key) % 26
            new_ascii = new_index + ord('a')
            new_letter = chr(new_ascii)
            result_text = result_text + new_letter
        else:
            result_text += el
    print(result_text)
    return result_text


test()
