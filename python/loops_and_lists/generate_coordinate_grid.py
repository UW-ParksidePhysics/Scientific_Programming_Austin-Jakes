import numpy as np

starting_value = 1
interval_len_h = 0.050
intervals = 2 + interval_len_h


x_coordinates = np.arange(starting_value,intervals,interval_len_h)

print(f'x = {x_coordinates}')

a,b,n = starting_value,intervals,interval_len_h

h = (b - a)/n

x_coordinate = np.arange(a,b,n)

print(f'{x_coordinate}')