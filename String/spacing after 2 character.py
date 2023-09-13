"""
########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = #FillinMissingCode
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    newString += #FillinMissingCode (assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2
#check to add the chars at the end
#FillinMissingCode

print (newString)
"""

inputString = str(input("Enter the String: "))
i = 0    # counter to track the chars
newString = ""
while i < len(inputString):
    newString += inputString[i:i+2]             # this line shows i is starting and i+2  is ending character
    if i + 3 <= len(inputString):
        newString += " "   # add space
    i += 2
# check to add the chars at the end
# Fill in MissingCode
#newString += inputString[i:]
print(newString)

"""
Output:
Enter the String: Hariprasanna
Ha ri pr as an na

"""