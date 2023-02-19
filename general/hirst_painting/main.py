# 19.02.2023 Sergii Logosha sergiilogosha@gmail.com

# Program extracts colors of the dots from original Hirst's painting and
# paints its own painting

from colorgram import Color, extract
from turtle import Turtle, Screen
from random import choice


def draw_line_of_dots():
    for _ in range(10):
        tim.dot(30, choice(colors_list))
        tim.forward(50)


tim = Turtle()
screen = Screen()
tim.hideturtle()
tim.speed(5)
screen.screensize(600, 600)
screen.colormode(255)

colors = extract('hirst_painting.jpg', 40)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = r, g, b
    colors_list.append(rgb_color)
for _ in range(3):  # deleting first three tuples with background color
    colors_list.pop(0)

x = -250
y = -250
tim.penup()
tim.setposition(x, y)
for _ in range(10):
    draw_line_of_dots()
    y += 50
    tim.goto(x, y)

screen.exitonclick()
