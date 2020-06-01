""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.17 """


def factorial(x):

    if x == 0:
        return 1
    else:
        for i in range(1, x):
            x = x * i
    return x


factorial_number = int(input("Insert a positive integer number: "))
print(factorial(factorial_number))
