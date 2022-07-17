# Sergii Logosha, 03 Jul 2022

# Program-joke that calculates the index of compatibility between two people based on their names
# and gives the resulted conclusion.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
full_name = name1 + name2

t_number = full_name.count("t")
r_number = full_name.count("r")
u_number = full_name.count("u")
e_number = full_name.count("e")
first_number = t_number + r_number + u_number + e_number

l_number = full_name.count("l")
o_number = full_name.count("o")
v_number = full_name.count("v")
e_number = full_name.count("e")
second_number = l_number + o_number + v_number + e_number

score = str(first_number) + str(second_number)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
