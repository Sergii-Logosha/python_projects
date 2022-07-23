# Sergii Logosha, 22 Jul 2022

# The program prompts user to input lengths of all the sides of the triangle
# and prints out the class of the triangle

side1_length = float(input("The length of the first side(mm): "))
side2_length = float(input("The length of the second side(mm): "))
side3_length = float(input("The length of the third side(mm): "))

if side1_length == side2_length == side3_length:
    print('The triangle is EQUILATERAL(рівносторонній).')
elif side1_length != side2_length == side3_length \
     or side2_length != side1_length == side3_length \
     or side3_length != side1_length == side2_length:
    print('The triangle is ISOSCELES(рівнобедрений).')
elif side1_length != side2_length != side3_length:
    print('The triangle is SCALENE(різносторонній).')
