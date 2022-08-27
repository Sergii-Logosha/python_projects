rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

storage = [rock, paper, scissors, ]
computers_choice = random.choice(storage)

while True:
    answer = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if answer < 0 or answer > 2:
        continue
    else:
        break

users_choice = storage[answer]
print(users_choice)
print("Computer chose:")
print(computers_choice)

if (computers_choice == rock and users_choice == scissors) or (
        computers_choice == paper and users_choice == rock) or (
        computers_choice == scissors and users_choice == paper):
    print("You lose")
elif computers_choice == users_choice:
    print("Its a draw")
else:
    print("You win")