""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.18 """


def fibonacci(x):
    list_out = [1, 1]
    i = 2
    while True:
        number = list_out[i-1] + list_out[i-2]
        if x == 0:
            return 0
        elif x < 0:
            return "Not a valid input!"
        elif number > x:
            return list_out
        else:
            list_out.append(number)
        i += 1


threshold = int(input("Set the threshold (integer positive number) for your Fibonacci series: "))
print(fibonacci(threshold))
