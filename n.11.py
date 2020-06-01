import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 40)
y1 = 2*x
y2 = x**2
y3 = x**3

plt.plot(x, y1, "g-")
plt.plot(x, y2, "b.")
plt.plot(x, y3, "r^")
plt.show()
