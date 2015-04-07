#!/usr/bin/env python3
from re import match


class Panda:

    def __init__(self, name, mail_addr, gender):
        self.name = name
        self.gender = gender
        self.mail = self._email(mail_addr)

    def _email(self, address):
        pattern = "[\.\w]{2,}[@]\w+[.]\w+"
        if match(pattern, address):
            return address
        else:
            raise NotValidEmail

    def _gender(self):
        return self.gender

    def isFemale(self):
        if self.gender == 'female':
            return True

        return False

    def isMale(self):
        if self.gender == 'male':
            return True

        return False

    def __eq__(self, other):
        eq_names = self.name == other.name
        eq_email = self.mail == other.mail
        eq_gender = self.gender == other.gender
        return eq_names and eq_email and eq_gender

    def __str__(self):
        #return self.name + self.gender + self.mail
        return self.name

    def __hash__(self):
        return hash(self.__str__())

class NotValidEmail(Exception):
    pass
