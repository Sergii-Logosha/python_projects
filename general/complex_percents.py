# Sergii Logosha, 12 Jun 2022

# Program asks user to input an amount of the deposit and prints out the amount of money on the deposit
# after first, second and third year

DEPOSIT_RATE = 0.04

# Prompt user to input the deposit amount
deposit_amount = float(input("What is the original deposit amount?\n$"))

# Calculating the amount of money on the deposit after the first year
deposit_percents = deposit_amount * DEPOSIT_RATE
deposit_1_year = deposit_amount + deposit_percents

# Calculating the amount of money on the deposit after second and third year
deposit_percents_2_year = deposit_1_year * DEPOSIT_RATE
deposit_2_year = deposit_1_year + deposit_percents_2_year
deposit_percents_3_year = deposit_2_year * DEPOSIT_RATE
deposit_3_year = deposit_2_year + deposit_percents_3_year

# Printing out the final message
print("If the client deposit $%.2f, after the firs year it will grow up to $%.2f, after the second year, up to $%.2f, \
after the third year? up to $%.2f." % (deposit_amount, deposit_1_year, deposit_2_year, deposit_3_year))