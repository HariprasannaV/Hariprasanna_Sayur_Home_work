"""
########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = #FillinMissingCode
for letter in myName:
    print(#FillinMissingCode)
"""
#getting name as input
myName = str(input("Enter Your Name: "))
# Looping through each letter in the myname
for letter in myName:
    print(myName[0:myName.index(letter)+1])

# for i in range(len(myName)):
#     for j in range(i + 1):
#         print(myName[j], end="")
#     print()

"""
output:
Enter Your Name: hari
h
ha
har
hari
"""