class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self.name = name
        self.spent_money = 0
        self.borrow = {}
        self.spent = 0

    def spending(self, spent_money):

        self.spent_money += spent_money

    def paid(self, money, *args):

        self.spent += money
        self_money = money / len(args)

        for Person_obj in args:
            Person_obj.spending(self_money)
            self.set_borrow(Person_obj, self_money)

    def set_borrow(self, Person_obj, self_money):

        if Person_obj.name != self.name:
            if Person_obj.name in self.borrow:
                if self.borrow.get(Person_obj.name) <= self_money:

                    diff = self_money - self.borrow.get(Person_obj.name)
                    print("------------")
                    print(diff, self.borrow.get(Person_obj.name), self_money)
                    Person_obj.update_borrow(diff, self.name)
                    self.borrow.update({Person_obj.name: 0})

                elif self.borrow.get(Person_obj.name) > self_money:

                    diff = self.borrow.get(Person_obj.name) - self_money
                    print("++++++++++++")
                    print(diff, self.borrow.get(Person_obj.name), self_money)
                    self.borrow.update({Person_obj.name: diff})
            else:

                Person_obj.update_borrow(self_money, self.name)

    def update_borrow(self, money, name):

        if self.borrow.get(name):
            money += self.borrow.get(name)

        self.borrow.update({name: money})


Dimas = Person("Dimas")
Orest = Person("Orest")
Vitalik = Person("Vitalik")


Orest.paid(10, Dimas, Orest)
Dimas.paid(20, Dimas, Orest)
Dimas.paid(20, Dimas, Orest)
Dimas.paid(200, Orest, Vitalik)
Orest.paid(10, Dimas, Orest)
Orest.paid(1000, Dimas, Orest, Vitalik)
Dimas.paid(200, Dimas, Orest)
Vitalik.paid(10, Dimas, Orest)
Vitalik.paid(1000, Dimas, Orest)


print(Dimas.name, Dimas.spent, Dimas.spent_money, Dimas.borrow)
print()
print(Orest.name, Orest.spent, Orest.spent_money, Orest.borrow)
print()
print(Vitalik.name, Vitalik.spent, Vitalik.spent_money, Vitalik.borrow)
print()
