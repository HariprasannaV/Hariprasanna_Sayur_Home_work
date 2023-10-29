"""
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba


look at the output and find the pattern. Hint - add next letter in the alphabet in each row
"""

# Define the alphabet and include a space character
alphabet = 'abcdefghijklmnopqrstuvwxyz '

# Get a letter as input from the user and convert it to lowercase
letter = str(input("Enter the letter: ")).lower()

# Find the position (index) of the input letter in the alphabet
position = alphabet.find(letter)

# Initialize an empty string for the pattern
patternString = ""

# Loop through the alphabet up to the position of the input letter
for i in range(position + 1):
    # Build the patternString by adding characters from the alphabet
    patternString = patternString + alphabet[i] + patternString

    # Print the current state of patternString in each iteration
    print(patternString)
