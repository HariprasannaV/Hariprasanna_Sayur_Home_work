"""
From a given passage extract unique words and print them.
Accept the passage as an input from the user
"""
# Prompt the user to enter a sentence
sentence = input("Enter the sentence here: ")

# Initialize an empty list to store lowercase words
lower_case_word_list = []

# a list of symbols to remove from the sentence
symbols = ['.', ',', '<', '>', '/', '?', ';', ':', '"', "'", '[', ']', '{', '}', '|', '~', '`', '!', '@', '#', '$', '%',
           '^', '&', '*', '(', ')', '_', '-', '+', '=', '±', '”']

# Loop through each character in the sentence
for cr in sentence:
    # Check if the character is in the list of symbols
    for i in range(len(symbols)):
        if cr == symbols[i]:
            # Replace the character with an empty string (remove it)
            sentence = sentence.replace(cr, "")

# Print the sentence with symbols removed
# print(sentence)

# Convert the sentence to lowercase and split it into words
lower_case_word_list = sentence.lower().split()

# Initialize an empty list to store unique lowercase words
empty_list = []

# Loop through each word in the lowercase word list
for word in lower_case_word_list:
    # Check if the word is not already in the empty list
    if word not in empty_list:
        # If not, add it to the empty list
        empty_list.append(word)

# Print the list of unique lowercase words
print(empty_list)

"""

Input:
Enter the sentence here: A dog has a strong power of smell. They are more liked by people because of their faithfulness. 
They are intelligent, they are watchfulness. The dogs have many colors such as grey, white, black, brown and red. 
They are of many kinds such as bloodhound, greyhound, german shepherd, Labrador, Rottweiler, bulldog poodle, etc.

output:
['a', 'dog', 'has', 'strong', 'power', 'of', 'smell', 'they', 'are', 'more', 'liked', 'by', 'people', 'because', 
'their', 'faithfulness', 'intelligent', 'watchfulness', 'the', 'dogs', 'have', 'many', 'colors', 'such', 'as', 'grey', 
'white', 'black', 'brown', 'and', 'red', 'kinds', 'bloodhound', 'greyhound', 'german', 'shepherd', 'labrador', 
'rottweiler', 'bulldog', 'poodle', 'etc']

"""