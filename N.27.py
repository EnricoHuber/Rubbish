""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.27 """


library = {
    "La paranza dei bambini": 10,
    "Cent'anni di solitudine": 13,
    "Cinquanta sfumature di nero": 7,
    "Orgoglio e pregiudizio": 2
}

print(library.items())
book_title = input("Choose a book title: ")
if book_title not in library:
    print("We don't have that book, sorry.")
else:
    library[book_title] -= 1
print(library.items())