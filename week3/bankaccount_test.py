#!/usr/bin/env python3
import unittest
from bankaccount import BankAccount


class Test_BankAccount(unittest.TestCase):

    def setUp(self):
        self.user1 = BankAccount("Ivan", 100, "BGN")
        self.user2 = BankAccount("Petar", 20, "BGN")

    def test_create_new_account(self):
        self.assertIsInstance(self.user1, BankAccount)
        self.assertIsInstance(self.user2, BankAccount)

    def test_validate_deposit(self):
        with self.assertRaises(ValueError):
            self.user2.deposit(-10)

        with self.assertRaises(TypeError):
            self.user1.deposit("10")

    def test_return_balance(self):
        self.assertEqual(self.user1.amount, 100)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.user1.withdraw(200)

        with self.assertRaises(TypeError):
            self.user1.withdraw("25")

    def test_if_string(self):
        self.assertEqual(str(self.user2),
                         "Bank account for {} with balance of {}{}".format(
            self.user2.name, self.user2.amount, self.user2.currency))

    def test_if_int(self):
        self.assertTrue(int(self.user2) == 20)

    def test_currency_comparison(self):
        self.assertEqual(self.user1.currency, self.user2.currency)

    def test_transfer_money(self):
        self.assertTrue(self.user1.transfer_to(self.user2, 10))

    def test_history(self):
        self.assertGreater(len(self.user1.history()), 0)

if __name__ == '__main__':
    unittest.main()
