# 25.03.23 Sergii Logosha sergiilogosha@gmail.com

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.list_of_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect crossing finish line
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
