# 06.03.2023 Sergii Logosha sergiilogosha@gmail.com
# Last modified 19.03.2023

from ball import Ball
from time import sleep
from turtle import Screen
from paddle import Paddle

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.setup(width=800, height=600)
screen.title('The Pong Game')
screen.bgcolor('green')
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()

    # Ball collides with the top wall
    if ball.ycor() > 290:
        ball.bounce()

    if ball.xcor() < -390 or ball.xcor() > 390:
        game_is_on = False

screen.exitonclick()
