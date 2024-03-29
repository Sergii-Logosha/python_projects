# 06.03.2023 Sergii Logosha sergiilogosha@gmail.com
# Last modified 21.03.2023

from ball import Ball
from time import sleep
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

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
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball collides with the top and bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Ball collides with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

screen.exitonclick()
