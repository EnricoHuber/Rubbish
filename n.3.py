import matplotlib.pyplot as plt


f = open(r"C:\Users\Enrico\Desktop\Data.txt", "r")
x_values = []
y_values = []
flag = True         # it helps to append one values per list
for line in f:
    for data in line.split():
        if flag:
            x_values.append(int(data))
            flag = False
        else:
            y_values.append(int(data))
            flag = True

print(x_values)
print(y_values)

plt.plot(x_values, y_values)
plt.title("Sample graph!")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
