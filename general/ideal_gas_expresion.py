# Sergii Logosha, 17 Jul 2022

# The program calculates the amount of the ideal gas

R = 8.314

temperature = float(input("Temperature (C): ").strip())
volume = float(input("Volume (L): ").strip())
pressure = float(input("Pressure (P): ").strip())

temperature_kelvin = temperature + 273.15

gas_amount = (pressure * volume) / (R * temperature_kelvin)

print(f"Gas amount is equal {gas_amount:.2f} moles.")
