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
colors = ["red", "green", "yellow", "blue"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
