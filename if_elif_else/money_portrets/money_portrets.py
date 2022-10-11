# Sergii Logosha, 11.10.2022

# Program prompts user to input the value of the note and prints out the person
# whose portret is placed on the note

ONE_DOLLAR = "Джордж Вашингтон"
TWO_DOLLARS = "Томас Джеферсон"
FIVE_DOLLARS = "Авраам Лінкольн"
TEN_DOLLARS = "Олександр Гамільтон"
TWENTY_DOLLARS = "Ендрю Джексон"
FIFTY_DOLLARS = "Уліс Грант"
ONE_HUNDRED_DOLLARS = "Бенджамін Франклін"

note_value = input("Номінал банкноти, $")
if note_value == "1":
    print(f"На банкноті ${note_value} зображений {ONE_DOLLAR}.")
elif note_value == "2":
    print(f"На банкноті ${note_value} зображений {TWO_DOLLARS}.")
elif note_value == "5":
    print(f"На банкноті ${note_value} зображений {FIVE_DOLLARS}.")
elif note_value == "10":
    print(f"На банкноті ${note_value} зображений {TEN_DOLLARS}.")
elif note_value == "20":
    print(f"На банкноті ${note_value} зображений {TWENTY_DOLLARS}.")
elif note_value == "50":
    print(f"На банкноті ${note_value} зображений {FIFTY_DOLLARS}.")
elif note_value == "100":
    print(f"На банкноті ${note_value} зображений {ONE_HUNDRED_DOLLARS}.")
else:
    print("Введіть правильний номінал банкноти.")