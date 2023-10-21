import pyfiglet


def test():
    string = 'heLLo WorLD'
    block_print(string)


def block_print(string):
    string = string.upper()
    ascii_string = pyfiglet.figlet_format(string, font='alphabet')
    print(ascii_string)


test()
