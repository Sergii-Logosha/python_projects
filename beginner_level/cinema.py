# Sergii Logosha, 21 Jun 22

# Program for selling cinema tickets. It asks user it's age, checks if there are available sits and
# sells or not the tickets.

films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Basters": [12, 5]
}

while True:
    choice = input('What film would you like to watch?\n"Finding Dory"\n"Bourne"\n'
                   '"Tarzan"\n"Ghost Basters"\n').strip().title()

    if choice in films:
        age = int(input("How old are you?\n").strip())

        if age >= films[choice][0]:

            if films[choice][1] > 0:
                print("Enjoy the film.")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are sold out.")
        else:
            print("You are too young to watch that film.")

    else:
        print("Sorry, we don't have that film...")