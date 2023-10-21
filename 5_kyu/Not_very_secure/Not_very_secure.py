def test():
    password = 'PassW0rld'
    alphanumeric(password)


letter_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for el in range(ord('a'), ord('z')+1):
    letter_number += chr(el)

for el in range(ord('A'), ord('Z')+1):
    letter_number += chr(el)


def alphanumeric(password):
    """
    Требуется проверить чтобы в строке были только буквы и цифры
    :param password:
    :return:
    """
    result_list = []
    if password == '':
        return False
    else:
        for letter in password:
            if letter not in letter_number:
                result_list.append(letter)

        print(result_list)

        if len(result_list) == 0:
            print(True)
            return True
        else:
            print(False)
            return False

# Второй способ

# def alphanumeric(password):
#     return password.isalnum()


test()
