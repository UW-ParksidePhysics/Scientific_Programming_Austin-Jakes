import matplotlib.pyplot as plt
import numpy as np
from math import pi

gravity = 9.81
depth_h = 50 #meters

#temp 20 Celcius

pure_water = 7.2*10**-2 #Newton/meter
sea_water = 6.5*10**-2 #Newton/meter
s_air_surface_tension = np.array([pure_water, sea_water])

pure_density = 988 #kg/meter^3
sea_density = 1025 #kg/meter^3
p_density = np.array([pure_density, sea_density])



number_of_lambda = 2
small_start_lambda, small_stop_lambda, large_start_lambda, large_stop_lambda = 0.001, 0.1, 1, 2
lambda_x_values = np.linspace(small_start_lambda,small_stop_lambda,number_of_lambda)
lambda_y_values = ((gravity*lambda_x_values/2*pi)*(1 + s_air_surface_tension*(4*pi**2/p_density*gravity*lambda_x_values)*np.tanh(2*pi*depth_h/lambda_x_values)))**.5


plt.plot(lambda_x_values,lambda_y_values, color = 'red')

plt.xlim((large_start_lambda, large_stop_lambda))
plt.ylim((large_start_lambda, large_stop_lambda))

plt.axvline(color='black')
plt.axhline(color='black')

plt.show()

