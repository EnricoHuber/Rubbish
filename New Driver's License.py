my_name = input("")
n_agents = int(input(""))
people_names = input("")
list_of_names = people_names.split()
list_of_names.append(my_name)
list_of_names = [name.lower() for name in list_of_names]
list_of_names.sort()
time = 0
for i in range(len(list_of_names)+1//n_agents):
    if i != (len(list_of_names)+1//n_agents) - 1:
        if my_name in list_of_names[i*n_agents:(i*n_agents)+2]:
            time = (i+1) * 20
    else:
        if my_name in list_of_names[i*n_agents:]:
            time = (i+1) * 20
print(list_of_names)
print(time)
