myList1 = []
items_to_append = [76, 93.3, "hello", True, 4, 76]
for i in range(len(items_to_append)):
    myList1 = myList1 + [items_to_append[i]]
myList1.append("apple", 76)
print(myList1)

myList1.insert("cat", 3)
print(myList1)
# myList1[3:3] = "cat"
