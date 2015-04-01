#!/usr/bin/env python3
# from panda import Panda
from pandaNet import PandaSocialNetwork
from pandaNet import PandaAlreadyThere
from pandaNet import PandasAlreadyFriends
from panda import Panda
import unittest


class Test_PandaNet(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo","ivo@pandamail.com", "male")
        self.drago = Panda("Drago", "drago@yahoo.com", "male")
        self.iva = Panda("Iva", "iva@gmail.com","female")
        self.dora = Panda("Dora", "dora@abv.bg", "female")
        self.pandaland = PandaSocialNetwork()

    def test_growth_panda_net(self):
        self.assertIsInstance(self.pandaland, PandaSocialNetwork)

    def test_register_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.pandaland.add_panda(self.drago)
            self.pandaland.add_panda(self.drago)

    def test_has_panda(self):
        self.pandaland.add_panda(self.drago)
        self.assertTrue(self.pandaland.has_panda(self.drago))
        self.assertFalse(self.pandaland.has_panda(self.ivo))

    def test_make_friends(self):
        with self.assertRaises(PandasAlreadyFriends):
            self.pandaland.make_friends(self.ivo, self.dora)

    def test_friendship(self):
         self.assertFalse(self.pandaland.are_friends(self.ivo,
                                                     self.drago))

    def test_relationship(self):
        pass

    def test_connection(self):
        pass

    def test_connected_pandas(self):
        pass

    def test_how_many_genders(self):
        pass


if __name__ == '__main__':
    unittest.main()
