from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('yellow')
        self.penup()
        self.goto(-10, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.scores} High score: {self.high_score}',
                   move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scores += 1
        self.update_score()

    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.scores = 0
        self.update_score()

