# Sergii Logosha, 23 Jun 2022

# The program asks user for the height in feet and inches and converts it into centimeters

INCHES_PER_FOOT = 12
CENTIMETERS_PER_INCH = 2.54

# Get from user their height in feet and inches
height_feet = int(input("How many feet are in your height?\n").strip())
height_inches = int(input("How many inches are in your height?\n").strip())

# Converting height in feet to inches
height = height_feet * INCHES_PER_FOOT

# Calculating the height in centimeters
height_cent = height * CENTIMETERS_PER_INCH

# Printing out the results
print(f"Your height in centimeters is {height_cent}.")
