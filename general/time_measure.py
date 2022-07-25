# Sergii Logosha, 25 Jul 2022

# The program prompts user to input time interval in days, hours, minutes,
# seconds and then calculates and prints out that interval in seconds

days = int(input("Type in days: "))
hours = int(input("Type in hours: "))
minutes = int(input("Type in minutes: "))
seconds = int(input("Type in seconds: "))

total_seconds = ((days * 86400) + (hours * 3600) + (minutes * 60) + seconds)

print(f"In seconds it will be: {total_seconds} seconds.")