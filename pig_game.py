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
            print('\nEnter a number between 1 and 4')



