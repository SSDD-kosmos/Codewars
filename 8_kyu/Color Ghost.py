# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python

import random


class Ghost:
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])
