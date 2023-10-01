"""

Write a program for Collatz_conjecture.
# Collatz_conjecture means -  start with the input number.
# For even number , divide by 2 (n/2)
# For odd number - 3n + 1
# apply the above for the result number until the answer is 1

Here we are giving 2 numbers and comparing the number of iterations
"""


def hari(num, count):

    for n in num:
        c = 0  # we have initialized it as 0 since we need to find the count of both the numbers
        while n != 1:
            if n % 2 == 0:
                n = (n // 2)
            else:
                n = 3 * n + 1

            c += 1  # this iterates till that particular number becomes 1
        count.append(c)  # count stores the iteration counts of both the numbers

    minimum_count = min(count)  # checks which number has minimum iterations
    minimum_iterations = []
    for c in count:
        if c == minimum_count:
            position = count.index(c)
            minimum_iterations.append(num[position])
            count[position] = c + 1
        else:
            continue
    print(minimum_iterations)

    if len(minimum_iterations) == 1:
        print(f"The number {minimum_iterations[0]} has undergone minimum iterations {minimum_count} ")
    else:
        print("the numbers ", end="")
        for i in range(len(minimum_iterations)):
            print(minimum_iterations[i], end=" ")
        print(f'have undergone minimum iterations {minimum_count}')


# prints the number in the count index which has the minimum count with the minimum iterations


num = []
count = []
for i in range(2):  # range=2 so that 2 numbers can be inputted since index={0,1} will be considered
    n1 = int(input("Enter number: "))
    num.append(n1)  # append is used to join the number to the end of the list.. so here n1 is added to num
hari(num, count)

