"""
Problem #1
write a program that reads a passage and reverses the order of
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS
"""
import re

# Get input sentence from the user
ip_sentence = str(input("Enter the Sentence:\n"))

# Use regular expression to find all words in the sentence
words = re.findall(r'\b\w+\b', ip_sentence)

# Reverse each word and print them
for word in words:
    # Reverse the word using slicing and print with a space at the end
    print(word[::-1], end=" ")

# End of the program
