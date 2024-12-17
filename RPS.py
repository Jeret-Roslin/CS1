import random                                                               # random choice is imported 
import sys                                                                  # Makes the code exit
import os                                                                   # Makes the code clear 
import time                                                                 # Imports time to the code
print("Welcome to the Rock, Paper, Scissors Simulator!")                     # prints message 
weapons = ['rock','paper','scissors']                                            # list of responses

p1_name = input("Player 1, what is your name? ")                                # asks player 1 their name

while True:                                                                             # forever loop
    game_style = input("Do you want to play against the computer or another player? ")  # asks the user a question
    time.sleep(1)                                                               # code is paused for 1 sec
    
    if game_style == "computer":                                                # computer mode is chosen
        p2_name = "bot"                                                         # player 2 is bot
    elif game_style == "another player":                                        # game mode is another player"
        p2_name = input("Player 2, what is your name? ")                        # asks player 2 their name
    else:                                                                       # if and elif choices aren't chosen
        print("Invalid response")                                               # user response is invalid
        continue

    player_1_score=0                                                            #player 1 score is set to 0
    player_2_score=0                                                            # player 2 is set to 0

    while player_1_score < 2 and player_2_score < 2:                                 # player 1 and 2 score are less than 2
        player_1_weapon = str.lower(input(f"{p1_name}, choose rock, paper, or scissors "))  # player 1 chooses weapon
        
        if player_1_weapon not in weapons:                                                  # response is not a weapon
            continue                                                                        # repeats question
        
        if game_style == "computer":                                                        # game mode is computer
            player_2_weapon = random.choice(weapons)                                   # computer weapon generates random choice from the list
        else:
            os.system('cls')                                                                # hides player 1's response for player 2
            player_2_weapon = str.lower(input(f"{p2_name}, choose rock, paper, or scissors "))    # player 2 chooses weapon
            if player_2_weapon not in weapons:                                                      # player 2 response is not in weapons
                continue                                                                        # repeats question    os.system('cls') 
        print('calculating')                                                            # displays message
        time.sleep(2)                                                                   # pauses code for 2 secs    
        print(f"{p1_name} chose {player_1_weapon} and {p2_name} chose {player_2_weapon}") # displays choosen weapon for both players
        print("AI is generating winner...")                                             # displays message
        time.sleep (2)                                                                  # pauses code for 2 secs
        
        if player_1_weapon == player_2_weapon:                                                # player 1 and player 2 weapons are the same
            print("tie")                                                               # displays message
        elif player_1_weapon == "rock":                                         # user chooses rock
            if player_2_weapon == "paper":                                      # computer chooses paper
                print(f"{p2_name} won!")                                           # displays message
                player_2_score+=1                                                    # player 2's score is +1 point
            else:                                                                # happens when if and elif aren't choosen
                print(f"{p1_name} won!")                                           # displays message
                player_1_score+=1                                                    # player 1's  score is -1 point
        elif player_1_weapon == "paper":                                        # player 1  chooses paper
            if player_2_weapon == "scissors":                                   # player 2 chooses scissors
                print(f"{p2_name} won!")                                           # displays message
                player_2_score+=1                                                    # player 2'sscore is -1 point
            else:                                                                       # happens when if and elif aren't choosen
                print(f"{p1_name} won!")                                           # displays message
                player_1_score+=1                                                    # user's score is -1 point
        elif player_1_weapon== "scissors":                                     # player 1 chooses scissors
            if player_2_weapon == "rock":                                       # player 2 chooses rock
                print(f"{p2_name} won!")                                           # displays message
                player_2_score+=1                                                    # user's score is -1 point
            else:                                                       # happens when if and elif aren't choosen
                print(f"{p1_name} won!")                                           # displays message
                player_1_score+=1                                                    # player 1's score is -1 point
        print(f"{p1_name} has {player_1_score} points and {p2_name} has {player_2_score} points") # displays score
    
    if player_1_score > player_2_score:                                                 # player 1 and player 2 have the same score
        print(f"{p1_name} won this game")                                               # displays message 
    else:                                                                               # happens when if isn't choosen
        print(f"{p2_name} won this game")                                               # displays message
    while True:                                                                          # forever loop
        play_again = input(f"The score was {player_1_score} to {player_2_score}. Do you want to play again? ")          # asks player a question        # asks the user a question
        
        if play_again == "yes":                                                          # user says yes to playing again
            break                                                                        # terminates code
        elif play_again == "no":                                                         # user chooses not to play again
            sys.exit()                                                                   # ends code
        else:                                                                             # happens when if and elif statements aren't choosen
            print("Invalid")                                                              # user response is invalid
