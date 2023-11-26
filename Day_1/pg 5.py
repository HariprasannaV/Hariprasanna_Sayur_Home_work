"""
In your college Python is taught in 3 different departments by the same professor.
For each dept, get the no of students studying Python and their marks in the final exam
Get the input as comma separated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.
"""
total_classes = 3

all_top_marks_per_class = []
all_marks = []

pass_mark = 50
failed_students_per_class = []

for i in range(total_classes):
    failed_students = 0
    ip_no_of_students = int(input(f"Enter the Total number of students in Class {i+1} : "))
    ip_mark_list_str = (input(f"Enter the marks for all the students in the class {i+1} (separated by comma) : ")).split(",")

    if (ip_no_of_students != len(ip_mark_list_str)) or (ip_no_of_students < 3):
        break

    # Converting the marks in the list into integer type
    mark_list = []
    mark_list_copy = []
    for mark in ip_mark_list_str:
        if int(mark) >= pass_mark:
            mark_list_copy.append(int(mark))
        else:
            failed_students += 1
        mark_list.append(int(mark))
    failed_students_per_class.append(failed_students)

    all_marks.append(mark_list_copy)

    print(f"The top three marks in the Class {i + 1} are ", end="")
    # Top 3 marks in the i-th Class
    top_3_marks_in_the_class = []
    for j in range(3):
        maximum_mark = max(mark_list)
        top_3_marks_in_the_class.append(maximum_mark)
        mark_list.remove(maximum_mark)  # Removing the maximum mark to avoid adding the same value in the list
        print(maximum_mark, end=" ")
    print("\n")

    all_top_marks_per_class.append(top_3_marks_in_the_class)

all_top_marks = []
for class_i in all_top_marks_per_class:
    for mark in class_i:
        all_top_marks.append(mark)

top_3_marks = []
for i in range(3):
    top_3_marks.append(max(all_top_marks))
    all_top_marks.remove(max(all_top_marks))

print(f"\nThe Top 3 Marks in the {total_classes} class(es) are ", end=" ")
for mark in top_3_marks:
    print(mark, end=" ")
print("\n\n")

all_marks_for_all_classes = []
avg_marks_for_all_classes = []
for i in range(len(all_marks)):
    sum_ = 0
    for mark in all_marks[i]:
        all_marks_for_all_classes.append(mark)
        sum_ += mark
    avg = sum_/len(all_marks[i])
    print(f"The Average Mark of Passed Students of Class {i+1} is {avg}")
    avg_marks_for_all_classes.append(avg)


overall_mark = 0
for mark in all_marks_for_all_classes:
    overall_mark += mark
print(f"\nThe Average Mark of All {total_classes} class(es) is {overall_mark/len(all_marks_for_all_classes)}")

position_of_best_class_with_high_avg = avg_marks_for_all_classes.index(max(avg_marks_for_all_classes))
print(f"The Class with Best Average is Class {position_of_best_class_with_high_avg+1}")

position_of_best_class_with_low_fail_students = failed_students_per_class.index(min(failed_students_per_class))
print(f"The Class with Least Number of Failed Students is Class {position_of_best_class_with_low_fail_students+1}")

"""
Output:


Enter the Total number of students in Class 1 : 4
Enter the marks for all the students in the class 1 (separated by comma) : 90, 80, 70, 40
The top three marks in the Class 1 are 90 80 70 

Enter the Total number of students in Class 2 : 5
Enter the marks for all the students in the class 2 (separated by comma) : 90, 80, 70, 50, 40
The top three marks in the Class 2 are 90 80 70 

Enter the Total number of students in Class 3 : 6
Enter the marks for all the students in the class 3 (separated by comma) : 99, 30, 100, 45, 67, 34
The top three marks in the Class 3 are 100 99 67 


The Top 3 Marks in the 3 class(es) are  100 99 90 


The Average Mark of Passed Students of Class 1 is 80.0
The Average Mark of Passed Students of Class 2 is 72.5
The Average Mark of Passed Students of Class 3 is 88.66666666666667

The Average Mark of All 3 class(es) is 79.6
The Class with Best Average is Class 3
The Class with Least Number of Failed Students is Class 1
"""