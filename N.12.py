""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.12 """


string_in = input("Insert the string: ")
string_out = ""
vowels = "aeiouAEIOU"
for char in string_in:
    if char in vowels:
        string_out = string_out + char
    else:
        string_out = string_out + char + "o" + char
print(string_out)
