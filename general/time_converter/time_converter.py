# Sergii Logosha, 31 Jul 2022

# Program prompts user to input some period of time in seconds and converts
# it to the format DD:HH:MM:SS

time_seconds = int(input("Time interval(sec): ").strip())

days = time_seconds // 86400
remainder = time_seconds % 86400
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
remainder = remainder % 60
seconds = remainder

print(f'That is: {days:d}:{hours:02d}:{minutes:02d}:{seconds:02d} (DD:HH:MM:SS)')
