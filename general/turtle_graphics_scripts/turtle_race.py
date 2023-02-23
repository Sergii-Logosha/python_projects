# 23.02.2023 Sergii Logosha sergiilogosha@gmail.com

from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='What turtle come '
                                                          'first to the '
                                                          'finish? Pick the '
                                                          'color (red/green/'
                                                          'blue/orange/purple/'
                                                          'sienna: ')
turtle_colors = ['red', 'green', 'blue', 'orange', 'purple', 'sienna']
y_coordinates = [150, 90, 30, -30, -90, -150]
turtles_list = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle_colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-235, y_coordinates[turtle])
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the "
                      f"winner")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
