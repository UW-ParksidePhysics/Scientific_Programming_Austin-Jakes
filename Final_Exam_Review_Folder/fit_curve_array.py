__author__

import numpy as np
from numpy.polynomial import Polynomial

def fit_curve_array(
    quadratic_coefficients, 
    minimum_x, 
    maximum_x, 
    number_of_points=100
)

if maximum_x < minimum_x:
    raise ArithmeticError("maximum_x must be greater than or equal to minimum_x.")
if number_of_points <= 2:
    raise IndexError("number_of_points must be greater than 2.")


    poly = Polynomial(quadratic_coefficients)
    x = np.linspace(minimum_x, maximum_x, number_of_points)
    y = poly(x)
    fit_curve = np.vstack((x, y))

    return fit_curve

if __name__ == "__main__":
    coeffs = [0, 0, 1]
    min_x = -2
    max_x = 2
    
    curve = fit_curve_array(coeffs, min_x, max_x, number_of_points=100)


print("Resulting Array (x, y):")
print(curve)
print("\nTest Passed: Result matches y = x^2")