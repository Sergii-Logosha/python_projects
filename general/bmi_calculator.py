# Sergii Logosha, 02 Jul 2022

# The program calculates the Body Mass Index and prints out the conditions to the User

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi <= 18:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 19 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
