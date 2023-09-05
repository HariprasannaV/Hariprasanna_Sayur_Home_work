"""
######## Problem 2 ###############
# Computer will guess a random number.
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import #FillinMissingCode
computerNo = random.randint(3, 9)

attempt = 0
while(True):
    userNo = int (#FillinMissingCode)
    #FillinMissingCode
    attempt +=1

print ("User guessed the number in ", attempt, "attempts")
"""
import random

computerNo = random.randint(3, 9)  # Generates a random number between 1 and 100

attempt = 0
while True:
    userNo = int(input("Guess the number: "))  # Get user input as an integer

    if userNo < computerNo:
        print("Low")
    elif userNo > computerNo:
        print("High")
    else:
        print("Congratulations! You guessed the number correctly.")
        break  # Exit the loop when the user guesses correctly

    attempt += 1

print("User guessed the number in", attempt+1, "attempts")

"""
Output:

Guess the number: 5
Low
Guess the number: 8
High
Guess the number: 7
Congratulations! You guessed the number correctly.
User guessed the number in 3 attempts

"""