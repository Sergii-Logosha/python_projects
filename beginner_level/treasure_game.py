# Sergii Logosha, 04 Jul 2022

# Program-joke, lets User find treasure by making different decisions.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are going on th strait road. Suddenly there is an intersection."
      " You have to chose to go to the right or to go to the left.")
turn = input("Where are you going to turn? Right or left? ").lower()

if turn == "left":
    print(
        "You turned left. Soon you came to the bank of a big river. Now you have to chose swim it over or wait for "
        "boat.")
    river = input("Are you going to swim or wait? ").lower()
    if river == "wait":
        print("The boat took you to the other side of the river. There was a big, old castle.\n"
              "You entered the castle and there were three doors inside: red, blue and yellow.")
        doors = input("Which door do you chose? ")
        if doors == "red":
            print("You are burned by fire. Game over!")
        elif doors == "blue":
            print("You are eaten by beasts. Game over")
        elif doors == "yellow":
            print("You win! The treasure is yours!")
        else:
            print("You are not following the rules. You are baned! Game over!")
    elif river == "swim":
        print("At the middle of the river you were eaten by green crocodile. For you game over!")
    else:
        print("You are not following the rules. You are baned! Game over!")
elif turn == "right":
    print("There was a trap. You fall into a hole. Sorry, game over!")
else:
    print("You are not following the rules. You are baned! Game over!")
