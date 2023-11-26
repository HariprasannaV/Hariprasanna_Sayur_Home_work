"""
Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."
"""


import re

# Get input sentence from the user
Sentence = str(input("Enter the sentence: "))

# Extract all words from the sentence using regular expression
words = re.findall(r'\b\w+\b', Sentence)

# Convert all words to lowercase for case-insensitive comparison
small_words = re.findall(r'\b\w+\b', Sentence.lower())

# List to store repeated words
Empty_list = []

# Check for repeated adjacent words
for i in range(len(small_words)-1):
    if small_words[i] == small_words[i+1]:
        # Print the repeated words
        print(words[i], words[i+1])
        # Add the repeated word to the list
        Empty_list.append(words[i])

# Dictionary to store the count of each repeated word
Empty_dict = {}

# Count the occurrences of each repeated word
for i in Empty_list:
    count = Empty_list.count(i)
    Empty_dict[i] = count

# Print the dictionary with repeated word counts
print(Empty_dict)

# Print the occurrences of each repeated word
for i, j in Empty_dict.items():
    print(f'The occurrences of {i} {i} is {j} times!')
