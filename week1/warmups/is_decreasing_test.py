#!/usr/bin/env python3

from unittest import TestCase, main
from is_decreasing import is_decreasing


class Test_IS_Decreasing(TestCase):

    def test_dec(self):
        self.assertFalse(is_decreasing([99, 0.0900, 0.9, 0.38]))


if __name__ == "__main__":
    main()
