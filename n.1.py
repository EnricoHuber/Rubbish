from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(1, 20, 40)
y = x*3


plt.plot(x, y)
plt.xlabel('x-axis')
plt.xlabel('y-axis')
plt.title("Draw a line.")
plt.show()
