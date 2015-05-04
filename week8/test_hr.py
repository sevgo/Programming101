#!/usr/bin/env python3
from hr import HackBulgaria
from unittest import TestCase


class Test_HB(TestCase):

    def setUp(self):
        self.hb = HackBulgaria.read_json_from_web(
            'https://hackbulgaria.com/api/students/')
