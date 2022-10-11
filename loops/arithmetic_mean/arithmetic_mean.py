# Sergii Logosha, 11.10.2022

# Program prompts user to input numbers and calculates arithmetic mean of those
# numbers. 0 is exit character.

number = int(input("Number: "))
total = 0
i = 1
while number != 0:
    total = total + number
    arythmetic_mean = round(total / i)
    print(f"Arythmetic mean of given number(s) is {arythmetic_mean}")
    i += 1
    number = int(input("Number: "))
print("0 is an exit character.")