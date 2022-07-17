# Sergii Logosha, 09 Jun 2022

# Program asks user the amount of bottles and calculates how much money user could get for those bottles

LITTLE_BOTTLES_PRICE = 0.10
BIG_BOTTLES_PRICE = 0.25

# Ask user how many little bottles it has
little_bottles = int(input("How many little bottles do you have? "))

# Ask user how many big bottles it has
big_bottles = int(input("How many big bottles do you have? "))

# Calculate the amount of money user can get for the bottles
little_bottles_cost = little_bottles * LITTLE_BOTTLES_PRICE
big_bottles_cost = big_bottles * BIG_BOTTLES_PRICE
total = round(little_bottles_cost + big_bottles_cost, 2)

# Printing the final message
print(f"The amount of money you can get for the bottles is $%.2f." % total)