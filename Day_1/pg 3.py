"""
you have a list of student names. you have one list each for their marks in CS, Math and English.
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or at least one A and the rest B.
Try to use only one if statement.
"""

# Hardcoded student names and their marks
students = ["Hari", "Raja", "Siva", "Ganesh", "Ram"]
marks_cs = [90, 80, 90, 40, 90]
marks_math = [80, 70, 90, 60, 80]
marks_english = [80, 90, 80, 40, 90]

# Pass mark
pass_mark = 50

# Iterate through students
for i in range(len(students)):
    # Check if all subjects have grade A or at least one A and the rest B
    if all(mark >= 90 for mark in [marks_cs[i], marks_math[i], marks_english[i]]) or any(mark >= 90 for mark in [marks_cs[i], marks_math[i], marks_english[i]]) and all(mark >= 80 for mark in [marks_cs[i], marks_math[i], marks_english[i]]):
        print(f"{students[i]} got A in all subjects or at least one A and the rest B.")

"""
Output:

Hari got A in all subjects or at least one A and the rest B.
Siva got A in all subjects or at least one A and the rest B.
Ram got A in all subjects or at least one A and the rest B.
"""