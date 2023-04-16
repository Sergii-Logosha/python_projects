# 16.04.2023 Sergii Logosha sergiilogosha@gmail.com

# Program outputs list of NATO accepted words for every letter in the word
# that user inputs

import pandas
nato_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')

csv_to_dict = nato_alphabet_df.to_dict()
nato_alphabet_dict = {row['letter']: row['code'] for (index, row)
                      in nato_alphabet_df.iterrows()}

user_input = input('Type in a word: ').upper()
nato_alphabet_list = [nato_alphabet_dict[letter] for letter in user_input]
print(nato_alphabet_list)
