# Sergii Logosha, 08 Jun 2022

# Program ask user to input the length and width of the room and calculates and prints out the area

# prompt user to input the length and the width of the room
length = float(input("What is the lenth of your room(in meters)?\n"))
width = float(input("What is the width of your room(in meters)?\n"))

# calculating the area of the room
area = round(length * width, 2)

# printing out the result message
print("The area of your room is", area, "square meters.")