# 02.04.2023 Sergii Logosha sergiilogosha@gmail.com

# TODO: Create a letter using starting_letter.txt
# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you:
# https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you:
# https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you:
# https://www.w3schools.com/python/ref_string_strip.asp

raw_list_of_names = open('Input/Names/invited_names.txt')
name_list_for_insertion = [name.strip('\n')
                           for name in raw_list_of_names.readlines()]

starting_letter = open('Input/Letters/starting_letter.txt')
starting_letter_for_insertion = starting_letter.readlines()

for name in name_list_for_insertion:
    starting_letter_for_insertion[0] = starting_letter_for_insertion[0].replace('[name]', name)
    complete_letter = open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w')
    for line in starting_letter_for_insertion:
        complete_letter.write(line)
    starting_letter_for_insertion[0] = starting_letter_for_insertion[0].replace(name, '[name]')

raw_list_of_names.close()
starting_letter.close()
complete_letter.close()
