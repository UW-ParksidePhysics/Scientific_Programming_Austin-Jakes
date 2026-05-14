__author__

describe(a, axis=0, ddof=1, bias=True, nan_policy='propagate')

import numpy as np
from scipy import stats

def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
     if data.shape[0] != 2 or data.shape[1] < 2:
        raise IndexError("Data must be a 2xM array with M >= 2")

    x = data[0, :]
    y = data[1, :]

    y_desc = stats.describe(y)
    std_y = np.sqrt(y_desc.variance)

return np.array([
    y_desc.mean,
    std_y,
    np.min(x),
    np.max(x),
    np.min(y),
    np.max(y)
])

def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:

       if data.shape[0] != 2 or data.shape[1] < 3:
        raise IndexError("Data must be a 2xM array with M >= 3 for quadratic fit")
        
    x = data[0, :]
    y = data[1, :]

    return np.polynomial.polyfit(x, y, 2)


if __name__ == "__main__":

    x_test = np.linspace(-10, 10, 100)
    y_test = x_test**2
    data_test = np.vstack((x_test, y_test))

    stats_result = calculate_bivariate_statistics(data_test)
    print("Stats [MeanY, StdY, MinX, MaxX, MinY, MaxY]:\n", stats_result)

    coeffs = calculate_quadratic_fit(data_test)
    print("\nQuadratic Fit Coefficients (c + bx + ax^2):\n", coeffs)                