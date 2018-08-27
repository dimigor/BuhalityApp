class Money(object):
    """docstring for Money"""

    def __init__(self, money):
        self.money = money
        self.paid = 0

    def spent_money(self, money):
        self.money += money

    def paid_money(self, money):
        self.paid += money


class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self.name = name
        self.borrow = {}
        self.Money = Money(0)

    def paid(self, money, *args):

        self.Money.paid_money(money)
        spent_money = money / len(args)

        for Person_obj in args:
            Person_obj.Money.spent_money(spent_money)
            self.set_borrow(Person_obj, spent_money)

    def set_borrow(self, Person_obj, spent_money):

        if Person_obj.name != self.name:
            if Person_obj.name in self.borrow:
                if self.borrow.get(Person_obj.name) <= spent_money:

                    diff = spent_money - self.borrow.get(Person_obj.name)
                    Person_obj.update_borrow(diff, self.name)
                    self.borrow.update({Person_obj.name: 0})

                elif self.borrow.get(Person_obj.name) > spent_money:

                    diff = self.borrow.get(Person_obj.name) - spent_money
                    self.borrow.update({Person_obj.name: diff})
            else:
                Person_obj.update_borrow(spent_money, self.name)

    def update_borrow(self, money, name):

        if self.borrow.get(name):
            money += self.borrow.get(name)

        self.borrow.update({name: money})
