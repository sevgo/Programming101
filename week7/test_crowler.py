#!/usr/bin/env python3

from unittest import main, TestCase
from crowler import Crowler


class Test_Crowler(TestCase):
    def setUp(self):
        self.crowler = Crowler()
