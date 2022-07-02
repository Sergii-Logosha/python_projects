# Author: Sergii Logosha
# Date Created: 30.05.2022
# Last Modified: 12.06.2022

# Description 
# Program asks for number and answering if the guess was right.

# Usage
# 

from random import randint
secret = randint (1, 20)

# printing out the welcome message
print("Welcome to the Game!!!")

number = 0
while number != secret:
# prompt user to insert number betweenn 0 and 20
  number = int(input("Please, gues the number in between 0 and 20\n"))

# checking the conditions and making decision
  if number == secret :
    print("You win!")
  else :
    if number > secret :
      print("Too high!")
    else :
      print("Too low")

# print out the final message
print("Game over!")
