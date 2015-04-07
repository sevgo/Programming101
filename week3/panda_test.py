#!/usr/bin/env python3
import unittest
from panda import Panda, NotValidEmail


class Test_Panda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo","ivo@pandamail.com", "male")
        self.drago = Panda("Drago", "drago@yahoo.com", "male")
        self.iva = Panda("Iva", "iva@gmail.com","female")
        self.dora = Panda("Dora", "dora@abv.bg", "female")

    def test_panda_birth(self):
        self.assertIsInstance(self.dora, Panda)
        self.assertIsInstance(self.drago, Panda)

    def test_email_address(self):
        with self.assertRaises(NotValidEmail):
            self.dora.mail = self.dora._email('.asd@fgg')

    def test_gender(self):
        self.assertTrue(self.iva._gender() == 'female')
        self.assertTrue(self.drago._gender() == 'male')

    def test_is_female(self):
        self.assertTrue(self.iva.isFemale())
        self.assertFalse(self.iva.isMale())


    def test_compare_pandas(self):
        gosho = Panda("Ivo","ivo@pandamail.com", "male")
        self.assertEqual(self.ivo, gosho)
        self.assertFalse(self.iva == self.dora)

    def test_panda_hash(self):
        self.assertIsInstance(hash(self.drago), int)


if __name__ == '__main__':
    unittest.main()
