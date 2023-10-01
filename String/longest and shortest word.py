"""
2. From a given passage find the longest and shortest word
and print the same. Accept the passage as an input from user
"""

sentence = input("Enter the sentence here : ")
lower_case_word_list = []
symbols = ['.', ',', '<', '>', '/', '?', ';', ':', '"', "'", '[', ']', '{', '}', '|', '~', '`', '!', '@', '#', '$', '%',
           '^', '&', '*', '(', ')', '_', '-', '+', '=']

# Removing the symbols from the input sentence
for chr in sentence:
    for i in range(len(symbols)):
        if chr == symbols[i]:
            sentence = sentence.replace(chr, "")

# Converting all the characters of the sentence into lowercase letters
lower_case_word_list = (sentence.lower()).split()

# Removing the duplicated words from the list "lower_case_word_list"
duplication_removed_words = []
for word in lower_case_word_list:
    if word not in duplication_removed_words:
        duplication_removed_words.append(word)

# Storing the lengths of all the strings of the list "duplication_removed_words" in another list
len_of_dup_removed_words = []
for word in duplication_removed_words:
    len_of_dup_removed_words.append(len(word))
# print(duplication_removed_words)
# print(len_of_dup_removed_words)

# Checking for the highest number (length of the strings) in the list
highest_len = 0
for length_value in len_of_dup_removed_words:
    if length_value > highest_len:
        highest_len = length_value
# print(highest_len)

# Checking for the Position of the longest word and storing the first longest word in a variable
position_of_longest_word = len_of_dup_removed_words.index(highest_len)
longest_word = duplication_removed_words[position_of_longest_word]

# Checking for the smallest number (length of the strings) in the list
smallest_len = highest_len
for length_value in len_of_dup_removed_words:
    if length_value < smallest_len:
        smallest_len = length_value
# print(smallest_len)

# Checking for the Position of the shortest word and storing the first shortest word in a variable
position_of_shortest_word = len_of_dup_removed_words.index(smallest_len)
shortest_word = duplication_removed_words[position_of_shortest_word]

# Printing the first longest and first shortest word
print(f"Longest word : {longest_word}")
print(f"Shortest word: {shortest_word}")
