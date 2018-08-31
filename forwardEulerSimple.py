# Use forward Euler to solve the equation dy/dt = y - b

import numpy as np

import matplotlib.pyplot as plt

# Set variables
y0 = 100  # Initial condition
b = 20  # Constant
h = 0.01  # Step size


y = np.array([y0])
ts = np.array([0])
# Forward Euler
t = h
count = 1
while t <= 2:
    y = np.append(y, y[count-1] + h*(y[count-1] - b))
    ts = np.append(ts, t)
    count += 1
    t += h

plt.plot(ts, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Forward Euler on dy/dt = y - b')
plt.show()







