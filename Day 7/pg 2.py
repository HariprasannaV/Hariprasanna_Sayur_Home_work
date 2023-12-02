"""

Problem 2:
  In the input, find the first A and last A, print all the letters between these two A.
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B.
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.
"""


def findingAandBandC(sentence):  # Define a function named findingAandBandC
    # Loop through each letter in the list 'letter'
    for n in letter:
        # Find the index of the first occurrence of the letter 'n' in the sentence
        first_letter = sentence.lower().find(n)

        # Check if the letter 'n' was found in the sentence
        if first_letter >= 0:
            # Find the index of the last occurrence of the letter 'n' in the sentence
            last_letter = sentence.lower().rfind(n)

            # Check if there is only one occurrence of the letter 'n'
            if last_letter == first_letter:
                print(f"There is only one {n}")
            else:
                # Print the substring of the sentence between the first and last occurrence of 'n'
                print(sentence[first_letter + 1:last_letter])
                break  # Exit the loop once the first occurrence is found
        else:
            # Print a message indicating that the letter 'n' was not found in the sentence
            print(f"There is No {n}")


# Define a list of letters to search for in the sentence
letter = ["a", "b", "c"]

# enter a sentence
Sentence = str(input("Enter the statement: "))

# Call the function to find occurrences of 'a', 'b', and 'c' in the sentence
findingAandBandC(Sentence)
