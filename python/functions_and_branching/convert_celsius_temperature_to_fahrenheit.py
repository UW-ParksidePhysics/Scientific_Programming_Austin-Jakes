def fahrenheit_temperature(celsius_temperature):
    fahrenheit_value = 9.0 / 5.0 * celsius_temperature + 32.0
    return fahrenheit_value


print(f'C|F')

celsius_temperatures = [0,21,100] #Freezing point water, 21 degrees celcius, boiling point water  

for celsius_temperature in celsius_temperatures:
        print(
        f"{celsius_temperature:5.1f} "
        f"{fahrenheit_temperature(celsius_temperature):.1f}"
    )