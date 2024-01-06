# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        secret_code = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                index = ((self.alphabet.index(text[i]) + self.alphabet.index(self.key[i % (len(self.key))]))
                         % len(self.alphabet))
                secret_code += self.alphabet[index]
            else:
                secret_code += text[i]
        return secret_code

    def decode(self, text):
        original_text = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                index = ((self.alphabet.index(text[i]) - self.alphabet.index(self.key[i % (len(self.key))]))
                         % len(self.alphabet))
                original_text += self.alphabet[index]
            else:
                original_text += text[i]
        return original_text


code = VigenereCipher('カタカナ', 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー')
print(code.encode('タモタワ'))











