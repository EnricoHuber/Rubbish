import matplotlib.pyplot as plt


x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]
plt.plot(x, y, color="red", linestyle="dashdot", marker="o", markerfacecolor="blue", ms=13)
plt.xlim(0, 8)
plt.xlabel("x-axis")
plt.ylim(1, 7)
plt.ylabel("y-axis")
plt.title("Display marker")
plt.show()
