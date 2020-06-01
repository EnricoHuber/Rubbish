import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10)
y = x*7

plt.plot(x, y)
plt.title("Draw a line.")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
print(plt.axis())
plt.axis([0, 20, 0, 80])
plt.show()
