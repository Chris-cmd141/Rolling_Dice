## the purpose of this project: To create a programme that will ask the user to roll the dice, give him a random roll result from 1 to 6, then to ask the user if they want to play again.


import random ## import the random module for the dice rolling - this will help us create a function that randomly selects a number from 1 to 6.

## Below we choose the min and max values that the dice can roll. we've created variables for the minimum and maximum values when the dice is rolled
minimum_value = 1
maximum_value = 6
name = input("Welcome! What is your name? ") ##This is the first message to the user when the programme is executed.

print(f"Hi {name}, let's play a dice rolling game!")  ##Once the user writes their name the programme will invite him to roll the dice. Based on the name variable the user is invited to roll the dice
print("Rolling dice...")

def roll_dice():                                       ## this allows us get random numbers from 1 to 6. We've used "return" so we can use the same random algorythm in the next function where the game is actually played
    return random.randint(minimum_value, maximum_value)

def play_game():  ## this allows us to create the loop for the user to keep rolling
    while True:
        result = roll_dice()
        print(f"You've rolled a {result}!")

        roll_again = input("Do you want to play again? (yes/no): ").lower()   ##this invites the user to roll again.  ".lower" is used so the programme applies the same rule for capitals or lower "yes/no"
        
        if roll_again != "yes": ## if the user selects anything that is not "YES" or "yes" then the loop will stop, the programme will stop asking if they want to roll.
            break ##the break command stops the loop once the user writes "no"

play_game() ## function is being called, this command runs the programme.
print("Thanks for playing!") ##last closing message









