"""

Problem 1
Print the following pattern
Problem 1
Print the following pattern
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

"""


# Function to calculate factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Get the number of rows from the user
row = int(input("Enter the number of rows: "))

# Outer loop to iterate through each row
for i in range(row):
    # Print to give spaces 
    for j in range(row - i):
        print(" ", end="")

    # Inner loop to calculate and print the values in each row
    for j in range(i + 1):
        # Use the binomial coefficient formula to calculate the value
        coefficient = int(factorial(i) / (factorial(i - j) * factorial(j)))

        print(coefficient, end=" ")

    # Move to the next line after printing each row
    print()
