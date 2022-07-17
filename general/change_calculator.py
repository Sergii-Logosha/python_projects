# Sergii Logosha, 17 Jun 2022

# Program asks user to input the amount of change the machine should give back and calculates
# how many different coins will be in the change

TWO_DOLLARS = 200
ONE_DOLLAR = 100
TWENTY_FIVE_CENTS = 25
TEN_CENTS = 10
FIVE_CENTS = 5

# Prompt user to type the amount of change in cents
change = float(input("The change that should be given back in cents: "))

# Calculating the number of two dollar coins and the reminder
two_dollar = int(change // TWO_DOLLARS)
change = change % TWO_DOLLARS
print("You should get:\n", two_dollar, '"two dollar" coins,')

# Calculating the number of one dollar coins and the reminder
one_dollar = int(change // ONE_DOLLAR)
change = change % ONE_DOLLAR
print("", one_dollar, '"one dollar" coins,')

# Calculating the number of 25 cents coins
twenty_five_cents = int(change // TWENTY_FIVE_CENTS)
change = change % TWENTY_FIVE_CENTS
print("", twenty_five_cents, '"twenty five cents" coins,')

# Calculating the number of 10 cents coins
ten_cents = int(change // TEN_CENTS)
change = change % TEN_CENTS
print("", ten_cents, '"ten cents" coins,')

# Calculating the number of 5 cents coins
five_cents = int(change // FIVE_CENTS)
change = change % FIVE_CENTS
print("", five_cents, '"five cents" coins,')

# Printing out the number of 1 cent coins
print("", int(change), '"one cent" coins.')



