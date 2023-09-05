"""
######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines
"""
num = int(input("Enter the number: "))

for i in range(-num, num):
    if i <= 0:
        l = -i
    else:
        l = i
    for space in range(0, l):
        print(" ",end="")
    for symbol in range(0,num-l):
        print("$",end=" ")
    nxt_line = input()

    if nxt_line != " ":
        break;
    # print()


