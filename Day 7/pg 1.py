"""
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
"""


# Define a function named printingLettersBetweenA
def printingLettersBetweenA(sentence):
    # Find the index of the first occurrence of 'a' in the sentence
    first_A = sentence.lower().find("a")

    # Find the index of the last occurrence of 'a' in the sentence
    last_A = sentence.lower().rfind('a')
    # print(first_A,last_A)

    # Check if 'a' was not found in the sentence
    if first_A == -1:
        return "There is no 'A'"
    # Check if there is only one occurrence of 'a' in the sentence
    elif first_A == last_A:
        return "There is only one 'A'"
    else:
        # Print the substring of the sentence between the first and last occurrence of 'a'

        return sentence[first_A + 1:last_A]


# Prompt the user to enter a sentence and convert it to lowercase
Sentence = str(input("Enter the statement: "))

# Call the function to find and print letters between the first and last 'a' in the sentence
print(printingLettersBetweenA(Sentence))
