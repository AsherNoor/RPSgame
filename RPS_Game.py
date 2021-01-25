""" 
Rock Paper Scissors
---------------------
PyGame
Coded by: ryn0f1sh (Ash Noor)
Version: 001
Date: Dec/26/2020
"""

# -- The Imports --
import random
import os
import sys
import math
import time
#-------------------






#-- Play Again Function --
def playAgain():
    answer = input("\nWould you like to play again? y/n: ")
    if answer.lower() == 'y':
        #-- calling The Game Function
        theGame()
    else:
        print("Thanks For Playing")
        time.sleep(2)
        exit()
#-- End of Play Again Function --
#--------------------------------






#-- The Game Function --
def theGame():
    #-- The Variables
    rounds = 1
    u1points = 0 #-- User 1 points counter
    u2points = 0 #-- User 2 points counter
    #----------------

    #-- The Game's 3 Rounds While Loop
    while (rounds <= 3):
        print("\n Round: " + str(rounds),
        "\n User 1: " + str(u1points),
        "\n User 2: " + str(u2points))


        #-- RPS Menu
        print("\n[1] is Rock -- [2] -- is Paper -- [3] is Scissors.\n")

        #-- UI: Making the choice.
        u1choice = random.randint(1,3) #Computer will randomly choose a number.
        print("Gamebot has chosen")
        u2choice = int(input("User 2 Choose: 1, 2, or 3: "))



        ''' --------------------------------
            The Algorithm & Scoring section
            --------------------------------'''

        #-- ROCK
        if u1choice == 1 and u2choice == 3:
            u1points += 1
            print("Rock beats Scissor - Point for Gamebot")
            time.sleep(2)
        if u2choice == 1 and u1choice == 3:
            u2points +=1
            print("Rock beats Scissor - Point for You")
            time.sleep(2)

        #-- PAPER
        if u1choice == 2 and u2choice == 1:
            u1points += 1
            print("Paper beats Rock - Point for Gamebot")
            time.sleep(2)
        if u2choice == 2 and u1choice == 1:
            u2points += 1
            print("Paper beats Rock - Point for You")
            time.sleep(2)

        #-- SCISSORS
        if u1choice == 3 and u2choice == 2:
            u1points += 1
            print("Scissor beats Paper - Point for Gamebot")
            time.sleep(2)
        if u2choice == 3 and u1choice == 2:
            u2points += 1
            print("Scissor beats Paper - Point for You")
            time.sleep(2)


        #-- A TIE
        if u1choice == u2choice:
            print("Its a tie, No points")
            time.sleep(2)


        #-- The Next round/turn begins
        rounds +=1

    #-- End of the While Loop --




    # -- Declaring the winner
    print("\n\nThe Final Score"
          "\n----------------")
    if u1points > u2points:
        print("Gamebot wins with [ " + str(u1points) + " ] out of 3 points.")
    elif u1points == u2points:
        print("No One Wins this time.")
    else:
        print("You win with [ " + str(u2points) + " ] out of 3 points.")


    #-- Calling the Play Again function
    playAgain()

# -- End of The Game Function --
# ------------------------------








#-- Intro Function --
def intro():
    print("\n- - - - - - - - - - - -"
          "\nWelcome to Rock Paper Scissor"
          "\nLets Play!"
          "\n- - - - - - - - - - - - \n")

    #-- Calling the Game Function
    theGame()

#-- End of Intro Function --
#---------------------------




#-- Calling The Intro function to start the program.
intro()


