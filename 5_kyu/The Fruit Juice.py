# https://www.codewars.com/kata/5264603df227072e6500006d/train/python

class Jar:
    def __init__(self):
        self.total = 0
        self.fruits = dict()

    def add(self, amount, kind):
        self.fruits[kind] = self.fruits.get(kind, 0) + amount
        self.total += amount

    def pour_out(self, amount):
        self.fruits = {k: v * (self.total - amount) / self.total for k, v in self.fruits.items()}
        self.total -= amount

    def get_total_amount(self):
        return self.total

    def get_concentration(self, kind):
        return self.fruits.get(kind, 0) / self.total if self.total else 0


jar = Jar()
jar.add(100, "apple")
jar.add(100, "apple")
jar.add(200, "banana")
jar.pour_out(200)
jar.add(200, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))
