# Sergii Logosha, 10.10.2022

# The program asks user to input temperature and wind speed and then
# displays how the temperature feels considering wind

print("Best of all to do calculations for the temperature lower then "
      "10 degrees Celsius and wind speed higher then 4.8 km/h")

temperature = float(input("Temperature (C): "))
wind_speed = float(input("Wind speed (km/h): "))

wci = round(13.12 + (0.6215 * temperature) - (11.37 * (wind_speed ** 0.16)) + \
      (0.3965 * temperature * (wind_speed ** 0.16)), 1)

print(f"{temperature}C would feel like {wci}C, with wind speed of {wind_speed}"
      f"km/h.")