# Sergii Logosha, 12 Jun 2022

# Program prompts user to input two whole numbers, makes basic arythmetic and outputs thr results

import math

# Prompt user to input two whole numbers
first_number = int(input("Please, enter the first whole number\n"))
second_number = int(input("Please, enter the second whole number\n"))

# Make basic arithmetic operations and print out the results
print("The results of basic arithmetic operations with", first_number, "and", second_number, "are:")
addition = first_number + second_number
print(first_number, "+", second_number, "=", addition)
subtraction = first_number - second_number
print(first_number, "-", second_number, "=", subtraction)
multiplication = first_number * second_number
print(first_number, "*", second_number, "=", multiplication)
division = first_number / second_number
print(first_number, "/", second_number, "=", division)
floor_division = first_number // second_number
print(first_number, "//", second_number, "=", floor_division)
modulo_result = first_number % second_number
print(first_number, "%", second_number, "=", modulo_result)
log_base_10_1 = math.log10(first_number)
print("log10(", first_number, ")", "=", log_base_10_1)
log_base_10_2 = math.log10(second_number)
print("log10(", second_number, ")", "=", log_base_10_2)
power_to = first_number ** second_number
print(first_number, "**", second_number, "=", power_to)