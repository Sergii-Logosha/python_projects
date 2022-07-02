# Sergii Logosha, 23 Jun 2022

# The program asks user to input some distance in feet and converts it into inches, yards and miles

INCHES_PER_FOOT = 12
FEET_PER_YARD = 3
FEET_PER_MILE = 5280

# Getting the distance in feet from user
distance_feet = float(input("What is the distance in feet?\n").strip())

# Calculating and printing out the distance in inches
distance_inches = distance_feet * INCHES_PER_FOOT
print(f"It will be {distance_inches:.2f} inches.")

# Calculating and printing out the distance in yards
distance_yards = distance_feet / FEET_PER_YARD
print("Or it will be {:.2f} yards".format(distance_yards))

# Calculating and printing out the distance in miles
distance_miles = distance_feet / FEET_PER_MILE
print(f"In miles it will be {distance_miles:.2f}.")
