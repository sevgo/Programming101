#!/usr/bin/env python3


class BankAccount:

    __history = []

    def __init__(self, name, amount, currency):
        self.name = name
        self.amount = amount
        self.currency = currency
        self.__history = ['Account was created']

    def deposit(self, money):
        if money <= 0:
            raise ValueError
        elif not isinstance(money, int):
            raise TypeError
        else:
            self.amount += money
            self.__history.append('Deposited {}BGN'.format(money))

    def balance(self):
        self.__history.append('Balance check -> {}BGN'.format(self.amount))
        #print(self.amount)
        return self.amount

    def withdraw(self, money):
        if money > self.amount:
            raise ValueError
        elif not isinstance(money, int):
            raise TypeError
        else:
            self.amount -= money
            self.__history.append('{}BGN was withdrawed'.format(money))
            return True

        return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name,
                                                                  self.amount,
                                                                  self.currency)

    def __int__(self):
        self.__history.append('__int__ check -> {}{}'.format(self.amount,
                                                              self.currency))
        return self.balance()

    def __eq__(self, other):
        if self.currency == other.currency:
            return True

        return False

    def transfer_to(self, other, amount):
        if self == other:
            self.withdraw(amount)
            other.deposit(amount)
            self.__history.append("Transfer to {} for {}{}".format(other.name,
                                                                    amount,
                                                                    self.currency))
            return True

        return False

    def history(self):
        # print(self.__history)
        return self.__history


if __name__ == '__main__':
    user1 = BankAccount("Ivan", 100, "BGN")
    user2 = BankAccount("Petar", 20, "BGN")
    print(user1)
    print(user2)
    user1.deposit(100)
    user2.withdraw(10)
    print(user1.balance())
    user1.transfer_to(user2, 70)
    print(user1.history())
    print(user2.balance())
    print(user2.history())
