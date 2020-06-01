""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.21 """
import string


def encrypting(string_in):
    alphabet = list(string.ascii_lowercase)
    str_out = ""
    for char in string_in:
        if alphabet.index(char) >= (len(alphabet) - 13):
            str_out = str_out + alphabet[(13 - (len(alphabet) - alphabet.index(char)))]
        else:
            str_out = str_out + alphabet[alphabet.index(char) + 13]
    return str_out


def main():
    string_to_encrypte = input("Insert the string to encrypte: ")
    print(encrypting(string_to_encrypte))


if __name__ == '__main__':
    main()
