# Sergii Logosha, 10 Jul 2022

# The program asks user for a letter and tells if it's consonant or vowel

letter = input("Please, enter a letter: ").strip().lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f'The letter "{letter}" is vowel.')
elif letter == "y":
    print(f'The letter "{letter}" can be either vowel or consonant.')
else:
    print(f'The letter "{letter}" is consonant')
