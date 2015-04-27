#!/usr/bin/env python3

from histogram import Histogram
from unittest import TestCase, main


class Test_Histogram(TestCase):

    def setUp(self):
        self.h = Histogram()
        self.h.add("Apache")
        self.h.add("Apache")

    def test_histogram_init(self):
        self.assertIsInstance(self.h, Histogram)

    def test_agent_adding(self):
        self.assertTrue(self.h._have_agent("Apache"))

    def test_agent_count(self):
        self.assertEqual(self.h.count("Apache"), 2)

    def test_is_dict(self):
        self.assertIsInstance(self.h.get_dict(), dict)
        self.assertEqual(self.h.get_dict(), {"Apache":2})

    def test_histogram_items(self):
        item = ("lighthttpd", 7)
        for count in range(item[1]):
            self.h.add(item[0])

        self.assertTrue(item in self.h.items())

if __name__ == "__main__":
    main()
