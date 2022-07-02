# Author: Sergii Logosha
# Date Created: 29.05.2022
# Last Modified: 29.05.2022

# Description 
# Program calculates amount of money everyone from the group should pay including tips.

# Usage
# 

# printing out the welcome message
print("Welcome to the tip calculator.\n")

# prompting user to insert the total amount that was paid without tips
total = input("What was the total bill? $")

# changing the type of the variable total to float
total = float(total)

# prompting the user to insert the procentage of the tips
percent_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

# changing the type of the variable percent_tip to float
percent_tip = float(percent_tip)

# prompting the user to insert the amount of people the total amount should be splited beetwin
people = input("How many people to split the bill? ")

# changing the type of the variable people to float
people = float(people)

# calculations of the amount of tips
tip_percentage = percent_tip / 100
tip = total * tip_percentage

# calculating the total amount of the bill with tips
grand_total = total + tip

# calculating the amount each person should pay
amount_to_pay = grand_total / people
amount_to_pay = round(amount_to_pay, 2)
amount_to_pay = "{:.2f}".format(amount_to_pay)
print(f"Each person should pay: ${amount_to_pay}")