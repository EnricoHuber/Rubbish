import matplotlib.pyplot as plt


x1 = [2, 3, 5, 6, 8]
# Make an array of y values for each x value
y1 = [1, 5, 10, 18, 20]
# Make an array of x values
x2 = [3, 4, 6, 7, 9]
# Make an array of y values for each x value
y2 = [2, 6, 11, 20, 22]
# set new axes limits
plt.axis([0, 10, 0, 30])
plt.plot(x1, y1, "b*")
plt.plot(x2, y2, "ro")
plt.show()
