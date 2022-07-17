# Sergii Logosha, 11 Jun 2022

# Program asks user to input the amount of purchased toys ang souvenirs and outputs message with total weight of the purchase

MASS_OF_TOY = 0.112
MASS_OF_SOUVENIR = 0.75

#Prompt user to input the amount of purchased toys
amount_toys = int(input("How many toys have you bought?\n"))

# Prompt user to input the amount of purchased souvenirs
amount_souvenirs = int(input("How many souvenirs have you bought?\n"))

# Calculating the weight of the purchase
total_weight = (amount_toys * MASS_OF_TOY) + (amount_souvenirs * MASS_OF_SOUVENIR)

# Printing out the final message
print("The total weight of the purchase is %.2f kg." % total_weight)