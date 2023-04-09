# 09.04.23 Sergii Logosha sergiilogosha@gmail.com

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv('50_states.csv')
list_of_states = df.state.tolist()

right_guess = 0
attempts = 100
while len(list_of_states) > 0 and attempts > 0:
    answer_state = screen.textinput(title=f'Guess The State: {right_guess}/50',
                                    prompt='Guess the state name:').title()

    if answer_state in list_of_states:
        state_data = df[df.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state, align="center",
                         font=("Comic Sans", 8, "bold"))
        list_of_states.remove(answer_state)
        right_guess += 1

    attempts -= 1
