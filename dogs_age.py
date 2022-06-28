# Sergii Logosha, 28 Jun 2022

# The program prompts user to input dog's real age and calculates its age in "human years"

real_age = float(input("How old is the dog (years)? ").strip())

if real_age > 0:
    if real_age <= 2:
        dogs_age = int(real_age * 10.5)
        print(f'The dog\'s age in "human years" is {dogs_age} years.')
    elif real_age > 2:
        first_two_years = 2 * 10.5
        other_years = (real_age - 2) * 4
        total_dogs_age = int(first_two_years + other_years)
        print('The dog\'s age in "human years" is {} years.'.format(total_dogs_age))
else:
    print("Type in correct age, please.")
