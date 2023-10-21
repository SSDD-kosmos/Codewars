def test():
    s = 'ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'
    generate_hashtag(s)


def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output


test()
