""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.11 """


def search_max(list_in):
    max_n = list_in[0]
    i = 0
    while i < len(list_in):
        if list_in[i] > max_n:
            max_n = list_in[i]
        i += 1
    return max_n


list_numbers = [11, 1379, 51, 218, 81, -597979, 7179]
print(search_max(list_numbers))
