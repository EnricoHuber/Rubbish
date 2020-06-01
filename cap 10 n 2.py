myList1 = []
items_to_append = [76, 93.3, "hello", True, 4, 76]
for i in range(len(items_to_append)):
    myList1 = myList1 + [items_to_append[i]]
print(myList1)

myList2 = []
for i in range(len(items_to_append)):
    myList2.append(items_to_append[i])
print(myList2)
