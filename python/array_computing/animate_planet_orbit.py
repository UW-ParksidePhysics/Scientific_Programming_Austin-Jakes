import matplotlib.pyplot as plt
import numpy as np
from math import pi

angular_velocity = 5
time = np.array([1,2,3,4,5,6,7,8,9,10])

semi_major_a = 50
semi_minor_b =100

x_position = semi_major_a*np.cos(angular_velocity*time)
y_position = semi_minor_b*np.sin(angular_velocity*time)

velocity_vector = np.array([-angular_velocity*semi_major_a*np.sin(angular_velocity*time),
                            angular_velocity*semi_minor_b*np.cos(angular_velocity*time)
                            ])
vector_magnitude = angular_velocity*((semi_major_a)*np.sin(angular_velocity*time)*(semi_minor_b**2)*np.cos(angular_velocity*time))**.5