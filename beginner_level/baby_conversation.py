# Sergii Logosha, 22 Jun 22

# Program copies child continuously asking questions

from random import choice

questions = ["Why the water is wet?\n", "Why the Sun is so bright?\n", "Why my dog can't talk?\n"]
question = choice(questions)
answer = input(question).lower().strip()

while answer != "just because":
    answer = input("Why?\n").strip().lower()
print("Oh... Okay")
