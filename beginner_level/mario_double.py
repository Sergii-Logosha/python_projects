# Sergii Logosha, 24 Jun 2022

# Program asks user the hight of the pyramid in range from 1 to 10 and builds two pyramids:
# one right align and another left align with gap between them

hight = 1
while True:
    hight = int(input("Please, type in the height of the pyramid in range from 1 to 10: ").strip())

    if 0 < hight <= 10:
        i = 1
        while i <= hight:
            print(f" " * (hight - i), "#" * i, "#" * i)
            i += 1
