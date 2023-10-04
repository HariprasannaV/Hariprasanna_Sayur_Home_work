"""
Problem 5:
Write a program to sort an array of numbers in ascending order. Use functions.
"""


def sorting():
    integer_array = []
    num_list = input("Enter the Array of Numbers here  : ").split()
    for i in num_list:
        integer_array.append(int(i))
    print(sorted(integer_array))


sorting()
