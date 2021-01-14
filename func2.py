import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1)
y = x**2
plt.plot(x,y, 'r--o')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graphics of a function")
plt.grid()
plt.show()