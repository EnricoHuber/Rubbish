import matplotlib.pyplot as plt


x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]
plt.plot(x, y1, label="line1")
plt.plot(x, y2, label="line2")
plt.title("Two or more lines plot with suitable legends")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
