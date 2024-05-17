"""Create a game where the user must correctly guess a randomly generated integer between 1 and 100."""

import random
def create_rand_number():
    """This creates the random interger."""
    return random.randint(1,100)



"""The block below is the main logic code."""
guess = False# loop condition
answer = create_rand_number() #get the target
while not guess:#main loop
    user_guess = int(input("Enter your guess:"))#retrive input
    if user_guess == answer:#check if it is right
        guess = True
    elif guess > user_guess:#give hints
        print("Your guess was too high!")
    elif guess < user_guess:#give hints
        print("Your guess was too low!")
print("You guessed the right answer!")