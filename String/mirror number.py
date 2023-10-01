"""
Accept 2 integers. print all nos which are mirror nos falling
between the range.
eg: first no 300
 second no 400
303,313,323.......393
"""

# Getting input from the user for the starting number
s = int(input("Enter the number here : "))
# Getting input from the user for the ending number
e = int(input("Enter the number here : "))
for i in range(s, e+1):
    if str(i) == str(i)[::-1]:
        print(i)
