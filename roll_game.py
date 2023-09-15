import random ## import the random module for the dice rolling

## we#ve created variables for the minimum and maximum values when the dice is rolled
minimum_value = 1
maximum_value = 6
name = input("Welcome! What is your name? ") ##This is the first message to the user

print(f"Hi {name}, let's play a dice rolling game!")  ##Based on the name variable the user is invited to roll the dice
print("Rolling dice...")

def roll_dice():                                       ## this allows us get random numbers from 1 to 6
    return random.randint(minimum_value, maximum_value)

def play_game():  ## this allows us to create the loop for the user to keep rolling
    while True:
        result = roll_dice()
        print(f"You've rolled a {result}!")

        roll_again = input("Do you want to play again? (yes/no): ").lower()   ##this invites the user to roll again
        if roll_again != "yes":
            break

play_game() ## function is being called
print("Thanks for playing!") ##last closing message
