# Task3: Caesar cipher
#

def caesar_encrypt(str, n):
    encrypted_msg = ""
    for el in str:
        num = ord(el)
        offset = num + el
        if offset > 122:
            offset = offset % 122
        elif offset > 90:
            offset = offset % 90 
        print ("encrypted: %s" % encrypted_msg)
        encrypted_msg += chr(offset)

    return encrypted_msg


if __name__ == "__main__":
    print (caesar_encrypt("Zbcz",2))
