"""

Problem 3:
  In the input, find the first A and last A, print all the letters between these two A.
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B.

  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C.

"""


# Define a function named findLetter
def findLetter():
    # Prompt the user to enter a sentence and convert it to lowercase
    sentence = str(input("Enter the statement: ")).lower()

    # Loop through each letter in the list 'letter'
    for n in letter:

        # Find the index of the first occurrence of the letter 'n' in the sentence
        first_letter_index = sentence.find(n)
        # print(f'{n} {first_letter_index}')

        # Check if the letter 'n' was found in the sentence
        if first_letter_index >= 0:
            # Find the index of the last occurrence of the letter 'n' in the sentence
            last_letter_index = sentence.rfind(n)

            # Check if there is only one occurrence of the letter 'n'
            if last_letter_index == first_letter_index:
                print(f"There is only one {n}")

                # Update the sentence to start from the next character after the first occurrence
                sentence = sentence[first_letter_index + 1:]

                # Continue to the next letter in the list
                continue
            else:
                # Print the substring of the sentence between the first and last occurrence of 'n'
                print(sentence[first_letter_index + 1:last_letter_index])

                # Exit the loop once the first occurrence is found
                break

        else:
            # Print a message indicating that the letter 'n' was not found in the sentence
            print(f"There is No {n}")


# Define a list of letters to search for in the sentence
letter = ["a", "b", "c"]

# Call the function to find occurrences of 'a', 'b', and 'c' in the sentence
findLetter()
