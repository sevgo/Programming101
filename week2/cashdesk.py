#!/usr/bin/env python3
class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A bill of ${}".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))

    def __int__(self):
        return int(self.amount)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        total = 0
        for element in self.bills:
            total += int(element)

        return total

    def __int__(self):
        return self.total()

    def __repr__(self):
        return self.bills


class CashDesk:

    def __init__(self):
        self.desk = []

    def take_money(self, money):
        # self.desk.append(money)
        self.desk += money

    def total(self):
        total = 0
        for money in self.desk:
            total += int(money)

        return total

    def __getitem__(self, index):
        return int(self.desk[index])

    # def inspect(self):



if __name__ == '__main__':
    amounts = [10, 20, 30, 40, 50]
    bills = [Bill(y) for y in amounts]
    batch = BatchBill(bills)
    desk = CashDesk()
    desk.take_money(batch)
    print(desk)
