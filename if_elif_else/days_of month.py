# Sergii Logosha, 19 Jul 2022

# The program prompts user to input name of the month and prints out the amount
# of the days in the month

month = input("The month name(January, February etc.): ").strip()

if month == "January" or month == "March" or month == "May" or month == "July"\
        or month == "August" or month == "October" or month == "December":
    print(f"{month} has 31 days.")
elif month == "February":
    print(f"{month} has either 28 or 29 days.")
elif month == "April" or month == "June" or month == "September" \
        or month == "November":
    print(f"{month} has 30 days.")
