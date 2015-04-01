#!/usr/bin/env python3
from panda import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def add_panda(self,new_member):

        if hash(new_member) in self.network:
            raise PandaAlreadyThere
        else:
            self.network[hash(new_member)] = []

    def has_panda(self, panda):

        if hash(panda) in self.network:
            return True
        else:
            return False

    def make_friends(self, panda1, panda2):

        member_A = hash(panda1)
        member_B = hash(panda2)
        network = self.network
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        else:
            network[member_A].append(member_B)
            network[member_B].append(member_A)


    def are_friends(self, panda1, panda2):
        member_A = hash(panda1)
        member_B = hash(panda2)
        network = self.network

        for key in network.keys():
            if key == member_A and member_B in network[key]:
                return False
            elif key == member_B and member_A in network[key]:
                return False
            else:
                return True

class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass
