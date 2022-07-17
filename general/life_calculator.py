# Author: Sergii Logosha
# Date Created: 29.05.2022
# Last Modified: 29.05.2022

# Description 
# Program calculates how many days, weeks, months left to live if the person would live to 90 years.

# Usage
# 

age = input("What is your current age?")
age = int(age)
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")