def reverse(stringToBeReversed):
    """
    reverse a string
    :param stringToBeReversed:
    :return: output
    """
    output = ""
    for c in stringToBeReversed:
        output = c + output
    return output.lower()


def is_palindrom(string_in):
    """
    Find if a word is palindrom
    :param string_in: 
    :return: 
    """
    if string_in.lower() == reverse(string_in.lower()):
        return True
    else:
        return False


# print(is_palindrom("onorarono"))

def is_palind_with_slice(string_in):
    if len(string_in) % 2 == 0:       # Se la stringa è lunghezza pari
        if string_in[0:((len(string_in))//2):1] == string_in[-(len(string_in))//2:]:
            return True
    elif len(string_in) % 2 != 0:     # Se la stringa è lunghezza dispari
        if string_in[0:((len(string_in)-1)//2):1] == string_in[-(len(string_in)+1)//2:]:
            return True
    else:
        return False


print(is_palind_with_slice("roberto"))
