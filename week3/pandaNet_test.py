#!/usr/bin/env python3
# from panda import Panda
from pandaNet import PandaSocialNetwork
from pandaNet import PandaAlreadyThere
from pandaNet import PandasAlreadyFriends
from panda import Panda
import unittest


class Test_PandaNet(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.ana = Panda("Anna", "ann@gmail.com", "female")
        self.desi = Panda("Desi", "desi@dir.bg", "female")
        self.dido = Panda("Dido", "didko@mail.bg", "male")
        self.rado = Panda("Radoslav", "radko@altavista.com", "male")
        self.vyara = Panda("Vyara", "VyaraNadejdaLubov@mail.ru", "female")
        # Has no friends
        self.pesho = Panda("Petar", "peshko@outlook.com", "male")
        # Adding some pandas to the network
        self.pandaland = PandaSocialNetwork()
        self.pandaland.add_panda(self.ivo)
        self.pandaland.add_panda(self.ana)
        self.pandaland.add_panda(self.desi)
        self.pandaland.add_panda(self.dido)
        self.pandaland.add_panda(self.rado)
        self.pandaland.add_panda(self.vyara)
        self.pandaland.add_panda(self.pesho)
        # Not in the network
        self.dora = Panda("Dora", "dora@abv.bg", "female")
        # Ivo's friends are:
        self.pandaland.make_friends(self.ivo, self.vyara)
        self.pandaland.make_friends(self.ivo, self.ana)
        self.pandaland.make_friends(self.ivo, self.rado)
        # Rado's friends are:
        self.pandaland.make_friends(self.rado, self.vyara)
        self.pandaland.make_friends(self.rado, self.desi)
        # Ana's friends are:
        self.pandaland.make_friends(self.ana, self.dido)
        self.pandaland.make_friends(self.ana, self.vyara)

    def test_growth_panda_net(self):
        self.assertIsInstance(self.pandaland, PandaSocialNetwork)

    def test_register_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.pandaland.add_panda(self.pesho)

    def test_has_panda(self):
        self.assertFalse(self.pandaland.has_panda(self.dora))
        self.assertTrue(self.pandaland.has_panda(self.ivo))

    def test_make_friends(self):
        with self.assertRaises(PandasAlreadyFriends):
            self.pandaland.make_friends(self.ivo, self.rado)

    def test_friendship(self):
        self.assertFalse(self.pandaland.are_friends(self.ivo, self.desi))

    def test_all_friends(self):
        self.assertEqual(len(self.pandaland.friends_of(self.pesho)), 0)
        self.assertTrue(type(self.pandaland.friends_of(self.desi)) == list)

    def test_connection(self):
        pass

    def test_connected_pandas(self):
        pass

    def test_how_many_genders(self):
        pass


if __name__ == '__main__':
    unittest.main()
