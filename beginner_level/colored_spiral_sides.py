# Author: Sergii Logosha
# Date Created: 01.06.2022
# Last Modified: 01.06.2022

# Description 
# Program paints square multicolored spirals.

# Usage
#

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# You can assine frome 2 to 6 sides to get even better figures.
sides = eval(input("Input sides number from 2 to 9: "))
colors = ["red", "green", "yellow", "orange", "white", "gold", "salmon", "purple", "blue"]
for x in range(200):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)
