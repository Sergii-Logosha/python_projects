# Sergii Logosha, 14 Jun 2022

# Program asks to input coordinates of two points on the surface of the Earth and calculates the shortest distance
# between these points

import math

# Prompt user to input the coordinates of the two points
t1 = float(input("What is the latitude of the first point?\n"))
g1 = float(input("What is the longitude of the first point?\n"))
t2 = float(input("What is the latitude of the second point?\n"))
g2 = float(input("What is the longitude of the second point?\n"))

# Calculating radians out of grad
t1_rad = math.radians(t1)
g1_rad = math.radians(g1)
t2_rad = math.radians(t2)
g2_rad = math.radians(g2)

# Calculating the distance between two points
distance = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))
print("The distance between the points you`ve entered is %.2f km." % distance)