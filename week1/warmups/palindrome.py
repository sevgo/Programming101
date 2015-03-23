def palindrome(obj):                                                            
    return obj == obj[::-1]

if __name__ == "__main__": 
    print (palindrome("\"abba_abba"))
