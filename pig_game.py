#getting back into coding after finishing the Eco_Warrior game!

#This first project is a game called Pig. Its a dice game where players take turns to roll a 6-sided die and get points. 
#The goal is to reach a certain score (50) before the other player. 
#If a player rolls a 1, they lose all points in that turn and their turn ends. 
#Players can choose to "hold" their points, passing the turn to the next player.

import random

def roll():
    min_value =1 #lower limit
    max_value = 6 #upper limit
    roll = random.randint(min_value, max_value) #randomly chooses an integer between 1 and 6 and stores it in the roll variable. min and max ARE included.
    return roll #returns the value of the roll variable

while True:
    num_players = input("\nHow many players are playing? (2-4):  ")
    if num_players.isdigit(): #acts a saftey check to make sure we aren't trying to a string into an integer. 
        num_players = int(num_players)
        if 2<= num_players <= 4: #only 2-4 players
            print(f'\n{num_players} player(s) are playing!')
            break
        else:
            print('\nEnter a number between 2 and 4')
    else:
        print('\nInvalid. Must enter a number between 2 and 4')

max_score = 50 #max score to win the game
player_scores = [0 for _ in range(num_players)] #stores the scores of each player
print(player_scores)
#This is the first time I have seen/used list comprehension. Essentially its a shortcut for writing the code commented out below.

#player_scores = []
#for i in range(num_players):
    #player_scores.append(0)

#Both have the same functionality, its just that list comprehension is cleaner and faster.

while max(player_scores) < max_score: #winning condition of the game. 
    for player_index in range(num_players): #simulates each player's individual turn.
        while True: #loops that player's turn until they either roll a 1 or choose to hold their points.
            current_score = 0
            print(f'\nPlayer number {player_index + 1}\'s turn has begun!\n')
            should_roll = input(f'Would you like to roll the dice? (y) ?  ')
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                current_score = 0 #reset score if they roll a one
                print(f'You rolled a 1! You lost all points for this turn. Better luck next time!')
                break
            else: 
                print(f'You rolled a {value}! You earned {value} points this turn!')
                current_score += value
            print(f'Your current score is: {current_score}')
    
    player_scores[player_index] += current_score
    print(f'Your total score is: {player_scores[player_index]}')
