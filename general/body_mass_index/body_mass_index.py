# Sergii Logosha, 05.10.2022

# Program calculates BMI fof metric units and for imperial units

units = input('Choose measure units - "metric" or "imperial": ')
weight = int(input("Your weight: "))
height = float(input("Your height: "))

if units == "metric":
    bmi = round(weight / (height ** 2))
    print(f"Your BMI is {bmi}.")
elif units == "imperial":
    bmi = round((weight / (height ** 2)) * 703)
    print (f"Your BMI is {bmi}.")
else:
    print("Choose proper units")

