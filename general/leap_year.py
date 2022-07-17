# Sergii Logosha, 02 Jul 2022

# The program prompts user to input any desired year and calculates if it is a leap year
# The rules to distinguish a leap year:
# 1. Every year that is evenly divisible by 4
# 2. EXCEPT every year that is evenly divisible by 100
# 3. UNLESS the year is also evenly divisible by 400

year = int(input("Which year do you want to check? ").strip())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
