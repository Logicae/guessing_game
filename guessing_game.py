import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correctly, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

user_guess = ""

while user_guess != random_number:  
    user_guess = int(input('Pick a number between 1 and 10: '))
    if user_guess > 10 or user_guess < 1: 
        print('Your number was out of range.')
    elif user_guess < random_number:
        print('Your guess was too low.')
    elif user_guess > random_number: 
        print('Your guess was too high.')
    else: 
        print('Winner!')
        new_game = input("Want to play again? (y/n) ")
        if new_game == 'y': 
            random_number = random.randint(1,10)
            user_guess = ""
        else: 
            print('No worries! Peace.')
            break