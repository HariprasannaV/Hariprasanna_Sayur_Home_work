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


def collatzConjecture(num):
    if num == 1:
        print(int(num))

    while num != 1:

        if num % 2 == 0:
            num /= 2
            print(int(num),end=" ")
        else:
            num = (3 * num) + 1
            print(int(num),end=" ")


num = int(input("Enter the number: "))
print(num,end=" ")
collatzConjecture(num)