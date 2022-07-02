# Sergii Logosha, 16 Jun 2022

# Program prompts user to type in a number and then prints out is this number even or odd

# Prompt user to input a whole number
number = int(input("Type in a whole number: "))

# Making calculations
if number % 2 == 0:
    print("The", number, "is an even number.")
else:
    print("The", number, "is an odd number.")
