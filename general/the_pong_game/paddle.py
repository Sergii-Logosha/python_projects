from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.x_coor = x_coordinate
        self.y_coor = y_coordinate
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.x_coor, self.y_coor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
