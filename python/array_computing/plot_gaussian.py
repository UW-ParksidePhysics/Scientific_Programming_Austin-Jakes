import matplotlib.pyplot as plt
import numpy as np

from math import pi


positions = np.linspace(-4,4,41)

gaussian_values = (1/(2*pi)**5)*np.exp(-.5*(positions**2))

plt.plot(positions, gaussian_values, color = 'green')
plt.axvline(color='black')
plt.axhline(color='black')

plt.show()

print('Positions = ', positions.tolist())
print('gaussian_values = ', gaussian_values.tolist())