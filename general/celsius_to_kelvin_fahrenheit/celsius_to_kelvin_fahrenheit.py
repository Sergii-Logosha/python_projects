# Sergii Logosha, 15.11.2022

# User inputs temperature in Celsius and program outputs it in Kelvin and
# Fahrenheit
TEMP_COEFFICIENT = 273.15

temp_celsius = float(input("Temperature(Celsius): "))

temp_kelvin = temp_celsius + TEMP_COEFFICIENT
print(f"Temperature(Kelvin): {temp_kelvin:.1f}")

temp_fahrenheit = (temp_celsius * (9 / 5)) + 32
print(f"Temperature(Fahrenheit): {temp_fahrenheit:.1f}")
