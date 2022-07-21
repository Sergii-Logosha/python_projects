# Sergii Logosha, 21 Jul 2022

# The program prompts user to input lengths of all three sides of the triangle
# and prints out the area of the triangle

import math

side_a = int(input("Side A length(mm): "))
side_b = int(input("Side B length(mm): "))
side_c = int(input("Side C length(mm): "))

s = (side_a + side_b + side_c) / 2

area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

print(f"The area of the triangle is equal {area:.2f} sq.mm")
