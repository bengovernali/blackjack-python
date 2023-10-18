import random

# Deck of Cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# State items 
game_running = True
game_over = False
player_turn = True

# Dictionary for storing hands
hands = {
    "player": [],
    "cpu": []
}

# Function for dealing hands
def deal_cards():
    hands["player"].append(random.choice(cards))
    hands["player"].append(random.choice(cards))
    hands["cpu"].append(random.choice(cards))
    hands["cpu"].append(random.choice(cards))

# Function for displaying cards/scores
def show_hands():
    # Always print full player hand
    print(f'Player Hand: {hands["player"]}')
    # Only print full cpu hand on cpu turn
    if player_turn:
        print(f'CPU Hand: [{hands["cpu"][0]}, X]')
    else:
        print(f'CPU Hand: {hands["cpu"]}')

deal_cards()
show_hands()