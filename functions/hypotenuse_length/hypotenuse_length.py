# Sergii Logosha, 12.10.2022

# Program prompts user to input length of both catets of the triangle and
# calculates and prints out the length of the hypotenuse

from math import sqrt


def hypotenuse_length(catet_1, catet_2):
    hypo_len = sqrt((catet_1 ** 2) + (catet_2 ** 2))
    return hypo_len


catet_1_len = int(input("First catet length: "))
catet_2_len = int(input("Second catet length: "))
hypotenuse_len = round(hypotenuse_length(catet_1_len, catet_2_len), 1)
print(f"The length of the hypotenuse is {hypotenuse_len}.")
