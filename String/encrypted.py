"""
Input is an encrypted  string where there will be chars followed by number. The way to decrypt is
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd.
 ac2acc#cd3 acaccdcdcd
"""

import re

# Get the encrypted input from the user
s = input("Enter the encrypted form here : ")
# Initialize an empty string
decrypted = ''
# Find all matches of the pattern in the string
matches = re.findall(r'([a-z]+)(\d+)', s)
# print(matches)

for match in matches:
    # repeat the characters by the number of times and add to the decrypted string
    # print(match[0])
    # print(int(match[1]))
    decrypted += match[0] * int(match[1])

print('Decrypted word:', decrypted)  # Print the decrypted word
print('Length:', len(decrypted)) # Print the length of the decrypted word

"""
Output:
Enter the encrypted form here : ab2bb#cd3
Decrypted word: ababcdcdcd
Length: 10
"""