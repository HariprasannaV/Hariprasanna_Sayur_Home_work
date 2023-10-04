"""
Problem 5:
Write a program to sort an array of numbers in ascending order. Use functions.
"""


def sorting():
    # initializing empty List
    integer_array = []
    # here getting input by splitting the numbers by spaces
    num_list = input("Enter the Array of Numbers here  : ").split()
    for i in num_list:
        integer_array.append(int(i))
    print(sorted(integer_array)) # here sorted function is used to sort the list in ascending order


sorting()
