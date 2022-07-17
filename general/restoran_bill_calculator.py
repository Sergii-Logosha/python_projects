# Sergii Logosha, 11 Jun 2022

# Program asks user to input the bill from restoran and calculates taxes and tips


# Prompt user to input the bill from the restoran
bill = float(input("What is the bill? $"))

# Calculation of the taxes
tax_rate = float(input("What are taxes in your region? % "))
taxes = bill * (tax_rate / 100)

# Calculation of the tips
tip_percentage = float(input("What tips would you like to give? % "))
tips = bill * (tip_percentage / 100)

# Calculation of the total amount of money to be paid
total = bill + taxes + tips

# Printing out the final message
# print("The taxes for the bill are $%.2f" % taxes)
# print("The tips for the bill are $%.2f" % tips)
# print("The total amount to be paid is $%.2f" % total)

# The other way to print the final message:

print("The taxes for the bill are $%.2f, the tips are $%.2f, \
the total amount to be paid is $%.2f" % (taxes, tips, total))