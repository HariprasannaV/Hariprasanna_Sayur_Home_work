"""
Problem #2
Read a passage from a file.
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servant. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
"""
try:
    # Import the regular expression module
    import re

    # Open the file in read mode
    file = open("story", "r")

    # List to store words from each line
    word_list = []

    # Iterate through each line in the file
    for line in file:
        print(line)

        # Use regular expression to find words, convert to lowercase
        words = re.findall(r'\b\w+\b', line.lower())

        # Add the words to the word_list
        word_list.extend(words)

    # Initialize count for occurrences
    count = 0

    # Iterate through the list of words
    for i in range(len(word_list)):
        if word_list[i] == "the":
            # Iterate from the next word to find occurrences until "a" is encountered
            for j in range(i + 1, len(word_list)):
                if word_list[j] == "a":
                    break
                elif word_list[j] == "the":
                    count += 1
                    break

    # Print the total occurrence count
    print(f'The total occurrence {count}')

except Exception as e:
    # Handle any exceptions that may occur
    print(f"An error occurred: {e}")
