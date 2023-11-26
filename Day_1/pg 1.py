"""
Problem #1
Generate the following output using for loop. Go until g.
a
a-b-a
aba-c-aba
abacaba-d-abacaba
abacabadabacaba-e-abacabadabacaba


"""

alpha = ["a", "b", "c", "d", "e", "f", "g"]
newString = ""
for i in alpha:

    newString = newString + i + newString
    print(newString)

# import string
#
# alpha = []
# alphabet = string.ascii
# # _lowercase
# for letter in alphabet:
#     alpha.append(letter)
#     if letter == "g":
#         break
# print(alpha)

"""
Output:

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabawhile
"""

"""
ascii_lowercase: All lowercase letters from 'a' to 'z'.
ascii_uppercase: All uppercase letters from 'A' to 'Z'.
ascii_letters: All letters, both uppercase and lowercase.
digits: All numeric digits from '0' to '9'.
hexdigits: All hexadecimal digits (0-9, a-f, A-F).
octdigits: All octal digits (0-7).
punctuation: All ASCII punctuation characters.
printable: All printable ASCII characters."""

