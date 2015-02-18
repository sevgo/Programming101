# Task3: Caesar cipher
#

U = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def find_char(char, secret, lst):
    """Takes a character from given string,
    shifts it secret times and return the
    character from lst depending on case of
    the taken character."""


    pos = lst.index(char)
    offset = (pos + secret) % 26
    ch = lst[offset]
    return ch


def caesar_encrypt(str, n):
    """Method that takes a string, encrypt it
    char by char and returns encrypted string"""


    encrypted_msg = ""
    for element in str:
        if element in U:
            char = find_char(element, n, U)
        elif element in l:
            char = find_char(element, n, l)
        else:
            char = element

        encrypted_msg += char

    return encrypted_msg


if __name__ == "__main__":
    print (caesar_encrypt("Hello World!",2))
