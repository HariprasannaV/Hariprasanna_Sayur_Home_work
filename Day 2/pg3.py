"""
Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump.
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.
"""

import random

# Initialize the starting point
point = 0

# Main game loop
while True:
    # Display the current point
    print(f"Your Point: {point}\n ")

    # Check if the player has reached the winning point
    if point >= 50:
        print("You Won!!")
        break
    else:
        # Player is prompted to roll the dice
        x = input("Press Enter to Roll the Dice")

        # Generate a random number between 0 and 6 (inclusive) as the dice outcome
        dice_number = random.randint(0, 6)
        print(f'Dice number: {dice_number}')

        # Check if the dice outcome is 0, meaning the player loses
        if dice_number == 0:
            print("You Lose!")
            break
        # Check if the dice outcome is even
        elif dice_number % 2 == 0:
            # If even, add 2 to the player's point
            point += 2
            # Optional: Display the updated point after an even roll
            # print(f"Your Point: {point}")
        else:
            # If odd, check if the dice outcome is 1 or 3 and print "JUMP!" if true
            if dice_number == 1 or dice_number == 3:
                print("JUMP!")
            else:
                # If the dice outcome is any other odd number, add 3 to the player's point
                point += 3
