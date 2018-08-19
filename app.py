"""
Created by Dimitri Gorbachevskii
"""


class Money(object):
    """docstring for Money"""

    def __init__(self, amount):

        self.amount = amount

    def getBorrow():
        pass


class Person(object):
    """docstring for Person"""

    def __init__(self, name):

        self.name = name
        self.spent_money = 0
        self.has_paid = 0
        self.borrow = {}
        self.spenting_money = 0

    def spending(self, spent_money):

        self.spent_money += spent_money

    def paid(self, money, *args):
        self.has_paid = money
        self_money = money / len(args)
        for Person_obj in args:
            Person_obj.spending(self_money)

            if Person_obj.name != self.name:
                Person_obj.getBorrow(self_money, self.name)

    def getBorrow(self, spent_money, name):

        self.spenting_money += spent_money
        self.borrow.update({name: self.spenting_money})


Dimas = Person("Dimas")
Orest = Person("Orest")
Vitalik = Person("Vitalik")


Dimas.paid(10, Dimas, Orest)

Orest.paid(10, Dimas, Orest)
#Orest.paid(10, Dimas, Orest)
Vitalik.paid(10, Dimas, Vitalik, Orest)

print(Dimas.spent_money, Dimas.borrow)
print()
print(Orest.spent_money, Orest.borrow)
print()
print(Vitalik.spent_money, Vitalik.borrow)
# print(Vitalik.spent_money)

# print(Dimas.has_paid)
# print(Orest.has_paid)
# print(Vitalik.has_paid)
