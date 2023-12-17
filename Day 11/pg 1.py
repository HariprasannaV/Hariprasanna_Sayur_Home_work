"""
Problem #1
1. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.' etc.)

Write all constraints.
Get an input as string. Return if it is valid or not.
Use string functions.
"""

import string


def IPv4():
    symbol = "!\"#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"
    if ("." in ip_address_string) and all(x not in string.ascii_letters for x in ip_address_string) and all(x not in symbol for x in ip_address_string) and ((" " or "..") not in ip_address_string) :
        dot_count = 0

        for i in ip_address_string:
            if i == ".":
                dot_count += 1

        if dot_count == 3:
            num_list = ip_address_string.split(".")

            number = [int(x) for x in num_list if 0 <= int(x) <= 255]
            if (len(number) == 4) and (len(ip_address_string) <= 15):
                return "Valid"

            else:
                return "Invalid"

        else:
            return "Invalid"

    else:
        return "Invalid"


ip_address_string = str(input("Enter the ip address: "))
print(f'{ip_address_string} is {IPv4()}')

"""
ascii_lowercase: All lowercase letters from 'a' to 'z'.
ascii_uppercase: All uppercase letters from 'A' to 'Z'.
ascii_letters: All letters, both uppercase and lowercase.
digits: All numeric digits from '0' to '9'.
hexdigits: All hexadecimal digits (0-9, a-f, A-F).
octdigits: All octal digits (0-7).
punctuation: All ASCII punctuation characters.
printable: All printable ASCII characters."""

# for i in string.punctuation:
#     print(i,end=" ")
#
# print(string.punctuation)