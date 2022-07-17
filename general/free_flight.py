# Sergii Logosha, 08 Jul 2022

# The program calculates the speed of the object that is falling to the Earth at the ground level

G = 9.8
V0 = 0

import math

height = float(input("Height the object was lifted up to (m): "))

speed = math.sqrt((V0 ** 2) + (2 * G * height))

print(f"The object thrown from {height} meters, will gain speed {speed:.2f} m/s at ground level.")
