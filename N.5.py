""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.5 """


def infinite_multiplication(total, x):
    total = total * x
    return total


result = 1 #for moltiplication, initialize it at the value 1
while True:
    number = int(input("Insert the number (-1 to exit): "))
    if number == -1:
        break
    result = infinite_multiplication(result, number)
print(f"The total is {result}")

