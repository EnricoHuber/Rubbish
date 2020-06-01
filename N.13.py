""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.13 """


def is_in_list(x, list_to_check):
    if x in list_to_check:
        return True
    else:
        return False


list_in = [1, 13, 2, 5, 7, 8, 91, 12, 7, 54]
number = int(input("Insert the number you want to check (return True if the number is in list, False otherwise): "))
print(is_in_list(number, list_in))
