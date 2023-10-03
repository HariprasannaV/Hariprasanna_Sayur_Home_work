"""
Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the last 3 exams.
"""

num_of_students = int(input("Enter the No. of student in Your class : "))


# this is the function definition for calculating average
def avg_calculation():
    for i in range(num_of_students):
        sum_of_marks = cs_mark[i][0] + cs_mark[i][1] + cs_mark[i][2]
        avg = sum_of_marks/3
        print(f'The average marks of Student {i+1} in CS subject in the last 3 exams is  {round(avg,3)}.')


cs_mark = []

# this for loop used to looping for getting marks
for i in range(num_of_students):
    student_list = []
    for sub in range(3):

        mark = float(input(f"Enter CS Subject mark {sub + 1} of Student {i+1} : "))  # getting marks as input
        student_list.append(mark)  # adding marks to cs_mark list
    cs_mark.append(student_list)

print()
avg_calculation()  # calling the function
