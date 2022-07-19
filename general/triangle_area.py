# Sergii Logosha, 19 Jul 2022

# The program prompts user to input the base and the hight of the triangle and
# prints out the area of the triangle

base = float(input("The triangle base(mm): ").strip())
height = float(input("The triangle height(mm): ").strip())

area = (base * height) / 2

print(f"The area of the triangle is {area:.2f} sq.mm.")

