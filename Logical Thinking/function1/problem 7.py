"""
Its is a single player game where the user starts with 0 points. User keeps rolling the
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump.
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.
"""


# Import the 'random' module for generating random numbers
def random():
    import random
    # Generate a random number between 0 and 6(randint is used to generate random number)
    random_no = random.randint(0, 6)
    return random_no


# Initialize the player's point
point = 0

# Start an infinite loop to play the game
while True:
    inp = input("press enter key to roll the dice")  # Wait for user to press Enter
    random_no = random()  # Call the random() function to get a random number
    print(random_no)  # Print the random number

    # Check the player's points to determine if the game should continue or end
    if point < 50:
        if random_no == 0:
            print("Your Total Points :", point)
            print("Game ends ! ")
            print("You Lose ! ")
            break  # Exit the loop if the random number is 0, indicating a loss
        elif random_no % 2 == 0:
            point += 2  # Add 2 points to the player's total for even numbers
            print("Your Points :", point)
        elif random_no % 2 != 0:
            if (random_no == 1) or (random_no == 3):
                print("Jump")  # Print "Jump" for 1 or 3
                continue  # Continue to the next iteration of the loop
            elif random_no == 5:
                point += 3  # Add 3 points to the player's total for 5
                print("Your Points :", point)
    else:
        print("Your Points :", point)
        print('You won ! ')  # Print a message indicating that the player has won
