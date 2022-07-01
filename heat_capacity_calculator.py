# Sergii Logosha,01 Jul 2022

# The program asks user to input mass of the water and the difference between the starting temperature
# and the temperature at the end. Program calculates the amount of energy needed to heat up or cool down
# that amount of water. The program also calculates the cost of heating up the water.

WATER_HEAT_CAPACITY = 4.186
KWH_TO_JOULE = 0.000000277777778
ELECTRICITY_COST = 8.9

water_mass = int(input("Mass of the pattern of water (grams): ").strip())
start_temp = float(input("Temperature at the beginning (C): ").strip())
finish_temp = float(input("Temperature at the end (C): ").strip())
temp_difference = finish_temp - start_temp

energy_amount = water_mass * WATER_HEAT_CAPACITY * temp_difference

if temp_difference > 0:
    print(f"The amount of energy needed to heat up {water_mass} gram of water from {start_temp}C to {finish_temp}C "
          f"is {energy_amount:.2f} Joules.")
    cost = ((KWH_TO_JOULE * energy_amount) * ELECTRICITY_COST) / 100
    print(f"It will cost ${cost:.2f} spent on electricity.")

elif temp_difference == 0:
    print("The temperature of the water hasn't changed.")

else:
    energy_amount = abs(energy_amount)
    print(f"The amount of energy needed to cool down {water_mass} gram of water from {start_temp}C to {finish_temp}C "
          f"is {energy_amount:.2f} Joules.")


