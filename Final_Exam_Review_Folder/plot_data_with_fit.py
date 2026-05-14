__author__

import numpy as np
import matplotlib.pyplot as plt

def plot_data_with_fit(
    data: np.ndarray, 
    fit_curve: np.ndarray, 
    data_format: str = 'o', 
    fit_format: str = ''
):

   if data.shape[0] != 2 or fit_curve.shape[0] != 2:
        raise IndexError("Both input arrays must have shape (2, N)")

    p1 = plt.plot(data[0, :], data[1, :], data_format, label='Data')
    p2 = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format, label='Fit')
    combined_plot = p1 + p2
    
    return combined_plot

data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
x_fit = np.linspace(-2, 2, 100)
fit_curve = np.array([x_fit, x_fit**2])

plt.figure()
plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
plt.show()