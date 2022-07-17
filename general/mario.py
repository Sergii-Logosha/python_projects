# Sergii Logosha, 24 Jun 2022

# The program prompts user to input a whole number from 1 to 10 and builds right align pyramid using # symbols

hight = 1
while True:
    hight = int(input("Set the hight of the pyramid in range from 1 to 10: ").strip())

    if 0 < hight <= 10:
        i = 1
        while i <= hight:
            print(f" " * (hight - i), "#" * i)
            i += 1
