# Sergii Logosha, 18 Jun 2022

# Program checks if the user in the list. If it in, program suggests to delete him. If user is not in the list, it
# suggests to add him

# List of the system's known users
known_users = ["Sergii", "Ira", "Alina", "Marina", "Katy", "Laura", "Barry", "Tom"]

# Printing greeting message and prompt user to input their name
while True:
    print("Hi, my name is RSS")
    name = input("And what is your name? ").strip().capitalize()

# Checking if the user in the list if known users
    if name in known_users:
        print("Hello, " + name + ", wellcome in!")

# Asking user if he wants to be removed from the system
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        else:
            print("I'm glad, that you are staying with us.")

# Message for unrecognised users
    else:
        print("Hmm-mmm, I don't think we met before, " + name + "!")
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        else:
            print("I will be glad to see you around.")
