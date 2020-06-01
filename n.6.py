import matplotlib.pyplot as plt


x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]
plt.plot(x, y1, color="blue", label="line1-width-3", linewidth=3)
plt.plot(x, y2, color="red", label="line2-width-5", linewidth=5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two or more lines with different widths and colors with suitable legends")
plt.legend()
plt.show()
