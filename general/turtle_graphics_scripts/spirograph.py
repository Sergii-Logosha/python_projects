from turtle import Turtle, Screen
from random import randint
tim = Turtle()
tim.shape('turtle')
tim.width(5)
tim.speed(10)
my_screen = Screen()
my_screen.colormode(255)


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


for _ in range(36):
    tim.pencolor(get_random_color())
    tim.circle(150)
    tim.right(10)

my_screen.exitonclick()
