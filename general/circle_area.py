# Sergii Logosha, 26 Jun 2022

# Program prompts user to input the radius and calculates the area of the circle and the volume of the sphere

import math

# Prompt user to insert the radius
r = float(input("Type in the radius, please (mm): "))

# Calculating and printing out the area of the circle
area = round(math.pi * r ** 2, 2)
print(f"The area of the circle is {area} mm2.")

# Calculating the volume of the sphere
volume = round((4 / 3) * math.pi * r ** 3, 2)
print("The volume of the sphere is {} mm3.".format(volume))

