""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.16 """

import string
import random


def simple_password():
    char_available = string.ascii_letters + string.digits
    list_of_char = list(char_available)
    password = ""
    for i in range(8):
        password = password + list_of_char[random.randint(0, len(list_of_char) - 1)]
    return password


def complex_password():
    char_available = string.ascii_letters + string.digits + string.punctuation
    list_of_char = list(char_available)
    password = ""
    for i in range(20):
        password = password + list_of_char[random.randint(0, len(list_of_char) - 1)]
    return password


decision = int(input("Choose between a simple (type 0) or a complex (type 1) password: "))
if decision == 0:
    print(f"The password requested is {simple_password()}")

elif decision == 1:
    print(f"The password requested is {complex_password()}")

else:
    print("Not a valid input!")
