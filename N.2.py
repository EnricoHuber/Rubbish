""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.2 """


def max_of_three_numbers(x, y, z):
    """ Takes 3 numbers and outputs the biggest one"""

    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return "The three numbers are equal"


first = int(input("Insert the first number: "))
second = int(input("Insert the second number: "))
third = int(input("Insert the third number: "))
print(max_of_three_numbers(first, second, third))
