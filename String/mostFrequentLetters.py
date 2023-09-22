"""
3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
"""

import re

sentence = input("Enter the string here: ")  # Get the input string from the user
output = re.findall(r'\w', sentence)

output_list = []
for char in output:     # changing sentence into lower case and inserting it into a list called output_list
    new_char = char.lower()
    output_list.append(new_char)
# print(output_list)

char_count_list = []
for char in output_list:  # To print letter and its count
    char_count = 0
    for element in output_list:
        # print("Element", element)
        if element == char:
            char_count += 1
    char = str(char) + str(char_count)
    char_count_list.append(char)
# print("char_count_list:", char_count_list)

# remove duplicated elements
unique_sorted_char_list = []
for element in char_count_list:
    if element not in unique_sorted_char_list:
        unique_sorted_char_list.append(element)
# print("unique_sorted_char_list:", unique_sorted_char_list)

# to rearrange the element in correct order
for i in range(len(unique_sorted_char_list)):
    for j in range(i, len(unique_sorted_char_list)):
        if unique_sorted_char_list[i][1] < unique_sorted_char_list[j][1]:
            unique_sorted_char_list[i], unique_sorted_char_list[j] = unique_sorted_char_list[j], unique_sorted_char_list[i]

        elif unique_sorted_char_list[i][1] == unique_sorted_char_list[j][1]:
            if unique_sorted_char_list[i][0] > unique_sorted_char_list[j][0]:
                unique_sorted_char_list[i], unique_sorted_char_list[j] = unique_sorted_char_list[j], unique_sorted_char_list[i]
    # print(unique_sorted_char_list)

# to print ordered elements
output_string = ""
for i in unique_sorted_char_list:
    output_string += i[0]

print(output_string)

"""
output:
Enter the string here: We Attack at Dawn
atwcdekn

"""