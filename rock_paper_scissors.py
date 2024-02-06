import random
import time

choises = ['Rock', 'Paper', 'Scissors']

#####
def startGame() -> None:
    
    while True:
        print('\nEnter choice')
        print('1. Rock')
        print('2. paper')
        print('3. Scissor')

        # user choice
        usr_choice = ''
        while True:
            usr_choice = input('-> ')
            if usr_choice == '1' or usr_choice == '2' or usr_choice == '3': break

        usr_choice = choises[int(usr_choice)-1]
        print('\nUser choice is:', usr_choice)

        # computer chooses randomly
        comp_choice = random.choice(choises)                
        print('Computer choice is:', comp_choice, end='\n')

        # check who the winner is
        if comp_choice == usr_choice: # Draw
            print('\nDraw!\n')
        elif comp_choice == 'Rock' and usr_choice == 'Paper': # user wins
            print('\nYou win!\n')
        elif comp_choice == 'Rock' and usr_choice == 'Scissors': # computer wins
            print('\nComputer wins!\n')
        elif comp_choice == 'Paper' and usr_choice == 'Rock': # computer wins
            print('\nComputer wins!\n')
        elif comp_choice == 'Paper' and usr_choice == 'Scissors': # user wins
            print('\nYou win!\n')
        elif comp_choice == 'Scissors' and usr_choice == 'Rock': # user wins
            print('\nYou win!\n')
        elif comp_choice == 'Scissors' and usr_choice == 'Paper': # computer wins
            print('\nComputer wins!\n')

        time.sleep(1)

        # ask if the user wants to play again or not
        response = ''
        while True:
            response = input('Do you want to play again? (yes/no): ')
            if response.lower() == 'yes' or response.lower() == 'no': break
        if response == 'no': break
#####

startGame()