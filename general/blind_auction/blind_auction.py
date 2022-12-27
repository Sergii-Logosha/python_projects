# 27.12.22. Sergii Logosha sergiilogosha@gmail.com

# Program simulates blind auction. Biders input their names and bids and program outputs the winner
# with the bigest bid.

from art import logo
from replit import clear

print(logo)
print('Welcome to the Blind Auction!')

biders_dict = {}

other_biders = True
while other_biders:
    biders_name = input('Your name: ')
    bid = int(input('Your bid: $'))
    biders_dict[biders_name] = bid
    more_biders = input('Are there any other biders (yes/no): ')
    if more_biders == 'yes':
        other_biders = True
        clear()
    elif more_biders == 'no':
        other_biders = False
    else:
        print("Give the proper answer!")

bids_list = []
for bid in biders_dict:
    bids_list.append(biders_dict[bid])
max_bid = max(bids_list)

list_of_names = list(biders_dict.keys())
position = bids_list.index(max_bid)
bider_name = list_of_names[position]

print(f'The winner is {bider_name} with the bid ${max_bid}.')
