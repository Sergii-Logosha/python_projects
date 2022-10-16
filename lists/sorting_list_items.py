# Sergii Logosha, 16.10.2022

# Program prompts user for the whole numbers, saves them to the list after that
# put the items to the order and prints them out

numbers = []
number = int(input("Enter a whole number (to finish enter 0): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter a whole number (to finish enter 0): "))
numbers.sort()
for number in numbers:
    print(number)
