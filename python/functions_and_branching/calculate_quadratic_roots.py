from numpy.lib.scimath import sqrt

def calculate_quadratic_roots(a, b, c):
    delta = (b**2) - (4*a*c)
    root1 = (-b - sqrt(delta)) / (2*a)
    root2 = (-b + sqrt(delta)) / (2*a)

    return (root1, root2)


roots_complex = calculate_quadratic_roots(1, 2, 5)
print(f"roots of x^2 + 2x + 5 = 0: {roots_complex}")

roots_real = calculate_quadratic_roots(1, -3, 2)
print(f"roots of x^2 - 3x + 2 = 0: {roots_real}")

roots_equal = calculate_quadratic_roots(1, -4, 4)
print(f"roots of x^2 - 4x + 4 = 0: {roots_equal}")