# Sergii Logosha, 11 Jun 2022

# Program calculstes the sum of first n numbers

# Prompt user to input some whole number
number = int(input("Type in any whole number\n"))

# Calculating the sum of the first n numbers
sum_of_numbers = int((number * (number + 1)) / 2)

# Printing out the final message
print("The sum of numbers from 1 to", number, "is", sum_of_numbers, ".")