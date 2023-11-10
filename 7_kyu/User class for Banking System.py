# https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, draw):
        if self.balance - draw < 0:
            return ValueError()
        else:
            self.balance -= draw
            return f'{self.name} has {self.balance}.'

    def check(self, other, sum):
        if not other.checking_account or other.balance < sum:
            raise ValueError()
        self.balance += sum
        other.balance -= sum
        return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'

    def add_cash(self, sum):
        self.balance += sum
        return f'{self.name} has {self.balance}.'


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

Jeff.withdraw(2)
print(Joe.check(Jeff, 50))
