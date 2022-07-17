# Sergii Logosha, 17 Jul 2022

# Program prompts user to insert the number of the sides of the figure and prints out the name of the figure

while True:
    number_of_sides = int(input("How many sides the figure have? ").strip())

    if 0 < number_of_sides <= 10:
        if number_of_sides == 1:
            print("The figure with {} side is MONOGON.".format(number_of_sides))
        elif number_of_sides == 2:
            print(f"The figure witn {number_of_sides} sides is DIGON.")
        elif number_of_sides == 3:
            print(f"The figure with {number_of_sides} sides is TRIANGLE.")
        elif number_of_sides == 4:
            print("The figure with {} sides is QUADRILATERAL.".format(number_of_sides))
        elif number_of_sides == 5:
            print(f"The figure witn {number_of_sides} sides is PENTAGON.")
        elif number_of_sides == 6:
            print(f"The figure with {number_of_sides} sides is HEXAGON.")
        elif number_of_sides == 7:
            print(f"The figure with {number_of_sides} sides is HEPTAGON.")
        elif number_of_sides == 8:
            print("The figure with {} sides is OCTAGON.".format(number_of_sides))
        elif number_of_sides == 9:
            print(f"The figure witn {number_of_sides} sides is NONAGON.")
        elif number_of_sides == 10:
            print(f"The figure with {number_of_sides} sides is DECAGON.")
    else:
        print("You have to type in the correct number if sides (between 1 and 10).")
