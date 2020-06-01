""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.6 """


def string_reverser(str_to_reverse):
    str_reversed = ""
    for char in str_to_reverse:
        str_reversed = char + str_reversed
    return str_reversed


string_in = input("Insert the string you want to reverse: ")
print(string_reverser(string_in))
