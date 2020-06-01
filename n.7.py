import matplotlib.pyplot as plt


x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]

plt.plot(x, y1, linestyle="dotted", color="lightblue", linewidth=3, label="line1-dotted")
plt.plot(x, y2, linestyle="dashed", color="red", linewidth=5, label="line1-dashed")
plt.title("Plot with two or more lines with different styles")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
