# 13.01.23 Sergii Logosha sergiilogosha@gmail.com
# Last updated 04.02.23

# The program is simulating Blacjack game

from art import logo
from os import system
from random import choice

def play_game():
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = choice(cards)
        return card
    
    
    def calculate_score(cards_list):
        score = sum(cards_list)
        if score == 21:
            return 0
        if 11 in cards_list and score > 21:
            cards_list.remove(11)
            cards_list.append(1)
        return score
    
    
    def compare(user_score, computer_score):
        if user_score > 21:
            return 'You went over, you loose'
        elif user_score == computer_score:
            return 'Its a draw!'
        elif computer_score == 0:
            return 'Computer wins, it has a Blackjack'
        elif user_score == 0:
            return 'You win, you have a Blackjack'
        elif computer_score > 21:
            return 'Computer went over, you win'
        elif computer_score > user_score:
            return 'Computer wins'
        else:
            return 'You win'
            
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, your current score: {user_score}')
        print(f'Computers first card: {computer_cards[0]}')
        
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input('Type "y" to get another card, type "n" to pass: ')
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'Computers final hand: {computer_cards}, final score: {computer_score}')
    print(compare(user_score, computer_score))

while input('Do you want to play Blackjack game("y"/"n"): ') == 'y':
    system('clear')
    play_game()
