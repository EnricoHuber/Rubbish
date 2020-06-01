import string


def e_counts(string):
    e_numbers = 0
    n_characters = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        if i in 'eE':
            e_numbers += 1
        if i in alphabet:
            n_characters += 1
    e_percentage = (e_numbers/n_characters)*100
    str_out = f"Your text contains {n_characters} alphabetic characters, of which {e_numbers} ({e_percentage:.2f}%) are 'e'"
    return str_out

string_in = """
Essere o non essere
"""
print(e_counts(string_in))
