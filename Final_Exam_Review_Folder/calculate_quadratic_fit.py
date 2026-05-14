__author__

import numpy as np

def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:
    if data.shape[0] != 2 or data.shape[1] < 3:
        raise IndexError("Data must be shape (2, M) with M >= 3")

    x = data[0, :]
    y = data[1, :]

    coeffs = np.polyfit(x, y, 2)
    return np.array([coeffs[2], coeffs[1], coeffs[0]])

if __name__ == "__main__":
    x_test = np.linspace(-1, 1, 50)
    y_test = x_test**2  # y = 0 + 0x + 1x^2
    test_data = np.vstack((x_test, y_test))

    try:
        coefficients = calculate_quadratic_fit(test_data)
        print("Quadratic Coefficients [constant, linear, quadratic]:")
        print(np.round(coefficients, 10))
    except IndexError as e:
        print(e)
