"""
3.Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal.
    Eg - input - cat, arrow. (length is not equal)
    Output - cataa, arrow (length is equal by adding a)
"""


# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Equalize the names
while len(name1) < len(name2):
    name1 += 'a'
while len(name2) < len(name1):
    name2 += 'a'

# Print the equal names
print("Equal names:")
print(name1)
print(name2)

"""
Output:
Enter the first name: cat
Enter the second name: arrow
Equal names:
cataa
arrow
"""