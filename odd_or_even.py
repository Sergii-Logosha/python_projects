# Sergii Logosha, 27 Jun 2022

# The program prompts user to insert a whole number and returns an answer is the number even or odd

number = int(input("Type in a whole number, please: ").strip())

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print("The number {} is odd.".format(number))
