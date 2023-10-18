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

def calculate_score(user):
    score = sum(hands[user])
    #if score > 21 and 11 in hand, replace with 1 then recalculate score.
    if score > 21 and 11 in hands[user]:
        index_of_ace = hands[user].index(11)
        hands[user][index_of_ace] = 1
        score = sum(hands[user])
    print(score)
    return score

def player_turn():
    # prompt the user to draw a card
    user_choice = input("Would you like to draw a card? Please type 'y' for yes or 'n' for no. ")
    if user_choice == 'n':
        cpu_turn()
    else:
        hands["player"].append(random.choice(cards))
        calculate_score("player")

def cpu_turn():
    print("CPU TURN")

deal_cards()
show_hands()
calculate_score("player")
calculate_score("cpu")
player_turn()