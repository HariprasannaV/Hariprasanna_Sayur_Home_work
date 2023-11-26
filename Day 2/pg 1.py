"""
Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)
"""

# Get input number from the user
number = int(input("Enter the number: "))

# Outer loop to iterate from 1 to the input number
for i in range(1, number+1):
    # First inner loop to print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # Second inner loop to print increasing numbers, starting from 2
    for k in range(1, i):
        print(k+1, end="")

    # Move to the next line after printing each row
    print()

"""
Output:

Enter the number: 6
1
212
32123
4321234
543212345
65432123456

"""