# 19.02.2023 Sergii Logosha sergiilogosha@gmail.com

from turtle import Turtle, Screen
from random import choice
tim = Turtle()
tim.shape('turtle')
tim.color('ForestGreen')
tim.width(10)
tim.speed(5)

ANGLE = [0, 90, 180, 270]
TURTLE_COLORS = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'navy',
                 'maroon', 'sienna', 'tomato', 'salmon', 'coral', 'brown']

while True:
    tim.forward(25)
    tim.setheading(choice(ANGLE))
    tim.color(choice(TURTLE_COLORS))

my_screen = Screen()
my_screen.exitonclick()