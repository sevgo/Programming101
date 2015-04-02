#!/usr/bin/env python3
from panda import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def add_panda(self, new_member):

        if new_member in self.network:
            raise PandaAlreadyThere
        else:
            self.network[new_member] = []

    def has_panda(self, panda):

        if panda in self.network:
            return True
        else:
            return False

    def are_friends(self, panda1, panda2):
        network = self.network

        for key in network:
            panda1_n_panda2 = key == panda1 and panda2 in network[key]
            panda2_n_panda1 = key == panda2 and panda1 in network[key]

            if panda1_n_panda2 or panda2_n_panda1:
                return True
            else:
                return False

    def make_friends(self, panda1, panda2):

        network = self.network
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        else:
            network[panda1].append(panda2)
            network[panda2].append(panda1)

    def friends_of(self, member):
        if not self.has_panda(member):
            return False
        else:
            return self.network[member]


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


# if __name__ == '__main__':
#     ivo = Panda("Ivo","ivo@pandamail.com", "male")
#     drago = Panda("Drago", "drago@yahoo.com", "male")
#     ana = Panda("Anna", "ann@gmail.com","female")
#     desi = Panda("Desi", "desi@dir.bg", "female")
#     dido = Panda("Dido", "didko@mail.bg", "male")
#     rado = Panda("Radoslav", "radko@altavista.com", "male")
#     vyara = Panda("Vyara", "VyaraNadejdaLubov@mail.ru", "female")
#     pesho = Panda("Petar", "peshko@outlook.com", "male")

#     pandaland = PandaSocialNetwork()
#     pandaland.add_panda(ivo)
#     pandaland.add_panda(desi)
#     print(pandaland.are_friends(ivo, desi))
#     pandaland.make_friends(ivo, desi)
#     print(pandaland.are_friends(ivo, desi))
#     print(pandaland.network[ivo])
#     print(pandaland.network[desi])
#     pandaland.add_panda(drago)
#     pandaland.make_friends(desi, drago)
#     print(pandaland.are_friends(ivo, drago))
