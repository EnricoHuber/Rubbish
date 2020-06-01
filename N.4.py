""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.4 """


def infinite_sum(total, x):
    total += x
    return total


result = 0
while True:
    number = int(input("Insert the number (Shortcut to exit = -1): "))
    if number == -1:
        break
    result = infinite_sum(result, number)
print(f"The total is {result}")

