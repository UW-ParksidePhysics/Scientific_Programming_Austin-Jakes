"""
Converting between temperature scales
Types:
    Celsuis
    Kelvin
    Fahrenheit

Functions:
    celsius_to_fahrenheit: C = (5/9)*(F - 32)
    fahrenheit_to_celsius: F = (9/5)*C + 32
    celsius_to_kelvin: C = K - 273.15
    kelvin_to_celsius:  K = C + 273.15
    fahrenheit_to_kelvin: F = 9/5*(K - 273.15) + 32
    kelvin_to_fahrenheit: K = 5/9*(F - 32) + 273.15

"""

def celsius_to_fahrenheit(fahrenheit_temperature):
    return 5/9*(fahrenheit_temperature - 32)


def fahrenheit_to_celsius(celsius_temperature):
    return 9/5*celsius_temperature + 32


def celsius_to_kelvin(celsius_temperature):
    return celsius_temperature + 273.15


def kelvin_to_celsius(kelvin_temperature):
    return kelvin_temperature - 273.15


def fahrenheit_to_kelvin(kelvin_temperature):
    return 9/5*(kelvin_temperature - 273.15) + 32


def kelvin_to_fahrenheit(fahrenheit_temperature):
    return 5/9*(fahrenheit_temperature - 32) + 273.15


def test_conversion():
    test_fahrenheit = 212
    test_fahrenheit_output = celsius_to_fahrenheit(fahrenheit_to_celsius(test_fahrenheit))

    print (f'{test_fahrenheit_output} F = F(C({test_fahrenheit} F))')

if __name__ == "__main__":
    test_conversion()
