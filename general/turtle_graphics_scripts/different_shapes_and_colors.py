# 19.02.2023 Sergii Logosha sergiilogosha@gmail.com

from turtle import Turtle, Screen
from random import choice
tim = Turtle()
tim.shape('turtle')
tim.color('ForestGreen')

NUMBER_OF_SIDES = [3, 4, 5, 6, 7, 8, 9, 10]
COMPLETE_ANGLE = 360
TURTLE_COLORS = ['blue', 'green', 'red', 'yellow', 'orange', 'RoyalBlue',
                 'magenta']

for item in NUMBER_OF_SIDES:
    tim.color(choice(TURTLE_COLORS))
    for _ in range(item):
        tim.forward(100)
        tim.right(COMPLETE_ANGLE / item)


my_screen = Screen()
my_screen.exitonclick()