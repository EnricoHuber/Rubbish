""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.20 """


def rimario(word, list_of_words):
    flag = False
    for item in list_of_words:
        if word[len(word)-3:len(word)] == item[len(item)-3:len(item)]:
            print(f"{word} rhymes with {item}")
            flag = True
    if not flag:
        print("No rhymes found, sorry!")


def main():
    word_to_check = input("Insert the word you want to check: ")
    list_in = ["Abete", "Aratro",  "Ricetta", "Mantello", "Casa", "Riso", "Casta", "Pasta"]
    rimario(word_to_check, list_in)


if __name__ == '__main__':
    main()