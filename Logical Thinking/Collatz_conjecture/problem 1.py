"""Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number.
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.

Eg, input is 8
8, 4,2, 1
input is 9
9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1"""

# Define a function to perform the Collatz Conjecture
def collatzConjecture(num):
    # Check if the input number is already 1, and if so, print it and exit
    if num == 1:
        print(int(num))

    # Loop until the number becomes 1
    while num != 1:
        # If the number is even, divide it by 2
        if num % 2 == 0:
            num /= 2
            print(int(num), end=" ")
        # If the number is odd, multiply it by 3 and add 1
        else:
            num = (3 * num) + 1
            print(int(num), end=" ")

# Get the initial input number from the user
num = int(input("Enter the number: "))
# Print the initial number
print(num, end=" ")
# Call the Collatz Conjecture function with the input number
collatzConjecture(num)
