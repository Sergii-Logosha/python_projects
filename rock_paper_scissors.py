# Sergii Logosha, 01 Jul 2022
# Last modified 02 Jul 2022

# The program lets user play "Rock-Paper-Scissors" game with computer

import random

# In this section computer makes a random choice of "Rock", "Paper" or "Scissors"
random_choice = random.randint(0, 2)
if random_choice == 0:
    computer_choice = "Rock"
elif random_choice == 1:
    computer_choice = "Paper"
else:
    computer_choice = "Scissors"

# User makes it's choice
user_choice = ""
while user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissors":
    user_choice = input("Rock, Paper or Scissors? ").capitalize()

# Section with logic to find out the winner
winner = ""
if computer_choice == user_choice:
    winner = "Tie"

elif computer_choice == "Rock" and user_choice == "Scissors":
    winner = "Computer"

elif computer_choice == "Paper" and user_choice == "Rock":
    winner = "Computer"

elif computer_choice == "Scissors" and user_choice == "Paper":
    winner = "Computer"

else:
    winner = "User"

# Final messages section
if winner == "Tie":
    print(f"We both chose {computer_choice}, try again")

else:
    print(f"{winner} won, Computer chose {computer_choice}.")
