#!/usr/bin/env python3
# from panda import Panda
from pandaNet import PandaSocialNetwork
from pandaNet import PandaAlreadyThere
from pandaNet import PandasAlreadyFriends
from panda import Panda
import unittest


class Test_PandaNet(unittest.TestCase):

    def setUp(self):
        # Adding some pandas to the network
        self.pNet = PandaSocialNetwork()
        #
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.ana = Panda("Anna", "ann@gmail.com", "female")
        self.desi = Panda("Desi", "desi@dir.bg", "female")
        self.dido = Panda("Dido", "didko@mail.bg", "male")
        self.rado = Panda("Radoslav", "radko@altavista.com", "male")
        self.vyara = Panda("Vyara", "VyaraNadejdaLubov@mail.ru", "female")
        # Has no friends
        self.pesho = Panda("Petar", "peshko@outlook.com", "male")
        self.pNet.add_panda(self.ivo)
        self.pNet.add_panda(self.ana)
        self.pNet.add_panda(self.desi)
        self.pNet.add_panda(self.dido)
        self.pNet.add_panda(self.rado)
        self.pNet.add_panda(self.vyara)
        self.pNet.add_panda(self.pesho)
        # Not in the network
        self.dora = Panda("Dora", "dora@abv.bg", "female")
        # Ivo's friends are:
        self.pNet.make_friends(self.ivo, self.vyara)
        self.pNet.make_friends(self.ivo, self.rado)
        # Rado's friends are:
        self.pNet.make_friends(self.rado, self.desi)
        # Ana's friends are:
        self.pNet.make_friends(self.ana, self.dido)
        self.pNet.make_friends(self.ana, self.vyara)
        self.pNet.make_friends(self.ana, self.ivo)
        self.cveti = Panda("Cveti", "cv_e_ti@abv.bg", "female")

    def test_growth_panda_net(self):
        self.assertIsInstance(self.pNet, PandaSocialNetwork)

    def test_register_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.pNet.add_panda(self.pesho)

    def test_has_panda(self):
        self.assertFalse(self.pNet.has_panda(self.dora))
        self.assertTrue(self.pNet.has_panda(self.ivo))

    def test_make_friends(self):
        with self.assertRaises(PandasAlreadyFriends):
            self.pNet.make_friends(self.ivo, self.ana)

    def test_if_already_friends(self):
        self.assertFalse(self.pNet.are_friends(self.ivo, self.desi))

    def test_all_friends(self):
        self.assertEqual(len(self.pNet.friends_of(self.pesho)), 0)
        self.assertTrue(type(self.pNet.friends_of(self.desi)) == list)

    def test_connection(self):
        self.assertEqual(self.pNet.connection_level(self.ana, self.desi), 3)
        self.assertEqual(self.pNet.connection_level(self.ivo, self.rado), 1)
        self.assertFalse(self.pNet.connection_level(self.vyara, self.cveti))

    # def test_connected_pandas(self):
    #     pass

    # def test_how_many_genders(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
