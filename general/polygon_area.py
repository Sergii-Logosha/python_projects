# Sergii Logosha, 23 Jul 2022

# The program prompts user to type in the number of sides and their length
# and prints out the area of the polygon

import math

PI = 3.14

sides_number = int(input("Number of sides: ").strip())
sides_length = int(input("Length of sides(mm): ").strip())

area = (sides_number * (sides_length ** 2)) / (4 * math.tan(PI / sides_number))
print(f'The area of the polygon with {sides_number} sides is equal to '
      f'{area:.2f} sq.mm.')
