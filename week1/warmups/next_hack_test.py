#!/usr/bin/env python3

from unittest import TestCase, main
from next_hack import is_hack_number, next_hack


class Test_Next_Hack(TestCase):

    def setUp(self):
        self.number = 10

    def test_is_hack_number(self):
        self.assertFalse(is_hack_number(self.number))

    def test_next_hack(self):
        self.assertEqual(next_hack(10), 21)


if __name__ == "__main__":
    main()
