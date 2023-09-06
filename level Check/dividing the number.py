"""2.Get a number from the user. Divide it by 3 and print the result.
Divide again by 3 and print the result. Keep dividing until the number is less than 3.
Print the number of times the number was divided. """

number = int(input("Enter the number: "))  # getting a number from the user
# initiating time as 0
times = 0
divide_by_number = 3    # dividing number

while number >= divide_by_number:   # loop until the number is less than divide by number
    number = number/divide_by_number
    print(number)
    times = times+1  # incrementing the times
print("the number of times the number was divided", times)

"""
Output:
Enter the number: 16
5.333333333333333
1.7777777777777777
the number of times the number was divided 2
"""