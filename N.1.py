""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.1 """

def max_of_numbers(x, y):
    """ Take two numbers as parameters and calculate the maximum between them """

    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "The numbers are equal"


first_number = int(input("Insert the first number: "))
second_number = int(input("Insert the second number: "))
print(max_of_numbers(first_number, second_number))
