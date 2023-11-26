"""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"

"""

# Import the regular expression module
# Import the regular expression module
import re

# Open the file in read mode
file = open("story 2", "r")

word_list = []

# Iterate through each line in the file
for line in file:
    print(line)

    # Use regular expression to find words, convert to lowercase
    words = re.findall(r'\b\w+\b', line.lower())
    word_list.extend(words)

print(word_list)

four_letter_word = []

for word in word_list:
    if len(word) == 4:
        four_letter_word.append(word)

print(four_letter_word)

Empty_dict = {}

for word in four_letter_word:
    if word not in Empty_dict:
        Empty_dict[word] = 1

    else:
        Empty_dict[word] += 1

# print(Empty_dict)

file= open("story 2", "a")

file.write("\nSummary of 4 letter words\n")
for i, j in Empty_dict.items():
    file.write(f"The word {i} occurred {j} times\n")