def is_in_string(string_in, substring):
    """
    Is your substring in your string?
    :param string_in:
    :param substring:
    :return:
    """

    i, j = 0, 0
    while i <= len(string_in):
        if j <= len(substring) and j == i:
            if i == j:
                j += 1
        else:
            return True
        i += 1
    else:
        return False


print(is_in_string("Casabella", "Casa"))
