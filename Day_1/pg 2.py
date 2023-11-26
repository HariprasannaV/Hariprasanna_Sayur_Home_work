"""
Problem #2
you have a list of student names and another list with their marks in CS.
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
"""

studentName = ["hari", "raja", "siva", "ganesh", "ram"]
studentMark_in_CS = [90, 40, 70, 60, 49]

failed_student_count = 0

passMark = 50

print("Passed Students:")
for i in range(len(studentName)):
    # print(i)
    if studentMark_in_CS[i] >= passMark:
        print(f'{studentName[i]} : {studentMark_in_CS[i]}')
    else:
        failed_student_count += 1

print("\nFailed Student Count", failed_student_count)

"""
Output:

Passed Students:
hari : 90
siva : 70
ganesh : 60

Failed Student Count 2
"""
