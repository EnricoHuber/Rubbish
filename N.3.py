""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.3 """


def is_a_vowel(x):
    """ Finds out if a character is a vowel """
    x = x.lower()
    vocals = "aeiou"
    if x in vocals:
        return True
    else:
        return False


character = input("Insert the character (returns 'True' if it is a vowel, 'False' otherwise): ")
print(is_a_vowel(character))
