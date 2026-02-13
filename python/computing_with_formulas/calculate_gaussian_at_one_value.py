import numpy as np
from math import pi

mean_m = 0
standard_deviation_s = 2
input_value_x = 1

function_x = (1/((2*pi)*standard_deviation_s)**0.5)**((-1/2)*((input_value_x - mean_m)/standard_deviation_s)**2)

print(f'Mean:{mean_m}')
print(f'Standard Deviation:{standard_deviation_s}')
print(f'Input Value:{input_value_x}')
print(f'Result:{function_x}')