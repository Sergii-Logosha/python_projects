# Sergii Logosha, 09 Jun 2022

# Program prompts user to insert dimentions of the garden in feet and calculates area in acres

SQ_FEET_PER_ACRE = 43560

# prompt user to insert the length of the garden
length = float(input("What is the length of the garden (in feet)? "))

# Prompt user to insert the width of the garden
width = float(input("What is the width of the garden (in feet)? "))

# Calculatig the area of the garden
area = round(length * width / SQ_FEET_PER_ACRE, 2)

# Displaying the area in acres
print(f"The area of the garden is ", area, "acres.")