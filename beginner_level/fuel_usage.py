# Sergii Logosha, 13 Jun 2022

# Program asks user how much fuel the car takes in MPG and calculates how much it is in L/100 km.

KM_IN_MILE = 1.60934
LITERS_IN_GALON = 3.78541

# Prompt user to insert fuel usage in miles per galon
mpg = float(input("What is the fuel consumption in miles per galon (MPG)?\n"))

# Calculating kilometers per liter
km_per_lit = (mpg * KM_IN_MILE) / LITERS_IN_GALON

# Calculating liters per 100 kilometers
lit_per_100_km = 100 / km_per_lit
print(mpg, "miles per galon (MPG) is equal to %.2f" % lit_per_100_km, "liters per 100 kilometers.")