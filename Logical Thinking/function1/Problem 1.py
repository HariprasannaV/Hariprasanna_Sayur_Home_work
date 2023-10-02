"""
Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams.
"""


# this is the function definition for calculating average
def avg_calculation():
    sum_of_marks = cs_mark[0] + cs_mark[1] + cs_mark[2]
    avg = sum_of_marks/3
    print(f'your avg marks in CS subject in the last 3 exams is  {avg}')


cs_mark = []  # initializing empty list

# this for loop used to looping for getting marks
for sub in range(3):
    mark = float(input(f"Enter CS Subject mark {sub+1} : "))  # getting marks as input
    cs_mark.append(mark)  # adding marks to cs_mark list

avg_calculation()  # calling the function

"""
Output:

Enter CS Subject mark 1 : 98
Enter CS Subject mark 2 : 98
Enter CS Subject mark 3 : 100
your avg marks in CS subject in the last 3 exams is  98.66666666666667

"""