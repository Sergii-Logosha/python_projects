# Author: Sergii Logosha
# Date Created: 29.05.2022
# Last Modified: 29.05.2022

# Description 
# Program calculates the BMI index for given height and weight.

# Usage
# 

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height = float(height)
weight = float(weight)
bmi = weight / (height ** 2)
bmi = int(bmi)
print(bmi)