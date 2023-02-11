# 11.02.23 Sergii Logosha sergiilogosha@gmail.com

# Game where user has to guess which option has more followers

from art import logo, vs
from game_data import data
from os import system
from random import choice


def pick_option(data):
    option = choice(data)
    return option


def answer_evaluation(data_1, data_2, key):
    if key == 'A':
        result = data_1["follower_count"] > data_2["follower_count"]
    else:
        result = data_2["follower_count"] > data_1["follower_count"]
    return result
    

option_1 = pick_option(data)
score = 0
game_on = True
while game_on:
    system('clear')
    print(logo)
    if score == 0:
        print(f'Current score: {score}')
    else:
        print(f'You are right! Current score: {score}')
    print(f'Compare A: {option_1["name"]}, {option_1["description"]} from {option_1["country"]}')
    print(vs)
    option_2 = pick_option(data)
    while option_2 == option_1:
        option_2 = pick_option(data)
    print(f'Against B: {option_2["name"]}, {option_2["description"]} from {option_2["country"]}')
    users_answer = None
    while users_answer not in ('A', 'B'):
        users_answer = input('Who has more followers? Type "A" or "B": ').upper()
    if answer_evaluation(option_1, option_2, users_answer):
        option_1 = option_2
        score += 1
        game_on = True
    else:
        system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False
