"""

Get a input. Create a sequence of numbers from that input using the above alg.
Find the largest number in the sequence.
"""


def collatzConjecture(num):
    # Check if the input number is already 1, and if so, print it and exit
    if num == 1:
        print("please give another input")

    # Loop until the number becomes 1
    while num != 1:
        # If the number is even, divide it by 2
        if num % 2 == 0:
            num /= 2
            numList.append(int(num))
            print(int(num), end=" ")
        # If the number is odd, multiply it by 3 and add 1
        else:
            num = (3 * num) + 1
            numList.append(int(num))
            print(int(num), end=" ")


# Get the initial input number from the user
num = int(input("Enter the number: "))
# Empty list to store the numbers
numList = []
numList.append(int(num))
# Print the initial number
print(num, end=" ")
# Call the Collatz Conjecture function with the input number
collatzConjecture(num)

print(f'\n{numList}numList')
print(f'the largest number in the sequence {max(numList)}')