def test():
    text, width, tick = 'Beautiful is better than ugly.', 10, 5
    ticker(text, width, tick)


def ticker(text, width, tick):
    padding = ' ' * width
    text = padding + text

    counter = 0
    while counter <= tick:
        padding = text[counter:counter + width]
        counter += 1
        if counter > len(text) - width:
            text += text
    return padding


test()


# class Ticker:
#
#     def __init__(self, text='', width=0, tick=0):
#         self.text = str(text)
#         self.width = int(width)
#         self.tick = int(tick)
#
#     def ticker_class(self):
#         padding = ' ' * self.width
#         text = padding + self.text
#
#         counter = 0
#         while counter <= self.tick:
#             padding = text[counter:counter + self.width]
#             counter += 1
#             if counter > len(text) - self.width:
#                 text += text
#         return padding
