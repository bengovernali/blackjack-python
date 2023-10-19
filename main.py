import random

# Deck of Cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function for displaying cards/scores
def show_hands(user1, user2, turn):
    # Always print full player hand
    print(f'Player Hand: {user1}')
    if turn:
        print(f'CPU Hand: [{user2[0]}, X]')
    else:
        print(f'CPU Hand: {user2}')
    print()

# function for evaluating scores and determining next step
def evaluate_scores(score1, score2):
    # Calculate Scores / Modify hands if necessary
    if score1 == 0 and score2 == 0:
        return declare_winner("Nobody")
    elif score1 == 0 or score1 == 21:
        return declare_winner("Player")
    elif score2 == 0 or score2 == 21:
        return declare_winner("CPU")
    elif score1 > 21: 
        return declare_winner("CPU")
    elif score2 > 21: 
        return declare_winner("Player")
    else:
        return True

def calculate_score(user):
    score = sum(user)
    if score == 21 and len(user) == 2:
        score = 0
    #if score > 21 and 11 in hand, replace with 1 then recalculate score.
    elif score > 21 and 11 in user:
        index_of_ace = user.index(11)
        user[index_of_ace] = 1
        score = sum(user)
    return score

def declare_winner(user):
    print(f'{user} wins!')
    print()
    # prompt user to play again
    play_again = input("Would you like to play again? Enter 'y' for yes and 'n' for no: ")
    print()
    if play_again == 'y':
        return True
    else:
        return False

def blackjack():
    game_running = True
    
    while game_running:
        # initial setup
        player_hand = []
        cpu_hand = []
        is_player_turn = True

        # 'Deal' initial hands
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))

        # Reveal initial hands
        show_hands(player_hand, cpu_hand, is_player_turn)

        # calculate scores
        player_score = calculate_score(player_hand)
        cpu_score = calculate_score(cpu_hand)

        # evaluate initial scores
        game_running = evaluate_scores(player_score, cpu_score)

        # conduct player turns 
        
        while is_player_turn:
            # prompt user to draw a card
            draw_card = input("Would you like to draw a card? enter 'y' for yes and 'n' for no: ")
            # if user selected 'y'
            if draw_card =='y':
                # add another card to player hand
                player_hand.append(random.choice(cards))
                # recalculate player score
                player_score = calculate_score(player_hand)
                show_hands(player_hand, cpu_hand, is_player_turn)
                # reevaluate scores
                game_running = evaluate_scores(player_score, cpu_score)
            # end player turn, breaking the loop
            else:
                is_player_turn = False
        # conduct cpu turns
        while cpu_score < 17:
            cpu_hand.append(random.choice(cards))
            # recalculate cpu score
            cpu_score = calculate_score(cpu_hand)
            # reevaluate scores
            show_hands(player_hand, cpu_hand, is_player_turn)
            game_running = evaluate_scores(player_score, cpu_score)
        # compare score and declare winner
        show_hands(player_hand, cpu_hand, is_player_turn)
        if player_score > cpu_score:
            game_running = declare_winner("Player")
        else:
            game_running = declare_winner("CPU")
        player_hand = []
        cpu_hand = []

blackjack()