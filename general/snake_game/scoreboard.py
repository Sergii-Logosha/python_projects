from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.goto(-10, 280)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.scores}', move=False, align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.clear()
        self.scores += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER!', move=False, align=ALIGNMENT,
                   font=FONT)
