def reverse(string_to_be_reversed):
    string_out = ''
    for char in string_to_be_reversed:
        string_out = char + string_out
    return string_out


print(reverse("ciao bella come va"))
