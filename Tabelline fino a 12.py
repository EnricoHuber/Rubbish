size = int(input("Choose the size of your table: ")) + 1
for i in range(1, size):
    for j in range(1, size):
        print(i*j, end = '\t')
    print('\n')




