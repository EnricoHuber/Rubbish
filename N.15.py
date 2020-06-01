prove_string = input("Insert a string: > ")
string_as_list = prove_string.split()
string_final = ""
string_output = []
counter = len(string_as_list)
i = 0
max_elements = counter-1
while counter > 0:
    string_output.insert(i, string_as_list[counter-1])
    string_final = string_final + f"{string_output[i]} "
    i += 1
    counter -= 1
print(string_final)
