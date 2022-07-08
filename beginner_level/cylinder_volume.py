# Sergii Logosha, 08 Jul 2022

# Program calculates the volume of a cylinder

PI = 3.14159265359

radius = float(input("Cylinder base radius (mm): ").strip())
height = float(input("Cylinder height (mm): ").strip())

volume = (PI * (radius ** 2)) * height

print(f"The volume of the cylinder is {volume:.1f} mm3.")
