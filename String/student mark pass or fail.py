Student_name = ["Ganesha","murugan","siva","krishna","hari"]
marks = [90, 100, 40, 60, 75]
pass_students=[]
fail_student = 0
for i in range(len(marks)):
    if marks[i] >= 50:
         pass_students.append(Student_name[i] + str(marks[i]))
    else:
        fail_student += 1

print(f'The passed Student list {pass_students}')
