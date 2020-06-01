""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.19 """

import string
import random


def genera_MAC():
    char_available_list = list(string.digits + string.ascii_uppercase)
    counter = 1
    password = ""
    while True:
        password = password + f"{char_available_list[random.randint(0, len(char_available_list) - 1)]}" + f"{char_available_list[random.randint(0, len(char_available_list) - 1)]}"
        if counter <= 5:
            password = password + ":"
        else:
            return password
        counter += 1


def main():
    print(genera_MAC())


if __name__ == '__main__':
    main()
