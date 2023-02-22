# 22.02.2023 Sergii Logosha sergiilogosha@gmail.com

# Program emulates "Etch-a-Sketch" game. The turtle can be controlled by the
# "w", "s", "a", "d" and "c" keys

from turtle import Turtle, Screen


def move_forward():
    tim.forward(30)


def move_backward():
    tim.backward(30)


def move_clockwise():
    tim.right(10)


def move_counterclockwise():
    tim.left(10)


def clear_and_go_to_center():
    tim.clear()
    tim.penup()
    tim.setheading(0)
    tim.goto(0, 0)
    tim.pendown()


tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.color('green')
tim.speed(10)
tim.width(5)

screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=move_clockwise, key='d')
screen.onkey(fun=move_counterclockwise, key='a')
screen.onkey(fun=clear_and_go_to_center, key='c')
screen.listen()
screen.exitonclick()
